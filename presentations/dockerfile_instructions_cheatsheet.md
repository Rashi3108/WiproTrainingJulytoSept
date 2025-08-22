# 🐳 Dockerfile Instructions Cheat Sheet

This guide explains the most common Dockerfile instructions with examples.

---

## 1. FROM
- **Purpose:** Sets the base image for your Dockerfile.
- **Example:**
```dockerfile
FROM nginx:alpine
```

---

## 2. LABEL
- **Purpose:** Add metadata to the image (author, description, version).
- **Example:**
```dockerfile
LABEL maintainer="yourname@example.com"
```

---

## 3. RUN
- **Purpose:** Execute commands during the image build.
- **Example:**
```dockerfile
RUN apt-get update && apt-get install -y curl
```

---

## 4. COPY vs ADD
- **COPY:** Copy files from host to container.
- **ADD:** Copy + supports remote URLs and archive extraction.

**Example:**
```dockerfile
COPY index.html /usr/share/nginx/html/
```

---

## 5. WORKDIR
- **Purpose:** Set the working directory inside the container.
- **Example:**
```dockerfile
WORKDIR /app
```

---

## 6. EXPOSE
- **Purpose:** Document the port the container will listen on.
- **Example:**
```dockerfile
EXPOSE 80
```

---

## 7. CMD
- **Purpose:** Default command to run when the container starts.
- **Example:**
```dockerfile
CMD ["nginx", "-g", "daemon off;"]
```

---

## 8. ENTRYPOINT
- **Purpose:** Define a fixed command that cannot be easily overridden.
- **Example:**
```dockerfile
ENTRYPOINT ["echo"]
CMD ["Hello World"]
```
👉 Running this container will output: `Hello World`

---

## 9. ENV
- **Purpose:** Set environment variables inside the container.
- **Example:**
```dockerfile
ENV APP_ENV=production
```

---

## 10. VOLUME
- **Purpose:** Create a mount point for persistent data.
- **Example:**
```dockerfile
VOLUME /data
```

---

## 11. USER
- **Purpose:** Set the user that runs inside the container.
- **Example:**
```dockerfile
USER appuser
```

---

# ✅ Quick Analogy
Think of a Dockerfile like a **recipe**:

- **FROM** → Base ingredient  
- **RUN** → Cooking steps  
- **COPY/ADD** → Add spices/files  
- **EXPOSE** → Tell others which port to use  
- **CMD/ENTRYPOINT** → How to serve the dish  

---

# Example: Custom Nginx Dockerfile
```dockerfile
FROM nginx:alpine
RUN rm -rf /usr/share/nginx/html/*
COPY index.html /usr/share/nginx/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

---
