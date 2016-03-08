#!/usr/bin/env bash 

filename=$2
while read -r recipient
do
	mail -s $1 $recipient < $3
done < $filename

echo "Send Mail Completed..."

#mail -s $1 $2 < $3
