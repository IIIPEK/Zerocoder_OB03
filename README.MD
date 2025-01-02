# Zoo Management System

## Overview

The **Zoo Management System** is a Python-based application that simulates the operations of a zoo. It includes functionalities for managing animals and employees, demonstrating object-oriented programming principles such as inheritance, polymorphism, and composition.

## Features

- **Animal Management**
  - Support for various animal types: Birds, Mammals, and Reptiles.
  - Custom sounds and eating behaviors for each type of animal.
  - Display detailed information about animals in the zoo.

- **Employee Management**
  - Support for different employee roles: Zoo Keepers and Veterinarians.
  - Employees can perform specific tasks such as feeding and healing animals.

- **Zoo Operations**
  - Add and manage animals and employees.
  - List all animals and employees in the zoo.
  - Persistent zoo state storage (save and load zoo information to/from a file).

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/IIIPEK/Zerocoder_OB03
   ```

2. Navigate to the project directory:

   ```bash
   cd zoo-management-system
   ```

3. Run the main program:

   ```bash
   python main.py
   ```

## Usage

- The main entry point of the application is `main.py`. Run it to start the simulation of the zoo operations.
- The program demonstrates the following functionalities:
  1. Adding animals and employees to the zoo.
  2. Listing animals and employees.
  3. Performing actions like feeding and healing animals.

## File Structure

- `main.py`: The entry point of the program that ties all components together.
- `classes/animal.py`: Contains definitions for the `Animal` base class and its derived classes (`Bird`, `Mammal`, `Reptile`).
- `classes/employee.py`: Contains definitions for the `Employee` base class and its derived classes (`ZooKeeper`, `Veterinarian`).
- `classes/zoo.py`: Contains the `Zoo` class that handles the overall management of animals and employees.

## Example Output

```
Animals in the zoo:
- Bird: Pigeon is 2 years old
- Mammal: Lion is 5 years old
- Reptile: Snake is 3 years old

Employees in the zoo:
- Zoo Keeper John, Age: 30, Salary: 5000
- Veterinarian Jane, Age: 25, Salary: 6000

John is feeding Pigeon
I am a bird and I eat seeds
Jane is treating the disease in Pigeon
Chirp
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please submit issues or pull requests via the GitHub repository.

## Contact

For any inquiries or issues, please contact the repository maintainer.

## Acknowledgements

- [Python](https://www.python.org/)
- [Object-Oriented Programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
