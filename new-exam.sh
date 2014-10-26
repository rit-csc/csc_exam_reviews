#!/bin/bash

if [ "$#" -ne 2 ]; then
	echo "Usage ./new-exam.sh <class name> <exam name>"
	exit 1
fi

if [ -d "$1" ]; then
	echo "Directory $1 already exists. Exiting..."
	exit 1
fi

month=`date +%m`
year=`date +%Y`

if [ "$year" -lt 6 ]; then
	$[ year-- ]
fi

mkdir "$1"
cp "template.tex" "$1/CSC-$1-$2-$year-Review.tex"
cp "template-ANSWERS.tex" "$1/CSC-$1-$2-$year-Review-ANSWERS.tex"
mkdir "$1/questions"
cp "template-makefile" "$1/Makefile"
echo "\\input{CSC-$1-$2-$year-Review.tex}" >> "$1/CSC-$1-$2-$year-Review-ANSWERS.tex"
