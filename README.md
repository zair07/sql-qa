# Natural Language to SQL Query QnA

This project is a FastAPI application that converts natural language questions into SQL queries. It leverages OpenAI's language models to understand and generate SQL commands based on user input.

## Features

- Convert natural language questions into SQL queries.
- FastAPI backend for handling requests and responses.
- Utilizes OpenAI and Langchain for natural language processing.

## Prerequisites

Make sure you have the following installed:

- Python 3.10 or higher
- pip (Python package installer)

## Setup Instructions

1. **Clone the Repository:**
```
git clone https://github.com/zair07/sql-qa.git
cd sql-qa
```
2. **Set Up Python Virtual Environment:**
```
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
```
3. **Install Requirements:**
```
pip install -r requirements.txt
```
4. **Set Up Environment Variables:**
```
OPENAI_KEY=
LANGCHAIN_API_KEY=
LANGCHAIN_PROJECT=
DB_HOST=
DB_USER=
DB_PASSWORD=
DB_NAME=
```
5. **Run the Application:**
```
fastapi dev main.py
```

## Usage
- Send a GET request to the / endpoint with a q parameter containing the query.

Example:
```
http://127.0.0.1:8000/?q=what are the top 5 contributions
```