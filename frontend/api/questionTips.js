

export async function createQuestion(title, subtitle, example, type_question, question, id_language, xp_reward, response, created_at, dificuldade) {
    try {
        const myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");

        const requestOptions = {
            method: 'POST',
            headers: myHeaders,
            redirect: 'follow',
            body: JSON.stringify({
                "title": title,
                "subtitle": subtitle,
                "example": example,
                "type_question": type_question,
                "question": question,
                "id_language": id_language,
                "xp_reward": xp_reward,
                "response": response,
                "created_at": created_at || new Date().toISOString(),
                "dificulty": dificuldade // Define created_at para a data atual se não for fornecido
            })
        };

        const fetchResponse = await fetch(`http://localhost:5000/api/v1/createquestion`, requestOptions);
        const qResponse = await fetchResponse.json();

        if (qResponse.message === "Question created") {
            return qResponse.message;
        } else {
            return qResponse;
        }

    } catch (error) {
        console.log('Erro de rede:', error);
        throw error;
    }
}

export async function updateQuestion(id, title, subtitle, example, type_question, question, id_language, xp_reward, response, created_at, dificuldade) {
    try {
        const myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");

        const requestOptions = {
            method: 'PUT',
            headers: myHeaders,
            redirect: 'follow',
            body: JSON.stringify({
                "id": id,
                "title": title,
                "subtitle": subtitle,
                "example": example,
                "type_question": type_question,
                "question": question,
                "id_language": id_language,
                "xp_reward": xp_reward,
                "response": response,
                "created_at": created_at || new Date().toISOString(),
                "dificulty": dificuldade // Define created_at para a data atual se não for fornecido
            })
        };

        const fetchResponse = await fetch(`http://localhost:5000/api/v1/updatequestion`, requestOptions);
        const qResponse = await fetchResponse.json();

        if (qResponse.message === "Question created") {
            return qResponse.message;
        } else {
            return qResponse;
        }

    } catch (error) {
        console.log('Erro de rede:', error);
        throw error;
    }
}

//Deletar uma pergunta
export async function deleteQuestion(id) {
    try {
        const myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");

        const requestOptions = {
            method: 'DELETE',
            headers: myHeaders,
            redirect: 'follow',
            body: JSON.stringify({
                "id": id
            })
        };

        const fetchResponse = await fetch(`http://localhost:5000/api/v1/deletequestion`, requestOptions);
        const qResponse = await fetchResponse.json();

        if (qResponse.message === "Question deleted") {
            return qResponse.message;
        } else {
            return qResponse;
        }

    } catch (error) {
        console.log('Erro de rede:', error);
        throw error;
    }
}

export async function getResponses(){
    try {
        const myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");

        const requestOptions = {
            method: 'GET',
            headers: myHeaders,
            redirect: 'follow'
        };

        const response = await fetch(`http://localhost:5000/api/v1/responses`, requestOptions);
        const result = await response.json(); // Converte a resposta para JSON
        return result;

    } catch (error) {
        console.log('Erro de rede:', error);
        throw error;
    }
}







