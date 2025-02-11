/* eslint-disable no-useless-catch */
// Nehimya
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

// Zacarias
export const updateUserById = async (_id, userData) => {
  try {
    const res = await USER_INSTANCE.put(`/user/${_id}`, userData);
    console.log('```userServices```Res: ', res)
    return res.data
  } catch (error) {
    console.log(error);
    throw error;
  }
};

// Nehimya
export const deleteUserById = async (id) => {
  try {
    const res = await USER_INSTANCE.delete(`/user/${id}`);
    return res.data;
  } catch (error) {
    console.log(error);
    throw error;
  }
};
// Zacarias
export const logout = async () => {
  try {
    const res = await USER_INSTANCE.post('/user/logout', {}, { withCredentials: true })
    return res.data
  }
  catch (err) { throw err }
}

export const login = async activeUserData => {
  try {
    const res = await USER_INSTANCE.post('/user/login', activeUserData, { withCredentials: true })
    console.log(res.data)
    return res.data
  }
  catch (err) { throw err }
}