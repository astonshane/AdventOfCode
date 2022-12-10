package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"regexp"
	"strconv"
	"strings"
)

type Pos struct {
	x   int
	y   int
	dir int
}

func part1(file string) {
	fmt.Println("Part1:")
	pos := Pos{0, 0, 0}

	r, _ := regexp.Compile("(R|L)(\\d+)")

	for _, cmd := range strings.Split(file, ", ") {
		reg := r.FindStringSubmatch(cmd)
		turn := reg[1]
		dist, _ := strconv.Atoi(reg[2])

		if turn == "R" {
			pos.dir += 1
		} else {
			pos.dir -= 1
		}

		pos.dir = (pos.dir) % 4
		if pos.dir < 0 {
			pos.dir += 4
		}

		mod := 0
		if pos.dir < 2 {
			mod = 1
		} else {
			mod = -1
		}

		if pos.dir%2 == 0 {
			pos.y += mod * dist
		} else {
			pos.x += mod * dist
		}
	}
	fmt.Println("Final Location: ", pos)
	fmt.Println("Blocks: ", math.Abs(float64(pos.x))+math.Abs(float64(pos.y)))
}

func part2(file string) {
	fmt.Println("Part2:")
	visited := make(map[string]bool)
	visited["(0,0)"] = true

	pos := Pos{0, 0, 0}

	r, _ := regexp.Compile("(R|L)(\\d+)")

	for _, cmd := range strings.Split(file, ", ") {
		reg := r.FindStringSubmatch(cmd)
		turn := reg[1]
		dist, _ := strconv.Atoi(reg[2])

		if turn == "R" {
			pos.dir += 1
		} else {
			pos.dir -= 1
		}

		pos.dir = (pos.dir) % 4
		if pos.dir < 0 {
			pos.dir += 4
		}

		mod := 0
		if pos.dir < 2 {
			mod = 1
		} else {
			mod = -1
		}

		done := false
		visits := travel(pos, dist, mod)
		fmt.Println("############")
		fmt.Println("current: ", pos)
		fmt.Println("visited: ", visited)
		fmt.Println("visits: ", visits)
		fmt.Println("############")
		for _, v := range visits {
			if visited[v] {
				fmt.Printf("Visited %s twice!\n", v)
				done = true
				break
			} else {
				visited[v] = true
			}
		}
		if done {
			break
		}
		pos = NewPos(pos, dist, mod)
	}

}

func travel(pos Pos, dist, mod int) (visited []string) {
	newPos := NewPos(pos, dist, mod)

	if pos.dir%2 == 0 {
		for i := pos.y + mod; i < newPos.y+mod; i += mod {
			pos.y = i
			visited = append(visited, fmt.Sprintf("(%d,%d)", pos.x, pos.y))
		}
	} else {
		for i := pos.x + mod; i < newPos.x+mod; i += mod {
			pos.x = i
			visited = append(visited, fmt.Sprintf("(%d,%d)", pos.x, pos.y))
		}
	}

	return visited
}

func NewPos(pos Pos, dist, mod int) Pos {
	newPos := Pos{pos.x, pos.y, pos.dir}
	if pos.dir%2 == 0 {
		newPos.y += mod * dist
	} else {
		newPos.x += mod * dist
	}
	return newPos
}

func main() {
	dat, _ := ioutil.ReadFile("input.txt")
	file := string(dat)

	part1(file)
	part2(file)
}
