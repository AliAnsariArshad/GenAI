from openai_logic.api_client import call_openai_api
from openai_logic.prompts import SYSTEM_PROMPT, RESPONSE_PROMPT

# def generate_response(sentiment, product, department, issue_resolved=False):
#     prompt = RESPONSE_PROMPT.format(
#         sentiment=sentiment,
#         product=product,
#         department=department,
#         issue_resolved="Yes" if issue_resolved else "No"
#     )
#     return call_openai_api(prompt, SYSTEM_PROMPT)


from openai_logic.prompts import SYSTEM_PROMPT

def generate_response(sentiment, product, department, issue_resolved=False):
    prompt = f"""
    Task: Generate a response to customer feedback based on the following analysis:

    Sentiment: {sentiment}
    Product: {product}
    Department: {department}
    Issue Resolved: {"Yes" if issue_resolved else "No"}

    Instructions:
    1. Craft a concise, warm, and professional response addressing the customer's feedback.
    2. Follow these sentiment-specific guidelines:
    - Positive: Thank the customer warmly. Mention the product if specified.
    - Negative: Apologize for the negative experience. Mention the product if specified. Inform the customer that their concern has been forwarded to the {department} for further action.
    - Neutral: Thank the customer for their feedback.
    3. If the issue was resolved (Issue Resolved: Yes), express happiness that the solution worked and encourage future feedback.
    4. Do NOT include personal names, positions, or signatures in the response.
    5. Do NOT use salutations or phrases like "Sincerely," or "Best regards," at the end of the response.
    6. Keep the response concise and to the point.

    Respond with ONLY the customer feedback reply. Do not include any other text, explanations, metadata, or sign-offs.
    """

    return call_openai_api(prompt, SYSTEM_PROMPT)