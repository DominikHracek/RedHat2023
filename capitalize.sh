#!/bin/bash
echo "Your sentence: "
read sentence
for word in $sentence; do
	capitalized_word="${word^}"
	capitalized_sentence+=" $capitalized_word"
done
echo $capitalized_sentence

