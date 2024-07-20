<template>
        <section class="challeng-infos">
            <h3 class="tittle">Descrição do curso</h3>
            <p class="text-lg">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also </p>
            <h3 class="tittle">Detalhes do curso</h3>

            <div class="flex items-center gap-1">
            <UIcon name="i-heroicons-user" class="w-5 h-5" />
                <p>15 Participantes</p>
            </div>

            <div class="flex items-center gap-1">
            <UIcon name="i-heroicons-star" class="w-5 h-5" />
                <p>10 Completaram todos desafios</p>
            </div>

            <div class="flex items-center gap-1">
            <UIcon name="i-heroicons-clock" class="w-5 h-5" />
                <p>Ultima atualização em  13/07/2024</p>
            </div>
        </section>
</template>

<script setup>

</script>

<style scoped>

.challeng-infos{
    display: flex;
    flex-direction: column;
    align-items: start;
    justify-content: start;
    height: 100%;
    width: 100%;
    gap: 20px;
}

.tittle{
    font-size: 28px;
    font-weight: 500;
}



</style>