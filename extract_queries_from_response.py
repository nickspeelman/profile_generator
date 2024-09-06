import ast

def extract_queries_from_response(response):
    """Extract search queries from Manny's response."""
    try:
        # Locate the start of the list by finding the variable assignment
        start_index = response.find("search_queries_for_remi = [")
        if start_index != -1:
            # Extract the substring starting from the list
            list_str = response[start_index:].split('=', 1)[1].strip()

            # Ensure the string ends with a closing bracket for a Python list
            if not list_str.endswith(']'):
                list_str = list_str.split(']', 1)[0] + ']'

            # Use ast.literal_eval to safely evaluate the string as a Python list
            queries = ast.literal_eval(list_str)
            return queries
    except SyntaxError as se:
        print(f"Syntax error extracting queries: {se}")
    except Exception as e:
        print(f"Error extracting queries: {e}")

    # Return an empty list if no queries were found or if there was an error
    return []


