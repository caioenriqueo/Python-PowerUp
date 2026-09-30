# Bibliotecas = pacotes de codigo
# pip install pyautogui

import pyautogui
import time

# pyautogui.click -> clica
# pyautogui.write -> escreve um texto
# pyautogui.press -> aperta uma tecla
# pyautogui.hotkey -> aperta um atalho (hotkey)
pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Passo a passo do seu programa
# Passo 1: Entrar no sistema da empresa
# Abriria o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")
# Fazer uma pausa maior pro site carregar
time.sleep(3) 

# Passo 2: Fazer Login
# Clicar no campo de email
pyautogui.click(x=803, y=372)
# Escrever seu email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # passar para o proximo campo
pyautogui.write("suasenhaminhasenha")
pyautogui.press("tab") # Passar para o botão
pyautogui.press("enter")
# Fazer uma pausa maior pro site carregar
time.sleep(4)

# Passo 3: Abrir a base de dados (importar o arquivo)
# pip install pandas openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index: 
    # Passo 4: Cadastrar o produto
    # Codigo
    pyautogui.click(x=709, y=259) # Clicar no campo do codigo
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab") # Passar para o proximo campo
    # Marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    # Tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    # Categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    # Preco
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    # Custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    # Obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab") # Passar para o botão enviar

    pyautogui.press("enter") # Clicou no botão enviar
    # Voltar para o inicio da tela
    pyautogui.scroll(5000)
# Passo 5: Repetir o passo 4 ate acabar a lista de produtos 

