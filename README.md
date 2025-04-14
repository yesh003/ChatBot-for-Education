# Chatbot UI Project

This project is an interactive UI chatbot that allows users to send queries and receive responses in a graphical interface. The chatbot simulates interaction with ChatGPT without requiring an API key.

## Project Structure

```
chatbot-ui
├── src
│   ├── app.py               # Main entry point of the application
│   ├── ui
│   │   └── chatbot_ui.py    # Implementation of the interactive UI
│   ├── utils
│   │   └── response_handler.py # Logic for handling user queries and responses
├── requirements.txt          # List of dependencies
├── README.md                 # Project documentation
└── .gitignore                # Files to ignore in version control
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd chatbot-ui
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   Install the required libraries listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   Start the chatbot UI by running:
   ```bash
   python src/app.py
   ```

## Usage

- Once the application is running, a window will appear where you can type your queries.
- The chatbot will respond based on the simulated logic defined in the `response_handler.py` file.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes. 

## License

This project is licensed under the MIT License.