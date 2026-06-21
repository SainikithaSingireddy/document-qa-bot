from src.query import ask_question

def run_chatbot():
    print("\n🤖 RAG Document Q&A Bot Ready!\n")

    while True:
        question = input("Ask a question (or type 'exit'): ")

        if question.lower() == "exit":
            print("Goodbye!")
            break

        answer = ask_question(question)

        print("\n" + "="*60)
        print("\n📚 Answer:\n")
        print(answer)
        print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    run_chatbot()