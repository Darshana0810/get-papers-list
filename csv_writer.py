import pandas as pd

def write_to_csv(papers, filename):
    if not papers:
        print("No data to write.")
        return
    df = pd.DataFrame(papers)
    df.to_csv(filename, index=False)
