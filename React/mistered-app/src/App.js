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
    </div>
)
}

export default App;
