import {Loading} from '../api/statGlobal'


export async function verifyCode(type_question, question_id, question_response, language) {
  const myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");
  
  const raw = JSON.stringify({
      "type_question": type_question,
      "question_id": question_id,
      "questionresponse": question_response,
      "language": language
  });
  
  const requestOptions = {
      method: "POST",
      headers: myHeaders,
      body: raw,
      redirect: "follow"
  };
  Loading.value = true
  try {
      const response = await fetch("https://api.challengedev.tech/api/v1/verify", requestOptions);
      if (response.headers.get("content-type")?.includes("application/json")) {
          const result = await response.json();
          Loading.value = false
          return result;  // Retorne o resultado para a função chamadora
      } else {
            Loading.value = false
          throw new Error("Resposta não é JSON");
      }
  } catch (error) {
      console.error("Erro:", error);
      Loading.value = false
      throw error;  // Lance o erro para que a função chamadora possa tratá-lo
  }
}


export async function submitCode(type_question, question_id, question_response, language, user_id) {
  const myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");
  
  const raw = JSON.stringify({
      "type_question": type_question,
      "question_id": question_id,
      "questionresponse": question_response,
      "language": language,
      "user_id": user_id
  });
  
  const requestOptions = {
      method: "POST",
      headers: myHeaders,
      body: raw,
      redirect: "follow"
  };
  Loading.value = true
  try {
      const response = await fetch("https://api.challengedev.tech/api/v1/submit", requestOptions);
      if (response.headers.get("content-type")?.includes("application/json")) {
          const result = await response.json();
          Loading.value = false
          return result;  // Retorne o resultado para a função chamadora
      } else {
            Loading.value = false
          throw new Error("Resposta não é JSON");
      }
  } catch (error) {
    Loading.value = false
      console.error("Erro:", error);
      throw error;  // Lance o erro para que a função chamadora possa tratá-lo
  }
}
