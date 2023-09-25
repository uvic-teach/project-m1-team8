| Use case       | UC-4 ED Queue   <br> history created 21/09/2023 Miles Rose, last modified 24/09/2023 |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | User is assigned to an appropriate ED queue position using user location and virtual triage data.              
| Actors         | Patient/User (primary) <br> ED front desk operator                                                        
| Assumption     | The patient provides correct information about their health condition and finishes the triage and their data is correctly processed. |
| Steps          | 1. Check ED load, if there is space available notify user to head to ED 2. The information from the triage is used to determine the position in ED queue that the user will take. <br> 3. User is informed of their current position in queue through notifaction use case <br>  4. When the user has reached the front of the queue, they will be notified again to come to the ED. <br> 5. When the user arrives at the ED, they are ID'd and matched to their online information, and then processed accordingly by ED front desk operator. <br> 6. Once processed the user is removed from the queue.
| Variations     |   #1 User may decide to cancel and be removed from the queue. <br> #2 User fails to arrive within specified time frame, they are removed from the queue and notified.|
| Non-functional |   Reliability: ED queue system must be reliable 95% of the time. Down time is acceptable as users will just go to the ED in person. <br> Priority: ED queue system must be able to effectivley decide urgency and priority of users in such a manner that users do not deem it nessecary to show up to the ED before their alloted time. |
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


                                            
                                    
