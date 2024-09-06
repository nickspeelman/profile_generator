def generate_search_queries(conversation_history):
    """Generate potential search queries from the conversation history."""
    queries = []

    # Look for keywords or potential search topics
    for message in conversation_history:
        if message['role'] == 'user':
            # Extract potential search topics from user messages
            if "Remi" in message['content']:
                parts = message['content'].split('Remi, ', 1)
                if len(parts) > 1:
                    potential_query = parts[1].strip().strip("?").strip(".")
                    queries.append(potential_query)

    # Add a default query if no specific queries are found
    if not queries:
        queries.append("general knowledge about the topic")

    return queries