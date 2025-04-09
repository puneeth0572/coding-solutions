Problem 3: Alternate Series
Language: JavaScript
Generate Alternate numbers series based on input a

const a = parseInt(process.argv[2])

let series = [];
for(let i = 1; i <= a; i += 2){
    series.push(i);
}
console.log("Output:", series.join(', '));
