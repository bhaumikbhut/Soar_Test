import random
import string
from behave import given, when, then
import requests
import json
from locust import HttpUser, task, between

# Helper function to generate random strings
def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Step definition for generating random registration data
@given('I generate random user registration data')
def step_impl_generate_random_registration_data(context):
    context.registration_data = {
        "fullName": generate_random_string(10),
        "userName": generate_random_string(8),
        "email": f"{generate_random_string(5)}@gmail.com",
        "password": generate_random_string(8),
        "phone": f"+1{random.randint(1000000000, 9999999999)}"
    }

# Step definition for generating random login data
@given('I generate random login data')
def step_impl_generate_random_login_data(context):
    context.login_data = {
        "userName": generate_random_string(8),
        "email": f"{generate_random_string(5)}@gmail.com",
        "password": generate_random_string(8)
    }

# Step definition for sending the registration request
@when('I send a registration request to the /client_register endpoint')
def step_impl_send_registration_request(context):
    response = requests.post(
        "http://127.0.0.1:5000/client_registeration",  # Update with your Flask app URL
        data=context.registration_data
    )
    context.registration_response = response

# Step definition for sending the login request
@when('I send a login request to the /client_login endpoint')
def step_impl_send_login_request(context):
    response = requests.post(
        "http://127.0.0.1:5000/client_login",  # Update with your Flask app URL
        data=context.login_data
    )
    context.login_response = response

# Step definition for checking the registration response status
@then('the registration should succeed with a status code of 200')
def step_impl_check_registration_response(context):
    assert context.registration_response.status_code == 200, f"Expected status code 200 but got {context.registration_response.status_code}"

# Step definition for checking the login response status
@then('I should receive a token and a status code of 200')
def step_impl_check_login_response(context):
    assert context.login_response.status_code == 200, f"Expected status code 200 but got {context.login_response.status_code}"
    response_json = context.login_response.json()
    assert 'token' in response_json, "No token in response"
