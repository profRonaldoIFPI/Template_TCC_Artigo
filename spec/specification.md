# Especificação Técnica do Template LaTeX (TCC - Formato Artigo)

Este documento descreve a organização, estrutura e o funcionamento técnico do template LaTeX para Trabalho de Conclusão de Curso (TCC) no formato de artigo científico, adaptado e personalizado para o **Instituto Federal do Piauí (IFPI) - Campus Floriano**.

---

## 1. Visão Geral do Projeto

O projeto utiliza a classe `abntex2` (baseada na tradicional classe `memoir`), aplicando customizações para atender ao **Manual de Normalização de Trabalhos Acadêmicos do IFPI (2024)** e às principais normas da ABNT:

- **NBR 14724:2011**: Informação e documentação — Trabalhos acadêmicos — Apresentação.
- **NBR 6024:2012**: Numeração progressiva das seções de um documento escrito.
- **NBR 6027:2012**: Sumário — Apresentação.
- **NBR 10520:2023**: Citações em documentos — Apresentação.
- **NBR 6023:2018**: Referências — Apresentação.
- **NBR 15287:2011**: Projeto de pesquisa — Apresentação.

---

## 2. Estrutura de Diretórios e Arquivos

O projeto está organizado de maneira modular para facilitar a manutenção e a edição do conteúdo:

```text
├── main.tex                 # Arquivo principal (ponto de entrada)
├── referencias.bib          # Base de dados bibliográfica (BibTeX)
├── gerar_pdf.sh             # Script automatizado para compilação do projeto
├── config/
│   ├── config.tex           # Configurações gerais, pacotes e margens
│   └── abntex-ifpi.sty      # Pacote de estilo com customizações institucionais do IFPI
├── estrutura/
│   ├── dados.tex            # Metadados do trabalho (título, autor, orientador, etc.)
│   ├── pre_textuais.tex     # Capa, folha de rosto, resumo, abstract e aprovação
│   └── pos_textuais.tex     # Geração automática de referências e apêndices
└── img/                     # Diretório contendo imagens e logos institucionais
```

### Detalhamento dos Arquivos Principais

#### 1. [main.tex](file:///home/rpb/Repositórios/Template_TCC_Artigo/main.tex)

É o ponto de entrada da compilação. Ele coordena a inclusão dos arquivos de configuração e estrutura (`\input{...}`) e abriga os **Elementos Textuais**:

- `\section{INTRODUÇÃO}`
- `\section{REFERENCIAL TEÓRICO}`
- `\section{METODOLOGIA}`
- `\section{RESULTADOS E DISCUSSÃO}`
- `\section{CONSIDERAÇÕES FINAIS}`

#### 2. [config/config.tex](file:///home/rpb/Repositórios/Template_TCC_Artigo/config/config.tex)

Carrega a classe `abntex2` configurada como `article` e com fonte padrão `12pt`. Importa pacotes utilitários do LaTeX para manipulação de imagens, tabelas complexas, símbolos matemáticos e configura o espaçamento de parágrafos (`1.25cm`) e comportamento dos hiperlinks no PDF (`hyperref`).

#### 3. [config/abntex-ifpi.sty](file:///home/rpb/Repositórios/Template_TCC_Artigo/config/abntex-ifpi.sty)

Contém as customizações específicas desenvolvidas para o IFPI:

- **Cores Institucionais**: Define `ifpiazul` (RGB: 0, 51, 102), `ifpiverde` (RGB: 0, 150, 57) e `ifpicinza` (RGB: 102, 102, 102).
- **Margens**: Superior e esquerda de `3cm`, inferior e direita de `2cm` (conforme NBR 14724).
- **Capa e Folha de Rosto**: Layout customizado exibindo a logo do IFPI, nome do campus, curso e preâmbulo do artigo.
- **Formatação de Fontes**: Tamanho 12pt para todo o trabalho, incluindo corpo do texto, dados da capa, folha de rosto, títulos das seções, cabeçalho, resumos e palavras-chave/keywords (conforme orientações institucionais). Citações recuadas longas, notas de rodapé, paginação e legendas mantêm-se em tamanho menor (10pt).
- **Tratamento do Nome do Autor**: Na capa, folha de rosto e cabeçalho, o nome do autor deve vir com apenas as iniciais em maiúsculas (letra de caixa mista) e tamanho 12pt (Arial no cabeçalho).
- **Ambiente Quadro**: Define o elemento flutuante `quadro` com contador próprio, separado de `table` (tabelas).
- **Tratamento de Citação**: Implementa modificações para atender à norma **NBR 10520:2023** (citando autores com a capitalização correta em vez de caixa alta dentro de parênteses).

#### 4. [estrutura/dados.tex](file:///home/rpb/Repositórios/Template_TCC_Artigo/estrutura/dados.tex)

Contém os comandos de atribuição de dados que alimentam a capa, folha de rosto e cabeçalho do artigo. Exemplos:

- `\titulo{...}` e `\subtitulo{...}`
- `\autor{...}` e `\emailautor{...}`
- `\orientador{...}` e `\emailorientador{...}`
- `\curso{...}` e `\campus{...}`

#### 5. [estrutura/pre_textuais.tex](file:///home/rpb/Repositórios/Template_TCC_Artigo/estrutura/pre_textuais.tex)

Gera automaticamente a capa, a folha de rosto, o cabeçalho de título acadêmico e as seções de resumo e abstract. Inclui também o bloco para a data de aprovação do TCC.

#### 6. [estrutura/pos_textuais.tex](file:///home/rpb/Repositórios/Template_TCC_Artigo/estrutura/pos_textuais.tex)

Comanda a geração das Referências utilizando o comando `\bibliography{referencias}` e prepara os ambientes opcionais para Apêndices e Anexos.

---

## 3. Elementos Gráficos e de Dados (LaTeX)

### 3.1. Figuras

As figuras devem possuir legenda explicativa (título) no topo e indicação de fonte na parte inferior.

```latex
\begin{figure}[htbp]
    \centering
    \caption{Exemplo de figura no documento}
    \includegraphics[width=0.5\textwidth]{img/nome_da_imagem.png}
    \fonte{IFPI - Instituto Federal do Piauí.}
    \label{fig:exemplo}
\end{figure}
```

### 3.2. Tabelas vs. Quadros

- **Tabela**: Utilizada para dados predominantemente numéricos. Possui estrutura aberta nas laterais (sem bordas verticais externas), conforme as normas de apresentação tabular do IBGE.

```latex
\begin{table}[htbp]
    \centering
    \caption{Exemplo de tabela}
    \label{tab:exemplo}
    \begin{tabular}{p{4cm}cc}
        \toprule
        \textbf{Item} & \textbf{Coluna 1} & \textbf{Coluna 2} \\
        \midrule
        Dado A & 120 & 87\% \\
        Dado B & 32 & 74\% \\
        \bottomrule
    \end{tabular}
    \fonte{Elaborado pelo autor.}
\end{table}
```

- **Quadro**: Utilizado para dados textuais ou qualitativos. Possui estrutura fechada em todos os lados (com bordas verticais e horizontais delimitando todas as células).

```latex
\begin{quadro}[htbp]
    \centering
    \caption{Exemplo de quadro}
    \label{qua:exemplo}
    \begin{tabular}{|p{3cm}|p{4cm}|p{6cm}|}
        \hline
        \textbf{Categoria} & \textbf{Definição} & \textbf{Observação} \\
        \hline
        Teoria X & Explicação detalhada & Nota de rodapé explicativa \\ \hline
        Teoria Y & Outra explicação & Outra nota relevante \\ \hline
    \end{tabular}
    \fonte{Elaborado pelo autor.}
\end{quadro}
```

---

## 4. Sistema de Citações (NBR 10520:2023)

O pacote `abntex-ifpi.sty` redefine os comandos de citação padrão para implementar a nova regulamentação de citações da ABNT, onde autores não devem aparecer em caixa alta dentro dos parênteses.

1. **Citação Indireta / Entre Parênteses**: `\cite{chave}`
   - *Resultado esperado*: `(Silva, 2023)` em vez de `(SILVA, 2023)`.
2. **Citação Direta / No Corpo do Texto**: `\citeonline{chave}`
   - *Resultado esperado*: `Silva (2023)`.
3. **Citação Direta Longa** (mais de 3 linhas):
   - Deve ser inserida utilizando o ambiente `citacao`. O template formata automaticamente o recuo de 4cm da margem esquerda, com fonte reduzida (10pt) e espaçamento simples.

   ```latex
   \begin{citacao}
   Texto longo extraído literalmente da obra de origem, mantendo a integridade do pensamento do autor original \cite{chave}.
   \end{citacao}
   ```

---

## 5. Regras de Apresentação das Referências (NBR 6023)

Conforme a ABNT NBR 6023 e as diretivas específicas do Manual de Normalização do IFPI (Seção 11), a lista de referências ao final do trabalho deve obedecer às seguintes regras de formatação:

1. **Localização e Título**:
   - Inserida logo após o término dos elementos textuais.
   - O título deve ser **REFERÊNCIAS** (grafado em letras maiúsculas, negrito, centralizado e sem numeração de seção).
2. **Alinhamento e Espaçamento**:
   - Todo o corpo das referências deve estar **alinhado à margem esquerda** (sem recuo de parágrafo).
   - O espaçamento interno de cada referência deve ser **simples (1.0)**.
   - Cada referência deve ser separada da seguinte por **uma linha em branco** de espaçamento simples.
3. **Uniformidade Tipográfica**:
   - O recurso tipográfico escolhido para destacar o título da obra (no caso deste template, o **negrito**) deve ser aplicado uniformemente em todas as referências com autoria declarada.
   - Para obras sem indicação de autoria, a entrada é feita pelo próprio título em letras maiúsculas (apenas a primeira palavra), sem o destaque em negrito.
4. **Links e Acesso Eletrônico**:
   - Para referências retiradas da internet, o endereço da URL deve vir precedido de "`Disponível em: `" e a data de consulta precedida de "`Acesso em: `".

---

## 6. Instruções de Compilação

Para compilar o documento de forma que todas as citações cruzadas, referências bibliográficas, lista de figuras e tabelas sejam atualizadas corretamente, é necessária uma sequência específica de compilações.

O arquivo [gerar_pdf.sh](file:///home/rpb/Repositórios/Template_TCC_Artigo/gerar_pdf.sh) automatiza esse processo executando:

1. `pdflatex main` (primeira passada para coletar referências externas)
2. `bibtex main` (compilação do arquivo bibliográfico `.bib`)
3. `pdflatex main` (segunda passada para associar citações)
4. `pdflatex main` (terceira passada para resolver números de páginas e referências cruzadas)
