The UI microservices is split into 4 subservices<br>
#### 1.)Authentication<br>
- this service contains two actions: a login and register action<br>
- login: communicate with account information to validate credentials<br>
- register: communicate with account information to add new dredentials to account information<br>
#### 2.)Notification<br>
- this service generates and displays notifications when various tasks occur<br>
- some tasks include account info updates, updates to the triage record
#### 3.)TriageHandler<br>
- this service allows for triages to occur and triage records to be accessed.<br>
- communicates with the triage engine to perform triage<br>
- communicates with the triage record to get history

#### 4.)ER Service<br>
- this service allows for checking the current ED load from the ERDataSource<br><br>

Connectors:
#### internal:<br>
- Triage services requires the user to be logged in (from authentication)

#### External:<br>
- Authentication requires patient management to create patient credentials and validate patient credentials
- ERService requires ERDataSource from Health service management to determine load
- Notification services require patient management to determine changes in stored data to notify the patient about
- Triage services requires both patient management to access triage history and the triage engine from Health service management to perform a triage


