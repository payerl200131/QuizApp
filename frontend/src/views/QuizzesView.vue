<script setup>
import { ref, onMounted } from 'vue';
import { getQuizzes, deleteQuiz } from '../api/quiz';

const quizzes = ref([]);

onMounted(async () => {
  try {
    quizzes.value = await getQuizzes();
  } catch (error) {
    console.error("Failed to fetch quizzes:", error);
  }
});

const playQuiz = (quizId) => {
  console.log("playQuiz", quizId);
  window.location.href = `/play/${quizId}`;
}

const createQuiz = () => {
  window.location.href = '/create';
}

const updateQuiz = (quizId) => {
  window.location.href = `/update/${quizId}`;
}

const deleteQuizHandler = (quizId) => {
  deleteQuiz(quizId);
  window.location.reload();
}
</script>

<template v-if="quizzes">
  <div class="d-flex justify-content-between align-items-center mt-4 ml-4 mr-4 mb-0">
    <h3>Quizzes</h3>
    <button @click="createQuiz()" class="btn btn-success">Create Quiz</button>
  </div>
  <div class="table-responsive p-4">
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Name</th>
          <th scope="col">User</th>
          <th scope="col">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="quiz in quizzes" :key="quiz.quiz_id">
          <td>{{ quiz.name }}</td>
          <td>{{ quiz.user_id }}</td>
            <td>
              <button @click="playQuiz(quiz.quiz_id)" class="btn btn-success mx-1">Play</button>
              <button @click="updateQuiz(quiz.quiz_id)" class="btn btn-info mx-1">Update</button>
              <button @click="deleteQuizHandler(quiz.quiz_id)" class="btn btn-danger mx-1">Delete</button>
            </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
