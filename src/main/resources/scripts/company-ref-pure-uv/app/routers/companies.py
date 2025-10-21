from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
from app.models import CompanyCreate, CompanyUpdate, Company
from app.services.company_service import CompanyService

router = APIRouter(prefix="/companies", tags=["companies"])
svc = CompanyService()

@router.post("", response_model=Company, status_code=201)
def create_company(payload: CompanyCreate):
    created = svc.create_company(payload.model_dump())
    return created

@router.get("/{pk}/{id}", response_model=Company)
def get_company(pk: str, id: str):
    item = svc.get_company(id, pk)
    if not item:
        raise HTTPException(status_code=404, detail="Company not found")
    return item

@router.put("/{pk}/{id}", response_model=Company)
def update_company(pk: str, id: str, payload: CompanyUpdate):
    updated = svc.update_company(id, pk, payload.model_dump())
    if not updated:
        raise HTTPException(status_code=404, detail="Company not found")
    return updated

@router.delete("/{pk}/{id}", status_code=204)
def delete_company(pk: str, id: str):
    ok = svc.delete_company(id, pk)
    if not ok:
        raise HTTPException(status_code=404, detail="Company not found")
    return

@router.get("/search", response_model=List[dict])
def search(prefix: str = Query(..., min_length=1), limit: int = 20):
    return svc.search_by_name_prefix(prefix, limit)

@router.get("/validate")
def validate(name: str = Query(..., min_length=1)):
    return svc.validate_name_exists(name)

@router.get("/lookup")
def lookup(ticker: Optional[str] = None, isin: Optional[str] = None, lei: Optional[str] = None):
    if not any([ticker, isin, lei]):
        return []
    return svc.find_by_keys(ticker=ticker, isin=isin, lei=lei)
