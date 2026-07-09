# Diretório de Imagens e Figuras (`img/`)

Este diretório armazena todos os arquivos de imagem, ilustrações, gráficos, diagramas e logos que serão incorporados ao corpo do seu artigo científico.

## Conteúdo do Diretório

- **Logotipos do IFPI**: Versões do logo institucional em formato PNG para uso na capa e nos cabeçalhos (`Logo-IFPI-Floriano-Horizontal.png`, `Logo-IFPI-Floriano-Vertical.png` e `Logo-IFPI-IF.png`).
- **Imagens de Exemplo**: Figuras de exemplo utilizadas para demonstrar o uso do comando `\includegraphics{}` no arquivo `artigo.tex`.

---

## O que se pode ou deve alterar?

### 🟢 O que pode ser alterado/adicionado:
- **Novas Figuras e Gráficos**: Salve aqui todas as imagens, gráficos, capturas de tela e fluxogramas que você utilizará em seu artigo científico. Formatos recomendados:
  - **Gráficos e esquemas**: Dê preferência a formatos vetoriais como **PDF** ou **EPS** para garantir máxima nitidez durante a impressão.
  - **Fotografias e capturas de tela**: Use formatos rasterizados como **PNG** (para capturas de tela e interfaces) ou **JPEG** (para fotos reais).
- **Logotipos**: Se você estuda em outro campus que não seja Floriano, adicione as imagens de logotipo do seu respectivo campus mantendo o padrão ou atualize o caminho correspondente em `config/abntex-ifpi.sty` ou `estrutura/pre_textuais.tex`.

### ⚠️ Recomendações de Organização:
- Utilize nomes de arquivos simples, curtos e sem espaços ou caracteres especiais (ex: em vez de `Foto do Experimento 1.png`, prefira `experimento_01.png` ou `experimento01.png`). Isso evita erros na compilação do LaTeX.
- As imagens devem ser chamadas no código LaTeX usando o caminho relativo `img/nome_da_imagem`.
