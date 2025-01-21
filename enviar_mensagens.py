import pywhatkit as kit
import pandas as pd
import pyautogui
import time

# Caminho para o arquivo CSV
caminho_csv = "numeros.csv"

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
🛳️ *Fala, futuro(a) Embarcatecher!* 🚀
Você está quase lá! Faltam só uns cliques e um pouquinho de dedicação para concluir as atividades da plataforma MOODLE e cruzar a linha de chegada do *curso Embarcatech.* 🎓
Pensa em tudo que você já aprendeu e nas portas que estão se abrindo com esse conhecimento. Agora é hora de dar aquele gás final, porque o sabor da vitória é ainda melhor quando sabemos que demos nosso melhor até o fim. 💪✨
*Bora fazer acontecer?* Finalize suas tarefas, mande bem e celebre o resultado! Lembre-se: cada passo te aproxima do sucesso que você merece.
*Estamos torcendo por você!* 🥳
"""

# Lista para evitar duplicidade no envio
numeros_enviados = set()

# Envia a mensagem para cada número
for numero in df[coluna_numeros]:
    if numero not in numeros_enviados:
        try:
            print(f"Enviando mensagem para {numero}...")
            
            # Envia a mensagem
            kit.sendwhatmsg_instantly(numero, mensagem, wait_time=4, tab_close=False)  # Mantém a aba aberta
            
            # Aguarda alguns segundos para o carregamento
            time.sleep(4)

            # Simula um clique no botão de enviar
            pyautogui.click(x=4643, y=1209)  # Ajuste as coordenadas conforme necessário
            
            # Aguarda o envio da mensagem
            time.sleep(2)

            # Tenta fechar a aba
            pyautogui.hotkey("ctrl", "w")
            
            # Aguarda 1 segundo e confirma o fechamento, caso o pop-up apareça
            time.sleep(2)
            pyautogui.press("enter")  # Simula o "Enter" para confirmar
            
            # Adiciona o número à lista de enviados
            numeros_enviados.add(numero)
            print(f"Mensagem enviada para {numero}")
        except Exception as e:
            print(f"Erro ao enviar para {numero}: {e}")

print("Todas as mensagens foram enviadas!")
