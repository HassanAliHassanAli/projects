# 🚀 LLM Interactions Data Pipeline & MongoDB Stress Test

## 📌 Project Overview
This project demonstrates the power of NoSQL databases in handling large-scale, deeply nested data. It simulates a massive dataset of 1,000,000 AI Agent / LLM (Large Language Model) interaction logs. The goal is to stress-test MongoDB's import capabilities and perform high-speed aggregations and queries on complex JSON structures.

## 🛠️ The Engineering Challenge & Agile Adaptation
Initially, the project aimed to generate "Extreme RAG (Retrieval-Augmented Generation) Conversations" containing full context snippets and long-form reasoning chains. However, this deeply nested text generation rapidly consumed all available local storage on my primary drive. 

Instead of halting the project, I pivoted to a more optimized approach: generating **1,000,000 records of LLM Operational Logs**. This allowed me to push my Dell Precision 7720 workstation's CPU and Memory to their limits during data generation and MongoDB indexing, without hitting a storage bottleneck.

## 💻 Tech Stack
* **Python 3:** Data generation scripting.
* **Faker Library:** Mocking realistic UUIDs, timestamps, and model metrics.
* **MongoDB (NoSQL):** Data storage, querying, and aggregation.
* **MongoDB Compass:** GUI for data visualization and pipeline execution.

## 📂 Repository Structure
* `generate_llm_data.py`: The Python script used to generate the 1 Million JSON records in just over 100 seconds.
* `queries.mongodb`: A JavaScript file containing the exact MongoDB queries and aggregation pipelines used for analysis.
* `requirements.txt`: Python dependencies.

## 📊 Data Structure Highlights
Each document in the database represents a complete LLM request lifecycle, including:
* Nested Arrays (`processing_steps`).
* Numerical Metrics (`total_tokens_used`, `safety_score`).
* Categorical Data (`model_version`, `status`, `prompt_type`).

## 🔍 Key MongoDB Features Demonstrated
1. **High-Speed Indexing & Import:** Successfully imported 1M documents in a matter of seconds.
2. **Deep Nested Filtering (Dot Notation):** Extracted specific agent steps without the need for complex SQL `JOIN` statements.
3. **Aggregation Framework:** Used `$match` and `$group` pipelines to calculate the exact average of tokens consumed by each specific LLM model across the entire dataset.

## 🚀 How to Run Locally
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the generator script: `python generate_llm_data.py`
4. Import the resulting `.json` file into MongoDB Compass.
5. Open `queries.mongodb` to execute the analysis pipelines.

---
*Developed by Hassan Ali*