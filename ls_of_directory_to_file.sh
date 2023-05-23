#!/bin/bash
rm files.txt
for file in *; do
	if [[ -f "$file" ]]; then
		echo "$file" >> files.txt
	fi
done
