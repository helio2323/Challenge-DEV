export async function getUserInfos(id){
    try {
        const myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");

        const requestOptions = {
            method: 'GET',
            headers: myHeaders,
            redirect: 'follow'
        };

        const response = await fetch(`http://localhost:5000/api/v1/user/${id}`, requestOptions);
        const result = await response.json(); // Converte a resposta para JSON
        return result;

    } catch (error) {
        console.log('Erro de rede:', error);
        throw error;
    }
}