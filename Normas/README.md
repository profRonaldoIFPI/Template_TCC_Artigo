# Diretório de Normas e Referências (`Normas/`)

Este diretório reúne as versões oficiais das normas técnicas da **Associação Brasileira de Normas Técnicas (ABNT)**, as diretrizes de apresentação tabular do **IBGE**, o **Manual de Normalização de Trabalhos Acadêmicos do IFPI (2024)** e os **Modelos Oficiais de Artigo (DOCX e PDF)** disponibilizados pelo IFPI.

Esses documentos constituem a base regulatória e técnica utilizada para projetar, validar e manter a conformidade do **Template LaTeX para Trabalho de Conclusão de Curso (TCC) no formato Artigo Científico do IFPI**.

---

## 📑 Descrição Detalhada dos Arquivos

Abaixo é descrito o conteúdo, o escopo e a aplicação prática de cada arquivo presente neste diretório:

---

### 1. [`Manual de Normalização de Trabalho Acadêmicos do IFPI [2024].pdf`](<./Manual de Normalização de Trabalho Acadêmicos do IFPI [2024].pdf>)

* **Órgão Emissor:** Instituto Federal de Educação, Ciência e Tecnologia do Piauí (IFPI)
* **Ano / Edição:** 2024 (Edição revisada e atualizada)
* **Finalidade no Projeto:**
  * É a principal diretriz institucional do trabalho, aplicando as normas ABNT à realidade dos cursos do IFPI.
  * Define as exigências estruturais e normativas para Trabalhos de Conclusão de Curso (TCC), incluindo a modalidade de **Artigo Científico**.
  * Determina a inclusão obrigatória de elementos pré-textuais institucionais (**Capa** e **Folha de Rosto** do IFPI), mesmo na modalidade de artigo.
  * Fixa as exigências para o cabeçalho do artigo, **Resumo** na língua vernácula e **Abstract** em língua estrangeira (ambos com espaçamento entrelinhas simples 1,0 e indicação da data de aprovação), palavras-chave separadas por ponto e vírgula, e regras de formatação tipográfica e margens (3 cm superior/esquerda e 2 cm inferior/direita).

---

### 2. [`Modelo Artigo IFPI.docx`](<./Modelo Artigo IFPI.docx>) e [`Modelo Artigo IFPI.pdf`](<./Modelo Artigo IFPI.pdf>)

* **Órgão Emissor:** Instituto Federal do Piauí (IFPI) / Coordenações de Curso
* **Formato:** DOCX (Microsoft Word) e PDF
* **Finalidade no Projeto:**
  * Modelos referenciais oficiais fornecidos pelas coordenações do IFPI para orientar os alunos na elaboração de TCCs em formato de artigo científico.
  * Servem como **gabarito visual e estrutural** para demonstrar o layout esperado pela instituição: cabeçalho inicial, identificação dos autores e orientador, filiação institucional, disposição do resumo/abstract, títulos de seções em fluxo contínuo e formatação de ilustrações e tabelas.
  * Foram utilizados diretamente para calibrar os espaçamentos, fontes e layout deste template em LaTeX.

---

### 3. [`ABNT NBR 14724: Trabalhos acadêmicos_4ª edição [2024].pdf`](<./ABNT NBR 14724: Trabalhos acadêmicos_4ª edição [2024].pdf>)

* **Órgão Emissor:** Associação Brasileira de Normas Técnicas (ABNT)
* **Título Oficial:** *Informação e documentação — Trabalhos acadêmicos — Apresentação*
* **Ano / Edição:** 2024 (4ª edição)
* **Finalidade no Projeto:**
  * Estabelece os princípios fundamentais para a apresentação de trabalhos acadêmicos no Brasil (papel A4, margens de 3 cm superior e esquerda e 2 cm inferior e direita, paginação e regras tipográficas).
  * Regula a paginação: a contagem inicia na folha de rosto, mas a numeração só deve aparecer expressa a partir da primeira folha textual (Introdução), no canto superior direito.
  * Orienta a apresentação de ilustrações, tabelas, equações, apêndices e anexos.

---

### 4. [`ABNT NBR 10520: Citações em documentos_2ª edição [2023].pdf`](<./ABNT NBR 10520: Citações em documentos_2ª edição [2023].pdf>)

* **Órgão Emissor:** Associação Brasileira de Normas Técnicas (ABNT)
* **Título Oficial:** *Informação e documentação — Citações em documentos — Apresentação*
* **Ano / Edição:** 2023 (2ª edição)
* **Finalidade no Projeto:**
  * Padroniza o modo de apresentação de citações diretas (curtas e longas com recuo de 4 cm e fonte reduzida), indiretas e citações de citação (*apud*).
  * **Atualização Crítica (2023):** Determina que as chamadas autor-data entre parênteses no texto devem ser grafadas em **letras maiúsculas e minúsculas** (ex.: `(Silva, 2023)`) e não mais em caixa-alta (`(SILVA, 2023)`). O template já está plenamente configurado e auditado para essa norma.

---

### 5. [`ABNT NBR 6023: Referencias_2ª edição v2 [2020].pdf`](<./ABNT NBR 6023: Referencias_2ª edição v2 [2020].pdf>)

* **Órgão Emissor:** Associação Brasileira de Normas Técnicas (ABNT)
* **Título Oficial:** *Informação e documentação — Referências — Elaboração*
* **Ano / Edição:** 2018 / 2020 (2ª edição corrigida)
* **Finalidade no Projeto:**
  * Define os elementos essenciais e complementares para a lista de referências bibliográficas (livros, artigos de periódicos, teses, websites, legislação, patentes, etc.).
  * Estabelece o alinhamento à margem esquerda, espaçamento entrelinhas simples dentro de cada referência e espaço de uma linha em branco entre referências sucessivas.
  * Regula a conversão correta dos autores para CAIXA ALTA na lista de referências, implementada pelo motor `abntex2cite`.

---

### 6. [`ABNT NBR 6024: Numeração progressiva das seções de um documento_2ª Edição [2012].pdf`](<./ABNT NBR 6024: Numeração progressiva das seções de um documento_2ª Edição [2012].pdf>)

* **Órgão Emissor:** Associação Brasileira de Normas Técnicas (ABNT)
* **Título Oficial:** *Informação e documentação — Numeração progressiva das seções de um documento escrito — Apresentação*
* **Ano / Edição:** 2012 (2ª edição)
* **Finalidade no Projeto:**
  * Estabelece a numeração progressiva das seções do artigo (`1`, `1.1`, `1.1.1`, etc.).
  * Define a tipografia e a hierarquia visual dos títulos das seções.
  * Exige que títulos sem indicativo numérico (como as Referências, Agradecimentos, Apêndices e Anexos) sejam centralizados e destacados tipograficamente.

---

### 7. [`Normas de apresentação tabular - IBGE_3ª edição [1993].pdf`](<./Normas de apresentação tabular - IBGE_3ª edição [1993].pdf>)

* **Órgão Emissor:** Instituto Brasileiro de Geografia e Estatística (IBGE)
* **Título Oficial:** *Normas de apresentação tabular*
* **Ano / Edição:** 1993 (3ª edição)
* **Finalidade no Projeto:**
  * Norma oficial brasileira adotada pela ABNT para construção gráfica de **Tabelas** em trabalhos científicos.
  * Define que tabelas contêm predominantemente dados numéricos e estatísticos, topo e base delimitados por linhas horizontais, com laterais abertas (sem bordas verticais externas).
  * Estabelece a distinção conceitual em relação aos **Quadros** (que possuem moldura fechada e conteúdo prioritariamente textual ou conceitual).

---

### 8. [`ABNT NBR 15287: Projeto de pesquisa_3ª edição [2025].pdf`](<./ABNT NBR 15287: Projeto de pesquisa_3ª edição [2025].pdf>)

* **Órgão Emissor:** Associação Brasileira de Normas Técnicas (ABNT)
* **Título Oficial:** *Informação e documentação — Projeto de pesquisa — Apresentação*
* **Ano / Edição:** 2025 (3ª edição)
* **Finalidade no Projeto:**
  * Norma voltada a projetos de pesquisa acadêmicos.
  * Mantida neste acervo como **documento de apoio e consulta prévia**, permitindo que estudantes e orientadores consultem o projeto de pesquisa original que antecedeu a execução e escrita do TCC.

---

### 9. [`ABNT NBR 6027: Sumario_2ª edição [2012].pdf`](<./ABNT NBR 6027: Sumario_2ª edição [2012].pdf>)

* **Órgão Emissor:** Associação Brasileira de Normas Técnicas (ABNT)
* **Título Oficial:** *Informação e documentação — Sumário — Apresentação*
* **Ano / Edição:** 2012 (2ª edição)
* **Finalidade no Projeto:**
  * Fixa os requisitos para elaboração de sumários em trabalhos acadêmicos convencionais.
  * Mantida como documento de referência normativa geral. Vale salientar que, no formato de **Artigo Científico** (conforme a NBR 6022 e as diretrizes do IFPI), o texto possui fluxo contínuo e **não utiliza sumário**.

---

## 🛠️ Guia de Uso e Manutenção

> [!IMPORTANT]
> Este diretório tem caráter exclusivo de **consulta técnica e auditoria normativa**. Nenhum arquivo contido aqui interfere no processo de compilação do LaTeX ou na geração do `artigo.pdf`.

### 🟢 O que pode ser alterado ou adicionado

* **Novas Normas e Resoluções:** Caso o IFPI publique portarias ou atualizações do regulamento de TCC, ou a ABNT lance revisões das NBRs, os novos arquivos em PDF podem ser inseridos aqui para manter o repositório como acervo confiável e atualizado.
* **Critérios da Banca / Editais:** Modelos de formulários de avaliação ou instruções complementares de submissão específicas do seu campus ou comissão de TCC.

### 🔴 O que NÃO deve ser alterado

* Não exclua nem renomeie as normas técnicas e manuais vigentes, pois os nomes identificam de forma clara e padronizada os documentos de referência utilizados pelo template e pelo script de verificação de conformidade.

