# Diretório de Estrutura Modular (`estrutura/`)

Este diretório contém os componentes modulares do artigo científico estruturados em arquivos LaTeX específicos. A divisão facilita a organização do projeto separando dados, elementos pré-textuais e elementos pós-textuais do corpo do artigo (que fica concentrado no arquivo `artigo.tex` na raiz).

## Conteúdo do Diretório

- **`dados.tex`**: Arquivo de metadados do artigo. Armazena as variáveis de autoria, orientação, título e dados institucionais.
- **`pre_textuais.tex`**: Estrutura a capa institucional, folha de rosto, cabeçalho de artigo, resumos (resumo em português, abstract em inglês) e a data de aprovação.
- **`pos_textuais.tex`**: Gerencia os elementos finais do trabalho que sucedem o desenvolvimento: referências bibliográficas, glossário, apêndices, anexos e agradecimentos.

---

## O que se pode ou deve alterar?

### 🔴 `dados.tex` (DEVE SER ALTERADO)
Este é o primeiro arquivo que todo aluno **deve preencher obrigatoriamente** ao iniciar o trabalho.
- Substitua os dados de exemplo pelas suas informações reais:
  - Título e subtítulo.
  - Nome completo e e-mail.
  - Nome completo do Orientador (e Coorientador, se houver), e-mails e vínculos institucionais.
  - Curso, campus, localidade e ano de defesa.

### 🟢 `pre_textuais.tex` (Deve ser alterado)
Contém os elementos textuais iniciais do artigo:
- **Resumo e Abstract**: Escreva aqui o resumo do seu artigo (entre 150 e 250 palavras) e a tradução correspondente em inglês.
- **Palavras-chave e Keywords**: Altere para as palavras-chave que melhor representam o seu tema (de 3 a 5 termos, separados por ponto e vírgula `;`).
- **Data de Aprovação**: Atualize com a data real da sua defesa de TCC.

### 🟢 `pos_textuais.tex` (Pode ser alterado)
Controla a exibição e o conteúdo dos elementos pós-textuais opcionais:
- **Glossário**: Ative e edite caso seu trabalho faça uso de termos muito específicos ou técnicos de difícil compreensão.
- **Apêndices**: Adicione arquivos ou textos de sua própria autoria que complementem a pesquisa (ex: questionários aplicados, roteiro de entrevistas estruturadas).
- **Anexos**: Insira documentos ou materiais de terceiros que sirvam de comprovação ou ilustração (ex: autorizações, leis, prints de telas de sistemas terceiros).
- **Agradecimentos**: Edite o texto de agradecimentos (que no modelo de artigo científico do IFPI deve constar como o último elemento pós-textual).
- *Nota: Caso não use algum elemento opcional (como Apêndices ou Anexos), basta comentar ou remover a respectiva linha neste arquivo.*
