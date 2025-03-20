<script setup>
import { ref, onMounted } from 'vue';
import { getQuiz, updateQuiz, createQuiz } from '../api/quiz';
import { getQuestionsByQuiz, deleteQuestion, createQuestion, updateQuestion } from '../api/question';
import { getScoresByQuiz } from '../api/score';

const quiz = ref(null);
const questions = ref([]);
const scores = ref([]);
const saved = ref(null);

const addQuestionHandler = () => {
  questions.value.push({ quiz_id: quiz.value.quiz_id, question: '', answer: '' });
}

const deleteQuestionHandler = (question) => {
  if (question.question_id === undefined) {
    questions.value = questions.value.filter(q => q !== question);
    return;
  } else {
    questions.value = questions.value.filter(q => q !== question);    
    deleteQuestion(question.question_id);
  }
}

const saveChanges = async () => {
  try {
    if (quiz.value.name === '' && !quiz.value.quiz_id) {
      await createQuiz(quiz.value);
    } else {
      await updateQuiz(quiz.value.quiz_id, quiz.value);
    }

    for (let question of questions.value) {
      if (question.question === '' || question.answer === '') {
        continue;
      }
      if (!question.question_id) {
        const createdQuestion = await createQuestion(question);
        question.question_id = createdQuestion.question_id;
      } else {
        await updateQuestion(question.question_id, question);
      }
    }
    saved.value = true;
  } catch (error) {
    console.error("Failed to save changes:", error);
  }
}

onMounted(async () => {
  try {
    const url = window.location.href;
    const parts = url.split('/');
    const id = parts[parts.length - 1];
    quiz.value = await getQuiz(id);

    questions.value = await getQuestionsByQuiz(id);
    // scores.value = await getScoresByQuiz(id);

  } catch (error) {
    console.error("Failed to fetch quiz:", error);
  }
});
</script>

<template>
  <div class="p-4">
    <h3 class="text-center">Quiz Edit</h3>
    <div v-if="saved" class="alert alert-success mt-4" role="alert">
      Changes saved.
      <a :href="'/play/' + quiz.quiz_id">Test the quiz!</a>
    </div>
    <h6>Quiz Information:</h6>
    <input v-if="quiz" class="form-control my-3" id="name" name="name" type="input" placeholder="Name" v-model="quiz.name" />
    <h6>All Questions:</h6>
    <div v-for="question in questions" :key="question.id" class="">
      <div class="mt-3">
        <div class="d-flex align-items-center mb-1 justify-content-between">
          <p class="mb-0">Question {{ questions.indexOf(question) + 1 }}:</p>
          <button @click="deleteQuestionHandler(question)" class="btn btn-danger btn-sm ms-auto">Delete</button>
        </div>
        <input class="form-control" id="answer" name="answer" type="input" placeholder="Question" autocomplete="off" v-model="question.question" />
        <input class="form-control" id="question" name="question" type="input" placeholder="Answer" autocomplete="off" v-model="question.answer" />
      </div>
    </div>
    <div class="d-flex justify-content-between">
      <button @click="saveChanges()" class="btn btn-primary mt-3 ml-1">Save Changes</button>
      <button @click="addQuestionHandler()" class="btn btn-success mt-3">Add Question</button>
    </div>
  </div>
</template>
