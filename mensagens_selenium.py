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
*Revisaê! Hoje tem encontro online sobre Raciocínio Lógico* – bora fortalecer seus conhecimentos e avançar no Capacita Brasil!

Nesta quarta-feira (7/5), às 19h, continuamos nossa revisão guiada – uma oportunidade perfeita para revisar o conteúdo, resolver qualquer pendência da Fase 1 e seguir firme na sua jornada no Programa. 
Conecte-se, participe ativamente, tire suas dúvidas e garanta mais um passo rumo à sua evolução! 

*Clique no link e participe:* meet.google.com/hmg-sndh-ebx
"""

driver = uc.Chrome()
driver.get("https://web.whatsapp.com")
input("Escaneie o QR Code e pressione Enter para continuar...")

numeros_enviados = set()

for numero in df[coluna_numeros]:
    if numero not in numeros_enviados:
        try:
            print(f"Enviando mensagem para {numero}...")
            driver.get(f"https://web.whatsapp.com/send?phone={numero}")
            time.sleep(11)

            text_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')

            for linha in mensagem.split("\n"):
                text_box.send_keys(linha)
                text_box.send_keys(Keys.SHIFT + Keys.ENTER)
                time.sleep(0.3)

            text_box.send_keys(Keys.ENTER) 
            time.sleep(2)

            numeros_enviados.add(numero)
            print(f"Mensagem enviada para {numero}")

        except Exception as e:
            print(f"Erro ao enviar para {numero}: {e}")

driver.quit()
print("Todas as mensagens foram enviadas!")
