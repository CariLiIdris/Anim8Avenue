import axios from "axios"

const USER_INSTANCE = axios.create({
    baseURL:"http://localhost:8000/user"
})
export const createUser = async userData=>{
    try{
        const res = await USER_INSTANCE.post("/",userData)
        return res.data
    } catch(error){ 
        console.log(error)
        throw error}
}

export const getUserById = async id =>{
    try{
        const res = await USER_INSTANCE.get(`/${id}`)
        return res.data
    } catch(error){throw error}
}
export const getAllUsers = async () =>{
    try{
        const res = await USER_INSTANCE.get("/")
        return res.data
    } catch(error){throw error}
}
export const deleteUserById = async id =>{
    try{
        const res = await USER_INSTANCE.delete(`/${id}`)
        return res.data
    } catch(error){throw error}
}
export const updateUserById = async userData =>{
    try{
        const res = await USER_INSTANCE.put(`/${userData._id}`,userData)
        return res.data
    } catch(error){throw error}
}