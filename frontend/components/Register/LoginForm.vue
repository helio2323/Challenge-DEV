<script setup lang="ts">
import type { FormError, FormSubmitEvent } from '#ui/types'

import {login} from "../../api/authentication"

const state = reactive({
  email: "",
  password: "",
})


const validate = (state: any): FormError[] => {
  const errors = []
  if (!state.email) errors.push({ path: 'email', message: 'Required' })
  if (!state.password) errors.push({ path: 'password', message: 'Required' })
  return errors

}

// chamada api para registro
const toast = useToast()

function onClick () {
  alert('Tentando logar...')
}
async function onSubmit(event: FormSubmitEvent<any>) {
    // Do something with data
    const email = event.data.email;
    const password = event.data.password;
    
    
    try {
        // Usar await na chamada da API
        const response = await login(email, password);
        
        const respStatus = response.response

        console.log(email, password)

       if (respStatus === "User logged in") { // Verificar o conteúdo da resposta
            
            const respToken = response.token
            const respEmail = response.email

            localStorage.setItem('token', respToken);
            localStorage.setItem('email', respEmail);
            localStorage.setItem('userid', response.userid);
            localStorage.setItem('status', 'Logged in');
            
            navigateTo('/desafios');

       } else {
            console.log("Erro: ", response.message);
            //mensagem de alerta
            errors.push({ path: 'password', message: 'Required' })

       }
    } catch (error) {
        console.log('Erro ao registrar:', error);
        toast.add({ title: 'Erro ao logar', click: onClick, color: 'red', position: 'top-0 right-50' })
    }
}

</script>

<template>
<div>

    <UForm :validate="validate" :state="state" class="space-y-4" @submit="onSubmit">

    <UFormGroup label="Email" name="email">
      <UInput placeholder="Email" v-model="state.email" />
    </UFormGroup>

    <UFormGroup label="Senha" name="senha">
      <UInput placeholder="Senha" v-model="state.password" type="password" />
    </UFormGroup>

    <UButton class="btn" type="submit">
      Login
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

