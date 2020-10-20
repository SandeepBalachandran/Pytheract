window.onload = main;

function getFileNameWithExt(event) {

    if (!event || !event.target || !event.target.files || event.target.files.length === 0) {
        return;
    }

    const name = event.target.files[0].name;
    console.log(event.target.files[0])
    // const lastDot = name.lastIndexOf('.');

    // const fileName = name.substring(0, lastDot);
    // const ext = name.substring(lastDot + 1);
    var placeholder = document.getElementById("filename");

    placeholder.innerHTML = "Filename : " + "<b>" + name + "</b>";
    submitbtn.style.display = "initial";
    // outputfile.value = fileName;
    // extension.value = ext;

}

function onFileSubmit() {
   console.log('ee')
    // uploaddiv.classList.add("width-50");
    // uploaddiv.classList.add("flt-lft");
    // resultdiv.style.display = "initial";

}
// var uploaddiv = document.getElementById('uploaddiv')
// var submitbtn = document.getElementById('submitbtn');
// var resultdiv = document.getElementById('resultdiv')
function main() {
    // resultdiv.style.display = "none";
    // submitbtn.style.display = "none";
    
}


