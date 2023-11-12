//import React, {useState, useEffect} from 'react'
//import api from './api'
import { BrowserRouter, Route, Routes} from 'react-router-dom';
import MainPage from "./Pages/MainPage";
import UserInfo from "./Pages/UserInfo";
import AuthenticationPage from "./Pages/Authentication";

const App = () => {

/*
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
*/
  return (
    <div>
      <nav>
        <ul>
        <li><a href="/authentication/">Login/Register</a></li>
          <li><a href="/notifications/">Notifications</a></li>
          <li><a href="/userinfo/">UserInfo</a></li>
          <li><a href="/">MainPage</a></li>
        </ul>
      </nav>

      <BrowserRouter>
        <Routes>
        <Route path="/authentication/" element={<AuthenticationPage/>}>
            </Route>
         
          <Route path="/userinfo/" element={<UserInfo/>}>
            <Route />
          </Route>
          <Route path="/" element={<MainPage/>}>
          </Route>
        </Routes>
      </BrowserRouter>
      
    </div>
)
}
/*

          <Route path="/notifications/" >
            </Route>
*/
export default App;

