from locust import HttpUser, task, between
import random
import string

# Helper function to generate random data
def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

class BDDLoadTestUser(HttpUser):
    wait_time = between(1, 2)  # Wait time between requests (1 to 2 seconds)

    @task(1)
    def register(self):
        # Generate random registration data
        registration_data = {
            "fullName": generate_random_string(10),
            "userName": generate_random_string(8),
            "email": f"{generate_random_string(5)}@gmail.com",
            "password": generate_random_string(8),
            "phone": f"+1{random.randint(1000000000, 9999999999)}"
        }

        # Send POST request to the /client_register endpoint
        response = self.client.post("/client_registeration", data=registration_data)

        # Log response for debugging
        print(f"Registration status: {response.status_code}")

    @task(2)  # Heavier weight for login task
    def login(self):
        # Generate random login data
        login_data = {
            "userName": generate_random_string(8),
            "email": f"{generate_random_string(5)}@gmail.com",
            "password": generate_random_string(8)
        }

        # Send POST request to the /client_login endpoint
        response = self.client.post("/client_login", data=login_data)

        # Log response for debugging
        if response.status_code == 200:
            print(f"Login successful! Token: {response.json().get('token')}")
        else:
            print(f"Login failed! Status code: {response.status_code}")

