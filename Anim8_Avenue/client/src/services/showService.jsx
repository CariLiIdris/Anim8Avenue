/* eslint-disable no-useless-catch */
import axios from "axios";

const SHOW_INSTANCE = axios.create({
  baseURL: "http://localhost:8000/api/shows"
});

export const createShow = async (showData) => {
  try {
    const response = await SHOW_INSTANCE.post("/", showData);
    return response.data;
  } catch (error) {
    console.log(error);
    throw error;
  }
};

export const getAllShows = async () => {
  try {
    const response = await SHOW_INSTANCE.get("/");
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const getShowById = async (id) => {
  try {
    const response = await SHOW_INSTANCE.get(`/${id}`);
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const updateShowById = async (id, showData) => {
  try {
    const response = await SHOW_INSTANCE.put(`/${id}`, showData);
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const deleteShowById = async (id) => {
  try {
    const response = await SHOW_INSTANCE.delete(`/${id}`);
    return response.data;
  } catch (error) {
    throw error;
  }
};