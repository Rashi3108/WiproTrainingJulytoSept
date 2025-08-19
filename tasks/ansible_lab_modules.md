
# Ansible Lab Guide: Testing Common Modules on EC2 Ubuntu

This lab will help you practice Ansible modules on **two EC2 Ubuntu machines**:  
- **Controller EC2** → where Ansible is installed  
- **Managed EC2** → where tasks will be executed  

---

## 1. Pre-requisites

1. Ensure Ansible is installed on **controller EC2**:

```bash
sudo apt update -y
sudo apt install ansible -y
```

2. Copy your `.pem` key to controller EC2 (from local machine):

**On Mac/Linux:**

```bash
scp -i ~/.ssh/YourKey.pem ~/.ssh/YourKey.pem ubuntu@<controller-ec2-ip>:~/.ssh/
```

**On Windows PowerShell:**

```powershell
scp -i C:\Users\YourUser\Downloads\YourKey.pem C:\Users\YourUser\Downloads\YourKey.pem ubuntu@<controller-ec2-ip>:~/.ssh/
```

3. Set permissions on controller EC2:

```bash
chmod 600 ~/.ssh/YourKey.pem
```

4. Configure inventory (`/etc/ansible/hosts`):

```ini
[webservers]
ansible_host=<managed-ec2-public-ip> ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/YourKey.pem
```

5. Test connection:

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

## 2. Lab Exercises – Common Ansible Modules

### 🔹 APT Module (Install Packages)

Create `install_git.yml`:

```yaml
---
- name: Install Git on managed EC2
  hosts: webservers
  become: yes

  tasks:
    - name: Install Git
      apt:
        name: git
        state: present
        update_cache: yes
```

Run:

```bash
ansible-playbook install_git.yml
```

---

### 🔹 SERVICE Module (Manage Services)

Create `apache_service.yml`:

```yaml
---
- name: Ensure Apache is running
  hosts: webservers
  become: yes

  tasks:
    - name: Start Apache service
      service:
        name: apache2
        state: started
        enabled: yes
```

---

### 🔹 COPY Module (Copy Files)

Create a file:

```bash
echo "<h1>Hello from Ansible Copy Module</h1>" > index.html
```

Create `copy_file.yml`:

```yaml
---
- name: Copy index.html to Apache directory
  hosts: webservers
  become: yes

  tasks:
    - name: Copy index.html
      copy:
        src: ./index.html
        dest: /var/www/html/index.html
```

Run:

```bash
ansible-playbook copy_file.yml
```

Check in browser: `http://<managed-ec2-public-ip>/`

---

### 🔹 FILE Module (Manage Files & Permissions)

Create `file_permission.yml`:

```yaml
---
- name: Manage file permissions
  hosts: webservers
  become: yes

  tasks:
    - name: Create test file
      file:
        path: /tmp/testfile
        state: touch
        mode: '0644'
```

---

### 🔹 USER Module (Create User)

Create `create_user.yml`:

```yaml
---
- name: Create user on EC2
  hosts: webservers
  become: yes

  tasks:
    - name: Add user devuser
      user:
        name: devuser
        state: present
```

Run and verify:

```bash
ansible-playbook create_user.yml
ssh -i ~/.ssh/YourKey.pem ubuntu@<managed-ec2-ip> "id devuser"
```

---

### 🔹 TEMPLATE Module (Dynamic Content)

Create template `index.html.j2`:

```html
<h1>Hello from {{ ansible_hostname }}</h1>
```

Create playbook `template_file.yml`:

```yaml
---
- name: Deploy template to Apache directory
  hosts: webservers
  become: yes

  tasks:
    - name: Copy template
      template:
        src: ./index.html.j2
        dest: /var/www/html/index.html
```

Run:

```bash
ansible-playbook template_file.yml
```

Check in browser → It should display the hostname of the EC2.

---

## 3. Summary

- **apt** → install packages  
- **service** → start/stop services  
- **copy** → copy files  
- **file** → manage files/permissions  
- **user** → create/manage users  
- **template** → generate dynamic files with variables  

With these modules, you can automate almost all basic server management tasks 🚀
