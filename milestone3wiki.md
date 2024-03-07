# Mister ED

## Incremental Construction: 

### Microservice #1: UI

Accomplishments made in Milestone 3: 
- Backend code for  Authentication, Notifications. 
- Frontend code for the Main page, changing to login/register page, and changing to user info page.

Goals for Milestone 4: 
- Complete remaining Backend Code from Sprint #1. 
- Create Backend code for communicating with the triage engine and checking ED Load.
- add frontend functionality to backend code.
- Improve the aesthetics of the pages.

### Microservice #2: Patient Management

During Milestone 3, we successfully achieved the implementation of the userHealthInfo database, which was subsequently deployed. This database plays a crucial role in storing, updating, and managing user’s health information in our microservice, contributing to the overall functionality and data integrity of our system. We also completed the docker implementation for our microservice which enabled our course instructor, and TAs to test out our databases functionalities at any time.

As we transition to Milestone 4, our primary objectives include implementing and deploying the two remaining databases: triageRecord and userAccountInfo. Where triageRecord would hold all of the user’s triage logs with the results of each triage, and the userAccountInfo would hold all the user’s account information such as login credentials, and contact information. Building on the lessons learned from Milestone 3, we aim to streamline the development process and enhance the overall system robustness.

Simultaneously, our architectural tactic involves implementing a fault detection mechanism using ping/echo to identify component or connection failures and address potential network congestion issues. To achieve this, we are incorporating connection control between modules and databases, ensuring reliability and security in the interactions between various system components and services. We acknowledge that Milestone 4 may present new challenges, since we would be merging our microservice implementation with the other microservices that our group members are working on. This may cause minor merge conflict, but we are confident in our skills that we can tackle any oncoming issues successfully end of Milestone 4.

### Microservice #3: Health Service Management

#### Work done:
**Setup template FastAPI + SlqAlchemy**
* Estimated Time: 8 hours
* Status: Resolved
* Description: 
   - The goal of this ticket is to set up a FastAPI project with integration for SQLAlchemy, a powerful and flexible Object-Relational Mapping (ORM) library. This configuration will enable seamless interaction with a relational database, providing a solid foundation for building robust and scalable web applications.
* Testing: 
   - Test the setup by running the FastAPI application and confirming successful startup.

**Setup model and schema for ER Queue capacity checking and booking system**
* Estimated Time: 8 hours
* Status: Resolved
* Description: 
   - The objective of this ticket is to establish the foundational structure for an Emergency Room (ER) Queue Capacity Checking and Booking System. This involves defining data models and schemas to manage the capacity of the ER queue and facilitate the booking of appointments efficiently, and integrating models and schemas in FastAPI. The defined model and schema will serve as the foundation for further development of the System.
* Testing: 
   - Test the integration of the models and schemas within the FastAPI application.

#### Work for milestone 4
**Setup models and schemas for Health Workers**
* Estimated Time: 3 hours
* Status: Open
* Description:
   - The objective of this ticket is to establish the data models and schemas necessary to manage information related to health workers (nurses, clinician, etc.) within the system. This includes defining the structure of the database tables for health workers, creating schemas for data validation and serialization, and integrating models and schemas in FastAPI. The defined model and schema will serve as the foundation for further development of the System.
* Testing: 
   - Test the integration of the models and schemas within the FastAPI application.
   - Implement unit tests to ensure the correctness of the health worker model and schema definitions.

**Setup models and schemas for Medicine**
* Estimated Time: 2 hours
* Status: In Progress
* Description: 
   - The objective of this ticket is to establish the data models and schemas necessary to manage information related to medicine within the system. This includes defining the structure of the database tables for medicine, creating schemas for data validation and serialization, and integrating models and schemas in FastAPI. The defined model and schema will serve as the foundation for further development of the System.
* Testing: 
   - Test the integration of the models and schemas within the FastAPI application.
   - Implement unit tests to ensure the correctness of the health worker model and schema definitions.

**Setup models and schemas for Health Suggestions**
* Estimated Time: 7 hours
* Status: In Progress
* Description: 
   - The objective of this ticket is to establish the data models and schemas necessary to manage information related to health suggestion after triage within the system, incorporating the Abstract Factory pattern to ensure a flexible and extensible design. This includes defining the structure of the database tables for health suggestion, creating schemas for data validation and serialization,  implementing the Abstract Factory pattern for suggestion creation, and integrating models and schemas in FastAPI. The defined model and schema will serve as the foundation for further development of the System.
* Testing: 
   - Test the integration of the models and schemas within the FastAPI application.
   - Implement unit tests to ensure the correctness of the health worker model and schema definitions.

**Setup models and schemas for Triage Record and Result**
* Estimated Time: 5 hours
* Status: Open
* Description: 
   - The objective of this ticket is to establish the data models and schemas necessary to manage information related to triage records of patients within the system. This includes defining the structure of the database tables for triage records and triage result, creating schemas for data validation and serialization, and integrating models and schemas in FastAPI. The defined model and schema will serve as the foundation for further development of the System.
* Testing: 
   - Test the integration of the models and schemas within the FastAPI application.
   - Implement unit tests to ensure the correctness of the health worker model and schema definitions.

**Containerize the system**
* Estimated Time: 5 hours
* Status: In Progress
* Description: 
   - The objective of this ticket is to containerize the system using Docker, providing a consistent and reproducible environment for deployment. This involves creating a Dockerfile to define the application's container image and a Docker Compose configuration for orchestrating multiple containers.
   - Ensure that the Dockerfile and Docker Compose configuration meet the specific requirements of the system.
   - Consider parameterizing the Docker Compose configuration for flexibility in different environments (development, testing, production).
   - Provide any additional instructions or considerations for developers working with the containerized system.
* Testing: 
   -  Verify that the system functions correctly within the Docker containers.
- Test access to the application through the specified ports.

**Deploy system on GCP**
* Estimated Time: 15 hours
*  hours
* Status: In Progress
* Description: 
   - The goal of this ticket is to deploy the system on the Google Cloud Platform (GCP), leveraging GCP's services for scalability, reliability, and ease of management. This deployment will involve setting up necessary resources, configuring networking, deploying containerized applications, and ensuring a secure production environment.
* Testing: 
   -  Verify that the system functions correctly.
   - Test access to the application through the specified ports.

**Integrate Health Service Management Microservice with Other Services And UI in the System**
* Estimated Time: 15 hours
*  hours
* Status: Open
* Description: 
   - The purpose of this ticket is to integrate the health service management microservice with Patient Management service and UI within the microservices system. This integration is crucial for seamless communication and collaboration between services, fostering a cohesive and efficient microservices architecture.
   - Update system documentation to include details about the newly integrated functionality, communication protocols, and any considerations for developers interacting with the integrated services.
* Testing:
   - Unit test: Develop comprehensive unit tests for the integration logic to verify that the microservice functions correctly in isolation.
   - Integration test: Conduct integration testing to validate the end-to-end functionality of the microservice when interacting with the target service. Emphasize scenarios such as successful communication, error scenarios, and edge cases.

## Architectural Tactics:

Tactics Group | Tactics Question | Support?(Y/N) | Risk | Design Decisions and Location | Rationale and Assumptions
-- | -- | -- | -- | -- | --
Detect Faults | Does the system use ping/echo to detect failure of a component or connection, or network congestion? | N | Low | Instead of ping/echo, we use prometheus/grafana to monitor the system. | Keeping echo to log to make sure the system healthy may poison the log, and since we deploy the system on cloud, storing too many logs may increase the cost of the system.
Detect Faults | Does the system use a component to monitor the state of health of other parts of the system? A system monitor can detect failure or congestion in the network or other shared resources, such as from a denial-of-service attack. | Y | High | We use Google Cloud Platform to deploy our system, and Google Cloud Managed Service supports Prometheus that we can use it to monitor the network and resources usage (CPU, Memory) of deployment nodes | It provides insights into the overall health and performance of the system, allowing for proactive measures to maintain operational excellence and respond to potential challenges.
Detect Faults | Does the system use a heartbeat — a periodic message exchange between a system monitor and a process — to detect failure of a component or connection, or network congestion? | Y | Low | We can implement a heartbeat metrics to detect failure of a component or connection, and monitor it via grafana. | Contribute to the reliability and availability of the system by minimizing the time between the occurrence of a fault and its detection, allowing for faster recovery.
Detect Faults | Does the system use a timestamp to detect incorrect sequences of events in distributed systems? | Y | Low | All the log messages will be logged with timestamp for debugging and tracking purposes. | Timestamps assist in concurrency control by helping to determine the order of concurrent events. This is crucial for maintaining consistency in distributed databases and systems.
Detect Faults | Does the system use voting to check that replicated components are producing the same results?The replicated components may be identical replicas, functionally redundant, or analytically redundant. | Y | High | We deploy multiple replicas of deployment in Kubernetes cluster and monitoring it. | Voting enhances fault tolerance by allowing the system to tolerate faults in a subset of replicas while still producing correct results based on the majority or a predefined quorum.
Detect Faults | Does the system use exception detection to detect a system condition that alters the normal flow of execution (e.g., system exception, parameter fence, parameter typing, timeout)? | Y | Medium | Implement mechanisms for capturing and handling exceptions, such as using try-catch blocks to respond to exceptional conditions. | Exception detection allows for the early identification of faults or abnormal conditions. Early detection is critical for minimizing the impact of issues on system functionality and performance.
Detect Faults | Can the system do a self-test to test itself for correct operation? | N | Low | Instead of automating system to perform self-test, we try to increase coverage of unit tests. | Unit tests is easier to implement but still can ensure the system work properly.
Recover from Faults(Preparation and Repair) | Does the system employ redundant spares?Is a component’s role as active versus spare fixed, or does it change in the presence of a fault? What is the switchover mechanism? What is the trigger for a switchover? How long does it take for a spare to assume its duties? | N | Low | Due to resource and system limit, we won't implement redundant spares. | Due to the limitation of the system and resources, we don't have plan to implement this in the next sprint, but it's recommended to consider to implement this in the future sprints.
Recover from Faults(Preparation and Repair) | Does the system employ exception handling to deal with faults?Typically the handling involves either reporting, correcting, or masking the fault. | Y | Low | When a fault occurs, the system generates reports or logs that capture details about the exception. These reports typically include informationsuch as the type of exception, the context in which it occurred, and any relevant data. | Reporting allows system administrators or developers to analyze the rootcause of the fault, diagnose issues, and take appropriate corrective actions.
Recover from Faults(Preparation and Repair) | Does the system employ rollback, so that it can revert to a previously saved good state (the “rollback line”) in the event of a fault? | Y | High | The system will support rollback for node deployment so we can rollback to the previous version in case the new deployment contains errors/bugs. | Rollback mechanisms are a crucial part of fault-tolerant and resilient system design. They contribute to system stability, reliability, and the ability to gracefully handle unexpected challenges.
Recover from Faults(Preparation and Repair) | Can the system perform in-service software upgrades to executable code images in a non-service-affecting manner? | N | Low | The system will be manually updated when there's new version. | Limited resources may need to be prioritized for more immediate concerns, such as system stability, security patches, or critical bug fixes, so we postpone the plan to implement this in the next sprint, and push that to the future sprints when the system is more mature and scaled.
Recover from Faults(Preparation and Repair) | Does the system systematically retry in cases where the component or connection failure may be transient? | Y | High | The system will support exponential retry for API requests and connection to databases to handle the case where connection failure may be transient. | Sometimes, the system fails due to a temporary accident, retry mechanism helps the system retry and continue to run.
Recover from Faults(Preparation and Repair) | Can the system simply ignore faulty behavior (e.g., ignore messages when it is determined that those messages are spurious)? | Y | Low | We combine the detected exception occur with the monitored metrics to determine to whether to ignore faulty behavior. | Some errors are just temporary and may happen due to an unexpected event but not from our system, so we should detect and ignore these errors.
Recover from Faults(Preparation and Repair) | Does the system have a policy of degradation when resources are compromised, maintaining the most critical system functions in the presence of component failures, and dropping less critical functions? | N | Medium | We decided not to implement this in this sprint. | Limited resources may need to be prioritized for more immediate concerns, such as system stability, security patches, or critical bug fixes, so we postpone the plan to implement this in the next sprint, and push that to the future sprints when the system is more mature and scaled.
Recover from Faults(Preparation and Repair) | Does the system have consistent policies and mechanisms for reconfiguration after failures, reassigning responsibilities to the resources left functioning, while maintaining as much functionality as possible? | Y | Low | Utilize load balancing algorithms to distribute the workload evenly across available resources, ensuring optimal resource utilization and preventing overload on specific components. | Dynamic resource reconfiguration allows the system to optimize resource usage by redistributing tasks among available resources, preventing bottlenecks and overload, which contributes to a positive user experience by minimizing disruptions and maintaining essential functionalities.
Recover from Faults(Reintroduction) | Can the system operate a previously failed or in-service upgraded component in a “shadow mode” for a predefined time prior to reverting the component back to an active role? | Y | Low | Design the system to support a shadow mode by introducing configuration options that allow specific components to operate in a shadow or test mode. | Operating in a shadow mode mitigates the risk of introducing potential issues into the production environment. It provides a controlled testing ground to catch and address issues before full deployment.
Recover from Faults(Reintroduction) | If the system uses active or passive redundancy, does it also employ state resynchronization to send state information from active components to standby components? | N | Low | The system is always in active state. We ensure that state updates are sent in real-time or near real-time to keep the standby components synchronized with the active one. This minimizes the risk of data inconsistencies during failover. | Ensures that redundant components have consistent and up-to-date data, avoiding discrepancies between the active and standby states.
Recover from Faults(Reintroduction) | Does the system employ escalating restart to recover from faults by varying the granularity of the component(s) restarted and minimizing the level of service affected? | Y | High | Establish different levels of escalation based on the severity of the fault. For example:Level 1: Restart the affected component.Level 2: Restart a group of related components.Level 3: Restart the entire system. | Allows for a more targeted approach to fault recovery, addressing specific problematic components without affecting the entire system.
Recover from Faults(Reintroduction) | Can message processing and routing portions of the system employ nonstop forwarding, where functionality is split into supervisory and data planes? | Y | Low | Implement stateful switchover mechanisms so that if a failure is detected in the supervisory plane, the system can switch to the backup without losing the existing state. | It provides fault tolerance by allowing the system to gracefully handle supervisory plane failures without impacting the ongoing message processing and routing.
Prevent Faults | Can the system remove components from service, temporarily placing a system component in an out-of-service state for the purpose of preempting potential system failures? | N | Low | We don't have plan to implement replicas of system components to handle out-of-service state of system failure. | Limited resources may need to be prioritized for more immediate concerns, such as system stability, security patches, or critical bug fixes, so we postpone the plan to implement this in the next sprint, and push that to the future sprints when the system is more mature and scaled.
Prevent Faults | Does the system employ transactions—bundling state updates so that asynchronous messages exchanged between distributed components are atomic, consistent, isolated, and durable? | Y | High | Design a transactional model that defines the boundaries and scope of a transaction. Transactions are sets of operations that need to be executed atomically. In addition, for distributed systems, we consider using a two-phase commit protocol. Inthe first phase, participants agree to commit, and in the second phase, the actual commit or rollback is performed.Implement transaction logging to record the state changes made during a transaction. This log ensures that even in the event of a failure, the system can recover and maintain consistency. | Since the system is health-related, it is required to be high-availability service and need to manage several data bases. Using distributed locking mechanisms prevents conflicts between concurrent transactions in a distributed environment; and implementing acknowledgment mechanisms between distributed components ensures that all parties involved are aware of the transaction's progress.
Prevent Faults | Does the system use a predictive model to monitor the state of health of a component to ensure that the system is operating within nominal parameters?When conditions are detected that are predictive of likely future faults, the model initiates corrective action. | Y | Low | Implement continuous monitoring of the system using the trained predictive model. The model analyzes real-time or near-real-time data to assess the current state of health of system components. | Predictive health monitoring allows for the proactive identification of potential issues before they escalate into full-fledged faults. This proactive approach helps prevent service disruptions.

### Microservice #1: UI

#### Availability tactics

#### *Detect Faults* 
* **Rollback**
   - Microservice keeps a log of the status of the previous State it was in before a change has occurred. When the microservice is faced with a failure, it rolls back to this previous state.
   - 
#### **How to test availability tactics**: 
- We should be able to test this attribute by having a test function to access the values of the last previous stable state. If these values are accurate to what is intended, then we can assume our tactic is working as intended.


### Microservice #2: Patient Management
#### *Detect Faults* 
* **Ping/echo mechanism**
* **Monitor**: Microservice monitors connections between modules and databases, reporting any occurrence of network congestion or unstable connections.
#### **How to test availability tactics**: 
- Testing can be done by setting a baseline to define the normal expectations of connection between modules and database. We can add failure simulations to see the mechanism work as expected. <br>


### Microservice #3: Health Service Management

#### Availability tactics
#### *Detect Faults*:
* **Monitor**: Employ continuous monitoring mechanisms to assess the overall health of the system, including resource utilization, response times, and error rates.
* **Heartbeat, timestamp**: Implement heartbeat and timestamp mechanisms to regularly check the liveliness of components and detect potential issues, allowing for timely responses.
* **Voting**: Deploy replicated components to enhance fault tolerance. Replicas can handle increased loads and provide redundancy in case of failures.
* **Exception Detection and Handling**: Implement robust exception detection and handling mechanisms to gracefully manage unexpected errors and prevent cascading failures.
#### *Recover from Faults - Preparation and Repair*:
* **Rollback**: Incorporate rollback mechanisms to revert to a previous stable version in case a new deployment introduces issues or unforeseen errors.
* **Retry**: Integrate retry mechanisms for transient failures, allowing the system to automatically reattempt operations that initially failed.
* **Reconfiguration**: Dynamically reassign responsibilities to available resources when a component fails, ensuring continuous operation and minimizing downtime.
#### *Recover from Faults - Reintroduction*:
* **Shadow**: Implement a shadow mode for updates, allowing changes to be tested in a live environment without affecting the production system. This helps identify potential issues before full deployment.
* **Escalating Restart**: Establish different levels of escalation based on the severity of the fault.
* **Nonstop forwarding**: Utilize stateful switchover mechanisms to seamlessly transition from one component or service to another, maintaining the system's overall state.
#### *Prevent Faults*:
* **Transactions**: Enforce ACID (Atomicity, Consistency, Isolation, Durability) properties for databases to ensure data integrity, consistency, and reliability, especially in the face of failures.
### How to test availability tactics:
* **Deploy and Test in Staging/Testing Environment**: Perform thorough testing in a staging or testing environment to simulate real-world conditions and identify potential issues before deploying changes to the production environment.
* **Scale Down and Test**: Simulate component failures by intentionally scaling down replicas or shutting down specific services to assess the system's resilience and the effectiveness of fault-tolerance mechanisms.
* **Redundancy Testing**: Validate the redundancy and failover capabilities by intentionally causing failures in primary components and ensuring that backups or replicas seamlessly take over.
* **Rollback Testing**: Test the rollback mechanism by deploying a new version of the system, intentionally introducing errors, and verifying the system's ability to revert to the previous version.
* **Performance and Stress Testing**: Assess the system's performance and stress limits to ensure that it can handle peak loads and unexpected conditions without compromising stability.
* **Shadow Deployment Testing**: Validate updates in shadow mode by deploying changes to a subset of users or components and monitoring the impact before completing a full deployment.
<br>

## Design Patterns:

### Microservice #1: UI

**“State” pattern**: The UI Microservice implements the “State” pattern. This pattern allows an object to have specific functions according to the current State it is in. The object can switch between states through certain events or flags triggered by the system. In our microservice, this state is manifested through the different “States” the UI page can have. For example, the Account/Personal UI State has behaviors related to the managing and accessing the Account/Personal Information of the current user. The transitions between our states are usually activated by the user pressing a button, but many require conditional triggers to be able to transition.

### Microservice #2: Patient Management

**Repository pattern**: One design pattern our microservice adopts is the repository pattern, wherein different modules interact with distinct databases, providing a clear separation of concerns. For instance, one module handling a user’s Triage Record might access a separate database, while another module dealing with user account health information accesses its respective database. Such practices allow the microservice to achieve a high level of modularity and maintainability. This clear separation is beneficial for testing and mocking database interactions.

**Adapter pattern**: Another design pattern that can be applied to the system is the Adapter pattern. This is exemplified by the AccountInformationManagement module that accesses the User's Health Info database and the Account Information database. Although a distinction should be maintained between User's Health Info and Account Information, they are nonetheless related. By using the Adapter pattern in this case, the system can verify the existence of duplicate accounts or update user health information using a shared ID.
<br>

### Microservice #3: Health Service Management

**Abstract Factory Pattern to Implement the Suggestion Class**: Each health recommendation involves creating a suggestion, details, and interaction. By using an abstract factory, we encapsulate the logic of creating these related objects, making it easier to manage and modify the creation process in the future. The pattern also ensures that the created objects adhere to a consistent interface. This can be beneficial when dealing with various health recommendations, as it provides a clear and standardized way to interact with suggestions, details, and interactions. Abstract Factory promotes flexibility and extensibility. If we need to add new types of health recommendations or change the way existing recommendations are created, you can introduce new concrete factories without modifying the existing client code. This makes it easier to extend the system without causing ripple effects. Moreover, the pattern helps in separating the concerns of creating objects from the client code that uses these objects. This separation can improve the maintainability of our codebase by isolating the construction logic and reducing dependencies between different parts of the system. Lastly, by using an Abstract Factory, the code becomes more readable and maintainable. The intention of creating related objects is clear, and the client code is shielded from the complexities of object creation.
<br>

## State Models:

### Microservice #1: UI

![image](https://github.com/uvic-teach/project-m1-team8/assets/145606952/a5843c0c-4c3e-43f6-9b68-3a30f1362cc9)
<br>

#### **Description**: <br>
This State Machine Model describes the stateful behavior of the User Interface of the Mister Ed system. When a user first loads the system, they are in the Authentication state and must either log in successfully to continue to the main page or click “Sign up” or “Forgot password” to initiate a User Credential Form state which will return to Authentication after successful completion of the form. Once a user logs in successfully, the Main Page state allows them to click a button to traverse to one of the Notification, Personal/Health Info, or Triage UI States. The Notification state allows the user to view their current notifications. The Personal/Health Info state allows the user to Display and Manage User credentials and Health Info in the same manner as the Sign Up/Forgot password Form.

The Triage state allows the user to request a virtual triage and fill out the corresponding form, or traverse to the triage related UI States of Triage Result, ER Booking, and Check ED Load Status. The ER Booking state allows the user to create a booking if they have a suggestion flag to create one from their triage result, and if they have a booking they can display their booking info or cancel their booking. The Triage Result state allows the user to view their triage result if their result is ready. The Check ED Load state allows the user to check the current ED Load at nearby hospitals to see if a virtual triage is even necessary. This state is unique as it does not require a user to be authenticated to be accessed, so this state also links to the authentication state if a non-authenticated user wishes to use the rest of the system.
<br>

### Microservice #2: Patient Management

![Patient_Management_State_Diagram drawio](https://github.com/uvic-teach/project-m1-team8/assets/145606952/802ec6dd-3574-4f15-a381-91c8578c6454)
<br>

#### **Description**:
The state diagram represents the "Patient Management" process using the Mister ED System. Initially, the user interacts with the system by either requesting to log in or clicking on "Create an Account." In the account creation pathway, the system directs the user to a registration website where they input their credentials to establish a new account. Upon successful registration, the Mister ED System sends a confirmation email. The user completes the registration by confirming the email. In the login pathway, upon the user's request to log in, the system checks the user's credentials. If they are valid, the login is successful; if not, the account is marked as invalid. Post-login, the user can request to access personal health information or their triage record. The system acknowledges these requests by receiving them and then subsequently shows the requested data, be it personal health records or triage record history, stored within the system.
<br>

### Microservice #3: Health Service Management

![image](https://github.com/uvic-teach/project-m1-team8/assets/145606952/154683b9-6df3-47ba-b7b2-9f694a0ab94f)
<br>

#### **Description**:
First, the system has to be authenticated before being able to request triage and move to the triage request created state. After that, a triage record will be created, depends on the status of the triage record (whether it's completed or still in progress), the system will transit to "triage record being calculated" or "triage complete" states. When the triage result is available, based on the result, the system will go to the suitable branch and retrieve the necessary info. If the triage result suggests the patient visiting the ER, the system will go to the ER booking initialized state, then ER booking confirm state. While the slot number is greater than 0, the patient remains in queue in the queue until the slot number = 0. If the patient doesn't visit the ER during a period of time, their ER booking will be canceled and they have to re-book the ER again.

## Activity Models: 

![activity_model](https://github.com/uvic-teach/project-m1-team8/assets/99488911/3362cefb-a440-4415-b190-930881acb615)

#### **Description**:
We start at the login page, where we can either continue to login or choose to register. If we choose to register, the account must be unique and not already exist. When we login, the credentials are checked and either the user is logged in or they are sent back to login with an error message. Once logged in, we display the account page. From that page, we can either check ED load or request triage. 


To perform triage, an assessment form is sent to the user and once it filled in form is returned, the assessment form is compared to the user's health info. After assessing the situation, the recent triage is saved and a recommendation is provided. If ER is needed, then the user is notified to book an appointment. The user inputs the location they are at and the system checks for available spots at the nearest ER to their location. If a spot is available, get the user to register at the available spot. Otherwise, prompt the user to find a different location.

If the ER is not needed, the user can ask for information on their recommended action. The system will then gather data on the recommended action and display to the user the best approach to completing the recommended action.
<br>

## Contributions: 

# Team Contribution
| Team Member                  | Task                                                                                                                                                                     |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Hang Duong                   | - Implemented Health Service Management Microservice. <br>  - State Diagram and Diagram. <br> - Design Pattern Description. <br> - Architectural Tactic questionaire list and description. <br> - Reviewed, editted and gave feedback on Wiki Page. |
| Dhuruvan Anavaratha Krishnan | - Patient Management Microservice. <br> - State Diagram and Description. <br> - Architectural Tactic description. <br>  - Constructed Design Pattern Description. <br> - Reviewed the codes for the microservice. <br> - Created and worked on the Wiki page. <br>                                                                              |
|  Minh Nguyen                 | - Patient Management Microservice. <br> - Activity Diagram. <br> - Architectural Tactic Description. <br> - Wrote the codes for the microservice. <br> - Setting up Docker. <br>                                                                                                 |
| Miles Rose                   | - Front Page UI Microservice. <br> - Back-end coding.<br> - Setup FastAPI, and React. <br> - State Diagram and Description. <br> - Design Pattern Description. <br> - Architectural Tactic Description. <br>                                                                                      |
| Oliver Ware                  | - Front Page UI Microservice. <br> - Edited/Fixed React. <br> - Created the basic Webpage. <br> - Activity Diagram and Description. <br> - Design Pattern Description. <br> - Architectural Tactic Description. <br> - Reviewed the Wiki page. <br>|

