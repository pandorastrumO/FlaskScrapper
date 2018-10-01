$(document).ready(function () {
    $("div[id='postLink1']").show();
    $("div[id='postLink2']").hide();
});
// function for changing post
function handleImport(btn) {
    var link = btn.children().first().val();
    if (link == "postLink1"){
        $("div[id='postLink1']").show();
        $("div[id='postLink2']").hide();
    } else if (link == "postLink2"){
        $("div[id='postLink1']").hide();
        $("div[id='postLink2']").show();
    }
}