#!/bin/bash
if [ -z "$1" ]; then
	echo "Please provide me a file name as string"
	exit
fi
file=$1
if [ -f "$file"]; then
	number_of_lines=0
	while read -r line; do
		let "number_of_lines+=1"
		echo "$number_of_lines + $line"
	done <$file
else
	echo "Please provide me a file"
fi
