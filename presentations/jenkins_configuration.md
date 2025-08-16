# Jenkins Configuration Guide

This guide explains how to configure Jenkins through the **UI** to set up required plugins, credentials, and tools.

---

## 1. Install Plugins

1. Log in to Jenkins UI (`http://<your-server>:8080`).
2. Navigate to **Manage Jenkins → Plugins → Available plugins**.
3. Search and install the following plugins:
   - **Git Plugin** (for source code integration)
   - **Pipeline Plugin** (for pipeline jobs)
   - **SonarQube Scanner for Jenkins** (for code quality analysis)
   - **Maven Integration Plugin** (to integrate Maven with Jenkins)
4. Restart Jenkins if prompted.

---

## 2. Configure Credentials

### a. Git Credentials
1. Go to **Manage Jenkins → Credentials → System → Global credentials → Add Credentials**.
2. Select type:
   - **Username with password** (for HTTPS-based Git access)
   - **SSH Username with private key** (for SSH-based Git access)
3. Provide ID (e.g., `git-credentials`) and save.

### b. SonarQube Token
1. Generate a token from your SonarQube server under **My Account → Security → Tokens**.
2. In Jenkins, go to **Manage Jenkins → Credentials → System → Global credentials → Add Credentials**.
3. Select **Secret text**, paste the token, and save with ID (e.g., `sonarqube-token`).

---

## 3. Configure Maven Tool

1. Go to **Manage Jenkins → Tools → Maven installations**.
2. Click **Add Maven**.
3. Provide:
   - Name: `maven`
   - Installation method: Select **Install automatically** or provide local installation path.
4. Save configuration.

---

## 4. Configure SonarQube in Jenkins

1. Go to **Manage Jenkins → Configure System**.
2. Scroll to **SonarQube servers** section.
3. Click **Add SonarQube** and provide:
   - Name: `MySonarQube`
   - Server URL: `http://<sonarqube-server>:9000`
   - Server authentication token: Select previously added credential (`sonarqube-token`).
4. Save.

---

✅ Jenkins is now ready with **plugins, credentials, and Maven tool configuration**.
