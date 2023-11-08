import React, {useState, useEffect} from 'react'
import api from './api'

const App = () => {

  const[notifications, setNotifications] = useState([]);
  const[formData, setFormData] = useState({
    message: '',
    username: '',
    date: ''
  });


  const fetchNotifications = async () => {
    const response = await api.get('/notifications/');
    setNotifications(response.data)
  }

  useEffect(() => {
    fetchNotifications();
  }, []);

  const handleInputChange = (event) => {
    const value = event.target.type === 'checkbox' ? event.target.checked: event.target.value;
    setFormData({
      ...formData,
      [event.target.name]: value,
    });
  };

  const handleFormSubmit = async (event) => {
    event.preventDefault();
    await api.post('/notifications/', formData);
    fetchNotifications();
    setFormData({
      message: '',
      username: '',
      date: ''
    });
  }

  return (
    <div>
      <nav className = 'navBar navbar-dark bg-primary'>
        <div className = 'container-fluid'>
          <a className = 'navbar-brand' href ="#">
            MisterEd App
          </a>
        </div>
      </nav>

      <div className = 'container'>
        <form onSubmit={handleFormSubmit}>

          <div className = 'mb-3 mt-3'>
            <label htmlFor='message' className='form-label'>
              Message
            </label>
            <input text = 'text' className='form-control' id = 'message' name= 'message' onChange = {handleInputChange} value= {formData.amount}/>
          </div>

          <div className = 'mb-3'>
            <label htmlFor='username' className='form-label'>
              Username
            </label>
            <input text = 'text' className='form-control' id = 'username' name= 'username' onChange = {handleInputChange} value= {formData.amount}/>
          </div>

          <div className = 'mb-3'>
            <label htmlFor='date' className='form-label'>
              Date
            </label>
            <input text = 'text' className='form-control' id = 'date' name= 'date' onChange = {handleInputChange} value= {formData.amount}/>
          </div>

          <button type='submit' className='btn btn-primary'>
            Submit
          </button>

          <table className='table table-striped table-bordered table-hover'>
            <thead>
              <tr>
                <th>Message</th>
                <th>Username</th>
                <th>Date</th>
              </tr>
            </thead>
            <tbody>
              {notifications.map((notification) => (
                <tr key={notification.id}>
                  <td>{notification.message}</td>
                  <td>{notification.username}</td>
                  <td>{notification.date}</td>
                </tr>
              ))}
            </tbody>
          </table>
        

        </form>
        </div>
    </div>
)
}

export default App;
