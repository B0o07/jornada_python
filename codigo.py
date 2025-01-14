# pip install pyautogui
# pyautogui.click -> clicar
# pyautogui.press -> pressionar uma tecla
# pyautogui.write -> escrever
# pyautogui.hotkey -> atalho de teclado ("ctrl", "c")

# Passo 1: Abrir o sistema da empresa
#   Sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 2

# Apertar tecla Windows
pyautogui.press("win")

# Escrever Chrome
pyautogui.write("chrome")

# Apertar Enter
pyautogui.press("enter")

# Entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Pedir para o computador esperar 3 segundos
time.sleep(3)

# Passo 2: Fazer loginplayssaulo@gmail.com  S@ul1nh0
pyautogui.click(x=2757, y=408)
pyautogui.write("playssaulo@gmail.com")
pyautogui.press("tab")
pyautogui.write("TakeMyLifeInToPieces")
pyautogui.press("enter")

# Passo 3: Importar a base de dados dos proutos
# pip install pandas openpyxl
tabela = pd.read_csv("produtos.csv")

print(tabela)

time.sleep(2)

# Passo 4:      
# Cadastrar 1 produto


for linha in tabela.index:

    pyautogui.click(x=2747, y=292)

    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("enter")

    pyautogui.scroll(10000)

# Passo 5: Repetir o passo 4 até acabar todos os produtos

