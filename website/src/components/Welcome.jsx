import React, { useState, useEffect } from "react";
import styled from "styled-components";
import Robot from "../assets/robot.gif";
export default function Welcome() {
  const [userName, setUserName] = useState("");
  const [error, setError] = useState(null);
  
  useEffect(() => {
    const fetchUserName = async () => {
      try {
        const user = JSON.parse(localStorage.getItem(process.env.REACT_APP_LOCALHOST_KEY));
        if (user && user.username) {
          setUserName(user.username);
        } else {
          throw new Error("Username not found");
        }
      } catch (err) {
        setError(err.message);
      }
    };

    fetchUserName();
  }, []);

  if (error) {
    return (
      <Container>
        <img src={Robot} alt="Robot" />
        <h1>Error: {error}</h1>
        <h3>Please try again later.</h3>
      </Container>
    );
  }

  return (
    <Container>
      <img src={Robot} alt="" />
      <h1>
        Welcome, <span>{userName}!</span>
      </h1>
      <h3>Please select a chat to Start messaging.</h3>
    </Container>
  );
}

const Container = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  flex-direction: column;
  img {
    height: 20rem;
  }
  span {
    color: #4e0eff;
  }
`;
