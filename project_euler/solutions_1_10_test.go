package project_euler

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func Test_solve_problem_1(t *testing.T) {
	tests := []struct {
		input  int
		output int
	}{
		{
			input:  10,
			output: 23,
		},
		{
			input:  1000,
			output: 233168,
		},
	}
	for _, tt := range tests {
		got := SolveProblem_1(tt.input)
		assert.Equal(t, got, tt.output)
	}
}

func Test_problem_2(t *testing.T) {
	tests := []struct {
		input  int
		output int
	}{
		{
			input:  35,
			output: 44,
		},
		{
			input:  4000000,
			output: 4613732,
		},
	}
	for _, tt := range tests {
		got, err := SolveProblem_2(tt.input)
		if err != nil {
			t.Errorf("Something broke.  Badly. [%+v]", err)
		}
		assert.Equal(t, got, tt.output)
	}
}
