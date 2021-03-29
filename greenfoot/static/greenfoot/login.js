document.addEventListener('DOMContentLoaded', function() {
    // toggle between register and login view
    document.querySelector('#register').addEventListener('click', () => register_view());
    document.querySelector('#login').addEventListener('click', () => login_view());

    
    // if there is a backend error show the proper page
    if (document.getElementById("rerror").innerHTML != "") {
        document.querySelector('#register-view').style.display = 'grid';
        document.querySelector('#login-view').style.display = 'none';
    } else {
        document.querySelector('#register-view').style.display = 'none';
        document.querySelector('#login-view').style.display = 'grid';
    }
})


function register_view() {
    document.querySelector('#register-view').style.display = 'grid';
    document.querySelector('#login-view').style.display = 'none';
    document.getElementById("lerror").innerHTML = ""
}


function login_view() {
    document.querySelector('#register-view').style.display = 'none';
    document.querySelector('#login-view').style.display = 'grid';
    document.getElementById("rerror").innerHTML = ""
}


function register(e) {
    e.preventDefault();

    // check if passwords are the same
    var password = document.getElementById("rp").value;
    var passwordConfirm = document.getElementById("rpc").value;

    if (password != passwordConfirm) {
        alert("Passwords do not match");
        return
    } else {
        document.getElementById('rf').submit();
    }
}   