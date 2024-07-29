<template>
    <section class="ud-features">
        <div class="content-features">
            <strong><p>Features</p></strong>
            <h2>Conheça os nossos recursos</h2>
            <p>Aprenda de maneira simples e eficaz</p>

            <section class="card-features">
                <IndexFeaturesCard  />
                <IndexFeaturesCard
                imgLogo="https://img.icons8.com/ios-glyphs/30/FFFFFF/console.png"
                title="Console Web"
                subtitle="A plataforma Challenge DEV tem terminal integrado
                para execução do código no navegador" />
                <IndexFeaturesCard
                imgLogo="https://img.icons8.com/ios/50/FFFFFF/xbox-controller.png"
                title="Gamificação"
                subtitle="Responde perguntas, ganhe pontos de XP e avance de nível
                e evolua junto com seus amigos"
                 />
                
                <IndexFeaturesCard
                imgLogo="https://img.icons8.com/external-vitaliy-gorbachev-lineal-vitaly-gorbachev/60/FFFFFF/external-free-sales-vitaliy-gorbachev-lineal-vitaly-gorbachev.png"
                title="Forever FREE"
                subtitle="O Challenge DEV é gratuito para sempre
                não tem limitações para usuários"
                 />
            </section>
        </div>
    </section>
</template>

<script setup>

</script>

<style  scoped>

.ud-features{
    width: 100%;
    max-width: 1920px;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    height: 100%;
    padding: 20px;
    margin-top: 50px;
    margin-bottom: 50px;
}

.content-features{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: start;
    width: 80%;
    height: 100%;
}

.card-features {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(1, 1fr);
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
    gap: 20px;
}

strong {
    color: var(--Primary);
}

/* Para telas menores que 1200px */
@media (max-width: 1200px) {
    .card-features {
        grid-template-columns: repeat(3, 1fr);
    }

    .content-features {
        width: 100%;
    }
}

/* Para telas menores que 900px */
@media (max-width: 900px) {
    .card-features {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    justify-items: center; /* Centraliza horizontalmente os itens dentro da grade */
    align-items: center;   /* Centraliza verticalmente os itens dentro da grade */
    gap: 20px;             /* Espaço entre os itens da grade */
}

    .content-features{
        justify-content: center;
        align-items: center;
    }

    .content-features h2 {
        text-align: center;
    }
    
}

/* Para telas menores que 600px */
@media (max-width: 600px) {
    .card-features {
        grid-template-columns: 1fr;
    }

    .ud-features{
        padding: 10px;
    }

    .content-features h2 {
       width: 100%;
    }
}





</style>