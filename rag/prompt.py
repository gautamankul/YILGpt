from transformers import pipeline, GenerationConfig

# generator = pipeline(
#     "text-generation", model="mistralai/Mistral-7B-Instruct-v0.1", device_map="auto"
# )

generator = pipeline("text-generation", model="microsoft/phi-2", device_map="auto")

generation_config = GenerationConfig(
    max_new_tokens=200,
    temperature=0.3,
    do_sample=True,
    pad_token_id=2,  # avoids warning
)


# def generate_answer(context: str, question: str):

#     prompt = f"""
# You are a helpful assistant.

# Use ONLY the provided context.

# Context:
# {context}/n

# Question:
# {question}/n

# Answer:
# """

#     output = generator(prompt, generation_config=generation_config)

#     return output[0]["generated_text"]


def generate_answer(context: str, question: str):

    prompt = f"""Context: {context}

   Q: {question}
   
   A:"""

    output = generator(prompt, generation_config=generation_config)

    generated = output[0]["generated_text"]

    # Remove prompt part
    answer = generated.replace(prompt, "").strip()

    return answer
