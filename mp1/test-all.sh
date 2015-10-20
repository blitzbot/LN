#!/bin/bash

sh run.sh

# Testes
FILES=/tests/*
echo "Compiling tests..."
for f in tests/*.txt
do
    name=${f##*/}
    base=${name%.txt}
    #echo "compile ${base}"
    fstcompile --isymbols=data.sym --osymbols=data.sym  $f  > tests/${base}.fst
    fstcompose tests/${base}.fst transdutor.fst > tests/${base}_result.fst
    fstdraw --isymbols=data.sym --osymbols=data.sym  tests/${base}_result.fst | dot -Tpdf > tests/pdfs/${base}_result.pdf
    
done
echo "Finished!"
#mv tests/*.pdf tests/pdfs