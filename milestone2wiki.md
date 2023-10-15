## Design - Component & Connector View
### Component Diagram


#### Health Service Management Subsystem
**Components**:
The subsystem Health Service Management consists of 6 components:
- TriageEngine: Process request related to triage and compute the triage result based on the patient info input.
- ERManagement: Manage the state of the current ER capacity.
- NurseDatabase: Store the information related to nurses.
- ClinicDatabase: Store the information related to clinics.
- MedicineDatabase: Store the information related to medicine and pharmacy.
- ERDatabase: Store the information related to state and status of ER Queue in all hospitals in Canada.

**Connectors**:
__Internal (Among the components)__
- The TriageEngine requires interface Nurse, Clinic from NurseDatabase, ClinicDatabase respectively, and  Medicine and Pharmacy interface from MedicineDatabase. 
- The ERManagement requires interface ERData from ERDatabase and provides interface ER to the TriageEngine.

__External__
- __With Front Page UI Subsystem__:
  - Between `ERManagement` and `ERService` from the Front Page Subsystem: `ERService` component requires `ERBookingStatus` and `ERBooking` interface that `ERManagement` component provides, as well as `ERQueue` for Checking Current ER Queue Capacity. 
  - Between `TriageEngine` and `TriageServive` from the Front Page Subsystem: TriageServive component requires TriageResult and `TriageSuggestion` interface that `TriageEngine` component provides.
  - Between `TriageEngine` and `NotificationService` from the Front Page Subsystem: `NotificationService` component requires  `TriageResultNotifcation` interface that `TriageEngine` component provides.
- __With Patient Management Subsystem__:
  - Between the `TriageEngine` and `TriageRecord` component from the Patient Management Subsystem: `TriageRecord` component requires  `TriageResults` interface that `TriageEngine` component provides.

#### Patient Management Subsystem
One of the components in the Patient Management Component Diagram is the `TriageRecord`, which is responsible for maintaining a comprehensive log of all triages conducted by the user. This component plays a vital role in tracking and organizing user interactions within the triage system, ensuring a detailed record of all triage-related activities. Another essential component is the `Account Management`, which is further divided into two distinct branches: `HealthInformation` and `AccountInformation`. The HealthInformation branch stores crucial details about the user's health, forming a repository for pertinent health-related data. On the other hand, the `AccountInformation` branch encompasses essential user account details, including username, password, and other relevant information. These components collectively form a robust structure, facilitating efficient management of both user interactions and sensitive account data within the system.
*Components:**

The subsystem, which represents Patient Management as a microservice, comprises 5 components:
**Components:**

- _TriageRecordManagement:_ Provides information to the UI about the patient's triage history by accessing the _TriageRecord_ database.
- _TriageRecord database:_ Contains information about the patient's triage history.
- _AccountInformationManagement:_ Handles requests from the patient to create an account and authenticates user credentials for logging in. It also allows patients to access personal health information.
- _HealthInformation database:_ Contains information about the patient's personal health information.
- _AccountInformation database:_ Contains information about the patient's user account.

**Connectors:**
__Internal__ (Within the Patient Management subsystem)
- `TriageRecordManagement` requires the `TriageInfo` interface from the `TriageRecord` database.
- `AccountInformationManagement` requires `UserHealthInfo` and `AccountInfo` interfaces from the `HealthInformation` database and the `AccountInformation` database, respectively.

__External__
Between the Patient Management and UI subsystems:
- The `LogIn` service component in the UI requires the `TriageRecord` interface from `TriageRecordManagement`, as well as the `UserInfo` and `UserValidation` interfaces from `AccountInformationManagement`.
- The `Register` service component in the UI requires the `UserAccount` interface from `AccountInformationManagement`.
Between Patient Management and Health Service Management:
- `TriageRecord` requires `TriageResult` from the `TriageEngine` component in Health Service Management.

### Sequence Diagram
#### Use Case UC-01 System Overview
![Sequence Diagram](assets/images/general_sequence_diagram.jpg)
#### Description:
- **Participant**:
  - Patient (type: Actor)
  - Account Page (type: PageUI)
  - Virtual Triage (type: Virtual Triage module)
  - HealthService Database (type: Database)
  - Patient Database (type: Database)

- **Fragments**:
  - OPT Fragments for ER Service, Nurse Service, Pharmacy Visit, Clinic Visit.

- **Process**:
  - __Account Creation__: The patient can begin utilizing MisterEd by establishing an account, providing basic information during the registration process. The input will be securely stored in the Patient Database for both record-keeping and authentication purposes. Upon successful account creation, the patient will be directed to a summary page, showcasing the details of their newly established account.
  - __Logging in (Authentication)__: The patient is required to provide their username and password to access their accounts. The submitted credentials will be compared with records in the Patient Database. Upon successful authentication, users will be directed to the summary page of their account.
  - __Checking ED Capacity__: When the patient click the button to check the capacity of the nearest ED, the account page will request relevant information from the Health Service Database. The obtained information will be displayed to the patient.
  - __Requesting a Virtual Triage__: When patients click the button to request a Virtual Triage, they are required to provide recent basic health information, which will be sent to update records in the Patient Database. The health input is also used to initiate a triage with the Virtual Triage module. Based on the health input, the following options will be suggested.
    - _Visiting the Nearest ER_: If a visit to the ER is necessary, the account page will notify the patient of the recommendation. Once the patient requests the service, the Account Page will gather relevant patient information from Patient's Database, such as health status and location, which will then be used to query the Health Service Database for the nearest ED location. The account page will also search for any available spots in the queue and, if available, the patient will be notified of its availability.
    - _Contacting a Nurse_: If reaching out to a nurse is necessary, the account page will notify the patient of the recommendation. Once the service is requested, the Account Page will retrieve relevant patient information, such as health status and location, from the Patient Database. This information will be utilized to query the Health Service Database for the appropriate nurse hotline. The patient will be notified of the hotline to contact the nurse.
    - _Visiting a Clinic_: If a clinic visit is recommended, the account page will inform the patient of this advice. Upon service request, the Account Page will extract pertinent patient information, like health status and location, from the Patient Database. This data will subsequently be used to query the Health Service Database to identify the nearest clinic. The patient will then be notified of the location to visit.
    - _Taking Medication_: If taking prescribed medication is necessary, the account page will notify the patient of this recommendation. Upon service request, the Account Page will retrieve pertinent patient information, such as health status and location, from the Patient Database. This information will then be used to query the Health Service Database to identify the nearest pharmacy. Subsequently, the patient will be informed of the pharmacy location to visit.

### Sequence Diagram Specification
#### Use Case UC-02 User Authentication
![Login Sequence Diagram](assets/images/Login%20sequence.png)
For login we have a patient/user, a login page that takes a username and password, a authenticator module that takes the inputted user/pass and verifies it with the database, and the patient database labeled PatDB.
Alternative sequences in the diagram include the case where the patient has the wrong login details, and the case where the patient has forgotten their password

1) Start with Patient and move to login page as it loads.
2) Login page requires Login credentials and the user inputs the credentials into a box.
3) The login button is pressed on the page moving to the Authenticator.
4) Authenticator checks in with the patient database and validates/invalidates a patient.
5) Update login status (logged out for invalid, logged in for valid).
6a) If valid - load patient dashboard
6b) If invalid - reload loginpage with error message

**Alt task for login: forgot password:**
1) Load the login page
2) Page requests Login credentials but patient selects "forgot password" button.
3) Page requests username then patient inputs username.
4) The button "Send email" is selected and a confirmation email is sent.
5) Authenticator validates the username from the database and sends a verify email.
6) User inputs data from email and their new password to the page and the page sends the data to the authenticator.
7) The authenticator verifys the email data and the page sends an update message to the database.
8) The password is updated and a notification for successful password change is sent.

![Registration Sequence Diagram](assets/images/Registration-Sequence-Diagram.png)
For the Mister ED System, this sequence diagram outlines the streamlined process of user registration. Initiated by the patient/user, the sequence commences when they click the "Registration" button on the welcome/home page. Upon this action, the system redirects the user to a dedicated registration page where they input their desired login credentials. The system rigorously validates these credentials with the patient database, ensuring the uniqueness and compliance with system requirements. If successful, the system creates a new account for the user and sends the user a verification email to validate the user’s new account. After the verifies the email, the registration process is complete. The alternate outcome of this scenario that might occur is if the user attempts to re-register with existing credentials.
If the user tries to re-register with existing credentials then the system would send the “Account already Exists” message to the user, so that the user could enter different credentials to create their account.

#### Use Case UC-03 Perform Virtual Triage
![Virtual Triage](assets/images/VirtualTriage.png)

In the Virtual Triage sequence, the process initiates with the user logging into the Mister ED System. Upon login, the user triggers the virtual triage. The system responds by retrieving questions from the Triage Module for the user, then evaluating the severity of their medical condition based on the answers provided by the user. Based on the user's responses, the system determines the appropriate course of action, directing the user to either visit the Emergency Room (ER), a nearby clinic, or a pharmacy for over-the-counter medicine.
Alternatively, the user can opt for a remote consultation via the nurse hotline. Throughout this process, the system ensures a seamless flow of interactions, confirming the user's choice and providing additional instructions when necessary. At the end of the triage, the result on what action the user should follow would be displayed on the user’s screen, and the patient database to keep a log of the triages, and the results.

#### Use Case UC-04 Notify Triage's Result
![Notify](assets/images/notify.png)

__Participant__:
- Patient (Actor)
- Login Page (type: PageUI)
- Triage Result Page (type: PageUI)
- Notification Module (type: NotificationSvc)
- Patient Database (type: Database)
- HealthService Database (type: Database)


__Combined Fragments__:
- Alt Fragment for the suggestion process
- Ref Fragment to Login Use case
- Ref Fragment to Check ER Capacity and Assign Patient to ER Queue

__Process__:
- When the triage result is available, the Notification Service will send a notification to patient via email or text message.
- Then the patient can click on the link attached in the email/text message to be redirect to the login page.
- The patient is required to log in first before viewing their triage result. Therefore, the diagram refers to the sequence diagram of authentication use case.
- After patient logs in successfully, the system will redirect user to the result page, the UI also send request to get the triage results summary from Patient Database, and display the information to the patient.
- Based on the result, there would be 3 different scenarios:
    - If the patient is suggested to take counter medicine, the triage page will display a message suggesting patient to take counter medication, the user can click on the button and the UI will send request to get patient info, such as location, allergies, as well as list of pharmacies near-by patient's location, then display that to patient.
    - If the patient is suggested to contact nurses/clinician, the triage page will display a message suggesting patient to take contact nurses/clinician, the user can click on the button to get more help and the UI will send request to get patient info, such as location, health record, as well as list of available nurses/clinic near-by patient's location and their contact, then display that to patient.
    - If the patient is suggested to visit the ER, the triage result page will display a message suggesting patient to visit ER, and ask if the patient wants the system to help them book and be placed in ER queue. If the patient agrees, they will be redirect to Booking ER page to the Check ER current capacity and assign patient to ER Queue Use case.
- Alternatively, patient can click on the button to view the detail of their triage result instead of summary.

#### Use Case UC-05 Assign User To ER Queue
![Booking ER](assets/images/booking_er_sequence.png)

#### Use Case UC-06 Check ER Queue Load
![Check ER Status](assets/images/Check_Ed_Status.png)
Involved in checking the ED load are a patient/user, a database labelled edb, and a status page to display the requests from the database based on location data provided by the user.

1) Load the status page.
2) the page requests a Location and the patient inputs one then hits enter.
3) the page requests the load data from the database for that location.
4) the ED load is displayed on the status page for the patient to see.

## Allocation View
### Front Page UI Microservice
![UI](assets/images/Deployment_diagrams/UI_deployment.png)

### Health Service Mangement Microservice
![Health Service Management](assets/images/Deployment_diagrams/health_service_management.png)
#### Tech stack:
- **Python**: The main programming language for developing the service and leveraging libraries such as SQLAlchemy and FastAPI.
- **SQLAlchemy**: Used for interacting with databases and managing health service-related data efficiently.
- **FastAPI**: FastAPI is used to implement the API that allows interaction with the service. The API exposes endpoints for managing triage, accessing health service databases, and retrieving the state of the ER queue. FastAPI offers a modern and efficient way to build APIs with automatic interactive API documentation.

#### Service Components:

- **Triage Management**:
The triage management component handles the assessment and categorization of patients based on their medical condition and urgency. It assigns a triage level to each patient, indicating the severity of their condition, then suggests whether the patient needs to visit ER or take other actions. This component also manages the databases related to the health services. It stores and retrieves information about nurses details, clinic details, medicine information, medical inventory, and other relevant data. SQLAlchemy is used to interact with these databases.

- **ER Management Model**:
The ER Management component keeps track of the patients in the queue, their priority levels, estimated wait times, and other relevant information. It ensures a smooth flow of patients through the ER.

- **Database**:
The microservice uses Relational database to store the information for nurses, clinician, medicine, and ER.
   
#### Integration and Communication:
The Triage management and ER Management components interact to ensure that patients are placed in the queue based on their triage results if necessary. The health service databases management component integrates with both the triage management and ER queue components to fetch and update relevant information based on patient assessments.

#### Demo
[Health-svc-management-api-gcp-demo.webm](https://github.com/uvic-teach/project-m1-team8/assets/47402970/d7fe7b40-8da2-4288-9470-613ae7e65c36)

### Patient Mangement Microservice
![Patient Management](assets/images/Deployment_diagrams/patient_management.jpg)

At the heart of the system lies a Patient Database Server, running on a Linux operating system, serving as the central repository for patient data. This server hosts two critical schemas: TriageRecordSchema and UserHealthInfoSchema, which define the structure and relationships within the patient records. The communication between the server and the application components is facilitated through FastApi, a modern and efficient web framework.FastApi acts as the bridge, ensuring seamless interactions between the server and the User Interface (UI).
The system's architecture extends further with the incorporation of an Account Management execution environment. This component manages user accounts and interactions, ensuring data security and access control. Additionally, the system incorporates a Patient: Relational Database execution environment, emphasizing the utilization of relational database management systems tailored specifically for patient data. The integration of SQLAlchemy, a powerful SQL toolkit, enhances database management efficiency, ensuring smooth communication between the server and the schemas. In this configuration, the system's components are interlinked, guaranteeing a secure, efficient, and highly responsive healthcare management system that caters to diverse user needs.

### Team Contribution

| Sub-team                                   | Microservice                          | Task                                                                                        |
|--------------------------------------------|---------------------------------------|---------------------------------------------------------------------------------------------|
| Miles Rose &  Oliver Ware                  | Front Page UI Microservice            | - Component Diagram (WIP) <br> - Deployment Diagram (WIP)                                           |
| Hang Duong                                 | Health Service Mangement Microservice | - Component Diagram <br> - Deployment Diagram <br> - Service Demo on GCP <br> - API Documentation on SwaggerHub |
| Dhuruvan Krishnan Anavaratha & Minh Nguyen | Patient Mangement Microservice        | - Component Diagram (WIP) <br> - Deployment Diagram <br> - API Documentation on SwaggerHub                      |

## Interface specifications
### Front Page UI Microservice

### Health Service Mangement Microservice
[Link to API Documentation](https://app.swaggerhub.com/apis-docs/HangD/myster-ed_health_svc_management/0.1.0#/default/)

### Patient Mangement Microservice
[Link to API Documentation](https://app.swaggerhub.com/apis-docs/minhn201/patient_management_m2/1.0.0#/)

## Team Contribution
| Team Member                  | Task                                                                                                                                                                     |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dhuruvan Krishnan Anavaratha | - Sequence Diagram for Login and Perform Triage Usecases<br>  - Patient Management Microservice                                                                               |
| Hang Duong                   | - Sequence Diagram for Notify Usecase<br> - Health Service Management Microservice<br> - Reviewed and gave feedback other team members' PRs.<br> - Worked on the wiki page. <br> |
|  Minh Nguyen                 | - Sequence Diagram for General System<br>  - Patient Management Microservice                                                                                                   |
| Miles Rose                   | - Sequence Diagram for Assign User to ER QueueUsecase<br>  - Front Page UI Microservice                                                                                       |
| Oliver Ware                  | - Sequence Diagram for Login and Check ER Load Usecase<br>  - Front Page UI Microservice                                                                                      |
