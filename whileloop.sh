#!/bin/bash

echo -n "Input 1, 2, 3, or 4 For next step:"

valid=0

while
[ $valid == 0 ]
do
	read ans case
	case $ans in
	1	) 	echo "You are number 1"
			valid=1
			;;
	2	)	echo "You are number 2"
			valid=1
			;;
	3	)	echo "You are number 3"
			valid=1
			;;
	4	)	echo "You are number 4"
			valid=1
			;;
	*	)	echo Please Enter 1, 2, 3, 4;;
	esac
done
