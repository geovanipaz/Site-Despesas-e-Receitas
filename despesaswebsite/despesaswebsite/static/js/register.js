const usernameField = document.querySelector("#usernameField");
const feedBackArea = document.querySelector(".invalid_feedback");
const emailField = document.querySelector("#emailField")
const  emailFeedBackArea = document.querySelector(".emailFeedBackArea")
const usernameSuccessOutput = document.querySelector('.usernameSuccessOutput')
const showPasswordToggle = document.querySelector('.showPasswordToggle')
const passwordField = document.querySelector('#passwordField')
const submitBtn = document.querySelector(".submit-btn")

handleToggleInput = (e) =>{
    if(showPasswordToggle.textContent === "MOSTRAR"){
        showPasswordToggle.textContent = "ESCONDER"
        passwordField.setAttribute("type", "text");
    }else{
        showPasswordToggle.textContent = "MOSTRAR"
        passwordField.setAttribute("type", "password");
    }
};

showPasswordToggle.addEventListener("click", handleToggleInput);

emailField.addEventListener("keyup", (e) => {
    const emailVal = e.target.value;

    emailField.classList.remove("is-valid");
    emailFeedBackArea.style.display = "none"

    if(emailVal.length > 0){
        fetch("/autenticacao/validar-email", {
            body:JSON.stringify({email: emailVal}),
            method:"POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log("data", data);
            if (data.email_erro){
                //submitBtn.setAttribute("disabled","disabled");
                submitBtn.disabled = true;
                emailField.classList.add("is-valid");
                emailFeedBackArea.style.display = "block"
                emailFeedBackArea.innerHTML = `<p>${data.email_erro}</p>`
            }else{
                submitBtn.removeAttribute("disabled")
            }
        });
    }
})



//'keyup' ação de teclado
usernameField.addEventListener("keyup", (e) => {
    //console.log('7777', 8888);
    
    const usernameVal = e.target.value;

    usernameSuccessOutput.textContent=`Checking ${usernameVal}`

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
            usernameSuccessOutput.style.display="none";
            if (data.username_erro){
                usernameField.classList.add("is-valid");
                feedBackArea.style.display = "block"
                feedBackArea.innerHTML = `<p>${data.username_erro}</p>`;
                //submitBtn.add("disabled")
                submitBtn.disabled = true
            }else{
                submitBtn.removeAttribute("disabled")
            }
        });
    }
    
});