import undetected_chromedriver as uc
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

caminho_csv = "numeros.csv"
coluna_numeros = "Telefone"
coluna_nome = "Nome"

df = pd.read_csv(caminho_csv)

def formatar_numero(numero):
    numero = str(numero).strip()
    if not numero.startswith("+55"):
        numero = "+55" + numero.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    return numero

df[coluna_numeros] = df[coluna_numeros].apply(formatar_numero)

mensagem_base = """Olá {nome},

Me chamo Alana, sou do Capacita Brasil! Estou entrando em contato porque nosso sistema consta pendência na Fase 1. *Falta bem pouquinho para você concluir essa etapa — e quero te lembrar que estamos aqui pra te ajudar!*

Chegou a hora de acelerar nos estudos e finalizar essa fase com tudo! Está rolando o Revisaê — revisões guiadas no Google Meet — sempre às terças e quartas, das 19h às 20h. Você pode conferir tudo o que já aconteceu na playlist do YouTube https://www.youtube.com/playlist?list=PLNFOlu9HdVvsBN9lvOzgCy88EGo57vbx5 e já se organizar para os próximos encontros.

{aluno}, essa é a hora certa pra tirar dúvidas e concluir os minicursos da Fase 1 do Capacita Brasil – Ciclo 2. Confira o cronograma das revisões:
- Raciocínio Lógico – 13/5 (terça)
Projeto de Vida – 14/5 (quarta)
Empreendedorismo – 20/5 (terça)
Inglês para Profissionais de TIC – 21/5 (quarta)


*Importante: finalize a Fase 1 até 25 de maio e siga em dia com sua trilha da Fase 2.* Concluindo tudo dentro do prazo, você ainda pode receber uma bolsa de R$117 por 3 meses! Todos os quizzes já estão disponíveis no Moodle: https://ead.ifce.edu.br

*Qualquer dúvida, é só responder esta mensagem! Estamos juntos nessa.*
"""

driver = uc.Chrome()
driver.get("https://web.whatsapp.com")
input("Escaneie o QR Code e pressione Enter para continuar...")

wait = WebDriverWait(driver, 30)
numeros_enviados = set()

for _, linha in df.iterrows():
    numero = linha[coluna_numeros]
    nome = linha[coluna_nome].strip().split()[0] 

    if numero not in numeros_enviados:
        try:
            print(f"Enviando mensagem para {nome} ({numero})...")
            driver.get(f"https://web.whatsapp.com/send?phone={numero}")
            time.sleep(10)

            text_box = wait.until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
            )

            mensagem = mensagem_base.format(nome=nome, aluno=nome).strip().split("\n")

            for linha_mensagem in mensagem:
                text_box.send_keys(linha_mensagem)
                text_box.send_keys(Keys.SHIFT, Keys.ENTER)
                time.sleep(0.2)

            # Agora sim envia a mensagem inteira
            text_box.send_keys(Keys.ENTER)
            time.sleep(5)

            numeros_enviados.add(numero)
            print(f"Mensagem enviada para {nome}")

        except Exception as e:
            print(f"Erro ao enviar para {numero}: {e}")

driver.quit()
print("Todas as mensagens foram enviadas!")
