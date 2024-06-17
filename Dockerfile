# Utilize uma imagem oficial do Python como imagem base
FROM python:3.8-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia o conteúdo do diretório atual para o diretório /app no contêiner
COPY . /app

# Instala as dependências necessárias especificadas no arquivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 5000 para ser acessível externamente
EXPOSE 5000

# Define variáveis de ambiente necessárias para rodar a aplicação Flask
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0

# Comando para iniciar a aplicação quando o contêiner é iniciado
CMD ["flask", "run"]
