import { ref } from 'vue';

export function useCompLevel() {
    const useLevel = ref<any[]>([]);
    const question = ref<any>(null);
    const error = ref<null | Error>(null);

    const fetchLevel = async () => {
        // Aqui, deve haver a lógica do fetchLevel, se necessário
    };

    const getUserLevel = async (id: number) => {
        const myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");
    
        const raw = JSON.stringify({
            "userid": id
        });
    
        const requestOptions = {
            method: "POST",
            headers: myHeaders,
            body: raw,
            redirect: "follow"
        };
    
        try {
            const response = await fetch("https://api.challengedev.tech/api/v1/userlevel", requestOptions);
            
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
        useLevel,
        question,
        error,
        fetchLevel,
        getUserLevel
    };
}
