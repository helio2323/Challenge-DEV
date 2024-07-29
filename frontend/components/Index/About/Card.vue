<template>
    <main class="about-card">

        <div class="content">

            <section class="content-card">

                <span>
                    <p>Sobre nós</p>
                </span>

                <h3>Acreditamos que o conhecimento deve ser uma fonte gratuita </h3>

                <p>Acreditamos que o conhecimento deve ser acessível para todos. Nossa missão é democratizar a educação, garantindo que qualquer pessoa, independentemente de sua localização geográfica ou condição financeira, tenha acesso às ferramentas e recursos necessários para aprender e crescer.
                </p>

                <p>Ao promover a troca livre de informações e a colaboração global, aspiramos a criar uma comunidade onde o aprendizado contínuo e o desenvolvimento pessoal sejam valorizados e incentivados.
                </p>

                <UButton color="green" class="btn h-[50px] w-[150px] text-center justify-center ">
                    Saiba Mais
                </UButton>

            </section>
            <div class="content-img">
           
            </div>
        </div>

    </main>

</template>

<script setup>  

</script>

<style scoped>

.about-card {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    padding: 20px;
    gap: 20px;
    width: 100%;
    height: 100%;
    margin-bottom: 50px;
    max-width: 1920px;
}

.content {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: space-between;
    padding: 40px;
    margin-top: 50px;
    gap: 20px;
    width: 80%;
    background: var(--BackCover);
    border-radius: 10px;
    height: 100%;
}

.content img {
    width: 50%;
    height: 500px;
}

.content-card {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 0px;
    gap: 10px;
    width: 50%;
    min-height: 500px;
}

span {
    display: flex;
    background-color: var(--Primary);
    padding: 5px;
    width: 100px;
    align-items: center;
    justify-content: center;
    border-radius: 5px;
}
span p {
    color: var(--BackCover);
    font-weight: 500;
}

.btn {
    font-weight: 700;
    color: var(--BackCover);
}

.content-img {
    display: flex;
    flex-direction: column;
    width: 40%;
    min-height: 550px;
    background-image: url("../../../shared/images/student.png");
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
    border-radius: 10px;
}

@media (max-width: 1366px) {
    .content {
        width: 100%;
    }
}

/* Para telas menores que 900px */
@media (max-width: 950px) {
.content {
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    padding: 10px;
}
.content-img{
    width: 100%;
    min-height: 200px;
    background-image: url("../../../shared/images/student.png");
}
.content-card {
    width: 100%;
    align-items: center;
    text-align: center;
}


}
/* Para telas menores que 600px */
@media (max-width: 600px) {

}

</style>