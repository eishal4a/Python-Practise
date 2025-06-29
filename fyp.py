import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import seaborn as sns

# --------- Functions ---------
def calc_raw_score(sq, rt, ps):
    return 0.4 * sq + 0.3 * (10 - rt) + 0.3 * ps

def map_score(raw):
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

def show_graph(df):
    customers = df["Customer #"]
    scores = df["Predicted Score"]
    plt.figure(figsize=(8, 5))
    plt.plot(customers, scores, marker='o', linestyle='-', color='green')
    plt.title("📊 Predicted Feedback Score per Customer")
    plt.xlabel("Customer Number")
    plt.ylabel("Predicted Score")
    plt.xticks(customers)
    plt.yticks(range(1, 6))
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def show_gui(df):
    root = tk.Tk()
    root.title("Customer Feedback Table")
    root.geometry("800x450")
    root.config(bg="#f0f8ff")

    tk.Label(root, text="DECISION TREE CLASSIFIER USING SCIKIT-LEARN", font=("Arial", 13, "bold"), bg="#f0f8ff", fg="#003366").pack(pady=5)
    tk.Label(root, text="📋 Final Feedback Dataset", font=("Arial", 14, "bold"), bg="#f0f8ff").pack(pady=5)

    tree = ttk.Treeview(root)
    tree["columns"] = list(df.columns)
    tree["show"] = "headings"
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")
    for _, row in df.iterrows():
        tree.insert("", "end", values=list(row))

    tree.pack(padx=10, pady=10)
    tk.Button(root, text="📊 Show Graph", command=lambda: show_graph(df), bg="#007acc", fg="white").pack(pady=10)

    root.mainloop()

# --------- Initial Dataset ---------
data = {
    "Service Quality": [8, 6, 4, 6, 4],
    "Response Time": [5, 7, 8, 6, 5],
    "Product Satisfaction": [9, 7, 6, 1, 3]
}

# --------- Main Loop ---------
while True:
    df = pd.DataFrame(data)

    # Calculate raw and mapped feedback scores
    df["Raw Score"] = df.apply(lambda row: round(calc_raw_score(
    row["Service Quality"], row["Response Time"], row["Product Satisfaction"]
), 1), axis=1)

    df["Feedback Score"] = df["Raw Score"].apply(map_score)

    # -------- Show input and output tables in terminal --------
    print("\n📥 INPUT TABLE (from dataset):")
    print(df[["Service Quality", "Response Time", "Product Satisfaction"]].to_string(index=False))

    print("\n📤 OUTPUT TABLE (calculated scores):")
    print(df[["Raw Score", "Feedback Score"]].to_string(index=False))

    # Prepare features and labels
    X = df[["Service Quality", "Response Time", "Product Satisfaction"]]
    y = df["Feedback Score"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

    # Train model
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    print("\n🔍 Model Accuracy:", accuracy_score(y_test, y_pred))
    print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))

    # Predict for new input
    test_input = [[8, 3, 9]]
    pred = model.predict(test_input)[0]
    print(f"\n🔮 Predicted Feedback Score for input {test_input[0]} → {pred}")

    # Add predictions and customer #
    df["Predicted Score"] = model.predict(X)
    df.insert(0, "Customer #", [i+1 for i in range(len(df))])

    # Ask user to add more data
    ans = input("\n➕ Do you want to add another feedback? (yes/no): ").strip().lower()
    if ans == "yes":
        try:
            sq = int(input("Service Quality (1-10): "))
            rt = int(input("Response Time (1-10): "))
            ps = int(input("Product Satisfaction (1-10): "))
            data["Service Quality"].append(sq)
            data["Response Time"].append(rt)
            data["Product Satisfaction"].append(ps)
        except:
            print("❌ Invalid input. Please enter valid numbers.")
    else:
        show_gui(df)
        break
