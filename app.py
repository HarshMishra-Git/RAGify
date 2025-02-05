from pipeline import build_rag_pipeline, handle_query

if __name__ == "__main__":
    vector_store = build_rag_pipeline()
    print("RAG system is ready.")

    while True:
        query = input("Enter your query (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        answer = handle_query(query, vector_store)
        print("AI Response:", answer)
