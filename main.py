import argparse
import logging
from fetch_pubmed import fetch_pubmed_results
from affiliation_filter import filter_non_academic_authors
from csv_writer import write_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers and identify non-academic authors.")
    parser.add_argument('--query', required=True, help='PubMed search query')
    parser.add_argument('--max-results', type=int, default=20, help='Maximum number of results to fetch')
    parser.add_argument('--output', '-o', help='CSV output file')
    parser.add_argument('--debug', '-d', action='store_true', help='Enable debug logging')

    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    logging.debug(f"Query: {args.query}")
    papers = fetch_pubmed_results(args.query, args.max_results)

    if not papers:
        logging.warning("No papers found.")
        return

    filtered_papers = filter_non_academic_authors(papers)

    if args.output:
        write_to_csv(filtered_papers, args.output)
        print(f"Results saved to {args.output}")
    else:
        for paper in filtered_papers:
            print(paper)

if __name__ == "__main__":
    main()
