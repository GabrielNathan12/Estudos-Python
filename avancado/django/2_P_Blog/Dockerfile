# Use uma imagem base do Linux
FROM python:3.10.13-slim-bookworm

LABEL maintainer="gabrielnathanmiw@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1

# Define que a saída do Python será exibida imediatamente no console ou em 
# outros dispositivos de saída, sem ser armazenada em buffer.
# Em resumo, você verá os outputs do Python em tempo real.
ENV PYTHONUNBUFFERED 1

# Atualizar o sistema e instalar dependências
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    gettext \
    postgresql-client

# Criar e definir o diretório de trabalho
WORKDIR /app

# Copiar e instalar requisitos
COPY app/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código do aplicativo para o contêiner
COPY . /app/

# Executar comando padrão
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]