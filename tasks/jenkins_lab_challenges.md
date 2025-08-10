
# Jenkins Lab Challenges – Free-Style & Pipeline

---

## Lab 1 – Free-Style Basics  
**Challenge:**  
- Create a Free-Style job that prints:
  1. Your name
  2. Current date and time
  3. The current logged-in Jenkins build user (`whoami`)  
- The output should be visible in **Console Output**.  

**Bonus:** Add a build parameter for name instead of hardcoding it.

---

## Lab 2 – Git + Shell Commands (Free-Style)  
**Challenge:**  
- Create a Free-Style job that:
  1. Clones any public GitHub repository.
  2. Lists **only files modified in the last 24 hours**.  
- Display the result in the console.  

**Bonus:** Make the repo URL configurable via a String Parameter.

---

## Lab 3 – Parameterized Build with Logic (Free-Style)  
**Challenge:**  
- Create a parameterized Free-Style job with:
  - `DEPLOY_ENV` (Choice: dev, test, prod)
  - `VERSION` (String)  
- Job should:
  1. Echo the chosen environment.
  2. If `prod` is selected, display **"Production Deployment – Requires Approval"**.  
  3. If `dev` or `test` is selected, display **"Proceeding with deployment"**.  

**Bonus:** Use a `case` or `if` statement in your shell script.

---

## Lab 4 – Git + Automatic Trigger (Free-Style)  
**Challenge:**  
- Create a Free-Style job that:
  1. Clones a Git repository.
  2. Automatically builds when new commits are pushed (Use **Poll SCM** or Webhooks).  
- The job should also:
  - Print the latest commit ID.
  - Print the author name of the last commit.

---

## Lab 5 – Multi-Stage Pipeline  
**Challenge:**  
- Create a **Declarative Pipeline** that:
  1. Accepts parameters: `APP_NAME`, `DEPLOY_ENV`.
  2. Stage 1: Prints `Building APP_NAME for DEPLOY_ENV`.
  3. Stage 2: Clones a repository.
  4. Stage 3: Lists only `.java` files in the repo.
  5. Stage 4: Simulates a deployment using a `sleep` command for 5 seconds.  

**Bonus:**  
- Add a post-build action that:
  - Prints **"Build Successful"** if all stages pass.
  - Prints **"Build Failed"** if any stage fails.

---

## Lab 6 – Pipeline with Scheduled Polling & Old Build Discard  
**Challenge:**  
- Create a **Declarative Pipeline** that:
  1. Configures SCM polling to run **every day at 10:15 AM**.
  2. Discards old builds (keep only the last 5).
  3. Stages:
     - Stage 1: Print the build number and date.
     - Stage 2: Clone a Git repository.
     - Stage 3: List the number of commits in the repo.  

**Bonus:** Show the polling configuration in Jenkins.

---

## Lab 7 – Advanced Parameterized Multi-Stage Pipeline  
**Challenge:**  
- Create a **Declarative Pipeline** with:
  - Parameters:
    - `DEPLOY_ENV` (Choices: dev, qa, staging, prod)
    - `BUILD_TYPE` (Choices: full, incremental)
    - `RUN_TESTS` (Boolean)
  - Stages:
    1. Stage 1: Validate parameters and print them.
    2. Stage 2: Clone a Git repository.
    3. Stage 3: If `RUN_TESTS` is true, simulate running tests with `sleep 3`.
    4. Stage 4: Deploy only if `DEPLOY_ENV` is not `dev`.  
- Implement a **post** block to:
  - Send a success message.
  - Or send a failure message if any stage fails.

**Bonus:**  
- Add an **input approval step** before deploying to `prod`.

---
