import ctypes
import os
import random
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"
BASE = Path(__file__).resolve().parent.parent  / "assets"

#leitura do arquivo de frases
lines = []
with open(BASE / "frases.txt", "r", encoding="utf-8") as file:
    for line in file:
        lines.append(line.strip(";").replace(";", ""))
        nFrases = len(lines)

class classe_retorno():
    fechar = False
retorno = classe_retorno()

class classe_random():
    valor = random.randint(0, nFrases - 1)

random = classe_random()

def valor_random():
    return lines[random.valor]

def estudoClicado(e):
    
    #Processos encerrados
    os.system("taskkill /f /im steam.exe")
    os.system("taskkill /f /t /im RiotClientServices.exe")
    os.system("taskkill /f /t /im wallpaper32.exe")
    os.system("taskkill /f /t /im opera.exe")

    #Esconder ícones da área de trabalho
    os.system(f'"{ASSETS / "hide_icons.exe"}"')

    #Processos abertos
    os.system(r'start "" "caminho/do_seu_programa.exe"')

    #Definição do papel de parede
    ctypes.windll.user32.SystemParametersInfoW(20, 0, str(ASSETS / "black.png"), 0)
    
    retorno.fechar = True


def casualClicado(e):

    #Ícones da área de trabalho visíveis
    os.system(f'"{ASSETS / "unhide_icons.exe"}"')
    retorno.fechar = True


def arteClicado(e):
    
    #Processos encerrados
    os.system("taskkill /f /im steam.exe")
    os.system("taskkill /f /t /im RiotClientServices.exe")
    os.system("taskkill /f /t /im wallpaper32.exe")
    os.system("taskkill /f /t /im opera.exe.exe")

    #Esconder ícones da área de trabalho

    os.system(f'"{ASSETS / "hide_icons.exe"}"')
    
    #Processos abertos
    os.system(r'start "" "caminho/do_seu_programa.exe"')

    #Esconder ícones da área de trabalho
    os.system(f'"{ASSETS / "hide_icons.exe"}"')

    #Definição do papel de parede
    ctypes.windll.user32.SystemParametersInfoW(20, 0, str(ASSETS / "black.png"), 0)
    
    retorno.fechar = True