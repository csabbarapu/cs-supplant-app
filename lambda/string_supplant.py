import os

# This lambda is triggered by the ApiGateWay.
# Define the words to be replaced
words_to_replace = {
    "ABN": "ABN AMRO",
    "ING": "ING Bank",
    "Rabo": "Rabobank",
    "Triodos": "Triodos Bank",
    "Volksbank": "de Volksbank",
}


def lambda_handler(event, context):
    # Get the input string from the event data
    input_str = event["input_str"]

    # Replace the words in the input string using a list comprehension
    try:
        input_str = ".join([new_word if word in words_to_replace else word for word in input_str.split()])"
    except ValueError:
        return {"error": "Invalid input string"}

    # Return the result as a JSON response
    return {"result": input_str}
