import sys
from pathlib import Path
import json

# Add project root to sys.path
sys.path.append(str(Path(__file__).parent.parent))

from src.services.ingestor import JsonFileIngestor
import logging

def test_ingestion():
    print(">>> 1. Testing Normal Ingestion")
    ingestor = JsonFileIngestor("data/raw_mock_data.json")
    properties = ingestor.load_properties()
    
    print(f"Loaded {len(properties)} properties.")
    for p in properties:
        print(f" - {p.property_id}: {p.price} ({type(p.price)})")

    assert len(properties) == 3
    assert properties[0].property_id == "PROP-001"
    
    print("\n>>> 2. Testing Missing File")
    ingestor_missing = JsonFileIngestor("data/non_existent.json")
    properties_missing = ingestor_missing.load_properties()
    print(f"Loaded {len(properties_missing)} properties from missing file.")
    assert len(properties_missing) == 0

    print("\n>>> 3. Testing Fault Tolerance (Malformed Data)")
    # Create temporary malformed file
    malformed_path = Path("data/malformed_mock.json")
    malformed_data = [
        {
            "property_id": "PROP-VALID", 
            "address": "Valid St", 
            "price": 100000, 
            "raw_description": "Desc", 
            "link": "http://valid.com"
        },
        {
            "property_id": "PROP-INVALID",
            # Missing mandatory 'address' field
            "price": "NOT_A_NUMBER", 
             "raw_description": "Desc", 
             "link": "http://invalid.com"
        }
    ]
    with open(malformed_path, "w") as f:
        json.dump(malformed_data, f)
        
    try:
        ingestor_malformed = JsonFileIngestor(str(malformed_path))
        properties_malformed = ingestor_malformed.load_properties()
        
        print(f"Loaded {len(properties_malformed)} properties from malformed file.")
        assert len(properties_malformed) == 1
        assert properties_malformed[0].property_id == "PROP-VALID"
        print("Fault tolerance verification passed!")
        
    finally:
        if malformed_path.exists():
            malformed_path.unlink()

if __name__ == "__main__":
    test_ingestion()
