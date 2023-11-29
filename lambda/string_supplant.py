import os
import json


# This lambda is triggered by the ApiGateWay.
def lambda_handler(event, context):
    # Define the words to be replaced
    words_to_replace = {
        "ABN": "ABN AMRO",
        "ING": "ING Bank",
        "Rabo": "Rabobank",
        "Triodos": "Triodos Bank",
        "Volksbank": "de Volksbank",
    }
    # Print  event data
    print("request: {}".format(json.dumps(event)))
    # Get the input string from the event data
    input_str = event["input_str"]

    # Replace the words in the input string using a list comprehension
    try:
        """
        Here new_word is not defined in the try block. This is because new_word is only defined
        inside the if block that checks if the current word is in the words_to_replace dictionary.
        If the current word is not in the dictionary, new_word is not defined and the code raises a NameError.
        """
        input_str = " ".join(
            [
                new_word if word in words_to_replace else word
                for word in input_str.split()
            ]
        )
    except ValueError:
        return {"error": "Invalid input string"}

    # Return the result as a JSON response
    return {"result": input_str}
