<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import useQuestions from '@/composables/useQuestions';

const { questions, error, fetchAllQuestions, getOneQuestion } = useQuestions();

const columns = [{
  key: 'title',
  label: 'Titulo'
}, {
  key: 'subtitle',
  label: 'Subtitulo'
}, {
  key: 'dificulty',
  label: 'Dificuldade'
}, {
  key: 'response',
  label: 'Resposta'
}, {
  key: 'xp_reward',
  label: 'XP Reward'
}, {
  key: 'language',
  label: 'Linguagem'
}, {
  key: 'actions'
}];

const page = ref(1);
const pageCount = 10;

const rows = computed(() => {
  return questions.value ? questions.value.slice((page.value - 1) * pageCount, page.value * pageCount) : [];
});

const totalQuestions = computed(() => {
  return questions.value ? questions.value.length : 0;
});

import { questionObj } from '../../api/statGlobal';
import { qType } from '~/api/statGlobal';
import { getLanguages } from '~/api/languageTips';

const handleEditClick = async (row) => {
  try {
    // Obter dados da pergunta
    const questionData = await getOneQuestion(row.id);
    
    // Atualizar o objeto questionObj com os dados da pergunta
    questionObj.value = questionData;
    
    // Alterar o valor da linguagem dentro do questionObj
    const selectLanguage = await getLanguages(undefined, questionObj.value.id_language);
    questionObj.value.id_language = selectLanguage.name
    
    // Definir qType como verdadeiro (ou qualquer outra lógica que você tenha para isso)
    qType.value = true;
    
    // Navegar para a página de edição
    navigateTo(`/admnovodesafio`);
  } catch (error) {
    console.error('Erro ao obter a pergunta:', error);
  }
};

import { deleteQuestion } from '~/api/questionTips';
const handleDeleteClick = async (row) => {
  try {
    // Lógica para excluir a pergunta
    await deleteQuestion(row.id);
    isLoading.value = true;

    // Lógica para atualizar a tabela
    await fetchAllQuestions();
  } catch (error) {
    console.error('Erro ao excluir a pergunta:', error);
  } finally {
    isLoading.value = false;
  }
};

const items = (row) => [
  [{
    label: 'Edit',
    icon: 'i-heroicons-pencil-square-20-solid',
    click: () => handleEditClick(row) // Usa a função assíncrona
    
  },], [{
    label: 'Delete',
    icon: 'i-heroicons-trash-20-solid',
    click: () => handleDeleteClick(row)
  }]
];

const selected = ref([]);
const isLoading = ref(true);

onMounted(async () => {
  await fetchAllQuestions();
  isLoading.value = false;
});
</script>

<template>
  <div>
    <UTable :loading="isLoading"  :rows="rows" :columns="columns">
      <template #title-data="{ row }">
        <span :class="[selected.find(question => question.id === row.id) && 'text-primary-500 dark:text-primary-400']">{{ row.title }}</span>
      </template>
      <template #subtitle-data="{ row }">
        {{ row.subtitle }}
      </template>
      <template #dificulty-data="{ row }">
        {{ row.dificulty }}
      </template>
      <template #response-data="{ row }">
        {{ row.response }}
      </template>
      <template #xp_reward-data="{ row }">
        {{ row.xp_reward }}
      </template>
      <template #language-data="{ row }">
        {{  row.id_language }}
      </template>
      <template #actions-data="{ row }">
        <UDropdown :items="items(row)">
          <UButton color="gray" variant="ghost" icon="i-heroicons-ellipsis-horizontal-20-solid" />
        </UDropdown>
      </template>
    </UTable>
    <div class="flex w-full justify-end px-3 py-3.5 border-t border-gray-200 dark:border-gray-700">
      <UPagination v-model="page" :page-count="pageCount" :total="totalQuestions" />
    </div>
  </div>
</template>

<style scoped>
div {
    width: 100%;
    align-items: end;
    justify-content: end;
}

table {
    width: 100%;
}
</style>
