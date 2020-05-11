<img src="/logo.png" alt="logo" height="200" />

# `RNS-SDK-py`


Implementations for local resolvers for the RIF Name Service, available for python backends.


## Requirements

- Python Version: 3.7
- Pip Version: lastest
- VirtualEnv Version: lastest

## Testing

To run unit tests, clone this repository.

Run Rsk Node and deploy resolver contracts.
Check constants folder to specify, RPC_CLIENT_URL in client_constants.py file and RNS_RESOLVER_ADDRESS in
rns_constants.py file.

Add the PYTHONPATH environment variable of your operating system to the path of the folder where you cloned the project, this will allow the tests to directly invoke the file by console.

Run:

```
pip install virtualenv
```

```
virtualenv -p /yourLocalPythonPath/python3.7 rns_sdk_py_env
```

```
source rns_sdk_py_env/bin/activate
```

```
pip install -r requirements.txt
```

```
python setup.py develop

```

```
python3.7 tests/units/test_resolver_contract.py -v
```

Note: 

The library does not include domain names registration, therefore, you must register your own domains to make the tests work for now.


## Usage and Getting Started
Run the code from a Python console, or import it into your project.


### Usages

1. Using the library interface RnsPy

```

# MainNet initialization

from rns_sdk.constants.network_constants import MAINNET_ENV
rpc_endpoint = "https://public-node.rsk.co"
web3 = Web3(Web3.HTTPProvider(rpc_endpoint))
rnspy = RnsPy(web3, MAINNET_ENV)


# TestNet initialization

from rns_sdk.constants.network_constants import TESTNET_ENV
rpc_endpoint = "https://public-node.testnet.rsk.co"
web3 = Web3(Web3.HTTPProvider(rpc_endpoint))
rnspy = RnsPy(web3, TESTNET_ENV)


# RegTest initialization

from rns_sdk.constants.network_constants import REGTEST_ENV
rpc_endpoint = "http://localhost:4444"
web3 = Web3(Web3.HTTPProvider(rpc_endpoint))
rnspy = RnsPy(web3, REGTEST_ENV)
rnspy.set_public_resolver(REGTEST_PUBLIC_RESOLVER_ADDRESS)
rnspy.set_rns(REGTEST_RNS_ADDRESS)
rnspy.set_multichain_resolver(REGTEST_MULTICHAIN_RESOLVER_ADDRESS)

# Resolving a domain name

result = rnspy.addr("testdomain.rsk")

# Multicrypto resolve

from rns_sdk.constants.network_constants RSK_CHAIN_ID

result = rnspy.chain_addr("testdomain.rsk", RSK_CHAIN_ID)

```

2. Using the RNS smart contract wrappers


```

# Public Resolver 

from rns_sdk.contracts.resolver_contract import ResolverContract
rpc_endpoint = "http://localhost:4444"
web3 = Web3(Web3.HTTPProvider(rpc_endpoint))
resolver = ResolverContract(web3, REGTEST_PUBLIC_RESOLVER_ADDRESS, PUBLIC_RESOLVER_ABI)
resolver.addr("foo.rsk")

# RNS

from rns_sdk.contracts.rns_contract import RnsContract
rpc_endpoint = "http://localhost:4444"
web3 = Web3(Web3.HTTPProvider(rpc_endpoint))
rns_contract = RnsContract(web3, REGTEST_RNS_ADDRESS, RNS_ABI)
rns_contract.resolver("lumino.rsk")

```


## Build Source

To generate a compiled package you must use

```
python3.7 setup.py sdist bdist_wheel

```

## Contracts

### RNS.sol
Implementation of the RNS Registry, the central contract used to look up resolvers and owners for domains.

### PublicResolver.sol
Simple resolver implementation that allows the owner of any domain to configure how its name should resolve. One deployment of this contract allows any number of people to use it, by setting it as their resolver in the registry.


### MultichainResolver.sol
Resolver capable of resolve addresses from other blockchains using a chain id as an identifier

## Documentation

For more information, see [RNS Docs](https://docs.rns.rifos.org).

## Related links

- [RSK](https://rsk.co)
    - [Docs](https://docs.rsk.co)
- [RIF](https://rifos.org)
    - [Docs](https://www.rifos.org/documentation/)
    - [Whitepaper](https://docs.rifos.org/rif-whitepaper-en.pdf)
    - [Testnet faucet](https://faucet.rifos.org)
- RNS
    - [Docs](https://docs.rns.rifos.org)
    - [Manager](https://rns.rifos.org)
    - [Testnet registrar](https://testnet.rns.rifos.org)

