import pytesseract
from spellchecker import SpellChecker
from pdf2image import convert_from_path
from PIL import Image

#configura o caminho do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Converte o PDF em Imagens
paginas = convert_from_path("intolerancia_religiosa-artigo-1.pdf", dpi=300, poppler_path=r"C:\poppler\Release-24.08.0-0\poppler-24.08.0\Library\bin")

#Inicializa o corretor ortográfico
corretor = SpellChecker(language='pt')

#Prepara o arquivo de saída
with open("texto_corrigido.txr", "w", encoding="utf-8") as arquivo_saida:
    for i, imagem in enumerate(paginas):
        #Extrai o texto com OCR
        texto = pytesseract.image_to_string(imagem, lang='por')

        #Aplica correção ortográfica
        palavras = texto.split()
        corrigidas = [corretor.correction(p) or p for p in palavras]
        texto_corrigido = " ".join(corrigidas)

        #Escreve no arquivo .txt
        arquivo_saida.write(f"--- Página {i+1} ---\n")
        arquivo_saida.write(texto_corrigido)
        arquivo_saida.write("\n" + "="*60 + "\n\n")
print("Texto extraído, corrigido e salvo em 'texto_corrigido.txt'.")
