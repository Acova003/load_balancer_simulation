import unittest
from load_balancer.provider import Provider
from load_balancer.balancer import LoadBalancer


class TestProvider(unittest.TestCase):
    
        # Can generate provider
        def test_provider_id(self):
            provider = Provider()
            self.assertIsNotNone(provider.id)
    
        def test_provider_get(self):
            provider = Provider()
            self.assertIsNotNone(provider.get())
    
        def test_provider_check(self):
            provider = Provider()
            self.assertTrue(provider.check())
    
        


if __name__ == '__main__':
    unittest.main()
