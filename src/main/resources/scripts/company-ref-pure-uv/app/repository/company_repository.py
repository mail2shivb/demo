import uuid
from typing import Optional, List, Dict, Any
from azure.cosmos import exceptions
from app.db import get_container
from app.utils import normalize_name, derive_pk_from_name, non_empty

class CompanyRepository:
    def __init__(self):
        self._container = None

    @property
    def container(self):
        if self._container is None:
            self._container = get_container()
        return self._container

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        data = data.copy()
        data["id"] = data.get("id") or str(uuid.uuid4())
        data["name_lower"] = normalize_name(data["name"])
        data["pk"] = derive_pk_from_name(data["name"])
        if non_empty(data.get("ticker")):
            data["ticker"] = data["ticker"].upper()
        try:
            return self.container.create_item(body=data)
        except exceptions.CosmosHttpResponseError as e:
            raise e

    def get(self, id: str, pk: str) -> Optional[Dict[str, Any]]:
        try:
            return self.container.read_item(item=id, partition_key=pk)
        except exceptions.CosmosResourceNotFoundError:
            return None

    def update(self, id: str, pk: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        existing = self.get(id, pk)
        if not existing:
            return None
        for k, v in data.items():
            existing[k] = v
        if "name" in data and non_empty(data["name"]):
            existing["name_lower"] = normalize_name(existing["name"])
            existing["pk"] = derive_pk_from_name(existing["name"])
        if non_empty(existing.get("ticker")):
            existing["ticker"] = existing["ticker"].upper()
        return self.container.replace_item(item=existing["id"], body=existing)

    def delete(self, id: str, pk: str) -> bool:
        try:
            self.container.delete_item(item=id, partition_key=pk)
            return True
        except exceptions.CosmosResourceNotFoundError:
            return False

    def find_by_name_exact(self, name: str) -> Optional[Dict[str, Any]]:
        nl = normalize_name(name)
        query = "SELECT * FROM c WHERE c.name_lower = @nl"
        items = list(self.container.query_items(
            query=query,
            parameters=[{"name": "@nl", "value": nl}],
            enable_cross_partition_query=True
        ))
        return items[0] if items else None

    def search_by_name_prefix(self, prefix: str, limit: int = 20) -> List[Dict[str, Any]]:
        p = normalize_name(prefix)
        query = (
            "SELECT TOP @lim c.id, c.pk, c.name, c.ticker, c.isin, c.lei, c.country, c.sector "
            "FROM c WHERE STARTSWITH(c.name_lower, @p) "
            "ORDER BY c.name_lower"
        )
        items = list(self.container.query_items(
            query=query,
            parameters=[{"name": "@p", "value": p},
                        {"name": "@lim", "value": limit}],
            enable_cross_partition_query=True
        ))
        return items

    def find_by_keys(self, *, ticker: Optional[str]=None, isin: Optional[str]=None, lei: Optional[str]=None) -> List[Dict[str, Any]]:
        clauses = []
        params = []
        if non_empty(ticker):
            clauses.append("c.ticker = @t")
            params.append({"name": "@t", "value": ticker.upper()})
        if non_empty(isin):
            clauses.append("c.isin = @i")
            params.append({"name": "@i", "value": isin})
        if non_empty(lei):
            clauses.append("c.lei = @l")
            params.append({"name": "@l", "value": lei})
        if not clauses:
            return []
        query = "SELECT * FROM c WHERE " + " OR ".join(clauses)
        return list(self.container.query_items(
            query=query,
            parameters=params,
            enable_cross_partition_query=True
        ))
