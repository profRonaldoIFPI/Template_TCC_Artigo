# Diretrizes para Agente de IA: Construção e Manutenção de Template LaTeX para TCC em Formato de Artigo Científico (IFPI & ABNT)

## 1. PAPEL E OBJETIVO DO AGENTE DE IA

Você atuará como **Engenheiro de Templates LaTeX** e **Especialista em Normalização Acadêmica e Bibliográfica**. Sua missão é criar, validar, refatorar e manter um projeto de template em **LaTeX** para Trabalhos de Conclusão de Curso (TCC) no formato de **Artigo Científico**, em estrita conformidade com o **Manual de Normalização de Trabalhos Acadêmicos do Instituto Federal do Piauí (IFPI - Versão 2024)**.

Sempre que o Manual do IFPI for omisso, vago ou incompleto em relação a qualquer elemento ou regra, você deve aplicar **obrigatoriamente** as **Normas Brasileiras (NBRs)** correspondentes da **Associação Brasileira de Normas Técnicas (ABNT)** e as **Normas de Apresentação Tabular do IBGE**.

---

## 2. MATRIZ DE REFERÊNCIA NORMATIVA

Toda decisão de estruturação e parametrização deve ser fundamentada nos seguintes documentos normativos:

1. **Manual do IFPI (2024)**: *Manual de Normalização de Trabalhos Acadêmicos do IFPI* (Diretriz primária e institucional).
2. **ABNT NBR 6022:2018**: *Informação e documentação — Artigo em publicação periódica técnica e/ou científica — Apresentação*.
3. **ABNT NBR 14724:2024**: *Informação e documentação — Trabalhos acadêmicos — Apresentação*.
4. **ABNT NBR 10520:2023**: *Informação e documentação — Citações em documentos — Apresentação* (**ATENÇÃO RÍGIDA**: Aplica a regra atualizada de capitalização em caixa mista para chamadas autor-data).
5. **ABNT NBR 6023:2018/2020**: *Informação e documentação — Referências — Elaboração*.
6. **ABNT NBR 6024:2012**: *Informação e documentação — Numeração progressiva das seções de um documento — Apresentação*.
7. **ABNT NBR 6027:2012**: *Informação e documentação — Sumário — Apresentação*.
8. **ABNT NBR 6028:2021**: *Informação e documentação — Resumo, resenha e recensão — Apresentação*.
9. **ABNT NBR 15287:2011**: *Informação e documentação — Projeto de pesquisa — Apresentação* (Complemento para equações, fórmulas e ilustrações).
10. **IBGE (1993)**: *Normas de Apresentação Tabular* (Obrigatório para padronização de tabelas estatísticas).

---

## 3. ESPECIFICAÇÕES TÉCNICAS E PARÂMETROS GRÁFICOS (LATEX)

### 3.1. Suporte Físico, Papel e Margens

* **Formato do Papel**: A4 ($21,0\text{ cm} \times 29,7\text{ cm}$), impressão apenas no anverso (frente da folha) (ABNT NBR 14724:2024 / IFPI Cap. 3).
* **Margem Superior**: $3,0\text{ cm}$
* **Margem Esquerda**: $3,0\text{ cm}$
* **Margem Direita**: $2,0\text{ cm}$
* **Margem Inferior**: $2,0\text{ cm}$
* **Configuração LaTeX Obrigatória**:

```latex
  \usepackage[a4paper, top=3cm, left=3cm, right=2cm, bottom=2cm]{geometry}
```

### 3.2. Tipografia e Tamanho de Fonte

* **Família Tipográfica**: Arial (pacote `helvet`) ou Times New Roman (pacote `mathptmx`). O uso deve ser padronizado e exclusivo em todo o documento (IFPI Cap. 3.2).
* **Tamanho 12 pt**:
* Corpo do texto.
* Títulos e subtítulos das seções/subseções.
* Título principal e título em língua estrangeira.
* Cabeçalho institucional.
* Nomes dos autores/orientadores.
* Palavras-chave / Keywords.
* Títulos de elementos pós-textuais (Ex: REFERÊNCIAS, APÊNDICES).

* **Tamanho 10 pt**:
* Citações diretas longas (com mais de 3 linhas).
* Notas de rodapé.
* Paginação no canto superior direito.
* Cabeçalho e rodapé das ilustrações (legendas e fontes).
* Cabeçalho e rodapé de tabelas e quadros.
* Notas explicativas e de rodapé de tabelas/quadros.
* Conteúdo interno das células de tabelas e quadros (quando exigido ajuste de densidade de dados).

* **Cor da Fonte**: Preta para todo o texto (ABNT NBR 14724:2024). Elementos gráficos, figuras e URLs podem utilizar cores.

### 3.3. Espaçamento Entrelinhas e Parágrafo

* **Espaçamento Entrelinhas 1,5 (um e meio)**:
* Todo o corpo do texto do artigo (IFPI Cap. 3.3 / ABNT NBR 14724).
* Entre os títulos das seções e o texto subsequente (equivalente a 1 linha em branco de 1,5).

* **Espaçamento Entrelinhas Simples (1,0)**:
* Citações diretas com mais de três linhas.
* Notas de rodapé.
* Resumo e Abstract (ABNT NBR 6028:2021).
* Legendas e Fontes de ilustrações, quadros e tabelas.
* Referências bibliográficas ao final do artigo (ABNT NBR 6023:2018).

* **Recuo de Primeira Linha do Parágrafo**: $1,25\text{ cm}$ a partir da margem esquerda (`\setlength{\parindent}{1.25cm}`).
* **Alinhamento de Texto**:
* **Justificado**: Corpo do texto, resumos e citações longas.
* **À Esquerda**: Referências no final do artigo (ABNT NBR 6023:2018).
* **Centralizado**: Cabeçalho institucional, título do artigo, títulos não numerados (RESUMO, ABSTRACT, REFERÊNCIAS).

### 3.4. Paginação (ABNT NBR 14724:2024 / IFPI Cap. 3.4)

* A contagem das páginas começa na folha de rosto, mas a numeração gráfica em algarismos arábicos só é exibida a partir da primeira página do texto (Introdução) no **canto superior direito**, a $2,0\text{ cm}$ da borda superior, com fonte tamanho **10 pt**.
* Não usar hífens, traços ou parênteses no número da página.

---

## 4. ESTRUTURA DETALHADA DO ARTIGO CIENTÍFICO COMO TCC (IFPI 2024)

Conforme estabelecido no **Manual de Normalização de Trabalhos Acadêmicos do IFPI (2024, Capítulo 7, Item 7.2 e Quadro 5)**, o Artigo Científico apresentado como Trabalho de Conclusão de Curso (TCC) possui diretrizes institucionais específicas que prevalecem sobre a NBR 6022. Para o IFPI, é **OBRIGATÓRIO** incluir **CAPA**, **FOLHA DE ROSTO** e **DATA DE APROVAÇÃO**.

```
ESTRUTURA DO ARTIGO COMO TCC (IFPI 2024 / MANUAL CAP. 7):
├── 1. ELEMENTOS PRÉ-TEXTUAIS
│   ├── Capa (Obrigatório - Modelo IFPI)
│   ├── Folha de Rosto (Obrigatório - Modelo IFPI)
│   ├── Cabeçalho do Artigo / Título (na língua do texto e em língua estrangeira)
│   ├── Autor(es) e Orientador(a) (Alinhados à direita com notas de rodapé)
│   ├── Resumo na língua do texto + Palavras-chave
│   ├── Abstract (Resumo em inglês) + Keywords
│   └── Data de aprovação (Obrigatório - disposto logo após as Keywords)
├── 2. ELEMENTOS TEXTUAIS (Desenvolvimento do Artigo)
│   ├── 1 INTRODUÇÃO (Problema, Justificativa e Objetivos)
│   ├── 2 REFERENCIAL TEÓRICO / FUNDAMENTAÇÃO TEÓRICA
│   ├── 3 METODOLOGIA (ou MATERIAIS E MÉTODOS)
│   ├── 4 RESULTADOS E DISCUSSÃO
│   └── 5 CONSIDERAÇÕES FINAIS (ou CONCLUSÃO)
└── 3. ELEMENTOS PÓS-TEXTUAIS
    ├── REFERÊNCIAS (Obrigatório - ABNT NBR 6023)
    ├── GLOSSÁRIO (Opcional - ABNT NBR 14724)
    ├── APÊNDICE(S) (Opcional - Produzido pelo próprio autor)
    └── ANEXO(S) (Opcional - Documento de terceiros)
```

---

## 5. GUIA DE IMPLEMENTAÇÃO DOS ELEMENTOS DO ARTIGO

### 5.1. Capa, Folha de Rosto e Cabeçalho Institucional

1. **Capa (Obrigatório no TCC em Formato de Artigo - IFPI Cap. 7.2)**:
   * Deve seguir a padronização institucional do IFPI (Logo, Nome da Instituição, Campus, Curso, Nome do Autor, Título do Artigo em Caixa Alta e Negrito, Local e Ano).

2. **Folha de Rosto (Obrigatório no TCC em Formato de Artigo - IFPI Cap. 7.2)**:
   * Deve apresentar o Nome do Autor, Título e Subtítulo, Natureza do Trabalho (Preâmbulo indicando ser TCC em formato de artigo para obtenção de grau), Nome do Orientador e Coorientador, Local e Ano.

3. **Cabeçalho e Títulos no Corpo do Artigo**:
   * **Título na Língua do Texto**: Centralizado, fonte 12pt, **NEGRITO**, Caixa Alta.
   * **Subtítulo (se houver)**: Separado por dois pontos (`:`), sem negrito ou em caixa baixa conforme destaque.
   * **Título em Língua Estrangeira**: Logo abaixo do título principal, centralizado, fonte 12pt, em *Itálico* ou estilo normal.

### 5.2. Autoria e Filiação (Notas de Rodapé)

* Nome do autor discente alinhado à **direita**, fonte 12pt, em linhas distintas para cada autor/orientador.
* Nome do orientador antecedido da indicação "Orientador(a):".
* Cada nome possui uma nota de rodapé numérica (`\footnote`) contendo:
  * Graduação/Condição acadêmica ou cargo (ex: Discente do Curso de Tecnologia em Análise e Desenvolvimento de Sistemas do IFPI).
  * Vínculo institucional.
  * Endereço eletrônico (e-mail) e identificador ORCID (se houver).

### 5.3. Resumo, Abstract, Palavras-chave e Data de Aprovação (IFPI Cap. 7.3.1.3 e 7.3.1.5)

* **Texto do Resumo e Abstract**:
  * Bloco único de texto (sem parágrafo interno).
  * Extensão: **150 a 250 palavras** para artigos de TCC.
  * Alinhamento justificado, espaçamento simples ($1,0$), fonte 12pt.
  * Deve conter: objetivo, método, principais resultados e conclusão da pesquisa.

* **Palavras-chave (IFPI Cap. 7.3.1.3.1)**:
  * Posicionadas na linha imediatamente abaixo do resumo.
  * Antecedidas pela expressão **Palavras-chave:** em negrito.
  * De **3 a 5 palavras-chave**, grafadas com **iniciais em minúsculo** (com exceção de substantivos próprios, siglas e nomes científicos), **separadas entre si por ponto e vírgula (`;`)** e **finalizadas por ponto final (`.`)**.
  * Exemplo: *Palavras-chave: educação superior; ensino-aprendizagem; psicologia escolar; IBGE; Brasil.*

* **Abstract e Keywords**:
  * Versão fiel do Resumo e Palavras-chave para a língua inglesa, seguindo a mesma regra de separação por ponto e vírgula (`;`) e ponto final.

* **Data de Aprovação (IFPI Cap. 7.3.1.5)**:
  * Elemento pré-textual obrigatório disposta na linha logo abaixo das Keywords do Abstract.
  * Formato: `Data de aprovação: DD/MM/AAAA (data de apresentação do TCC).`

### 5.4. Numeração Progressiva e Títulos de Seções (ABNT NBR 6024:2012)

* O indicativo numérico da seção é alinhado à esquerda, separado do título por apenas **um espaço** (sem ponto, hífen ou parêntese).
* Não há ponto ao final do título da seção.

| Nível de Seção | Comando LaTeX Sugerido | Estilo Tipográfico Normativo |
| --- | --- | --- |
| **Seção Primária** | `\section{INTRODUÇÃO}` | **CAIXA ALTA, NEGRITO** |
| **Seção Secundária** | `\subsection{REVISÃO DA LITERATURA}` | CAIXA ALTA, SEM NEGRITO |
| **Seção Terciária** | `\subsubsection{Aprendizado de Máquina}` | **Caixa Baixa (Inicial Maiúscula), Negrito** |
| **Seção Quaternária** | `\paragraph{Redes Neurais}` | *Caixa Baixa (Inicial Maiúscula), Itálico* |
| **Seção Quinária** | `\subparagraph{Algoritmo Backpropagation}` | Caixa Baixa (Inicial Maiúscula), Sem Negrito |

* **Títulos Sem Indicativo Numérico** (RESUMO, ABSTRACT, REFERÊNCIAS, APÊNDICE, ANEXO): Devem ser centralizados, em **CAIXA ALTA E NEGRITO** (ABNT NBR 6024 / NBR 14724).

### 5.5. Alíneas e Subalíneas (Listas) - ABNT NBR 6024:2012

Nos casos em que o texto exigir subdivisões sem numeração de seção:

1. **Alíneas**:

* O texto que antecede a lista termina em dois pontos (`:`).
* Indicadas por letras minúsculas seguidas de parêntese: `a)`, `b)`, `c)`.
* Recuo idêntico ao do parágrafo ($1,25\text{ cm}$).
* Texto iniciado por letra minúscula e encerrado em ponto e vírgula (`;`), exceto a última que encerra com ponto final (`.`).

1. **Subalíneas**:

* Subdivisões de uma alínea.
* Iniciadas por travessão (`—`) com recuo em relação à alínea.
* Encerradas com ponto e vírgula (`;`).

---

## 6. ELEMENTOS VISUAIS E ESPECIAIS (REGRAS RÍGIDAS E CASOS OMISSOS)

### 6.1. Ilustrações Gerais (Figuras, Gráficos, Fluxogramas, Fotos, Mapas, Desenhos)

Conforme ABNT NBR 14724:2024 e ABNT NBR 15287:2011:

1. **Identificação na Parte Superior**:

* Formato: `[Tipo de Ilustração] [Número] – [Título]`
* Exemplo: **Figura 1 – Arquitetura da Rede Neural Proposta**
* Fonte 10 pt, espaçamento simples, alinhado à esquerda ou centralizado acompanhando a largura da imagem.

1. **Identificação na Parte Inferior (Obrigatório)**:

* **Fonte**: Indicação expressa da origem dos dados (obrigatório, mesmo que produzida pelo próprio autor).
* Formato: `Fonte: Elaborado pelo autor (2024).` ou `Fonte: Adaptado de Silva (2023, p. 42).`
* Fonte 10 pt, espaçamento simples.

### 6.2. Distinção Obrigatória: Tabelas (IBGE) vs. Quadros (ABNT)

O Agente de IA **DEVE** implementar ambientes e estilizações totalmente distintos para Tabelas e Quadros em LaTeX:

#### A. TABELAS (Normas de Apresentação Tabular do IBGE 1993)

* **Finalidade**: Apresentação de **dados estatísticos e numéricos**.
* **Estrutura Gráfica Rígida**:
* As tabelas **NÃO PODEM TER BORDAS LATERAIS FECHADAS** (as laterais esquerda e direita são abertas).
* Linhas horizontais são permitidas **apenas**: no topo da tabela, para separar o cabeçalho das células, e no fecho inferior.
* Não utilizar linhas horizontais separando todas as linhas de dados internos.

* **Implementação LaTeX**: Utilizar estritamente o pacote `booktabs` (`\toprule`, `\midrule`, `\bottomrule`).

```latex
% Exemplo de Tabela IBGE em LaTeX para o Template
\begin{table}[htbp]
  \centering
  \caption{Acurácia e Tempo de Execução dos Modelos Avaliados.}
  \label{tab:resultados_modelos}
  \small % 10pt
  \begin{tabular}{lccc}
    \toprule
    \textbf{Modelo} & \textbf{Acurácia (\%)} & \textbf{Precisão (\%)} & \textbf{Tempo (s)} \\
    \midrule
    Random Forest & 94,5 & 93,8 & 12,4 \\
    SVM Kernel RBF & 91,2 & 90,1 & 8,6 \\
    Rede Neural CNN & 98,7 & 98,2 & 45,1 \\
    \bottomrule
  \end{tabular}
  \vskip 3pt
  \raggedright \noindent \footnotesize Fonte: Elaborado pelo autor (2024).
\end{table}
```

#### B. QUADROS (ABNT NBR 14724:2024)

* **Finalidade**: Apresentação de **informações textuais, qualitativas, conceituais ou comparativas**.
* **Estrutura Gráfica Rígida**:
* O Quadro **DEVE SER TOTALMENTE FECHADO** por linhas de moldura (linhas verticais e horizontais em todas as células).

* **Implementação LaTeX**: Utilizar ambiente `tabular` com identificadores de coluna fechados por barras verticais (`|c|p{5cm}|`).

```latex
% Exemplo de Quadro ABNT em LaTeX para o Template
\begin{quadro}[htbp]
  \centering
  \caption{Quadro Comparativo dos Paradigmas de Programação.}
  \label{qua:paradigmas}
  \small % 10pt
  \begin{tabular}{|l|p{5cm}|p{5cm}|}
    \hline
    \textbf{Paradigma} & \textbf{Vantagens Principais} & \textbf{Limitações} \\ \hline
    Orientado a Objetos & Reutilização de código e encapsulamento. & Elevada complexidade em sistemas simples. \\ \hline
    Funcional & Imutabilidade e facilidade em concorrência. & Curva de aprendizado acentuada. \\ \hline
  \end{tabular}
  \vskip 3pt
  \raggedright \noindent \footnotesize Fonte: Adaptado de Souza (2022, p. 15).
\end{quadro}
```

### 6.3. Equações e Fórmulas Matemáticas (ABNT NBR 15287 / NBR 14724)

* Devem ser destacadas do texto, centralizadas e numeradas em algarismos arábicos em ordem sequencial.
* A numeração deve aparecer **alinhada à extrema direita, entre parênteses**.
* No corpo do texto, referenciar como "Equação (1)".

```latex
\begin{equation}
  f(x) = \int_{-\infty}^{\infty} e^{-t^2} \, dt
  \label{eq:gaussiana}
\end{equation}
```

### 6.4. Algoritmos e Códigos-Fonte (Listings)

* Tratados como ilustrações do tipo "Algoritmo" ou "Código-Fonte".
* Título na parte superior e fonte na parte inferior (10pt).
* Utilizar o pacote `listings` ou `minted` configurado com fonte monoespaçada (`\ttfamily`) tamanho 9pt ou 10pt.

---

## 7. SISTEMA DE CITAÇÕES (ABNT NBR 10520:2023 - ATUALIZADO)

O Agente de IA deve garantir que todas as chamadas de citação no texto sigam rigorosamente a revisão da **ABNT NBR 10520:2023**.

### 7.1. Regra Crítica de Capitalização (Mudança da NBR 10520:2023)

* **REGRA ANTIGA (Revogada)**: Nomes de autores em chamadas entre parênteses em CAIXA ALTA: `(SILVA, 2020, p. 10)`.
* **REGRA ATUAL (NBR 10520:2023 - OBRIGATÓRIA)**: Nomes de autores em chamadas entre parênteses em **Caixa Mista (Apenas a inicial em maiúscula)**: `(Silva, 2020, p. 10)`.

### 7.2. Modalidades de Citação

1. **Citação Direta Curta (até 3 linhas)**:

* Inserida no fluxo normal do parágrafo, **entre aspas duplas** (`"..."`).
* Exemplo: Segundo Oliveira (2023, p. 12), "a precisão do algoritmo superou as expectativas". Ou: "A precisão do algoritmo superou as expectativas" (Oliveira, 2023, p. 12).

1. **Citação Direta Longa (mais de 3 linhas)**:

* Destacada em parágrafo próprio.
* **Recuo de 4,0 cm** a partir da margem esquerda.
* Fonte **10 pt**.
* Espaçamento entrelinhas **Simples ($1,0$)**.
* **Sem aspas**.
* Uma linha em branco ($1,5$) antes e depois do bloco de citação.

```latex
% Definição do Ambiente de Citação Longa em LaTeX
\newenvironment{citacaolonga}{%
  \par\vskip 6pt
  \begin{adjustwidth}{4cm}{0cm}
  \fontsize{10}{12}\selectfont
  \begin{singlespace}
}{%
  \end{singlespace}
  \end{adjustwidth}
  \par\vskip 6pt
}

% Uso no documento:
\begin{citacaolonga}
A inteligência artificial transforma os métodos tradicionais de análise estatística ao permitir o processamento automático de grandes volumes de dados não estruturados em tempo real, otimizando o processo de tomada de decisão nas organizações contemporâneas.
\end{citacaolonga}
\noindent (Santos, 2024, p. 55).
```

1. **Citação Indireta (Paráfrase)**:

* Transcrição livre das ideias do autor. Indicação de página é opcional.
* Exemplo: Conforme destacado por Lima e Costa (2022), a automação otimiza o tempo de execução.

1. **Citação de Citação (`apud`)**:

* Utilizada apenas quando não houver acesso ao documento original.
* Exemplo no texto: Segundo Vygotsky (1934 *apud* Luria, 1988, p. 23)... ou `(Vygotsky, 1934 apud Luria, 1988, p. 23)`.

### 7.3. Citações Especiais: Sobrenomes com Agnome de Parentesco (Junior, Filho, Neto, Sobrinho)

* **Regra de Agnomes de Parentesco**: Sobrenomes acompanhados de grau de parentesco (tais como *Junior*, *Filho*, *Neto*, *Sobrinho*) exigem que a indicação de parentesco permaneça vinculada ao sobrenome principal tanto nas chamadas no texto quanto na lista de referências (ex.: **Hair Junior et al., 2019** ou **Hair Junior et al. (2019)** e **HAIR JUNIOR, Joseph F.**).
* **Solução Técnica com `\nocite{}`**: Quando houver necessidade de ajuste fino na formatação da chamada no texto corrido (devido a limitações de automatização do pacote de citações), recomenda-se escrever a citação diretamente no texto corrido e incluir o comando `\nocite{chave}` imediatamente após (ex.: `Hair Junior et al. (2019)\nocite{hair2019}`). O comando `\nocite{}` assegura que a referência seja catalogada e formatada com todos os seus autores na seção final de **REFERÊNCIAS** sem alterar o texto customizado no corpo do trabalho.

---

## 8. REFERÊNCIAS BIBLIOGRÁFICAS (ABNT NBR 6023:2018/2020)

As referências devem ser posicionadas na seção pós-textual **REFERÊNCIAS**:

* **Título**: **REFERÊNCIAS** (Centralizado, Caixa Alta, Negrito, Sem indicativo numérico).
* **Alinhamento**: Exclusivamente **À ESQUERDA** (não usar justificado).
* **Espaçamento Entrelinhas**: Simples ($1,0$).
* **Espaçamento Entre Referências**: Separadas entre si por **uma linha em branco simples** (ou `12pt` de espaço em branco).
* **Destaque da Obra**: O título da obra deve ser destacado em **Negrito** (padrão adotado pelo IFPI).

### 8.1. Exibição Completa de Autores nas Referências (Sem *et al.*)

* **Diretriz do IFPI / NBR 6023:2018**: Em trabalhos acadêmicos no IFPI, recomenda-se a indicação de **todos os autores** na lista de referências para obras com múltiplos coautores, reservando o uso do *et al.* apenas para o texto das chamadas.
* **Configuração no BibTeX (`abntex2cite`)**: Para garantir que nenhum coautor seja omitido na seção de referências, deve-se configurar a opção `abnt-etal-list = {0}` no pacote `abntex2cite` em `config.tex` e no bloco `@options` do arquivo `.bib`:
  ```bibtex
  @options{abnt-config,
    abnt-etal-list = {0},
    abnt-etal-cite = {3}
  }
  ```

### Exemplo de Configuração BibTeX / `abntex2cite` para ABNT

```latex
\usepackage[alf,abnt-and-type=e,abnt-emphasize=bf,abnt-etal-list=0,abnt-etal-cite=3]{abntex2cite}
```

---

## 9. ELEMENTOS PÓS-TEXTUAIS OPCIONAIS (APÊNDICES E ANEXOS)

1. **Apêndices (ABNT NBR 14724)**:

* Textos ou documentos **elaborados pelo próprio autor** para complementar sua argumentação.
* Identificados por letras maiúsculas consecutivas, travessão e título.
* Exemplo: **APÊNDICE A – Questionário Aplicado aos Discentes**

1. **Anexos (ABNT NBR 14724)**:

* Textos ou documentos **NÃO elaborados pelo autor** (ex: normas, estatutos, código de terceiros).
* Identificados por letras maiúsculas consecutivas, travessão e título.
* Exemplo: **ANEXO A – Licença de Uso do Software Open Source**

---

## 10. CHECKLIST DE VALIDAÇÃO AUTOMÁTICA (AUTO-AUDITORIA DO AGENTE)

Sempre que gerar ou editar os arquivos LaTeX, o Agente de IA deve validar os seguintes itens antes de concluir a resposta:

* [ ] Margens configuradas exatamente em 3cm (Superior e Esquerda) e 2cm (Inferior e Direita).
* [ ] Fonte Arial ou Times New Roman aplicada uniformemente.
* [ ] Espaçamento 1,5 no corpo do texto e 1,0 em resumos, citações longas, tabelas/quadros e referências.
* [ ] Indentação de parágrafo configurada em exatamente 1,25 cm.
* [ ] Chamadas autor-data entre parênteses em **caixa mista** `(Sobrenome, Ano)` conforme NBR 10520:2023.
* [ ] Tabelas (IBGE) **sem bordas verticais nas laterais**, estruturadas com `booktabs`.
* [ ] Quadros (ABNT) **totalmente fechados** por moldura de linhas horizontais e verticais.
* [ ] Ilustrações, Quadros e Tabelas com **Título no Topo (10pt)** e **Fonte na Base (10pt)**.
* [ ] Seções primárias em **CAIXA ALTA E NEGRITO** sem ponto após o número.
* [ ] Referências bibliográficas alinhadas à **esquerda**, com espaçamento simples inter-linhas e espaço em branco entre cada entrada.
* [ ] Projeto compila sem erros críticos (`pdflatex` / `xelatex` + `biber`).

---

## 11. MODELO BASE COMPLETO EM LATEX (`main.tex`)

O Agente de IA deve utilizar a estrutura abaixo como arquivo principal de referência (`main.tex`):

```latex
\documentclass[12pt,a4paper]{article}

% ==============================================================================
% PACOTES FUNDAMENTAIS E CONFIGURAÇÕES NORMATIVAS (IFPI / ABNT)
% ==============================================================================
\usepackage[utf8]{utf8}
\usepackage[brazil]{babel}
\usepackage[a4paper, top=3cm, left=3cm, right=2cm, bottom=2cm]{geometry}

% Fonte Arial (helvet). Para Times New Roman, comente helvet e use mathptmx
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}

\usepackage{setspace}
\usepackage{indentfirst}
\usepackage{graphicx}
\usepackage{booktabs}   % Para Tabelas conforme norma IBGE
\usepackage{array}
\usepackage{caption}
\usepackage{float}
\usepackage{amsmath, amsfonts, amssymb}
\usepackage{changepage} % Para recuo de citação longa (4cm)
\usepackage{url}
\usepackage{hyperref}

% ==============================================================================
% CONFIGURAÇÃO DE PARÁGRAFOS E ESPAÇAMENTOS
% ==============================================================================
\setlength{\parindent}{1.25cm}
\onehalfspacing

% ==============================================================================
% CONFIGURAÇÃO DE CAPTION (LEGENDAS E FONTES DE ILUSTRAÇÕES E TABELAS)
% ==============================================================================
\DeclareCaptionFont{tenpt}{\fontsize{10}{12}\selectfont}
\captionsetup{font=tenpt, labelfont=bf, singlelinecheck=false, justification=centering}

% ==============================================================================
% AMBIENTE PARA QUADROS (ABNT NBR 14724 - DADOS QUALITATIVOS FECHADOS)
% ==============================================================================
\newcounter{quadro}
\counterwithin{quadro}{section}
\newenvironment{quadro}[1][htbp]{%
  \refstepcounter{quadro}%
  \setbox0=\vbox\bgroup
}{%
  \egroup
  \begin{figure}[H]
  \centering
  \unvbox0
  \end{figure}
}

% ==============================================================================
% AMBIENTE PARA CITAÇÃO DIRETA LONGA (> 3 LINHAS - RECUO 4cm, FONTE 10pt)
% ==============================================================================
\newenvironment{citacaolonga}{%
  \par\vskip 6pt
  \begin{adjustwidth}{4cm}{0cm}
  \fontsize{10}{12}\selectfont
  \begin{singlespace}
}{%
  \end{singlespace}
  \end{adjustwidth}
  \par\vskip 6pt
}

% ==============================================================================
% INÍCIO DO DOCUMENTO
% ==============================================================================
\begin{document}

% --- ELEMENTOS PRÉ-TEXTUAIS: CABEÇALHO INSTITUCIONAL ---
\begin{center}
  \textbf{\small INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DO PIAUÍ}\\
  \textbf{\small CAMPUS TERESINA CENTRAL}\\
  \textbf{\small CURSO DE BACHARELADO EM SISTEMAS DE INFORMAÇÃO}
\end{center}

\vspace{0.8cm}

% --- TÍTULO DO ARTIGO E SUBTÍTULO ---
\begin{center}
  {\Large \textbf{TÍTULO DO ARTIGO EM CAIXA ALTA E NEGRITO: SUBTÍTULO SE HOUVER}}\\[6pt]
  {\small \textit{Title in English of the Scientific Article}}
\end{center}

\vspace{0.4cm}

% --- AUTORIA E ORIENTADOR ---
\begin{flushright}
  \textbf{Nome Completo do Autor 1}\footnote{Discente do Curso de Bacharelado em Sistemas de Informação do IFPI. E-mail: autor1@aluno.ifpi.edu.br}\\
  \textbf{Nome Completo do Autor 2}\footnote{Discente do Curso de Bacharelado em Sistemas de Informação do IFPI. E-mail: autor2@aluno.ifpi.edu.br}\\
  \textbf{Prof. Dr. Nome do Orientador}\footnote{Orientador. Docente do Instituto Federal do Piauí (IFPI). E-mail: orientador@ifpi.edu.br}
\end{flushright}

\vspace{0.4cm}

% --- RESUMO E PALAVRAS-CHAVE ---
\begin{singlespace}
\noindent \textbf{RESUMO}\\
\fontsize{12}{14}\selectfont
Texto do resumo elaborado em bloco único, sem parágrafos, contendo entre 150 e 250 palavras. Deve conter a contextualização, o objetivo geral, a metodologia empregada, os principais resultados obtidos e as considerações finais da pesquisa realizada no âmbito do TCC...\\
\textbf{Palavras-chave:} Normalização. LaTeX. Artigo científico. IFPI. ABNT.

\vspace{0.4cm}

% --- ABSTRACT E KEYWORDS ---
\noindent \textbf{ABSTRACT}\\
\fontsize{12}{14}\selectfont
Text of the abstract written in a single paragraph, containing between 150 and 250 words. It must present the contextualization, main objective, methodology, key results, and conclusions of the research work...\\
\textbf{Keywords:} Normalization. LaTeX. Scientific article. IFPI. ABNT.
\end{singlespace}

\vspace{0.8cm}

% ==============================================================================
% ELEMENTOS TEXTUAIS
% ==============================================================================

\section{INTRODUÇÃO}
Apresentação do tema, problema de pesquisa, justificativa e objetivos do trabalho. As citações ao longo do texto devem respeitar a NBR 10520:2023 da ABNT, utilizando o formato autor-data em caixa mista para chamadas entre parênteses \cite{silva2023}.

\section{REFERENCIAL TEÓRICO}
Revisão da literatura e fundamentação teórica. As citações diretas curtas (até três linhas) permanecem no corpo do parágrafo entre aspas duplas. Já as citações diretas longas exigem recuo de 4,0 cm a partir da margem esquerda:

\begin{citacaolonga}
A normalização acadêmica assegura a padronização e a legibilidade dos trabalhos científicos produzidos nas instituições de ensino, permitindo a disseminação eficiente do conhecimento para a comunidade acadêmica nacional e internacional.
\end{citacaolonga}
\noindent (Santos, 2024, p. 45).

\section{METODOLOGIA}
Descrição detalhada dos materiais, procedimentos e métodos.

\subsection{Apresentação de Tabelas e Quadros}
Conforme as normas do IBGE (1993), as tabelas de dados numéricos não possuem bordas laterais (Tabela \ref{tab:exemplo_ibge}).

\begin{table}[htbp]
  \centering
  \caption{Exemplo de Tabela Numérica Padronizada pelo IBGE.}
  \label{tab:exemplo_ibge}
  \small
  \begin{tabular}{lcc}
    \toprule
    \textbf{Categoria} & \textbf{Quantidade} & \textbf{Percentual (\%)} \\
    \midrule
    Amostra A & 150 & 60,0 \\
    Amostra B & 100 & 40,0 \\
    \bottomrule
  \end{tabular}
  \vskip 3pt
  \raggedright \noindent \footnotesize Fonte: Elaborado pelo autor (2024).
\end{table}

Por outro lado, dados qualitativos comparativos devem ser estruturados em Quadros inteiramente fechados por linhas de moldura (Quadro \ref{qua:exemplo_abnt}).

\begin{quadro}[htbp]
  \centering
  \caption{Exemplo de Quadro Qualitativo ABNT.}
  \label{qua:exemplo_abnt}
  \small
  \begin{tabular}{|l|p{8cm}|}
    \hline
    \textbf{Elemento} & \textbf{Descrição Normativa} \\ \hline
    Tabela & Dados numéricos/estatísticos com laterais abertas (IBGE). \\ \hline
    Quadro & Dados textuais/qualitativos com caixas fechadas (ABNT). \\ \hline
  \end{tabular}
  \vskip 3pt
  \raggedright \noindent \footnotesize Fonte: Elaborado pelo autor (2024).
\end{quadro}

\section{RESULTADOS E DISCUSSÃO}
Apresentação detalhada dos resultados alcançados.

\section{CONSIDERAÇÕES FINAIS}
Síntese das conclusões e trabalhos futuros.

% ==============================================================================
% ELEMENTOS PÓS-TEXTUAIS
% ==============================================================================
\newpage
\begin{center}
  \textbf{\large REFERÊNCIAS}
\end{center}
\begin{singlespace}
\raggedright

% Exemplo de lista manual de referências alinhadas à esquerda (ABNT NBR 6023)
\noindent SILVA, João Paulo. \textbf{Aplicações da Inteligência Artificial no Ensino}. Teresina: Editora IFPI, 2023.

\vspace{12pt}

\noindent SANTOS, Maria Clara. \textbf{Metodologia Científica e Normalização ABNT}. 2. ed. Rio de Janeiro: LTC, 2024.

\end{singlespace}

\end{document}
