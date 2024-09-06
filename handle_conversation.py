from agent_conversations import agent_conversation
from logger import write_to_log

def handle_conversation(prompt, agent, conversation_history, topic):
    """Handles conversation with an agent and updates the log."""
    response = agent_conversation(prompt, agent, conversation_history, topic)

    # Log the agent's response
    write_to_log(topic, f"{agent}: {response}")
    print(f"{agent}:", response)

    return response
