$(document).ready(function () {
    $("div[id='login1']").show();
    $("div[id='login2']").hide();
    $("div[id='postlink1']").show();
    $("div[id='postlink2']").hide();
});
// functions for changing login
function handleLogin(btn) {
    var login = btn.children().first().val();
    if (login == "login2"){
        $("div[id='login1']").hide();
        $("div[id='login2']").show();
    } else if (login == "login1"){
        $("div[id='login1']").show();
        $("div[id='login2']").hide();
    }
}
// function for changing post
function handleImport(btn) {
    var link = btn.children().first().val();
    if (link == "postLink1"){
        $("div[id='postlink1']").show();
        $("div[id='postlink2']").hide();
    } else if (link == "postLink2"){
        $("div[id='postlink1']").hide();
        $("div[id='postlink2']").show();
    }
}