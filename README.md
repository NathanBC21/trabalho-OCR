Descrição do Processo de Desenvolvimento

Primeiramente Importar as bibliotecas "pytesseract" e "spellchecker"

	import pytesseract

	from spellchecker import SpellChecker

	from pdf2image import convert_from_path

	from PIL import Image

Em seguida, é preciso configurar o caminho em que o Tesseract se encontra no Windows.
Exemplo:

  	pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

Agora precisamos transformar o PDF em imagens utilizando o pdf2image, pois o pytesseract só trabalha com imagens

	paginas = convert_from_path("intolerancia_religiosa-artigo-1.pdf", dpi=300, poppler_path=r"C:\poppler\Release-24.08.0-0\poppler-24.08.0\Library\bin")
 
Obs: poppler_path é um conjunto de ferramentas que o pdf2image utiliza para converter PDFs em imagens. É necessário instalar ele caso não tenha instalado


Após feito tudo isso, temos que inicializar o corretor automático, utilizando o SpellChecker

	corretor = SpellChecker(language='pt')
 
Então preparamos o arquivo de saída

	with open("texto_corrigido.txr", "w", encoding="utf-8") as arquivo_saida:
 
   		for i, imagem in enumerate(paginas):
     
        		#Extrai o texto com OCR
	  
        		texto = pytesseract.image_to_string(imagem, lang='por')

Aplicamos a correção ortográfica

	palavras = texto.split()

        corrigidas = [corretor.correction(p) or p for p in palavras]
	
        texto_corrigido = " ".join(corrigidas)

E por fim, escrevemos no arquivo .txt

        	arquivo_saida.write(f"--- Página {i+1} ---\n")
	
        	arquivo_saida.write(texto_corrigido)
	
        	arquivo_saida.write("\n" + "="*60 + "\n\n")
	
	print("Texto extraído, corrigido e salvo em 'texto_corrigido.txt'.")
 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Como Executar o Programa

Passo 1: Baixe o código fonte em seu computador

Passo 2: Abra ele em uma IDE que suporte a linguagem Python

Passo 3: Instale as bibliotecas "pytesseract" e "spellchecker"

	‘pip install pytesseract pdf2image pillow’

	‘pip install pyspellchecker’

Passo 4: Instalar o poppler, caso não o tenha instalado em sua máquina

	https://github.com/oschwartz10612/poppler-windows/releases/

Passo 5: Pegue um arquivo em PDF de sua preferência e jogue-o dentro da pasta do projeto.

Passo 6: informe o caminho do seu PDF (pdf_path) na seguinte linha:

	paginas = convert_from_path("SEU PDF AQUI.pdf", dpi=300, poppler_path=r"C:\poppler\Release-24.08.0-0\poppler-24.08.0\Library\bin")
 
Passo 7: Se for necessário, coloque também o caminho em que está instalado o seu poppler

	paginas = convert_from_path("SEU PDF AQUI.pdf", dpi=300, poppler_path=r"CAMINHO DO POPPLER ")
 
Passo 8: Execute o código fonte.
