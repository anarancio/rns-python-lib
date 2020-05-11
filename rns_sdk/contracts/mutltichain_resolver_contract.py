import binascii

from eth_utils import to_checksum_address

from rns_sdk.constants.network_constants import RSK_CHAIN_ID
from rns_sdk.contracts.resolver_contract import ResolverContract
from rns_sdk.exceptions.rns_error import RnsError
from rns_sdk.utils.namehash import namehash
from rns_sdk.utils.rns import is_rns_address


class MultichainResolverContract(ResolverContract):
    """
     Provides an easy-to-use interface to the RSK Name Service Multichain Resolver.
    """

    def __init__(self, web3_provider,
                 resolver_address,
                 resolver_abi):
        """
        Constructor
        :param web3_provider: A web3 provider to use to communicate with the blockchain.
        :param resolver_address: The address of the RNS Multichain Resolver.
        :param resolver_abi: The abi of the RNS Multichain Resolver.
        """
        super().__init__(web3_provider, resolver_address, resolver_abi)

    def chain_addr(self, name_domain: str, chain_id: int = RSK_CHAIN_ID) -> str:
        """
        Returns the address associated with an RNS node for a specific chain id.
        or 0x00 if address is not set.

        :param chain_id: The RNS' chain id. Defaults to rsk chain id.
        :param name_domain: The RNS' name domain to query.

        :return: rsk address
        """
        if is_rns_address(name_domain):
            eip137hash = namehash(name_domain)
            resolved_address = self.resolver_contract.functions.chainAddr(eip137hash, chain_id).call()
            return resolved_address
        else:
            raise RnsError("Invalid RNS domain")
