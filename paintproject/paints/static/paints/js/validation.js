/*const email = document.getElementById("mail");
email.addEventListener("input", function (event) {
  if (email.validity.typeMismatch) {
    email.setCustomValidity("u forgot @ in it");
  } else if(email.valueMissing){
    email.setCustomValidity("u forgot . in it");
  }
  else{
    email.setCustomValidity("");
  }
});


    document.getElementsByTagName("form")[0].onsubmit = function() {
        if (document.getElementsByName("password")[0].value == document.getElementsByName("psw-repeat")[0].value)
         { return true; } else { alert("Ошибка! Пароли не совпадают."); return false; }
    };

const togglePassword = document.getElementById('togglePassword');

const showOrHidePassword = () => {
  const password = document.getElementById('password');
  if (password.type === 'password') {
    password.type = 'text';
  } else {
    password.type = 'password';
  }
};

togglePassword.addEventListener('change', showOrHidePassword);

const togglePassword1 = document.getElementById('togglePassword1');

const showOrHidePassword1 = () => {
  const password = document.getElementById('psw-input');
  if (password.type === 'password') {
    password.type = 'text';
  } else {
    password.type = 'password';
  }
};

togglePassword1.addEventListener('change', showOrHidePassword1);

function openForm() {
    document.getElementById("myForm").style.display = "block";
}

function closeForm() {
    document.getElementById("myForm").style.display = "none";
}*/

const name = document.forms["login_form"]["name"];
const password = document.forms["login_form"]["password"];

//Password validation
password.addEventListener("input", function (event) {
  let password_reg = /^[A-Za-z\d]+$/;

  if(!password_reg.test(password.value)) {
    password.setCustomValidity("Используются только латинские буквы и цифры!");
  } else {
    password.setCustomValidity("");
  }
});

