package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	//open file
	dat, err := ioutil.ReadFile("dayOne.txt")
	if err != nil {

	}
	//split by newline, put into an array
	lines := strings.Split(string(dat), "\n")
	// for ind, i := range lines {
	// 	fmt.Println(ind, i)
	// }
	//find the entries that sum to 2020
	for ind, i := range lines {
		for indJ, j := range lines[ind:] {
			for _, k := range lines[indJ:] {
				valueI, err := strconv.Atoi(i)
				if err != nil {

				}

				valueJ, err := strconv.Atoi(j)
				if err != nil {

				}
				valueK, err := strconv.Atoi(k)
				if err != nil {

				}

				if valueI+valueJ+valueK == 2020 {
					fmt.Println(valueI * valueJ * valueK)
				}

			}

		}
	}
}
