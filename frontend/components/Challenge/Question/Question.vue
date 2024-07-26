<template>
    <div class="question">
        <h2>{{ challengeStar.title }}</h2>

        <p>{{ challengeStar.pergunta }}</p>

        <h3>Exemplo:</h3>

        <p>{{ challengeStar.exemplo }}</p>

        
    </div>
</template>

<script setup>

import { challengeStar } from '~/api/statGlobal';

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