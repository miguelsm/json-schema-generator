# JSON Schema Generator

This Python script generates a JSON Schema from an example JSON document provided in a file and prints the schema to the console.

## Installation

1. **Clone the Repository or Download the Script:**

   Clone the repository or download the `generate_schema.py` script and the `requirements.txt` file.

2. **Install Dependencies:**

   ```sh
   python -m venv .venv
   . ./.venv/bin/activate
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare Your JSON Document:**

   Create an example JSON document and save it as `input.json` in the same directory as the script.

2. **Run the Script:**

   ```sh
   python generate_schema.py
   ```

   This will read the JSON document from `input.json`, generate the corresponding JSON schema, and print it to the console.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
