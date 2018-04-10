#!/bin/bash

exec 10<&0

exec < $1
in=$1

echo "Expected lines : `wc -l $in`"

file = "./cuu_textfile.txt"

let count=0

while read LINE
do
   echo $LINE
   ((count++))
   echo $LINE >> $file
   if  [ $? -ne 0 ]
    then echo "Error in writing to file ${file}; check its permission!"
    exit 1
   fi
done

echo No of Lines: $count" 
exec 0<&10 10<&-
