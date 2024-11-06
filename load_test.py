from locust import HttpUser, task, between
import random
import string

# Function to generate random string of a given length
def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)  # Wait time between task executions

    @task(1)
    def register(self):
        # Generate random data for registration
        full_name = generate_random_string(10)
        user_name = generate_random_string(8)
        email = f"{generate_random_string(5)}@gmail.com"
        password = generate_random_string(8)
        phone = f"+1{random.randint(1000000000, 9999999999)}"

        # Send POST request to the /client_register endpoint
        response = self.client.post("/client_registeration", data={
            "fullName": full_name,
            "userName": user_name,
            "email": email,
            "password": password,
            "phone": phone
        })

        # Print response status for debugging
        print(response.status_code)
        if response.status_code != 200:
            print(response.text)

# For running with a load test command like:
# locust -f load_test.py --host=http://127.0.0.1:5000
