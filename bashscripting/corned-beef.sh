#!/bin/bash

COMPAREHASH='70dad256878571774efef5fb41661ef1'
for NUM in {000..999}
do
FLAG="FS{cabbage-wait_that's_not_right_${NUM}}"
HASH=$(echo -n $FLAG | md5sum | cut -d ' ' -f 1 )
if [[ ${HASH} == ${COMPAREHASH} ]]
then
    echo ${FLAG}
fi
done
