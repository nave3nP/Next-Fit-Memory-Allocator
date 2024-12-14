import tkinter as tk
from tkinter import ttk, messagebox


class NextFitMemoryAllocator:
    def __init__(self, memory_blocks):
        self.memory_blocks = memory_blocks  # List of block sizes
        self.block_capacities = memory_blocks.copy()  # Store original capacities
        self.last_allocated_index = 0  # Start from the first block

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


class MemoryAllocatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Next Fit Memory Allocator")

        # Example memory blocks
        self.memory_blocks = [100, 500, 200, 300, 600]
        self.allocator = None  # Placeholder for allocator instance
        self.bars = []  # Progress bars for visualization

        self.create_widgets()

    def create_widgets(self):
        # Title
        tk.Label(self.root, text="Next Fit Memory Allocator", font=("Arial", 16)).pack(pady=10)

        # Initialization Frame
        init_frame = tk.Frame(self.root)
        init_frame.pack(pady=10)

        tk.Label(init_frame, text="Memory Blocks (comma-separated):").grid(row=0, column=0)
        self.blocks_entry = tk.Entry(init_frame, width=30)
        self.blocks_entry.grid(row=0, column=1)

        init_button = tk.Button(init_frame, text="Initialize", command=self.initialize_memory)
        init_button.grid(row=0, column=2, padx=10)

        # Frame for progress bars
        self.bar_frame = tk.Frame(self.root)
        self.bar_frame.pack(pady=10)

        # Input Section
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        tk.Label(self.input_frame, text="Process Size: ").grid(row=0, column=0)
        self.process_size_entry = tk.Entry(self.input_frame, width=10)
        self.process_size_entry.grid(row=0, column=1)

        allocate_button = tk.Button(self.input_frame, text="Allocate", command=self.allocate_memory)
        allocate_button.grid(row=0, column=2, padx=10)

        # Reset Button
        reset_button = tk.Button(self.input_frame, text="Reset All", command=self.reset_memory)
        reset_button.grid(row=0, column=3, padx=10)

    def initialize_memory(self):
        try:
            # Get block sizes from user input
            block_sizes = list(map(int, self.blocks_entry.get().split(",")))
            if not block_sizes:
                raise ValueError("No blocks provided!")

            # Initialize allocator
            self.memory_blocks = block_sizes
            self.allocator = NextFitMemoryAllocator(self.memory_blocks)

            # Clear existing progress bars
            for widget in self.bar_frame.winfo_children():
                widget.destroy()
            self.bars = []

            # Create new progress bars
            for i, capacity in enumerate(self.memory_blocks):
                frame = tk.Frame(self.bar_frame)
                frame.pack(pady=5, fill=tk.X)

                # Block Label
                tk.Label(frame, text=f"Block {i + 1}:").pack(side=tk.LEFT, padx=5)

                # Progress Bar
                progress_var = tk.DoubleVar()
                progress_bar = ttk.Progressbar(
                    frame, variable=progress_var, maximum=capacity, length=400
                )
                progress_bar.pack(side=tk.LEFT, padx=5)
                self.bars.append((progress_bar, progress_var, capacity))

                # Text showing free/used memory
                tk.Label(frame, text=f" / {capacity} units").pack(side=tk.LEFT)

            # Initial display update
            self.update_memory_display()

        except ValueError as e:
            messagebox.showerror("Invalid Input", f"Error: {e}")

    def update_memory_display(self):
        if not self.allocator:
            return

        for i, (progress_bar, progress_var, capacity) in enumerate(self.bars):
            used = capacity - self.memory_blocks[i]  # Calculate used memory
            progress_var.set(used)  # Update progress bar

    def allocate_memory(self):
        if not self.allocator:
            messagebox.showerror("Not Initialized", "Please initialize memory blocks first!")
            return

        try:
            process_size = int(self.process_size_entry.get())
            result = self.allocator.allocate_memory(process_size)
            messagebox.showinfo("Allocation Result", result)
            self.update_memory_display()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer for process size.")

    def reset_memory(self):
        if not self.allocator:
            messagebox.showerror("Not Initialized", "Please initialize memory blocks first!")
            return

        self.allocator.reset()
        self.update_memory_display()
        messagebox.showinfo("Reset Successful", "Memory blocks have been reset to their original states.")


if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryAllocatorApp(root)
    root.mainloop()
