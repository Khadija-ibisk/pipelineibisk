import pandas as pd

data = {
    "order_id": ["ORD030","ORD031","ORD032"],
    "customer_name": ["Anna Klein","Marco Rossi","Yuki Tanaka"],
    "country": ["Germany","Italy","Japan"],
    "product": ["Monitor","Keyboard","Mouse"],
    "quantity": [1, 4, 2],
    "price": [320.0, 60.0, 30.0],
    "order_date": ["2024-02-15","2024-02-16","2024-02-17"]
}

pd.DataFrame(data).to_excel("data/raw/orders.xlsx", index=False)
print("✅ Excel créé !")