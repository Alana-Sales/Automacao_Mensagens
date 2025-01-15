import pywhatkit as kit
import pandas as pd
import time

caminho_csv = "numeros.csv"  # Substitua pelo caminho correto do seu arquivo CSV

coluna_numeros = "Telefone"  # Substitua se necessário
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
Mensagem que precisa ser enviada 
"""
numeros_enviados = set()

for numero in df[coluna_numeros]:
    if numero not in numeros_enviados:
        try:
            print(f"Enviando mensagem para {numero}...")
            kit.sendwhatmsg_instantly(numero, mensagem, wait_time=6, tab_close=True)  # Tempo em que a aba ficará aberta 
            time.sleep(1)  # Pausa após o fechamento da aba
            numeros_enviados.add(numero)  # Adiciona o número à lista de enviados
            print(f"Mensagem enviada para {numero}")
        except Exception as e:
            print(f"Erro ao enviar para {numero}: {e}")

print("Todas as mensagens foram enviadas!")
