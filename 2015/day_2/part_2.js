const fs = require('fs')

fs.readFile(__dirname + '/input.txt', 'utf8', (err, data) =>{
    var total_ribbon = 0;

    data.split(/\r?\n/).forEach((data) => {
        var lwh = data.split('x');
        var l = lwh[0], w = lwh[1], h = lwh[2];
    
        res = [l, w, h].sort((a,b) => a - b).slice(0, 2);
        total_ribbon += 2*res[0] + 2*res[1] + l*w*h;
    })

    console.log(total_ribbon);
})