# 🚀 Local LLM Engineering Portfolio: AI in Enterprise Workflows

## 📌 Project Overview
This repository serves as a comprehensive portfolio demonstrating the advanced capabilities of a locally hosted, offline Multimodal Large Language Model (**Qwen2-VL-7B-Instruct** running via LM Studio). 

The primary objective is to showcase how zero-shot, privacy-first AI agents can be utilized as "Expert Consultants" and "Data Engineers" across diverse software engineering, business analysis, and data extraction domains—without relying on cloud APIs.

---

## 📂 Repository Structure & Technical Scenarios

### 🧾 1. Financial OCR & Data Extraction
**[View Financial OCR Workflow](./1_Financial_OCR_Extraction/financial_ocr_workflow.md)**
* **Domain:** Data Engineering & Automated Accounting.
* **Concept:** Extracted structured JSON data (Store Name, Total, Tax, Date) from highly noisy, real-world receipt images (e.g., crumpled Walmart and Trader Joe's receipts).
* **Technique Used:** Implemented a "2-Step Extraction Strategy" to bypass the inherent hallucination limits of 7B models. Step 1: Raw vision OCR. Step 2: Strict JSON structuring using an English-override constraint prompt.

### 📄 2. Intelligent PDF Parsing (Resume Analysis)
**[View CV Analysis Log](./2_PDF_Resume_Parser/cv_pdf_analysis.md)**
* **Domain:** HR Automation & Unstructured Data Processing.
* **Concept:** Parsed a complex, multi-page PDF document (CV) to accurately extract targeted metadata.
* **Technique Used:** Directed the multimodal AI to act as an HR screener, successfully isolating contact information and specific professional certifications (e.g., Supply Chain Foundations, Business Analysis) directly from the document without external parsers.

### 🛡️ 3. Database Architecture & Cybersecurity
**[View Database Load Testing Script](./3_Database_Architecture_Security/database_load_testing.md)** | **[View SQLi Defense Guide](./3_Database_Architecture_Security/sqli_defense_guide.md)**
* **Domain:** Database Administration (DBA) & Penetration Testing.
* **Concept 1 (Architecture):** Generated a massive SQL script to create a normalized relational database schema (Customers, Products, Orders, Transactions), populated it with dummy data, and wrote a safe reverse-order `DROP TABLE` sequence for teardown.
* **Concept 2 (Security):** Created a highly technical executive guide detailing the 3 main vectors of SQL Injection (In-band, Inferential, Out-of-band), provided theoretical malicious payloads, and demonstrated absolute mitigation using Parameterized Queries.

### 📊 4. Agile Project Management & AI Automation
**[View Agile Methodology Guide](./4_Agile_AI_Automation/agile_jira_methodology.md)** | **[View AI-Jira Integration Architecture](./4_Agile_AI_Automation/ai_jira_integration.md)**
* **Domain:** Systems Analysis, Scrum Management & AI Workflow Automation.
* **Concept 1 (Agile Map):** An executive breakdown of Agile philosophy, Scrum ceremonies, and strict mapping into Atlassian Jira's hierarchy (Epics ➔ Stories ➔ Tasks ➔ Bugs).
* **Concept 2 (AI Vision):** A cutting-edge architectural proposal detailing how LLMs can integrate with Jira's REST API to autonomously translate raw client requirements into perfectly formatted User Stories, decompose Epics, and predict QA testing risks based on historical data.

---

## 🛠️ Tech Stack & Execution Environment
* **Inference Engine:** LM Studio (Local, 100% Offline)
* **Model:** Qwen2-VL-7B-Instruct (Quantized)
* **Hardware Utilization:** GPU accelerated local processing.
* **Prompt Engineering Strategy:** * Role-based constraint prompting.
  * Delimiter usage to prevent context-window collapse.
  * Structural formatting (Strict JSON & Markdown).
  * Cognitive load reduction (using English prompts for complex logic tasks).

---
*Developed as a proof of concept for integrating local AI into secure, enterprise-level engineering workflows.*