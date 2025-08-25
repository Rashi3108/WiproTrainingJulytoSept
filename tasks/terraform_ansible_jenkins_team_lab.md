# Hands-on Lab: Terraform + Ansible + Jenkins on AWS EC2 (Team-Based)

## Objective

Participants will learn how to: 1. Provision AWS infrastructure with
**Terraform** (shared VPC + Jenkins, individual app servers). 2.
Configure servers with **Ansible**. 3. Deploy and run **Jenkins** on a
team-shared EC2 instance. 4. Use Jenkins to run a simple **CI/CD
pipeline** that deploys to each student's app server.

------------------------------------------------------------------------

## Lab Structure

-   Participants are divided into **5 teams** (about 6 participants per team).\
-   Each team provisions **one Jenkins server** and **one shared VPC**.\
-   Each student provisions their **own app server EC2 instance** inside
    the team's VPC.\
-   Jenkins pipelines deploy code to **each student's app server**.

------------------------------------------------------------------------

##  Lab Flow

### Phase 1: Team Setup (Shared by All Team Members)

1.  **Terraform**
    -   Create **1 VPC**, **subnet**, **internet gateway**, **route
        table**.
    -   Create a **security group** allowing ports 22, 80, 8080.
    -   Provision a **Jenkins EC2 instance (t2.medium)** inside the
        shared VPC.
    -   Output the Jenkins public IP.
2.  **Ansible**
    -   Install Java and Jenkins on the Jenkins instance.
    -   Ensure Jenkins is running at `http://<jenkins-ip>:8080`.

Deliverable: A running Jenkins instance shared by the whole team.

------------------------------------------------------------------------

### Phase 2: Individual Student Work

1.  **Terraform**
    -   Write Terraform to create a **t2.micro EC2 app server** inside
        the team's VPC.
    -   Attach it to the existing security group.
2.  **Ansible**
    -   Configure the app server with:
        -   Update packages.
        -   Install **Nginx/Apache** as a web server.

Deliverable: Each student has a personal app server accessible at its
public IP.

------------------------------------------------------------------------

### Phase 3: Jenkins Pipeline (Team Jenkins, Individual Targets)

-   Inside the **team's Jenkins server**:
    -   Create individual pipeline.
    -   Pipeline steps:
        -   Clone a sample GitHub repo (use your own springboot app).
        -   Run a simple build using Maven.
        -   Deploy build output to the your own app server via
            SSH/Ansible.

Deliverable: A Jenkins job that successfully deploys to each
participant's app server.

------------------------------------------------------------------------

## Skills Practiced

-   **Terraform**: EC2, VPC, networking, variables, outputs.
-   **Ansible**: inventories, playbooks.
-   **Jenkins**: installation, pipeline creation, CI/CD integration.
-   **Team collaboration**: shared infra + individual app servers.

------------------------------------------------------------------------

## Final Deliverables

-   **Per Team**:
    -   1 Jenkins server (t2.medium) running in a shared VPC.
    -   1 shared Terraform + Ansible setup for VPC and Jenkins.
-   **Per Student**:
    -   1 EC2 app server (t2.micro) provisioned by Terraform.
    -   Configured with Ansible as a web server.
    -   Deployed application via Jenkins pipeline.

------------------------------------------------------------------------

Good Luck to all teams :)

