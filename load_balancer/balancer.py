import random
import threading
from time import sleep

class LoadBalancer:
    def __init__(self, max_parallel_requests_per_provider):
        self.providers = [] # Step 2: List of providers
        self.max_providers = 10  # Step 2: Limit on number of providers
        self.current_index = 0  # For round-robin selection
        self.max_parallel_requests_per_provider = max_parallel_requests_per_provider  # Step 8: Cluster Capacity Limit
        self.current_requests_by_provider = {}  # Tracks active requests per provider
        self.heartbeat_interval = 10  # Step 6: Heartbeat interval in seconds
        self.providers_seen_count = {}  # Step 7: Tracks health-check passes for each provider
        self.heartbeat_thread = threading.Thread(target=self.check_providers, daemon=True) # background daemon thread for step 6 heartbeat checker
        self.heartbeat_thread.start()  # Step 6: Starts the heartbeat checking in a separate thread

    # Step 2: Register a list of providers
    def register_provider(self, provider):
        if len(self.providers) < self.max_providers:
            self.providers.append(provider)
            self.current_requests_by_provider[provider] = 0  
        else:
            raise Exception('Max number of providers reached')

    # Step 3: Random Invocation
    def get_random(self):
        if self.providers:
            chosen_provider = random.choice(self.providers)
            return chosen_provider
        else:
            raise Exception('No providers available')

    # Step 8: Cluster Capacity Limit
    def can_accept_request(self):
        total_capacity = self.max_parallel_requests_per_provider * len(self.providers)
        current_requests = sum(self.current_requests_by_provider.values())
        return current_requests < total_capacity

    # Step 4: Round Robin Invocation
    def get_round_robin(self):
        if not self.can_accept_request():
            raise Exception("Capacity limit reached")
        if self.providers:
            chosen_provider = self.providers[self.current_index]
            self.current_index = (self.current_index + 1) % len(self.providers)
            return chosen_provider
        else:
            raise Exception('No providers available')

    # Step 5: Manual node exclusion / inclusion
    def exclude_provider(self, provider):
        if provider in self.providers:
            self.providers.remove(provider)
            if provider in self.current_requests_by_provider:  
                del self.current_requests_by_provider[provider]

    def include_provider(self, provider):
        if provider not in self.providers and len(self.providers) < self.max_providers:
            self.providers.append(provider)
            self.current_requests_by_provider[provider] = 0  

    # Step 6 & 7: Heartbeat checker and improvement
    def check_providers(self):
        while True:
            for provider in list(self.providers_seen_count.keys()):
                if provider.check():
                    if self.providers_seen_count[provider] == 1:
                        self.include_provider(provider)
                        del self.providers_seen_count[provider] 
                    else:
                        self.providers_seen_count[provider] = 1 
                else:
                    self.exclude_provider(provider)
                    self.providers_seen_count[provider] = 0  
            sleep(self.heartbeat_interval)



    


