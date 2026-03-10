#!/bin/bash

# Extrai os dados do arquivo dados.tex usando expressões regulares
TITULO=$(grep -oP '(?<=\\titulo\{)[^}]+' estrutura/dados.tex)
AUTOR=$(grep -oP '(?<=\\autor\{)[^}]+' estrutura/dados.tex)
ANO=$(grep -oP '(?<=\\data\{)[^}]+' estrutura/dados.tex)

# Remove espaços em branco extras do início e fim
TITULO=$(echo "$TITULO" | xargs)
AUTOR=$(echo "$AUTOR" | xargs)
ANO=$(echo "$ANO" | xargs)

# Limpa caracteres que podem ser inválidos para nomes de arquivos (como / ou :)
NOME_ARQUIVO=$(echo "$TITULO - $AUTOR - $ANO" | tr -d ':/\\*?"<>|')

# Adiciona a extensão
NOME_ARQUIVO="${NOME_ARQUIVO}.pdf"

echo "=========================================================="
echo " Iniciando compilação do LaTeX..."
echo " Arquivo de saída planejado: $NOME_ARQUIVO"
echo "=========================================================="

# Comando de compilação (rodando várias vezes para fechar referências)
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex

echo "=========================================================="
# Verifica se a compilação gerou o main.pdf com sucesso
if [ -f "main.pdf" ]; then
    # Renomeia o documento
    mv main.pdf "$NOME_ARQUIVO"
    echo "✅ Sucesso! O PDF foi gerado e renomeado para:"
    echo "   $NOME_ARQUIVO"
else
    echo "❌ Erro: O arquivo main.pdf não foi gerado. Verifique os erros de compilação do LaTeX."
fi
echo "=========================================================="
