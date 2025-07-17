# get-papers-list
Python program to fetch filtered research papers using PubMed API
# PubMed Paper Extractor (get-paper-list)

This Python project fetches research papers from **PubMed** using a keyword-based query (e.g., "Pfizer"), then extracts and saves details like titles, publication dates, author affiliations, and emails—focusing especially on papers with **non-academic authors** such as those from **pharmaceutical** or **biotech companies**.



## Features

- Search PubMed with any query (e.g., "Pfizer", "mRNA vaccine", "biotech cancer research")
- Output results to a structured **CSV** file
- Detect **non-academic authors** based on affiliations (e.g., Pfizer, Novartis, etc.)
-  Extract **corresponding author emails**
-  Clean CLI interface for custom queries



## Output Format (CSV)

The output CSV contains:

| PubmedID | Title | Publication Date | Non-academic Authors | Company Affiliations | Corresponding Author Email |
|----------|-------|------------------|------------------------|-----------------------|-----------------------------|





### 1. Install Dependencies


poetry install
poetry run python main.py --query "Pfizer" --output output.csv
poetry run python main.py --query "COVID-19 Pfizer vaccine" --output pfizer_papers.csv --debug
get-paper-list/
├── main.py                   # Entry point of the program
├── fetch_pubmed.py           # Fetch and parse PubMed data using BioPython
├── affiliation_filter.py     # Filter and detect non-academic affiliations
├── email_extractor.py        # Extract corresponding author emails
├── output_writer.py          # Format and write data to CSV
├── pyproject.toml            # Poetry project configuration
└── README.md                 # This file











This project is open-source and free to use under the MIT License.
