																		**Module 5- Computer Systems (2022-23)**        

​																									**Project**                                       

​																				<img src="C:\Users\SarmahDK\AppData\Roaming\Typora\typora-user-images\image-20210603140931451.png" alt="image-20210603140931451" style="zoom:80%;" />                                          

   

#### 																Security by Design Checklist 

#### 															(Requirement Analysis Phase 1)

| Team ID:          | Team Members:  |
| ----------------- | -------------- |
| **Project Name:** | **Mentor(s):** |

**Steps to be performed:**

- You should select a minimum of one security mechanism from each  of the security requirements from authentication and authorization ( auditing  is not included here).

- The auditing requirements should be considered as suggested  in the table according to your application. Other than the normal check on  protecting log files, backup files, etc, you should also think about the GDPR obligations, software licensing, etc.  in line with your application.

- The given security mechanisms are for your inspiration. You  can select other mechanisms also according to the requirement of your  application. For example: If you select "authentication" as one  of the security requirements, the mechanism can be logging/password  checking, biometric, OAuth, etc. The same is applicable for authorization and  auditing.

- Justify the reason to select a particular mechanism for the requirements in  the given column ‘C’.

- Write supplement requirement(s) in the form of a user story or  Abuse case for the application (refer to the example given on the table, column ‘D’).  (The supplement requirements should be according to the goals and  non-functional requirement (s) identified for your application.)

- Write the possible risks involved for the supplement requirements (refer to  the example given in the table, column ‘E’).

- Write the resources/mechanisms/tools to avoid/mitigate those risks for  security controls (refer to the example of the column heading "Appropriate  Security Control" (column ‘F’))

- This document must be reviewed with the team members and approved by your  mentor(s)/TAs.

- Put  checkmark in the last column for all verified items.

- This  document should be appended to the Software Requirement Specification (SRS)  document.

  **Follow  these 5 points for each of the Security Mechanisms and write them under  Appropriate Security Controls**:

  (i) Supplement security requirements to avoid risk. 
  
  (ii) Write the requirement of the resources to mitigate such risks. For example:  The type of Authentication software, security tokens, password management  software, etc.
  
  (iii) Devise a plan/method (tentative) to work on the identified risks.
  
  (iv)  Review the documentation within your team.
  
  (v)  Approve the document by your mentor.

  
  
  
  
  | Security  Policy                                           | Confidentiality, Integrity, and Availability                 |                                                              |                                                              |                                                              |                                                              |                                                              |
  | ---------------------------------------------------------- | ------------------------------------------------------------ | :----------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | **<span style="color:blue">Security  Requirements</span>** | **<span style="color:blue">Security  mechanisms (List down for your application)</span>** | **<span style="color:blue">Remarks  on why you considered these requirements? (in a brief)</span>** | **<span style="color:blue">Supplement  requirements for your application       (user story/Abuse case)</span>** | **<span style="color:blue">Risk  identification/Threat Assessment (at least one risk identification/abuse case)</span>** | **<span style="color:blue">Appropriate  Security Controls</span>** | **<span style="color:blue">Tick ✔if  you have applied the given security controls as suggested in the left  column </span>** |
  | **1.** **Authentication**                                  | ***For example:*** Checking password                         |                                                              | ***Example:***                                               | ***Consider  the same Example:***                            | Follow  the 5 points mentioned above.                        |                                                              |
  |                                                            | ***Examples:** [Biometric](https://www.youtube.com/watch?v=MBtzOzPakt8), Account security via [Two factor authentication](https://www.youtube.com/watch?v=0mvCeNsTa1g)/[Multi  Factor Authentication](https://www.youtube.com/watch?v=6kJgM4jiuUA), Smartphone communication (registered phone number),  [OAuth](https://www.youtube.com/watch?v=CPbvxxslDTU), [Proof of User's physical presence for authentication](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/windows-hello-face-authentication) ,  [Proximity based authentication](https://www.youtube.com/watch?v=TglHPqP9iSE), etc.* |                                                              | **Goal:** The system verifies  that there are no default passwords used by the application or any of its  components. **Requirement:** To  access the application, one should require authentication. **User story:** “As a user, I can enter  my user name and passwords to access the application.” **Abuse Case:** As an attacker, I can  enter the default passwords to access the application. | **Risk identication:** i) The  length of the passwords is less than 1023 characters., ii) The password is  not very strong., iii) You enter a wrong password more than 3 times, etc. | Follow  the 5 points mentioned above.                        |                                                              |
  | **2. Authorization**                                       | Access  control policies-User based, role-based, etc.        |                                                              |                                                              |                                                              | Follow  the 5 points mentioned above.                        |                                                              |
  | **3. Audit**                                               | Protection  of Log files,                                    |                                                              |                                                              |                                                              | Follow  the 5 points mentioned above.                        |                                                              |
  |                                                            | Backup  files,                                               |                                                              |                                                              |                                                              | Follow  the 5 points mentioned above.                        |                                                              |
  |                                                            | Temporary  files, software and database licenses (Legal aspect), processing of personal  identifiable information on the devices (Legal aspect/GDPR policies), etc. |                                                              |                                                              |                                                              | Follow  the 5 points mentioned above.                        |                                                              |
  
  

| Team members’ reviewed             | <span style="color:blue">(Member 1, yes), (Member 2, Yes),…</span> |
| ---------------------------------- | ------------------------------------------------------------ |
| **Mentors’ reviewed and verified** | <span style="color:blue">**(Mentor 1, yes), (Mentor 2, Yes)**</span> |

