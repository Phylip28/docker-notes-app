# Imagen base
FROM python:3.12-slim

# Directorio de trabajo
WORKDIR /app

# Archivos necesarios
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ ./app/

# Exponer el puerto
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app/main.py"]
