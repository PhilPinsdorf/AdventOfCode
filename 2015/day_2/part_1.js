const fs = require('fs')

fs.readFile(__dirname + '/input.txt', 'utf8', (err, data) =>{
    var total_wrapping = 0;

    data.split(/\r?\n/).forEach((data) => {
        var lwh = data.split('x');
        var l = lwh[0], w = lwh[1], h = lwh[2];
    
        var lw = l*w, wh = w*h, lh = l*h;
    
        var smallest = Math.min(...[lw, wh, lh])
        total_wrapping += 2*lw + 2*wh + 2*lh + smallest;
    })

    console.log(total_wrapping);
})