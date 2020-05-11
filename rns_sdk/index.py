from web3 import Web3

from rns_sdk.constants.network_constants import MAINNET_ENV, TESTNET_ENV, RSK_CHAIN_ID
from rns_sdk.constants.rns_constants import MAINNET_RNS_ADDRESS, RNS_ABI, PUBLIC_RESOLVER_ABI, \
    MAINNET_PUBLIC_RESOLVER_ADDRESS, TESTNET_PUBLIC_RESOLVER_ADDRESS, TESTNET_RNS_ADDRESS, \
    MAINNET_MULTICHAIN_RESOLVER_ADDRESS, MULTICHAIN_RESOLVER_ABI, TESTNET_MULTICHAIN_RESOLVER_ADDRESS
from rns_sdk.contracts.mutltichain_resolver_contract import MultichainResolverContract
from rns_sdk.contracts.resolver_contract import ResolverContract
from rns_sdk.contracts.rns_contract import RnsContract
from rns_sdk.utils.rns import is_rns_address


class RnsPy:
    """
     Provides an easy-to-use interface to the RSK Name Service.
    """

    def __init__(self,
                 web3: Web3,
                 environment: str = MAINNET_ENV,
                 ):
        """
        Constructor
        :param web3: A web3 instance
        :param environment: a network_constants.py environment mode.
        """
        self.web3 = web3
        self.rns_contract = None
        self.public_resolver = None
        self.multichain_resolver = None

        if environment == MAINNET_ENV:
            self.rns_contract = RnsContract(web3, MAINNET_RNS_ADDRESS, RNS_ABI)
            self.public_resolver = ResolverContract(web3, MAINNET_PUBLIC_RESOLVER_ADDRESS, PUBLIC_RESOLVER_ABI)
            self.multichain_resolver = MultichainResolverContract(web3, MAINNET_MULTICHAIN_RESOLVER_ADDRESS,
                                                                  MULTICHAIN_RESOLVER_ABI)
        elif environment == TESTNET_ENV:
            self.rns_contract = RnsContract(web3, TESTNET_RNS_ADDRESS, RNS_ABI)
            self.public_resolver = ResolverContract(web3, TESTNET_PUBLIC_RESOLVER_ADDRESS, PUBLIC_RESOLVER_ABI)
            self.multichain_resolver = MultichainResolverContract(web3, TESTNET_MULTICHAIN_RESOLVER_ADDRESS,
                                                                  MULTICHAIN_RESOLVER_ABI)

    def set_public_resolver(self, address):
        """
               Override public resolver. For example, if you want to use it on regtest
               :param address: public resolver address.
               """

        self.public_resolver = ResolverContract(self.web3, address, PUBLIC_RESOLVER_ABI)

    def set_rns(self, address):
        """
               Override rns instance. For example, if you want to use it on regtest
               :param address: rns address.
               """
        self.rns_contract = RnsContract(self.web3, address, RNS_ABI)

    def set_multichain_resolver(self, address):
        """
               Override multichain resolver. For example, if you want to use it on regtest
               :param address: multichain resolver address.
               """
        self.multichain_resolver = MultichainResolverContract(self.web3, address, MULTICHAIN_RESOLVER_ABI)

    def addr(self, name_domain=None) -> str:
        """
        Returns the address associated with the domain
        This function gets first the resolver associated with the domain and then try to resolve the address on it.

        :param name_domain: The RNS' name domain to query.
        :return: resolved address
        """
        self.__init_sanity_assertions()
        if not is_rns_address(name_domain):
            raise Exception("Bad name_domain")

        resolver_address = self.rns_contract.resolver(name_domain)
        if resolver_address == self.public_resolver.address:
            # Public resolver was set
            resolved_address = self.public_resolver.addr(name_domain)
            return resolved_address
        elif resolver_address == self.multichain_resolver.address:
            # Public resolver was set
            resolved_address = self.multichain_resolver.addr(name_domain)
            return resolved_address

    def chain_addr(self, name_domain: str, chain_id: int = RSK_CHAIN_ID) -> str:
        """
        Returns the address associated with an RNS node for a specific chain id.
        or 0x00 if address is not set.

        :param chain_id: The RNS' chain id. Defaults to rsk chain id.
        :param name_domain: The RNS' name domain to query.

        :return: rsk address
        """
        return self.multichain_resolver.chain_addr(name_domain, chain_id)

    def __init_sanity_assertions(self):
        assert self.public_resolver is not None, "Forgot to call set_public_resolver() ?"
        assert self.rns_contract is not None, "Forgot to call set_rns() ?"
        assert self.public_resolver.address is not None, "Forgot to call set_public_resolver() ?"
        assert self.public_resolver.abi is not None, "Forgot to call set_public_resolver() ?"
        assert self.rns_contract.address is not None, "Forgot to call set_rns() ?"
        assert self.rns_contract.abi is not None, "Forgot to call set_rns() ?"
