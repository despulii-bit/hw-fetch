from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, Field, HttpUrl


class ComponentCategory(str, Enum):
    CPU = "cpu"
    GPU = "gpu"
    MOTHERBOARD = "motherboard"
    RAM = "ram"
    STORAGE = "storage"
    PSU = "psu"


class HardwareSpecification(BaseModel):
    """
    The gold standard for a single hardware component's data.
    """

    brand: str = Field(
        ..., description="The manufacturer, e.g., NVIDIA, AMD, Intel, ASUS"
    )
    model_name: str = Field(
        ..., description="The full commercial name, e.g., GeForce RTX 4090"
    )
    model_number: Optional[str] = Field(
        None, description="The specific SKU or MPN if available"
    )
    category: ComponentCategory = Field(
        ..., description="The type of hardware component"
    )

    # The 'Brain' of the spec sheet
    specs: Dict[str, str] = Field(
        ...,
        description="A dictionary of technical specifications (e.g., {'Clock Speed': '3.5GHz', 'VRAM': '24GB'})",
    )

    # Metadata for verification
    source_url: HttpUrl = Field(
        ..., description="The exact URL where this data was scraped"
    )
    raw_summary: Optional[str] = Field(
        None, description="A brief AI-generated summary of the product features"
    )
    tags: List[str] = Field(
        default_factory=list,
        description="Keywords like 'Gaming', 'Workstation', 'Low-profile'",
    )

    class Config:
        # This ensures the LLM doesn't try to hallucinate extra random fields
        extra = "forbid"
