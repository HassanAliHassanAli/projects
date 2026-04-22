# 🧾 Financial OCR & Data Extraction Workflow

## 📌 Overview
This section demonstrates the ability to extract highly accurate, structured financial data from noisy, real-world receipt images (Expenses Receipt OCR) using a locally hosted `Qwen-VL-7B` model.

## 🛠️ The 2-Step Extraction Strategy

To prevent model hallucination and context-window collapse, the data extraction was split into two distinct steps:

### Step 1: Raw Text Extraction (Zero-Shot OCR)
First, the model acts as a pure Vision/OCR engine to extract all text without structuring it.

**The Prompt Used:**
> "قم باستخراج كل كلمة ورقم وحرف موجود في صورة الفاتورة المرفقة، مع الحفاظ على الترتيب السطري قدر الإمكان. لا تقم بتنظيم البيانات في JSON أو جداول؛ فقط قم بتوفير النص 'الخام' بالكامل كما هو."

### Step 2: Structured JSON Output (Anti-Hallucination)
Once the raw text is extracted, a highly constrained prompt is used to format the data into a JSON array, preventing cross-contamination between multiple invoices.

**The Prompt Used (English Override for Precision):**
> "You are a strict Data Extraction AI. I will provide raw OCR text from 5 different receipts, separated by '=== RECEIPT ==='.
> Your task is to extract the exact financial data for each receipt and output ONLY a JSON Array containing objects.
> 
> Required Keys:
> "Store_Name", "Store_Address", "Transaction_Date", "Total_Amount", "Tax_Amount".
> 
> STRICT RULES:
> 1. Extract exact values from the text. DO NOT calculate or invent numbers.
> 2. If a value is missing, output null.
> 3. Output ONLY valid JSON. No conversational text."

## 📁 Attached Files
* See the images in this directory for the exact test dataset used.