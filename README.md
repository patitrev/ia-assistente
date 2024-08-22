# Projeto de Residencia em TIC UNOESC-BRISA Turma 2

Desenvolvimento de uma IA para a empresa Dotse Software Engeneering,
para adicionar valor aos seus produtos.

Esse respositírio terá como fim registrar tudo que for desenvolvido e tratado entre bolsistas, supervisores e empresa. 
Bem como registros de reuniões, projeto e código do projeto.

Passo a passo para rodar a aplicação:

========
1º Passo
========
	- Por primeiro, precisará declarar a sua Chave API como uma variável ambiente na sua máquina:

		-------------------------------
		Nome da Variável: OPEN_API_KEY
		-------------------------------

		-------------------------------------------------------------------------------------------------------------------
		Valor da variável: Aqui vai uma chave gerada na API da OpenAI
		-------------------------------------------------------------------------------------------------------------------

========
2º Passo
========
	- Abrirá o o projeto em seu VSCode. Assim que abri-lo, irá abrir um novo terminal no prórpio VSCode e digitará o seguinte comando:
	  
	  -------------------------------
	  pip install -r requirements.txt
	  -------------------------------

	- Após digitar esse comando, ele irá instalar todas as bibliotecas necessárias, para que seu código funcione corretamente em sua máquina.

========
3º Passo
========
	- Após o 2º passo, você digitará o seguinte comando no terminal do VSCode:

	----------------------
	streamlit run app22.py
	----------------------
	
	- Esse comando iniciará uma tela em HTML (localhost) para que você possa subir PDFs e fazer perguntas.

========
4º Passo
========
	- Suba um PDF ao site, para que ele possa ler. Após isso, pode fazer qualquer pergunta referente a esse PDF, que ele responderá com êxito.

	- OBS: Quanto mais formatado o PDF for, mais coerente será a resposta do assistente.
