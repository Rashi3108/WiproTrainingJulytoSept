# Lab: Jenkins Pipeline Practice – Declarative & Scripted

## Objective
Implement the same CI pipeline in **both Declarative** and **Scripted** pipeline syntax.

---

## Requirements
1. Checkout a Maven-based Java project from GitHub.
2. Build the project using Maven.
3. Run SonarQube analysis using a secure token stored in Jenkins credentials.

---

## Details
- **Git Repository:** Use your own or the sample:  
  `https://github.com/Rashi3108/MySpringBootApp.git`
- **Branch:** `main`
- **GitHub Credentials ID in Jenkins:** `local-jenkins-rashi`
- **Maven Tool Name in Jenkins:** `maven`
- **SonarQube Project Key:** `springboot-demo`
- **SonarQube URL:** Use your ngrok/public URL for SonarQube server
- **SonarQube Token Credential ID:** `local-sonarqube`

---

## Tasks

### Part A – Declarative Pipeline
Create a Jenkins pipeline using Declarative syntax with:
- `pipeline {}`, `agent any`, `tools {}`, `environment {}` blocks
- Stages:
  1. **Checkout** – Use Jenkins Git step with credentials.
  2. **Build** – Run `mvn clean install`.
  3. **Package** – Run `mvn package`.
  4. **SonarQube Analysis** – Run `mvn sonar:sonar` with token from credentials.

---

### Part B – Scripted Pipeline
Implement the **same stages** in Scripted syntax using:
- `node {}`, `stage {}`, and `withCredentials` blocks
- Call Maven from the Maven tool path dynamically
- Use the same secure credential handling for the SonarQube token

---
