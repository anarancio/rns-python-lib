import unittest
from web3 import Web3

from rns_sdk.constants.rns_constants import REGTEST_PUBLIC_RESOLVER_ADDRESS, PUBLIC_RESOLVER_ABI, REGTEST_RNS_ADDRESS, \
    RNS_ABI
from rns_sdk.contracts.resolver_contract import ResolverContract
from rns_sdk.contracts.rns_contract import RnsContract


class TestResolverContract(unittest.TestCase):
    """
    Test methods of interface to the RSK Name Service.
    """

    def test_addr_not_set(self):
        result = resolver.addr(foo_domain)
        self.assertEqual(result, "0x0000000000000000000000000000000000000000")

    def test_has_other_kind(self):
        result = resolver.has(foo_domain, "other")
        self.assertFalse(result)

    def test_supports_interface(self):
        result = resolver.supports_interface("0x3b3b57de")
        self.assertTrue(result)

    def test_unsupports_interface(self):
        result = resolver.supports_interface("0x3b3b57d1")
        self.assertFalse(result)

    def test_get_rns_registrar(self):
        result = rns_contract.resolver("lumino.rsk")
        self.assertEqual(result, "0xDA7Ce79725418F4F6E13Bf5F520C89Cec5f6A974")

    def test_set_content(self):
        response = resolver.set_content(foo_domain, a_hash, accounts[0])
        self.assertIsNotNone(response)


if __name__ == '__main__':
    rpc_endpoint = "http://localhost:4444"
    web3 = Web3(Web3.HTTPProvider(rpc_endpoint))

    resolver = ResolverContract(web3, REGTEST_PUBLIC_RESOLVER_ADDRESS, PUBLIC_RESOLVER_ABI)
    rns_contract = RnsContract(web3, REGTEST_RNS_ADDRESS, RNS_ABI)

    foo_domain = "foo.rsk"
    a_hash = "0x89ad40fcd44690fb5aa90e0fa51637c1b2d388f8056d68430d41c8284a6a7d5e";
    accounts = web3.eth.accounts

    unittest.main()
