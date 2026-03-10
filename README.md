# Template LaTeX para TCC em formato de Artigo Científico - IFPI

Template preparado para artigos científicos apresentados como Trabalhos de Conclusão de Curso (TCC) do Instituto Federal do Piauí (IFPI), alinhado com as normas ABNT e com o *Manual de Trabalhos Acadêmicos do IFPI (2024)*.

## Características

- **Base**: classe `abntex2` atualizada
- **Normas atendidas**: NBR 6022:2018 (Artigo Científico), 10520:2023, 6024, 6027, 6023 (versões vigentes) e Manual TCC IFPI.
- **Formatação padrão**: margens 3 cm/2 cm, Arial/Times New Roman 12 pt, espaçamento simples.
- **Personalização**: folha de rosto, cabeçalho de artigo e comandos específicos do IFPI.
- **Pronto para uso**: estrutura completa com exemplos comentados.
- **Idioma padrão**: português do Brasil (babel `brazil`).

## Como usar

### 1. Personalização dos dados

Edite o arquivo `estrutura/dados.tex` e ajuste os campos:

```latex
% Dados do artigo (estrutura/dados.tex)
\titulo{SEU TÍTULO AQUI}
\autor{SEU NOME COMPLETO}
\emailautor{seuemail@aluno.ifpi.edu.br}
\orientador{Prof. Dr. Nome do Orientador}
\emailorientador{orientador@ifpi.edu.br}
% ...outros dados institucionais e de data
```

Para ajustes de pacotes e de formatação geral, utilize `config/config.tex`.

### 2. Estrutura do documento

```
main.tex               # Arquivo principal
config/
    config.tex         # Classe e configurações do documento
    abntex-ifpi.sty    # Personalizações IFPI
estrutura/
    dados.tex          # Dados do projeto de pesquisa
img/                   # Imagens do documento
referencias.bib        # Bibliografia
README.md              # Este arquivo
```

### 3. Compilação

Para compilar o documento e automaticamente gerar um PDF com o nome `Título - Autor - Ano.pdf`, você pode usar o script incluso no terminal (Linux/macOS):

```bash
./gerar_pdf.sh
```

Ou, se preferir compilar manualmente (o arquivo sairá como `main.pdf`):

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Conteúdo do template

### Elementos pré-textuais e Cabeçalho
- Capa institucional IFPI
- Folha de rosto
- Cabeçalho do Artigo (Título, Autores, Instituição, E-mails)
- Resumo (português) e Abstract (inglês) com palavras-chave
- Data de aprovação

### Elementos textuais
- Introdução
- Referencial Teórico / Estudos Relacionados
- Metodologia
- Resultados e Discussões
- Considerações Finais

### Elementos pós-textuais
- Referências bibliográficas conforme ABNT NBR 6023:2018
- Glossário (opcional)
- Apêndices e Anexos (opcionais)
- Agradecimentos (opcional)

## Recursos especiais

- Comando `\inserirfigura{arquivo}{largura}{legenda}{label}` para figuras com fonte padronizada.
- Comandos `\cite{}` e `\citeonline{}` já configurados para ABNT (pacote `abntex2cite`).  
- Ajustes de metadados PDF automáticos (`config/config.tex` + `estrutura/dados.tex`).  

## Dicas rápidas

- Use `estrutura/dados.tex` para atualizar rapidamente título, autores, orientadores e dados institucionais.  
- Ajustes finos (pacotes adicionais, comandos personalizados) vão em `config/config.tex`.  
- Mantenha imagens em `img/` e referencie com caminhos relativos (`img/arquivo.png`).  
- Sempre recompile na ordem indicada para evitar referências quebradas.  
- Utilize `.gitignore` fornecido para evitar versionar artefatos temporários do LaTeX.

---

**Professor Ronaldo Pires Borges**
