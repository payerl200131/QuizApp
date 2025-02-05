import axios from "axios";

export const getQuizzes = async () => {
  try {
    const response = await axios.get("http://localhost:5001/api/quizzes");
    return response.data;
  } catch (error) {
    console.error("Error fetching quizzes:", error);
    throw error;
  }
};
