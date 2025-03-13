import axios from "axios";

export const getQuestionsByQuiz = async (quiz_id) => {
    try {
        const response = await axios.get(`http://localhost:5001/api/question?quiz_id=${quiz_id}`);
        return response.data;
    } catch (error) {
        console.error("Error fetching questions:", error);
        throw error;
    }
}

export const deleteQuestion = async (id) => {
    try {
        const response = await axios.delete("http://localhost:5001/api/question/" + id);
        return response.data;
    } catch (error) {
        console.error("Error deleting question:", error);
        throw error;
    }
}

export const updateQuestion = async (id, question) => {
    try {
        const response = await axios.put("http://localhost:5001/api/question/" + id, question);
        return response.data;
    } catch (error) {
        console.error("Error updating question:", error);
        throw error;
    }
}

export const createQuestion = async (question) => {
    try {
        const response = await axios.post("http://localhost:5001/api/question", question);
        return response.data;
    } catch (error) {
        console.error("Error creating question:", error);
        throw error;
    }
}
