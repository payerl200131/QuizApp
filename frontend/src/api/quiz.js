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

export const getQuiz = async (id) => {
  try {
    const response = await axios.get("http://localhost:5001/api/quizzes/" + id);
    return response.data;
  } catch (error) {
    console.error("Error fetching quiz:", error);
    throw error;
  }
}

export const deleteQuiz = async (id) => {
  try {
    const response = await axios.delete("http://localhost:5001/api/quizzes/" + id);
    return response.data;
  } catch (error) {
    console.error("Error deleting quiz:", error);
    throw error;
  }
}

export const updateQuiz = async (id, quiz) => {
  try {
    const response = await axios.put(`http://localhost:5001/api/quizzes/${id}`, {
      name: quiz.value.name
    }, {
      headers: {
        'Content-Type': 'application/json'
      }
    });
    return response.data;
  } catch (error) {
    console.error("Error updating quiz:", error);
    throw error;
  }
}

export const createQuiz = async (quiz) => {
  try {
    const response = await axios.post("http://localhost:5001/api/quizzes", quiz);
    return response.data;
  } catch (error) {
    console.error("Error creating quiz:", error);
    throw error;
  }
}
