#!/bin/bash

if ! type "radon" > /dev/null; then
	echo "please make sure radon is installed before running this script."
	echo "see https://pypi.org/project/radon/"
	exit 1
fi

echo "radon is installed, proceeding with analysis"

dir="radon_results"
if ! [[ -d "$dir" ]]
then
	mkdir "$dir"
	echo "created $dir because it didn't exist"
fi


radon cc -a website/ > "$dir/cyclomatic_complexity.txt"
radon mi website/ > "$dir/maintainability_index.txt"
radon hal website/ > "$dir/halstead_complexity.txt"


