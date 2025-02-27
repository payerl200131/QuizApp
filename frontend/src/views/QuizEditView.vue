<script setup>
import { ref, onMounted } from 'vue';
import { createQuiz } from '../api/quiz';

const quiz = ref(null);

</script>

<template>
<div class="p-4">
    <h3 class="text-center">Add Quiz</h3>
    <form class="m-3">
        <div class="mt-3">
            <label class="form-label" for="user_id">User</label>
            <input class="form-control" type="text" id="user_id" name="user_id" required disabled>
        </div>
        <div class="mt-3">
            <label class="form-label" for="name">Name</label>
            <input class="form-control" type="text" id="name" name="name" required>
        </div>
        <div class="mt-3">
            <button type="submit" class="btn btn-primary mt-3">Submit</button>
        </div>
    </form>
</div>
</template>