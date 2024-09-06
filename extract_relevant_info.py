from fetch_webpage_content_selenium import fetch_webpage_content_selenium
from logger import get_profile_folder

def extract_relevant_info(search_results, topic=None):
    """Extract relevant information from search results."""
    formatted_results = []
    profile_folder = get_profile_folder(topic)
    for result in search_results.get('webPages', {}).get('value', []):
        title = result.get('name', 'No Title Available')  # Use 'name' for the title
        url = result.get('url', 'No URL Available')
        snippet = result.get('snippet', 'No Snippet Available')
        content = fetch_webpage_content_selenium(url, profile_folder)

        formatted_results.append({
            'title': title,
            'url': url,
            'snippet': snippet,
            'body_content': content
        })

    return formatted_results