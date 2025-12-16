### **Troubleshooting Notes**

**1. GitHub Authentication Failure**

Root Cause: GitHub deprecated password-based authentication.    
Resolution: Configured authentication using a Personal Access Token (PAT).


**2. Docker Permission Denied**

Root Cause: User was not part of the docker group.    
Resolution: Added the user to the docker group and restarted the session.


**3. Minikube Failed Due to Insufficient Memory**

Root Cause: VM allocated fewer resources than required.     
Resolution: Switched to Kind as a lightweight Kubernetes alternative.


**4. Pod Status Showed Completed Instead of Running**

Root Cause: The application executed once and exited (no long-running process).      
Resolution: Verified container lifecycle behavior, checked logs, and validated service exposure.
