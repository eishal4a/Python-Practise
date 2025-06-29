import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Step 1: Prepare dataset
data = {
    "Service Quality": [8, 6, 4, 6, 4],
    "Response Time": [5, 7, 8, 6, 5],
    "Product Satisfaction": [9, 7, 6, 1, 3]
}

def calculate_score(sq, rt, ps):
    return round(0.4 * sq + 0.3 * (10 - rt) + 0.3 * ps)

df = pd.DataFrame(data)
df["Feedback Score"] = df.apply(lambda row: calculate_score(row["Service Quality"], row["Response Time"], row["Product Satisfaction"]), axis=1)

# Step 2: Train the model
X = df[["Service Quality", "Response Time", "Product Satisfaction"]]
y = df["Feedback Score"]

model = DecisionTreeClassifier()
model.fit(X, y)

# Step 3: Get input from user at runtime
try:
    print("\n📥 Enter customer details:")

    sq = int(input("Service Quality (1-10): "))
    rt = int(input("Response Time (1-10): "))
    ps = int(input("Product Satisfaction (1-10): "))

    # Step 4: Predict and show result
    prediction = model.predict([[sq, rt, ps]])
    print(f"\n🔮 Predicted Feedback Score: {prediction[0]}")

except ValueError:
    print("❌ Please enter only numbers between 1 and 10.")
