# Usar uma imagem oficial do Python como base
FROM python:3.9-slim

# Definir variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean

# Copiar e instalar dependências do Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o projeto para o diretório de trabalho
COPY . /app/

# Coletar arquivos estáticos
RUN python manage.py collectstatic --noinput

# Remover a configuração padrão do Nginx e adicionar a personalizada
RUN rm /etc/nginx/sites-enabled/default
COPY nginx.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/

# Expor a porta 80 para o Nginx
EXPOSE 80

# Iniciar o Nginx e o Gunicorn
CMD service nginx start && gunicorn Job_Project.wsgi:application --bind 0.0.0.0:8000

