#!/bin/bash
file=$1
number_of_lines=0
while read -r line; do
	let "number_of_lines+=1"
	echo "$number_of_lines + $line"
done <$file
