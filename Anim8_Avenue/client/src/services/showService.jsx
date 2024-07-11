/* eslint-disable no-useless-catch */
import axios from "axios";

const SHOW_INSTANCE = axios.create({
  baseURL: "http://localhost:8000/api",
  withCredentials: true
});

export const createShow = async (showData) => {
  try {
    const formData = new FormData();
    for (const key in showData) {
      formData.append(key, showData[key]);
    }
    const response = await SHOW_INSTANCE.post("/shows", formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    return response.data;
  } catch (error) {
    console.log(error);
    throw error;
  }
};

export const getAllShows = async () => {
  try {
    const response = await SHOW_INSTANCE.get("/shows");
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const getShowById = async (id) => {
  try {
    const response = await SHOW_INSTANCE.get(`/shows/${id}`);
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const updateShowById = async (id, showData) => {
  try {
    const formData = new FormData();
    for (const key in showData) {
      formData.append(key, showData[key]);
    }
    const response = await SHOW_INSTANCE.put(`/show/${id}`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  } catch (error) {
    throw error;
  }
};
export const deleteShowById = async (id) => {
  try {
    const response = await SHOW_INSTANCE.delete(`/show/${id}`);
    return response.data;
  } catch (error) {
    throw error;
  }
};