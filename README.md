1. **Pré-requisitos**
   - Ter o Python instalado (versão 3.11 ou superior)
   - Instalar as bibliotecas necessárias:
     ```bash
     pip install pandas pywhatkit
     ```

2. **Configuração**
   - Certifique-se de ter uma planilha `alunos.csv` no mesmo diretório do arquivo do código.
   - O arquivo deve conter as colunas:
     - `Número de Telefone`: os números com DDD da cidade (ex.: (11) 91234-5678).
   - Adicione o código do país e ajuste os números automaticamente ao executar o script.
   - Obtenha as Coordenadas do Mouse:
     - Execute o seguinte script em Python para descobrir as coordenadas do botão de envio no 
       WhatsApp Web:
        ```bash
        python
        import pyautogui
        print(pyautogui.position())
        ```
   - Com o terminal aberto e o script rodando, posicione o mouse sobre o botão de envio no 
     WhatsApp Web e anote os valores de X e Y exibidos no terminal.
   - Substitua os valores x=500 e y=800 no comando pyautogui.click(x=500, y=800) no código 
     principal pelo X e Y obtidos.
     
3. **Execução**
   - Para rodar o código, use o seguinte comando no terminal:
     ```bash
     python enviar_mensagens.py
     ```
