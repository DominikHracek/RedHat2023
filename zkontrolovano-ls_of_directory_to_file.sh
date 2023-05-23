#!/bin/bash
FILE=files.txt
if [ -f "$FILE" ]; then
	rm files.txt
fi
for file in *; do
	if [[ -f "$file" ]]; then
		echo "$file" >> files.txt
	fi
done
