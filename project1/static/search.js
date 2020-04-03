function search_books() {
    var xhr = new XMLHttpRequest();
    var search_query = document.getElementById("txtSearch").value;
    // alert("text is :" + value);
    // xhr.open('GET', '/api/search?type='+search_query);
    var theUrl = "/api/search"
    xhr.open("POST", theUrl);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({ "type": search_query}));
    xhr.onload = function() {
        if (xhr.status === 200) {
            let s = JSON.parse(xhr.responseText);
            let json_array = s["books"];
            var content = "";
            for (x in json_array) {
                content += '<tr> <th scope="row"> <a id="#book_details" href="#" onclick=get_book_details("'+ json_array[x]["isbn"] + '")>' + json_array[x]["title"] +'</a> </th> </tr>';
            }
            document.querySelector("#search_books").innerHTML = content;
        } else {
            document.querySelector("#search_books").innerHTML = "Invalid ISBN Number";
        }
    };
    // xhr.send();
}