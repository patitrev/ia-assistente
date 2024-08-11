from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain


#transformando os chunks em vectors:
#inicializando a vectory store  com os embedding dos arquivos que fizemos o upload
def create_vectorstore(chunks):
    embeddings = OpenAIEmbeddings()
    
    #cria uma vectostore com os nossos textos (chunks sendo transrmados em embeddings)
    #assim podemos verificar a assimilaridade
    vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)

    return vectorstore
#-----------------------------------------------------------------
 #criando a conversasao:
def create_conversation_chain(vectorstore):
  
    #também faz as comparações de similaridade
    llm = ChatOpenAI()  #padrao: gpt-3.5-turbo , pode modificar se quiser

    #historico da conversa:
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )

    return conversation_chain