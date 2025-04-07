<script setup>
import { ref } from 'vue';
import { createQuiz } from '../api/quiz';

const quiz_name = ref('');
const saved = ref(null);
const quiz = ref(null);

const createQuizHandler = async (event) => {
  event.preventDefault();
  try {
    await createQuiz({ name: quiz_name.value });
    console.log(quiz);
    saved.value = true;
    quiz_name.value = '';
  } catch (error) {
    console.error('Failed to create quiz:', error);
  }
};
</script>

<template>
  <div class="p-4">
    <h3 class="text-center">Add Quiz</h3>
    <div v-if="saved" class="alert alert-success mt-4" role="alert">
      Quiz created successfully!
    </div>
    <form class="m-3" @submit="createQuizHandler">
      <div class="mt-3">
        <label class="form-label" for="name">Name</label>
        <input v-model="quiz_name" class="form-control" type="text" id="name" name="name" required>
      </div>
      <div class="mt-3">
        <button type="submit" class="btn btn-primary mt-3">Submit</button>
      </div>
    </form>
  </div>
</template>
