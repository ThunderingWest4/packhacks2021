let tutors = {};
let taken_times = [];

// function loadTutors() {
//     const fs = require('fs');

//     let dirname = "assets\tutorinfo"
//     readFiles(dirname, function(filename, content) {
//         let temp = JSON.parse(content);
//         tutors[temp["name"].join(" ")] = temp;
//       }, function(err) {
//         throw err;
//       });

//     // we've read in the tutor data and stored it
// }

// function readFiles(dirname, onFileContent, onError) {
//     fs.readdir(dirname, function(err, filenames) {
//       if (err) {
//         onError(err);
//         return;
//       }
//       filenames.forEach(function(filename) {
//         fs.readFile(dirname + filename, 'utf-8', function(err, content) {
//           if (err) {
//             onError(err);
//             return;
//           }
//           onFileContent(filename, content);
//         });
//       });
//     });
//   }

function loadTimes() {
    let innercontent;
    fetch("http://127.0.0.1:5000/api/v1/tutors/opentimes/math").then(function(response) {
        // return response.json();
        innercontent = response.join(", ");
    }).then(function(data) {
        // continue;
    }).catch(function() {
        innercontent = "Error fetching times";
    });
    document.getElementById("math-tutortimes").innerText = innercontent;

}