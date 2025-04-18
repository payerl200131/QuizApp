import request from './req';

export const getScoresByQuiz = async (quiz_id) => request('GET', `/scores/${quiz_id}`).then(response => response.data);
export const getScoresByUser = async (quiz_id) => request('GET', `/scores/${quiz_id}/own`).then(response => response.data);

export const createScore = async (score) => request('POST', '/scores', score).then(response => response.data);

export const updateScore = async (score) => request('PUT', `/scores`, score).then(response => response.data);

export const deleteScore = async (id) => request('DELETE', `/scores/${id}`).then(response => response.data);
