# **Personal Task Manager**
A lightweight, terminal based **personal task manager** built with Python. This application allow users to create, view, track and delete tasks right their command line interface(CLI). It includes a profound storage, ensuring your tasks are saved even after closing a program.

## features
- **profound storage**:Tasks are automatically saved to and loaded from 'task.json'.
- **Robust Error handling**:Prevents crashes fom invalid inputs, empty task entries or missing data files.
- **Four operations**:Full capability to Create, Read, Update and Delete tasks.
- **Visual status trackin**:instantly viewing of progress by using indicators [X] and [ ]
- **Modular Codebase:** Clean separation of concerns between user interface interaction ('main.py') and data logic ('tasks_functions.py').

## python concepts reinforced
- **Data layout:** Using a list of dictionaries to manage complex, structured data.
- **Modular Programming:** Importing custom helper module to write clean, reusable code.
- **File Systems & JSON Syntax:** Utilizing the built-in json module to serial and deserialize data to a hard drive file.

## Project Structure
'''text
|----main.py:
|----task_functions.py
|----tasks.json
'''

## How to run
### Prerequisites
- Make sure you have python installed on your computer

### Steps
- clone or download this project folder to you system.
- put both 'main.py' and 'task_functions.py' in the **same directory**
- open your terminal or command prompt and navigate to that directory.
- run the program with the following command

## user guide
When you launch the program, you will interact with the following numeric menu options:
- **1. View task:**Prints out a numbered list of your active and finished tasks.
- **2. Add Task:**Prompts you for text input to add a new objective to the registry.
- **3. Complete Task:**Display current tasks and asks for a number to flip its status
- **4. Delete Task:**Display current tasks and permanently removes a specific item from your list.
- **5. Exit:**Safely saves changes and stops the application execution loop.