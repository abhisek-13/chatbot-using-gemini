// To submit the prompt in the webpage
function submitPrompt(){

    const prompt = document.querySelector(".prompt").value;
    
    fetch('/result',{
        method: "POST",
        headers:{"Content-Type": "application/json"},
        body: JSON.stringify({"prompt":prompt})})
        .then(Response => Response.json())
        .then(data => {document.querySelector(".answer").value = data.response;})

}

// To clear the textarea
function clearPrompt(){
    document.querySelector(".answer").value = "";
    document.querySelector(".prompt").value = "";
}