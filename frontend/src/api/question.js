import request from './req';

export const getQuestionsByQuiz = async (quiz_id) => request('GET', `/questions/${quiz_id}`).then(response => response.data);

export const deleteQuestion = async (id) => request('DELETE', `/questions/${id}`).then(response => response.data);

export const updateQuestion = async (id, question) => request('PUT', `/questions/${id}`, question).then(response => response.data);

export const createQuestion = async (question) => request('POST', '/questions', question).then(response => response.data);
