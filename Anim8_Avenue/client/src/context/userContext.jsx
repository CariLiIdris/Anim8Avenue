/* eslint-disable no-unused-vars */
/* eslint-disable react/prop-types */
import React from "react";
import { createContext, useEffect, useState } from "react";
import { getUserById } from "../services/userService";

// Context declaration
export const userContext = createContext();

export const UserProvider = ({ children }) => {
  const [user, setUser] = useState({})
  // Collect stored logged in user id
  const id = window.localStorage.getItem('Logged in user id')

  // Get user by id stored in local storage
  useEffect(() => {
    if (id) {
      getUserById(id)
        .then((res) => {
          // console.log(res)
          setUser(res)
          document.cookie = `userToken=${id}; path=/;`
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }, [id])

  // Store id in local storage
  const storeIdInLocalStorage = (id) => {
    window.localStorage.setItem('Logged in user id', id)
  }

  return (
    <userContext.Provider value={{ user, setUser, storeIdInLocalStorage }}>
      {children}
    </userContext.Provider>
  )
}