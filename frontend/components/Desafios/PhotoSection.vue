<template>
    <main class="main-photo">
        <section class="cover-photo">
            <DesafiosPhotoComponentsMainText
            text="PYTHON" />
            <div class="input-menu">
                <DesafiosPhotoComponentsLanguageInput />
                <DesafiosPhotoComponentsLevelInput />
            </div>

            <DesafiosPhotoComponentsProgressBar />
        </section>
    </main>

</template>

<script setup>

</script>

<style scoped>
.main-photo {
    width: 100%;
    display: flex;
    flex-direction: column;
    background-color: red;
    height: 250px;
    border-radius: 20px 20px 0px 0px;
    background-image: url('../../shared/images/ww-one-bit.jpg');
    background-size: cover;
    background-position: center;
}

.cover-photo {
    width: 100%;
    height: 100%;
    background-color: rgba(19, 30, 44, 0.7);
    border-radius: 20px 20px 0px 0px;
    display: flex;
    flex-direction: column;
    padding: 20px;
    gap: 10px;
}



.aside-data {
    width: 100%;
    height: 100%;
    background-color: #131E2C;
    border-radius: 0px 0px 20px 20px;
}

.input-menu {
    display: flex;
    flex-direction: row;
    gap: 20px;
}

@media screen and (max-width: 500px) {
    .cover-photo{
        padding: 10px;
    }
}

</style>
