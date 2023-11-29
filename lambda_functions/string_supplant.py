import os
import json
import logging

# Define the words to be replaced
words_to_replace = {
    "ABN": "ABN AMRO",
    "ING": "ING Bank",
    "Rabo": "Rabobank",
    "Triodos": "Triodos Bank",
    "Volksbank": "de Volksbank",
}

# Declare Logger
default_log_args = {
    "level": logging.DEBUG if os.environ.get("DEBUG", False) else logging.INFO,
    "format": "[%(levelname)s] [+] %(message)s",
    "force": True,  # AWS Lambda already employs a root handler hence the force override here
}
logging.basicConfig(**default_log_args)
logger = logging.getLogger()


# This lambda is triggered by the ApiGateWay.
def lambda_handler(event, context):
    # Log event data
    logger.debug("request: {}".format(json.dumps(event)))
    # Get the input string from the event data
    parse_event = json.loads(event["body"])
    input_str = json.dumps(parse_event["input_str"])

    logger.info(f"your input string is {input_str}")
    # Flag to track if any replacement is made
    output_made = False
    # Initialize with the original input string
    output_string = input_str

    for key, value in words_to_replace.items():
        if key.lower() in input_str.lower():
            # Get the index from the original string for the key
            index = input_str.lower().find(key.lower())
            logger.debug(index)
            # Get the keyword from original string to be replaced
            word_to_replace = input_str[index : index + len(key.lower())]
            logger.debug(words_to_replace)
            with_value = value
            logger.debug(value)
            # Now do actual replace
            output_string = input_str.replace(word_to_replace, with_value)
            output_made = True

    if not output_made:
        """
        Raising value error in this block instead of
        try-exception as replace does not raise any value error.
        """
        logger.error("Invalid input string")
        return {
            "statusCode": 422,
            "headers": {"Content-Type": "text/plain"},
            "body": "Invalid input string provided.",
        }
    else:
        logger.info(f"your result is {output_string}")
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "text/plain"},
            "body": f"Hello, TMNL Team! Here is your expected output: \n {output_string}",
        }
