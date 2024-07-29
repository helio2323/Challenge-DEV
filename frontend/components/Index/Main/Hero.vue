<template>
    <IndexMainHeader />
    <main class="main-hero">
        <section class="hero-section">
            <div class="hero-text gap-y-[20px]">
                <h1>O seu verdadeiro desafio começa aqui programador!</h1>
                <p>Aprenda a programar utilizando nossa plataforma de aprendizagem
                ganhando pontos e evoluindo junto a outros desenvolvedores.</p>

                <div class="flex flex-row justify-center gap-x-[20px]">
                    <UButton @click="handleGOTO" class="text-xl h-14 btn justify-center align-middle" type="submit">
                    Começar Agora!
                    </UButton>
                    <NuxtLink to="https://github.com/helio2323/OneBitDev" target="_blank" >
                    <UButton variant="outline" class="text-xl h-14 btn justify-center align-middle bg-transparent"
                        type="submit">Repositorio
                    </UButton>
                    </NuxtLink>
                </div>

                <div class="hero-languages flex flex-row gap-4">
                    <img width="50" height="50" src="https://img.icons8.com/ios-filled/50/FFFFFF/python.png" alt="python"/>
                    <img width="50" height="50" src="https://img.icons8.com/ios-filled/50/FFFFFF/javascript.png" alt="python"/>
                    <img width="50" height="50" src="https://img.icons8.com/ios/50/FFFFFF/java-coffee-cup-logo--v1.png" alt="java-coffee-cup-logo--v1"/>
                    <img width="50" height="50" src="https://img.icons8.com/external-tal-revivo-color-tal-revivo/24/FFFFFF/external-rust-is-a-multi-paradigm-system-programming-language-logo-color-tal-revivo.png" alt="external-rust-is-a-multi-paradigm-system-programming-language-logo-color-tal-revivo"/>
                </div>

                <div class="img-hero w-full"></div>
            </div>

        </section>
    </main>
</template>

<script setup>
const handleGOTO = () => {
    navigateTo('/register');
}
</script>

<style scoped>
.main-hero {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: fit-content;
    background: var(--Background);
    justify-content: end;
    align-items: center;
}

.hero-section{
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    max-width: 1920px;
    height: fit-content;
}

.hero-text {
    width: 50%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: end;
    align-items: center;
    margin-top: 100px;
}

.hero-text h1 {
    text-align: center;
    margin-bottom: 10px;
    font-weight: bold;
    padding: 10px;
}

.hero-text p {
    width: 80%;
    text-align: center;
    justify-content: center;
    font-size: 20px;
    font-weight: 400;
    padding: 10px;
    opacity: 0.8;
}

.img-hero {
    background-image: url('../../../shared/images/hero/plataform-image.png');
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    border-radius: 10px 10px 0 0;
    min-height: 300px;
}

.hero-languages img {
    opacity: 0.5;
    margin: 10px;
}
.hero-languages:hover img {
    opacity: 1;
    transition: all 0.5s;
}

.btn {
    width: 250px;
}

@media (max-width: 1366px) {
    .hero-text {
        width: 70%;
    }
}

/* Para telas menores que 900px */
@media (max-width: 950px) {
    .hero-text {
        width: 100%;
    }

    .img-hero{
        display: none;
    }

    .btn {
        width: 150px;
        font-size: 16px;
    }
    .hero-languages img {
        width: 40px;
        height: 40px;
    }
}

/* Para telas menores que 600px */
@media (max-width: 600px) {
    .hero-text {
        width: 100%;
    }

    .hero-text p {
        width: 100%;
    }
}


</style>
