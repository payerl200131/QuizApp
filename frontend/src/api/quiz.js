import axios from 'axios';
import request from './req';

export const getQuizzes = async () => request('GET', '/quizzes').then(response => response.data);

export const getQuiz = async (id) => request('GET', `/quizzes/${id}`).then(response => response.data);

export const deleteQuiz = async (id) => request('DELETE', `/quizzes/${id}`).then(response => response.data);

export const updateQuiz = async (id, quiz) => request('PUT', `/quizzes/${id}`, quiz).then(response => response.data);

export const createQuiz = async (quiz_name) => {
    return request('POST', `/quizzes?quiz_name=${encodeURIComponent(quiz_name)}`).then(response => response.data);
};