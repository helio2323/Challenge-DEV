<template>
    <main class="layout">
      <div class="layout-geral">
        <section class="main-section">
          <div class="main-header">
            <h1>TOP USUÁRIO <strong>GERAL</strong></h1>
          </div>
          <RankingDiarioTable :data="weeklyRanking" />
        </section>
      </div>
      <div class="layout-diario">
        <section class="main-section">
          <div class="main-header">
            <h1>TOP USUÁRIO <strong>DIÁRIO</strong></h1>
          </div>
          <RankingDiarioTable :data="dailyRanking" />
          
        </section>
      </div>
    </main>
  </template>
  
  <script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import useRanking from '@/composables/useRanking';
  
  const { fetchAllRanking, fetchDailyRanking } = useRanking();
  const dailyRanking = ref<Array<{ id: number; usuario: string; pontos: number; respostas: number }>>([]);
  const weeklyRanking = ref<Array<{ id: number; usuario: string; pontos: number; respostas: number }>>([]);
  
  onMounted(async () => {
      try {
          const resultDaily = await fetchDailyRanking();
          dailyRanking.value = resultDaily.map((item: any) => ({
              id: item.id,
              usuario: item.name,
              pontos: item.points,
              respostas: item.responses,
          }));
  
          const resultWeekly = await fetchAllRanking();
          weeklyRanking.value = resultWeekly.map((item: any) => ({
              id: item.id,
              usuario: item.name,
              pontos: item.points,
              respostas: item.responses,
          }));
      } catch (error) {
          console.error('Error fetching rankings:', error);
      }
  });
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
}

.layout {
    display: flex;
    flex-direction: row;
    justify-content: start;
    align-items: center;
    width: 100%;
    height: 100%;
    gap: 20px;
    padding: 20px;
}

.layout-diario {
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: start;
    width: 50%;
    height: 100%;
    background-color: var(--BackCover);
    border-radius: 20px;
    padding:  0;
}

.layout-geral {
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: start;
    width: 50%;
    height: 100%;
    background-color: var(--BackCover);
    border-radius: 20px;
    padding:  0;
}

.main-header {
    padding-top: 10px;
    padding-bottom: 10px;
    border-bottom: solid 1px var(--Gray700);
}

.main-header h1 {
    font-size: 1.5rem;
    font-weight: 600;
}

strong{
    color: var(--Primary);

}

.main-section{
    padding: 20px;
}

@media screen and (max-width: 1150px) {
    .layout {
        flex-direction: column;
    }

    .layout-diario {
        width: 100%;
        align-items: center;
    }

    .layout-geral {
        width: 100%;
        align-items: center;
    }
}

</style>
  