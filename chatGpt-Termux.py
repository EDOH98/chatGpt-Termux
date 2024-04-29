import requests
import json

# Replace 'YOUR_API_KEY' with your OpenAI API key
api_key = 'YOUR_API_KEY'

# Define the API endpoint and headers
api_endpoint = 'https://api.openai.com/v1/chat/completions'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

# Define the message to send to ChatGPT
message = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, ChatGPT!"}
    ]
}

# Send a POST request to the API
response = requests.post(api_endpoint, headers=headers, json=message)

# Parse the JSON response
response_json = response.json()

# Print the assistant's response
assistant_response = response_json["choices"][0]["message"]["content"]
print(assistant_response)
