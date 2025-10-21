import re
from typing import Optional

def normalize_name(name: str) -> str:
    x = name.strip().lower()
    x = re.sub(r"\s+", " ", x)
    return x

def derive_pk_from_name(name: str) -> str:
    n = normalize_name(name)
    return n[0] if n else "_"

def non_empty(x: Optional[str]) -> bool:
    return isinstance(x, str) and x.strip() != ""
