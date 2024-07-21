<script setup lang="ts">
import type { FormSubmitEvent } from '#ui/types'

const state = reactive({
  email: undefined,
  password: undefined
})

async function onSubmit (event: FormSubmitEvent<Schema>) {
  // Do something with event.data
  console.log(event.data)
}
</script>

<template>
  <UForm :schema="schema" :state="state" class="space-y-4 max-w-3xl form-group" @submit="onSubmit">

    <section class="flex flex-row gap-5 w-full ">
      <UFormGroup class="flex-col w-full max-w-96 form-group" label="Titulo" name="titulo">
        <UInput class="w-full" v-model="state.title" />
      </UFormGroup>
      <UFormGroup class="w-full max-w-96 form-group" label="Subtitle" name="subtitle">
        <UInput v-model="state.subtitle" />
      </UFormGroup>
    </section>

    <section class="flex flex-row gap-5 w-full">
      <UFormGroup class="w-full max-w-96 form-group" label="Tipo Desafio" name="tipodesafio">
        <UInputMenu v-model="selectedSubtitle" :options="subtitles" />
      </UFormGroup>
      <UFormGroup class="w-full max-w-96 h-fit form-group" label="Exemplo" name="exemplo">
        <UTextarea autoresize v-model="value" />
      </UFormGroup>
    
    </section>
    <section>
        <UFormGroup class="w-full max-w-96 h-fit form-group" label="Pergunta" name="pergunta">
          <UTextarea autoresize class="" v-model="value" />
      </UFormGroup>
    </section>
    <section class="flex flex-row gap-5 w-full form-group">
      <UFormGroup class="w-full max-w-96 " label="Linguagem" name="linguagem">
        <UInputMenu v-model="selectedSubtitle" :options="subtitles" />
      </UFormGroup>
      <UFormGroup class="w-full max-w-96 form-group" label="XP Reward" name="xpreward">
        <UInput v-model="state.subtitle" />
      </UFormGroup>
    </section>
    <h3>Resposta</h3>
    <section class="flex flex-row gap-5 w-full">
      <UFormGroup class="w-full max-w-96 form-group " label="Range Opções" name="rangeopcoes">
        <UInputMenu v-model="selectedSubtitle" :options="subtitles" />
      </UFormGroup>
      <UFormGroup class="w-full max-w-96 form-group" label="Resposta" name="resposta">
        <UInput v-model="state.subtitle" />
      </UFormGroup>
    </section>
    <section class="flex flex-row gap-5 w-full justify-end ">
      <UButton class="w-48 h-8 justify-center rounded-3xl " type="submit">
        + Desafio
      </UButton>
    </section>
  </UForm>
</template>

<style scoped>
.input {
  width: 100%;
}

h3 {
  font-size: 1.2rem;
  font-weight: 600;
  width: 100%;
  color: var(--Primary);
}

@media screen and (max-width: 1150px) {
  section {
    width: 100%;
    flex-direction: column;
    align-items: start;
    justify-content: start;
    margin: 0;
  }

  .form-group {
    width: 100%;
    max-width: 100%;
  }

}

</style>

