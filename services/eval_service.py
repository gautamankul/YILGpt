from ragas import evaluate

def evaluate_rag(dataset):
    metrics = ["faithfulness", "answer_relevance", "context_precision"]
    result = evaluate(dataset, metrics=metrics)
    return result