"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs_1 = require("fs");
var file = (0, fs_1.readFileSync)("../inputs/day1.txt");
var data = file.toString();
var floor = 0;
var position = 0;
data.split('').forEach(function (item) {
    position += 1;
    if (item === '(') {
        floor += 1;
    }
    else if (item === ')') {
        floor -= 1;
    }
    if (floor === -1) {
        console.log(position);
        return;
    }
});
console.log(floor);
