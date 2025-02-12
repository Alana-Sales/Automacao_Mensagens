# Envio de mensagens sem emoji com selenium

import undetected_chromedriver as uc 
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

caminho_csv = "numeros.csv"
coluna_numeros = "Telefone"

df = pd.read_csv(caminho_csv)
def formatar_numero(numero):
    numero = str(numero).strip()
    if numero.startswith("("):
        numero = "+55" + numero.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    return numero
df[coluna_numeros] = df[coluna_numeros].apply(formatar_numero)

mensagem = """
Mensagem a ser enviada
"""

driver = uc.Chrome()
driver.get("https://web.whatsapp.com")
input("Escaneie o QR Code e pressione Enter para continuar...")

numeros_enviados = set() # Evita duplicidade no envio
for numero in df[coluna_numeros]:
    if numero not in numeros_enviados:
        try:
            print(f"Enviando mensagem para {numero}...")
            driver.get(f"https://web.whatsapp.com/send?phone={numero}")
            time.sleep(10)
            text_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            text_box.send_keys(mensagem)
            text_box.send_keys(Keys.ENTER)
            time.sleep(2)
            numeros_enviados.add(numero)
            print(f"Mensagem enviada para {numero}")
        except Exception as e:
            print(f"Erro ao enviar para {numero}: {e}")
driver.quit()

print("Todas as mensagens foram enviadas!")
