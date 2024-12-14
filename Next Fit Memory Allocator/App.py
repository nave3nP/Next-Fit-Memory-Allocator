import tkinter as tk
from tkinter import messagebox


class NextFitMemoryAllocator:
    def __init__(self, memory_blocks):
        self.memory_blocks = memory_blocks  # List of block sizes
        self.last_allocated_index = 0  # Start from the first block

    def allocate_memory(self, process_size):
        n = len(self.memory_blocks)
        start_index = self.last_allocated_index

        for i in range(n):
            index = (start_index + i) % n
            if self.memory_blocks[index] >= process_size:
                self.memory_blocks[index] -= process_size
                self.last_allocated_index = index
                return f"Allocated process of size {process_size} to block {index + 1}."
        return f"Failed to allocate process of size {process_size}. Not enough memory."

    def get_memory_state(self):
        return self.memory_blocks


class MemoryAllocatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Next Fit Memory Allocator")

        self.memory_blocks = [100, 500, 200, 300, 600]  # Example memory sizes
        self.allocator = NextFitMemoryAllocator(self.memory_blocks)

        self.block_canvas = None  # For graphical representation
        self.create_widgets()

    def create_widgets(self):
        # Title
        tk.Label(self.root, text="Next Fit Memory Allocator", font=("Arial", 16)).pack(pady=10)

        # Memory Canvas
        self.block_canvas = tk.Canvas(self.root, width=600, height=200, bg="white")
        self.block_canvas.pack(pady=10)
        self.update_memory_display()

        # Input Section
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        tk.Label(self.input_frame, text="Process Size: ").grid(row=0, column=0)
        self.process_size_entry = tk.Entry(self.input_frame, width=10)
        self.process_size_entry.grid(row=0, column=1)

        # Allocate Button
        self.allocate_button = tk.Button(self.input_frame, text="Allocate", command=self.allocate_memory)
        self.allocate_button.grid(row=0, column=2, padx=10)

    def update_memory_display(self):
        self.block_canvas.delete("all")  # Clear the canvas
        total_memory = sum(self.memory_blocks)
        current_x = 10  # Start position for the first block
        canvas_width = 580  # Total width for visualization
        for i, block in enumerate(self.memory_blocks):
            block_width = int((block / total_memory) * canvas_width)
            color = "green" if block > 0 else "red"  # Green for available, red for exhausted
            self.block_canvas.create_rectangle(
                current_x, 50, current_x + block_width, 150, fill=color, outline="black"
            )
            self.block_canvas.create_text(
                current_x + block_width / 2, 100, text=f"Block {i + 1}\n{block} units", fill="white"
            )
            current_x += block_width + 10  # Leave space between blocks

    def allocate_memory(self):
        try:
            process_size = int(self.process_size_entry.get())
            result = self.allocator.allocate_memory(process_size)
            messagebox.showinfo("Allocation Result", result)
            self.update_memory_display()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer for process size.")


if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryAllocatorApp(root)
    root.mainloop()
