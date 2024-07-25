import axios from 'axios'

export default defineNuxtPlugin(() => {
  const instance = axios.create({
    baseURL: 'http://localhost:3000/api/v1' // URL base da sua API
  })

  return {
    provide: {
      axios: instance
    }
  }
})
