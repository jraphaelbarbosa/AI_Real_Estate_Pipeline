from decimal import Decimal
from typing import List, Union
from enum import Enum
from pydantic import BaseModel, HttpUrl, Field

class PropertyInput(BaseModel):
    property_id: str
    address: str
    price: Decimal
    raw_description: str
    link: Union[HttpUrl, str]

class ActionEnum(str, Enum):
    BUY = "BUY"
    PASS = "PASS"
    INVESTIGATE = "INVESTIGATE"

class PropertyAnalysis(BaseModel):
    viability_score: int = Field(..., ge=0, le=100, description="Score from 0-100")
    summary: str = Field(..., description="Executive summary, max 2 sentences")
    risk_factors: List[str]
    recommended_action: ActionEnum
    arv: Decimal = Field(..., description="After Repair Value")
    renovation_cost: Decimal = Field(..., description="Estimated Renovation Cost")
