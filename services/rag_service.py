from rag.retriever import get_retriever
from rag.reranker import rerank
from rag.prompt import generate_answer
from services.cache_service import get_cached, set_cache

retriever = get_retriever()


def process_query(query: str):
    MAX_CHARS = 1000

    cached = get_cached(query)
    if cached:
        return cached.decode("utf-8")

    nodes = retriever.retrieve(query)

    if not nodes:
        return "No relevant information found."

    # Hugging Face reranker
    nodes = rerank(query, nodes)

    # context = "\n".join([n.text for n in nodes])
    context = "\n".join([n.text[:300] for n in nodes[:2]])[:MAX_CHARS]

    answer = generate_answer(context, query)

    set_cache(query, answer)

    return answer
