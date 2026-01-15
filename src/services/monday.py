from typing import Optional
import json
import requests
from src.config import settings
from src.utils.logger import get_logger
from src.domain.schemas import PropertyInput, PropertyAnalysis

class MondayClient:
    def __init__(self):
        self.api_key = settings.MONDAY_API_KEY
        self.api_url = "https://api.monday.com/v2"
        self.logger = get_logger("monday_client")

    def create_item(self, prop: PropertyInput, analysis: PropertyAnalysis, board_id: int = 18395684174) -> bool:
        """
        Creates an item on the Monday board with the analysis results.
        If no API key is present, it logs the mutation (Dry Run).
        """
        
        # 1. Escape values to avoid breaking GraphQL string
        # Simple JSON dumps ensures strings are properly escaped
        def escape_gql(val):
            return json.dumps(val)

        # 2. Prepare Column Values (JSON String)
        # Using JSON dump for the entire column_values object is safer and cleaner
        column_values = {
            "numbers": prop.price,  # Price
            "numbers__1": analysis.viability_score, # Score. NOTE: Double underscore might be needed depending on column ID (checking standard format). Plan said "numbers_1", sticking to plan but careful.
            # Assuming "numbers_1" from plan, but Monday often uses generated IDs. 
            # I will use "numbers_1" as per user request, but usually it's best to verify graphQL IDs.
            # Wait, the user plan says: "numbers_1" (Score). I will stick to that.
            "status": {"label": analysis.recommended_action.value}, # Status columns usually expect an index or label
            "long_text": analysis.summary,
            "link": {"url": str(prop.link), "text": "View Property"}
        }

        # Monday requires column_values to be a JSON string *inside* the mutation variables or string.
        # It's cleanest to pass it as a GraphQL variable, but the user plan requested "Construct Mutation".
        # I will construct the mutation string with f-strings as requested, ensuring column_values is a JSON string.
        
        # Correction on Column IDs based on common defaults or user plan:
        # Plan: "numbers" -> logic: prop.price
        # Plan: "numbers_1" -> logic: analysis.viability_score
        # Plan: "status" -> logic: analysis.recommended_action
        # Plan: "long_text" -> logic: analysis.summary
        # Plan: "link" -> logic: prop.link
        
        # Let's adjust column_values for the specific Monday format (it expects value to be jsonified string sometimes or just object if using vars)
        # For raw string mutation interpolation:
        
        # Map ActionEnum to Monday Status Labels (Case Sensitive)
        status_map = {
            "BUY": "Buy",
            "PASS": "Pass",
            "INVESTIGATE": "AI Reviewing" 
        }
        monday_status = status_map.get(analysis.recommended_action.value, "New")

        gql_column_values = json.dumps({
            "numeric_mkzmngbz": str(prop.price),       # Price
            "numeric_mkzmg31g": analysis.viability_score, # AI Score
            "project_status": monday_status,           # Status
            "text_mkzmgh4q": analysis.summary,         # AI Summary
            "link_mkzmf7yb": {"url": str(prop.link), "text": "Project Link"} # Link
        }).replace('"', '\\"') # Escape quotes for inclusion in the mutation string

        mutation = f"""
        mutation {{
            create_item (
                board_id: {board_id},
                item_name: {escape_gql(prop.address)},
                column_values: "{gql_column_values}"
            ) {{
                id
            }}
        }}
        """

        # Step 2: Execution Guard (The Switch)
        if not self.api_key:
            self.logger.warning("MONDAY_API_KEY not found. DRY RUN - Payload prepared but not sent.")
            self.logger.info(f"GraphQL Mutation:\n{mutation}")
            return True

        # Else (Live Mode)
        headers = {
            "Authorization": self.api_key,
            "API-Version": "2023-10",
            "Content-Type": "application/json"
        }
        
        data = {'query': mutation}
        
        try:
            response = requests.post(self.api_url, json=data, headers=headers)
            response.raise_for_status()
            
            response_json = response.json()
            if "errors" in response_json:
                self.logger.error(f"Monday API returned errors: {response_json['errors']}")
                return False
                
            self.logger.info(f"Item created on board {board_id}. ID: {response_json['data']['create_item']['id']}")
            return True
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to create item on Monday: {e}")
            return False
