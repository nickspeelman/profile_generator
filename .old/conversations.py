def format_combined_search_results(search_queries_obj):
    """Format the combined search results for all queries."""
    combined_results = []

    for search in search_queries_obj:
        combined_results.append(f"Results for query '{search['query']}':")

        if search['results']:
            for result in search['results']:
                title = result.get('title', 'No title available')
                url = result.get('url', 'No URL available')
                snippet = result.get('snippet', 'No snippet available')

                combined_results.append(f"Title: {title}")
                combined_results.append(f"Link: {url}")
                combined_results.append(f"Snippet: {snippet}")
                combined_results.append("")  # Add a blank line for spacing between results
        else:
            combined_results.append("No results found for this query.")

    return "\n".join(combined_results)

