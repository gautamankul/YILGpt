from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

def generate_answer(context: str, question: str):

    prompt = f"""
You are a helpful assistant.

Use ONLY the provided context.

Context:
{context}

Question:
{question}

If the answer is not in the context, say "I don't know".
"""

    response = llm.invoke(prompt)

    return response.content