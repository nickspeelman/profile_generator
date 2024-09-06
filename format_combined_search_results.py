def format_combined_search_results(search_queries_obj):
    """Format the combined search results into a readable format."""
    combined_results = []

    for search_query in search_queries_obj:
        query = search_query["query"]
        results = search_query["results"]

        result_summaries = []
        for result in results:
            if result['url'].lower().endswith('.pdf'):
                result_summaries.append(f"PDF Link: {result['url']}")
            else:
                # Include body content in addition to title, URL, and snippet
                result_summaries.append(
                    f"Title: {result['title']}\n"
                    f"Link: {result['url']}\n"
                    f"Snippet: {result['snippet']}\n"
                    f"Body Content: {result['body_content']}\n"
                )

        # Format the results for this query
        formatted_results = f"Results for '{query}':\n" + "\n".join(result_summaries)
        combined_results.append(formatted_results)

    return "\n\n".join(combined_results)
