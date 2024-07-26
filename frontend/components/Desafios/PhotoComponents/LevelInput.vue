<template>
  <UInputMenu
    v-model="selected"
    :options="options"
    placeholder="Select a person"
    by="id"
    option-attribute="name"
    :search-attributes="['name', 'colors']"
    @close="handleClick"
  >
    <template #option="{ option: person }">
      <span v-for="color in person.colors" :key="color.id" class="h-2 w-2 rounded-full" :class="`bg-${color}-500 dark:bg-${color}-400`" />
      <span class="truncate">{{ person.name }}</span>
    </template>
  </UInputMenu>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import {dificultyFilter} from '@/api/statGlobal'

const handleClick = () => {
  dificultyFilter.value = selected.value.name;
  console.log(selected.value.name);
};

const options = [
  { id: 1, name: 'Easy', colors: ['green'] },
  { id: 2, name: 'Medium', colors: ['yellow'] },
  { id: 3, name: 'True Challenge', colors: ['red'] },

]
const selected = ref(options[1])
</script>

