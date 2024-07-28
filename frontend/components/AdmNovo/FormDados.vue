<script setup lang="ts">
import { ref, reactive, onMounted, watch } from 'vue';
import type { FormError, FormSubmitEvent } from '#ui/types';
import { createQuestion, updateQuestion } from "../../api/questionTips";
import { getLanguages } from "../../api/languageTips";
import { questionObj } from "../../api/statGlobal";

const people = ['quizz', 'code'];
const linguagem = ['Python', 'Javascript', 'Java', 'Rust'];
const dificuldade = ['Easy', 'Medium', 'True Challenge'];

const state = reactive({
  title: '',
  subtitle: '',
  tipodesafio: '',
  exemplo: '',
  pergunta: '',
  xpreward: '',
  resposta: '',
  linguagem: '',
  dificuldade: ''
});

// Inicializa o estado com base em `questionObj` quando o componente é montado
onMounted(() => {
  if (questionObj && Object.keys(questionObj).length) {
    state.title = questionObj.value?.title || '';
    state.subtitle = questionObj.value?.subtitle || '';
    state.tipodesafio = questionObj.value?.type_question || '';
    state.exemplo = questionObj.value?.example || '';
    state.pergunta = questionObj.value?.question || '';
    state.xpreward = parseInt(questionObj.value?.xp_reward || '0', 10); // Converta para número inteiro
    state.resposta = questionObj.value?.response || '';
    state.linguagem = questionObj.value?.id_language || '';
    state.dificuldade = questionObj.value?.dificulty || '';
  }
});

watch(() => questionObj.value, (newObj) => {
  if (newObj && Object.keys(newObj).length) {
    state.title = newObj.title || '';
    state.subtitle = newObj.subtitle || '';
    state.tipodesafio = newObj.type_question || '';
    state.exemplo = newObj.example || '';
    state.pergunta = newObj.question || '';
    state.xpreward = parseInt(newObj.xp_reward || '0', 10); // Converta para número inteiro
    state.resposta = newObj.response || '';
    state.linguagem = newObj.id_language || '';
    state.dificuldade = newObj.dificulty || '';
  }
}, { deep: true });
async function onSubmit(event: FormSubmitEvent<any>) {
  const selectLanguage = await getLanguages(state.linguagem, undefined);
  
  try {
    const response = await updateQuestion(
      questionObj.value?.id,
      state.title,
      state.subtitle,
      state.exemplo,
      state.tipodesafio,
      state.pergunta,
      selectLanguage.id,
      state.xpreward,
      state.resposta,
      "",
      state.dificuldade
    );
    console.log(response);
    navigateTo('/admlist');
  } catch (error) {
    console.log('Erro ao registrar:', error);
  }
}

const validate = (state: any): FormError[] => {
  const errors = []
  
  if (!state.title) errors.push({ path: 'title', message: 'Required' })
  if (!state.subtitle) errors.push({ path: 'subtitle', message: 'Required' })
  if (!state.tipodesafio) errors.push({ path: 'tipodesafio', message: 'Required' })
  if (!state.exemplo) errors.push({ path: 'exemplo', message: 'Required' })
  if (!state.pergunta) errors.push({ path: 'pergunta', message: 'Required' })
  if (!state.linguagem) errors.push({ path: 'linguagem', message: 'Required' })
  if (!state.dificuldade) errors.push({ path: 'dificuldade', message: 'Required' })
  if (!state.resposta) errors.push({ path: 'resposta', message: 'Required' })
  if (!state.xpreward) errors.push({ path: 'xpreward', message: 'Required' })
  return errors
}
</script>

<template>
  <UForm :validate="validate" :state="state" class="space-y-4 max-w-3xl form-group" @submit="onSubmit">
    <section class="flex flex-row gap-5 w-full">
      <UFormGroup class="flex-col w-full max-w-96 form-group" label="Titulo" name="title">
        <UInput class="w-full" v-model="state.title" />
      </UFormGroup>
      <UFormGroup class="w-full max-w-96 form-group" label="Subtitle" name="subtitle">
        <UInput v-model="state.subtitle" />
      </UFormGroup>
    </section>

    <section class="flex flex-row gap-5 w-full">
      <UFormGroup class="w-full max-w-96 form-group" label="Tipo Desafio" name="people">
        <UInputMenu v-model="state.tipodesafio" :options="people" />
      </UFormGroup>
      <UFormGroup class="w-full max-w-96 h-fit form-group" label="Exemplo" name="exemplo">
        <UTextarea autoresize v-model="state.exemplo" />
      </UFormGroup>
    </section>

    <section>
      <UFormGroup class="w-full max-w-96 h-fit form-group" label="Pergunta" name="pergunta">
        <UTextarea autoresize v-model="state.pergunta" />
      </UFormGroup>
    </section>

    <section class="flex flex-row gap-5 w-full form-group">
      <UFormGroup class="w-full max-w-96" label="Linguagem" name="linguagem">
        <UInputMenu v-model="state.linguagem" :options="linguagem" />
      </UFormGroup>
      <UFormGroup class="w-full max-w-96 form-group" label="XP Reward" name="xpreward">
        <UInput v-model="state.xpreward" />
      </UFormGroup>
    </section>

    <section class="flex flex-row gap-5 w-full form-group">
      <UFormGroup class="w-full max-w-96" label="Dificuldade" name="dificuldade">
        <UInputMenu v-model="state.dificuldade" :options="dificuldade" />
      </UFormGroup>
    </section>

    <h3>Resposta</h3>
    <section class="flex flex-row gap-5 w-full">
      <UFormGroup class="w-full max-w-96 form-group" label="Resposta" name="resposta">
        <UInput v-model="state.resposta" />
      </UFormGroup>
    </section>

    <section class="flex flex-row gap-5 w-full justify-end">
      <UButton class="w-48 h-8 justify-center rounded-xl" color="yellow" type="submit">
        Atualizar Desafio
      </UButton>
    </section>
  </UForm>
</template>

<style scoped>
.input {
  width: 100%;
}

h3 {
  font-size: 1.2rem;
  font-weight: 600;
  width: 100%;
  color: var(--Primary);
}

@media screen and (max-width: 1150px) {
  section {
    width: 100%;
    flex-direction: column;
    align-items: start;
    justify-content: start;
    margin: 0;
  }

  .form-group {
    width: 100%;
    max-width: 100%;
  }
}
</style>
