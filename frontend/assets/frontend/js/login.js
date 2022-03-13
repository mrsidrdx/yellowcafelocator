const usernameInput = document.getElementById("id_username");
const passwordInput = document.getElementById("id_password");
const btn = document.getElementById("id_submit");

btn.addEventListener("click", (event) => {
    event.preventDefault();
    const username = usernameInput.value;
    const password = passwordInput.value;
    let query = { username: username, password: password };
    console.log(query);
    let apiUrl = '/api/login/';
    axios.post(apiUrl, query).then(
        (response) => {
            var result = response.data;
            console.log(result);
            localStorage.setItem("yellow-cafe-token", result["token"]);
            let errorMsg = document.getElementById("id_error_msg");
            errorMsg.textContent = '';
            window.location.href = '/home'; // Redirect to the home page
        },
        (error) => {
            console.log(error);
            let errorMsg = document.getElementById("id_error_msg");
            errorMsg.textContent = 'Invalid username or password';
        }
    );
});
