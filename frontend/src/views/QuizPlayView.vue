<script setup>
import { ref, onMounted, computed } from 'vue';
import { getQuiz } from '../api/quiz';
import { getQuestionsByQuiz } from '../api/question';
import { getScoresByQuiz } from '../api/score';

const quiz = ref(null);
const questions = ref([]);
const answers = ref({});
const scores = ref([]);

onMounted(async () => {
  try {
    const url = window.location.href;
    const parts = url.split('/');
    const id = parts[parts.length - 1];
    quiz.value = await getQuiz(id);

    questions.value = await getQuestionsByQuiz(id);
    scores.value = await getScoresByQuiz(id);
    console.log(score.value);

  } catch (error) {
    console.error("Failed to fetch quiz:", error);
  }
});

const checkAnswer = (questionId, answer) => {
  const question = questions.value.find(q => q.question_id === questionId);
  if (question && question.answer.replace(/\s+/g, '').toLowerCase() === answer.replace(/\s+/g, '').toLowerCase()) {
    answers.value[questionId] = true;
  }
};

const allAnswered = computed(() => {
  return questions.value.length > 0 && questions.value.every(q => answers.value[q.question_id]);
});

</script>

<template>
  <div v-if="quiz" class="p-4">
    <div class="text-center border rounded p-2">
      <h3>{{ quiz.name }}</h3>
      <h5>Creator: {{ quiz.user_id }}</h5>
      <h6>Scores:</h6>
      <div v-for="score in scores" :key="score.user_id">
        <p>{{ score.user_id }}: {{ score.score }}</p>
      </div>
    </div>
    <div v-if="allAnswered" class="alert alert-success mt-4" role="alert">
      You have answered all the questions!
      Restart? <a :href="'/play/' + quiz.quiz_id">Click here</a>
    </div>
    <div v-for="question in questions" :key="question.question_id" class="mt-4">
    <label :for="question.question_id" class="h5">{{ question.question }}</label>
    <div>
      <input
        type="text"
        :id="question.question_id"
        :disabled="answers[question.question_id]"
        @input="event => checkAnswer(question.question_id, event.target.value)"
        class="rounded border border-secondary"
        autocomplete="off"
      />
    </div>
    </div>
  </div>
</template>
