#Nossa primeira automação em python
#Escrever a lógica (passo a passo)
# 1-Instalar e Usar as bibliotecas
# 2- Iniciar a nossa automação
#    2.1- Replicar a tarefa do usuario  para cadastro
#    2.2 ler a base de dados
#    2.3 Fazer o cadastro de Aluno por Aluno

# Pandas biblioteca feita para analise de dados.
# pyautogui biblioteca que faz a automação.

import pandas as pd
import pyautogui
import time

pyautogui.PAUSE= 0.5
pyautogui.press('win')
pyautogui.write('Edge')
pyautogui.press('enter')

#entrar no link
pyautogui.write('http://www.sauer.pro.br/python/automacao/index.html')
pyautogui.press('enter')
time.sleep(5)

pyautogui.click(x=344, y=298)
pyautogui.write('admin')
pyautogui.press('tab')
pyautogui.write('SimplificaPython')
pyautogui.press('tab')
pyautogui.press('enter')
#importar a base de dados de alunos para cadastrar
dados = pd.read_csv('alunos.csv')
time.sleep(2)

for linha in dados.index:
    pyautogui.click(x=260, y=394)
    nome = dados.loc[linha, 'Nome']
    pyautogui.write(nome)
    pyautogui.press('tab')

    email= dados.loc[linha, 'Email']
    pyautogui.write(email)
    pyautogui.press('tab')

    endereco= dados.loc[linha, 'Endereco']
    pyautogui.write(endereco)
    pyautogui.press('tab')

    telefone= dados.loc[linha, 'Telefone']
    pyautogui.write(telefone)
    pyautogui.press('tab')

    pyautogui.press('enter')
    pyautogui.scroll(5000)




