# Jenkins & SonarQube Installation Guide on Ubuntu EC2

## 1. Prerequisites

- AWS EC2 Instance running Ubuntu (t2.medium or larger for SonarQube to avoid memory errors)
- Security Group: Open ports **8080** (Jenkins) and **9000** (SonarQube)
- SSH access to the instance

---

## 2. Install Jenkins on Ubuntu EC2

### Step 1: Update System

```bash
sudo apt update && sudo apt upgrade -y
```

### Step 2: Install Java (Required by Jenkins)

```bash
sudo apt install openjdk-17-jdk -y
java -version
```

### Step 3: Add Jenkins Repository & Install

```bash
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb https://pkg.jenkins.io/debian binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update
sudo apt install jenkins -y
```

### Step 4: Start & Enable Jenkins

```bash
sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins
```

### Step 5: Access Jenkins

- Open browser: `http://<EC2-Public-IP>:8080`
- Get initial admin password:

```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

- Follow on-screen setup wizard.

---

## 3. Install SonarQube on Ubuntu EC2 (Docker Method)

### Step 1: Install Docker

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install docker.io -y
sudo systemctl enable docker
sudo systemctl start docker
```

### Step 2: Run SonarQube Container

```bash
sudo docker run -d --name sonarqube \
  -p 9000:9000 \
  -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true \
  sonarqube:9.9-community
```

### Step 3: Check Logs

```bash
sudo docker logs -f sonarqube
```

Wait until "SonarQube is up" appears.

### Step 4: Access SonarQube

- Open browser: `http://<EC2-Public-IP>:9000`
- Login:

```
Username: admin
Password: admin
```

- Change password on first login.

---

## 4. Notes

- Always use t2.medium or larger for SonarQube to avoid memory errors.

