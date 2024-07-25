<template>
        <div class="layout-diario">
            <section class="main-section">
                <div class="main-header">
                    <h1>Inclusão de Desafio</h1>
                    <div class="button-adm">
                        <AdmListButton class="button" @click="handleClick"/>
                    </div>
                </div>
                <AdmTable />
            </section>
        </div>


</template>

<script setup>
import { qType } from '~/api/statGlobal';

const handleClick = () => {
    qType.value = false;
}

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
    border-radius: 20px;
}

.layout-diario {
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: start;
    width: 100%;
    height: 100%;
    background-color: var(--BackCover);
    border-radius: 20px;
    padding:  20px;
}

.main-header {
    display: flex;
    flex-direction: column;
    width: 100%;
    padding-top: 10px;
    padding-bottom: 10px;
    border-bottom: solid 1px var(--Gray700);
}

.main-header h1 {
    font-size: 1.5rem;
    font-weight: 600;
    width: 100%;
}

.button-adm {
    display: flex;
    width: 100%;
    justify-content: end;
    align-items: end;
    gap: 10px;
}



</style>