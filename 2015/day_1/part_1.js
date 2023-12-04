const fs = require('fs')

fs.readFile(__dirname + '/input.txt', 'utf8' , (err, data) => {
    var count = 0;

    data.split('').forEach(char => {
        switch (char) {
            case '(':
                count++;
                break;
            case ')':
                count--;
                break;
        }
    })

    console.log(count);
})