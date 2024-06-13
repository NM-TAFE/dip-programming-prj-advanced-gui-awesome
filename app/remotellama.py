import requests
import json
import time

class LlamaInterface:
    url = "http://chaostree.xyz:3002/"
    headers = {"Content-Type": "application/json"}
    def query(question):
        data = {"prompt": question}
        try:
            response = requests.post(LlamaInterface.url + 'llama', headers=LlamaInterface.headers, json=data)
        except requests.exceptions.ConnectTimeout:
            return "Timeout Error has occurred"
        response_data = response.json()
        # Check if the response is a dictionary before trying to access it
        if isinstance(response_data, dict):
            #if the response message is "server starting"
            if response_data.get("message") == "server starting":
                print("Server is starting, please hold...")
                #wait 2 seconds then try again
                time.sleep(2)
                return LlamaInterface.query(question)
            elif response.status_code == 500:
                return response_data.get("error")
            else:
                return response_data.get("message")
        else:
            return response_data  # Return the response as is if it's not a dictionary
    
    def query_with_default(content, language):
        data = {"prompt": content, "language": language}
        response = requests.post(LlamaInterface.url + 'llamapreprompt', headers=LlamaInterface.headers, json=data)
        response_data = response.json()
        # Check if the response is a dictionary before trying to access it
        if isinstance(response_data, dict):
            #if the response message is "server starting"
            if response_data.get("message") == "server starting":
                print("Server is starting, please hold...")
                #wait 2 seconds then try again
                time.sleep(2)
                return LlamaInterface.query_with_default(content)
            elif response.status_code == 500:
                return response_data.get("error")
            else:
                return response_data.get("message")
        else:
            return response_data  # Return the response as is if it's not a dictionary

    def set_prompt(prompt = None):
        if not prompt:
            data = {}
        else:
            if("%QUESTION%" not in prompt):
                raise ValueError("Prompt must contain %QUESTION%")
            data = {"newPrompt": prompt}
        response = requests.post(LlamaInterface.url + 'llamasetprompt', headers=LlamaInterface.headers, json=data)
        response_data = response.json()
        # Check if the response is a dictionary before trying to access it
        if isinstance(response_data, dict):
            #if the data was none or empty return the response
            if not data:
                return response_data.get("prompt")
            else:
                return [response_data.get("prompt"), response_data.get("oldPrompt")]
        else:
            return response_data