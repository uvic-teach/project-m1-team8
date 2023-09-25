

Welcome to the project-m1-team8 wiki!

1. System Description:

"Provides a comprehensive, insightful, and detailed overview of the application, its objectives, and goals."

The MisterEd system allows users to both check the current load of the ER as well as register/log in for a virtual triage. After this virtual triage is complete, their patient data will be updated and the user will be notified of which actions they should follow. If it is deemed necessary, the user will be added to virtual ER queue with a queue number determined by urgency. The user will then be notified when the ER is ready for them (front of the queue). The system will secure a spot at the ER for the user for a certain amount of time, after which the user will be removed from the queue. If an ER visit is deemed unnecessary, the user will be notified with information relaying them to either a nurse hotline, regular primary care clinic, or over-the counter-medication.

2. Use Case View

    Here is our groups use case diagram:
    ![Use Case Diagram](https://ibb.co/Z6MJ879)

   Here are our groups individual use case descriptions:

| Use case       | UC-4 ED Queue   <br> history created 21/09/2023 Miles Rose, last modified 24/09/2023 |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | User is assigned to an appropriate ED queue position using user location and virtual triage data.              
| Actors         | Patient/User (primary) <br> ED front desk operator                                                        
| Assumption     | The patient provides correct information about their health condition and finishes the triage and their data is correctly processed. |
| Steps          | 1. The information from the triage is used to determine the position in ED queue that the user will take. <br> 2. User is informed of their current position in queue through notifaction use case <br>  3. When the user has reached the front of the queue, they will be notified again to come to the ED. <br> 4. When the user arrives at the ED, they are ID'd and matched to their online information, and then processed accordingly by ED front desk operator. <br> 5. Once processed the user is removed from the queue.
| Variations     |   #1 User may decide to cancel and be removed from the queue. <br> #2 User fails to arrive within specified time frame, they are removed from the queue and notified.|
| Non-functional |   Reliability: ED queue system must be very reliable to have user trust. <br> Priority: ED queue system must be able to effectivley decide urgency and priority of users. |
| Issues         |   How does the ED staff interact with the system? How are in-person ED visitors accounted for in the system? |

| Use case extension  | UC-4.1 ED Queue User Exit **extends** ER queue|
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Change         | User is removed from ED queue  |                                                             
| Assumption     | User is currently in ED queue|
| Steps          | 2.1 If the user clicks on the "remove from queue" button then they are removed from ED queue <br> 2.2 User is notified they were removed from queue. |


| Use case extension  | UC-4.2 ED Queue User Timed Out **extends** ER queue|
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Change         | User is removed from ED queue |                                                                    
| Assumption     | 1. User is currently in ED queue <br> 2. User has exceeded given time period for ED visit|
| Steps          | 2.1 If the user fails to arrive within specified time period, then they are removed from queue in the system. <br> 2.2 User is notified that they have failed to show up in their alloted time and have been removed from the queue. |
| Issues         | Timing can be tricky, if someone is in serious peril they shouldn't be turned away because of technicality |


                                            
                                    

2. Contributions

Everyone collaborated to setting up team communication (Discord) and team expectations.

Everyone contributed collaboratively to the designing of the general road map to decide on our use cases.

Each member was assigned 1 use case to complete on their own time.

Miles wrote the system description and team members reviewed the writing and suggested edits and additions.

