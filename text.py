from PyPDF2 import PdfReader

#pacage responsavel por quebrar um texto em parte menores
from langchain.text_splitter import CharacterTextSplitter

def process_files(files):

    text = "" #string gigantesca

    # transformar nossos pdf's em uma string gigantesca:
    for file in files:
        pdf = PdfReader(file)
        for page in pdf.pages:
            text += page.extract_text()

    return text

#criar a funcao que pega os arquivos extraidos e transformar esta string(text) em pequenos textos, ou seja quebrá-los
#--------------------------------------------------------------------------------------

def create_text_chunks(text):

      #usamos aqui o langchain par processr textos (langchain.text_aplitter) para particionar um texto maior para 
    #em pedaços menores 


    text_splitter = CharacterTextSplitter(
        separator='\n', 

        chunk_size=1500,  #quantia de caracteres que cada chunk terá
        chunk_overlap=300,  #overlap : faz uma sobreposição para que o chunk proximo compense a quantia de caracter
        length_function=len #para ver o tamanho do chunk 
    )

    chunks = text_splitter.split_text(text)  #pegar os chunks passando o texto


    return chunks