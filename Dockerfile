# Imagem base leve e oficial do Python 3.11
FROM python:3.11-slim

# Define a pasta central de operações dentro do container
WORKDIR /app

# Garante o buffer imediato de logs e impressões do Python no terminal
ENV PYTHONUNBUFFERED=1

# Injeta o código local no container
COPY src/ /app/src/

# Gatilho que dispara a execução da aplicação
CMD ["python", "src/main.py"]
