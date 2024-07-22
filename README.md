# LOGNOTE

LOGNOTE is a Tkinter-based GUI application designed for user management, note-taking, and messaging. This application provides login functionality for both admins and regular users, with different interfaces and features based on the user's role.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **User Authentication**: Separate login interfaces for admins and regular users.
- **Admin Interface**: 
  - Add, delete, and view user records.
  - Clear fields and display records in a tree view.
  - Status messages for user feedback.
- **User Interface**:
  - Messaging functionality with an entry box for the message subject.
- **Database Management**: Handles database creation and table management.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/rinsane/LOGNOTE.git
    cd LOGNOTE
    ```

2. **Activate the virtual environment and download the dependencies**:
    ```bash
    chmod +x inint.sh
    ./init.sh
    ```
    (for Windows users, just run `init.sh` somehow)

3. **Activate the virtual environment**:
    ```bash
    source venv/bin/activate
    ```
    
4. **Run the application**:
    ```bash
    python main.py
    ```

## Usage

- **Login**: 
  - Admins can log in using admin credentials.
  - Regular users can log in using user credentials.
  
- **Admin Interface**:
  - **Add User**: Fill in the user details and click 'Add'.
  - **Delete User**: Select a user from the list and click 'Delete'.
  - **View Users**: Click 'Show Records' to display all user records.
  - **Clear Fields**: Click 'Clear' to clear input fields.

- **User Interface**:
  - **Messaging**: Enter the subject and message content, then send.

## File Structure

- **main.py**: The main file that handles database creation and table management.
- **LOGNOTE.py**: The file that handles user login.
- **for_admin.py**: Contains the `call_admin` function for the admin interface.
- **for_users.py**: Handles user-specific functionality.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the project's coding standards.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI.
- Community contributions and feedback.
