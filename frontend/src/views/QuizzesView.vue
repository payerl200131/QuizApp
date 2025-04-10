<script setup>
import { ref, onMounted } from 'vue';
import { getQuizzes } from '../api/quiz';
import { useRouter } from 'vue-router';1

const quizzes = ref([]);
const router = useRouter();

onMounted(async () => {
  try {
    quizzes.value = await getQuizzes();
  } catch (error) {
    console.error("Failed to fetch quizzes:", error);
  }
});

const playQuiz = (quizId) => {
  router.push(`/play/${quizId}`);
}

const createQuiz = () => {
  router.push(`/create`);
}

const updateQuiz = (quizId) => {
  router.push(`/update/${quizId}`);
}
</script>

<template>
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
              <button @click="playQuiz(quiz.quiz_id)" class="btn btn-success mb-1 mr-1">Play</button>
              <button @click="updateQuiz(quiz.quiz_id)" class="btn btn-info mb-1 mr-1">Update</button>
            </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
