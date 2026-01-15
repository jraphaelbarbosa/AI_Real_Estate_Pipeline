from abc import ABC, abstractmethod
from typing import List

from src.domain.schemas import PropertyInput

class DataIngestor(ABC):
    """
    Abstract Interface for Data Ingestion.
    Adheres to Open/Closed Principle - new sources can be added by extending this class.
    """
    
    @abstractmethod
    def load_properties(self) -> List[PropertyInput]:
        """
        Abstract method to load property data.
        Must return a list of PropertyInput objects.
        """
        pass
