
<template>
  <div class="menu">
    <UVerticalNavigation :links="links"
    :ui="{
        size: 'text-xl',
        padding: 'p-2',
    }"/>

<div class="gap-4 my-24">
    <DefaultDivider />

    <UVerticalNavigation :links="linklog"
    :ui="{
        size: 'text-xl',
        padding: 'p-2',
    }"/>
    
</div>
  </div>
</template>

<script setup lang="ts">
const route = useRoute()

const linklog = [
    [{
        label: "Sair",
        icon: 'i-heroicons-arrow-left-on-rectangle'
    }]
]


const links = [
  [{
    label: 'Meu Progresso',
    icon: 'i-heroicons-user',
    to: '/progresso',

  },
  {
    label: 'Desafios',
    icon: 'i-heroicons-light-bulb',
    to: '/progresso',
    
  },
  {
    label: 'Ranking',
    icon: 'i-heroicons-trophy',
    to: '/progresso',
    
  }, ]
]
</script>

<style scoped>

div {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.menu {
    height: 100%;
    display: flex;
    flex-direction: column;
    gap: 10px;
}

</style>

