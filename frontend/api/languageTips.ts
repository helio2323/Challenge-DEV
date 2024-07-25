export async function getLanguages(languageName?: string, languageId?: number) {
    try {
        const myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");

        const requestOptions = {
            method: 'GET',
            headers: myHeaders,
            redirect: 'follow'
        };

        // Faz a chamada para a API para obter a lista de linguagens
        const response = await fetch(`http://localhost:5000/api/v1/languages`, requestOptions);
        if (!response.ok) {
            // Se a resposta não for ok, lança um erro
            throw new Error('Network response was not ok');
        }

        const result = await response.json(); // Converte a resposta para JSON

        // Função auxiliar para encontrar a linguagem pelo nome ou ID
        const findLanguage = (lang: { language: string; id: number }) => {
            if (languageName && lang.language === languageName) {
                return true;
            }
            if (languageId && lang.id === languageId) {
                return true;
            }
            return false;
        };

        // Encontra a linguagem pelo nome ou ID e retorna o objeto completo
        const language = result.find(findLanguage);

        // Retorna o objeto da linguagem se encontrado, caso contrário retorna um objeto padrão
        return language ? { name: language.language, id: language.id } : { name: null, id: null };

    } catch (error) {
        console.log('Erro de rede:', error);
        throw error;
    }
}
