from groq import Groq
from dotenv import load_dotenv
from string_check import parse_test_string
import os

# Initialize the client with your API key
load_dotenv()
client = Groq(api_key=os.getenv("API_KEY"))


def use_llama(msg):
    # Define the message for the model
    messages = [
        {
            "role": "user",
            "content": msg
        }
    ]

    # Create the completion
    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=messages,
        temperature=0.2,
        max_tokens=1024,
        top_p=0.9,
        stream=False,
        stop=None,
    )
    return completion.choices[0].message.content


def get_questions_and_answers(test_query):
    # Extract and print the content
    test_check = use_llama(test_query)

    questions, answers = parse_test_string(test_check)
    return questions, answers


# test_maker = ("Build a test at algebra with 6 questions and 4 multi-option answers for 8th grade. "
#               "- At your respond give just the test by the next format: "
#               "Question(number)\n"
#               "the question.\n\n"
#               "the answers (from A to D)")

# ans = use_llama(test_maker)
# print(ans)
# while True:
#     # os.system('clear')
#     query = input('how can i help you?  ')
#     answer = use_llama(query)
#     print(answer)
# for i, (q, a) in enumerate(zip(questions, answers)):
#     print(f"{q}\n")
#     for ans in a:
#         print(ans)
#     print()
