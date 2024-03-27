# Load Balancer Simulation

## Description

This program simulates a simple load balancer mechanism. It distributes requests among a predefined set of providers based on different strategies: round-robin and random selection. The simulation includes features such as registering service providers, handling requests based on the load balancing strategy, and performing health checks on providers (heartbeat checks). It demonstrates key concepts of load balancing in distributed systems without the need for actual network setup.

## Requirements

-Python 3.6 or higher

## Running the Program

To run the load balancer simulation, follow these steps:

1. Open your terminal or command prompt

2. Install packages with `pip install -r requirements.txt`

3. Navigate to the directory containing the program files `cd load_balancer`

4. Run the program using Python: `python main.py`

Upon running, the program will simulate the registration of providers, selection of providers for handling requests, and the inclusion or exclusion of providers based on heartbeat checks.

These functionalities are broken down into the following steps:

- Step 1: Generate Provider
- Step 2: Register a list of providers
- Step 3: Random invocation
- Step 4: Round Robin invocation
- Step 5: Manual node exclusion / inclusion
- Step 6: Heart beat checker
- Step 7: Improving Heart beat checker
- Step 8: Cluster Capacity Limit

## Example Output

    Registering providers...
    Registered provider with ID: 6b32dc12-1f13-4444-ac97-90c7bc5a3ede
    Registered provider with ID: d9292f4c-88a6-4b02-8cbf-2a0ac144aaa0
    Registered provider with ID: b50a7900-3188-4193-b0dd-1fbb913708e3
    Registered provider with ID: facba093-5be1-4f6a-9ce4-922330581a07
    Registered provider with ID: e4cb4030-17a2-415f-aaaa-5b99387b6437
    Total registered providers: 5
    Provider IDs: ['6b32dc12-1f13-4444-ac97-90c7bc5a3ede', 'd9292f4c-88a6-4b02-8cbf-2a0ac144aaa0', 'b50a7900-3188-4193-b0dd-1fbb913708e3', 'facba093-5be1-4f6a-9ce4-922330581a07', 'e4cb4030-17a2-415f-aaaa-5b99387b6437']


    Demonstrating Load Balancing - Round Robin
    Selection: 6b32dc12-1f13-4444-ac97-90c7bc5a3ede
    Selection: d9292f4c-88a6-4b02-8cbf-2a0ac144aaa0
    Selection: b50a7900-3188-4193-b0dd-1fbb913708e3

    Demonstrating Load Balancing - Random Selection
    Selection: e4cb4030-17a2-415f-aaaa-5b99387b6437
    Selection: 6b32dc12-1f13-4444-ac97-90c7bc5a3ede
    Selection: facba093-5be1-4f6a-9ce4-922330581a07


    Step 5: Manual node exclusion / inclusion
    Excluding provider with ID: 6b32dc12-1f13-4444-ac97-90c7bc5a3ede
    Providers after exclusion: ['d9292f4c-88a6-4b02-8cbf-2a0ac144aaa0', 'b50a7900-3188-4193-b0dd-1fbb913708e3', 'facba093-5be1-4f6a-9ce4-922330581a07', 'e4cb4030-17a2-415f-aaaa-5b99387b6437']
    Including provider with ID: 6b32dc12-1f13-4444-ac97-90c7bc5a3ede back
    Providers after inclusion: ['d9292f4c-88a6-4b02-8cbf-2a0ac144aaa0', 'b50a7900-3188-4193-b0dd-1fbb913708e3', 'facba093-5be1-4f6a-9ce4-922330581a07', 'e4cb4030-17a2-415f-aaaa-5b99387b6437', '6b32dc12-1f13-4444-ac97-90c7bc5a3ede']


    Step 6 & 7: Heartbeat checker (simulated for demonstration)
    Assuming heartbeat checks are occurring; providers may be excluded or included based on their health.
    Current providers (before simulated health checks): ['d9292f4c-88a6-4b02-8cbf-2a0ac144aaa0', 'b50a7900-3188-4193-b0dd-1fbb913708e3', 'facba093-5be1-4f6a-9ce4-922330581a07', 'e4cb4030-17a2-415f-aaaa-5b99387b6437', '6b32dc12-1f13-4444-ac97-90c7bc5a3ede']
    Waiting for a few heartbeat intervals...
    Current providers (after simulated health checks): ['d9292f4c-88a6-4b02-8cbf-2a0ac144aaa0', 'b50a7900-3188-4193-b0dd-1fbb913708e3', 'facba093-5be1-4f6a-9ce4-922330581a07', 'e4cb4030-17a2-415f-aaaa-5b99387b6437', '6b32dc12-1f13-4444-ac97-90c7bc5a3ede']

## Testing

### Running all tests

Navigate to your project root and run: `pytest`

### Individual tests

From root directory, `cd tests`

Testing load balancer `pytest test_balancer.py`

Testing provider `pytest test_provider.py`

Note: The tests are still in development
