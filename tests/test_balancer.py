import unittest
from load_balancer.provider import Provider
from load_balancer.balancer import LoadBalancer


class TestBalancer(unittest.TestCase):

    # Can handle multiple requests
    def test_can_accept_request(self):
        provider = Provider()
        balancer = LoadBalancer(10)
        balancer.register_provider(provider)
        self.assertTrue(balancer.can_accept_request())

if __name__ == '__main__':
    unittest.main()