import { ref } from 'vue';

export default function useQuestions() {
    const questions = ref<any[]>([]);
    const question = ref<any>(null);
    const error = ref<null | Error>(null);
    const loading = ref(false);
    const fetchAllQuestions = async () => {
        loading.value = true;
        try {
            const response = await fetch("http://127.0.0.1:5000/api/v1/getallquestions", {
                method: 'GET',
                headers: {
                    "Content-Type": "application/json",
                },
                redirect: 'follow'
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const result = await response.json(); // Converte a resposta para JSON
            questions.value = result;
        } catch (err) {
            error.value = err as Error;
            console.error('Erro ao fazer a requisição:', err);
        } finally {
            loading.value = false;
        }
    };

    const getOneQuestion = async (id: number) => {
        loading.value = true;
        const myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");
    
        const raw = JSON.stringify({
            "id": id
        });
    
        const requestOptions = {
            method: "POST",
            headers: myHeaders,
            body: raw,
            redirect: "follow"
        };
    
        try {
            const response = await fetch("http://127.0.0.1:5000/api/v1/getonequestion", requestOptions);
            
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
    
            const result = await response.json();
            return result;
        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
            throw error; // Re-throw the error if you want the caller to handle it
        }
    };

    return {
        questions,
        question,
        error,
        loading,
        fetchAllQuestions,
        getOneQuestion,
        
    };
}

