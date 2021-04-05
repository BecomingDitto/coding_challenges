package project_euler

import (
	"testing"
	"github.com/stretchr/testify/assert"
  )

func Test_solve(t *testing.T) {
	tests := []struct{
		input  int
		output int
	}{
		{
			input: 10,
			output: 23,
		},
		{
			input: 1000,
			output: 233168,
		},
	}
	for _, tt := range tests {
		got := solve(tt.input)
		assert.Equal(t, got, tt.output)
	}
}
