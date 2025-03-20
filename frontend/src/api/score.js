import axios from "axios";
import request from './req';

export const getScoresByQuiz = async () => request('GET', '/scores').then(response => response.data);

export const createScore = async (score) => request('POST', '/scores', score).then(response => response.data);

export const updateScore = async (id, score) => request('PUT', `/scores/${id}`, score).then(response => response.data);

export const deleteScore = async (id) => request('DELETE', `/scores/${id}`).then(response => response.data);
