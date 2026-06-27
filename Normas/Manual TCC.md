# Manual de Instruções TCC IFPI / ABNT

Este documento é um **guia paramétrico e estrutural** desenhado para instruir um agente de Inteligência Artificial a gerar um arquivo `.tex` (template LaTeX) rigorosamente alinhado ao Manual de Normalização do IFPI (2024), normas ABNT vigentes e diretrizes de apresentação tabular do IBGE.

---

## 1. Definições Globais (Classe e Geometria)

O agente deve iniciar o documento com configurações precisas de classe e layout de página.

* **Classe do Documento:** Recomenda-se o uso da classe `article` padrão ou `abntex2` com a opção `article`.
  * `\documentclass[12pt, a4paper, brazil]{article}`
* **Geometria da Página (Pacote `geometry`):**
  * `a4paper` (210 mm x 297 mm)
  * Margem Superior (`top`): `3cm`
  * Margem Esquerda (`left`): `3cm`
  * Margem Inferior (`bottom`): `2cm`
  * Margem Direita (`right`): `2cm`
* **Codificação e Idioma:**
  * `\usepackage[utf8]{inputenc}`
  * `\usepackage[T1]{fontenc}`
  * `\usepackage[brazil]{babel}`

---

## 2. Tipografia e Espaçamento

O template deve refletir os padrões visuais exigidos para TCCs.

* **Fonte Principal:** Times New Roman (pacote `mathptmx` ou `newtxtext,newtxmath`) ou Arial (pacote `helvet` com `\renewcommand{\familydefault}{\sfdefault}`).
* **Tamanho Base:** `12pt` para o texto principal.
* **Espaçamento Entrelinhas (Pacote `setspace`):**
  * Texto principal: `1.5` (`\onehalfspacing`).
  * Citações longas, notas de rodapé, referências e legendas: Simples (`\singlespacing`).
* **Recuo de Parágrafo:**
  * `\setlength{\parindent}{1.25cm}` (ou `1.5cm`, defina como variável ajustável).
  * Sem espaçamento extra entre parágrafos (`\setlength{\parskip}{0pt}`).

---

## 3. Elementos Pré-Textuais (Estrutura do Artigo)

O agente deve criar comandos personalizados ou usar os nativos para estruturar o cabeçalho do artigo.

* **Título:** Centralizado, tamanho 12pt (ou 14pt dependendo da variação local do IFPI), **negrito**, letras maiúsculas.
* **Título Estrangeiro:** Logo abaixo do título original, centralizado, *itálico*, sem negrito.
* **Autoria e Filiação:** Alinhado à direita ou centralizado. Usar notas de rodapé (com símbolos ou números) para indicar filiação institucional (IFPI), curso e e-mail.
* **Resumo (Ambiente `abstract`):**
  * Palavra "Resumo" centralizada, sem numeração.
  * Texto do resumo: parágrafo único, sem recuo na primeira linha, espaçamento simples (`\singlespacing`), tamanho 12pt.
  * **Palavras-chave:** Inseridas logo após o resumo. Formato: "Palavras-chave: Palavra 1; Palavra 2; Palavra 3."
* **Abstract (Língua Estrangeira):** Mesma formatação do resumo, com a palavra "Abstract" e "Keywords".

---

## 4. Numeração Progressiva e Títulos de Seção (NBR 6024)

O agente deve configurar o pacote `titlesec` para garantir que as seções obedeçam à NBR 6024. Não deve haver ponto após o número da seção (ex: "1 INTRODUÇÃO", não "1. INTRODUÇÃO").

* **Seção Primária (`\section`):** Algarismo arábico, CAIXA ALTA, **Negrito**, tamanho 12pt.
  * *Comando titlesec:* `\titleformat{\section}{\normalfont\normalsize\bfseries\uppercase}{\thesection}{1em}{}`
* **Seção Secundária (`\subsection`):** Algarismo arábico, Caixa baixa (apenas 1ª letra maiúscula), **Negrito**, tamanho 12pt.
* **Seção Terciária (`\subsubsection`):** Algarismo arábico, Caixa baixa, sem negrito, *Itálico* ou Sublinhado, tamanho 12pt.
* **Espaçamento das Seções:** Uma linha em branco (1.5 de entrelinhas) antes e depois de cada título de seção.

---

## 5. Citações e Atualização ABNT NBR 10520:2023

Esta é a instrução mais crítica para o agente de IA, devido à recente mudança nas normas.

* **Pacote de Bibliografia:** Recomenda-se o uso do `biblatex` com o estilo `abnt` (`biblatex-abnt`).
  * `\usepackage[style=abnt, itrim=false, justify]{biblatex}`
* **Regra de Ouro (2023):** Nomes de autores dentro de parênteses **NÃO** são mais escritos em CAIXA ALTA, apenas com a primeira letra em maiúscula (Ex: Silva, 2021). O agente deve configurar o `biblatex-abnt` para refletir isso ou instruir a escrita correta no texto caso se use citação manual.
* **Citação Longa (Ambiente customizado `citacaolonga`):**
  * Criar um ambiente baseado em `quote` ou `quotation`.
  * Recuo à esquerda de `4cm`.
  * Fonte tamanho `10pt` (`\small`).
  * Espaçamento simples (`\singlespacing`).
  * Sem aspas. Sem recuo de primeira linha dentro da citação.

---

## 6. Ilustrações e Tabelas Padrão IBGE

O agente deve gerar macros ou instruções de uso para figuras e tabelas. O uso do pacote `caption` é obrigatório para padronizar fontes.

* **Configuração de Legendas (`caption`):**
  * Tamanho da fonte: 10pt (`font=small` ou `font=footnotesize`).
  * Posição: Superior para o Título (ex: **Tabela 1 – Título**), Inferior para a Fonte/Notas.
  * Alinhamento: Esquerda ou centralizado (depende do tamanho, preferencialmente justificado ou à esquerda).
* **Instruções para Tabelas (Padrão IBGE):**
  * Obrigatório o uso do pacote `booktabs`.
  * **Proibido:** Uso de linhas verticais (nunca usar `|` no ambiente tabular).
  * **Proibido:** Linhas horizontais internas para separar cada linha de dados.
  * **Estrutura esperada em código:**

        ```latex
        \begin{table}[htb]
            \centering
            \caption{Título da Tabela}
            \begin{tabular}{lcc}
                \toprule
                Cabeçalho 1 & Cabeçalho 2 & Cabeçalho 3 \\
                \midrule
                Dado A & 10 & 20 \\
                Dado B & 30 & 40 \\
                \bottomrule
            \end{tabular}
            \par\vspace{1ex}
            {\footnotesize Fonte: Elaborada pelo autor (2024).}
        \end{table}
        ```

---

## 7. Elementos Pós-Textuais

* **Referências:** Devem ser inseridas através do comando de impressão do `biblatex` (`\printbibliography[title=Referências]`), com alinhamento justificado ou à esquerda (a depender da configuração exata do IFPI - geralmente alinhado à esquerda na NBR 6023). Espaçamento simples entre as linhas da mesma referência, e espaçamento de uma linha em branco (ou 12pt) entre referências distintas.
* **Apêndices e Anexos:** O agente deve criar comandos ou usar o pacote `appendix` para transição correta da nomenclatura (ex: "APÊNDICE A - Título").
Manual_LaTeX_IA_TCC_IFPI.md
Exibindo Manual_LaTeX_IA_TCC_IFPI.md.
