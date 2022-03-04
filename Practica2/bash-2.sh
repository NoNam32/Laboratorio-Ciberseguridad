#!/bin/bash

echo -n 'Dame un numero inicial: '
read inicio

echo -n 'Dame un numero final: '
read final

for (( i=$inicio; i<$final; i++ ))
do
    echo $i
done