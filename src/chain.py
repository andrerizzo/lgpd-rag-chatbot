from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_core.callbacks import StdOutCallbackHandler


def build_chain(vectorstore, model_name):
    """
    Cria a cadeia conversacional com LLM, memória e retriever.

    Parameters:
        vectorstore (Chroma): Banco vetorial.
        model_name (str): Nome do modelo LLM.

    Returns:
        ConversationalRetrievalChain: Cadeia LangChain configurada.
    """
    llm = ChatOpenAI(temperature=0.7, model=model_name)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    retriever = vectorstore.as_retriever()
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm, retriever=retriever, memory=memory
    )
    return conversation_chain