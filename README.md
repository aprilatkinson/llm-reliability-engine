# LLM Reliability Engine
### Prompt Engineering, Evaluation & Governance Pipeline

This project demonstrates a systematic approach to improving Large Language Model (LLM) reliability through structured prompt engineering, empirical testing, and production-style validation pipelines.

The project was developed where a company’s chatbot produced inconsistent outputs across multiple tasks. The objective was to diagnose failure modes and improve reliability through iteration, structure, and evaluation.

---

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

---

## Keyword & Intent Ingestion (Semrush / Helium10-style Inputs)

To simulate real-world ecommerce workflows, the system supports ingestion of structured keyword and intent data exported from tools such as Semrush or Helium10.

Instead of generating product copy from raw prompts alone, each product is first converted into a structured **Content Brief**, which guides generation while maintaining governance and reliability constraints.

### Supported Input Format

The ingestion layer accepts CSV or XLSX files with the following columns:

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
├── prompt_engineering_lab.ipynb
├── ingestion/
│ ├── keyword_ingestion.py
│ └── sample_keywords.csv
├── outputs/
├── results/
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

Generate a reliability report
Latest results: results/product_v1_5runs_20260210_165619.json
Task: product | Version: v1 | Model: gpt-4o-mini
Runs: 5
Valid: 5
Invalid: 0
Not validated: 0
Reliability score: 100.0/100
Unique outputs: 2/5


Example output:

## How to Run prompt_engineering_lab.ipynb

1. Create a virtual environment
2. Install dependencies
3. Add your OpenAI API key to `.env`
4. Run the notebook:


---



## Author

April Atkinson  
AI GTM & Governance Consultant