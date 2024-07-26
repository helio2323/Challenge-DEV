<template>
  <UInputMenu v-model="selected" :options="people" @close="handleClick">
    <template #leading>
      <UIcon v-if="selected.icon" :name="(selected.icon as string)" class="w-5 h-5" />
      <UAvatar v-else-if="selected.avatar" v-bind="(selected.avatar as Avatar)" size="2xs" />
    </template>
  </UInputMenu>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import type { Avatar } from '#ui/types';
import { languageFilter } from '@/api/statGlobal';

// Dados para o menu
const people = [
  {
    id: 1,
    label: 'Python',
    href: 'https://github.com/benjamincanac',
    target: '_blank',
    avatar: { src: 'https://img.icons8.com/fluency/48/python.png' }
  },
  {
    id: 2,
    label: 'JavaScript',
    href: 'https://github.com/Atinux',
    target: '_blank',
    avatar: { src: 'https://img.icons8.com/fluency/48/javascript.png' }
  },
  {
    id: 3,
    label: 'Java',
    href: 'https://github.com/Atinux',
    target: '_blank',
    avatar: { src: 'https://img.icons8.com/color/48/java-coffee-cup-logo--v1.png' }
  },
  {
    id: 4,
    label: 'Rust',
    href: 'https://github.com/Atinux',
    target: '_blank',
    avatar: { src: 'https://img.icons8.com/external-tal-revivo-bold-tal-revivo/24/external-rust-is-a-multi-paradigm-system-programming-language-logo-bold-tal-revivo.png' }
  },
];

// Estado do item selecionado
const selected = ref(people[0]);

// Função chamada ao clicar no menu
const handleClick = () => {
  languageFilter.value = selected.value.id;
  console.log(languageFilter.value);
};
</script>
