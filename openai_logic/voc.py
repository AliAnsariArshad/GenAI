from openai_logic.feedback_analyzer import FeedbackAnalyzer
from openai_logic.response_generator import generate_response
from openai_logic.api_client import call_openai_api
from openai_logic.prompts import SYSTEM_PROMPT, REGENERATE_FEEDBACK_PROMPT


def handle_missing_info(feedback, sentiment, initial_product, initial_department):
    print("\nAdditional information needed for your feedback.")

    if initial_product == 'General':
        additional_product = input("Please specify the product you're providing feedback about: ").strip()
    else:
        additional_product = initial_product

    prompt = REGENERATE_FEEDBACK_PROMPT.format(feedback=feedback, sentiment=sentiment, product=additional_product,
        department=initial_department)
    regenerated_feedback = call_openai_api(prompt, SYSTEM_PROMPT)

    return regenerated_feedback, additional_product, initial_department


def process_feedback(feedback):
    analyzer = FeedbackAnalyzer()
    sentiment = analyzer.analyze_sentiment(feedback)
    print(f"Sentiment: {sentiment}")

    product = analyzer.identify_product(feedback)
    department = analyzer.determine_department(feedback)
    print(f"Product: {product}")
    print(f"Department: {department}")

    if sentiment == 'Negative':
        if product == 'General':
            feedback, product, department = handle_missing_info(feedback, sentiment, product, department)
            print("\nRegenerated feedback:")
            print(feedback)
            suggested_solution = analyzer.suggest_solution(feedback, product)
            if suggested_solution != "No simple solution":
                print(f"\nSuggested solution: {suggested_solution}")
                return {"Suggested solution": suggested_solution}, product, department
                # user_response = input("Did this solution resolve your issue? (yes/no): ").strip().lower()
                # if user_response == 'yes':
                #     return generate_response('Positive', product, department)
                # TODO
        else:
            suggested_solution = analyzer.suggest_solution(feedback, product)
            if suggested_solution != "No simple solution":
                print(f"\nSuggested solution: {suggested_solution}")
                return {"Suggested solution": suggested_solution}
                # user_response = input("Did this solution resolve your issue? (yes/no): ").strip().lower()
                # if user_response == 'yes':
                #     return generate_response('Positive', product, department)
                # TODO

    return generate_response(sentiment, product, department)

# if __name__ == "__main__":
#     print("Welcome to the Voice of Customer Feedback System!")
#     print("You can provide feedback, and our AI will analyze and respond to it.")
#     print("Type 'exit' at any time to quit the program.\n")

    # while True:
    #     # name = input("Please neter your name: ").strip()
    #
    #     # email_id = input("Please neter your email id: ").strip()
    #     user_feedback = input("Please enter your feedback: ").strip()
    #     # user_feedback = "hi my name is {name} and my email id is {email_id}, {user_feedback}"
    #     if user_feedback.lower() == 'exit':
    #         print("Thank you for using our feedback system. Goodbye!")
    #         break
    #     if not user_feedback:
    #         print("Feedback cannot be empty. Please try again.")
    #         continue
    #     try:
    #         response = process_feedback(user_feedback)
    #         print("\nResponse to customer:")
    #         print(response)
    #     except Exception as e:
    #         print(f"An error occurred: {e}")
    #         print("We apologize, but an error occurred while processing your feedback. Please try again.")
    #     print()
