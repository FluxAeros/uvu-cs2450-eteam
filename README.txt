#UVSim: Basic Machine Language Simulator#

---Project Description---
UVSim is a versatile software simulator crafted specifically for computer science students to delve
into the intricacies of machine language and computer architecture.
By executing programs written in BasicML, UVSim emulates fundamental aspects of a computer system,
including a CPU, an accumulator, and a main memory with a capacity of 250 words.
It supports a broad spectrum of operations, ranging from input/output to arithmetic and control instructions.
UVSim stands as an essential educational tool, offering students a tangible,
hands-on experience that significantly deepens their understanding of the underlying principles of computing.

---Features---
Simulated CPU and Accumulator: Mimics the core functions of a central processing unit and an accumulator for arithmetic operations.
250-Word Main Memory: Offers a simplified model of computer memory, allowing for straightforward program execution.
Support for BasicML: Executes Basic Machine Language (BasicML) instructions, covering I/O, arithmetic, and control operations.
Interactive Command Execution: Users can input their machine language commands directly, facilitating an engaging learning process.
Color changing UI: Users can Background color and Button color of the ui.

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
Note: UVSim can edit and run multiple program files simultaneously.

4. Execute the Program:
Click the "Run" button to start the simulation.
UVSim will process the file and display output information within its window.

5. Input Codes as Prompted:
If UVSim requires additional input during execution, enter the codes when prompted. Inputs should be in the format of +000000 for positive numbers or -000000 for negative numbers, where 000000 represents your numeric value.

---Additional Features---
1. Viewing/Editing Files:
Once a file has been loaded into the simulation, click the "View file" button. From here you can view the file that has been
loaded, as well as make changes. Upon finishing, you can click the "Save" button and save your changes to the same file, or a
new one. Otherwise, you can click the "Cancel" or "X" buttons to close the file viewer without saving.

2. Changing Color Scheme:
You can click the "Background Color" or "Button Color" buttons to customize the colors of the simulation's window.
Both buttons will pull up a color setting menu, where you just need to select the desired color and click "OK"

3. Close Window Feature:
Like mentioned before UVSim allows the user to run multiple files in different windows simultaneously.
These windows can be closed at anytime by selecting the close button in the top left.
The close button will only close the window that is selected and not other windows that are currently open.

4. Command conversion:
UVSim comes with the option to change code that is in the format of '+0000' to '+000000' at the click of a button.
If a file is selected where the format of the document is 4 digits UVSim will have a pop up window and ask the user to convert to the 6 digit format and run the code/