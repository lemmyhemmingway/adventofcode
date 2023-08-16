package main

import (
	"fmt"
	"io/ioutil"
)


func main()  {
    part1()
    part2()
}

func part1() {
    data, err := ioutil.ReadFile("inputs/day1.txt")
    if err != nil {
        fmt.Printf("%v", err)
    }
    floor := 0
    for _, ch := range string(data) {
        if ch == '(' {
            floor += 1
        }
        if ch == ')' {
            floor -= 1
        }
        
    }
    fmt.Printf("%d\n", floor)

}
func part2() {
    data, err := ioutil.ReadFile("inputs/day1.txt")
    if err != nil {
        fmt.Printf("%v", err)
    }
    floor := 0
    position := 0
    for _, ch := range string(data) {
        position += 1
        if ch == '(' {
            floor += 1
        }
        if ch == ')' {
            floor -= 1
        }

        if floor == -1 {
            fmt.Printf("%d\n", position)
            break
        }

    }
}
