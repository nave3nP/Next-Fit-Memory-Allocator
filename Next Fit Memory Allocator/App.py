import tkinter as tk
from tkinter import messagebox

class NextFitMemoryAllocator:
    def __init__(self, memory_blocks):
        self.memory_blocks = memory_blocks
        self.last_allocated_index = 0

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
        return [f"Block {i + 1}: {size} units free" for i, size in enumerate(self.memory_blocks)]


class MemoryAllocatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Next Fit Memory Allocator")

        self.memory_blocks = [100, 500, 200, 300, 600]  # Example memory block sizes
        self.allocator = NextFitMemoryAllocator(self.memory_blocks)

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        tk.Label(self.root, text="Next Fit Memory Allocator", font=("Arial", 16)).pack(pady=10)

        # Memory Display
        self.memory_display = tk.Text(self.root, width=50, height=10, state=tk.DISABLED)
        self.memory_display.pack(pady=10)
        self.update_memory_display()

        # Input and Allocate Button
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        tk.Label(self.input_frame, text="Process Size: ").grid(row=0, column=0)
        self.process_size_entry = tk.Entry(self.input_frame, width=10)
        self.process_size_entry.grid(row=0, column=1)

        self.allocate_button = tk.Button(self.input_frame, text="Allocate", command=self.allocate_memory)
        self.allocate_button.grid(row=0, column=2, padx=10)

    def update_memory_display(self):
        self.memory_display.config(state=tk.NORMAL)
        self.memory_display.delete(1.0, tk.END)
        memory_state = self.allocator.get_memory_state()
        self.memory_display.insert(tk.END, "\n".join(memory_state))
        self.memory_display.config(state=tk.DISABLED)

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
