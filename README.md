# Template LaTeX para TCC em Formato de Artigo Científico — IFPI

Template em LaTeX para elaboração de Trabalhos de Conclusão de Curso (TCC) em formato de artigo científico do **Instituto Federal do Piauí (IFPI)**, totalmente alinhado às normas ABNT vigentes (incluindo a NBR 10520:2023 para citações) e ao *Manual de Trabalhos Acadêmicos do IFPI (2024)*.

---

📄 **Visualizar Exemplo da Saída (PDF):**  
Para ver o resultado final formatado, acesse diretamente o modelo compilado:  
👉 **[artigo.pdf](artigo.pdf)**

---

## 📁 Estrutura Completa do Repositório

```text
Template_TCC_Artigo/
├── artigo.tex                # Arquivo principal do artigo (corpo do texto e seções)
├── artigo.pdf                # Modelo compilado em PDF (resultado final)
├── referencias.bib           # Base de dados de referências bibliográficas (BibTeX)
├── gerar_pdf.sh              # Script de compilação automática para Linux / macOS
├── gerar_pdf.bat             # Script de compilação automática para Windows
├── verificar_conformidade.py # Script Python para verificação de conformidade ABNT/IFPI
├── manual_text.txt           # Extração textual do Manual TCC IFPI para referência
├── LICENSE                   # Licença de uso do modelo
├── README.md                 # Guia de documentação e utilização
├── config/                   # Configurações do LaTeX e personalizações
│   ├── config.tex            # Pacotes, formatação da classe abntex2 e metadados
│   ├── abntex-ifpi.sty       # Pacote customizado com regras específicas do IFPI
│   └── README.md             # Instruções sobre o diretório de configurações
├── estrutura/                # Módulos de conteúdo e dados do trabalho
│   ├── dados.tex             # Dados cadastrais (título, autor, orientador, campus)
│   ├── pre_textuais.tex      # Elementos pré-textuais (cabeçalho, resumo e abstract)
│   ├── pos_textuais.tex      # Elementos pós-textuais (referências, apêndices, anexos)
│   └── README.md             # Orientações sobre a estrutura textual
├── img/                      # Imagens, logotipos e figuras do trabalho
│   ├── Logo-IFPI-Floriano-Horizontal.png
│   ├── Logo-IFPI-Floriano-Vertical.png
│   ├── Logo-IFPI-IF.png
│   ├── tema do tcc.png
│   └── README.md             # Recomendações sobre inclusão de imagens
├── Normas/                   # Acervo de normas ABNT e manuais institucionais em PDF/Docx
│   ├── ABNT-NBR-6023-Referencias-Bibliograficas.pdf
│   ├── ABNT-NBR-6024-Numeracao-progressiva-das-secoes-de-um-documento.pdf
│   ├── ABNT-NBR-6027-Sumario.pdf
│   ├── ABNT_NBR_14724_2024-1.pdf
└── Normas/                   # Acervo de normas ABNT e manuais institucionais em PDF/Docx
    ├── ABNT-NBR-6023-Referencias-Bibliograficas.pdf
    ├── ABNT-NBR-6024-Numeracao-progressiva-das-secoes-de-um-documento.pdf
    ├── ABNT-NBR-6027-Sumario.pdf
    ├── ABNT_NBR_14724_2024-1.pdf
    ├── ABNT_NBR_15287-2011_Projeto-de-Pesquisa-1.pdf
    ├── Abnt_nbr_10520_2023.pdf
    ├── Manual TCC - IFPI.pdf
    ├── Modelo Artigo IFPI.docx
    ├── Modelo Artigo IFPI.pdf
    ├── NBR-15287_2025_Projeto-de-pesquisa.pdf
    ├── Normas de apresentação tabular - IBGE - 1993.pdf
    └── README.md             # Relação descritiva das normas incluídas
```

---

## 🚀 Como Usar

Você pode utilizar este template tanto **localmente em seu computador** (recomendado) quanto via **Overleaf**.

### Opção 1: Uso Local (Linux, Windows ou macOS)

Requer uma distribuição LaTeX instalada:
- **Windows**: [MiKTeX](https://miktex.org/) ou [TeX Live](https://www.tug.org/texlive/)
- **Linux**: TeX Live (`sudo apt install texlive-full` ou pacotes base + `texlive-lang-portuguese` `texlive-publishers`)
- **macOS**: [MacTeX](https://www.tug.org/mactex/)

#### Compilação Automatizada:
O repositório inclui scripts que executam todo o fluxo de compilação (`pdflatex` + `bibtex` + `pdflatex` x2) para gerar o `artigo.pdf`:

- **Windows**: Dê um duplo clique no arquivo `gerar_pdf.bat` ou execute no Prompt de Comando (CMD):
  ```cmd
  gerar_pdf.bat
  ```
- **Linux / macOS**: Execute no terminal:
  ```bash
  ./gerar_pdf.sh
  ```

Se preferir utilizar um editor (como VS Code com a extensão *LaTeX Workshop*, TeXstudio ou Texmaker), basta abrir a pasta do projeto e compilar o arquivo principal `artigo.tex`.

---

### Opção 2: Uso no Overleaf

1. Baixe o repositório em formato `.zip` (**Code** > **Download ZIP** no GitHub).
2. Acesse o [Overleaf](https://www.overleaf.com/) e clique em **New Project** > **Upload Project**.
3. Envie o arquivo `.zip`. O Overleaf identificará automaticamente o arquivo principal `artigo.tex`.

---

## ✏️ Edição do Documento

1. **Dados do Artigo (`estrutura/dados.tex`)**:  
   Preencha o título, nome do autor, orientador, e-mails e vínculo institucional.

2. **Corpo do Texto (`artigo.tex`)**:  
   Escreva o conteúdo das seções (Introdução, Referencial Teórico, Metodologia, Resultados e Conclusão).

3. **Citações e Referências (`referencias.bib`)**:  
   Adicione suas referências em formato BibTeX.

> ℹ️ **Regra ABNT NBR 10520:2023 (Citações)**:  
> As chamadas no texto utilizam autor/organização em **minúsculas** com a primeira letra maiúscula (ex: `(Borges, 2025)` e `Organização das Nações Unidas (2025)`). Nas Referências ao final, os nomes/siglas aparecem automaticamente em **CAIXA ALTA**.
>
> Para instituições/organizações no `.bib`, utilize o campo `organization` sem chaves duplas e, se houver sigla, o campo `org-short`:
> ```bibtex
> @manual{ibge2025,
>     organization = {Instituto Brasileiro de Geografia e Estat{\'e}stica},
>     org-short = {IBGE},
>     title = {Normas de Apresenta{\c c}{\~a}o Tabular},
>     year = {2025}
> }
> ```
> *Nota: Proteja caracteres acentuados em `organization` com sintaxe LaTeX (ex: `{\c c}`, `{\~a}`, `{\'e}`).*

---

## 🔍 Verificação de Conformidade

Este template conta com um script em Python para validar a estrutura e conformidade do seu documento:

```bash
python3 verificar_conformidade.py
```

---

**Professor Ronaldo Pires Borges**
 
- Sempre recompile na ordem indicada para evitar referências quebradas.  
- Utilize `.gitignore` fornecido para evitar versionar artefatos temporários do LaTeX.

---

**Professor Ronaldo Pires Borges**
