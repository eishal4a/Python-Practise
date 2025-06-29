# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Define dataset from document
data = {
    "Service Quality": [8, 6, 4, 6, 4],
    "Response Time": [5, 7, 8, 6, 5],
    "Product Satisfaction": [9, 7, 6, 1, 3]
}

# Step 2: Apply the given formula to calculate raw score
def calculate_raw_score(sq, rt, ps):
    return 0.4 * sq + 0.3 * (10 - rt) + 0.3 * ps

# Step 3: Map raw score to final Feedback Score (1 to 5)
def map_to_feedback_score(raw):
    if raw >= 8:
        return 5
    elif raw >= 6.5:
        return 4
    elif raw >= 5:
        return 3
    elif raw >= 3.5:
        return 2
    else:
        return 1

# Step 4: Create DataFrame and compute scores
df = pd.DataFrame(data)
df["Raw Score"] = df.apply(lambda row: calculate_raw_score(
    row["Service Quality"], row["Response Time"], row["Product Satisfaction"]), axis=1)
df["Feedback Score"] = df["Raw Score"].apply(map_to_feedback_score)

print("📦 Final Dataset with Calculated Scores:\n")
print(df)

# Step 5: Prepare features and labels
X = df[["Service Quality", "Response Time", "Product Satisfaction"]]
y = df["Feedback Score"]

# Step 6: Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=42)

# Step 7: Train Decision Tree Classifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Step 8: Make predictions on test data
y_pred = model.predict(X_test)

# Step 9: Evaluate model
print("\n🔍 Model Accuracy:", accuracy_score(y_test, y_pred))
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))

# Step 10: Predict for a new input (as per document)
new_input = [[8, 3, 9]]  # Service Quality, Response Time, Product Satisfaction
predicted_score = model.predict(new_input)[0]
print(f"\n🔮 Predicted Feedback Score for {new_input[0]} → {predicted_score}")

# Step 11: Optional - Correlation Heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(df.drop(columns=["Feedback Score"]).corr(), annot=True, cmap="coolwarm")
plt.title("📊 Feature Correlation Heatmap")
plt.tight_layout()
plt.show()
