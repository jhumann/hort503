egrep "\[Term\]|\[Typedef]|^id: \w+|^name: \w+*|^namespace: \w+*|^def: \w+*" goslim_plant.obo | head --lines=-40 | sed ':a;N;$!ba;s/\n//g'| sed 's/\[Term\]/\n/g' | sed 's/id://g' | sed 's/name:/\t/g' | sed 's/namespace:/\t/g'| sed 's/def:/\t/g' > goslim_plant_terms.txt
