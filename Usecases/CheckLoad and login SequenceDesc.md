### CheckLoad:<br>
Involved in checking the ED load are a patient/user, a database labelled edb, and a status page to display the requests from the database based on location data provided by the user.

1.) Load the status page<br>
2.) the page requests a Location and the patient inputs one then hits enter<br>
3.) the page requests the load data from the database for that location
4.) the ED load is displayed on the status page for the patient to see

### Login:<br>
For login we have a patient/user, a login page that takes a username and password, a authenticator module that takes the inputted user/pass and verifies it with the database, and the patient database labeled PatDB.
Alternative sequences in the diagram include the case where the patient has the wrong login details, and the case where the patient has forgotten their password<br>

1.)Start with Patient and move to login page as it loads<br>
2.)Login page requires Login credentials and the user inputs the credentials into a box<br>
3.)the login button is pressed on the page moving to the Authenticator<br>
4.)Authenticator checks in with the patient database and validates/invalidates a patient<br>
5.)Update login status (logged out for invalid, logged in for valid)<br>
6a.) valid - load patient dashboard<br>
6b.) invalid - reload loginpage with error message

#### alt task for login: forgot password:<br>
1.)load the login page<br>
2.)page requests Login credentials but patient selects "forgot password" button<br>
3.)page requests username then patient inputs username<br>
4.)The button "Send email" is selected and a confirmation email is sent<br>
5.)Authenticator validates the username from the database and sends a verify email<br>
6.) user inputs data from email and their new password to the page 
and the page sends the data to the authenticator<br>
7.) the authenticator verifys the email data and the page sends an update message to the database<br>
8.)The password is updated and a notification for successful password change is sent

