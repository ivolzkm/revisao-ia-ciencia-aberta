
# Revisão Rápida da Literatura com IA (SciELO)

Ferramenta em Python para buscar e extrair artigos do **SciELO** (repositório de ciência aberta) sobre temas em saúde pública, com foco em **inteligência artificial**.

## Objetivo
Automatizar a **triagem inicial** de literatura para revisões rápidas, apoiando projetos de **Ciência Aberta no Brasil**.

## Funcionalidades
- Busca por palavras-chave
- Extrai: Título, Autores, Resumo, Link
- Salva em CSV (pronto para análise com pandas, LLMs ou Zotero)

## Como usar
```bash
pip install requests beautifulsoup4 pandas
python scraper_scielo.py
```

## Exemplo de saída
```csv
Título,Autores,Resumo,Link
"IA na epidemiologia...", "Silva, J.; Souza, M.", "Estudo sobre uso de ML em...", "https://..."
```

## Tecnologias
- Python
- BeautifulSoup
- pandas
- SciELO Search API

---
Desenvolvido por Ivo Ricardo Lozekam Junior | UFCSPA | 2025
```

