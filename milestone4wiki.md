# MisterEd

## Software Architecture Documentation (SAD)

## Goal and implementation
### 1. Patient Management Service
#### 1.1 Objective
- Design and implement the modules for account and triage managements, with their respective databases.
- Deploy them online using Docker and Google Cloud services.
- Integrate the microservice with the rest of the system.
#### 1.2 Result
- The microservice as a whole is implemented and successfully functioning.
- The system is deployed using Docker and Google Cloud services as intended.
- Integration is considered but not being implemented due to a lack of feasibility.

### 2. Health Management Service
#### 2.1 Objective
- Fully implement the prototype of triage module
- Fully implement the prototype of ER module
- Deploy the service with database on GCP
#### 2.2 Result
- ER module prototype is implemented
- Triage module is WIP
- Local database is setup
- Docker image is built and pushed to DockerHub
- Helm Chart to deploy the service to GCP
- 
### 3. User Interface Service
#### 3.1 Objective
- Fully implement the prototype of Frontend
- Fully implement the prototype of Backend
- Explore deployment possibilities
#### 3.2 Result
- Backend prototype is implemented
- Deployment possibilities explored but not implemented

## Team Contribution
| Team Member                  | Task                                                                                                                                                                     |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dhuruvan Krishnan Anavaratha | - SAD: Behaviour and Constraints for Module, Interface and Context Diagram for Allocation View, for Patient Management Service, and Behaviour for C&C diagram.|
| Hang Duong                   | - Health Management Service (codebase, cloud deployment). </br> - SAD: Problem definition, Module and Allocation View for Health Management Service, Context Diagram for C&C diagram.|
|  Minh Nguyen                 | - Code Development for Patient Management Microservice. </br> - Contribute to SAD, primarily writing module and allocation view descriptions for Patient Management microservice. |
| Miles Rose                   | - User Interface Service (Backend Development). </br> - SAD: Solution Background, Module and Allocation View for User Interface Service, and the View Description, Elements, and Relations and Context Diagram for C&C view.|
| Oliver Ware                  | |
                                                       
