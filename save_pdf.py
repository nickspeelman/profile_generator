import os
import requests



def save_pdf(profile_folder, url):
    """Download and save PDF to the profile folder."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        pdf_name = os.path.basename(url)
        pdf_path = os.path.join(profile_folder, pdf_name)

        with open(pdf_path, 'wb') as f:
            f.write(response.content)

        return pdf_name
    except Exception as e:
        return f"Error downloading PDF from {url}: {e}"
