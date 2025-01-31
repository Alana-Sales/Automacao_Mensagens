import undetected_chromedriver as uc  # Importa o undetected-chromedriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Caminho para o arquivo CSV
caminho_csv = "numeros - Página1.csv"

# Nome da coluna contendo os números de telefone
coluna_numeros = "Telefone"

# Lê os números do arquivo CSV
df = pd.read_csv(caminho_csv)

# Adiciona o código do país +55
def formatar_numero(numero):
    numero = str(numero).strip()
    if numero.startswith("("):
        numero = "+55" + numero.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    return numero

# Formatação dos números
df[coluna_numeros] = df[coluna_numeros].apply(formatar_numero)

# Mensagem a ser enviada
mensagem = """
Mensagem a ser enviada
"""

# Configuração do WebDriver com undetected-chromedriver
driver = uc.Chrome()  # Inicializa o ChromeDriver automaticamente

# Abre o WhatsApp Web
driver.get("https://web.whatsapp.com")

# Aguarda o usuário escanear o QR Code
input("Escaneie o QR Code e pressione Enter para continuar...")

# Lista para evitar duplicidade no envio
numeros_enviados = set()

# Envia a mensagem para cada número
for numero in df[coluna_numeros]:
    if numero not in numeros_enviados:
        try:
            print(f"Enviando mensagem para {numero}...")
            
            # Abre a conversa com o número
            driver.get(f"https://web.whatsapp.com/send?phone={numero}")
            
            # Aguarda o carregamento da página
            time.sleep(10)  # Ajuste o tempo conforme necessário
            
            # Localiza o campo de texto e envia a mensagem
            text_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            text_box.send_keys(mensagem)
            text_box.send_keys(Keys.ENTER)
            
            # Aguarda o envio da mensagem
            time.sleep(2)
            
            # Adiciona o número à lista de enviados
            numeros_enviados.add(numero)
            print(f"Mensagem enviada para {numero}")
        except Exception as e:
            print(f"Erro ao enviar para {numero}: {e}")

# Fecha o navegador
driver.quit()

print("Todas as mensagens foram enviadas!")

