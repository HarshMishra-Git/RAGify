

from transformers import pipeline

# Initialize Hugging Face pipeline for text generation
model_name = "gpt2"  # You can replace this with another model like 'gpt-neo', 'distilgpt2', etc.
generator = pipeline('text-generation', model=model_name)

def generate_response(query, context):
    """
    Generates a response based on the provided query and context using Hugging Face's model.
    
    Parameters:
    - query (str): The user's query.
    - context (str): The context to be considered for the response generation.

    Returns:
    - str: The generated response.
    """
    input_text = context + " " + query  # Combine the query and context
    response = generator(input_text, max_length=150, num_return_sequences=1)
    return response[0]['generated_text']

# Example usage (replace this with your actual query and context)
if __name__ == "__main__":
    context = "Artificial Intelligence (AI) is a field of computer science that aims to create machines that can perform tasks that typically require human intelligence."
    query = "What is AI?"
    
    answer = generate_response(query, context)
    print(f"Answer: {answer}")
