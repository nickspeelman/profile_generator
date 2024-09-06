from extract_relevant_info import extract_relevant_info
from perform_search import perform_search

def fetch_and_log_content(query, profile_folder):
    """Fetch the content of each search result URL and log it, handling PDFs appropriately."""
    search_results = perform_search(query)
    relevant_info = extract_relevant_info(search_results)

    for result in relevant_info:
        url = result["url"]
        if url.lower().endswith('.pdf'):
            # Log the PDF link and download it
            save_pdf(profile_folder, url)
        else:
            # Fetch webpage content and log it
            webpage_content = fetch_webpage_content_selenium(url, profile_folder)
            result["body_content"] = webpage_content

    return relevant_info
