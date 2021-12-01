const fs = require('fs')

// Open Filereader
fs.readFile(__dirname + '/input.txt', 'utf8' , (err, data) => {
    // Look for Errors
    if (err) {
      console.error(err)
      return
    }

    // Counting Var
    var count = 0;
    var position = 1;
    var found_basement = false;

    //For Each Char
    data.split('').forEach(char => {
        // '(' => +1
        // ')' => -1
        switch (char) {
            case '(':
                count++;
                break;
            case ')':
                count--;
                break;
        }

        if(!found_basement){
            if(count === -1){
                found_basement = true;
            } else {
                position++;
            }
        }
    })

    // Print Result
    console.log('Final Floor: ' + count);
    console.log('First Basement: ' + position)
})

// My Result => 232