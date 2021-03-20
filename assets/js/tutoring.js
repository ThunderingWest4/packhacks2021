let tutors = {};
let taken_times = [];

function loadTutors() {
    const fs = require('fs');

    let dirname = "assets\\tutorinfo\\"
    readFiles(dirname, function(filename, content) {
        let temp = JSON.parse(content);
        tutors[temp["name"].join(" ")] = temp;
      }, function(err) {
        throw err;
      });

    // we've read in the tutor data and stored it
}

function readFiles(dirname, onFileContent, onError) {
    fs.readdir(dirname, function(err, filenames) {
      if (err) {
        onError(err);
        return;
      }
      filenames.forEach(function(filename) {
        fs.readFile(dirname + filename, 'utf-8', function(err, content) {
          if (err) {
            onError(err);
            return;
          }
          onFileContent(filename, content);
        });
      });
    });
  }

function loadTimes(subject) {

    loadTutors();
    let times = [];
    for (var key in tutors) {
        let info = tutors[key];
        let validSubj = false;
        for (var x in info["subjects"]) {
            if(x.split("-")[0]===subject) {
                validSubj = true;
            }
        }
        // adding times
        if(validSubj) {
            for(var x in info["open-times"]) {
                if (!([key, x] in taken_times) && !(x in times)) {
                    // if time not taken
                    times.push(x)
                }
            }
        }
        // format it good
        if(times !== []) {

            let formattedTimes = [];
            for(var x in times) {
                formattedTimes.push(x.join(" to "));
            }
            document.getElementById(subject+"-tutortimes").innerText = formattedTimes.join("\n");

        } else {
            // no availible times
            document.getElementById(subject+"-tutortimes").innerText = "None. All times taken";
        }
    }

}