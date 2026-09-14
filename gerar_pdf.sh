#!/bin/bash

echo "=========================================================="
echo " Iniciando compilação do LaTeX (artigo.tex)..."
echo "=========================================================="

# Comando de compilação (rodando várias vezes para fechar referências)
pdflatex -interaction=nonstopmode artigo.tex
bibtex artigo
pdflatex -interaction=nonstopmode artigo.tex
pdflatex -interaction=nonstopmode artigo.tex

echo "=========================================================="
# Limpeza de arquivos temporários e auxiliares gerados pelo LaTeX
echo " Limpando arquivos temporários de compilação..."
rm -f *.aux *.bbl *.blg *.brf *.idx *.ilg *.ind *.lof *.log *.lol *.lot *.loq *.out *.toc *.synctex* *.fdb_latexmk *.fls *.bcf *.run.xml
rm -f config/*.aux config/*.log config/*.fls config/*.fdb_latexmk
rm -f estrutura/*.aux estrutura/*.log
echo "=========================================================="

# Verifica se a compilação gerou o artigo.pdf com sucesso
if [ -f "artigo.pdf" ]; then
    echo "✅ Sucesso! O PDF foi gerado como artigo.pdf"
else
    echo "❌ Erro: O arquivo artigo.pdf não foi gerado. Verifique os erros de compilação do LaTeX."
fi
echo "=========================================================="

