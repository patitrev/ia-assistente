import streamlit as st
from utils import chatbot, text
from streamlit_chat import message


def main():
    # Configura a página do Streamlit com título e ícone
    st.set_page_config(page_title='ChatPDF DotSet', page_icon=':books:')

    # Cria o cabeçalho da página com o título
    st.header('Converse com seus PDFs')

    # Cria um campo de entrada de texto para o usuário digitar sua pergunta
    user_question = st.text_input("Qual a sua dúvida?")

    # Inicializa o estado da sessão do Streamlit se ainda não estiver configurado
    # 'conversation' irá armazenar o histórico da conversa
    if 'conversation' not in st.session_state:
        st.session_state.conversation = None
        print(st.session_state.conversation)

    # Se o usuário enviou uma pergunta, processa a resposta
    if user_question:
        # Obtém a resposta do chatbot, incluindo o histórico da conversa
        response = st.session_state.conversation(user_question)['chat_history']

        # Itera sobre o histórico da conversa e exibe cada mensagem
        for i, text_message in enumerate(response):
            # Verifica se o índice é par ou ímpar para determinar o remetente da mensagem
            # Alterna entre mensagens enviadas pelo usuário (índice par) e pelo chatbot (índice ímpar)
            if i % 2 == 0:
                message(text_message.content,
                        is_user=True, key=str(i) + '_user')
            else:
                message(text_message.content,
                        is_user=False, key=str(i) + '_bot')

    # Configura a barra lateral do Streamlit para upload de arquivos PDF
    with st.sidebar:
        st.subheader('Seus arquivos')

        # Cria um uploader de arquivos que permite o upload de múltiplos arquivos PDF
        pdf_docs = st.file_uploader(
            "Carregue os seus arquivos em formato PDF", accept_multiple_files=True)

        # Cria um botão para processar os arquivos PDF carregados
        if st.button('Processar'):
            # Processa o conteúdo dos arquivos PDF carregados
            all_files_text = text.process_files(pdf_docs)

            # Divide o texto extraído dos PDFs em pequenos chunks (fragmentos)
            chunks = text.create_text_chunks(all_files_text)

            # Cria uma vectorstore com os chunks de texto usando embeddings
            vectorstore = chatbot.create_vectorstore(chunks)

            # Cria um objeto de cadeia de conversa (Conversational Retrieval Chain) usando a vectorstore
            st.session_state.conversation = chatbot.create_conversation_chain(
                vectorstore)


# Executa a função principal apenas se este arquivo for executado diretamente
if __name__ == '__main__':
    main()
