# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Define dataset
data = {
    "Service Quality": [8, 6, 4, 6, 4],
    "Response Time": [5, 7, 8, 6, 5],
    "Product Satisfaction": [9, 7, 6, 1, 3]
}

# Step 2: Calculate Feedback Score using formula
def calculate_score(sq, rt, ps):
    return round(0.4 * sq + 0.3 * (10 - rt) + 0.3 * ps)

df = pd.DataFrame(data)
df["Feedback Score"] = df.apply(lambda row: calculate_score(row["Service Quality"], row["Response Time"], row["Product Satisfaction"]), axis=1)

print("Dataset:\n", df)

# Step 3: Split features and target
X = df[["Service Quality", "Response Time", "Product Satisfaction"]]
y = df["Feedback Score"]

# Step 4: Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Step 5: Create and train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Step 6: Make predictions
y_pred = model.predict(X_test)

# Step 7: Evaluation
print("\n🔍 Model Accuracy:", accuracy_score(y_test, y_pred))
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))

# Step 8: Predict new input
new_input = [[8, 3, 9]]
predicted_score = model.predict(new_input)
print(f"\n🔮 Predicted Feedback Score for {new_input[0]}: {predicted_score[0]}")

# Step 9: Optional - Visualize
plt.figure(figsize=(6, 4))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation")
plt.show()
