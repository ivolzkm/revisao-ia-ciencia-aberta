# scraper_scielo.py
# Ferramenta para revisão rápida da literatura em SciELO (Ciência Aberta + Saúde)
# Autor: [SEU NOME]
# GitHub: [seu-user]

import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

def buscar_artigos_scielo(termo, max_paginas=2):
    """
    Busca artigos no SciELO por termo e extrai título, autores e resumo.
    Ex: termo = "inteligência artificial saúde"
    """
    base_url = "https://search.scielo.org/"
    artigos = []

    for pagina in range(1, max_paginas + 1):
        params = {
            'q': termo,
            'lang': 'pt',
            'page': pagina,
            'format': 'summary'
        }
        try:
            response = requests.get(base_url, params=params, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            for item in soup.select('.item'):
                titulo_tag = item.select_one('.line a')
                autores_tag = item.select_one('.authors')
                resumo_tag = item.select_one('.summary')

                if titulo_tag:
                    titulo = titulo_tag.get_text(strip=True)
                    link = "https://search.scielo.org" + titulo_tag['href']
                    autores = autores_tag.get_text(strip=True) if autores_tag else "N/A"
                    resumo = resumo_tag.get_text(strip=True)[:500] + "..." if resumo_tag else "N/A"

                    artigos.append({
                        'Título': titulo,
                        'Autores': autores,
                        'Resumo': resumo,
                        'Link': link
                    })
            print(f"Página {pagina} processada ({len(artigos)} artigos)")
            time.sleep(1)  # respeita o servidor
        except Exception as e:
            print(f"Erro na página {pagina}: {e}")

    return pd.DataFrame(artigos)

# === EXECUÇÃO ===
if __name__ == "__main__":
    termo_busca = "inteligência artificial saúde pública"  # mude aqui
    print(f"Buscando por: {termo_busca}...")
    df = buscar_artigos_scielo(termo_busca, max_paginas=3)

    # Salva em CSV
    df.to_csv('resultados_scielo.csv', index=False, encoding='utf-8')
    print(f"\n✅ {len(df)} artigos salvos em 'resultados_scielo.csv'")
    print("Pronto para revisão rápida com IA!")
