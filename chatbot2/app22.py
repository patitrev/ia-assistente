import streamlit as st
from utils import chatbot, text
from streamlit_chat import message



def main():

    st.set_page_config(page_title='ChatPDF DotSet', page_icon=':books:')

     #input do usuario
    st.header('Converse com seus PDFs')
    user_question = st.text_input("Qual a sua dúvida?")
#-------------------------------------------------------------------------
    if('conversation' not in st.session_state):
        st.session_state.conversation = None
        

#-----------------------------------------------------------------------
    if(user_question):  #se existir uma conversa responda ao usuario
        
        #vai conter a resposta do chatboot
        #chat_history para armazenar o historico da conversa 
        response = st.session_state.conversation(user_question)['chat_history']

        for i, text_message in enumerate(response): #pega a posição(indice) na fila do historico
           
            # entao se o indice for par é pergunta senao é resposta 
            # ey é o id da resposta do usuário  para o gerenciamento dos balazinhos 

            if(i % 2 == 0):
                message(text_message.content, is_user=True, key=str(i) + '_user')

            else:
                message(text_message.content, is_user=False, key=str(i) + '_bot')


    with st.sidebar:

        st.subheader('Seus arquivos')

         # abre o navegador de arquivos - segundo argumento é para aceitar vários arquivos
        pdf_docs = st.file_uploader("Carregue os seus arquivos em formato PDF", accept_multiple_files=True)
         #  print(pdf_docs)  # vai imprimir no cmd - so para testar 


        if st.button('Processar'):   # o if é necessário para não executar toda a função cada vez que clicar
               
         

            all_files_text = text.process_files(pdf_docs)
               # print(all_files_text) #impriir só para teste
            
            #chamando a funão que cria os chunks em text.py
            chunks = text.create_text_chunks(all_files_text)

            vectorstore = chatbot.create_vectorstore(chunks)
            # print (vectorstore) #so pra saber se criou vectorestore

            #precisa retornar: <langchain_community.vectorstores.faiss.FAISS object at 0

            #st.session_state são armazenadas os valores das variaveis durante a sessao
            #se nao ela apaga a cada interação e não sao reiniciadas
            st.session_state.conversation = chatbot.create_conversation_chain(vectorstore)

            

if __name__ == '__main__':

    main()