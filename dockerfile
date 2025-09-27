# Imagen base oficial de Python
FROM python:3.12-slim

# Definir directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar requirements primero (mejora el cacheo de capas)
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Exponer el puerto que usa Uvicorn
EXPOSE 8000

# Comando para arrancar la app
CMD ["uvicorn", "ms_productos.main:app", "--host", "0.0.0.0", "--port", "8000"]
