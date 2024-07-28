<template>
    <section class="main-testemunhas">
        <div class="section-testemunhas">
            <div class="title-infos">
                <span>
                    <strong>Nosso time</strong>
                </span>
                <h2>Conheça nosso time estretamente capacitado</h2>
                <h4>
                    Contamos com especialistas e instrutores certificados para garantir que o aprendizado seja de qualidade.
                </h4>

            </div>
            <div class="cards">
                <IndexTeamCard />

            </div>
        </div>
    </section>
</template>

<style  scoped>

.main-testemunhas {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
    margin-top: 60px;
}

.section-testemunhas {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 80%;
    height: 100%;
}

.title-infos {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
    gap: 20px;
}

strong {
    font-weight: 600;
    text-align: center;
    width: 50%;
    color: var(--Primary);
}

.title-infos h4 {
    font-size: 18px;
    font-weight: 400;
    text-align: center;
    width: 50%;
    opacity: 0.5;
}

.cards { 
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
    gap: 20px;
    margin-bottom: 50px;

}


</style>