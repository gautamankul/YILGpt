from rag.retriever import get_retriever
from rag.reranker import get_reranker
from rag.prompt import generate_answer
from services.cache_service import get_cached, set_cache

retriever = get_retriever()
reranker = get_reranker()

def process_query(query: str):

    # Cache check
    cached = get_cached(query)
    if cached:
        return cached.decode("utf-8")

    # Retrieve
    nodes = retriever.retrieve(query)

    if not nodes:
        return "No relevant information found."

    # Rerank
    nodes = reranker.postprocess_nodes(nodes, query=query)

    # Build context
    context = "\n".join([n.text for n in nodes])

    # Generate answer
    answer = generate_answer(context, query)

    # Cache response
    set_cache(query, answer)

    return answer