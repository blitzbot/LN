#!/bin/bash

rm -f hours.fst
rm -f hours.pdf

fstcompile --isymbols=data.sym --osymbols=data.sym  transdutor.txt  > hours.fst
fstdraw  --isymbols=data.sym --osymbols=data.sym  hours.fst | dot -Tpdf > hours.pdf