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
# Verifica se a compilação gerou o artigo.pdf com sucesso
if [ -f "artigo.pdf" ]; then
    echo "✅ Sucesso! O PDF foi gerado como artigo.pdf"
else
    echo "❌ Erro: O arquivo artigo.pdf não foi gerado. Verifique os erros de compilação do LaTeX."
fi
echo "=========================================================="
