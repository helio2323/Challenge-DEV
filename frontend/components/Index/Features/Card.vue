<template>
    <div class="card">
        <div class="card-image">
            <img width="35" height="35" :src="imgLogo" alt="code--v1"/>
        </div>

        <h4>{{ title }}</h4>
        <p>{{ subtitle }}</p>

        <NuxtLink to="/login">{{ callToAction }}</NuxtLink>

    </div>
</template>

<script setup>


const props = defineProps ({
    title: {
        type: String,
        default: 'Gratís e Open Source'
    },
    subtitle: {
        type: String,
        default: 'Nossa plataforma é totalmente gratís, voce pode aprender vendo nosso código'
    },
    callToAction: {
        type: String,
        default: 'Começar Agra!'
    },
    imgLogo: {
        type: String,
        default: 'https://img.icons8.com/ios/50/FFFFFF/code--v1.png'
    }
})

</script>

<style scoped>

.card {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    width: 280px;
    height: 300px;
    border-radius: 10px;
    padding: 20px;
    margin-top: 30px;
    border: solid 1px rgba(0, 220, 130,0.5);
}

.card:hover{
    border: solid 1px var(--Primary);
    background: rgba(0, 220, 130, 0.5);
    box-shadow: 0 0 20px rgba(0, 220, 130, 0.5);
    transition: all 0.5s;
}

.card-image {
    min-width: 60px;
    min-height: 60px;
    max-width: 60px;
    max-height: 60px;
    background: var(--Primary);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.card h4 {
    font-size: 20px;
    font-weight: bold;
    margin-top: 10px;
}

.card p {
    opacity: 0.7;
    margin-top: 15px;

}

.card a {
    opacity: 0.9;
    margin-top: 25px;
    text-decoration: none;
    font-weight: 500;
    transition: 0.3s; 
}

</style>