# Usar uma imagem oficial do Python como base
FROM python:3.9-slim

# Definir variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && \
    apt-get -y install nginx && \
    apt-get clean

# Remover configuração padrão do Nginx
RUN rm /etc/nginx/sites-enabled/default

# Instalar dependências do Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o projeto para o diretório de trabalho
COPY . /app/

# Coletar arquivos estáticos
RUN python manage.py collectstatic --noinput

# Configurar o Nginx
COPY ./nginx.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled

# Expor a porta 80 para o Nginx e a porta 8000 para o Gunicorn
EXPOSE 80 8000

# Definir o comando para iniciar o Nginx e o Gunicorn
CMD ["sh", "-c", "service nginx start && gunicorn Job_Project.wsgi:application --bind 0.0.0.0:8000"]
