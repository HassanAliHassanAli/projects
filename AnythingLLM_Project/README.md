# 🔬 Local LLM Stress Test & Architectural QA Analysis

![LLM Testing](https://img.shields.io/badge/Testing-LLM_QA-blue.svg)
![Environment](https://img.shields.io/badge/Environment-Local_Deployment-success.svg)
![Model](https://img.shields.io/badge/Model-Qwen2__VL__7B-orange.svg)
![Framework](https://img.shields.io/badge/Framework-AnythingLLM_%7C_LM_Studio-purple.svg)

## 📌 Executive Summary
This repository contains a comprehensive Quality Assurance (QA) and Stress Testing case study focused on evaluating the capabilities of small-parameter local Large Language Models (LLMs) — specifically in the 7B parameter range. 

The primary objective of this project is to benchmark the model's reliability, logical reasoning, and hallucination rates when tasked with highly complex, enterprise-level prompts. Rather than testing basic conversational abilities, this suite pushes the model to generate production-ready code, design cloud architectures, and simulate advanced cybersecurity automations.

The findings establish a clear boundary between tasks suitable for local, consumer-hardware deployment versus tasks requiring advanced Cloud APIs.

---

## ⚙️ System Architecture & Environment Setup

The testing environment was configured to simulate a fully private, local AI workspace ensuring zero data leakage.

* **Frontend / Workspace Manager:** `AnythingLLM (v1.12.0)`
* **Inference Backend:** `LM Studio`
* **Local Model Selected:** `qwen2-vl-7b-instruct` (Quantized format for memory efficiency)
* **Context Window Configured:** `16,384 Tokens`
* **Hardware Acceleration:** GPU Offloading enabled via CUDA.

---

## 🧪 Testing Methodology & Prompt Engineering Strategy

To accurately assess the model's limits, the prompts were engineered using strict constraints:
1. **Persona Adoption:** The model was forced to act as Senior Engineers, Architects, and CISOs.
2. **Constraint Enforcement:** Strict instructions such as *"Do not use placeholders,"* *"Write production-ready code,"* and *"Ensure mathematical accuracy"* were enforced.
3. **Complexity Layering:** Tasks required multi-step reasoning, integrating multiple libraries (e.g., FastAPI + Scikit-learn, Terraform AWS resources).

---

## 📊 Detailed Test Cases & QA Results

The analysis is divided into four distinct engineering domains. Below is the executive summary of the performance in each domain. *(Detailed raw outputs and technical reviews can be found in their respective directories).*

### 1️⃣ Cybersecurity Mind Map & Study Roadmap
* **Objective:** Design a structured 5-year career roadmap from foundational networking to Red/Blue teaming.
* **Category:** Text Generation, Summarization, Domain Mapping.
* **Result:** 🟢 **PASS (9/10)**
* **Technical Observation:** The model excels at organizing concepts. It accurately mapped out logical career progressions, utilized correct markdown formatting for nested lists, and correctly identified industry-standard certifications (CISSP, CEH).

### 2️⃣ Machine Learning Anomaly Detection (FastAPI + Scikit-Learn)
* **Objective:** Build a REST API for financial fraud detection using an Isolation Forest model.
* **Category:** Complex Logic, Mathematical Reasoning, Code Generation.
* **Result:** 🔴 **FAIL (3/10)**
* **Technical Observation:** Critical failure in mathematical logic. The model introduced a fatal Data Leakage/Zero Division error in the preprocessing pipeline (`(df - df.mean()) / df.std()`) and skipped the actual training phase entirely, proving it cannot reliably generate production-ready ML infrastructure.

### 3️⃣ Blue Team Incident Response (OS Automation)
* **Objective:** Write a Ransomware response playbook and an automated Python script to isolate compromised nodes via firewall rules.
* **Category:** Low-Level System Interaction, Cybersecurity Automation.
* **Result:** 🔴 **FAIL (2/10)**
* **Technical Observation:** Severe library hallucination. The model fabricated WMI classes (e.g., `Win32_NetworkFirewallRule`) and invented Python methods that do not exist in the Windows OS architecture. The code is non-executable.

### 4️⃣ AWS Cloud Architecture (Terraform IaC)
* **Objective:** Provision a highly available E-commerce infrastructure (VPC, ALB, ASG, RDS, ElastiCache) using HashiCorp Configuration Language (HCL).
* **Category:** Infrastructure as Code (IaC), Cloud Architecture.
* **Result:** 🔴 **FAIL (2/10)**
* **Technical Observation:** The generated `.tf` code was riddled with fatal syntax errors, illegal resource nesting (placing `launch_config` inside an `aws_autoscaling_group`), and critical security flaws (opening SSH to `0.0.0.0/0`).

---

## 📂 Repository Structure

The repository is organized into specific test domains. Each folder contains the engineered prompt, the raw response from the LLM, and a strict technical code review.

```text
Local-LLM-Engineering-Portfolio/
│
├── 01_Cybersecurity_Roadmap/
│   ├── Prompt_1.md
│   ├── Raw_Response_1.md
│   └── Technical_Review_1.md
│
├── 02_ML_Anomaly_Detection/
│   ├── Prompt_2.md
│   ├── Raw_Response_2.md
│   └── Technical_Review_2.md
│
├── 03_BlueTeam_Incident_Response/
│   ├── Prompt_3.md
│   ├── Raw_Response_3.md
│   └── Technical_Review_3.md
│
├── 04_AWS_Cloud_Architecture/
│   ├── Prompt_4.md
│   ├── Raw_Response_4.md
│   └── Technical_Review_4.md
│
└── README.md