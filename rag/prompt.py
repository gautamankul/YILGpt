from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.1",
    device_map="auto"
)

def generate_answer(context: str, question: str):

    prompt = f"""
You are a helpful assistant.

Use ONLY the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

    output = generator(
        prompt,
        max_new_tokens=200,
        temperature=0.3,
        do_sample=True
    )

    return output[0]["generated_text"]