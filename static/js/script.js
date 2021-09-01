var select = document.getElementById('select-cipher')

change_config_form(1)

select.addEventListener('change', () => {
    change_config_form(select.value)
});


function execute() {
    var request = new XMLHttpRequest();
    var result = document.getElementById('output-text-box');
    
    request.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200) {
            result.value = this.responseText;
        }
    }
    
    request.open('POST', '/update', true);
    request.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    request.send("name=" + document.getElementById('input-text-box').value);
}

function change_config_form(id) {
    var request = new XMLHttpRequest();
    var result = document.getElementById('app-setting-form-dynamic');

    request.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200) {
            result.innerHTML = this.responseText;
        }
    }

    request.open('POST', '/form', true);
    request.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    request.send("cipher_id=" + id);
}

function change_action(src) {
    
    if(src.id == "encrypt") {
        state = "encrypt";
        document.getElementById("left-tab").innerHTML = "Plaintext";
        document.getElementById("right-tab").innerHTML = "Ciphertext";
    } else {
        state = "decrypt"
        document.getElementById("right-tab").innerHTML = "Plaintext";
        document.getElementById("left-tab").innerHTML = "Ciphertext";
    }

    var request = new XMLHttpRequest();
    
    request.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200) {
            console.log(this.responseText);
        }
    }

    request.open('POST', '/action', true);
    request.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    request.send("state=" + src.id);

}

var upload = document.getElementById('input-file');

upload.addEventListener('change', () => {
    var filename =  upload.value.replaceAll("\\", " ").split(" ");
    document.getElementById('file-label').innerHTML = filename[filename.length-1]
    
    var file = document.getElementById('input-file').files[0];

    const reader = new FileReader();
    reader.onload = (e) => {
        document.getElementById('input-text-box').value = e.target.result;
    }
    reader.readAsText(file);
});

var input = document.getElementById('input-text-box');

input.addEventListener('input', () => {
    document.getElementById('file-label').innerHTML = "Choose Input File!";
})

function download(filename, textInput) {

    var element = document.createElement('a');
    element.setAttribute('href','data:text/plain;charset=utf-8,' + encodeURIComponent(textInput));
    element.setAttribute('download', filename);
    document.body.appendChild(element);
    element.click();

}

document.getElementById("download-button").addEventListener("click", () => {
    var text = document.getElementById("output-text-box").value;
    var filename = document.getElementById('file-label').innerHTML != "Choose Input File!" ? document.getElementById('file-label').innerHTML.split(".")[0] : "text";
    var fileextension = document.getElementById('file-label').innerHTML.split(".")[1] != undefined ? document.getElementById('file-label').innerHTML.split(".")[1] : "txt";
    var downloadname = new Date().toJSON().slice(0, 19).replaceAll("-", "").replaceAll(":", "").replaceAll("T", "_") + "_" + filename + (document.getElementById("right-tab").innerHTML == "Ciphertext" ? "_encrypted." : "_decrypted.") + fileextension;
    download(downloadname, text);
}, false);

function change_m_key(src) {

    var ele = document.getElementsByName("key-m-options");
    for(var i=0; i<ele.length; i++) {
        if(ele[i].id != src.id) {
            ele[i].classList.remove('active')
            ele[i].checked = false;
            ele[i].active = false;
        }
    }

    var div = document.getElementsByClassName("cipher-key-radio");
    for(var i=0; i<div.length; i++) {
        div[i].classList.remove('active')
    }

    document.getElementById(src.id).checked = true
    document.getElementById(src.id).active = true

    console.log("====> " + src.id)
}
