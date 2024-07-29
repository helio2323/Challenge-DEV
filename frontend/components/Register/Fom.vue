<script setup lang="ts">
import type { FormError, FormSubmitEvent } from '#ui/types'
import {Loading} from '../frontend/api/statGlobal'

import {register} from "../../api/authentication"

const state = reactive({
  email: "",
  password: "",
  nome: "",
  confirmesuasenha: ""
})


const validate = (state: any): FormError[] => {
  const errors = []
  if (!state.nome) errors.push({ path: 'nome', message: 'Required' })
  if (!state.email) errors.push({ path: 'email', message: 'Required' })
  if (!state.password) errors.push({ path: 'password', message: 'Required' })
  if (state.password !== state.confirmesuasenha) errors.push({ path: 'confirmesuasenha', message: 'Invalid password' })

  return errors

}

// chamada api para registro
const toast = useToast()

function onClick () {
  alert('Clicked!')
}
async function onSubmit(event: FormSubmitEvent<any>) {
    // Do something with data
    const name = event.data.nome;
    const email = event.data.email;
    const password = event.data.password;
    Loading.value = true
    try {
        // Usar await na chamada da API
        const response = await register(name, email, password);
        
        if (response.message === "User created") { // Verificar o conteúdo da resposta
            // Redirecionar para login
            navigateTo('/login')
            Loading.value = false
        } else {
            console.log("Erro: ", response.message);
            Loading.value = false
        }
    } catch (error) {
        Loading.value = false
        console.log('Erro ao registrar:', error);
        
        
    }
}

</script>

<template>
<div>
    <UForm :validate="validate" :state="state" class="space-y-4" @submit="onSubmit">
      <UFormGroup label="Nome" name="nome">
        <UInput placeholder="Nome" v-model="state.nome" />
      </UFormGroup>

      <UFormGroup label="Email" name="email">
        <UInput placeholder="Email" v-model="state.email" />
      </UFormGroup>

      <UFormGroup label="Senha" name="password">
        <UInput placeholder="Senha" v-model="state.password" type="password" />
      </UFormGroup>

      <UFormGroup label="Confirme sua senha" name="confirmesuasenha">
        <UInput placeholder="Confirme sua senha" v-model="state.confirmesuasenha" type="password" />
      </UFormGroup>   

      <UButton @click="toast.add({ title: 'Click me', click: onClick })" class="btn" type="submit">
        Criar Conta
      </UButton>

  </UForm>
</div>
</template>

<style scoped>

div {
    width: 100%;
}

.btn {
    width: 100%;
    height: 40px;
    border-radius: 10px;
    background-color: var(--Primary);
    color: white;
    font-weight: 600;
    align-items: center;
    justify-content: center;
    border-radius: 20px;
}

</style>

