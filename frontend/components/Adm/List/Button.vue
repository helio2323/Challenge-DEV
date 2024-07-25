<template>
  <div class="button-adm">
    <NuxtLink class="nuxt-link" to="/admnovodesafio">
      <UButton
        class="btn"
        size="sm"
        color="primary"
        variant="solid"
        label="+ Desafio"
        :trailing="false"
      />
    </NuxtLink>
  </div>
</template>

<style scoped>
.button-adm {
  display: flex;
  flex-direction: row;
  width: 220px;
  align-items: center;
  justify-content: center;
  gap: 20px;
  border-radius: 15px;
  
}

.btn {
  width: 100%;
  height: 40px;
  border-radius: 15px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  }

  .button-adm a {
    width: 220px;
    
  }

</style>
