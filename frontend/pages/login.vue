<template>
    <main>
       <div class="register">
            <div class="register-form">                 
                <div class="register-form-itens">
                    <img width="50" height="50" src="https://img.icons8.com/material-sharp/24/FFFFFF/user-male-circle.png" alt="user-male-circle"/>
                    <h1>Sejam bem vindo</h1>
                    <p>Não tem uma conta? <a href="/register">Criar conta</a></p>
                    <RegisterLoginForm />
                </div>
            </div>

            <div class="image-form">
                <div class="image-form-cover">
                    <img src="../shared/images/Logo.png" alt="">
                </div>
            </div>
       
       </div>
    </main>
</template>

<script setup>

definePageMeta({
    layout: 'empty',
})

</script>

<style scoped>

main {
    width: 100vw;
    height: 100vh;
    background-color: var(--Background);
    padding: 20px;
}

.register {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: row;
    gap: 20px;
    align-items: center;
    justify-content: center
}

.register-form {
    width: 50%;
    height: 100%;
    padding: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.register-form-itens h1 {
    font-size: 40px;
    font-weight: 600;
    width: 100%;
    text-align: center;
}

.register-form-itens p {
    font-size: 18px;
    font-weight: 400;
}

.register-form-itens a:hover {
    text-decoration: underline;
}

.register-form-itens a {
    color: var(--Primary);
    text-decoration: none;
}

.register-form-itens {
    width: 60%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 20px;
}


.image-form {
    width: 50%;
    height: 100%;
    background-image: url("../shared/images/ww-one-bit.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    border-radius: 20px
}

.image-form-cover{
    width: 100%;
    height: 100%;
    background-color: rgba(19, 30, 44, 0.8);
    border-radius: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.image-form-cover img {
   
}

@media screen and (max-width: 1150px) {
    .register-form-itens {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 20px;
}

@media screen and (max-width: 850px) {
    .image-form {
        display: none;
    }
    .register {
        flex-direction: column;
        align-items: center;
        justify-content: center
    }
    .register-form {
        width: 100%;
        align-items: center;
        justify-content: center;
    }
}

@media screen and (max-width: 500px) {
    main {
        padding: 0;
    }

    .register-form-itens h1 {
        font-size: 36px;
        font-weight: 600;
        text-align: center;
    }

    .register-form-itens p {
        font-size: 16px;
        font-weight: 400;
        text-align: center;

    }

    .register-form-itens a {
        color: var(--Primary);
        text-decoration: none;
    }

    .register-form {
        padding: 10px;
    }
}

}


</style>