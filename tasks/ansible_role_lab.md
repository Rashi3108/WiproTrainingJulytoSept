
# Ansible Lab: Creating and Using a Simple Role

This lab will guide you to create a simple **Ansible Role** and use it in a playbook.  
We will create a role to **install and configure Apache** on an Ubuntu EC2 instance.

---

## 1. Pre-requisites

- Ansible installed on **controller EC2**
- Managed EC2 added in `hosts` file:

```ini
[webservers]
ansible_host=<managed-ec2-public-ip> ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/YourKey.pem
```

Test connection:

```bash
ansible webservers -m ping
```

---

## 2. Create Role Structure

Use `ansible-galaxy` to generate role skeleton:

```bash
mkdir ansible_project
cd ansible_project
mkdir roles
cd roles
ansible-galaxy init apache_role
```

This creates the structure:

```
apache_role/
├── defaults/
│   └── main.yml
├── files/
├── handlers/
│   └── main.yml
├── meta/
│   └── main.yml
├── tasks/
│   └── main.yml
├── templates/
├── tests/
├── vars/
│   └── main.yml
```

---

## 3. Define Tasks

Edit `apache_role/tasks/main.yml`:

```yaml
---
- name: Install Apache
  apt:
    name: apache2
    state: present
    update_cache: yes

- name: Start Apache service
  service:
    name: apache2
    state: started
    enabled: yes
```

---

## 4. Add a Handler

Edit `apache_role/handlers/main.yml`:

```yaml
---
- name: restart apache
  service:
    name: apache2
    state: restarted
```

---

## 5. Create a Template

Create `apache_role/templates/index.html.j2`:

```html
<h1>Hello from Ansible Role on {{ ansible_hostname }}</h1>
```

Update `apache_role/tasks/main.yml` to deploy the template:

```yaml
- name: Deploy custom index page
  template:
    src: index.html.j2
    dest: /var/www/html/index.html
  notify: restart apache
```

---

## 6. Create Playbook Using Role

Create `site.yml`:

```
ansible-project/
├── site.yml
└── roles/
    └── apache_role/
```


```yaml
---
- name: Apply Apache Role
  hosts: webservers
  become: yes
  roles:
    - apache_role
```

---

## 7. Run the Playbook

```bash
ansible-playbook site.yml
```

---

## 8. Verify

1. Open browser → `http://<managed-ec2-public-ip>/`
2. You should see:

```
Hello from Ansible Role on <hostname>
```

---

## 9. Summary

- Roles organize playbooks into reusable components.  
- Our `apache_role` installed Apache, configured service, and deployed a template.  
- Roles make automation **modular, reusable, and scalable**.  
