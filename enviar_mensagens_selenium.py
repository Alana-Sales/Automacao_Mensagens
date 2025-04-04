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
*Mensagem teste*
"""

driver = uc.Chrome()
driver.get("https://web.whatsapp.com")
input("Escaneie o QR Code e pressione Enter para continuar...")

numeros_enviados = set()
tentativas_erro = {}
numeros_falharam = set()

def enviar_mensagem(numero):
    try:
        print(f"Tentando enviar mensagem para {numero}...")
        driver.get(f"https://web.whatsapp.com/send?phone={numero}")
        time.sleep(11)

        text_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')

        for linha in mensagem.strip().split("\n"):
            text_box.send_keys(linha)
            text_box.send_keys(Keys.SHIFT + Keys.ENTER)
            time.sleep(0.3)

        text_box.send_keys(Keys.ENTER)
        time.sleep(2)

        numeros_enviados.add(numero)
        print(f"✅ Mensagem enviada para {numero}")
        return True

    except Exception as e:
        print(f"❌ Erro ao enviar para {numero}: {e}")
        return False

for numero in df[coluna_numeros]:
    if numero not in numeros_enviados:
        sucesso = enviar_mensagem(numero)
        if not sucesso:
            tentativas_erro[numero] = 1

print("\n🔁 Iniciando reenvio para números que falharam...")
while True:
    pendentes = [n for n in tentativas_erro if tentativas_erro[n] < 3 and n not in numeros_enviados]
    if not pendentes:
        break

    for numero in pendentes:
        sucesso = enviar_mensagem(numero)
        if sucesso:
            continue
        tentativas_erro[numero] += 1
        if tentativas_erro[numero] >= 3:
            numeros_falharam.add(numero)

if numeros_falharam:
    print("\n⚠️ Os seguintes números falharam após 3 tentativas:")
    for numero in numeros_falharam:
        print(f"{numero}")
else:
    print("\n🎉 Todas as mensagens foram enviadas com sucesso!")

driver.quit()
