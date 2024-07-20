<template>
    
    <main class="main-card-profile">
        <h2>Atividades</h2>
        <div class="card-profile"> 
            <div class="image">
                <img src="https://cdn3d.iconscout.com/3d/premium/thumb/python-6815592-5602757.png?f=webp" alt="">
            </div>
            <div class="infos">
                <p>Helio F</p>
                <p>Level</p>
                <p>20 XP</p>
            </div>
            
        </div>

    </main>


</template>

<script setup>

</script>

<style scoped>

.main-card-profile {
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: start;
    width: 100%;
    gap: 20px;
}
.main-card-profile h2 {
    width: 100%;
    font-size: 20px;
    font-weight: bold;
}

.card-profile {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: fit-content;
}

.card-profile img {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    margin-right: 20px;
}

.infos {
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: start;
    width: 100%;
    height: 100%;
    gap: 5px;
}

.image {
    display: flex;
    flex-direction: column;
    height: 100%;
    align-items: center;
    justify-content: center;
}

</style>