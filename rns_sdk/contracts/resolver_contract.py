import binascii

from eth_utils import to_checksum_address

from rns_sdk.exceptions.rns_error import RnsError
from rns_sdk.utils.namehash import namehash
from rns_sdk.utils.rns import is_rns_address


class ResolverContract:
    """
     Provides an easy-to-use interface to the RSK Name Service PublicResolver.
    """

    def __init__(self, web3_provider,
                 resolver_address,
                 resolver_abi):
        """
        Constructor
        :param web3_provider: A web3 provider to use to communicate with the blockchain.
        :param resolver_address: The address of the RNS Resolver.
        :param resolver_abi: The abi of the RNS Resolver.
        """
        self.address = resolver_address
        self.abi = resolver_abi
        self.resolver_contract = web3_provider.eth.contract(
            abi=resolver_abi, address=to_checksum_address(resolver_address))

    def addr(self, name_domain=None) -> str:
        """
        Returns the address associated with an RNS node.
        or 0x00 if address is not set.
        :param name_domain: The RNS' name domain to query.
        :return: rsk address
        """
        if is_rns_address(name_domain):
            eip137hash = namehash(name_domain)
            resolved_address = self.resolver_contract.functions.addr(eip137hash).call()
            return resolved_address
        else:
            raise RnsError("Invalid RNS domain")

    def has(self, name_domain, kind):
        """
        Returns true if the specified node has the specified record type.
        :param name_domain: The RNS' name domain to query.
        :param kind: The record type name, as specified in RNSIP01.
        :return: True if this resolver has a record of the provided type on the provided node.
        """
        eip137hash = namehash(name_domain)
        byte_str_kind = kind.encode()
        byte_str_hex_kind = binascii.hexlify(byte_str_kind)
        str_hex_kind = byte_str_hex_kind.decode("utf-8")

        response = self.resolver_contract.functions.has(eip137hash, str_hex_kind).call()
        return response

    def supports_interface(self, interface_id):
        """
        Returns true if the resolver implements the interface specified by the provided interfaceID (hash).
        :param interface_id: The ID (hash) of the interface to check for.
        :return: True if the contract implements the requested interface.
        """
        return self.resolver_contract.functions.supportsInterface(interface_id).call()

    def set_addr(self, name_domain, addr, from_account):
        """
        Sets the address associated with an RNS domain.
        May only be called by the owner of that node in the RNS registry.
        :param name_domain: The domain to update.
        :param addr: The address to set.
        :param from_account: The spender address
        :return:
        """
        eip137hash = namehash(name_domain)
        response = self.resolver_contract.functions.setAddr(eip137hash, addr).transact({"from": from_account})
        return response

    def set_content(self, name_domain, hash, from_account):
        """
        Sets the hash associated with an RNS domain.
        May only be called by the owner of that node in the RNS registry.
        :param name_domain: The domain to update.
        :param hash: The address to set.
        :param from_account: The spender address
        :return:
        """
        eip137hash = namehash(name_domain)
        response = self.resolver_contract.functions.setContent(eip137hash, hash).transact({"from": from_account})
        return response

    def content(self, name_domain):
        """
        Returns the hash associated with an RNS domain.
        or 0x00 if hash is not set.
        :param name_domain:
        :return:
        """
        eip137hash = namehash(name_domain)
        response = self.resolver_contract.functions.content(eip137hash).call()
        return response
