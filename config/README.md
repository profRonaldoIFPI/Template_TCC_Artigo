# Diretório de Configurações (`config/`)

Este diretório contém os arquivos responsáveis por definir a classe do documento, carregar pacotes adicionais e aplicar as regras de estilo e identidade visual exigidas pelo IFPI.

## Conteúdo do Diretório

- **`config.tex`**: Arquivo de configuração geral do LaTeX. Define a classe do documento (baseada em `abntex2` adaptada para artigos), carrega pacotes fundamentais e configura opções gerais como cores de hiperlinks e metadados básicos.
- **`abntex-ifpi.sty`**: Arquivo de estilo do LaTeX (`.sty`). Contém as definições de formatação específicas da instituição (cabeçalhos, capas, folha de rosto, estilo de citações ABNT NBR 10520:2023, espaçamentos e fontes).

---

## O que se pode ou deve alterar?

### 🟢 `config.tex` (Pode ser alterado)
Você **pode e deve** alterar este arquivo para:
- **Carregar pacotes adicionais**: Se o seu artigo necessitar de pacotes específicos para desenhar diagramas (ex: `tikz`), inserir fórmulas matemáticas complexas (ex: `amsmath`, `amssymb`), criar tabelas mais elaboradas (ex: `booktabs`, `makecell`) ou formatar algoritmos e códigos-fonte (ex: `listings`, `algorithm2e`).
- **Definir comandos personalizados**: Criar atalhos ou macros personalizadas para facilitar a digitação de termos repetitivos ou fórmulas matemáticas específicas da sua pesquisa.

### 🟡 `abntex-ifpi.sty` (Alterar com Cuidado)
Este arquivo implementa o design system e a normalização técnica do template. Você **só deve** alterá-lo se:
- Houver alguma atualização ou correção necessária na estrutura de citações ou referências bibliográficas.
- A coordenação do curso ou biblioteca do IFPI alterar regras específicas de espaçamento, margem ou fontes do modelo de artigo.
- Quiser personalizar algum aspecto visual profundo que não seja contemplado pelas opções padrão.
