# Apenas para envio de mensagens com emojis. 
# Congela o PC devido ao uso do pyautogui para automação de cliques.

import pywhatkit as kit
import pandas as pd
import pyautogui
import time

caminho_csv = "numeros.csv" # Planilha com números
coluna_numeros = "Telefone"

df = pd.read_csv(caminho_csv)
def formatar_numero(numero):
    numero = str(numero).strip()
    numero = numero.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    if numero.startswith("+55"):
        numero = numero[3:]
    
    return numero
df[coluna_numeros] = df[coluna_numeros].apply(formatar_numero)

mensagem = """
🚀 Mensagem
"""

numeros_enviados = set()
for numero in df[coluna_numeros]:
    if numero not in numeros_enviados:
        try:
            print(f"Enviando mensagem para {numero}...")
            kit.sendwhatmsg_instantly(f"+55{numero}", mensagem, wait_time=5, tab_close=False)
            time.sleep(4)
            pyautogui.click(x=4641, y=1204) # Ajuste as coordenadas conforme necessário
            time.sleep(2)
            pyautogui.hotkey("ctrl", "w")
            time.sleep(1)
            pyautogui.press("enter")
            numeros_enviados.add(numero)
            print(f"Mensagem enviada para {numero}")
        except Exception as e:
            print(f"Erro ao enviar para {numero}: {e}")

print("Todas as mensagens foram enviadas!")
