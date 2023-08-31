import { readFileSync } from "fs";

const file: Buffer = readFileSync("../inputs/day1.txt")
const data = file.toString();

let floor: number = 0;
let position: number = 0;
data.split('').forEach((item) => {
    position += 1;
    if (item === '(') {
        floor += 1;
    } else if (item === ')') {
        floor -= 1;
    }
    if (floor === -1) {
        console.log(position);
        return
    }
})
console.log(floor);
