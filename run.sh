#!/bin/bash

sh clean.sh

fstcompile --isymbols=data.sym --osymbols=data.sym  transdutor.txt  > transdutor.fst
fstdraw  --isymbols=data.sym --osymbols=data.sym  transdutor.fst | dot -Tpdf > transdutor.pdf

# Invert
fstinvert transdutor.fst > invertTransdutor.fst
fstdraw  --isymbols=data.sym --osymbols=data.sym  invertTransdutor.fst | dot -Tpdf > invertTransdutor.pdf

# Testes
FILES=/tests/*
for f in tests/*.txt
do
    name=${f##*/}
    base=${name%.txt}
    echo "compile ${base}"
    fstcompile --isymbols=data.sym --osymbols=data.sym  $f  > tests/${base}.fst
    fstcompose tests/${base}.fst transdutor.fst > tests/${base}_result.fst
    fstdraw --isymbols=data.sym --osymbols=data.sym  tests/${base}_result.fst | dot -Tpdf > tests/${base}_result.pdf
    
done

mv tests/*.pdf tests/pdfs

#fstcompile --isymbols=data.sym --osymbols=data.sym  tests/12_30.txt  > tests/12_30.fst
#fstcompose tests/12_30.fst transdutor.fst > tests/12_30_result.fst
#fstdraw --isymbols=data.sym --osymbols=data.sym  tests/12_30_result.fst | dot -Tpdf > tests/12_30_result.pdf

#fstcompile --isymbols=data.sym --osymbols=data.sym  tests/00_15.txt  > tests/00_15.fst
#fstcompose tests/00_15.fst transdutor.fst > tests/00_15_result.fst
#fstdraw --isymbols=data.sym --osymbols=data.sym  tests/00_15_result.fst | dot -Tpdf > tests/00_15_result.pdf
