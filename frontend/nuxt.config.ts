// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  modules: ["@nuxt/ui", "@nuxtjs/tailwindcss", "nuxt-monaco-editor"],
  
  alias: {
    css: "/<rootDir>/assets/css",
    },
    css: ["~/assets/css/main.css"],
      app: {
    pageTransition: { name: 'page', mode: 'out-in' }
  },
})