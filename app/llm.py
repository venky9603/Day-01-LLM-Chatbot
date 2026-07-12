from google import genai
from google.genai import types

from app.config import (
    GEMINI_API_KEY,
    TEMPERATURE,
    MAX_OUTPUT_TOKENS,
    TOP_P,
    TOP_K
)

from app.prompts import SYSTEM_PROMPT
from app.logger import logger


# Initialize Gemini Client
client = genai.Client(
    api_key=GEMINI_API_KEY
)


# Store conversation history
conversation_history = []


def generate_response(user_message: str) -> str:

    try:

        


        # Add user message to history
        conversation_history.append(
            {
                "role": "user",
                "content": user_message
            }
        )


        # Combine system prompt + conversation
        prompt = f"""
{SYSTEM_PROMPT}

Conversation History:
{conversation_history}

User:
{user_message}
"""


        


        response = client.models.generate_content(

            model="gemini-2.5-flash",

            contents=prompt,

            config=types.GenerateContentConfig(

                temperature=TEMPERATURE,

                max_output_tokens=MAX_OUTPUT_TOKENS,

                top_p=TOP_P,

                top_k=TOP_K

            )
        )


        answer = response.text


        # Store assistant response
        conversation_history.append(
            {
                "role": "assistant",
                "content": answer
            }
        )


        


        return answer



    except Exception as e:

        logger.error(
            f"Error while generating response: {e}"
        )

        return "Something went wrong while generating the response."