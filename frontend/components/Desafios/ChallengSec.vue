<template>
    <div class="challeng">
        <section class="challeng-cards">
            <div class="tittle-infos">
                <h3 class="tittle">Inicie agora seu aprendizado</h3>
                <DesafiosChallengSecModalInfos class="phone-infos"/>
            </div>
            <DesafiosChallengSecChallengCard />
            <DesafiosChallengSecChallengCard />
            <DesafiosChallengSecChallengCard /> 
            <DesafiosChallengSecChallengCard /> 
            <DesafiosChallengSecChallengCard /> 
            <DesafiosChallengSecChallengCard /> 
            <DesafiosChallengSecChallengCard /> 
            <div class="challeng-pagination">
                <DesafiosChallengSecChallengPagination />
            </div>
            
        </section>
        <DesafiosChallengSecChallengInfos class="challeng-infos" />
    </div>
</template>

<script setup>

</script>

<style  scoped>

.tittle-infos{
    display: flex;
    width: 100%;
    justify-content: space-between;
}

.challeng {
    display: flex;
    flex-direction: row;
    gap: 40px;
}

.tittle{
    font-size: 28px;
    font-weight: 500;
}

.challeng-cards{
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: start;
    justify-content: start;
    gap: 20px;
}

.challeng-pagination{
    display: flex;
    flex-direction: row;
    align-items: start;
    justify-content: end;
    height: 100%;
    width: 100%;
    gap: 20px;
}

.phone-infos{
    display: none;
}

@media screen and (max-width: 950px) {
    .challeng {
        display: flex;
        flex-direction: column;
        width: 100%;
        align-items: center;
    }

    .challeng-cards{
        width: 100%;
    }

    .challeng-infos{
        display: none;
    }

    .phone-infos{
        display: flex;
    }   

@media screen and (max-width: 500px) { 
    .tittle {
        font-size: 20px;
    }
    
}
}

</style>