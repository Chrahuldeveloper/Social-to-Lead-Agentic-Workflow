from agent.state import AgentState
from rag.vectorstore import retrive_info
from rag.generator import generate_answer
from config import GEMINI_CLIENT,GEMINI_MODEL

def detect_intent(question) :
    prompt = f"""
    Classify the user intent into ONE of these:
    - factual_question
    - pricing_question
    - support_question
    - irrelevant

    Return ONLY the label

    Question: {question}
     """
    resp = GEMINI_CLIENT.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )
    return resp.text.strip().lower()


TOOLS = {
    "rag": generate_answer
}

def run_agent(question):
    state = AgentState(question)
    state.intent = detect_intent(question)

    if state.intent in ["factual_question", "pricing_question"]:
        state.context = retrive_info(state.question,3)
        state.answer = TOOLS["rag"](state.question, state.context)

    elif state.intent == "irrelevant":
        state.answer = "I can only answer questions related to the provided knowledge"

    else:
        state.answer = "I don't know"

    return state
