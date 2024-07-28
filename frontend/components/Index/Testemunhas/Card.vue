<template>
    <div class="card">
        <div class="card-image">
            <img width="15" height="15" :src="imgLogo" alt="code--v1"/>
            <img width="15" height="15" :src="imgLogo" alt="code--v1"/>
            <img width="15" height="15" :src="imgLogo" alt="code--v1"/>
            <img width="15" height="15" :src="imgLogo" alt="code--v1"/>
            <img width="15" height="15" :src="imgLogo" alt="code--v1"/>
        </div>

        <p>{{ subtitle }}</p>

        <div class="testemunha">
            <img :src="avatarImg" alt="">
            <div class="testemunha-text">
                <NuxtLink target="_blank" :to="tLink">{{ callToAction }}</NuxtLink>
                <p>{{ Skill }}</p>
            </div>
        </div>

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
        default: '"Depois que comecei a usar o Challenge DEV melhorei muito minhas habilidades com python"'
    },
    callToAction: {
        type: String,
        default: 'Helio Fernandes'
    },
    imgLogo: {
        type: String,
        default: 'https://img.icons8.com/fluency/48/star--v1.png'
    },
    tLink: {
        type: String,
        default: 'https://github.com/helio2323'
    },
    Skill: {
        type: String,
        default: 'FullStack Developer'
    },
    avatarImg: {
        type: String,
        default: 'https://github.com/helio2323.png'
    },

})

</script>

<style scoped>

.card {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    width: 280px;
    height: 270px;
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
    display: flex;
    flex-direction: row;
    width: 100%;
    gap: 5px;
}

.testemunha{
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 10px;
    align-items: center;
    margin-top: 20px;
}

.testemunha img{
    width: 40px;
    height: 40px;
    border-radius: 50%;
}

.testemunha-text {
    display: flex;
    flex-direction: column;
    align-items: start;
    justify-content: start;
}

.testemunha-text p {
    opacity: 0.7;
    font-size: 14px;

}

</style>