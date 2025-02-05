<script setup>
import { ref, onMounted } from 'vue';
import { getQuizzes } from '../api/quiz';

const quizzes = ref([]);

onMounted(async () => {
  try {
    quizzes.value = await getQuizzes();
  } catch (error) {
    console.error("Failed to fetch quizzes:", error);
  }
});
</script>

<template>
    <div class="d-flex m-4" v-for="quiz in quizzes" :key="quiz.quiz_id">
      <div class="bg-secondary p-4 rounded">
        <h5 class="text-white">{{ quiz.name }}</h5>
        <h6 class="text-white">{{ quiz.user_id }}</h6>
        <button class="btn btn-primary">Open</button>
      </div>
    </div>
</template>
