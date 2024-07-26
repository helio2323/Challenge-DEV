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
  
  try {
      const response = await fetch("http://127.0.0.1:5000/api/v1/verify", requestOptions);
      if (response.headers.get("content-type")?.includes("application/json")) {
          const result = await response.json();
          return result;  // Retorne o resultado para a função chamadora
      } else {
          throw new Error("Resposta não é JSON");
      }
  } catch (error) {
      console.error("Erro:", error);
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
  
  try {
      const response = await fetch("http://127.0.0.1:5000/api/v1/submit", requestOptions);
      if (response.headers.get("content-type")?.includes("application/json")) {
          const result = await response.json();
          return result;  // Retorne o resultado para a função chamadora
      } else {
          throw new Error("Resposta não é JSON");
      }
  } catch (error) {
      console.error("Erro:", error);
      throw error;  // Lance o erro para que a função chamadora possa tratá-lo
  }
}
