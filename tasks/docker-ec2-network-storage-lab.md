
# Docker Lab on EC2: Bridge + Host Networks with Named Volumes (Nginx + phpMyAdmin + MySQL)

This hands-on lab is designed for **Ubuntu EC2 instances** with Docker installed.  
We will:
- Run **MySQL** on a user-defined bridge network with a **named volume** for persistence.
- Run **phpMyAdmin** on the bridge network for DB management (with login screen).
- Run **Nginx** on the **host network** to directly expose phpMyAdmin on port 80 of the EC2 instance.
- Verify **data persistence** across container restarts.

---

## 🔹 0) Prerequisites
1. An **Ubuntu EC2 instance** with Docker installed:
   ```bash
   sudo apt update -y
   sudo apt install -y docker.io
   sudo usermod -aG docker ubuntu
   newgrp docker
   ```

2. Ensure the EC2 **Security Group** allows:
   - **TCP 22** (SSH)
   - **TCP 80** (Nginx host network)
   - **TCP 8081** (phpMyAdmin test access)

---

## 🔹 1) Create a user-defined bridge network
```bash
docker network create app_net
docker network ls | grep app_net
```

---

## 🔹 2) Create a named volume for MySQL data
```bash
docker volume create mysql_data
docker volume ls | grep mysql_data
```

---

## 🔹 3) Run MySQL with bridge network + named volume
```bash
export MYSQL_ROOT_PASSWORD='MyS3cret!42'

docker run -d --name mysql8   --network app_net   -e MYSQL_ROOT_PASSWORD="${MYSQL_ROOT_PASSWORD}"   -v mysql_data:/var/lib/mysql   mysql:8.0
```

Check logs until `ready for connections` appears:
```bash
docker logs -f mysql8
```

---

## 🔹 4) Run phpMyAdmin on the bridge network (with login screen)
We will **not** pass username/password env vars, so phpMyAdmin will prompt for login.

```bash
docker run -d --name phpmyadmin   --network app_net   -e PMA_HOST=mysql8   -p 8081:80   phpmyadmin:5-apache
```

Test from EC2:
```bash
curl -I http://localhost:8081/
```

Also test from browser: **http://<EC2-Public-IP>:8081**  
You should now see the **phpMyAdmin login page**.

Login with:
- **User:** root  
- **Password:** MyS3cret!42  

---

## 🔹 5) Configure Nginx as reverse proxy on host network
Create `nginx-host.conf`:
```bash
cat > nginx-host.conf <<'NGINX'
events {}
http {
  server {
    listen 80;
    location / {
      proxy_pass http://127.0.0.1:8081;
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header X-Forwarded-Proto $scheme;
    }
  }
}
NGINX
```

Run Nginx container on host network:
```bash
docker run -d --name nginx_host   --network host   -v "$(pwd)/nginx-host.conf:/etc/nginx/nginx.conf:ro"   nginx:alpine
```

---

## 🔹 6) Test the setup
Open browser → **http://<EC2-Public-IP>/**  
You should see phpMyAdmin login page.  
Login with:
- **User:** root  
- **Password:** MyS3cret!42  

---

## 🔹 7) Insert and verify persistent data
1. Inside phpMyAdmin, create a new database `labdb`.  
2. Inside `labdb`, create a new table `note` with:  
   - Column `id` (INT, Primary key)  
   - Column `msg` (VARCHAR(64))  

3. Insert a row into the table:  
   - `id = 1`  
   - `msg = persists via named volume`  

4. Confirm the row appears in phpMyAdmin when you **browse the table**.

---

## 🔹 8) Restart MySQL container to test persistence
Stop and remove MySQL container but **do not delete the volume**:
```bash
docker stop mysql8 && docker rm mysql8

docker run -d --name mysql8   --network app_net   -e MYSQL_ROOT_PASSWORD="${MYSQL_ROOT_PASSWORD}"   -v mysql_data:/var/lib/mysql   mysql:8.0
```

Now refresh phpMyAdmin, browse the `labdb.note` table again.  
✅ You should still see the row:  
```
1 | persists via named volume
```  

This proves the data persisted because of the **named volume**.

---

## 🔹 9) Cleanup
```bash
docker stop phpmyadmin nginx_host mysql8
docker rm phpmyadmin nginx_host mysql8
docker network rm app_net
docker volume rm mysql_data
```

---

## ✅ What you learned
- **Bridge network** for inter-container communication.  
- **Host network** for direct port exposure (Nginx on EC2 public IP).  
- **Named volume** for persistent database data.  
- How to manually confirm persistence by creating and verifying a row in MySQL (`labdb.note`).
