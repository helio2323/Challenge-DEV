<template>
  <div class="app">
    <NuxtLayout>
      <NuxtRouteAnnouncer />
      <NuxtPage />
    </NuxtLayout>
    <UNotifications />
  </div>
</template>

<script setup>

const userLoginVerify = () => {
        if (localStorage.getItem('token')) {
          return true
        } else {
          navigateTo('/login')
          return false
        }
      }

onMounted(() => {
    userLoginVerify()
})


</script>
<style scoped>

</style>

