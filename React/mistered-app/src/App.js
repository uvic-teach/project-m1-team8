import React, {useState, useEffect} from 'react'
import api from './api'
import { BrowserRouter, Route, Routes} from 'react-router-dom';

const App = () => {

  const[notifications, setNotifications] = useState([]);
  const[formData, setFormData] = useState({
    message: '',
    username: '',
    date: ''
  });


  const fetchNotifications = async () => {
    const response = await api.get('/Pages/Notifications.html');
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
    await api.post('/Pages/Notifications.html', formData);
    fetchNotifications();
    setFormData({
      message: '',
      username: '',
      date: ''
    });
  }

  return (
    <div>
      <nav>
        <ul>
        <li><a href="localhost:/authentication">Authentication</a></li>
          <li><a href="/Notifications">Notifications</a></li>
          <li><a href="/userinfo">UserInfo</a></li>
          <li><a href="/">MainPage</a></li>
        </ul>
      </nav>
      <BrowserRouter>
        <Routes>
          <Route path="/Notifications" >
            </Route>
         
          <Route path="/userinfo">
            <Route />
          </Route>
          <Route path="/">
            <Route />
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
)
}

export default App;

