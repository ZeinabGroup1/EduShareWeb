function valid() {
    $(".error").html('&nbsp;');
    var email = $('#email').val();
    var filter = /^[a-z0-9._-]+@[a-z]+.[a-z]{2,5}$/i;
    var password = $('#password').val();
    // var skills = $('#skills').val();
    // var name = $('#name').val();


    if(email == ""){
        $("#email-error").html("*Please enter valid email").css("color","red");
        $('#email').focus();
        return false;
    }else if(!filter.test(email)){
                $("#email-error").html("*Please enter valid email.");
                $("#email").focus();
                return false;
            }
    if(password == ""){
        $("#password-error").html("*Please enter valid password").css("color","red");
        $('#password').focus();
        return false;
    } else if (password.length < 6) {
        $("#password-error").html("*Password should be at least 6 characters long").css("color", "red");
        $('#password').focus();
        return false;
    }
}

// if(name == ""){
    // 	$("#name-error").html("*Please enter the name").css("color","red");
    // 	$('#name').focus();
    // 	return false;
    // }


