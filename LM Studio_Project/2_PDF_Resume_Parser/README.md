# 📄 Intelligent PDF Parsing (Resume Analysis)

## 📌 Overview
This section demonstrates the ability of a locally hosted Multimodal LLM (`Qwen-VL-7B`) to process and analyze unstructured, multi-page PDF documents entirely offline, ensuring complete data privacy.

## 🎯 Core Tasks Performed
The model was tasked with acting as an automated HR screening tool. It successfully parsed a complex CV and extracted highly specific metadata without external APIs.

### Extracted Data Points:
1. **Contact Information Tracking:** Accurately extracted the candidate's Email, Phone Number, and physical Address from the document header.
2. **Certification Extraction:** Filtered out general text to specifically isolate and list professional certifications, including:
   * CSCMP Supply Chain Foundations
   * Career Essentials in Business Analysis (Microsoft/LinkedIn)
   * Career Essentials in Data Analysis & Generative AI

## 📁 Attached Files
* `cv_pdf_analysis.md`: Contains the exact prompts and raw model output demonstrating the extraction process.
* Proof of concept screenshots demonstrating the model reading the PDF directly within the local environment.