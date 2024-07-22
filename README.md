# LOGNOTE

LOGNOTE is a Tkinter-based GUI application designed for student management, note-taking, and messaging. This application provides login functionality for both admins and regular users, with different interfaces and features based on the user's role.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **User Authentication**: Separate login interfaces for admins and students.
- **Admin Interface**: 
  - Add, delete, and view student records.
  - Clear fields and display records in a tree view.
  - Status messages for user feedback.
- **Student Interface**:
  - Messaging functionality with an entry box for the message subject.
- **Database Management**: Handles database creation and table management.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/rinsane/LOGNOTE.git
    cd LOGNOTE
    ```

2. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```bash
    python main.py
    ```

## Usage

- **Login**: 
  - Admins can log in using admin credentials.
  - Students can log in using student credentials.
  
- **Admin Interface**:
  - **Add Student**: Fill in the student details and click 'Add'.
  - **Delete Student**: Select a student from the list and click 'Delete'.
  - **View Students**: Click 'Show Records' to display all student records.
  - **Clear Fields**: Click 'Clear' to clear input fields.

- **Student Interface**:
  - **Messaging**: Enter the subject and message content, then send.

## File Structure

- **main.py**: The main file that handles database creation and table management.
- **LOGNOTE.py**: The file that handles user login.
- **for_admin.py**: Contains the `call_admin` function for the admin interface.
- **for_students.py**: Handles student-specific functionality.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the project's coding standards.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI.
- Community contributions and feedback.
