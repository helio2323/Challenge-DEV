<template>
    
    <main class="layout">
        <section class="main-section">
        <IndexMainHero />
        </section>
        <section class="feature-section">
            <IndexFeaturesMain />
        </section>
        <section class="ab-sec">
            <IndexAboutCard />
        </section>

        <section class="pricing-section">
            <IndexPrincingMain />
        </section>

        <section class="testemunhas-section">
            <IndexTestemunhasMain />
        </section>

        <section class="team-section">
            <IndexTeamMain />
        </section>

        <section class="team-section">
            <IndexFooterMain />
        </section>
    
    </main>

</template>

<script setup>

</script>

<style  scoped>
.layout{
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: center;
    width: 100vw;
    height: fit-content;
    background-color: var(--BackCover);
}
.main-section {
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: start;
    width: 100%;
    height: 80%;
    height: fit-content;
    background-color: var(--BackCover);
}

.feature-section {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: fit-content;
    background-color: var(--BackCover);
}

.ab-sec {
    width: 100vw;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
    background-color: var(--Background);
}

.pricing-section {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100vw;
    height: 100%;
    background-color: var(--Background);
}

.testemunhas-section{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100vw;
    height: 100%;
    background-color: var(--BackCover);
}

.team-section{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100vw;
    height: 100%;
    background-color: var(--Background);
}
</style>