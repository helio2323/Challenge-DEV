<template>
    <div class="pricing-layout">
        <section class="pricing-main">
            
            <div class="pricing-header">
                <span><p>Preços</p></span>
                <h2>Conheça nosso plano</h2>
                <p>Sim isso mesmo, totalmente gratuito, fazemos questao de mostrar para nossos usuarios
                que conhecimento e experiência fazem a diferência</p>
            </div>

            <div class="pricing-cards"> 
                
                <IndexPrincingCard
                price="0,00"
                :items="freePlan" />
            
            </div>
        
        </section>
    </div>
</template>

<script setup>

const check = 'https://img.icons8.com/flat-round/64/checkmark.png'
 const no = 'https://img.icons8.com/color/48/cancel--v1.png'


 const freePlan = [
  { text: 'Acesso ao código fonte', icon: check },
  { text: 'Acesso a todos exercícios', icon: check },
  { text: 'Exercícios de programação', icon: check },
  { text: 'Executar o código no navegador', icon: check },
  { text: 'Executar o código em celulares', icon: check },
  { text: 'Exercícios de Quiz', icon: check },

  // Novos itens...
  { text: 'Feedback automático em exercícios', icon: check },
  { text: 'Acesso a webinars', icon: check },
  { text: 'Código exemplo comentado', icon: check },
  { text: 'Atualizações regulares de conteúdo', icon: check },
  { text: 'Integração com GitHub', icon: check },
];


</script>

<style  scoped>

.pricing-layout {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
    background-color: var(--Backcover);
    max-width: 1920px;

}

.pricing-main {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 80%;
    height: fit-content;
    margin-top: 20px;
}

.pricing-header {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 100%;
    gap: 20px;
}

.pricing-header p {
    width: 50%;
    text-align: center;
}

.pricing-cards {
    margin-bottom: 50px;
}

span p {
    font-size: 20px;
    font-weight: 500;
    color: var(--Primary);
}


@media (max-width: 1366px) {
    .pricing-layout {
        padding: 10px;
    }
}

/* Para telas menores que 900px */
@media (max-width: 950px) {
    .pricing-main{
        width: 100%;
    }

}
/* Para telas menores que 600px */
@media (max-width: 600px) {
.pricing-header p {
    width: 100%;
}
}

</style>