<template>
        <section class="challeng-infos">
            <h3 class="tittle">Descrição do curso</h3>
            <p class="text-lg">Aprenda os fundamentos e técnicas avançadas de programação com o nosso curso abrangente. Desde os conceitos básicos até os tópicos mais avançados, este curso foi projetado para equipá-lo com habilidades práticas e teóricas em várias linguagens de programação. Aproveite uma abordagem prática com projetos desafiadores e avaliações interativas que garantem uma compreensão sólida e aplicável. Através de exemplos reais e exercícios práticos, você estará preparado para enfrentar desafios de programação do mundo real. </p>
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