# Ansible Setup and Apache Installation Guide

This guide explains how to set up **Ansible** on an EC2 controller instance, copy your `.pem` key from your local machine (Windows/Mac) to the controller, configure the inventory, test connectivity, and run a playbook to install Apache on a managed EC2 instance.

---

## 1. Install Ansible on Controller EC2

Login to your **Ansible Controller EC2** instance and run:

```bash
sudo apt update -y
sudo apt install software-properties-common -y
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install ansible -y

# Verify installation
ansible --version
```

---

## 2. Copy `.pem` File to Controller EC2

### 🔹 On **Mac/Linux**

From your **local machine**, run:

```bash
scp -i ~/.ssh/YourKey.pem ~/.ssh/YourKey.pem ubuntu@<controller-ec2-public-ip>:~/.ssh/
```

### 🔹 On **Windows (PowerShell)**

If you are using PowerShell, run:

```powershell
scp -i C:\Users\YourUser\Downloads\YourKey.pem C:\Users\YourUser\Downloads\YourKey.pem ubuntu@<controller-ec2-public-ip>:~/.ssh/
```

After copying, SSH into your **controller EC2** and set correct permissions:

```bash
ssh -i ~/.ssh/YourKey.pem ubuntu@<controller-ec2-public-ip>
chmod 600 ~/.ssh/YourKey.pem
```

---

## 3. Configure Inventory File

On the **controller EC2**, edit the inventory file:

```bash
sudo nano /etc/ansible/hosts
```

Add the managed EC2 details:

```ini
[webservers]
<managed-ec2-public-ip> ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/YourKey.pem
```

---

## 4. Test Ansible Connection

Run:

```bash
ansible webservers -m ping
```

Expected output:

```json
<managed-ec2-public-ip> | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

---

## 5. Create Ansible Playbook for Apache

Create a file `apache.yml`:

```yaml
---
- name: Install and start Apache on Ubuntu EC2
  hosts: webservers
  become: yes

  tasks:
    - name: Update apt cache
      apt:
        update_cache: yes

    - name: Install Apache2
      apt:
        name: apache2
        state: present

    - name: Ensure Apache is running
      service:
        name: apache2
        state: started
        enabled: yes
```

---

## 6. Run the Playbook

Execute:

```bash
ansible-playbook -i /etc/ansible/hosts apache.yml
```

---

## 7. Verify Apache Installation

Open your browser and visit:

```
http://<managed-ec2-public-ip>/
```

You should see the **Apache2 Ubuntu Default Page** 🎉
