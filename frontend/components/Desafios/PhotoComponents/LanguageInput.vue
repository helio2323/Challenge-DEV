<template>
  <UInputMenu v-model="selected" :options="people"  >
    <template #leading>
      <UIcon v-if="selected.icon" :name="(selected.icon as string)" class="w-5 h-5" />
      <UAvatar v-else-if="selected.avatar" v-bind="(selected.avatar as Avatar)" size="2xs" />
    </template>
  </UInputMenu>
</template>

<script setup lang="ts">
import type { Avatar } from '#ui/types'

const people = [{
  id: 'python',
  label: 'Python',
  href: 'https://github.com/benjamincanac',
  target: '_blank',
  avatar: { src: 'https://img.icons8.com/fluency/48/python.png' }
}, {
  id: 'python',
  label: 'Python',
  href: 'https://github.com/Atinux',
  target: '_blank',
  avatar: { src: 'https://img.icons8.com/fluency/48/javascript.png' }
},]

const selected = ref(people[0])
</script>

