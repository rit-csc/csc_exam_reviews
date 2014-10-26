#!/bin/bash

if [ "$#" -ne 2 ]; then
	echo "Usage ./new-exam.sh <class name> <exam name>"
	exit 1
fi

month=`date +%m`
year=`date +%Y`

if [ "$year" -lt 6 ]; then
	$[ year-- ]
fi

if [ ! -d "$1" ]; then
	mkdir "$1"
	cp "template-makefile" "$1/Makefile"
fi
if [ ! -f "$1/CSC-$1-$2-$year-Review.tex" ]; then
	cp "template.tex" "$1/CSC-$1-$2-$year-Review.tex"
	cp "template-ANSWERS.tex" "$1/CSC-$1-$2-$year-Review-ANSWERS.tex"
fi
if [ ! -d "$1/questions" ]; then
	mkdir "$1/questions"
fi
echo "\\input{CSC-$1-$2-$year-Review.tex}" >> "$1/CSC-$1-$2-$year-Review-ANSWERS.tex"
