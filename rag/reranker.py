from sentence_transformers import CrossEncoder

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def get_reranker():
    return model


def rerank(query, nodes):
    pairs = [[query, n.text] for n in nodes]
    scores = model.predict(pairs)

    ranked = sorted(zip(nodes, scores), key=lambda x: x[1], reverse=True)

    return [node for node, _ in ranked[:3]]
