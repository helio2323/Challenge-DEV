<script setup lang="ts">
const route = useRoute()

const links = [{
  icon: 'i-heroicons-sun',
}, {
  icon: 'i-heroicons-bell',
  
}, {
    label: "Profile",
    avatar: {
        src: "https://avatars.githubusercontent.com/u/739984?v=4",
        size: 'sm',
    }
}]
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

