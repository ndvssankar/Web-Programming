// document.addEventListener("DOMContentLoaded", () => {
//     document.querySelector('#book_details').onclick = () => {
//         const request = new XMLHttpRequest();
//         const isbn = document.querySelector("#isbn_number").value;
//         request.open('POST', '/api/book/');
//         request.onload = () => {
//             const book_details = JSON.parse(request.responseText);
//             if (book_details.success) {
//                 const content = '<tr> <th scope="row">ISBN Number</th> <td> {{ book.isbn }}</td></tr>'
//                 document.querySelector("#book_details").innerHTML = content;
//             } else {
//                 document.querySelector("#book_details").innerHTML = "Invalid ISBN Number"
//             }
//         }
//         const data = data.append('isbn_number', isbn);
//         request.send(data);
//         return false;
//     }
// });

function get_book_details(isbn_number) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/api/book?isbn_number='+isbn_number);
    xhr.onload = function() {
        if (xhr.status === 200) {
            let s = JSON.parse(xhr.responseText);
            const content = '<tr> <td scope="row">ISBN Number</td><td>' + s.ISBN + '</td></tr>' +
                            '<tr> <td scope="row">Title</td><td>' + s.Title + '</td></tr>' +
                            '<tr> <td scope="row">Auhtor</td><td>' + s.Author + '</td></tr>' +
                            '<tr> <td scope="row">Year</td><td>' + s.Year + '</td></tr>'

            document.querySelector("#book_details").innerHTML = content;
        }
        else {
            document.querySelector("#book_details").innerHTML = "Invalid ISBN Number";
        }
    };
    xhr.send();
}