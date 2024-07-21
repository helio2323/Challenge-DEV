
<template>
  <UDropdown class="profile" :items="items" :ui="{ item: { disabled: 'cursor-text select-text' } }" :popper="{ placement: 'bottom-start' }">
    <UAvatar src="https://avatars.githubusercontent.com/u/739984?v=4" />

    <template #account="{ item }">
      <div class="text-left">
        <p>
          Signed in as
        </p>
        <p class="truncate font-medium text-gray-900 dark:text-white">
          {{ item.label }}
        </p>
      </div>
    </template>

    <template #item="{ item }">
      <span class="truncate">{{ item.label }}</span>

      <UIcon :name="item.icon" class="flex-shrink-0 h-4 w-4 text-gray-400 dark:text-gray-500 ms-auto" />
    </template>
  </UDropdown>
</template>

<script setup lang="ts">
const items = [
  [{
    label: 'ben@example.com',
    slot: 'account',
    disabled: true
  }], [{
    label: 'Meu Progresso',
    icon: 'i-heroicons-user',
    to: '/meuprogresso'
  }], [{
    label: 'Desafios',
    icon: 'i-heroicons-light-bulb',
    to: '/desafios'
  }, {
    label: 'Ranking',
    icon: 'i-heroicons-trophy',
    to: '/ranking'
  },], [{
    label: 'Administrador',
    icon: 'i-heroicons-lock-closed',
    to: '/admlist'

  }],[{
    label: 'Sair',
    icon: 'i-heroicons-arrow-left-on-rectangle'
  }]
]
</script>

<style scoped>
.profile{
    display: none;
}

@media screen and (max-width: 1150px) {
    .profile{
        display: flex;
    }
}
</style>

