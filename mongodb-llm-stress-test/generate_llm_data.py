import json
import random
from faker import Faker
import time

fake = Faker()

# هنولد مليون جلسة تفكير لنموذج ذكاء اصطناعي
NUM_SESSIONS = 1000000
FILE_NAME = "llm_interactions_massive.json"

# مكونات وخطوات تفكير الـ LLM
components = ["PromptAnalyzer", "SafetyFilter", "ContextRetriever", "ResponseGenerator", "FactChecker"]
tasks = ["Creative_Writing", "Code_Debugging", "General_Q&A", "Summarization", "Translation"]
statuses = ["Success", "Filtered_Unsafe", "Timeout", "Hallucination_Detected"]
models = ["Model-v1.5-Turbo", "Model-v2-Pro", "Model-Mini-Fast"]

print(f"🚀 جاري توليد {NUM_SESSIONS} جلسة تفكير لنموذج LLM... راقب أداء جهازك!")
start_time = time.time()

with open(FILE_NAME, "w", encoding="utf-8") as file:
    file.write("[\n") 

    for i in range(NUM_SESSIONS):
        # توليد بيانات معقدة لمحاكاة تفكير النموذج اللغوي
        session = {
            "interaction_id": f"req_{fake.uuid4()}",
            "user_id": f"usr_{random.randint(1000, 99999)}",
            "prompt_type": random.choice(tasks),
            "model_version": random.choice(models),
            "total_tokens_used": random.randint(50, 4000),
            "status": random.choice(statuses) if random.random() > 0.1 else "Success", # أغلب الطلبات بتنجح
            "processing_steps": [
                {
                    "component": "PromptAnalyzer",
                    "action": "Tokenization_and_Intent_Parsing",
                    "metrics": {
                        "prompt_tokens": random.randint(10, 500),
                        "detected_language": random.choice(["en", "ar", "es", "fr"]),
                        "complexity_score": round(random.uniform(0.1, 0.9), 2)
                    },
                    "timestamp": fake.iso8601()
                },
                {
                    "component": "ContextRetriever",
                    "action": "Vector_Database_Search",
                    "metrics": {
                        "documents_retrieved": random.randint(0, 5),
                        "search_latency_ms": random.randint(15, 120)
                    },
                    "timestamp": fake.iso8601()
                },
                {
                    "component": "ResponseGenerator",
                    "action": "Drafting_Output",
                    "metrics": {
                        "completion_tokens": random.randint(20, 3500),
                        "generation_time_ms": random.randint(200, 3000),
                        "temperature_used": round(random.uniform(0.0, 1.0), 1)
                    },
                    "timestamp": fake.iso8601()
                }
            ],
            "safety_score": round(random.uniform(0.8, 1.0), 2)
        }

        json.dump(session, file)

        if i < NUM_SESSIONS - 1:
            file.write(",\n")
        else:
            file.write("\n")

        if (i + 1) % 100000 == 0:
            print(f"✅ تم توليد سجلات {i + 1} سؤال وجواب...")

    file.write("]") 

end_time = time.time()
print(f"🎉 تمت العملية بنجاح في {round(end_time - start_time, 2)} ثانية!")
print(f"📁 الملف جاهز باسم: {FILE_NAME}")