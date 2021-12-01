const fs = require('fs')

// Open Filereader
fs.readFile(__dirname + '/input.txt', 'utf8', (err, data) =>{
    var total_wrapping = 0;
    var total_ribbon = 0;

    data.split(/\r?\n/).forEach((data) => {
        // Look for Errors
        if (err) {
          console.error(err)
          return
        }
    
        var lwh = data.split('x');
        var l = lwh[0];
        var w = lwh[1];
        var h = lwh[2];
    
        var lw = l*w;
        var wh = w*h;
        var lh = l*h;
    
        var smallest = Math.min(...[lw, wh, lh])
        total_wrapping += 2*lw + 2*wh + 2*lh + smallest;


        res = [l, w, h].sort((a,b) => a - b).slice(0, 2);
        total_ribbon += 2*res[0] + 2*res[1] + l*w*h;
    })

    console.log('Wrapping Paper: ' + total_wrapping);
    console.log('Ribbon: ' + total_ribbon);
})

// My Result => 232