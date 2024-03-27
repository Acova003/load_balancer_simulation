from time import sleep
from balancer import LoadBalancer
from provider import Provider

# Initialize LoadBalancer with a specific capacity
lb = LoadBalancer(max_parallel_requests_per_provider=5)

# Registering providers to the LoadBalancer
print("Registering providers...")
for i in range(5):  # Adjust the number based on your needs
    provider = Provider()
    lb.register_provider(provider)
    print(f"Registered provider with ID: {provider.id}")

print(f"Total registered providers: {len(lb.providers)}")
print(f"Provider IDs: {[p.id for p in lb.providers]}")
print("\n")

# Demonstrating Round Robin and Random selection
print("Demonstrating Load Balancing - Round Robin")
for _ in range(3):  # Make three selections
    print("Selection:", lb.get_round_robin().get())

print("\nDemonstrating Load Balancing - Random Selection")
for _ in range(3):  # Make three random selections
    print("Selection:", lb.get_random().get())
print("\n")

# Step 5: Manual node exclusion / inclusion
print("Step 5: Manual node exclusion / inclusion")
# Assuming the first provider in the list will be excluded and then included back
provider_to_exclude = lb.providers[0]
print(f"Excluding provider with ID: {provider_to_exclude.id}")
lb.exclude_provider(provider_to_exclude)
print("Providers after exclusion:", [p.id for p in lb.providers])

print(f"Including provider with ID: {provider_to_exclude.id} back")
lb.include_provider(provider_to_exclude)
print("Providers after inclusion:", [p.id for p in lb.providers])
print("\n")

# Note for Step 6 & 7: Heartbeat checker runs in the background and affects provider availability.
# The actual changes depend on the providers' responses to health checks.
# The following is a simulated output assuming we could control or observe health checks:

print("Step 6 & 7: Heartbeat checker (simulated for demonstration)")
print("Assuming heartbeat checks are occurring; providers may be excluded or included based on their health.")
print("Current providers (before simulated health checks):", [p.id for p in lb.providers])

# Simulate time passing for a few heartbeat intervals
print("Waiting for a few heartbeat intervals...")
sleep(5)  # Adjust the sleep time based on your heartbeat_interval and needed demonstration time

print("Current providers (after simulated health checks):", [p.id for p in lb.providers])


