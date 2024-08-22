from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter


def process_files(files):
    """
    Extrai o texto de uma lista de arquivos PDF e o combina em uma única string.

    Args:
        files (list of file-like objects): Lista de arquivos PDF carregados pelo usuário.

    Returns:
        str: Texto combinado extraído de todos os arquivos PDF.
    """
    text = ""  # Inicializa uma string para armazenar o texto combinado

    # Itera sobre cada arquivo na lista de arquivos
    for file in files:
        pdf = PdfReader(file)  # Cria um objeto PdfReader para o arquivo PDF
        # Itera sobre cada página do PDF
        for page in pdf.pages:
            text += page.extract_text()  # Extrai e adiciona o texto da página à string

    return text


def create_text_chunks(text):
    """
    Divide o texto em partes menores (chunks) para facilitar o processamento.

    Args:
        text (str): Texto a ser dividido em chunks.

    Returns:
        list of str: Lista de textos divididos em chunks.
    """
    # Configura o divididor de texto para dividir o texto em chunks menores
    text_splitter = CharacterTextSplitter(
        separator='\n',          # Caracter que separa os chunks
        chunk_size=1500,         # Tamanho máximo de cada chunk em caracteres
        chunk_overlap=300,       # Número de caracteres de sobreposição entre chunks consecutivos
        length_function=len      # Função usada para calcular o tamanho do chunk
    )

    # Divide o texto em chunks e retorna a lista de chunks
    chunks = text_splitter.split_text(text)

    return chunks
