/* eslint-disable no-useless-catch */
import axios from 'axios';

const USER_INSTANCE = axios.create({
  baseURL: 'http://localhost:8000/api'
});

export const createUser = async (userData) => {
  try {
    const res = await USER_INSTANCE.post('/users', userData);
    return res.data;
  } catch (error) {
    console.log(error);
    throw error;
  }
};

export const getAllUsers = async () => {
  try {
    const res = await USER_INSTANCE.get('/users');
    return res.data;
  } catch (error) {
    console.log(error);
    throw error;
  }
};

export const getUserById = async (id) => {
  try {
    const res = await USER_INSTANCE.get(`/users/${id}`);
    return res.data;
  } catch (error) {
    console.log(error);
    throw error;
  }
};

export const updateUserById = async (id, userData) => {
  try {
    const res = await USER_INSTANCE.put(`/user/${id}`, userData);
    return res.data;
  } catch (error) {
    console.log(error);
    throw error;
  }
};

export const deleteUserById = async (id) => {
  try {
    const res = await USER_INSTANCE.delete(`/user/${id}`);
    return res.data;
  } catch (error) {
    console.log(error);
    throw error;
  }
};

export const logout = async activeUserData => {
  try {
    const res = await USER_INSTANCE.post('/user/logout', activeUserData)
    return res.data
  }
  catch (err) { throw err }
}

export const login = async activeUserData => {
  try {
    const res = await USER_INSTANCE.post('/user/login', activeUserData)
    // console.log(res.data)
    return res.data
  }
  catch (err) { throw err }
}