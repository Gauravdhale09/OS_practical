class MemoryBlock:
    def __init__(self, start, size, processId=-1):
        self.start = start
        self.size = size
        self.processId = processId

def first_fit(blocks, processId, memorySize):
    for block in blocks:
        if block.processId == -1 and block.size >= memorySize:
            block.processId = processId
            print(f"Memory allocated to Process {processId} from Block {block.start} to {block.start + memorySize - 1}")
            block.size -= memorySize
            block.start += memorySize
            return

    print(f"No available block found for Process {processId}")

def display_memory_blocks(blocks):
    print("Memory Blocks:")
    for i, block in enumerate(blocks):
        print(f"Block {i}: Start={block.start}, Size={block.size}, ProcessID={block.processId}")
    print()

# Main function
if __name__ == "__main__":
    # Initialize memory blocks
    blocks = [
        MemoryBlock(0, 100),
        MemoryBlock(100, 50),
        MemoryBlock(150, 200),
        MemoryBlock(350, 80)
    ]

    print("Initial Memory Allocation:")
    display_memory_blocks(blocks)

    first_fit(blocks, 1, 100)
    first_fit(blocks, 2, 510)
    first_fit(blocks, 3, 20)
    first_fit(blocks, 4, 80)

    print("Final Memory Allocation:")
    display_memory_blocks(blocks)
