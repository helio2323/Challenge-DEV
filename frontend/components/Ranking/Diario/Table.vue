<template>
  <div>
    <UTable :rows="formattedRows" />
    <div class="flex w-full justify-end px-3 py-3.5 border-t border-gray-200 dark:border-gray-700">
      <UPagination v-model="page" :page="page" :page-count="pageCount" :total="props.data?.length || 0" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, defineProps, ref } from 'vue';

const props = defineProps<{
  data: Array<{ id: number; usuario: string; pontos: number; respostas: number }> | undefined;
}>();

const page = ref(1);
const pageCount = 8;

const rows = computed(() => {
  if (props.data) {
    return props.data.slice((page.value - 1) * pageCount, page.value * pageCount);
  }
  return [];
});

const formattedRows = computed(() => {
  return rows.value.map(row => ({
    usuario: row.usuario,
    pontos: row.pontos,
    respostas: row.respostas,
  }));
  
});
</script>

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
