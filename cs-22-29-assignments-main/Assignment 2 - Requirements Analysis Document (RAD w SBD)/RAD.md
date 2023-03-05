#### 												**Module 5- Computer Systems (2022-23)**         						  <img src="C:\Users\SarmahDK\AppData\Roaming\Typora\typora-user-images\image-20210602115950778.png" alt="image-20210602115950778" style="zoom:60%;" />                                                                          

#### 																		**Project**                                   

##### ` `**Requirement Analysis Document Template**


|**Project Name:**|**Team Members:**|
| :- | :- |
|**Team ID:**|**Mentor(s):**|

**Instructions:**

a. All the sections should be written in a clear, concise, and understandable way.

b. You must fill in the basic information about your projects such as Project Name, Team Members, Team ID, and Mentor(s). 

c. Make sure to consider the checklist of the Requirement Analysis phase provided in the Security by Design document.

d. The length of the document should be between 4-8 pages.



1. **Introduction**

   There are several existing applications that you can select as a base for your project. In this section, you need to give a small background of already existing applications. The following points are introduced to get to know the purpose of your application, limitations of the existing system on which your project is based, etc.

   **A.** **Purpose**: 

   ​		You should know the purpose of creating your application. Write the reason for selecting this project by mentioning the usefulness, quality, etc. of the system.

- **For example:** 

  <span style="color:blue"> ***“The project namely IOT based home automation system is selected for the following reasons:***</span>

  - <span style="color:blue"> 	*This can digitally monitor and control the home devices such as electronic appliances, light systems, etc., from a remote location using smartphones/tablets. You have to just connect to the internet.*</span>

  - <span style="color:blue"> *This can be used for safety and security purposes by including the access control feature and the alarm systems in a front door.*</span>

  - <span style="color:blue"> *This...*</span>

    

  **B. Limitations of the current system(If any):**

  ​	List down the limitations of the currently existing similar systems. 

  ​	***For example:***,

  ​		<span style="color:blue">***“The current limitations of already existing smart home automation system are*** </span>

  - <span style="color:blue">*The web interface is not user-friendly.*</span>
  - <span style="color:blue">*The synchronization issue, if connecting with different IoT devices at the same time.*</span>
  -    <span style="color:blue">*The network connectivity problem.*</span>
  -    <span style="color:blue">*a lot of energy/power consumption.*</span>
  -    <span style="color:blue">*no decision-making capability.* </span>
  -   <span style="color:blue">*....”*</span>

  

  **C.  Intended Audience**

  ​	Write about the targeted audience who can have access to your product or the documents. **For example**  <span style="color:blue">*users/stakeholders (Mentor, Project Coordinator, Module Coordinator, Project Members, Any specific users, etc.)* </span>

  

  **E.** **Define SMART Goals**: 

  This section is used to list down the target/expected results from the project. All the goals should be written in a SMART (Specific + Measurable + Attainable + Relevant + Time-bound) way.

  **For example** 

  <span style="color:blue">*“The goals for the project IoT based smart home system are as follows:*</span>


|<span style="color:green">**Specific (What)**</span>|<span style="color:green">**Measurable (Up to)**</span>|<span style="color:green">**Attainable (How)**</span>|<span style="color:green">**Relevant (Why)**</span>|<span style="color:green">Time-bound (when)</span>|
| :-: | :- | :- | :- | :- |
|<span style="color:blue">*1. To improve the **efficiency** of the system by having a user-friendly web interface.*</span> |<span style="color:blue">*To evaluate success rate/errors for improving the system.*</span>|<span style="color:blue">*To test the system with the improved web interface.*</span>|<span style="color:blue">*To ensure within the team the success of the system regarding the web interface.*</span>|<span style="color:blue">*To finish the task between Week 4-Week 5.*</span>|
|<span style="color:blue">*2. To improve the **productivity** of the system by adding sensors such as door and window sensor, motion sensor, light sensor, temperature sensor, etc. for controlling the devices.*</span>|||||
|<span style="color:blue">*3. To improve the **quality** of the system…*</span>|||||
|<span style="color:blue">*4. To improve the **security** of the system…*</span>|||||



​	**F.  Scope:**

​				This section is required to write about the important resources to achieve the goals of your system. The technology 				used to develop your project (methods/algorithms, software requirements, hardware requirements), the duration of the 				project, and the project constraints should be included here. The project constraints can be any technical hiccups, lack of 				resources, internal and external conditions (boundary conditions), etc. that can help further to avoid the related 				problems in the future during execution. In short, you can utilize this section to write about the limitations and       				boundaries of your project. 

​		***For example***

- **<span style="color:green">*i) System boundaries (Software and hardware):*</span>** 
  - <span style="color:blue">*Software: MQTT server to manage the flow of data between IoT devices, Mobile application, Python language, HTML,  	PHP,Algorithms used, etc.*</span>
  - <span style="color:blue">*Hardware: Raspberry Pi 4, Sensors, Power supply, USB web camera, etc.*</span>
  - <span style="color:blue">*Interfaces: To name a few such as the Internet via WiFi, backup methods such as 4G hotspot,  etc.*</span>

- ​	<span style="color:green">***ii)* *Limitations:*** </span>
  - <span style="color:blue">*This project can only monitor and control the lights of a home.* </span>
  - <span style="color:blue">*This project can only control the ‘n’ IoT devices at a time.*</span>
  - <span style="color:blue"> …”*</span>

2. **Product features (Ref: https://medium.com/omarelgabrys-blog/requirements-engineering-introduction-part-1-6d49001526d3) (To understand functional and non-functional requirements:** 

   This section describes the functionality that you want to have in your product such as the components used for the application and its functionality, appearance, performance in terms of speed/time, etc. You can specify them in the form of functional and non-functional requirements. <span style="color:blue">A minimum number of 7 requirements (9 in case of selecting an existing application), counting functional/non-functiona/security requirements cumulatively. However, it is highly probable that you will need more than the minimum amount to fully cover all the requirements. 
   
   While listing your requirements, you are also required to assign the level of priority to the requirements as done in the examples below. The priority levels are: High [**H**], Medium [**M**] and Low [**L**].
   
   <span style="color:red">Note:</span> that **at least 2** should be **Security Requirements**.</span>

   

   ​	**A.** **Functional requirements:** 
   ​		Write the requirements that are directly connected with the functionality of the application. 

   ​		**For example**, 

   - ​	<span style="color:blue">*i) “The functional requirements of a **smart home automation system** are:*</span>
     - <span style="color:blue">* [**L**] The system should give the option to the user to select the mode between cloud and stand-alone.*</span>
     - <span style="color:blue">* [**H**]The system should allow users to control and monitor their home devices using smartphones/tablets.*</span>
     - <span style="color:blue">*The system should...*</span>
     - <span style="color:blue">*The system should...  ”*</span>
   - <span style="color:green">*ii) “The functional requirements of a **simple calculator** are:* </span>
     - <span style="color:green">*  [**H**] The system/product should perform all the arithmetic operations according to the given keys.*</span>
     - <span style="color:green">* [**M**] The system/product should have the On/Off button to switch on or switch off the calculator.*</span>
     - <span style="color:green">*The system should ...”*</span>

   

   **B.** **Nonfunctional requirements:** 

   ​	Write the requirements that are not the specific actions for your application but improve the quality of the system. This can be related to the storage capacity, performance requirements,  Security requirements (Refer to the checklist given in SBD document-Phase 1), etc. 

   **For example:**,

   - <span style="color:blue">*“The nonfunctional requirements of a **smart home automation system** are:*</span>
     - <span style="color:blue">* [**L**] The system should be able to monitor the average latency between the gateway and the devices.*</span>
     - <span style="color:blue">*…”*</span>
   - <span style="color:green">*“The nonfunctional requirements of a **simple calculator** are:*</span>
     - <span style="color:green">* [**H**] The layout for the keys should not exceed more space than the layout of the calculator.*</span>
     - <span style="color:green">* [**H**] The system should be able to work with a minimum of 10 digits.*</span>
     - <span style="color:green">* [**M**] The system should not exceed the specified memory range.*</span>
     - <span style="color:green">* [**L**] The system should complete the arithmetic operation computation within t milliseconds.*</span>
     - <span style="color:green">***…”***</span>

   **C.** **Security requirements:** 

   ​	Write the requirements that are the security requirements of your application (Refer to the checklist given in SBD document-Phase 1), etc. 

   ​		**For example**, 

   - ​	<span style="color:blue">*i) "The functional requirements of a **smart home automation system** are:*</span>
     - <span style="color:blue">* [**M**] The system should perform user authentication.*</span>
     - <span style="color:blue">* [**H**] The system should give control of the smart devices to the authorized user.*</span>
     - <span style="color:blue">*The system should...  ”*</span>
   - ​	<span style="color:green">*ii) "The functional requirements of a **simple calculator** are:* </span>
     - <span style="color:green">* [**M**] To access the application, one should require authentication.* </span>
     - <span style="color:green">*The system should ...”*</span>

<span style="color:red">Note:</span> You are recommended to use the given priorities to produce a plan for your sprints such that you are able to deliver an **MVP** by the end of **Sprint 3**.

3. **Conclusion:** Write the concluding remarks here. You can do this by **highlighting noteworthy decisions and challenges** for the next phase that you recognized.

4. **Reference**: List the existing literature (documents/articles/blogs/research papers) references you have considered for finalizing the project idea.



[^1]: **The security requirements should be mapped with the SBD requirement analysis (phase 1) checklist. You are free to write the security requirements in the form of a user story/abuse case.**

​																																										

​																																										Prepared by: Dipti K. Sarmah                               
