function do_ajax() {
    var request = new XMLHttpRequest();
    var result = document.getElementById('output-text-box');
    
    request.onreadystatechange = function(){
        if(this.readyState == 4 && this.status == 200) {
            result.value = this.responseText;
        }
        console.log("EXIT" + this.responseText)
    }

    request.open('POST', '/update', true);
    request.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    console.log(document.getElementById('input-text-box').value);
    request.send("name=" + document.getElementById('input-text-box').value);
}