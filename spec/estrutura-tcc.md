# Estrutura do TCC (Formato Artigo Científico)

Este documento define a estrutura completa de seções, subseções e elementos do TCC em formato de artigo científico para o IFPI Campus Floriano. A definição baseia-se na harmonização entre as diretrizes do **Manual de Normalização de Trabalhos Acadêmicos do IFPI (2024)** e a estrutura implementada no arquivo [artigo.tex](file:///home/rpb/Repositórios/Template_TCC_Artigo/artigo.tex), priorizando o Manual do IFPI em caso de quaisquer divergências.

---

## 1. Tabela Comparativa e Visão Geral da Estrutura

| Elemento | Tipo | Detalhes / Regras (Manual do IFPI) | Arquivo Relacionado |
| :--- | :--- | :--- | :--- |
| **Capa** | Obrigatório | Logomarca do IFPI, Instituição, Campus, Curso, Autor, Título, Local e Ano. | [pre_textuais.tex](file:///home/rpb/Repositórios/Template_TCC_Artigo/estrutura/pre_textuais.tex) |
| **Folha de Rosto** | Obrigatório | Autor, Título, Natureza do trabalho (Preâmbulo), Orientador, Local e Ano. | [pre_textuais.tex](file:///home/rpb/Repositórios/Template_TCC_Artigo/estrutura/pre_textuais.tex) |
| **Cabeçalho do Artigo** | Obrigatório | Título (e subtítulo se houver), Autor, Orientador e Coorientador (notas de rodapé com e-mail/vínculo). | [pre_textuais.tex](file:///home/rpb/Repositórios/Template_TCC_Artigo/estrutura/pre_textuais.tex) |
| **Resumo** | Obrigatório | De 150 a 250 palavras, sem citações/siglas, com 3 a 5 palavras-chave. | [pre_textuais.tex](file:///home/rpb/Repositórios/Template_TCC_Artigo/estrutura/pre_textuais.tex) |
| **Abstract** | Obrigatório | Resumo traduzido para o inglês, contendo keywords de 3 a 5 termos. | [pre_textuais.tex](file:///home/rpb/Repositórios/Template_TCC_Artigo/estrutura/pre_textuais.tex) |
| **Data de Aprovação** | Obrigatório | Formato `dia, mês e ano` (ex: 30/06/2026), posicionado logo abaixo das Keywords/Abstract. | [pre_textuais.tex](file:///home/rpb/Repositórios/Template_TCC_Artigo/estrutura/pre_textuais.tex) |
| **Introdução** | Obrigatório | Contextualização, problemática, justificativa, objetivos e metodologia resumida. | [artigo.tex (L41)](file:///home/rpb/Repositórios/Template_TCC_Artigo/artigo.tex#L41) |
| **Desenvolvimento** | Obrigatório | Subdividido em Referencial Teórico, Metodologia e Resultados. | [artigo.tex (L47)](file:///home/rpb/Repositórios/Template_TCC_Artigo/artigo.tex#L47) |
| **Considerações Finais** | Obrigatório | Afirmação sintética baseada nos objetivos, sem ferir os direitos humanos. | [artigo.tex (L202)](file:///home/rpb/Repositórios/Template_TCC_Artigo/artigo.tex#L202) |
| **Referências** | Obrigatório | Obras citadas no texto, ordenadas alfabeticamente com espaçamento simples. | [pos_textuais.tex](file:///home/rpb/Repositórios/Template_TCC_Artigo/estrutura/pos_textuais.tex) |
| **Glossário** | Opcional | Lista alfabética para esclarecimento de termos obscuros. | [pos_textuais.tex](file:///home/rpb/Repositórios/Template_TCC_Artigo/estrutura/pos_textuais.tex) |
| **Apêndices** | Opcional | Materiais elaborados pelo próprio autor (APÊNDICE A - TÍTULO). | [pos_textuais.tex](file:///home/rpb/Repositórios/Template_TCC_Artigo/estrutura/pos_textuais.tex) |
| **Anexos** | Opcional | Materiais de terceiros não elaborados pelo autor (ANEXO A - TÍTULO). | [pos_textuais.tex](file:///home/rpb/Repositórios/Template_TCC_Artigo/estrutura/pos_textuais.tex) |
| **Índice** | Opcional | Relação de termos ordenados para localização no texto. | [pos_textuais.tex](file:///home/rpb/Repositórios/Template_TCC_Artigo/estrutura/pos_textuais.tex) |
| **Agradecimentos** | Opcional | Último elemento pós-textual. Texto curto dirigido aos colaboradores. | [pos_textuais.tex](file:///home/rpb/Repositórios/Template_TCC_Artigo/estrutura/pos_textuais.tex) |

---

## 2. Detalhamento e Regras dos Elementos

### 2.1. Elementos Pré-Textuais

1. **Autoria Individual**:
   - Conforme a Resolução Normativa nº 180/2023, o TCC deve ser realizado individualmente. Deve constar apenas **um único autor** com nome e sobrenome de forma direta.
2. **Resumo e Abstract**:
   - Fonte Arial ou Times, tamanho 12, espaçamento simples, parágrafo único (sem recuo na primeira linha).
   - **Tamanho**: Entre 150 e 250 palavras.
   - **Palavras-chave / Keywords**: De 3 a 5 descritores, grafados em letras minúsculas (exceto siglas, nomes próprios ou científicos), separados por ponto e vírgula (`;`) e finalizados por ponto (`.`).
3. **Data de Aprovação**:
   - Elemento obrigatório posicionado imediatamente abaixo do Abstract/Keywords.

### 2.2. Elementos Textuais

O corpo do artigo deve ser escrito com fonte tamanho 12, espaçamento 1,5 entre linhas (configurado automaticamente no pacote `abntex-ifpi.sty`), e parágrafos com recuo de `1.25cm` na primeira linha.

#### 1. INTRODUÇÃO
Seção primária de abertura. Deve delimitar o tema, conter a questão de pesquisa/problemática, os objetivos (geral e específicos) e a justificativa da relevância do estudo de forma fluida no texto.

#### 2. REFERENCIAL TEÓRICO (Desenvolvimento - Parte 1)
Fundamentação teórica que dá suporte lógico ao trabalho. Recomenda-se subdividir em temas conceituais e estudos relacionados:
- `\subsection{Fundamentação Teórica}` (Subtópico para conceitos chaves e autores clássicos).
- `\subsection{Estudos Relacionados}` (Revisão da literatura recente).

#### 3. METODOLOGIA (Desenvolvimento - Parte 2)
Detalhamento de como a pesquisa foi executada. Deve conter:
- `\subsection{Caracterização da Pesquisa}`: Classificação quanto aos objetivos, abordagem e procedimentos técnicos.
- `\subsection{População e Amostra}`: Universo do estudo e técnica de amostragem.
- `\subsection{Coleta de Dados}`: Descrição das ferramentas de coleta (questionários, entrevistas, logs, etc.).
- `\subsection{Análise de Dados}`: Como as informações coletadas foram tratadas (estatística descritiva, análise de conteúdo, etc.).
- `\subsection{Aspectos Éticos}`: Atendimento aos comitês de ética e uso do Termo de Consentimento Livre e Esclarecido (TCLE), se aplicável.

#### 4. RESULTADOS E DISCUSSÃO (Desenvolvimento - Parte 3)
Apresentação dos dados obtidos seguidos pela confrontação analítica com a literatura levantada no Referencial Teórico.

#### 5. CONSIDERAÇÕES FINAIS
Síntese das conclusões alcançadas relacionando-as diretamente com os objetivos propostos na Introdução, indicando as limitações e sugestões para trabalhos futuros.

### 2.3. Elementos Pós-Textuais (Ordenação Rigorosa)

O Manual de Normalização do IFPI prescreve que os elementos pós-textuais devem seguir obrigatoriamente a ordem abaixo:

1. **Referências** (Obrigatório):
   - Alinhadas à margem esquerda, com espaçamento simples e separadas entre si por uma linha em branco.
2. **Glossário** (Opcional):
   - Ordenado alfabeticamente. Título centralizado, caixa alta e negrito (`\chapter*{GLOSSÁRIO}`).
3. **Apêndice** (Opcional):
   - Documentos elaborados pelo próprio autor. Identificados por letras maiúsculas consecutivas, travessão e título (ex: `APÊNDICE A – QUESTIONÁRIO`).
4. **Anexo** (Opcional):
   - Documentos produzidos por terceiros. Identificados por letras maiúsculas consecutivas, travessão e título (ex: `ANEXO A – LEGISLAÇÃO`).
5. **Índice** (Opcional):
   - Relação remissiva de termos.
6. **Agradecimentos** (Opcional):
   - Por ser um formato de artigo científico, os agradecimentos devem constar obrigatoriamente como o **último elemento pós-textual**, e não nas páginas iniciais como ocorre em monografias. Título centralizado, caixa alta e negrito (`\chapter*{AGRADECIMENTOS}`).
