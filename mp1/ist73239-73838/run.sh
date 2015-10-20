#!/bin/bash

sh clean.sh

fstcompile --isymbols=data.sym --osymbols=data.sym  transdutor.txt  > horas.fst
fstdraw  --isymbols=data.sym --osymbols=data.sym  horas.fst | dot -Tpdf > horas.pdf

# Invert
fstinvert horas.fst > horas-inv.fst
fstdraw  --isymbols=data.sym --osymbols=data.sym  horas-inv.fst | dot -Tpdf > horas-inv.pdf

fstcompile --isymbols=data.sym --osymbols=data.sym  testes/12_30.txt  > testes/12_30.fst
fstcompose testes/12_30.fst horas.fst > testes/12_30_result.fst
fstdraw --isymbols=data.sym --osymbols=data.sym  testes/12_30_result.fst | dot -Tpdf > testes/pdfs/12_30_result.pdf

fstcompile --isymbols=data.sym --osymbols=data.sym  testes/02_15.txt  > testes/02_15.fst
fstcompose testes/02_15.fst horas.fst > testes/02_15_result.fst
fstdraw --isymbols=data.sym --osymbols=data.sym  testes/02_15_result.fst | dot -Tpdf > testes/pdfs/02_15_result.pdf

fstcompile --isymbols=data.sym --osymbols=data.sym  testes/tres_quarenta_cinco.txt  > testes/tres_quarenta_cinco.fst
fstcompose testes/tres_quarenta_cinco.fst horas-inv.fst > testes/tres_quarenta_cinco_result.fst
fstdraw --isymbols=data.sym --osymbols=data.sym  testes/tres_quarenta_cinco_result.fst | dot -Tpdf > testes/pdfs/tres_quarenta_cinco_result.pdf
