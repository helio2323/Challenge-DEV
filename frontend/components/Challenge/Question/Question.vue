<template>
    <div class="question">
        <h2>{{ challengeStar.title }}</h2>

        <!-- Use v-html para renderizar HTML -->
        <p v-html="formattedQuestion"></p>

        <h3>Exemplo:</h3>

        <p>{{ challengeStar.exemplo }}</p>
    </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import { challengeStar } from '~/api/statGlobal';

const formattedQuestion = ref('');

// Watch for changes in challengeStar.pergunta and update formattedQuestion
watch(() => challengeStar.value.pergunta, (newValue) => {
    if (newValue) {
        formattedQuestion.value = newValue.replace(/\n/g, '<br>');
    } else {
        formattedQuestion.value = '';
    }
}, { immediate: true });

console.log("challengeStar:", challengeStar);
</script>

<style scoped>
.question {
    display: flex;
    flex-direction: column;
    gap: 20px;
    width: 100%;
}

.question h2 {
    font-size: 28px;
    font-weight: bold;
}

.question h3 {
    font-size: 18px;
    font-weight: bold;
}
</style>
