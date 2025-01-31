1. **Pré-requisitos**
   - Ter o Python instalado (versão 3.11 ou superior)
   - Instalar as bibliotecas necessárias:
     ```bash
     pip install undetected-chromedriver selenium pandas
     ```

2. **Configuração**
   - Certifique-se de ter uma planilha `alunos.csv` no mesmo diretório do arquivo do código.
   - O arquivo deve conter as colunas:
     - `Número de Telefone`: os números com DDD da cidade (ex.: (11) 91234-5678).
   - Obtenha as Coordenadas do Mouse:
     - Abra o interpretador Python no terminal ou no IDLE:
        - No terminal ou prompt de comando, digite python e pressione Enter.
        - Isso abrirá o interpretador interativo do Python.
     - Cole e execute o seguinte script no interpretador:
        ```bash
        import pyautogui
        print(pyautogui.position())
        ```
   - Edite a variável mensagem no script para alterar o conteúdo da mensagem enviada:
     ```bash
     mensagem = """
     Olá, esta é uma mensagem automática.
     """
     ```

3. **Execução**
   - Para rodar o código, use o seguinte comando no terminal:
     ```bash
     python enviar_mensagens.py
     ```

❓ Dúvidas Frequentes
1. Posso usar outro navegador?
Não, o script foi desenvolvido para funcionar com o Google Chrome.

2. O script funciona no WhatsApp Desktop?
Não, este script foi desenvolvido para o WhatsApp Web. Para o WhatsApp Desktop, seria necessário usar uma abordagem diferente (como automação de interface gráfica).

3. Posso enviar imagens ou arquivos?
Sim, mas isso requer modificações no script. Entre em contato com o desenvolvedor para mais detalhes.
