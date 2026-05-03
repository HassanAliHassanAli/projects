import json
import random
from faker import Faker
import time
import uuid

fake = Faker()

# مليون جلسة، بس المرة دي الجلسة الواحدة دسمة جداً
NUM_SESSIONS = 1000000
FILE_NAME = "llm_extreme_rag_conversations.json"

print(f"🔥 جاري توليد {NUM_SESSIONS} جلسة معقدة جداً... اربط الحزام عشان الملف ده هيكون عملاق!")
start_time = time.time()

with open(FILE_NAME, "w", encoding="utf-8") as file:
    file.write("[\n") 

    for i in range(NUM_SESSIONS):
        # الهيكل الأساسي للجلسة
        session = {
            "session_id": str(uuid.uuid4()),
            "user_metadata": {
                "ip_address": fake.ipv4(),
                "device_info": fake.user_agent(),
                "geolocation": {"country": fake.country(), "city": fake.city()}
            },
            "conversation_history": [] # مصفوفة هتشيل المحادثات
        }

        # كل جلسة هيكون فيها من محادثتين لـ 5 محادثات (عشان نضخم حجم البيانات)
        for _ in range(random.randint(2, 5)):
            turn = {
                "message_id": str(uuid.uuid4()),
                "user_prompt": fake.sentence(nb_words=15), # سؤال المستخدم
                
                # تخيل النموذج بيدور في داتا بيز وبيجيب مقالات كاملة (RAG)
                "retrieved_context": [
                    {
                        "source_url": fake.url(),
                        "content_snippet": fake.paragraph(nb_sentences=6), # فقرة كاملة لكل مصدر
                        "relevance_score": round(random.uniform(0.75, 0.99), 4)
                    } for _ in range(random.randint(2, 6)) # من مصدرين لـ 6 مصادر لكل سؤال
                ],
                
                # النموذج بيفكر على خطوات
                "agent_reasoning_chain": [
                    {"step": "Intent Mapping", "result": fake.sentence(nb_words=5)},
                    {"step": "Fact Checking", "result": fake.sentence(nb_words=8)},
                    {"step": "Drafting", "result": "Generating output based on retrieved context."}
                ],
                
                # الرد النهائي للنموذج (نص طويل جداً)
                "final_llm_response": fake.text(max_nb_chars=1000), 
                "execution_metrics": {
                    "total_latency_ms": random.randint(300, 5000),
                    "prompt_tokens": random.randint(50, 500),
                    "completion_tokens": random.randint(100, 1500)
                }
            }
            session["conversation_history"].append(turn)

        json.dump(session, file)

        if i < NUM_SESSIONS - 1:
            file.write(",\n")
        else:
            file.write("\n")

        if (i + 1) % 50000 == 0:
            print(f"⏳ تم عصر {i + 1} جلسة... كمل، الجهاز لسه بيتنفس!")

    file.write("]") 

end_time = time.time()
print(f"💀 التحدي خلص في {round(end_time - start_time, 2)} ثانية!")
print(f"📁 روح شوف حجم الملف ({FILE_NAME}) وصل لكام جيجا!")