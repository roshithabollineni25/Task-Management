import google.generativeai as genai


genai.configure(
    api_key="AQ.Ab8RN6KtUEcOVvlLn6bx1O1pScq0d3ZYWPr51ah-oDXTMQl82g"
)


model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def ask_ai_service(message):

    response = model.generate_content(
        message
    )

    return response.text
