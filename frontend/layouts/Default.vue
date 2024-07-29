<template>
<div class="container">
    <div class="main">
        <main class="main-header">
            <img class="logo" src="../shared/images/Logo.png" @click="handleIndex">
            <DefaultHeader />    
            <DefaultProfile />
        </main>
        <aside>
            <section class="menu-section">
                <DefaultMenu />
            </section>
            <section class="main-section">
                <slot />
            </section>
        </aside>
        
    </div>
</div>
</template>

<script setup>

const handleIndex = () => {
    navigateTo('/meuprogresso')
}



</script>

<style scoped>
.logo {
    width: 150px;
    height: 100px;
    object-fit: contain;
    cursor: pointer;
}

.container{
    max-width: 100vw;
    max-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    

    
}
.main {
    background-color: var(--Background);
    width: 100%;
    max-width: 1920px;
    display: flex;
    flex-direction: column;
    height: 100vh; /* Garante que ocupe a altura total da viewport */
    
}

.main-header {
    width: 100%;
    height: 70px; /* Altura fixa de 70px */
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    border-bottom: solid 1px #475569;
}


aside {
    width: 100%;
    flex: 1; /* Faz o aside ocupar o espaço restante */
    display: flex;
    flex-direction: row;
}

.menu-section{
    width: 20%;
    height: 100%;
    max-width: 250px;
    padding: 5px 0px 100px 10px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.main-section{
    box-sizing: border-box;
    width: 100%;
    height: 100%;
    padding: 5px 20px;
}

@media screen and (max-width: 1150px) {
    .menu-section{
        display: none;
    }

    .main-section{
        padding: 0;
    }
}



</style>