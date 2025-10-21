from typing import Optional, List, Dict, Any
from azure.cosmos import exceptions
from fastapi import HTTPException
from app.repository.company_repository import CompanyRepository

class CompanyService:
    def __init__(self, repo: CompanyRepository | None = None):
        self.repo = repo or CompanyRepository()

    def create_company(self, data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            return self.repo.create(data)
        except exceptions.CosmosHttpResponseError as e:
            if e.status_code == 409:
                raise HTTPException(status_code=409, detail=f"Company with name '{data.get('name')}' already exists")
            raise HTTPException(status_code=500, detail="Internal server error")

    def get_company(self, id: str, pk: str):
        return self.repo.get(id, pk)

    def update_company(self, id: str, pk: str, data: Dict[str, Any]):
        return self.repo.update(id, pk, data)

    def delete_company(self, id: str, pk: str) -> bool:
        return self.repo.delete(id, pk)

    def search_by_name_prefix(self, prefix: str, limit: int = 20):
        return self.repo.search_by_name_prefix(prefix, limit)

    def validate_name_exists(self, name: str) -> Dict[str, Any]:
        hit = self.repo.find_by_name_exact(name)
        return {
            "query": name,
            "exists": hit is not None,
            "match": {"id": hit.get("id"), "name": hit.get("name")} if hit else None
        }

    def find_by_keys(self, **kwargs):
        return self.repo.find_by_keys(**kwargs)
