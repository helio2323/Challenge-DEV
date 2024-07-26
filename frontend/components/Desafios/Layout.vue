<template>
    <main class="main-desafios">
    <DesafiosPhotoSection />
    <section class="challeng-sec">
        <DesafiosChallengSec />
    </section>
    </main>
</template>

<script setup>


</script>

<style scoped>

.main-desafios{
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: center;
    width: 100%;
    height: 100%;
    background-color: var(--BackCover);
}

.challeng-sec{
    display: flex;
    flex-direction: row;
    width: 100%;
    height: 100%;
    padding: 20px;
}

@media screen and (max-width: 950px) {
   .challeng-sec{
        padding: 10px;
   } 
}

</style>