# FILE: /my-flask-app/my-flask-app/README.md

# My Flask App

This is a simple Flask application that serves an HTML page with a navigation bar and buttons for "Learn More" and "Login with Google".

## Project Structure

```
my-flask-app
├── app
│   ├── templates
│   │   └── index.html
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   └── js
│   │       └── scripts.js
│   └── __init__.py
├── app.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-flask-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the Flask application, execute the following command:
```
python app.py
```

The application will be available at `http://127.0.0.1:5000/`. 

## Usage

Visit the homepage to see the navigation bar and buttons. You can click "Learn More" for additional information or "Login with Google" to initiate the login process.