# ADRESSES
MAINNET_PUBLIC_RESOLVER_ADDRESS = "0xDA7Ce79725418F4F6E13Bf5F520C89Cec5f6A974"
TESTNET_PUBLIC_RESOLVER_ADDRESS = "0xDA7Ce79725418F4F6E13Bf5F520C89Cec5f6A974"
REGTEST_PUBLIC_RESOLVER_ADDRESS = "0xDA7Ce79725418F4F6E13Bf5F520C89Cec5f6A974"

TESTNET_RNS_ADDRESS = "0x77045E71a7A2c50903d88e564cD72fab11e82051"
MAINNET_RNS_ADDRESS = "0x77045E71a7A2c50903d88e564cD72fab11e82051"
REGTEST_RNS_ADDRESS = "0x77045E71a7A2c50903d88e564cD72fab11e82051"

# ABIS
RNS_ABI = [
    {
        "inputs": [],
        "payable": "false",
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": "false",
        "inputs": [
            {
                "indexed": "true",
                "internalType": "bytes32",
                "name": "node",
                "type": "bytes32"
            },
            {
                "indexed": "true",
                "internalType": "bytes32",
                "name": "label",
                "type": "bytes32"
            },
            {
                "indexed": "false",
                "internalType": "address",
                "name": "ownerAddress",
                "type": "address"
            }
        ],
        "name": "NewOwner",
        "type": "event"
    },
    {
        "anonymous": "false",
        "inputs": [
            {
                "indexed": "true",
                "internalType": "bytes32",
                "name": "node",
                "type": "bytes32"
            },
            {
                "indexed": "false",
                "internalType": "address",
                "name": "resolverAddress",
                "type": "address"
            }
        ],
        "name": "NewResolver",
        "type": "event"
    },
    {
        "anonymous": "false",
        "inputs": [
            {
                "indexed": "true",
                "internalType": "bytes32",
                "name": "node",
                "type": "bytes32"
            },
            {
                "indexed": "false",
                "internalType": "uint64",
                "name": "ttlValue",
                "type": "uint64"
            }
        ],
        "name": "NewTTL",
        "type": "event"
    },
    {
        "anonymous": "false",
        "inputs": [
            {
                "indexed": "true",
                "internalType": "bytes32",
                "name": "node",
                "type": "bytes32"
            },
            {
                "indexed": "false",
                "internalType": "address",
                "name": "ownerAddress",
                "type": "address"
            }
        ],
        "name": "Transfer",
        "type": "event"
    },
    {
        "constant": "true",
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "node",
                "type": "bytes32"
            }
        ],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": "false",
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": "true",
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "node",
                "type": "bytes32"
            }
        ],
        "name": "resolver",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": "false",
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": "true",
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "node",
                "type": "bytes32"
            }
        ],
        "name": "ttl",
        "outputs": [
            {
                "internalType": "uint64",
                "name": "",
                "type": "uint64"
            }
        ],
        "payable": "false",
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": "false",
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "node",
                "type": "bytes32"
            },
            {
                "internalType": "address",
                "name": "ownerAddress",
                "type": "address"
            }
        ],
        "name": "setOwner",
        "outputs": [],
        "payable": "false",
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": "false",
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "node",
                "type": "bytes32"
            },
            {
                "internalType": "bytes32",
                "name": "label",
                "type": "bytes32"
            },
            {
                "internalType": "address",
                "name": "ownerAddress",
                "type": "address"
            }
        ],
        "name": "setSubnodeOwner",
        "outputs": [],
        "payable": "false",
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": "false",
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "node",
                "type": "bytes32"
            },
            {
                "internalType": "address",
                "name": "resolverAddress",
                "type": "address"
            }
        ],
        "name": "setResolver",
        "outputs": [],
        "payable": "false",
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": "false",
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "node",
                "type": "bytes32"
            },
            {
                "internalType": "uint64",
                "name": "ttlValue",
                "type": "uint64"
            }
        ],
        "name": "setTTL",
        "outputs": [],
        "payable": "false",
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": "false",
        "inputs": [
            {
                "internalType": "address",
                "name": "_resolver",
                "type": "address"
            }
        ],
        "name": "setDefaultResolver",
        "outputs": [],
        "payable": "false",
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
PUBLIC_RESOLVER_ABI = [
    {
        "inputs": [
            {
                "internalType": "contract AbstractRNS",
                "name": "rnsAddr",
                "type": "address"
            }
        ],
        "payable": "false",
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "payable": "true",
        "stateMutability": "payable",
        "type": "fallback"
    },
    {
        "constant": "true",
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "node",
                "type": "bytes32"
            },
            {
                "internalType": "bytes32",
                "name": "kind",
                "type": "bytes32"
            }
        ],
        "name": "has",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": "false",
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": "true",
        "inputs": [
            {
                "internalType": "bytes4",
                "name": "interfaceID",
                "type": "bytes4"
            }
        ],
        "name": "supportsInterface",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": "false",
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "constant": "true",
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "node",
                "type": "bytes32"
            }
        ],
        "name": "addr",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": "false",
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": "false",
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "node",
                "type": "bytes32"
            },
            {
                "internalType": "address",
                "name": "addrValue",
                "type": "address"
            }
        ],
        "name": "setAddr",
        "outputs": [],
        "payable": "false",
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": "true",
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "node",
                "type": "bytes32"
            }
        ],
        "name": "content",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "payable": "false",
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": "false",
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "node",
                "type": "bytes32"
            },
            {
                "internalType": "bytes32",
                "name": "hash",
                "type": "bytes32"
            }
        ],
        "name": "setContent",
        "outputs": [],
        "payable": "false",
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

# CONSTANTS
RNS_ADDRESS_ZERO = "0x0000000000000000000000000000000000000000"
