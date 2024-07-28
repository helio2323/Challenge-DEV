<template>
<header>
    <section class="logo-section">
    <img class="logo" src="../../../shared/images/Logo.png" alt="">
    <div class="hamburger" @click="toggleMenu">
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
    </div>
    <ul class="menu" :class="{ active: isMenuActive }">
        <li>Home</li>
        <li>About</li>
        <li>Pricing</li>
        <li>Team</li>
        <li>Contact</li>
    </ul>
    <div class="buttons" :class="{ active: isMenuActive }">
        <UButton @click="handleRegister" variant="outline" class="text-sm h-10 w-[150px] justify-center align-middle" type="submit">
        Criar Conta
        </UButton>
        <UButton @click="handleLogin" class="text-sm h-10 w-[150px] justify-center align-middle bg-transparent" type="submit">
        Entrar
        </UButton>
    </div>

    </section>
</header>
</template>

<script setup>
import { ref } from 'vue';

const isMenuActive = ref(false);

const toggleMenu = () => {
isMenuActive.value = !isMenuActive.value;
};

const handleLogin = () => {
    navigateTo('/login');
};

const handleRegister = () => {
    navigateTo('/register');
}

</script>

<style  scoped>
header {
width: 100%;
display: flex;
flex-direction: column;
justify-content: center;
align-items: center;
padding: 5px 10%;
background-color: var(--Background);
}

.logo {
width: 200px;
height: auto;
}

.logo-section {
display: flex;
width: 100%;
max-width: 1920px;
align-items: center;
justify-content: space-between;
flex-wrap: wrap;
position: relative;
}

.menu {
display: flex;
gap: 20px;
list-style: none;
padding: 0;
margin: 0;
}

.menu li:hover {
color: var(--Primary);
cursor: pointer;
font-weight: bold;
text-decoration: underline;
text-underline-offset: 10px;
text-decoration-color: var(--Primary);
transition: all 0.5s;
}

.buttons {
display: flex;
gap: 20px;
margin-top: 10px;
}

.hamburger {
display: none;
flex-direction: column;
cursor: pointer;
}

.hamburger .bar {
width: 25px;
height: 3px;
background-color: var(--Primary);
margin: 4px 0;
transition: 0.4s;
}

@media screen and (max-width: 1366px) {

    header{
        padding: 5px 2%;
    }
    
}


@media (max-width: 950px) {
.menu, .buttons {
    display: none;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

.menu.active, .buttons.active {
    display: flex;
}

.hamburger {
    display: flex;
}
}
</style>
