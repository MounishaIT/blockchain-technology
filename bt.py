import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis Block", calculate_hash(0, "0", int(time.time()), "Genesis Block"))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = int(time.time())
    hash = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash)

def is_block_valid(new_block, previous_block):
    if previous_block.index + 1 != new_block.index:
        return False
    if previous_block.hash != new_block.previous_hash:
        return False
    if calculate_hash(new_block.index, new_block.previous_hash, new_block.timestamp, new_block.data) != new_block.hash:
        return False
    return True

def main():
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]

    num_of_blocks_to_add = 10

    for i in range(1, num_of_blocks_to_add + 1):
        new_block = create_new_block(previous_block, f"Block {i} Data")
        if is_block_valid(new_block, previous_block):
            blockchain.append(new_block)
            previous_block = new_block
            print(f"Block #{new_block.index} has been added to the blockchain!")
            print(f"Hash: {new_block.hash}\n")
        else:
            print("Invalid block!")

if __name__ == '__main__':
    main()
