#UVSim: Basic Machine Language Simulator#

---Project Description---
UVSim is a versatile software simulator crafted specifically for computer science students to delve
into the intricacies of machine language and computer architecture.
By executing programs written in BasicML, UVSim emulates fundamental aspects of a computer system,
including a CPU, an accumulator, and a main memory with a capacity of 100 words.
It supports a broad spectrum of operations, ranging from input/output to arithmetic and control instructions.
UVSim stands as an essential educational tool, offering students a tangible,
hands-on experience that significantly deepens their understanding of the underlying principles of computing.

---Features---
Simulated CPU and Accumulator: Mimics the core functions of a central processing unit and an accumulator for arithmetic operations.
250-Word Main Memory: Offers a simplified model of computer memory, allowing for straightforward program execution.
Support for BasicML: Executes Basic Machine Language (BasicML) instructions, covering I/O, arithmetic, and control operations.
Interactive Command Execution: Users can input their machine language commands directly, facilitating an engaging learning process.
Color changing UI: Users can change main and secondary color of the ui.


---Prerequisites---
Python 3.x installed on your system.


---Running UVSim---

1. Prepare Your Program File:
Create a text file containing your program written in BasicML.
Save this file within a convenient location in your project's folder structure.

2.Launch UVSim:
Execute the main application file. This can typically be done by running python3 main.py in
your terminal or command prompt, assuming you are in the UVSim project directory.

3. Load Your Program File:
Once UVSim opens, click on the "Select file" button.
Navigate through the file dialog to find and select the program file you prepared in step 1.

4. Execute the Program:
Click the "Run" button to start the simulation.
UVSim will process the file and display output information within its window.

5. Input Codes as Prompted:
If UVSim requires additional input during execution, enter the codes when prompted. Inputs should be in the format of +0000 for positive numbers or -0000 for negative numbers, where 0000 represents your numeric value.

6. Completion and Restart:
After the program finishes execution, UVSim will be ready for another run. You can choose to load another file and repeat the process as desired.

---Additional Features---
1. Viewing/Editing Files:
Once a file has been loaded into the simulation, click the "View file" button. From here you can view the file that has been
loaded, as well as make changes. Upon finishing, you can click the "Save" button and save your changes to the same file, or a
new one. Otherwise, you can click the "Cancel" or "X" buttons to close the file viewer without saving.

2. Changing Color Scheme:
You can click the "Change Primary Color" or "Change Off-Color" buttons to customize the colors of the simulation's window.
Both buttons will pull up a color setting menu, where you just need to select the desired color and click "OK"
