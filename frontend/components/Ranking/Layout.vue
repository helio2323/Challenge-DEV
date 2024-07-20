<template>
    <main class="layout">
        <div class="layout-diario">
            <section class="main-section">
                <div class="main-header">
                    <h1>TOP USUÁRIO <strong>DIÁRIO</strong></h1>
                </div>
                <RankingDiarioTable />
            </section>
        </div>

        <div class="layout-geral">
            <section class="main-section">
                <div class="main-header">
                    <h1>TOP USUÁRIO <strong>SEMANAL</strong></h1>
                </div>
                <RankingDiarioTable />

            </section>
        </div>
    </main>

</template>

<script setup>

</script>

<style scoped>

.main-section {
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: start;
    width: 100%;
    height: 100%;
    background-color: var(--BackCover);
}

.layout {
    display: flex;
    flex-direction: row;
    justify-content: start;
    align-items: center;
    width: 100%;
    height: 100%;
    gap: 20px;
    padding: 20px;
}

.layout-diario {
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: start;
    width: 50%;
    height: 100%;
    background-color: var(--BackCover);
    border-radius: 20px;
    padding:  0;
}

.layout-geral {
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: start;
    width: 50%;
    height: 100%;
    background-color: var(--BackCover);
    border-radius: 20px;
    padding:  0;
}

.main-header {
    padding-top: 10px;
    padding-bottom: 10px;
    border-bottom: solid 1px var(--Gray700);
}

.main-header h1 {
    font-size: 1.5rem;
    font-weight: 600;
}

strong{
    color: var(--Primary);

}

.main-section{
    padding: 20px;
}

@media screen and (max-width: 1150px) {
    .layout {
        flex-direction: column;
    }

    .layout-diario {
        width: 100%;
        align-items: center;
    }

    .layout-geral {
        width: 100%;
        align-items: center;
    }
}

</style>