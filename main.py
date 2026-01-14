def start():
    from agent.agent import run_agent
    from rag.vectorstore import push_doc

    query = input("Enter yout query")
    push_doc()
    state = run_agent(query)
    print("\n--- ANSWER ---\n")
    print(state.answer)


if __name__ == "__main__":
    start()
