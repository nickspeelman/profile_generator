from agents import agent_roles
from perform_search import perform_search
from format_combined_search_results import format_combined_search_results
from extract_relevant_info import extract_relevant_info
from chatgpt_api import get_response

def agent_conversation(prompt, agent, conversation_history, topic=None):
    """Simulate a conversation with an agent, maintaining conversation history."""
    agent_role = agent_roles.get(agent, "You are an agent without a specific role.")

    if agent == "Remi":
        # Directly use search queries extracted earlier
        conversation_history.append({"role": "user", "content": prompt})
        search_query = prompt.split("perform a search for:")[1].strip()

        print(f"Performing search for: {search_query}")  # Debug: print the search query

        # Perform the search
        search_results = perform_search(search_query)

        # Debug: Print raw search results
        #print(f"Raw search results: {search_results}")

        # Extract relevant information from the search results
        search_results_formatted = extract_relevant_info(search_results,topic)

        # Debug: Print formatted search results
        # print(f"Formatted search results: {search_results_formatted}")

        # Format the combined search result
        response = format_combined_search_results([{"query": search_query, "results": search_results_formatted}])

        # Add the search result to the conversation history as if it were a response from Remi
        conversation_history.append({"role": "assistant", "content": response})
    else:
        # Regular agents use conversation history for generating a response
        conversation_history.append({"role": "user", "content": prompt})
        response = get_response(conversation_history, agent_role)
        conversation_history.append({"role": "assistant", "content": response})

    return response
