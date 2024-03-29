import React from 'react';
import './HomePage.css';
import { FaUserCheck, FaUserPlus, FaQuestionCircle } from "react-icons/fa";

const HomePage = (props: any) => {
    return (
        <div className="home-page">
            <div className={""}></div>

            <img src={`${process.env.PUBLIC_URL}/logo.png`} width={250} height={250} alt="Logo" className="homepage-logo"/>
            <video autoPlay={true} loop={true} muted={true} className={"background-video"}>
                <source src={"/Videos/rain_in_reverse.mp4"} type={'video/mp4'}/>
            </video>
            <span className="text-gradient">Under the Weather</span>
            <div className="button-container">
                <button className={"custom-button"} onClick={() => props.onFormSwitch("login")}>
                    <FaUserCheck/>
                    <br/>
                    Login
                </button>
                <a href={"https://github.com/superhvarn/under-the-weather/blob/main/README.md"} target={"_blank"}>
                    <button className={"custom-button"}>
                        <FaQuestionCircle/>
                        <br/>
                        Help
                    </button>
                </a>
                <button className={"custom-button"} onClick={() => props.onFormSwitch("register")}>
                    <FaUserPlus/>
                    <br/>
                    Register
                </button>
            </div>
        </div>
    );
};

export default HomePage;
