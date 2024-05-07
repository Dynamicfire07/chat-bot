import openai
import os
class Chatbot:
    def __init__(self):
        openai.api_key="ENTER YOUR API KEY HERE"

    def get_response(self, user_input):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system","content": "Answer the request the user has"},
                {"role": "user", "content": user_input}
            ]
        )
        return response['choices'][0]['message']['content']

if __name__ == "__main__":
    chatbot= Chatbot()
    response = chatbot.get_response("Write a joke about windows")
    print(response)