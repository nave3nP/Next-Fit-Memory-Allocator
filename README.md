# Next Fit Memory Allocator

The **Next Fit Memory Allocator** is a graphical simulation tool for visualizing the Next Fit memory allocation algorithm. Designed for educational purposes, it allows users to interactively allocate memory for processes, observe fragmentation, and reset memory blocks.

---

## Features
- **Interactive GUI**: Built using Tkinter, with intuitive input fields, buttons, and visual feedback.
- **Real-Time Visualization**: Displays memory usage dynamically with progress bars.
- **Reset Functionality**: Reset memory blocks to their initial state for new experiments.
- **Dynamic Inputs**: Users can define custom memory block sizes and process sizes.
- **Error Handling**: Provides user-friendly error messages for invalid inputs.

---

## Getting Started

### Prerequisites
- Python 3.7 or above installed on your system.
- The `tkinter` library (comes pre-installed with Python).

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/next-fit-memory-allocator.git
   cd next-fit-memory-allocator
   ```
2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` is not available, ensure Python’s `tkinter` module is installed.)*

3. **Run the application:**
   ```bash
   python app.py
   ```

---

## How to Use

1. **Launch the application:**
   ```bash
   python app.py
   ```
2. **Initialize Memory Blocks:**
   - Enter block sizes (comma-separated) in the input field (e.g., `100, 200, 300`).
   - Click **"Initialize"** to set up the memory blocks.
3. **Allocate Memory:**
   - Enter a process size in the **"Process Size"** field.
   - Click **"Allocate"** to allocate the process to a memory block.
   - View the allocation result and updated memory usage.
4. **Reset All:**
   - Click **"Reset All"** to reset the memory blocks to their initial sizes.

Experiment with different configurations and observe how the Next Fit algorithm works!

---

## Screenshots

### Initialization Screen
![Initialization Screen](path/to/initialization-screen.png)

### Allocation Example
![Allocation Example](path/to/allocation-example.png)

---

## Code Structure

The project is contained in a single file, `app.py`, with the following key components:

### **NextFitMemoryAllocator Class**
- Implements the Next Fit memory allocation algorithm.
- Handles memory block management, allocation, and resets.

### **MemoryAllocatorApp Class**
- Manages the Tkinter-based graphical user interface.
- Interacts with the allocator to process user input and update the visualization.

---

## Example Input and Output

### Example Input
- **Memory Blocks:** `100, 200, 300, 400`
- **Process Sizes:** `50, 250, 300, 150`

### Output
```
Allocation of process 50 → Block 1 (50 used, 50 remaining).
Allocation of process 250 → Block 2 (200 used, 0 remaining).
Allocation of process 300 → Block 3 (300 used, 0 remaining).
Allocation of process 150 → Block 4 (150 used, 250 remaining).
```

---

## Future Enhancements
- Add support for other allocation algorithms (First Fit, Best Fit, etc.).
- Provide detailed fragmentation analysis.
- Include a web-based interface using frameworks like Streamlit.
- Allow export of allocation results for analysis (CSV or JSON).
- Add multi-language support for broader accessibility.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

This project is inspired by concepts from Operating Systems textbooks, including the Next Fit Memory Allocation algorithm. Special thanks to contributors and the community for their feedback and support.
