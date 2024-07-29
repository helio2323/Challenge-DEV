<template>
    <section class="main-testemunhas">
        <div class="section-testemunhas">
            <div class="title-infos">
                <span>
                    <strong>Testemunhas</strong>
                </span>
                <h2>Veja o que nossos alunos estão falando</h2>
                <h4>
                    Estamos sempre focados na evolução constante dos nossos alunos
                    e no desenvolvimento de novos desafios.
                </h4>

            </div>
            <div class="cards">
                <IndexTestemunhasCard />
                <IndexTestemunhasCard
                subtitle="Este curso é incrível! O conteúdo é de alta qualidade e os instrutores são muito dedicados. Aprendi muito mais do que esperava. Vale a pena!"
                Skill="Frontend Developer"
                callToAction="Jonatas Dev"
                avatarImg="https://cdn.discordapp.com/avatars/302867290452525056/feac1e8ba8674223a70e4fe2bdc4ac1a.webp?size=160"
                 />
                <IndexTestemunhasCard
                Skill="Backend Developer"
                callToAction="Alexandre"
                avatarImg="https://cdn.discordapp.com/avatars/955456986173026304/4f90dc6bb68025429d8d0e03e2a3dbff.webp?size=160"
                subtitle="Os tutoriais são excelentes e os exercícios práticos realmente me ajudaram a aprender. Recomendo este curso para todos que querem aprender programação!" />
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
    max-width: 1920px;
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
    width: 80%;
    opacity: 0.5;
}

.cards { 
    width: 100%;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: repeat(1, 1fr);
    justify-items: center;
    width: 100%;
    height: 100%;
    gap: 20px;
    margin-bottom: 50px;

}

@media screen and (max-width: 1000px) {
    .cards {
        grid-template-columns: repeat(2, 1fr);
    }

    .title-infos {
        width: 100%;
        align-items: center;
        text-align: center;
    }

    .section-testemunhas {
        width: 100%;
    }

    .title-infos h4 {
        width: 80%;
    }
}

@media screen and (max-width: 700px) {
    .title-infos h4 {
        width: 95%;
    }

    .cards {
        grid-template-columns: repeat(1, 1fr);
    }
}

</style>