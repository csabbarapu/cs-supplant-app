import json
import pytest
from lambda_functions.string_supplant import lambda_handler


def test_lambda_handler_correct_input():
    event = {"body": '{\n    "input_str": "The analysts of ABN did a great job!."\n}'}
    context = {}
    outcome = lambda_handler(event, context)
    expected_outcome = f'Hello, TMNL Team! Here is your expected output: \n "The analysts of ABN AMRO did a great job!."'
    assert outcome["body"] == expected_outcome


def test_lambda_handler_mixed_case_input():
    event = {
        "body": '{\n    "input_str": "The analysts of VolKsBanK did a great job!."\n}'
    }
    context = {}
    outcome = lambda_handler(event, context)
    expected_outcome = f'Hello, TMNL Team! Here is your expected output: \n "The analysts of de Volksbank did a great job!."'
    assert outcome["body"] == expected_outcome


def test_lambda_handler_wrong_input():
    event = {"body": '{\n    "input_str": "The analysts of IG did a great job!."\n}'}
    context = {}
    outcome = lambda_handler(event, context)
    expected_outcome = f"Invalid input string provided."
    assert outcome["body"] == expected_outcome
