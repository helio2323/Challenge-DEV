import { ref } from 'vue';

export default function useRanking() {
    const ranking = ref<any[]>([]);
    const question = ref<any>(null);
    const error = ref<null | Error>(null);
    const loading = ref(false);

    const fetchAllRanking = async () => {
        loading.value = true;
        try {
            const response = await fetch("http://127.0.0.1:5000/api/v1/ranking", {
                method: 'GET',
                headers: {
                    "Content-Type": "application/json",
                },
                redirect: 'follow'
            });
    
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const result = await response.json();
            ranking.value = result;  // Atualiza a variável global
            return result;  // Certifique-se de que a função retorna os dados
        } catch (err) {
            error.value = err as Error;
            console.error('Erro ao fazer a requisição:', err);
            return [];  // Retorne um array vazio em caso de erro
        } finally {
            loading.value = false;
        }
    };
    

    const fetchDailyRanking = async () => {
        loading.value = true;
        const myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");
    
        const requestOptions = {
            method: "GET",
            headers: myHeaders,
            redirect: "follow"
        };
    
        try {
            const response = await fetch("http://127.0.0.1:5000/api/v1/dailyranking", requestOptions);
            
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
    
            const result = await response.json();
            return result;  // Certifique-se de que a função retorna os dados
        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
            throw error;  // Re-throw the error if you want the caller to handle it
        } finally {
            loading.value = false;
        }
    };
    

    return {
        ranking,
        question,
        error,
        loading,
        fetchAllRanking,
        fetchDailyRanking,
        
    };
}
