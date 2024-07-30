from openai_logic.api_client import call_openai_api
from openai_logic.prompts import SYSTEM_PROMPT, SENTIMENT_PROMPT, PRODUCT_PROMPT, DEPARTMENT_PROMPT, SOLUTION_PROMPT


class FeedbackAnalyzer:
    @staticmethod
    def analyze_sentiment(feedback):
        prompt = SENTIMENT_PROMPT.format(feedback=feedback)
        return call_openai_api(prompt, SYSTEM_PROMPT)

    @staticmethod
    def identify_product(feedback):
        prompt = PRODUCT_PROMPT.format(feedback=feedback)
        return call_openai_api(prompt, SYSTEM_PROMPT)

    @staticmethod
    def determine_department(feedback):
        prompt = DEPARTMENT_PROMPT.format(feedback=feedback)
        return call_openai_api(prompt, SYSTEM_PROMPT)

    @staticmethod
    def suggest_solution(feedback, product):
        prompt = SOLUTION_PROMPT.format(feedback=feedback, product=product)
        return call_openai_api(prompt, SYSTEM_PROMPT)
