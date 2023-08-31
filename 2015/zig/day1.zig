const std = @import("std");
const data = @embedFile("day1.txt");

pub fn part1() !void {
    //    var ch = std.mem.split(u8, data, "");
    //   while (ch.next()) |x| {
    //      std.debug.print("{s}", .{x});
    // }
    var floor: i16 = 0;
    for (data) |x| {
        if (x == '(') {
            floor += 1;
        } else if (x == ')') {
            floor -= 1;
        }
    }
    std.debug.print("{d}\n", .{floor});
}

pub fn part2() !void {
    //    var ch = std.mem.split(u8, data, "");
    //   while (ch.next()) |x| {
    //      std.debug.print("{s}", .{x});
    // }
    var floor: i16 = 0;
    var position: i16 = 0;
    for (data) |x| {
        position += 1;
        if (x == '(') {
            floor += 1;
        } else if (x == ')') {
            floor -= 1;
        }
        if (floor == -1) {
            break;
        }
    }
    std.debug.print("{d}\n", .{position});
}

pub fn main() !void {
    try part1();
    try part2();
}
