.PHONY: all clean

all: global_var compound_assignment_ops

global_var:
	python benchmarks/global_var.py

compound_assignment_ops:
	python benchmarks/compound_assignment_ops.py

clean: