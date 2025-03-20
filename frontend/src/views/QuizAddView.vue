<script setup>
import { ref, onMounted } from 'vue';
import { createQuiz } from '../api/quiz';
// import { useProfile } from '../store/me';

const quiz = ref({
  user_id: '',
  name: ''
});


// TODO: don't use the user here just use the user in the backend function 

// const fetchCurrentUser = async () => {
//   try {
//     const response = await useProfile();
//     quiz.value.user_id = response.data.username;
//   } catch (error) {
//     console.error('Failed to fetch current user:', error);
//   }
// };

// onMounted(() => {
//   const creator = fetchCurrentUser();
//   console.log(creator);
// });

const createQuizHandler = async (event) => {
  event.preventDefault();
  try {
    await createQuiz(quiz.value);
    alert('Quiz created successfully!');
    quiz.value.name = '';
  } catch (error) {
    console.error('Failed to create quiz:', error);
    alert('Failed to create quiz.');
  }
};
</script>

<template>
  <div class="p-4">
    <h3 class="text-center">Add Quiz</h3>
    <form class="m-3" @submit="createQuizHandler">
      <div class="mt-3">
        <label class="form-label" for="user_id">User</label>
        <input v-model="quiz.user_id" class="form-control" type="text" id="user_id" name="user_id" disabled>
      </div>
      <div class="mt-3">
        <label class="form-label" for="name">Name</label>
        <input v-model="quiz.name" class="form-control" type="text" id="name" name="name" required>
      </div>
      <div class="mt-3">
        <button type="submit" class="btn btn-primary mt-3">Submit</button>
      </div>
    </form>
  </div>
</template>
