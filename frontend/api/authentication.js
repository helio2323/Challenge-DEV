// Função para registro
export async function register(nome, email, password) {
    try {
        const myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");

        const raw = JSON.stringify({
            "name": nome,
            "email": email,
            "password": password
        });

        const requestOptions = {
            method: 'POST',
            headers: myHeaders,
            body: raw,
            redirect: 'follow'
        };

        const response = await fetch("http://localhost:5000/api/v1/register", requestOptions);
        const result = await response.json(); // Converte a resposta para JSON
        return result;
    } catch (error) {
        console.log('Erro de rede:', error);
        throw error;
    }
}

// Função de envio do formulário
export async function login(email, password) {
    try {
        const myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");

        const raw = JSON.stringify({
            "email": email,
            "password": password
        });

        const requestOptions = {
            method: 'POST',
            headers: myHeaders,
            body: raw,
            redirect: 'follow'
        };

        const response = await fetch("http://localhost:5000/api/v1/login", requestOptions);
        const result = await response.json(); // Converte a resposta para JSON
        return result;
    } catch (error) {
        console.log('Erro de rede:', error);
        throw error;
    }
}