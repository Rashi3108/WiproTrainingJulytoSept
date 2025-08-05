# Day 12 Git Fundamentals - Group Activities
## 5 Groups × 6 Members Each - Collaborative Learning

---

## 🎯 Activity Overview
Each group will create a **private repository** and work through progressive Git scenarios that simulate real-world development workflows. These activities are designed to reinforce the Day 12 concepts through hands-on practice.

---

## 📋 Pre-Activity Setup (5 minutes)

### Group Formation & Repository Setup
1. **Group Leaders**: Each group selects one member as the "Repository Owner"
2. **Repository Creation**: Repository Owner creates a private GitHub repository named: `devops-git-lab-group[X]` (where X = group number)
3. **Team Invitation**: Repository Owner invites all 5 team members as collaborators
4. **Role Assignment**: 
   - 1 Repository Owner (manages main branch)
   - 2 Feature Developers (work on features)
   - 2 Code Reviewers (review and merge)
   - 1 Release Manager (handles tags and releases)

---

## 🚀 Activity 1: Git Basics Relay (15 minutes)
**Objective**: Master fundamental Git commands through team collaboration

### Scenario
Your team is starting a new project called "DevOps Task Manager" - a simple task management application.

### Instructions
**Round 1: Repository Initialization (Repository Owner)**
```bash
# Clone the empty repository
git clone https://github.com/[username]/devops-git-lab-group[X].git
cd devops-git-lab-group[X]

# Create initial project structure
mkdir src tests docs
echo "# DevOps Task Manager" > README.md
echo "A collaborative task management application built by Group [X]" >> README.md
echo "" >> README.md
echo "## Team Members" >> README.md
echo "- [List all 6 team member names]" >> README.md

# Create .gitignore
cat > .gitignore << EOF
node_modules/
.env
*.log
.DS_Store
dist/
EOF

# Initial commit
git add .
git commit -m "feat: initial project setup with team structure"
git push origin main
```

**Round 2: Feature Development (Feature Developers - 2 members)**

*Developer 1:*
```bash
# Pull latest changes
git pull origin main

# Create task management core
echo "class TaskManager {
    constructor() {
        this.tasks = [];
    }
    
    addTask(task) {
        this.tasks.push({
            id: Date.now(),
            title: task,
            completed: false,
            createdBy: 'Group[X]'
        });
    }
}" > src/taskManager.js

git add src/taskManager.js
git commit -m "feat: add TaskManager class with addTask method"
git push origin main
```

*Developer 2:*
```bash
# Pull latest changes (including Developer 1's work)
git pull origin main

# Add more functionality
echo "
    completeTask(id) {
        const task = this.tasks.find(t => t.id === id);
        if (task) {
            task.completed = true;
            return true;
        }
        return false;
    }
    
    getTasks() {
        return this.tasks;
    }
}" >> src/taskManager.js

git add src/taskManager.js
git commit -m "feat: add completeTask and getTasks methods"
git push origin main
```

**Round 3: Documentation & Testing (Code Reviewers - 2 members)**

*Reviewer 1:*
```bash
git pull origin main

# Add documentation
echo "# API Documentation

## TaskManager Class

### Methods

#### addTask(task)
- **Description**: Adds a new task to the task list
- **Parameters**: 
  - task (string): The task description
- **Returns**: void

#### completeTask(id)
- **Description**: Marks a task as completed
- **Parameters**: 
  - id (number): The task ID
- **Returns**: boolean - true if successful, false if task not found

#### getTasks()
- **Description**: Returns all tasks
- **Returns**: Array of task objects
" > docs/API.md

git add docs/API.md
git commit -m "docs: add API documentation for TaskManager"
git push origin main
```

*Reviewer 2:*
```bash
git pull origin main

# Add basic tests
echo "// Basic tests for TaskManager
const TaskManager = require('../src/taskManager');

// Test 1: Create TaskManager instance
const tm = new TaskManager();
console.log('✓ TaskManager instance created');

// Test 2: Add task
tm.addTask('Learn Git fundamentals');
console.log('✓ Task added successfully');

// Test 3: Get tasks
const tasks = tm.getTasks();
console.log('✓ Tasks retrieved:', tasks.length, 'task(s)');

// Test 4: Complete task
const success = tm.completeTask(tasks[0].id);
console.log('✓ Task completion:', success ? 'SUCCESS' : 'FAILED');

console.log('All tests completed by Group [X]!');
" > tests/taskManager.test.js

git add tests/taskManager.test.js
git commit -m "test: add basic tests for TaskManager functionality"
git push origin main
```

**Round 4: Release Management (Release Manager)**
```bash
git pull origin main

# Create version file
echo "1.0.0" > VERSION
git add VERSION
git commit -m "chore: add version file for release 1.0.0"

# Create release tag
git tag -a v1.0.0 -m "Release v1.0.0: Basic TaskManager with add, complete, and get functionality"
git push origin main
git push origin v1.0.0

# View project history
git log --oneline --graph
```

### 🎯 Learning Check Questions:
1. What's the difference between `git add .` and `git add filename`?
2. Why do we use `git pull` before making changes?
3. What information does `git log --oneline` show us?
4. What's the purpose of the .gitignore file?

---
