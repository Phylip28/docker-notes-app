# Docker Notes App

Una pequeña aplicación de notas contruida con flask y python y empacada con Docker.

## Caracteristicas

- Interfaz web simple para escribir notas
- Las notas se almacenan automaticamente en un archivo `notes.txt`
- Persistecia con volumenes para mantener los datos aun cuando se detiene/reinicia el contenedor

## Requisitos

- [Docker](https://www.docker.com/) instalado

## Como correr la app

### 1. Construir la imagen

```bash
docker buildx build -t docker-notes-app .
```

### 2. Crear el volumen para la persistencia

```bash
mkdir -p ~/docker/bind-volumes/notes-data
```

>**Nota:** Puedes cambiar la ruta del volumen a gusto, pero recuerda colocar la ruta que elegiste en el siguiente paso.

### 3. Crear y ejecutar el contenedor

```bash
docker run -d --name notes-container -p 5000:5000 -v ~/docker/bind-volumes/notes-data:/app/data docker-notes-app
```

### 4. Accede desde tu navegador a 

```bash
http://localhost:5000
```

