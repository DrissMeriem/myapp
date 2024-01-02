import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    @task
    def numerical_integral_task(self):
        self.client.get("api/numericalintegralservice?lower=0&upper=3.14159")
