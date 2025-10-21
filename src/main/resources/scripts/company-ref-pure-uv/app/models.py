from pydantic import BaseModel, Field, HttpUrl, field_validator
from typing import Optional, List
from datetime import date

class OwnershipBlock(BaseModel):
    holder_name: str
    holder_type: Optional[str] = Field(
        default=None, description="e.g., Institutional, Insider, Strategic"
    )
    percent: Optional[float] = Field(default=None, ge=0, le=100)

class AntiTakeoverProfile(BaseModel):
    poison_pill: bool = False
    staggered_board: bool = False
    supermajority_required: bool = False
    golden_parachute: bool = False
    dual_class_shares: bool = False
    notes: Optional[str] = None

class CompanyCreate(BaseModel):
    name: str = Field(..., min_length=1)
    ticker: Optional[str] = Field(None, description="e.g., AAPL")
    isin: Optional[str] = Field(None)
    lei: Optional[str] = Field(None, description="Legal Entity Identifier")
    country: Optional[str] = None
    jurisdiction_of_incorporation: Optional[str] = None
    industry: Optional[str] = None
    sector: Optional[str] = None
    exchange: Optional[str] = None
    website: Optional[HttpUrl] = None

    market_cap_usd: Optional[float] = None
    enterprise_value_usd: Optional[float] = None
    shares_outstanding: Optional[float] = None
    free_float_percent: Optional[float] = Field(None, ge=0, le=100)

    major_shareholders: Optional[List[OwnershipBlock]] = None
    anti_takeover: Optional[AntiTakeoverProfile] = AntiTakeoverProfile()

    board_members: Optional[List[str]] = None
    ceo: Optional[str] = None
    founded: Optional[date] = None
    notes: Optional[str] = None

    @field_validator("ticker", mode="before")
    @classmethod
    def norm_ticker(cls, v):
        return v.upper() if isinstance(v, str) else v

class CompanyUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1)
    ticker: Optional[str] = None
    isin: Optional[str] = None
    lei: Optional[str] = None
    country: Optional[str] = None
    sector: Optional[str] = None
    website: Optional[HttpUrl] = None
    listing_date: Optional[date] = None
    anti_takeover: Optional[AntiTakeoverProfile] = None
    anti_takeover_provisions: Optional[List[str]] = Field(default=None, description="List of anti-takeover provisions")
    ceo: Optional[str] = None
    board_members: Optional[List[str]] = None
    ownership: Optional[List[OwnershipBlock]] = None
    notes: Optional[str] = None

class Company(CompanyCreate):
    id: str
    pk: str
    name_lower: str
