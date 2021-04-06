package project_euler

import "errors"

func SolveProblem_1(max int) int {
	sum := 0
	for i := 1; i < max; i++ {
		if i%3 == 0 || i%5 == 0 {
			sum += i
		}
	}
	return sum
}

func SolveProblem_2(max int) (int, error) {
	if max > 0 && max < 3 {
		return 2, nil
	}
	num1 := make(chan int, 2)
	num2 := make(chan int, 2)
	a, b, c := 1, 2, 0
	num1 <- a
	num2 <- b
	sum := 2
	for b < max {
		a = <-num1
		b = <-num2
		c = a + b
		if c >= max {
			return sum, nil
		}
		if c%2 == 0 {
			sum += c
		}
		num1 <- b
		num2 <- c
	}
	return -1, errors.New("Something went really wrong")
}
