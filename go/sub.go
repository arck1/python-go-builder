package main

import "C"

func main(){}

//export summator
func summator(x int, y int) int {
	return x + y
}