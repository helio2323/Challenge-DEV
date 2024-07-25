<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getUserInfos } from '@/api/userTips'

const userName = ref('') // Criar uma variável reativa para userName

onMounted(async () => {
  
  const userInfos = await getUserInfos(1)
  userName.value = userInfos.name // Atualizar o valor da variável reativa

  console.log(userName.value)
})

const route = useRoute()
const links = computed(() => [{ // Usar computed para reagir às mudanças
  icon: 'i-heroicons-sun',
}, {
  icon: 'i-heroicons-bell',
}, {
  label: userName.value, // Usar o valor da variável reativa
  avatar: {
    src: "https://avatars.githubusercontent.com/u/739984?v=4",
    size: 'sm',
  }
}])
</script>

<template>
    <div>
      <UHorizontalNavigation :links="links" class=""
      :ui="{
        size: 'text-xl',
      }" />
      
    </div>
</template>

<style  scoped>

div {
    display: flex;
    height: 100%;
    align-items: center;
    justify-content: center;
}

@media screen and (max-width: 1150px) {
    div {
        display: none;
    }
}


</style>

