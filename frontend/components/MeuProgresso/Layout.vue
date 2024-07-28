<template>
    <div class="layout">
        <section class="main-section">
            <MeuProgressoCardProfile />
            <MeuProgressoProgress />
            <!-- 
                        <h2>Conquistas</h2>

            <div class="conquistas-section">
                <div class="conquistas">
                <MeuProgressoCardConquista />
                </div>
                <h2>Linaguagens Favoritas</h2>
                <div class="linguagens">
                    <MeuProgressoCardLinguagem />
                </div>
            </div>
            -->
        </section>
    </div>
</template>

<script setup>

</script>

<style scoped>

.layout {
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: center;
    width: 100%;
    height: 100%;
    padding: 20px;
}

.main-section {
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: start;
    width: 100%;
    height: 100%;
    background-color: var(--BackCover);
    border-radius: 20px;
    padding: 20px;
}

.main-section h2 {
    font-size: 20px;
    font-weight: bold;
    margin-top: 20px;
    margin-bottom: 20px;
}

.conquistas-section {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

</style>