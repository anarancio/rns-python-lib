import binascii

from web3 import Web3

from eth_utils import to_checksum_address

from rns_sdk.exceptions.rns_error import RnsError
from rns_sdk.utils.namehash import namehash
from rns_sdk.utils.rns import is_rns_address


class RnsContract:
    """
     Provides an easy-to-use interface to the RSK Name Service.
    """

    def __init__(self, web3_provider,
                 rns_address,
                 rns_abi):
        """
        Constructor
        :param web3_provider: A web3 provider to use to communicate with the blockchain.
        :param rns_address: The address of the RNS contract. Defaults to the MainNet one.
        :param rns_abi: The abi of the RNS Resolver. Defaults to the mainnet RNS 's abi.
        """
        self.address = rns_address
        self.abi = rns_abi
        self.rns_contract = web3_provider.eth.contract(
            abi=rns_abi, address=to_checksum_address(rns_address))

    def resolver(self, name_domain=None) -> str:
        """
        Returns the address associated with the domain resolver.
        or 0x00 if resolver is not set.
        :param name_domain: The RNS' name domain to query.
        :return: resolver address
        """
        if is_rns_address(name_domain):
            eip137hash = namehash(name_domain)
            resolver_resolved_address = self.rns_contract.functions.resolver(eip137hash).call()
            return resolver_resolved_address
        else:
            raise RnsError("Invalid RNS domain")


