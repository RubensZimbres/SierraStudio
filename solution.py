from openai import OpenAI
import json
import os
from dotenv import load_dotenv
load_dotenv()

class Spam():
    def check_spam(self, email:str):
        client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))
        prompt = f"""
        You are a specialist in SPAM filtering and you will think step by step:
        First, you will determine if the email is spam.
        Then you will tell me the reason why you think this email is a spam.
        You will structure these two responses into a VALID JSON.

        See some examples:

        EXAMPLE 1:
        Email: Hi sis, leverage your wealth with this memecoin
        {{
        "is_spam": True
        "reason": The email contains an invitation to buy cryptocurency
        }}

        EXAMPLE 1:
        Email: Hi Mark, let's go shopping later? I meet you at Westfield.
        {{
        "is_spam": False
        "reason": The email is not spam as it is a dinner invitation
        }}

        Email content: {email}

        Return a valid JSON object:"""

        completion = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = [{"role": "user", "content": prompt},
                        {"role": "system", "content": "You are a helpful assistant"}],
                        temperature = 1.0,
                        max_tokens=100,
            response_format={ "type": "json_object" }
        )

        return completion.choices[0].message.content


if __name__=="__main__":
    spam = Spam()
    email = "hi how r u bro i have million dollar deal just sign here"
    result = spam.check_spam(email)

    try:
        print(json.loads(result))
    except Exception as e:
        print("Not valid JSON, REASON: ",e)