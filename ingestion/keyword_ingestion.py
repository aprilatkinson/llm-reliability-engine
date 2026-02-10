from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict, Any, Optional
import csv
import os

try:
    import pandas as pd
except ImportError:
    pd = None


@dataclass
class ContentBrief:
    product: str
    price: str
    key_features: str
    audience: str
    primary_keyword: str
    secondary_keywords: List[str]
    intent: str
    marketplace: str


def _split_keywords(s: str) -> List[str]:
    if not s:
        return []
    # supports "a; b; c" or "a, b, c"
    parts = [p.strip() for p in s.replace(",", ";").split(";")]
    return [p for p in parts if p]


def load_briefs_from_csv(filepath: str) -> List[ContentBrief]:
    briefs: List[ContentBrief] = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            briefs.append(
                ContentBrief(
                    product=row.get("product", "").strip(),
                    price=row.get("price", "").strip(),
                    key_features=row.get("key_features", "").strip(),
                    audience=row.get("audience", "").strip(),
                    primary_keyword=row.get("primary_keyword", "").strip(),
                    secondary_keywords=_split_keywords(row.get("secondary_keywords", "")),
                    intent=row.get("intent", "").strip(),
                    marketplace=row.get("marketplace", "").strip(),
                )
            )
    return briefs


def load_briefs(filepath: str) -> List[ContentBrief]:
    """
    Loads ContentBrief rows from CSV or XLSX.
    - CSV requires Python's csv.
    - XLSX requires pandas + openpyxl installed.
    """
    ext = os.path.splitext(filepath)[1].lower()

    if ext == ".csv":
        return load_briefs_from_csv(filepath)

    if ext in {".xlsx", ".xls"}:
        if pd is None:
            raise ImportError("pandas is required for XLSX ingestion. pip install pandas openpyxl")
        df = pd.read_excel(filepath)
        # normalize column names (lowercase, strip)
        df.columns = [str(c).strip().lower() for c in df.columns]
        briefs: List[ContentBrief] = []

        for _, r in df.iterrows():
            briefs.append(
                ContentBrief(
                    product=str(r.get("product", "")).strip(),
                    price=str(r.get("price", "")).strip(),
                    key_features=str(r.get("key_features", "")).strip(),
                    audience=str(r.get("audience", "")).strip(),
                    primary_keyword=str(r.get("primary_keyword", "")).strip(),
                    secondary_keywords=_split_keywords(str(r.get("secondary_keywords", ""))),
                    intent=str(r.get("intent", "")).strip(),
                    marketplace=str(r.get("marketplace", "")).strip(),
                )
            )
        return briefs

    raise ValueError(f"Unsupported file type: {ext}. Use .csv or .xlsx")
