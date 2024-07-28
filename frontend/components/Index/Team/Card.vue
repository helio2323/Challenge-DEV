<template>
    <div class="card">
        
        <img :src="avatarImg" alt="">

        <div class="team">
            <div class="team-text">
                <NuxtLink target="_blank" :to="tLink">{{ callToAction }}</NuxtLink>
                <p>{{ Skill }}</p>
            </div>
        </div>

        <div class="team-infos">
            <NuxtLink to="https://github.com/helio2323" target="_blank" >
                <img width="50" height="50" src="https://img.icons8.com/ios-filled/50/FFFFFF/github.png" alt="github"/>
            </NuxtLink>
            <NuxtLink to="https://www.linkedin.com/in/helioreislima/" target="_blank" >
                <img width="50" height="50" src="https://img.icons8.com/ios-filled/50/FFFFFF/linkedin.png" alt="github"/>
            </NuxtLink>
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
    justify-content: start;
    align-items: center;
    gap: 20px;
    width: 280px;
    height: 270px;
    border-radius: 10px;
    padding: 20px;
    margin-top: 30px;
    border: solid 1px rgba(0, 220, 130,0.5);
}

.card img{
    width: 100px;
    height: 100px;
    border-radius: 50%;
    margin-top: 10px;
}

.card:hover{
    border: solid 1px var(--Primary);
    box-shadow: 0 0 40px rgba(0, 220, 130, 0.5);
    transition: all 0.5s;
}

.card-image {
    display: flex;
    flex-direction: row;
    width: 100%;
    gap: 5px;
}

.team{
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 10px;
    align-items: center;
}


.team-text {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: start;
}

.team-text p {
    opacity: 0.7;
    font-size: 14px;

}

.team-infos {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 30px;
}

.team-infos img {
    width: 30px;
    height: 30px;
    opacity: 0.5;
}

.team-infos img:hover {
    opacity: 1;
    transition: all 0.5s;
}

</style>