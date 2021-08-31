function do_ajax() {
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


function handleChange(src) {
    
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
