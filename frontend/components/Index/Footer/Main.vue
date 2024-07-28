<template>
<footer class="footer">
  <div class="footer__addr">
    <img class="footer__logo" src="../../../shared/images/Logo.png" alt="">
        
    <h2>Contact</h2>
    
    <address>
    +55 11 9999-9999<br>
          
      <a class="footer__btn" href="mailto:example@gmail.com">helio_lima@outlook.com.br</a>
    </address>
  </div>
  
  <ul class="footer__nav">
    <li class="nav__item">
      <h2 class="nav__title">Siga em</h2>

      <ul class="nav__ul">
        <li>
          <a href="https://github.com/helio2323">Github</a>
        </li>

        <li>
          <a href="https://www.linkedin.com/in/helioreislima/">Linkedin</a>
        </li>
      </ul>
    </li>
    
    <li class="nav__item">
      <h2 class="nav__title">Comunidade</h2>
      
      <ul class="nav__ul">
        <li>
          <a href="#">Youtube</a>
        </li>
        
        <li>
          <a href="#">Discord</a>
        </li>
        
        <li>
          <a href="#">Facebook</a>
        </li>
      </ul>
    </li>
    
    <li class="nav__item">
      <h2 class="nav__title">Plataformas</h2>
      
      <ul class="nav__ul">
        <li>
          <a href="#">Mobile</a>
        </li>
        
        <li>
          <a href="#">Desktop</a>
        </li>
        
        <li>
          <a href="#">Web</a>
        </li>
      </ul>
    </li>
  </ul>
  
  <div class="legal">
    <p>&copy; 2024 ChallengeDEV. All rights reserved.</p>
    
    <div class="legal__links">
      <span>Feito com <span class="heart">♥</span> por ChallengeDEV</span>
    </div>
  </div>
</footer>
</template>

<script setup lang="ts">

</script>

<style scoped>
*, *:before, *:after {
  box-sizing: border-box;
}

html {
  font-size: 100%;
}

body {
  font-family: acumin-pro, system-ui, sans-serif;
  margin: 0;
  display: grid;
  grid-template-rows: auto 1fr auto;
  font-size: 14px;
  background-color: #f4f4f4;
  align-items: start;
  min-height: 100vh;
}

.footer {
  display: flex;
  flex-flow: row wrap;
  padding: 30px 30px 20px 30px;
  color: var(--Primary);
  background-color: var(--Background);
  border-top: 1px solid #e5e5e5;
  width: 100%;
  height:fit-content;
}

.footer > * {
  flex:  1 100%;
}

.footer__addr {
  margin-right: 1.25em;
  margin-bottom: 2em;
}

.footer__logo {
  width: 150px;
}

.footer__addr h2 {
  margin-top: 1.3em;
  font-size: 15px;
  font-weight: 400;
}

.nav__title {
  font-weight: 600;
  font-size: 20px;
}

.footer address {
  font-style: normal;
  color: #FFF;
}

.footer__btn {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 36px;
  max-width: max-content;
  background-color: rgb(33, 33, 33, 0.07);
  border-radius: 100px;
  color: #FFF;
  line-height: 0;
  font-size: 1rem;
}

.footer ul {
  list-style: none;
  padding-left: 0;
}

.footer li {
  line-height: 2em;
}

.footer a {
  text-decoration: none;
}

.footer__nav {
  display: flex;
	flex-flow: row wrap;
}

.footer__nav > * {
  flex: 1 50%;
  margin-right: 1.25em;
}

.nav__ul a {
  color: #FFF;
}

.nav__ul--extra {
  column-count: 2;
  column-gap: 1.25em;
}

.legal {
  display: flex;
  flex-wrap: wrap;
  color: #FFF;
}
  
.legal__links {
  display: flex;
  align-items: center;
}

.heart {
  color: #FFF;
}

@media screen and (min-width: 24.375em) {
  .legal .legal__links {
    margin-left: auto;
  }
}

@media screen and (min-width: 40.375em) {
  .footer__nav > * {
    flex: 1;
  }
  
  .nav__item--extra {
    flex-grow: 2;
  }
  
  .footer__addr {
    flex: 1 0px;
  }
  
  .footer__nav {
    flex: 2 0px;
  }
}
</style>