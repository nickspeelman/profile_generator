import os
from datetime import datetime

# Define the base directory where all profile folders will be stored
log_directory = "profiles"

def get_profile_folder(topic):
    """Generate a folder name based on the current date and topic."""
    date_str = datetime.now().strftime("%Y%m%d")
    sanitized_topic = topic.replace(" ", "_")

    # Create the final folder inside the 'profiles' directory
    profile_folder = os.path.join(log_directory, f"{date_str}_{sanitized_topic}")

    # Ensure the profile folder exists
    os.makedirs(profile_folder, exist_ok=True)

    return profile_folder

def get_log_filename(topic):
    """Generate the full log file path."""
    profile_folder = get_profile_folder(topic)
    log_file_path = os.path.join(profile_folder, "log.txt")
    return log_file_path

def write_to_log(topic, message):
    """Write a message to the log file."""
    log_file_path = get_log_filename(topic)

    # Open the log file in append mode and write the message
    with open(log_file_path, 'a', encoding="utf-8") as log_file:
        log_file.write(message + "\n")
