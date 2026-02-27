from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, Field, HttpUrl


class ComponentCategory(str, Enum):
    CPU = "cpu"
    GPU = "gpu"
    HBA = "hba"
    MOTHERBOARD = "motherboard"
    RAM = "ram"
    STORAGE = "storage"
    PSU = "psu"
    OTHER = "other"


class HardwareSpecification(BaseModel):
    """
    The 'Bouncer' schema for the Autonomous Data Intelligence Scraper.
    """

    brand: str = Field(..., description="The manufacturer, e.g., NVIDIA, ASUS")
    model_name: str = Field(..., description="Full name, e.g., GeForce RTX 4090")
    model_number: Optional[str] = Field(None, description="The specific SKU or MPN")
    category: ComponentCategory = Field(
        ..., description="The type of hardware component"
    )

    specs: Dict[str, str] = Field(
        ..., description="Technical specifications (e.g., {'Clock Speed': '3.5GHz'})"
    )

    content_hash: str = Field(..., description="SHA-256 hash of the source markdown")

    source_url: HttpUrl = Field(..., description="The exact URL where this was scraped")
    raw_summary: Optional[str] = Field(None, description="Brief AI-generated summary")
    tags: List[str] = Field(default_factory=list)

    class Config:
        extra = "forbid"
        str_strip_whitespace = True
