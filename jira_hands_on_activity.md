# 🎯 Jira Advanced Administration Hands-On Activity
## Complete Project Setup & Configuration Exercise

### 📋 **Activity Overview**
**Duration:** 60 - 90 minutes  
**Participants:** 30 people 
**Objective:** Apply all advanced Jira concepts in a realistic business scenario  
**Skills Practiced:** Issue types, workflows, assignments, automation, and reporting

---

## 🎮 **Activity Scenario**

### **Business Context:**
You're the Jira administrator for **"TechFlow Solutions"** - a software company launching a new customer portal project. The company has different teams with unique workflows, and you need to set up a comprehensive Jira configuration that supports their diverse needs.

### **Teams Involved:**
- **Development Team:** Builds features and fixes bugs
- **QA Team:** Tests and validates functionality  
- **Design Team:** Creates UI/UX designs
- **DevOps Team:** Handles deployments and infrastructure
- **Support Team:** Manages customer issues
- **Management:** Tracks progress and makes decisions

---

## 🏗️ **Phase 1: Custom Issue Types Creation (20 minutes)**

### **Your Mission:**
Create custom issue types that match each team's specific needs.

### **Required Issue Types to Create:**

#### **1. Development Team Issue Types:**
```
Issue Type: "Feature Request"
- Description: "New functionality requested by customers or stakeholders"
- Icon: ⭐ (Star)
- Hierarchy Level: Standard
- Color: Blue

Issue Type: "Technical Debt"  
- Description: "Code improvements and refactoring tasks"
- Icon: 🔧 (Wrench)
- Hierarchy Level: Standard
- Color: Orange
```

#### **2. Design Team Issue Types:**
```
Issue Type: "Design Task"
- Description: "UI/UX design work including mockups and prototypes"
- Icon: 🎨 (Palette)
- Hierarchy Level: Standard
- Color: Purple

Issue Type: "Design Review"
- Description: "Review and approval of design deliverables"
- Icon: 👁️ (Eye)
- Hierarchy Level: Sub-task
- Color: Green
```

#### **3. DevOps Team Issue Types:**
```
Issue Type: "Deployment"
- Description: "Application deployment to various environments"
- Icon: 🚀 (Rocket)
- Hierarchy Level: Standard
- Color: Red

Issue Type: "Infrastructure"
- Description: "Server setup, configuration, and maintenance tasks"
- Icon: 🏗️ (Construction)
- Hierarchy Level: Standard
- Color: Gray
```

### **Success Criteria:**
- ✅ All 6 custom issue types created
- ✅ Appropriate icons and colors assigned
- ✅ Issue types available in your project
- ✅ Team can create issues using new types

---

## 🔄 **Phase 2: Custom Workflow Design (25 minutes)**

### **Your Mission:**
Create a custom workflow for "Feature Request" issues that includes approval and review stages.

### **Required Workflow: "Feature Development Process"**

#### **Workflow Statuses:**
1. **📝 Submitted** (To Do Category)
2. **👀 Under Review** (In Progress Category)  
3. **✅ Approved** (In Progress Category)
4. **🔨 In Development** (In Progress Category)
5. **🧪 Testing** (In Progress Category)
6. **📋 Code Review** (In Progress Category)
7. **🚀 Ready for Release** (Done Category)
8. **✅ Released** (Done Category)
9. **❌ Rejected** (Done Category)

---

## 👥 **Phase 3: User Management & Assignments (15 minutes)**

### **Your Mission:**
Set up users, groups, and assign issues to team members.

### **Required Setup:**

#### **1. Create User Groups:**
```
Group: "developers"
- Members: 2-3 team members
- Purpose: Development team access

Group: "qa-team"  
- Members: 1-2 team members
- Purpose: Quality assurance access

Group: "designers"
- Members: 1 team member  
- Purpose: Design team access

Group: "managers"
- Members: 1 team member
- Purpose: Approval permissions
```

#### **2. Create Test Issues:**
Create 10 sample issues using your new issue types:

```
Feature Request Issues (3):
1. "Add user profile customization"
2. "Implement dark mode theme"  
3. "Create advanced search functionality"

Design Task Issues (2):
4. "Design login page mockup"
5. "Create mobile app wireframes"

Technical Debt Issues (2):
6. "Refactor authentication module"
7. "Optimize database queries"

Deployment Issues (2):
8. "Deploy to staging environment"
9. "Production release v2.1"

Infrastructure Issue (1):
10. "Set up monitoring dashboard"
```

#### **3. Assignment Strategy:**
- Assign Feature Requests to developers
- Assign Design Tasks to designers  
- Assign Technical Debt to senior developers
- Assign Deployments to DevOps team members
- Leave some issues unassigned for practice

### **Step-by-Step Instructions:**

1. **Create Groups:**
   - Go to Settings → User Management → Groups
   - Create each required group
   - Add team members to appropriate groups

2. **Create Issues:**
   - Use "Create Issue" button
   - Select appropriate issue types
   - Fill in summary and description
   - Set priority and components as needed

3. **Assign Issues:**
   - Edit each issue
   - Set assignee based on issue type
   - Add relevant labels or components
   - Set due dates where appropriate

### **Success Criteria:**
- ✅ All user groups created with members
- ✅ 10 test issues created with different types
- ✅ Issues properly assigned to team members
- ✅ Issues have appropriate priorities and details

---

## 🤖 **Phase 4: Automation Rules (20 minutes)**

### **Your Mission:**
Create automation rules that streamline your workflow processes.

### **Required Automation Rules:**

#### **Rule 1: Auto-Assignment by Issue Type**
```
Rule Name: "Auto-assign by Issue Type"
Trigger: Issue Created
Conditions: 
- Issue Type = "Design Task" → Assign to designers group member
- Issue Type = "Deployment" → Assign to DevOps team member  
- Issue Type = "Technical Debt" → Assign to senior developer
Actions:
- Assign issue to appropriate person
- Add comment: "Auto-assigned based on issue type"
```

#### **Rule 2: Status Change Notifications**
```
Rule Name: "Development Status Updates"
Trigger: Issue Transitioned
Condition: Issue Type = "Feature Request"
Actions:
- If transitioned to "Testing" → Assign to QA team member
- If transitioned to "Code Review" → Assign to tech lead
```

### **Step-by-Step Instructions:**

1. **Access Automation:**
   - Go to Project Settings → Automation
   - Click "Create Rule"

2. **Create Each Rule:**
   - Select appropriate trigger
   - Add conditions as specified
   - Configure actions
   - Test rule with sample data

3. **Enable and Monitor:**
   - Turn on each rule
   - Test by creating/updating issues
   - Check audit log for rule execution

### **Success Criteria:**
- ✅ All automation rules created and enabled
- ✅ Rules tested with sample issues
- ✅ Automatic assignments working
- ✅ Notifications being sent correctly

---
