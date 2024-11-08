import json
import argparse

def extract_urls_by_keyword(input_file, keyword, output_file=None):
    with open(input_file, 'r') as f:
        data = json.load(f)

    matching_urls = set()
    
    for item in data.get("item", []):
        url = item.get("request", {}).get("url", {}).get("raw", "")
        if keyword.lower() in url.lower():
            matching_urls.add(url) 

    matching_urls = sorted(list(matching_urls))

    if output_file:
        with open(output_file, 'w') as f:
            f.write("\n".join(matching_urls))
    else:
        print("\n".join(matching_urls))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract URLs containing a specific keyword from a Postman collection")
    parser.add_argument("-i", "--input", required=True, help="Input JSON file (Postman collection)")
    parser.add_argument("-k", "--keyword", required=True, help="Keyword to search for in URLs")
    parser.add_argument("-o", "--output", help="Output file for matching URLs (optional)")

    args = parser.parse_args()
    extract_urls_by_keyword(args.input, args.keyword, args.output)
