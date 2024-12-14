import streamlit as st

class NextFitMemoryAllocator:
    def __init__(self, memory_blocks):
        self.memory_blocks = memory_blocks
        self.block_capacities = memory_blocks.copy()
        self.last_allocated_index = 0

    def allocate_memory(self, process_size):
        n = len(self.memory_blocks)
        start_index = self.last_allocated_index

        for i in range(n):
            index = (start_index + i) % n
            if self.memory_blocks[index] >= process_size:
                self.memory_blocks[index] -= process_size  # Allocate memory
                self.last_allocated_index = index  # Update last allocated index
                return f"Allocated process of size {process_size} to block {index + 1}."
        return f"Failed to allocate process of size {process_size}. Not enough memory."

    def reset(self):
        self.memory_blocks = self.block_capacities.copy()
        self.last_allocated_index = 0


# Streamlit UI
st.title("Next Fit Memory Allocator")

# Initialize session state
if "allocator" not in st.session_state:
    st.session_state.allocator = None
    st.session_state.memory_blocks = []
    st.session_state.used_memory = []

# Memory block input
block_sizes = st.text_input("Enter Memory Block Sizes (comma-separated)", placeholder="e.g., 100,500,300")
if st.button("Initialize"):
    try:
        # Parse memory blocks
        blocks = list(map(int, block_sizes.split(",")))
        st.session_state.allocator = NextFitMemoryAllocator(blocks)
        st.session_state.memory_blocks = blocks.copy()
        st.session_state.used_memory = [0] * len(blocks)  # Initialize all as unused
        st.success("Memory Blocks Initialized!")
    except ValueError:
        st.error("Invalid input. Please enter valid numbers separated by commas.")

# Display progress bars for memory blocks
if st.session_state.allocator:
    st.subheader("Memory Blocks Status")
    for i, block in enumerate(st.session_state.memory_blocks):
        # Calculate usage percentage
        used = st.session_state.allocator.block_capacities[i] - block
        st.session_state.used_memory[i] = used
        st.progress(int((used / st.session_state.allocator.block_capacities[i]) * 100), text=f"Block {i+1}: {used}/{st.session_state.allocator.block_capacities[i]}")

    # Input for memory allocation
    process_size = st.number_input("Enter Process Size to Allocate", min_value=1, step=1)
    if st.button("Allocate"):
        result = st.session_state.allocator.allocate_memory(process_size)
        st.info(result)

    # Reset memory blocks
    if st.button("Reset"):
        st.session_state.allocator.reset()
        st.session_state.memory_blocks = st.session_state.allocator.block_capacities.copy()
        st.session_state.used_memory = [0] * len(st.session_state.allocator.block_capacities)
        st.success("Memory blocks have been reset!")
