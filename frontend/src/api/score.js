import axios from "axios";

export const getScoresByQuiz = async () => {
    try {
        const response = await axios.get("http://localhost:5001/api/scores");
        return response.data;
    } catch (error) {
        console.error("Error fetching scores:", error);
        throw error;
    }
} 

export const createScore = async () => {
    try {
        const response = await axios.post("http://localhost:5001/api/scores");
        return response.data;
    } catch (error) {
        console.error("Error creating score:", error);
        throw error;
    }
}

export const updateScore = async () => {
    try {
        const response = await axios.put("http://localhost:5001/api/scores");
        return response.data;
    } catch (error) {
        console.error("Error updating score:", error);
        throw error;
    }
}

export const deleteScore = async () => {
    try {
        const response = await axios.delete("http://localhost:5001/api/scores");
        return response.data;
    } catch (error) {
        console.error("Error deleting score:", error);
        throw error;
    }
}
