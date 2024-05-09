package main

import (
	"context"
)

type NucleiScanner struct{}

func (n *NucleiScanner) RunNuclei(ctx context.Context, target string, options ...string) (string, error) {
	return dag.
		Container().
		From("nuclei/nuclei:latest").
		WithExec(append([]string{"nuclei"}, append(options, target)...)). 
		Stdout(ctx) 
}
