from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Union

from .llm import call_llm, call_llm_json, get_model


JsonDict = Dict[str, Any]
Output = Union[str, JsonDict]


@dataclass
class RunRecord:
    run: int
    output: Output
    valid: Optional[bool] = None
    reason: str = "not_validated"


@dataclass
class RunBundle:
    task: str
    version: str
    model: str
    temperature: float
    runs: int
    created_at: str
    records: List[RunRecord]


def run_many(
    prompt: str,
    *,
    task: str,
    version: str,
    runs: int = 10,
    temperature: float = 0.0,
    as_json: bool = False,
    validator: Optional[Callable[[Output], tuple[bool, str]]] = None,
) -> RunBundle:
    model = get_model()
    records: List[RunRecord] = []

    for i in range(1, runs + 1):
        if as_json:
            out: Output = call_llm_json(prompt, model=model, temperature=temperature)
        else:
            out = call_llm(prompt, model=model, temperature=temperature)

        valid: Optional[bool] = None
        reason = "not_validated"
        if validator is not None:
            valid, reason = validator(out)

        records.append(RunRecord(run=i, output=out, valid=valid, reason=reason))

    return RunBundle(
        task=task,
        version=version,
        model=model,
        temperature=temperature,
        runs=runs,
        created_at=datetime.utcnow().isoformat(),
        records=records,
    )


def save_bundle(bundle: RunBundle, out_dir: str = "results") -> Path:
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    stamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    filename = f"{bundle.task}_{bundle.version}_{bundle.runs}runs_{stamp}.json"
    file_path = out_path / filename

    import json
    file_path.write_text(json.dumps(asdict(bundle), indent=2, ensure_ascii=False), encoding="utf-8")
    return file_path
