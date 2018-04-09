#!/bin/bash

SRAs=$(cat SRA_IDs.txt)

## this works, but is an endless loop
# until [ for var in $SRAs -d ]
#  do
#    mkdir $SRAs
# done

## Not an endless loop, but runs several times (the number of SRR ids).
# for var in $SRAs [ -d ]
#   do
#     mkdir $SRAs
#   done

# this works, but doesn't use the test conditionals.  Thanks Dr. Google:-)
for sra in ${SRAs[*]}
do
  mkdir -p $sra
done
