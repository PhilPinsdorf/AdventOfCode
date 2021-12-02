const fs = require('fs')

fs.readFile(__dirname + '/input.txt', 'utf8' , (err, data) => {
    var count = 0;
    var position = 1;

    data.split('').some(char => {
        switch (char) {
            case '(':
                count++;
                break;
            case ')':
                count--;
                break;
        }

        if(count === -1) return true;

        position++;
    })
    
    console.log(position)
})