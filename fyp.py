import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from tkinter import Tk, ttk, Label
import tkinter.messagebox as msg

# --- Step 1: Prepare training data ---
training_data = {
    "Service Quality": [8, 6, 4, 6, 4],
    "Response Time": [5, 7, 8, 6, 5],
    "Product Satisfaction": [9, 7, 6, 1, 3]
}

# Function to calculate feedback score using the formula
def calculate_score(sq, rt, ps):
    return round(0.4 * sq + 0.3 * (10 - rt) + 0.3 * ps)

# Create DataFrame and calculate scores
df = pd.DataFrame(training_data)
df["Feedback Score"] = df.apply(lambda row: calculate_score(
    row["Service Quality"], row["Response Time"], row["Product Satisfaction"]), axis=1)

# Train the Decision Tree model
X = df[["Service Quality", "Response Time", "Product Satisfaction"]]
y = df["Feedback Score"]
model = DecisionTreeClassifier()
model.fit(X, y)

# --- Step 2: Collect up to 20 customer inputs ---
customer_feedbacks = []
max_customers = 20

print("\n📥 CUSTOMER FEEDBACK ENTRY")

for i in range(max_customers):
    print(f"\n➡️ Customer #{i + 1}")

    try:
        sq = int(input("Service Quality (1-10): "))
        rt = int(input("Response Time (1-10): "))
        ps = int(input("Product Satisfaction (1-10): "))

        # Predict feedback score
        pred_score = model.predict([[sq, rt, ps]])[0]

        # Store data
        customer_feedbacks.append({
            "Customer #": i + 1,
            "Service Quality": sq,
            "Response Time": rt,
            "Product Satisfaction": ps,
            "Predicted Score": pred_score
        })

        if i < max_customers - 1:  # Ask only if not already at 20
            cont = input("Do you want to add another customer? (yes/no): ").strip().lower()
            if cont != "yes":
                break

    except ValueError:
        print("❌ Invalid input. Please enter numbers from 1 to 10.")
        break

# --- Step 3: GUI display of results ---
def show_gui(data):
    root = Tk()
    root.title("Customer Feedback Results")

    Label(root, text="📊 All Customer Feedback Scores", font=("Arial", 14, "bold")).pack(pady=10)

    tree = ttk.Treeview(root)
    tree["columns"] = list(data[0].keys())
    tree["show"] = "headings"

    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    for row in data:
        tree.insert("", "end", values=list(row.values()))

    tree.pack(expand=True, fill="both", padx=20, pady=10)
    root.mainloop()

if customer_feedbacks:
    show_gui(customer_feedbacks)
else:
    msg.showinfo("No Data", "No customer feedback entered.")
