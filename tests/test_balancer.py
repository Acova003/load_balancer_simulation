import threading
import pytest
from load_balancer.balancer import LoadBalancer
from load_balancer.provider import Provider

# Define a mock request handler function
def mock_request_handler(load_balancer):
    provider = load_balancer.get_round_robin()  # Simulate requesting a provider
    # Process the request (mock implementation)
    return f"Request processed by {provider.get()}"

# Test case for handling multiple requests simultaneously
def test_multiple_requests():
    # Initialize LoadBalancer and register providers
    max_parallel_requests_per_provider = 5  # Adjust as needed
    balancer = LoadBalancer(max_parallel_requests_per_provider)
    num_providers = 3  # Adjust as needed
    providers = [Provider() for _ in range(num_providers)]
    for provider in providers:
        balancer.register_provider(provider)

    # Define the number of simultaneous requests to simulate
    num_simultaneous_requests = 10  # Adjust as needed

    # Function to simulate a single request
    def simulate_request():
        result = mock_request_handler(balancer)
        return result

    # Use threading to simulate multiple requests simultaneously
    results = []
    threads = []
    for _ in range(num_simultaneous_requests):
        thread = threading.Thread(target=lambda: results.append(simulate_request()))
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Validate results
    for result in results:
        assert "Request processed by" in result  # Check if each result indicates successful processing

# Run the test
if __name__ == "__main__":
    pytest.main([__file__])
