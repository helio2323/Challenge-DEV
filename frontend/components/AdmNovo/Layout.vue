<template>
    <div class="layout-diario">
        <section class="main-section">
            <div class="main-header">
                <h1>Inclusão de Desafio  / Novo Desafio</h1>

                <h3>Dados do Desafio</h3>

                <AdmNovoFormDados v-if="qType" />
                <AdmNovoFormNovoDado v-if="!qType" />
            </div>
        </section>
    </div>


</template>

<script setup>

import { qType } from '~/api/statGlobal';

</script>

<style scoped>

.main-section {
display: flex;
flex-direction: column;
justify-content: start;
align-items: start;
width: 100%;
height: 100%;
background-color: var(--BackCover);
border-radius: 20px;
}

.layout-diario {
display: flex;
flex-direction: column;
justify-content: start;
align-items: start;
width: 100%;
height: 100%;
background-color: var(--BackCover);
border-radius: 20px;
padding:  20px;
}

.main-header {
display: flex;
flex-direction: column;
width: 100%;
padding-top: 10px;
padding-bottom: 10px;
gap: 10px;
}

.main-header h1 {
font-size: 1.5rem;
font-weight: 600;
width: 100%;
}

.main-header h3 {
font-size: 1.2rem;
font-weight: 600;
width: 100%;
color: var(--Primary);
}

.button-adm {
display: flex;
width: 100%;
justify-content: end;
align-items: end;
gap: 10px;
}

.button {
display: flex;
flex-direction: row;
width: 220px;
align-items: center;
justify-content: center;
gap: 20px;
}

@media screen and (max-width: 1150px) {
    .main-header h1 {
    font-size: 1.3rem;
    font-weight: 600;
    width: 100%;
}
}

</style>