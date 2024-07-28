
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

import { ref, onMounted, computed } from 'vue'
import { getUserInfos } from '@/api/userTips'
import { useRouter } from 'vue-router'

const userName = ref('') // Criar uma variável reativa para userName
const router = useRouter()

onMounted(async () => {
  const userId = parseInt(localStorage.getItem('userid') || '0')
  const userInfos = await getUserInfos(userId)
  userName.value = userInfos.name // Atualizar o valor da variável reativa
  console.log(userId)
})

const handleLogout = () => {
  localStorage.removeItem('token')
  localStorage.removeItem('email')
  localStorage.removeItem('userid')
  router.push('/login')
}

const items = computed(() => [
  [{
    label: userName.value,
    slot: 'account',
    disabled: true
  }], 
  [{
    label: 'Meu Progresso',
    icon: 'i-heroicons-user',
    to: '/meuprogresso'
  }], 
  [{
    label: 'Desafios',
    icon: 'i-heroicons-light-bulb',
    to: '/desafios'
  }, {
    label: 'Ranking',
    icon: 'i-heroicons-trophy',
    to: '/ranking'
  }], 
  [{
    label: 'Administrador',
    icon: 'i-heroicons-lock-closed',
    to: '/admlist'
  }], 
  [{
    label: 'Sair',
    icon: 'i-heroicons-arrow-left-on-rectangle',
    click: () => handleLogout()
  }]
])

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

