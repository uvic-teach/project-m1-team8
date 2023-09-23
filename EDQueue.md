| Use case       | UC-4 ED Queue   <br> history created 21/09/2023 Miles Rose, last modified 22/09/2023 |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | User is assigned to an appropriate ED queue position using user location and virtual triage data.              
| Actors         | Patient/User (primary) <br> ED front desk operator                                                             
| Assumption     | The patient provides correct information about their health condition and finishes the triage and their data                       is correctly processed.                                                                             |
| Steps          | 1. The information from the triage is used to determine the position in ED queue that the user will take. <br> 2. User is informed of their current position in queue through notifaction use case <br>  3. When the user has reached the front of the queue, they will be notified again to come to the ED. <br> 4. When the user arrives at the ER, they are ID'd and matched to their online information, and then processed accordingly. <br> 5. Once processed the user is removed from the queue.
| Variations     |   #1 User may decide to cancel and be removed from the queue. <br> #2 User fails to arrive within specified time frame, they are removed from the queue and notified.
| Non-functional |                                                                         
| Issues         |                      |

| Use case extension      | UC-4.1 ED Queue User Exit **extends** ER queue
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Change    | User is removed from ED queue  |                                                             
| Assumption     | User is currently in ED queue                                                                             |
| Steps          | 2. User presses button to cancel position in ED queue <br> 2.1 System removes user from queue <br> 2.2 User is notified they were removed from queue. |


| Use case extension      | UC-4.2 ED Queue User Timed Out **extends** ER queue
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Change    | User is removed from ED queue                                                                      
| Assumption     | 1. User is currently in ED queue <br> 2. User has exceeded given time period for ED visit|
| Steps          | 3. User is removed from ED queue <br> 3.1 User is notified that they have failed to show up in their alloted time and have been removed from the queue. |



                                            
                                    
