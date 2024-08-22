import os
import openai
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém a chave da API OpenAI do ambiente
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError(
        "API key not found. Please set the OPENAI_API_KEY environment variable.")

# Inicializa a chave da API para a biblioteca OpenAI
openai.api_key = api_key

# Função para criar uma vectorstore a partir de chunks de texto


def create_vectorstore(chunks):
    """
    Cria uma vectorstore a partir de chunks de texto.

    Args:
        chunks (list of str): Lista de textos (chunks) para criar a vectorstore.

    Returns:
        FAISS: Objeto FAISS contendo os embeddings dos chunks.
    """
    # Inicializa o modelo de embeddings da OpenAI
    embeddings = OpenAIEmbeddings()

    # Cria uma vectorstore usando o FAISS para armazenar e consultar os embeddings dos chunks
    vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)

    return vectorstore

# Função para criar uma cadeia de conversa


def create_conversation_chain(vectorstore):
    """
    Cria uma cadeia de conversa usando um modelo de linguagem e uma vectorstore.

    Args:
        vectorstore (FAISS): Objeto FAISS que contém os embeddings dos chunks de texto.

    Returns:
        ConversationalRetrievalChain: Cadeia de conversa configurada.
    """
    # Inicializa o modelo de linguagem ChatOpenAI (padrão é o gpt-3.5-turbo)
    llm = ChatOpenAI()  # Pode-se modificar o modelo se desejado

    # Configura a memória para armazenar o histórico da conversa
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)

    # Cria uma cadeia de conversa que combina o modelo de linguagem, a vectorstore e a memória
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )

    return conversation_chain
