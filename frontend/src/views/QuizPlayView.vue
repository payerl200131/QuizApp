<script setup>
import { ref, onMounted } from 'vue';
import { getQuiz } from '../api/quiz';
import { getQuestionsByQuiz } from '../api/question';

const quiz = ref(null);
const questions = ref([]);
const answers = ref({});

onMounted(async () => {
  try {
    const url = window.location.href;
    const parts = url.split('/');
    const id = parts[parts.length - 1];
    quiz.value = await getQuiz(id);

    questions.value = await getQuestionsByQuiz(id);
  } catch (error) {
    console.error("Failed to fetch quiz:", error);
  }
});

const checkAnswer = (questionId, answer) => {
  const question = questions.value.find(q => q.question_id === questionId);
  if (question && question.answer === answer) {
    answers.value[questionId] = true;
  }
};

</script>

<template>
  <div v-if="quiz" class="p-4">
    <div class="text-center border rounded">
      <h3>{{ quiz.name }}</h3>
      <h6>Creator: {{ quiz.user_id }}</h6>
    </div>
    <div v-for="question in questions" :key="question.question_id" class="mt-4">
      <h5>{{ question.question }}</h5>
      <div>
        <input 
          type="input" 
          :name="question.question_id" 
          :disabled="answers[question.question_id]" 
          @input="checkAnswer(question.question_id, $event.target.value)" 
        />
      </div>
    </div>
  </div>
</template>
