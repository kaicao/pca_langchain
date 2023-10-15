import sys

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from pytesseract_loader import PytesseractLoader

from llama2_embedding import embed
from llama2_query import query
import json

PDF_PATH = 'document/red_hat_satellite.pdf'

def splitDocuments(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=0)
    splitted_docs = text_splitter.split_documents(documents)
    return splitted_docs

def embedExamplePdf():
    print('Start loading pdf')
    pdf_loader = PyPDFLoader('document/red_hat_satellite.pdf')
    splitted_docs = splitDocuments(pdf_loader.load())
    embed(splitted_docs)
    print('Embedded the loaded pdf')

def embedExampleImage():
    print('Start loading image')
    ocr_loader = PytesseractLoader('document/ocr_test5.png')
    text = ocr_loader.load()
    splitted_docs = splitDocuments(text)
    embed(splitted_docs)
    print('Embedded the loaded image')

def main():
    #embedExamplePdf()
    embedExampleImage()

    print('Please type in the question (type exit for stopping): ')
    chat_history = []
    for line in sys.stdin:
        strippedLine = line.strip()
        if not strippedLine:
            print('No input, so skip...')
            continue
        # when exit is received stop the thread
        elif strippedLine == 'exit':
            print('Exit command received, exiting...')
            break
        else:
            print('Query LLM for: ' + strippedLine)
            result = query(strippedLine, chat_history)
            # Issue with chat_history, slows down a lot and make invalid result
            #chat_history = [(strippedLine, result["answer"])]
            json_data = json.dumps(result["answer"], indent=2)
            print('\n\n')
            print('============================================== RESULT START ================================================')
            print('\n')
            print(json_data) 
            print('\n')
            print('============================================== RESULT END ==================================================')
            print('\n\n')
            print('Please type in the question: ')

if __name__ == "__main__":
    main()