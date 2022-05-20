The repo contains source code for the given tech task.

Clone the repo and change directory to downloaded one.

    git clone https://github.com/engineerhead/composable-task.git
    cd composable-task
To test  interpreter with provided Bytecode simply run

    python3 interpreter.py

To test with your own byte code, provide the file path of byte code as last argument

    python3 interpreter.py '/path/to/file'

To test the functions that prints put lines in the files matching the given extension, 

    python3 file_lines.py '/path/to/dir' '.ext'
where 3rd and 4th argument are path to directory and extension respectively.

As far as questions in task# 3 are concerned,  as per my understanding the concurrency model mentioned closely resembles Hoare's CSP i.e Communicating sequential processes.

Blocking nature of SEND_CHANNEL and RECIEVE_CHANNEL will likely be accomplished using an infinite loop which keeps sleeping and waking up to see if there is value to send or receive.

Regarding spawning concurrent functions, the following have to be executed after first function is launched

 - Interrupt the first function
 -  Save the stack state 
 - Launch the second function

After few instructions have been executed by 2nd function

 - Save the stack
 - Interrupt the execution
 - Restore the old stack
 - Continue with old function's execution

## Hashing in Blockchain
Hashing is the process of converting an input data of variable length into an output of fixed length.

 - Fixed length output(deterministic) means that tracing  the hash
   becomes easier whether the input was single word or huge amount of
   data.
 - Hashing is like one way street meaning input can't be inferred by using output. This makes blockchain secure.
 - Address on the blockchain are also derived from hashing.
 - Hashing is also critical in blockchain as valid nonce is found out by computing several hashes during mining. It enables to reach a consensus in blockchain.
 - Large amounts of data can stored easily in blockchain using hashing.

## UTXO in Blockchain
UTXO means unspent transaction output that can be utilised as input in a new transaction. UTXOs actually describe where each blockchain transaction starts and ends. It also serves a mechanism to keep track of where coins are given at a time.

## Block in Bitcoin
A block in bitcoin contains the data related to a transaction. They are mined with all the transactions being stored permanently. A block is connected to previous and next blocks using their hashes thus forming blockchain.

Bitcoin block contains a Merkle root which is the hash of all the transaction hashes. The hashes of a transaction are stored in the form of upside down Merkle Tree. Merkle root is at its top. Due to tree like nature, it is easy to traverse and verifications can be done quickly. [Source](https://medium.com/coinmonks/structure-of-a-bitcoin-block-7f6c4938a5fd)
![Merkle Tree](https://miro.medium.com/max/1164/1*5tARHb0EV_-svRNgmgL_Ng.jpeg)
## POW vs POS

Since Bitcoin is a decentralised anonymous system, stake holders i.e user and miners do not know each other and  everyone is trust less.  If user sends or recieve a transaction, how to know when it is settled? If some other user is informing that it is settled, we can't trust that information. This is called Byzantine Generals Problem.
Bitcoin uses Proof-of-Work mechanism to deal with trust. A miner must generate a hash that is within the  specified range. 
 - PoW lays out the ground work upon which decentralised  users can agree on which version of blockchain is valid.
 -  PoW imposes a cost on producing blocks thus preventing spam, Dos, and making it scarce.

Proof-of-Stake is an alternative consensus mechanism which hands over the control of network to owners of the tokens. It is an improvement as PoS doesn't require hardware and energy at the scale of PoW network to reach consensus. However, it creates governance problems as major stake holders can influence network to their benefit.
