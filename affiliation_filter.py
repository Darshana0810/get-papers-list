def is_non_academic(affiliation):
    if not affiliation:
        return False
    keywords = ["pharma", "pharmaceutical", "biotech", "inc", "corp", "ltd", "llc"]
    return any(kw in affiliation.lower() for kw in keywords)

def filter_non_academic_authors(papers):
    filtered = []
    for paper in papers:
        non_acad_authors = []
        companies = []
        emails = []

        for author in paper.get("Authors", []):
            affil = author.get("Affiliation", "")
            email = author.get("Email", "")

            if is_non_academic(affil):
                non_acad_authors.append(author["Name"])
                companies.append(affil)
                emails.append(email)

        if non_acad_authors:
            filtered.append({
                "PubmedID": paper["PubmedID"],
                "Title": paper["Title"],
                "Publication Date": paper["Publication Date"],
                "Non-academic Author(s)": "; ".join(non_acad_authors),
                "Company Affiliation(s)": "; ".join(companies),
                "Corresponding Author Email": "; ".join(emails)
            })
    return filtered
