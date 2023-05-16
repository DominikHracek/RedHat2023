#!/bin/bash
function vypocet_faktorialu() {
    vysledek=1
    for ((i=1; i<=$1; i++)); do
        vysledek=$((vysledek * i))
    done
}
number=$1
vysledek=$(vypocet_faktorialu $number)
if vypocet_faktorialu $number; then
	echo $vysledek
else
	echo "1"
fi
