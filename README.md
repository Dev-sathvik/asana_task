# Auto add project name in task title

---

## Programming language and tools used
* Python  
* VS Code
  
---

## Steps to set up the environment (e.g., software, libraries, dependencies)
1. Make sure python(above version 3) and pip is installed in your system.
2. Fork this repository, clone it and navigate to the directory.
3. Create and activate a virtual environment by running this in powershell.  
   ```python -m venv venv```  
   ```.\venv\Scripts\Activate.ps1```  
4. Install all the required packages  
    ```pip install -r requirements.txt```   
5. Create a virtual environment(.env) file in top level of directory and paste the PAT in the given form.  
    ```ASANA_PAT=<YOUR_TOKEN>```  

---

## Instructions to run the code
1. Navigate to the cloned directory.
2. Execute the following command to start the service.  
    ```python get_events.py```  
---

## Expected input/output format
### Input
   - Add a new task to the project named Qscripts in the asana platform.

### Output
   - After some seconds, the task name will be prefixed with project name.
     
---

## Any special notes (e.g., limitations, known issues, or next steps)

### Limitations, known issuses
- The system depends on how often we poll the API of asana, a large time gap improves the effectiveness of this service but takes longer to time to get updated. 
- If the time gap is very less, the task name may not have not get updated correctly.
- Sometimes updation may not happen correctly because only the partial change is captured because of the given time frame(10 seconds).

### Next steps
- Make this service work for all of the projects.
- Try to implement the webhooks approach using a cloud server and compare the effectiveness.
- Account for the case of renaming the existing task name with new name.

---
