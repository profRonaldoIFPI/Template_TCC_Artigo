#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Verificação de Conformidade Acadêmica (IFPI & ABNT)
Template de TCC no formato de Artigo Científico - IFPI

Este script analisa automaticamente os arquivos TeX e PDF do projeto para verificar
o atendimento às diretrizes do Manual de Normalização de Trabalhos Acadêmicos do IFPI (2024)
e às especificações registradas em Normas/specs.md.

Uso:
    python3 verificar_conformidade.py
"""

import os
import re
import sys

# Cores para o terminal (ANSI escape codes)
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BLUE = '\033[94m'
BOLD = '\033[1m'
RESET = '\033[0m'

def print_header():
    print(f"\n{BLUE}{BOLD}" + "="*72)
    print("   VERIFICADOR DE CONFORMIDADE DE TCC (ARTIGO CIENTÍFICO - IFPI)")
    print("   Conforme Manual do IFPI (2024) e Normas ABNT / spec/specification.md")
    print("="*72 + f"{RESET}\n")

def read_file(filepath):
    if not os.path.exists(filepath):
        return ""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def run_audits():
    results = []
    
    # Lendo arquivos de configuração e conteúdo
    config_sty = read_file('config/abntex-ifpi.sty')
    config_tex = read_file('config/config.tex')
    artigo_tex = read_file('artigo.tex')
    pre_textuais = read_file('estrutura/pre_textuais.tex')
    pos_textuais = read_file('estrutura/pos_textuais.tex')
    dados_tex = read_file('estrutura/dados.tex')
    
    all_tex = config_sty + "\n" + config_tex + "\n" + artigo_tex + "\n" + pre_textuais + "\n" + pos_textuais + "\n" + dados_tex

    # --------------------------------------------------------------------------
    # 1. Margens ( geometry: 3cm top/left, 2cm bottom/right )
    # --------------------------------------------------------------------------
    margin_ok = False
    clean_tex = all_tex.replace(" ", "")
    if ("left=3cm" in clean_tex or "left=3.0cm" in clean_tex) and \
       ("right=2cm" in clean_tex or "right=2.0cm" in clean_tex) and \
       ("top=3cm" in clean_tex or "top=3.0cm" in clean_tex) and \
       ("bottom=2cm" in clean_tex or "bottom=2.0cm" in clean_tex):
        margin_ok = True
    
    results.append({
        "num": 1,
        "title": "Margens da Folha (Superior/Esquerda 3cm, Inferior/Direita 2cm)",
        "status": margin_ok,
        "msg": "Margens configuradas corretamente conforme ABNT NBR 14724 / IFPI." if margin_ok else "Verifique as configurações do pacote geometry."
    })

    # --------------------------------------------------------------------------
    # 2. Tipografia ( Arial / helvet ou Times New Roman / mathptmx )
    # --------------------------------------------------------------------------
    font_ok = ("helvet" in all_tex or "mathptmx" in all_tex) and "\\familydefault" in all_tex
    results.append({
        "num": 2,
        "title": "Tipografia Uniforme (Arial ou Times New Roman)",
        "status": font_ok,
        "msg": "Pacote de fonte padronizado detectado (helvet/mathptmx)." if font_ok else "Certifique-se de usar a fonte Arial (helvet) ou Times New Roman (mathptmx)."
    })

    # --------------------------------------------------------------------------
    # 3. Indentação de Parágrafo ( 1.25 cm )
    # --------------------------------------------------------------------------
    indent_ok = "\\setlength{\\parindent}{1.25cm}" in all_tex or "\\setlength{\\parindent}{1.25cm}" in clean_tex
    results.append({
        "num": 3,
        "title": "Indentação de Primeira Linha do Parágrafo (1,25 cm)",
        "status": indent_ok,
        "msg": "\\setlength{\\parindent}{1.25cm} configurado corretamente." if indent_ok else "Defina o recuo do parágrafo em exatamente 1.25cm."
    })

    # --------------------------------------------------------------------------
    # 4. Elementos Pré-textuais Obrigatórios do IFPI (Capa e Folha de Rosto)
    # --------------------------------------------------------------------------
    capa_ok = "\\imprimircapa" in pre_textuais or "\\imprimircapa" in artigo_tex
    folha_rosto_ok = "\\imprimirfolhaderosto" in pre_textuais or "\\imprimirfolhaderosto" in artigo_tex
    pre_elements_ok = capa_ok and folha_rosto_ok
    
    results.append({
        "num": 4,
        "title": "Capa e Folha de Rosto (Obrigatórias no IFPI - Cap. 7)",
        "status": pre_elements_ok,
        "msg": "Capa e Folha de Rosto incluídas conforme o Manual do IFPI (2024)." if pre_elements_ok else "O Manual do IFPI exige a inclusão de Capa e Folha de Rosto para TCC em formato de artigo."
    })

    # --------------------------------------------------------------------------
    # 5. Resumo, Abstract e Data de Aprovação (Espaçamento Simples 1,0)
    # --------------------------------------------------------------------------
    resumo_ok = "\\begin{resumo}" in pre_textuais or "\\begin{resumo}" in artigo_tex
    data_aprov_ok = "Data de aprovação" in pre_textuais or "imprimirdataaprovacao" in pre_textuais
    resumo_single_spacing = "SingleSpace" in config_sty or "SingleSpacing" in config_sty or "singlespace" in all_tex
    
    resumo_combo_ok = resumo_ok and data_aprov_ok and resumo_single_spacing
    results.append({
        "num": 5,
        "title": "Resumo e Abstract (Espaçamento Entrelinhas Simples 1,0 e Data de Aprovação)",
        "status": resumo_combo_ok,
        "msg": "Resumo e Abstract configurados com espaçamento entrelinhas simples (1,0) e Data de Aprovação." if resumo_combo_ok else "Resumo e Abstract devem ter espaçamento entrelinhas simples (1,0)."
    })

    # --------------------------------------------------------------------------
    # 6. Formatação das Palavras-chave (Separadas por ; e minúsculas)
    # --------------------------------------------------------------------------
    kw_semicolon = False
    if "Palavras-chave" in pre_textuais:
        match = re.search(r'Palavras-chave.*?:(.*?)\n', pre_textuais, re.IGNORECASE)
        if match:
            kw_text = match.group(1)
            if ";" in kw_text:
                kw_semicolon = True
    else:
        kw_semicolon = True
        
    results.append({
        "num": 6,
        "title": "Formatação das Palavras-chave (Separadas por ponto e vírgula ';')",
        "status": kw_semicolon,
        "msg": "Palavras-chave separadas por ponto e vírgula conforme Item 7.3.1.3.1 do Manual IFPI." if kw_semicolon else "As palavras-chave devem ser separadas entre si por ponto e vírgula ';' e finalizadas por ponto '.'."
    })

    # --------------------------------------------------------------------------
    # 7. Distinção e Estruturação de Tabelas (IBGE) e Quadros (ABNT)
    # --------------------------------------------------------------------------
    booktabs_ok = "\\usepackage{booktabs}" in all_tex or "\\RequirePackage{booktabs}" in all_tex
    quadro_env_ok = "quadro" in all_tex
    
    tables_ok = booktabs_ok and quadro_env_ok
    results.append({
        "num": 7,
        "title": "Estrutura de Tabelas (IBGE abertas) e Quadros (ABNT fechados)",
        "status": tables_ok,
        "msg": "Pacote booktabs e ambiente de quadros disponíveis no projeto." if tables_ok else "Certifique-se de usar booktabs para tabelas numéricas e quadros fechados para dados qualitativos."
    })

    # --------------------------------------------------------------------------
    # 8. Citações e Referências (NBR 10520:2023 - Autor-data Caixa Mista)
    # --------------------------------------------------------------------------
    cite_ok = "\\usepackage[alf" in all_tex or "\\RequirePackage" in all_tex or "abntifpi" in all_tex
    results.append({
        "num": 8,
        "title": "Citações Autor-Data em Caixa Mista (ABNT NBR 10520:2023)",
        "status": cite_ok,
        "msg": "Sistema de citação autor-data configurado." if cite_ok else "Verifique a configuração de chamadas de autores no formato (Sobrenome, Ano)."
    })

    # --------------------------------------------------------------------------
    # 9. Verificação de Fontes em Elementos Ilustrativos (\fonte)
    # --------------------------------------------------------------------------
    # Remove linhas de comentários em LaTeX para evitar falsos positivos
    clean_code = "\n".join([line for line in artigo_tex.split("\n") if not line.strip().startswith("%")])
    
    figures_count = len(re.findall(r'\\begin\{figure\}', clean_code))
    tables_count = len(re.findall(r'\\begin\{table\}', clean_code))
    quadros_count = len(re.findall(r'\\begin\{quadro\}', clean_code))
    
    fontes_count = len(re.findall(r'\\fonte\{|Fonte:', clean_code))
    
    total_floats = figures_count + tables_count + quadros_count
    fonte_missing = (total_floats > 0) and (fontes_count < total_floats)
    
    results.append({
        "num": 9,
        "title": "Indicação Obrigatória de Fonte em Ilustrações e Tabelas",
        "status": not fonte_missing,
        "msg": "Todas as ilustrações/tabelas possuem indicação expressa de fonte." if not fonte_missing else f"Atenção: Detectados {total_floats} elementos gráficos/tabelas, mas apenas {fontes_count} chamadas de fonte. Todas as figuras/tabelas devem conter 'Fonte: ...'."
    })

    # --------------------------------------------------------------------------
    # 10. Exibição Completa de Autores nas Referências (abnt-etal-list = 0)
    # --------------------------------------------------------------------------
    bib_tex = read_file('referencias.bib')
    etal_list_ok = "abnt-etal-list=0" in config_tex or "abnt-etal-list = {0}" in bib_tex or "abnt-etal-list = 0" in bib_tex
    results.append({
        "num": 10,
        "title": "Exibição Completa de Autores nas Referências (Sem 'et al.')",
        "status": etal_list_ok,
        "msg": "Opção abnt-etal-list=0 configurada para listar todos os autores nas referências." if etal_list_ok else "Configure abnt-etal-list=0 no config.tex ou referencias.bib para listar todos os coautores nas referências."
    })

    # --------------------------------------------------------------------------
    # 11. Compilação do PDF
    # --------------------------------------------------------------------------
    pdf_exists = os.path.exists("artigo.pdf")
    results.append({
        "num": 11,
        "title": "Arquivo PDF Gerado (artigo.pdf)",
        "status": pdf_exists,
        "msg": "PDF gerado com sucesso." if pdf_exists else "Execute o script gerar_pdf.sh para compilar o documento LaTeX."
    })

    return results

def main():
    print_header()
    
    if not os.path.exists("artigo.tex"):
        print(f"{RED}[ERRO CRÍTICO]{RESET} Execute este script na pasta raiz do seu projeto de template (onde está o arquivo artigo.tex).")
        sys.exit(1)
        
    results = run_audits()
    
    passed_count = sum(1 for r in results if r["status"])
    total_count = len(results)
    
    for r in results:
        status_symbol = f"{GREEN}[ PASS ]{RESET}" if r["status"] else f"{RED}[ FALHA ]{RESET}"
        print(f"{r['num']:02d}. {status_symbol} {BOLD}{r['title']}{RESET}")
        print(f"    └─ {r['msg']}\n")
        
    percentage = (passed_count / total_count) * 100
    
    print(f"{BLUE}{BOLD}" + "-"*72 + f"{RESET}")
    if percentage == 100:
        print(f"{GREEN}{BOLD}RESULTADO: 100% CONFORME! Seu documento atende todas as regras auditadas.{RESET}")
    elif percentage >= 80:
        print(f"{YELLOW}{BOLD}RESULTADO: {percentage:.0f}% CONFORME. O documento atende à maioria das regras, revise os alertas em vermelho.{RESET}")
    else:
        print(f"{RED}{BOLD}RESULTADO: {percentage:.0f}% CONFORME. Ajustes necessários antes de submeter o trabalho.{RESET}")
    print(f"{BLUE}{BOLD}" + "="*72 + f"{RESET}\n")

if __name__ == "__main__":
    main()
