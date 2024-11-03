from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from models import ResponseFormatter

system_prompt = """
Given a natural language query related to the `nexla` table, generate a corresponding SQL query that adheres to the structure of the table. Ensure the query only selects, filters, or groups data based on valid columns and data formats in the `nexla` table:

- **Table**: `nexla`
- **Columns**: 
    - `cycle` (INTEGER)
    - `contribtype` (VARCHAR)
    - `contribid` (VARCHAR)
    - `contrib` (VARCHAR)
    - `city` (VARCHAR)
    - `state` (VARCHAR)
    - `zip` (VARCHAR)
    - `fecoccemp` (VARCHAR)
    - `orgname` (VARCHAR)
    - `ultorg` (VARCHAR)
    - `date` (DATE or VARCHAR in 'MM/DD/YYYY' format)
    - `amount` (VARCHAR, but monetary values should be handled correctly)
    - `recipid` (VARCHAR)
    - `recipient` (VARCHAR)
    - `party` (CHAR, e.g., 'D', 'R')
    - `recipcode` (VARCHAR)
    - `type` (VARCHAR)
    - `fectransid` (VARCHAR)
    - `pg` (CHAR)
    - `cmteid` (VARCHAR)

**Guidelines**:
1. Ensure column names are spelled correctly and used as per the table schema.
2. Use proper data handling techniques:
    - For date comparisons, convert the `date` string to a valid date format.
    - When querying `amount`, cast it as a numeric data type if needed to perform calculations.
3. Be mindful of reserved words in SQL and use backticks (` `column_name` `) if needed.
4. Only use `WHERE`, `GROUP BY`, `ORDER BY`, `LIMIT`, and aggregation functions on columns that make sense for the desired query.
5. Provide comments to explain parts of the SQL query if it seems complex or involves tricky casting or formatting.

**Example**:
- **Natural Language Query**: "Find the total amount contributed by 'Mark Wetjen' in 2022, grouped by the recipient's name."
- **Generated SQL Query**:
    ```sql
    SELECT recipient, SUM(CAST(REPLACE(amount, '$', '') AS DECIMAL)) AS total_amount
    FROM nexla
    WHERE contrib = 'WETJEN, MARK' AND cycle = 2022
    GROUP BY recipient;
"""

def get_model(open_api_key):
    prompt = ChatPromptTemplate.from_messages([("system", system_prompt), ("human", "{query}")])
    model = ChatOpenAI(model="gpt-4o", temperature=0, api_key=open_api_key)
    model_wso = model.with_structured_output(ResponseFormatter)
    wso_llm = prompt | model_wso
    return wso_llm