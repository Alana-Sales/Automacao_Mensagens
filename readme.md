# 🤖 Automatizador de Mensagens no WhatsApp

Este repositório contém três scripts de automação para envio em massa de mensagens personalizadas via WhatsApp. Cada script apresenta características distintas em termos de performance, suporte a emojis, personalização e consumo de recursos da máquina.

## Requisitos

- Python 3.8+
- Google Chrome
- WhatsApp Web
- Bibliotecas:

```bash
pip install pandas pywhatkit pyautogui undetected-chromedriver selenium
```

## Formato do CSV (numeros.csv)
O arquivo .csv deve conter pelo menos a coluna com os números de telefone no seguinte formato:

```
Telefone,Nome
(85) 91234-5678,Ana
(11) 98765-4321,Bruno
```

## Scripts Disponíveis
1️. mensagens_pyautogui.py <br/>
```
Envia mensagens com emojis usando pywhatkit e cliques automatizados com pyautogui.
```

- Suporta emojis
- Congela o computador durante a execução
- Requer ajuste das coordenadas do mouse no pyautogui.click()
- Recomendado apenas para pequenos envios

2️. mensagens_selenium.py <br/>
```
Usa Selenium para envio sem bloquear o PC, mas não suporta emojis.
```

- Utilização do computador permitida durante execução
- Emojis não são renderizados corretamente
- Faz até 3 tentativas por número
- Mais estável que o primeiro script

3️. mensagens_personalizado_nome.py <br/>
```
Envia mensagens personalizadas com nome, com estrutura robusta e sem travar o computador.
```

- Permite personalização da mensagem por nome
- Possível utilizar o computador durante envio
- Usa Selenium com WebDriverWait para maior estabilidade
- Ideal para mensagens institucionais com cronograma, links, etc.

##  Como Usar
1. Clone o repositório:

```
git clone https://github.com/seu-usuario/automacoes-whatsapp.git
cd automacoes-whatsapp
```

2. Instale os requisitos:

```
pip install -r requirements.txt
```

3. Adicione os números no numeros.csv.
4. Execute o script desejado:

```
python mensageiro_personalizado_nome.py
```
5. Escaneie o QR code no navegador com o seu WhatsApp.

## Observações <br/>

- Certifique-se de manter o WhatsApp Web aberto e logado durante toda a execução.
- O WhatsApp pode bloquear envios em massa se detectar comportamento suspeito.
