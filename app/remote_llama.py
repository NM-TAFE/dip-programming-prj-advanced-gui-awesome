import requests
import json
import time


class Llama:
    """
    A utility class for analysing extracted text using Llama.

    This class provides methods to send a prompt to Llama 3 8B models and get the response back.

    Note:
    There is no specific fine-tuning of the models used for this project.
    80B models have been ruled out due to storage requirements.
    """

    url = "http://chaostree.xyz:3002/"  # url of the API running Llama

    @staticmethod
    def query(question):
        data = {"prompt": question}

        try:
            response = requests.post(Llama.url + 'llama', json=data)
            response.raise_for_status()
            response_data = response.json()
        except requests.exceptions.RequestException as e:
            return "error : " + str(e)

        # Check if the response is a dictionary before trying to access it
        if isinstance(response_data, dict):
            # if the response message is "server starting"
            if response_data.get("message") == "server starting":
                print("Server is starting, please hold...")
                # wait 2 seconds then try again
                time.sleep(2)
                return Llama.query(question)
            else:
                return response_data.get("message")
        else:
            return response_data  # Return the response as is if it's not a dictionary

    @staticmethod
    def query_with_default(content, language):
        data = {"prompt": content, "language": language}

        try:
            response = requests.post(Llama.url + 'llamapreprompt', json=data)
            response.raise_for_status()
            response_data = response.json()
        except requests.exceptions.RequestException as e:
            return "error : " + str(e)

        # Check if the response is a dictionary before trying to access it
        if isinstance(response_data, dict):
            # if the response message is "server starting"
            if response_data.get("message") == "server starting":
                print("Server is starting, please hold...")
                # wait 2 seconds then try again
                time.sleep(2)
                return Llama.query_with_default(content)
            else:
                return response_data.get("message")
        else:
            return response_data  # Return the response as is if it's not a dictionary

    @staticmethod
    def set_prompt(prompt=None):
        if not prompt:
            data = {}
        else:
            if ("%QUESTION%" not in prompt):
                raise ValueError("Prompt must contain %QUESTION%")
            data = {"newPrompt": prompt}
        response = requests.post(Llama.url + 'llamasetprompt', json=data)
        response_data = response.json()
        # Check if the response is a dictionary before trying to access it
        if isinstance(response_data, dict):
            # if the data was none or empty return the response
            if not data:
                return response_data.get("prompt")
            else:
                return [response_data.get("prompt"), response_data.get("oldPrompt")]
        else:
            return response_data
