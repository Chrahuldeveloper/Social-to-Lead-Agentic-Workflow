def start():
    from agent.agent import run_agent
    from rag.vectorstore import push_doc

    push_doc()

    state = run_agent("what are the plans available")
    print("\n--- ANSWER ---\n")
    print(state.answer)


if __name__ == "__main__":
    start()
