#!/bin/bash

rm -f hours.fst
rm -f hours.pdf
rm -f example1.fst result1.pdf

fstcompile --isymbols=data.sym --osymbols=data.sym  transdutor.txt  > hours.fst
fstdraw  --isymbols=data.sym --osymbols=data.sym  hours.fst | dot -Tpdf > hours.pdf

# Testes
fstcompile --isymbols=data.sym --osymbols=data.sym  example1.txt  > example1.fst

fstcompose example1.fst hours.fst > result1.fst
fstdraw --isymbols=data.sym --osymbols=data.sym  result1.fst | dot -Tpdf > result1.pdf
