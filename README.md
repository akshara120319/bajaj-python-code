
# bajaj python code - Akshara Joshi

## Problem Statement
Build a Python application that:
1. Sends a POST request to generate a webhook.
2. Solves a SQL query based on provided data.
3. Submits the final SQL query using the webhook URL and token.

## Solution Details

### Final SQL Query
```sql
SELECT 
    p.AMOUNT AS SALARY,
    CONCAT(e.FIRST_NAME, ' ', e.LAST_NAME) AS NAME,
    FLOOR(DATEDIFF(CURDATE(), e.DOB)/365) AS AGE,
    d.DEPARTMENT_NAME
FROM PAYMENTS p
JOIN EMPLOYEE e ON p.EMP_ID = e.EMP_ID
JOIN DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID
WHERE DAY(p.PAYMENT_TIME) != 1
ORDER BY p.AMOUNT DESC
LIMIT 1;
```

## How to Run

### Step 1: Install Required Packages
```bash
pip install -r requirements.txt
```

### Step 2: Run the Script
```bash
python main.py
```

## Author
Akshara Joshi
