import json
from pathlib import Path
from collections import Counter


RESULTS_DIR = Path("results")


def load_latest_result():
    files = sorted(RESULTS_DIR.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not files:
        raise SystemExit("No result files found in /results")
    latest = files[0]
    data = json.loads(latest.read_text(encoding="utf-8"))
    return latest, data


def main():
    latest_file, data = load_latest_result()
    records = data.get("records", [])

    total = len(records)
    valid_count = sum(1 for r in records if r.get("valid") is True)
    invalid_count = sum(1 for r in records if r.get("valid") is False)
    not_validated = total - valid_count - invalid_count

    reasons = Counter(r.get("reason", "unknown") for r in records if r.get("valid") is False)
    
    valid_rate = (valid_count / total) if total else 0.0
    score = round(valid_rate * 100, 1)
   
    # crude drift signal: how many distinct outputs we got
    outputs = [json.dumps(r.get("output", {}), sort_keys=True, ensure_ascii=False) for r in records]
    unique_outputs = len(set(outputs))

    print(f"\nLatest results: {latest_file}")
    print(f"Task: {data.get('task')} | Version: {data.get('version')} | Model: {data.get('model')}")
    print(f"Runs: {total}")
    print(f"Valid: {valid_count}")
    print(f"Invalid: {invalid_count}")
    print(f"Reliability score: {score}/100")
    print(f"Not validated: {not_validated}")
    print(f"Unique outputs: {unique_outputs}/{total}")

    if invalid_count:
        print("\nTop failure reasons:")
        for reason, count in reasons.most_common(10):
            print(f"- {reason}: {count}")

    print("")


if __name__ == "__main__":
    main()

