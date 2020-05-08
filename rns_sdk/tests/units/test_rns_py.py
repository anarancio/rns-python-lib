import unittest
from web3 import Web3

from rns_sdk.constants.network_constants import REGTEST_ENV
from rns_sdk.constants.rns_constants import REGTEST_PUBLIC_RESOLVER_ADDRESS, \
    REGTEST_RNS_ADDRESS
from rns_sdk.index import RnsPy


class TestRnsPy(unittest.TestCase):
    """
    Test methods of interface to the RSK Name Service.
    """

    def test_resolve_domain(self):
        result = rnspy.addr(lumino_domain)
        self.assertEqual(result, "0x3278deEd4eE3DE26Bb53fFb82f4Be82a6bB66D19")


if __name__ == '__main__':
    rpc_endpoint = "http://localhost:4444"
    web3 = Web3(Web3.HTTPProvider(rpc_endpoint))
    rnspy = RnsPy(web3, REGTEST_ENV)
    rnspy.set_public_resolver(REGTEST_PUBLIC_RESOLVER_ADDRESS)
    rnspy.set_rns(REGTEST_RNS_ADDRESS)

    lumino_domain = "lumino.rsk"
    unittest.main()
