# ADRESSES
MAINNET_PUBLIC_RESOLVER_ADDRESS = "0x4EfD25E3D348F8F25a14Fb7655FbA6F72edFE93A"
TESTNET_PUBLIC_RESOLVER_ADDRESS = "0x1e7AE43e3503eFB886104ace36051Ea72b301CDf"
REGTEST_PUBLIC_RESOLVER_ADDRESS = "0xDA7Ce79725418F4F6E13Bf5F520C89Cec5f6A974"

MAINNET_MULTICHAIN_RESOLVER_ADDRESS = "0x99a12Be4C89CbF6cfD11d1F2c029904A7b644368"
TESTNET_MULTICHAIN_RESOLVER_ADDRESS = "0x404308F2A2EEc2CDc3CB53D7D295af11C903414E"
REGTEST_MULTICHAIN_RESOLVER_ADDRESS = "0x83C5541A6c8D2dBAD642f385d8d06Ca9B6C731ee"

TESTNET_RNS_ADDRESS = "0x7D284aAAC6E925aAD802a53C0C69efe3764597B8"
MAINNET_RNS_ADDRESS = "0xCB868AeAbd31E2b66F74E9a55cF064AbB31A4Ad5"
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
MULTICHAIN_RESOLVER_ABI =[
    {
      "inputs": [
        {
          "internalType": "contract AbstractRNS",
          "name": "_rns",
          "type": "address"
        },
        {
          "internalType": "contract AbstractPublicResolver",
          "name": "_publicResolver",
          "type": "address"
        }
      ],
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
          "indexed": "false",
          "internalType": "address",
          "name": "addr",
          "type": "address"
        }
      ],
      "name": "AddrChanged",
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
          "internalType": "bytes4",
          "name": "chain",
          "type": "bytes4"
        },
        {
          "indexed": "false",
          "internalType": "string",
          "name": "addr",
          "type": "string"
        }
      ],
      "name": "ChainAddrChanged",
      "type": "event"
    },
    {
      "anonymous": "false",
      "inputs": [
        {
          "indexed": "false",
          "internalType": "bytes32",
          "name": "node",
          "type": "bytes32"
        },
        {
          "indexed": "false",
          "internalType": "bytes4",
          "name": "chain",
          "type": "bytes4"
        },
        {
          "indexed": "false",
          "internalType": "bytes32",
          "name": "metadata",
          "type": "bytes32"
        }
      ],
      "name": "ChainMetadataChanged",
      "type": "event"
    },
    {
      "anonymous": "false",
      "inputs": [
        {
          "indexed": "false",
          "internalType": "bytes32",
          "name": "node",
          "type": "bytes32"
        },
        {
          "indexed": "false",
          "internalType": "bytes32",
          "name": "content",
          "type": "bytes32"
        }
      ],
      "name": "ContentChanged",
      "type": "event"
    },
    {
      "payable": "false",
      "stateMutability": "nonpayable",
      "type": "fallback"
    },
    {
      "constant": "true",
      "inputs": [
        {
          "internalType": "bytes4",
          "name": "interfaceId",
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
          "name": "contentValue",
          "type": "bytes32"
        }
      ],
      "name": "setContent",
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
        },
        {
          "internalType": "bytes4",
          "name": "chain",
          "type": "bytes4"
        }
      ],
      "name": "chainAddr",
      "outputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
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
          "internalType": "bytes4",
          "name": "chain",
          "type": "bytes4"
        },
        {
          "internalType": "string",
          "name": "addrValue",
          "type": "string"
        }
      ],
      "name": "setChainAddr",
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
        },
        {
          "internalType": "bytes4",
          "name": "chain",
          "type": "bytes4"
        }
      ],
      "name": "chainMetadata",
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
          "internalType": "bytes4",
          "name": "chain",
          "type": "bytes4"
        },
        {
          "internalType": "bytes32",
          "name": "metadataValue",
          "type": "bytes32"
        }
      ],
      "name": "setChainMetadata",
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
        },
        {
          "internalType": "bytes4",
          "name": "chain",
          "type": "bytes4"
        }
      ],
      "name": "chainAddrAndMetadata",
      "outputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        },
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
          "internalType": "bytes4",
          "name": "chain",
          "type": "bytes4"
        },
        {
          "internalType": "string",
          "name": "addrValue",
          "type": "string"
        },
        {
          "internalType": "bytes32",
          "name": "metadataValue",
          "type": "bytes32"
        }
      ],
      "name": "setChainAddrWithMetadata",
      "outputs": [],
      "payable": "false",
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]

# CONSTANTS
RNS_ADDRESS_ZERO = "0x0000000000000000000000000000000000000000"
