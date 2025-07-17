from Bio import Entrez

Entrez.email = "darshana08dayare@gmail.com"  # Replace with your email

def fetch_pubmed_results(query, max_results=20):
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    id_list = record["IdList"]

    papers = []
    if not id_list:
        return papers

    handle = Entrez.efetch(db="pubmed", id=",".join(id_list), rettype="medline", retmode="text")
    data = handle.read()

    # You can improve parsing later using `Bio.Medline`
    for pubmed_id in id_list:
        papers.append({
            "PubmedID": pubmed_id,
            "Title": "Sample Title for " + pubmed_id,
            "Publication Date": "2024-01-01",
            "Authors": [{"Name": "Dr. John Doe", "Affiliation": "Pfizer Inc.", "Email": "john@pfizer.com"}]
        })
    return papers
