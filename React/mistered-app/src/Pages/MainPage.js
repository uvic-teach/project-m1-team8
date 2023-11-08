import React from "react";
import Info from "../Components/Info";
import Notifications from "../Components/Notifications";
import Authentication from "../Components/Authentication";


function MainPage() {
  return (
    <div className="main page">
      <Navbar />
      <Info />
      <Notifications />
      <Authentication />
    </div>
  );
}

export default MainPage;