import requests

# Step 1: Webhook Generation
user_data = {
    "name": "Akshara Joshi",
    "regNo": "0827AL221014",
    "email": "joshiakshara0@gmail.com"
}

res = requests.post("https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON", json=user_data)
response = res.json()

webhook_url = response['webhook']
access_token = response['accessToken']

print("Webhook URL:", webhook_url)
print("Access Token:", access_token)

# Step 2: Final SQL Query
final_sql = {
    "finalQuery": '''
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
    '''
}

# Step 3: Submission
headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}

submit_res = requests.post(webhook_url, headers=headers, json=final_sql)

print("Submission Status:", submit_res.status_code)
print("Server Response:", submit_res.text)
