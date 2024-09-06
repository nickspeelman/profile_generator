from handle_conversation import handle_conversation
from logger import write_to_log
from fetch_webpage_content_selenium import fetch_webpage_content_selenium
from format_combined_search_results import format_combined_search_results

def handle_search_queries(search_queries, conversation_history, topic, profile_folder):
    """
    Perform searches based on the search queries, process the results,
    and fetch webpage content or download PDFs.
    """
    search_queries_obj = []
    for query in search_queries:
        # Prompt Remi to perform a search
        prompt_remi = f"Remi, perform a search for: {query}"
        response_remi = handle_conversation(prompt_remi, "Remi", conversation_history, topic)

        # Log Remi's response
        write_to_log(topic, f"Remi: {response_remi}")
        print("Remi:", response_remi)

        try:
            # Parse response_remi if needed (in case it's a string representation of a list)
            search_results = eval(response_remi) if isinstance(response_remi, str) else response_remi

            # Prepare to store results with content
            results_with_content = []

            # Iterate through search results
            for result in search_results:
                if isinstance(result, dict) and 'url' in result:
                    url = result['url']
                    print(f"Fetching content from URL: {url}")  # Debugging URL fetching

                    # Fetch the content or download PDFs using Selenium
                    content = fetch_webpage_content_selenium(url, profile_folder)
                    print(f'Content returned from selenium: {content}')

                    # Add body content to the result
                    result_with_content = {
                        'title': result.get('title', 'No Title Available'),
                        'url': url,
                        'snippet': result.get('snippet', 'No Snippet Available'),
                        'body_content': content  # Store the body content or PDF handling result
                    }
                    results_with_content.append(result_with_content)

            # Store query and results
            search_queries_obj.append({
                "query": query,
                "results": results_with_content
            })

            # Format the results for this query
            formatted_results = format_combined_search_results([{
                "query": query,
                "results": results_with_content
            }])

            # Add the formatted results to the conversation history as a response from Remi
            conversation_history.append({
                "role": "assistant",
                "content": f"Remi's search results for '{query}':\n{formatted_results}"
            })

        except Exception as e:
            error_message = f"Error handling Remi's results: {e}"
            write_to_log(topic, error_message)
            # Add error message to conversation history
            conversation_history.append({
                "role": "assistant",
                "content": error_message
            })

    # Format the results for all queries
    formatted_results = format_combined_search_results(search_queries_obj)
    return formatted_results
