def start():
    from agent.agent import run_agent
    from rag.vectorstore import push_doc
    
    while(True):
        query = input("Enter yout query : ")
        push_doc()
        state = run_agent(query)
        print("ANSWER")
        print(state.answer)


if __name__ == "__main__":
    start()
