# LLM Reliability Engine
### Prompt Engineering, Evaluation & Governance Pipeline

This project demonstrates a systematic approach to improving Large Language Model (LLM) reliability through structured prompt engineering, empirical testing, and production-style validation pipelines.

The goal is to move LLM usage from single-run experimentation toward repeatable, measurable, and governance-aware workflows suitable for production environments.

The project originated from diagnosing inconsistent outputs produced by an AI system across multiple tasks. The objective was to identify failure modes and improve reliability through iteration, structure, validation, and evaluation.

---
# Why Reliability Matters
LLMs are probabilistic systems. A correct output once does not imply reliable behavior under repetition.

In production environments — especially marketing, ecommerce, and data workflows — inconsistent outputs introduce operational risk. This project treats LLMs as production components that require measurement, validation, and enforcement layers before integration into downstream systems.

The focus is therefore on repeatability and consistency, not single-run output quality.

## Project Goals

The system improves reliability across three common AI tasks:

- **Sentiment Analysis**
- **Structured Data Extraction**
- **Product Description Generation**

Key objectives:

- Identify prompt failure patterns through repeated testing
- Improve consistency using few-shot prompting and structured outputs
- Apply Chain-of-Thought reasoning where appropriate
- Enforce output constraints for production reliability
- Demonstrate measurable improvements across iterations

---

## Key Concepts Demonstrated

- Zero-shot vs few-shot prompting
- Chain-of-Thought prompting
- Structured JSON outputs
- Reliability testing across multiple runs
- Failure analysis and consistency measurement
- Generate → Validate → Enforce pipeline design
- Governance-aware prompt constraints (brand & compliance)
- Separation of generation and validation layers 

---

## Keyword & Intent Ingestion (Semrush / Helium10-style Inputs)

To simulate real-world ecommerce workflows, the system supports ingestion of structured keyword and intent data exported from tools such as Semrush or Helium10.

Instead of generating product copy directly from prompts, product data is first normalized into a structured Content Brief, guiding generation while maintaining reliability and governance constraints.

### Supported Input Format

The ingestion layer accepts CSV or XLSX files with fields such as:

| Column | Description |
|---|---|
| product | Product name |
| price | Product price |
| key_features | Semicolon-separated feature list |
| audience | Target customer segment |
| primary_keyword | Main SEO/AIO keyword |
| secondary_keywords | Supporting keywords (semicolon-separated) |
| intent | Search intent (e.g., informational, commercial) |
| marketplace | Target channel (web, marketplace, etc.) |

---

## Pipeline Architecture

Keyword / Product Data (CSV/XLSX)
            ↓
Content Brief Normalization
            ↓
Prompt Generation (Brand + Compliance Constraints)
            ↓
LLM Generation
            ↓
Validation & Constraint Enforcement
            ↓
Structured JSON Output

---

## Reliability Results (Summary)

| Task | Version | Runs | Valid Rate | Notes |
|---|---|---|---|---|
| Sentiment Analysis | v3 | 15 | 1.0 | Few-shot examples stabilized output format |
| Data Extraction | v3 | 15 | 1.0 | JSON schema eliminated format drift |
| Product Generation (single-pass) | v3 | 15 | 0.0 | Word-count constraint failures |
| Product Generation (two-step pipeline) | v3 | 15 | 1.0 | Generate → Validate → Enforce solved constraint reliability |

---

## Repository Structure
├── src/
│   └── llm_reliability/
│       ├── llm.py              # OpenAI wrapper
│       ├── runner.py           # Multi-run execution engine
│       └── io.py               # Result storage utilities
│
├── scripts/
│   ├── run_product_test.py     # Example reliability test
│   └── report_latest.py        # Reliability report generator
│
├── ingestion/
│   ├── keyword_ingestion.py
│   └── sample_keywords.csv
│
├── results/                    # Generated run artifacts (ignored by git)
├── prompt_engineering_lab.ipynb
├── run.py                      # Single entrypoint runner
└── README.md


---
## Quick Start

Run a full reliability test and report with one command:

```bash
python run.py
This will:

Execute multiple LLM runs for the same prompt

Validate outputs against task constraints

Save structured results to /results

Generate a reliability report including:

- validity rate

- reliability score

- output drift signal

Example output:

Latest results: results/product_v1_5runs_XXXX.json
Task: product | Version: v1 | Model: gpt-4o-mini
Runs: 5
Valid: 5
Invalid: 0
Not validated: 0
Reliability score: 100.0/100
Unique outputs: 2/5


## Running the Notebook (Optional)

The original experimentation workflow is preserved in:
prompt_engineering_lab.ipynb

Steps:

- Create a virtual environment
- Install dependencies
- Add your OpenAI API key to a local .env file
- Run the notebook cells

Note: .env is not committed to the repository.


---



## Author

April Atkinson  
AI GTM & Governance Consultant
# LLM Reliability Engine
### Prompt Engineering, Evaluation & Governance Pipeline
