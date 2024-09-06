from handle_conversation import handle_conversation
from logger import get_profile_folder
from handle_search_queries import handle_search_queries
from extract_queries_from_response import extract_queries_from_response

# Prompt the user for a research topic
topic = input("Please enter the research topic: ")
queries_per_iteration = input("How many searches would you like Remi to perform each iteration: ")

# Initialize conversation history
conversation_history = []

# Ask Susan how to approach the research
prompt_susan = f"Susan, how should we approach gathering information on the topic '{topic}'?"
response_susan = handle_conversation(prompt_susan, "Susan", conversation_history, topic)

# Continue the conversation with Manny based on Susan's response
prompt_manny = f"Manny, here is the strategy from Susan: {response_susan}. What follow-up questions do you have for her?"
response_manny = handle_conversation(prompt_manny, "Manny", conversation_history, topic)

# Ask Susan for replies to Manny
prompt_susan = f"Susan, here are Manny's follow up questions: {response_manny} What is your reply'?"
response_susan = handle_conversation(prompt_susan, "Susan", conversation_history, topic)

# Ask Manny to prepare a list of search queries for Remi
prompt_manny = f"Manny, please prepare a list of {queries_per_iteration} specific search queries Remi should perform based on yours and Susan's conversation so far. Please format this list of search queries as a python list object named 'search_queries_for_remi'"
response_manny = handle_conversation(prompt_manny, "Manny", conversation_history, topic)

# Extract queries from Manny's response
search_queries = extract_queries_from_response(response_manny)

# Get the profile folder for saving logs and PDFs
profile_folder = get_profile_folder(topic)

# Pass the search queries to the search function
handle_search_queries(search_queries, conversation_history, topic, profile_folder)

# Send the results back to Susan for more questions:
prompt_susan = "Based on Remi's search results what follow up questions do you have?"
response_susan = handle_conversation(prompt_susan, "Susan", conversation_history, topic)

# Have Manny prepare a second set of searches:
prompt_manny = f"Based on this response from Susan: {response_susan} and the conversation so far, please prepare a list of {queries_per_iteration} specific search queries Remi should perform based on yours the conversation between you and Susan so far. Please format this list of search queries as a python list object named 'search_queries_for_remi'"
response_manny = handle_conversation(prompt_manny, "Manny", conversation_history, topic)

# Extract queries from Manny's response
search_queries = extract_queries_from_response(response_manny)

# Get the profile folder for saving logs and PDFs
profile_folder = get_profile_folder(topic)

# Pass the search queries to the search function
handle_search_queries(search_queries, conversation_history, topic, profile_folder)

# Have Susan preare the final synthesis
prompt_cindy = "Cindy, based on Susan's questions and Remi's search results, please prepare a final summary. This summary should be in the form of an html file. It should be broken into sections based on Susan's strategy notes. Each section should include a summary as well as the links provided by Remi in his research to the relevant searches. Please also link to any PDFs that may seem relevant to the root directory."
response_cindy = handle_conversation(prompt_cindy, "Cindy", conversation_history, topic)

# Have Susan provide feedback
prompt_susan = f"Susan, please review Cindy's response: {prompt_cindy} What feedback to you have?"
response_susan = handle_conversation(prompt_susan, "Susan", conversation_history, topic)

# Have Manny prepare final recommendations
prompt_manny = f"Manny, based on this response from Susan {response_susan} and your review of the product produced by Cindy: {response_cindy}, please provide recommedations for Cindy in performing her synthesis"
response_manny = handle_conversation(prompt_manny, "Manny", conversation_history, topic)

# Have Cindy prepare the final produect
prompt_cindy = f"Cindy, based on the final recommendation's from Manny: {response_manny}, please prepare a final draft of the research summary. It should again be an html document, including summary sections with links to relevant sources and links to potentially relevant PDFs in the root directory."
response_cindy = handle_conversation(prompt_cindy, "Cindy", conversation_history, topic)
