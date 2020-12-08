package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	dat, err := ioutil.ReadFile("dayTwo.txt")
	if err != nil {

	}
	validCount := 0
	//split by newline, put into an array
	lines := strings.Split(string(dat), "\n")
	for _, i := range lines {
		if evaluateRulePartTwo(i) {
			validCount++
		}
	}
	fmt.Println(validCount)
}

func evaluateRule(input string) bool {
	//first, split to the password and the rule

	if input != "" {
		spl := strings.Split(string(input), ": ")
		rule := spl[0]
		pass := spl[1]
		//parse the rule
		//first, split by space to get the letter and the counts
		spl = strings.Split(rule, " ")
		valuePair := strings.Split(spl[0], "-")
		letter := spl[1]
		charCount := strings.Count(pass, letter)
		paramOne, err := strconv.Atoi(valuePair[1])
		if err != nil {

		}
		paramZero, err := strconv.Atoi(valuePair[0])
		if err != nil {

		}
		if charCount <= paramOne && charCount >= paramZero {
			// fmt.Println(rule, pass)
			return true
		}

	}
	return false
}

func evaluateRulePartTwo(input string) bool {
	//first, split to the password and the rule

	if input != "" {
		spl := strings.Split(string(input), ": ")
		rule := spl[0]
		pass := spl[1]
		//parse the rule
		//first, split by space to get the letter and the counts
		spl = strings.Split(rule, " ")
		valuePair := strings.Split(spl[0], "-")
		letter := spl[1]

		// charCount := strings.Count(pass, letter)
		paramOne, err := strconv.Atoi(valuePair[1])
		if err != nil {

		}
		paramZero, err := strconv.Atoi(valuePair[0])
		if err != nil {

		}
		if (string(pass[paramZero-1]) == letter && string(pass[paramOne-1]) != letter) || (string(pass[paramZero-1]) != letter && string(pass[paramOne-1]) == letter) {
			// fmt.Println(rule, pass)
			return true
		}

	}
	return false
}
