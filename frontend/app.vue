<template>
  <div class="app">

    <LoadingLoad v-if="Loading"/>

    <NuxtLayout>
      <NuxtRouteAnnouncer />
      <NuxtPage />
    </NuxtLayout>
    <UNotifications />
  </div>
</template>

<script setup>

import {Loading} from '../frontend/api/statGlobal'


useSeoMeta
({
  title
: 'Challenge DEVs',
  ogTitle
: 'Challenge DEVs',
  description
: 'Venha aprimorar suas habilidades de desenvolvimento de software com o Challenge DEVs',
  ogDescription
: 'Venha aprimorar suas habilidades de desenvolvimento de software com o Challenge DEVs',
  ogImage
: 'https://img.icons8.com/fluency/48/laptop-coding.png',
  twitterCard
: 'https://img.icons8.com/fluency/48/laptop-coding.png',
})



</script>
<style >

.page-enter-active,
.page-leave-active {
  transition: all 0.4s;
}
.page-enter-from,
.page-leave-to {
  opacity: 0;
  filter: blur(1rem);
}

</style>

