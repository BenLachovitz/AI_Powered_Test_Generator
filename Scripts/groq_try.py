from groq import Groq
from string_check import parse_test_string

# Initialize the client with your API key
client = Groq(api_key="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")


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


# for i, (q, a) in enumerate(zip(questions, answers)):
#     print(f"{q}\n")
#     for ans in a:
#         print(ans)
#     print()



