																	**Module 5- Computer Systems (2022-23)** 

​																								**Project**       

![image-20210603160820291](C:\Users\SarmahDK\AppData\Roaming\Typora\typora-user-images\image-20210603160820291.png)



**Security by Design Checklist**

**(Design Phase)**



| Team ID:          | Team Members:  |
| ----------------- | -------------- |
| **Project Name:** | **Mentor(s):** |

**Instructions:**

1. Complete the sections in the below table and put a checkmark if you have done.
2. Think about your application and work on the sections accordingly.
3. Feel free to add extra requirements for reviewing security architecture and their countermeasures for your application, if needed. 
4. This document should be reviewed and approved by your team members and mentors before submission.
5. Make sure to submit this checklist along with the Software design document (SDD) on Canvas.



| Sr. No. | Review Security Architecture                                 | Put checkmark ✔ if you have completed the Review Security Architecture as suggested in the left column | Additional comments (If required) | Security Controls/Countermeasures                            | Put checkmark ✔ if you have completed the Security controls points as suggested in the left column | Additional comments (if required) |
| ------- | :----------------------------------------------------------- | ------------------------------------------------------------ | --------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------------------------- |
| 1.      | <span style='color:blue'>**Check Trust Boundaries,** </span>***for example***, if you assign a higher privilege's level to someone to access a particular resource. |                                                              |                                   | <span style='color:blue'>**Check the prevention criteria**, </span>***for example***, if your personal information is identified by logging into an application, then either you decide to disable the application by removing your personal information and logging in. This is a prevention criterion. |                                                              |                                   |
| 2.      | <span style='color:blue'>**Identify data flows**, </span>***for example,*** if you read data from an untrusted source for your  application. |                                                              |                                   | <span style='color:blue'>**Check the mitigation criteria to reduce the impact of the risk/threat for the application.**</span> ***For example:*** Assume you have a database of users' passwords that are stored as a hash. Two users in the database who have the same password, they'll also have the same hash value. If the attacker identifies the hash value and its associated password, he'll be able to identify all the other passwords that have the same hash value. This risk can be mitigated by adding a randomly generated string, i.e. salt to each password in the database. |                                                              |                                   |
| 3.      | **<span style='color:blue'>Entry and Exit points of the system and its components.</span>** |                                                              |                                   | **<span style='color:blue'>Make a data flow diagram to visualize and understand the data flow, input, output points, and trust boundary.</span>** |                                                              |                                   |
| 4.      | **<span style='color:blue'>Write the complete architecture in the SDD template. Review and approve among  yourselves and by your assigned mentor(s).</span>** |                                                              |                                   | **<span style='color:blue'>Analyze the cost involved to implement the security controls (if any). </span>** |                                                              |                                   |



| Team  members' reviewed:              | (Member  1, Yes), (Member 2, Yes),…      |
| ------------------------------------- | ---------------------------------------- |
| **Mentor(s)  reviewed and verified:** | **(Mentor  1, Yes), (Mentor 2, Yes), …** |

​																																											

​																																											Prepared by:

​																																											Dipti K. Sarmah
