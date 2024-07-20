<script setup lang="ts">
const people = [{
  id: 1,
  usuario: 'Lindsay Walton',
  desafios: '50',
  xp: '5500',  
}, {
  id: 2,
  usuario: 'Courtney Henry',
  desafios: '50',
  xp: '5500',
}, 
]

const page = ref(1)
const pageCount = 8

const rows = computed(() => {
  return people.slice((page.value - 1) * pageCount, (page.value) * pageCount)
})
</script>

<template>
  <div>
    <UTable :rows="rows" />
    <div class="flex w-full justify-end px-3 py-3.5 border-t border-gray-200 dark:border-gray-700">
      <UPagination v-model="page" :page-count="pageCount" :total="people.length" />
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

