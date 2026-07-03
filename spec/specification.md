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

O pacote `abntex-ifpi.sty` foi verificado em relação à norma **NBR 10520:2023** (Citações em documentos — Apresentação) e atende plenamente aos seus requisitos técnicos e de formatação.

### 4.1. Requisitos da Norma e Status de Conformidade

| Requisito NBR 10520:2023 | Descrição / Regra da Norma | Implementação no Template (`abntex-ifpi.sty`) | Status |
| :--- | :--- | :--- | :--- |
| **Caixa Mista** | Sobrenome do autor/entidade em letras maiúsculas e minúsculas (caixa mista) tanto dentro quanto fora dos parênteses. | O comando `\cite` foi redefinido (linhas 357-368) para extrair o valor `EXPL` do `.aux` e exibir `(Silva, 2023)` em vez de `(SILVA, 2023)`. | **Conforme** |
| **Citação com até 3 Autores** | Devem ser indicados os sobrenomes de todos os autores, separados por ponto e vírgula `;` (entre parênteses) ou por `e` (no corpo do texto). | O sistema de citação separa automaticamente múltiplos autores por ponto e vírgula quando compilado. Ex: `\cite{rastgoo2021}` resulta em `(Rastgoo; Kiani; Escalera, 2021)`. | **Conforme** |
| **Citação com 4 ou mais Autores** | Pode ser citado o primeiro autor seguido da expressão *et al.* (ou todos os autores, desde que mantida a uniformidade no documento). | Suportado nativamente pelo mecanismo do BibTeX/abnTeX2 integrado com as redefinições do arquivo de estilo. | **Conforme** |
| **Ponto Final nas Citações** | O ponto final deve ser usado para encerrar a frase e não a citação (ou seja, colocado após o fecho dos parênteses da citação). | O comando `\cite` não insere ponto final automático, delegando a pontuação ao fluxo do texto do usuário. | **Conforme** |
| **Citação Direta Curta** | Citações diretas de até 3 linhas devem vir no corpo do texto, inseridas entre aspas duplas. | Controle textual direto efetuado pelo autor no LaTeX usando aspas (`“...”`). | **Conforme** |
| **Citação Direta Longa** | Citações com mais de 3 linhas devem vir destacadas com recuo de 4cm da margem esquerda, fonte menor (10pt), espaçamento simples e sem aspas. | O ambiente `citacao` foi redefinido (linhas 70-76) com `\SingleSpacing`, `\footnotesize` (10pt) e recuo esquerdo de 4cm usando o pacote `changepage`. | **Conforme** |
| **Abreviaturas de Localizadores** | Uso padronizado de termos abreviados para páginas (`p.`), volumes (`v.`), capítulos (`cap.`) ou localizadores digitais (`local.`). | Aceita parâmetros opcionais passados no `\cite[p.~10]{chave}` ou `\cite[local.~72]{chave}` renderizando a abreviatura correta. | **Conforme** |

### 4.2. Exemplos de Comandos e Saídas Esperadas

1. **Citação Indireta / Entre Parênteses**: `\cite{chave}`
   - *Resultado*: `(Silva, 2023)` ou `(Rastgoo; Kiani; Escalera, 2021)`.
2. **Citação Direta / No Corpo do Texto**: `\citeonline{chave}`
   - *Resultado*: `Silva (2023)` ou `Rastgoo, Kiani e Escalera (2021)`.
3. **Citação Direta Longa** (mais de 3 linhas):
   - Deve ser inserida utilizando o ambiente `citacao`:
   ```latex
   \begin{citacao}
   Texto longo extraído literalmente da obra de origem, mantendo a integridade do pensamento do autor original \cite{chave}.
   \end{citacao}
   ```

---

## 5. Regras de Apresentação das Referências (NBR 6023)

Conforme o item 5.2.3.1 ("Referências") do Manual de Normalização de Trabalhos Acadêmicos do IFPI (páginas 56 e 57), a lista de referências, ordenada em uma única lista, deve ser padronizada quanto ao recurso tipográfico e à adoção dos elementos complementares. Para este template, o recurso tipográfico escolhido para destacar as obras é o **Negrito**.

A lista de referências deve estar em total conformidade com as normas ABNT NBR 10520:2023 e NBR 6023:2018:

### 5.1. Regras Gerais de Formatação
*   **Ordem:** A lista de referências deve ser organizada em **ordem alfabética**.
*   **Alinhamento:** As referências devem ser **alinhadas à margem esquerda** do texto.
*   **Espaçamento:** Devem ser elaboradas em **espaço simples (1,0)** e separadas entre si por **uma linha em branco** de espaço simples.
*   **Destaque (Negrito):** O negrito é utilizado para destacar o elemento principal da referência, que geralmente é o **título** da obra. Esse destaque deve ser **uniforme** em todas as referências da lista. *Exceção:* Obras sem indicação de autoria (cuja entrada é feita pelo próprio título em caixa alta) não recebem esse destaque.
*   **Documentos Online (URL e Acesso):** Para documentos acessados na internet, é obrigatório registrar o endereço eletrônico precedido da expressão "**Disponível em:**" e a data de acesso precedida da expressão "**Acesso em:**".

### 5.2. Regras e Estruturas por Tipo de Referência

#### Livros, Folhetos e Trabalhos Acadêmicos (Monografia no todo)
*   **Estrutura:** AUTOR. **Título do livro: subtítulo (se houver)**. Edição (se houver). Local de publicação: Editora, Ano de publicação.
*   **Exemplo:** GIL, Antônio Carlos. **Como elaborar projetos de pesquisa**. 6. ed. São Paulo: Atlas, 2019.

#### Capítulos de Livros (Parte de monografia)
*   **Estrutura:** AUTOR DA PARTE. Título do capítulo ou parte. *In*: AUTOR DO LIVRO. **Título do livro**. Edição. Local: Editora, Ano. páginas da parte referenciada.
*   **Exemplo:** CARDOSO, A. P.; LEMLE, A.; BETHLEM, N. Doenças pulmonares obstrutivas crônicas. In: BETHLEM, N. **Pneumologia**. 4. ed. São Paulo: Atheneu, 2000. p. 600-621.

#### Artigos de Revistas Científicas (Publicação periódica)
*   **Estrutura:** AUTOR DO ARTIGO. Título do artigo. **Título da Revista**, Local de publicação, numeração do volume, número/edição, páginas inicial e final do artigo, mês (abreviado) e Ano de publicação.
*   **Exemplo:** SANTOS, Ana Paula Lima dos; RODRIGUES, Mara Eliane Fonseca. Biblioteconomia: gênese, história e fundamentos. **Revista Brasileira de Biblioteconomia e Documentação**, São Paulo, v. 9, n. 2, p. 116-131, 2013.

#### Trabalhos Apresentados em Eventos (Congressos, Simpósios, etc.)
*   **Estrutura:** AUTOR DO TRABALHO. Título do trabalho. *In*: NOME DO EVENTO, numeração do evento., Ano de realização, Local (cidade) de realização. **Título do documento (Ex: Anais [...])**. Local de publicação: Editora, Ano de publicação. páginas inicial e final da parte.
*   **Exemplo:** BLATTMANN, Ursula; RADOS, Gregório Varvakis. Bibliotecas acadêmicas na educação a distância. In: SEMINÁRIO NACIONAL DE BIBLIOTECAS UNIVERSITÁRIAS, 12., 2000, Recife. **Memória SNBU 2000 [...]**. Recife: UFPE, 2000. Disponível em: http://snbu.bvs.br/snbu2000/docs/pt/doc/. Acesso em: 8 nov. 2017.

#### Legislação (Leis, Decretos, Portarias)
*   **Estrutura:** JURISDIÇÃO (em caixa alta). Título/Epígrafe (Lei nº X, data). Ementa. **Dados da publicação** (Ex: Diário Oficial da União...), Local, volume/ano, número, páginas, data exata de publicação.
*   **Exemplo:** BRASIL. Lei nº 9610, de 19 de fevereiro de 1998. Altera, atualiza e consolida a legislação sobre direitos autorais e dá outras providências. **Brasília, DF: Presidência da República**, 1998.

#### Informação de Sites, Redes Sociais ou Documentos Eletrônicos Exclusivos
*   **Estrutura:** AUTOR. Título da informação/serviço. Local, data. Descrição do meio (Ex: Twitter, Podcast). **Disponível em:** URL. **Acesso em:** dia mês. ano.
*   **Exemplo:** C&A BRASIL. E se ele escolher o look dela? Vale apostar no conjuntinho de blusa e saia estampadas no #DiaDosMisturados. Brasil, 1 jun. 2016. Twitter: @cea_brasil. Disponível em: https:twitter.com/cea_brasil/status/738128768921833472. Acesso em: 2 jun. 2020.

---

## 6. Instruções de Compilação

Para compilar o documento de forma que todas as citações cruzadas, referências bibliográficas, lista de figuras e tabelas sejam atualizadas corretamente, é necessária uma sequência específica de compilações.

O arquivo [gerar_pdf.sh](file:///home/rpb/Repositórios/Template_TCC_Artigo/gerar_pdf.sh) automatiza esse processo executando:

1. `pdflatex main` (primeira passada para coletar referências externas)
2. `bibtex main` (compilação do arquivo bibliográfico `.bib`)
3. `pdflatex main` (segunda passada para associar citações)
4. `pdflatex main` (terceira passada para resolver números de páginas e referências cruzadas)
