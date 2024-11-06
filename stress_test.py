from locust import HttpUser, task, between
import random
import string

# Function to generate a random string of a given length
def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Class that defines the behavior of the virtual user
class StressTestUser(HttpUser):
    wait_time = between(1, 2)  # Random wait time between requests (1 to 2 seconds)

    @task(1)  # The task to run during each iteration
    def login(self):
        # Generate random login data for username, email, and password
        user_name = generate_random_string(8)  # Random username
        email = f"{generate_random_string(5)}@gmail.com"  # Random email
        password = generate_random_string(8)  # Random password

        # Send POST request to the /client_login endpoint with the generated data
        response = self.client.post("/client_login", data={
            "userName": user_name,
            "email": email,
            "password": password
        })

        # Print response status for debugging (you can remove this in production)
        print(f"Login attempt: Username: {user_name}, Email: {email}, Status Code: {response.status_code}")
        if response.status_code != 200:
            print(response.text)

