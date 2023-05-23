#!/bin/bash
function vypocet_faktorialu() {
    vysledek=1
    for ((i=1 ; i<=$1 ; i++)); do
        vysledek=$((vysledek * i))
    done
}
number=$1
if ! [ $1 -eq $1 ] 2> /dev/null; then
	echo "Sorry integers only"
	exit
fi
if [ -z "$1" ]; then
	echo "Please provide me a integer, not empty string"
	exit
fi
if ! [ $1 -gt 1 ] | [ $1 -lt 21 ]; then
        echo "Please input a number greater than 0 and smaller than 21"
        exit
fi

vysledek=$(vypocet_faktorialu $number)
if vypocet_faktorialu $number; then
	echo "Faktorial of the number $number is: $vysledek"
fi
