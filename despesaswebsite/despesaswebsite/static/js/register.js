const usernameField = document.querySelector("#usernameField");
const feedBackArea = document.querySelector(".invalid_feedback");
//'keyup' ação de teclado
usernameField.addEventListener("keyup", (e) => {
    console.log('7777', 8888);

    const usernameVal = e.target.value;

    usernameField.classList.remove("is-valid");
    feedBackArea.style.display = "none"

    if(usernameVal.length > 0){
        fetch("/autenticacao/validar-username", {
            body:JSON.stringify({username: usernameVal}),
            method:"POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log("data", data);
            if (data.username_erro){
                usernameField.classList.add("is-valid");
                feedBackArea.style.display = "block"
                feedBackArea.innerHTML = `<p>${data.username_erro}</p>`
            }
        });
    }
    
});