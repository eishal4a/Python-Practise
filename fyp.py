import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from tkinter import Tk, ttk, Label
import tkinter.messagebox as msg

# Base dataset to train model
base_data = {
    "Service Quality": [8, 6, 4, 6, 4],
    "Response Time": [5, 7, 8, 6, 5],
    "Product Satisfaction": [9, 7, 6, 1, 3]
}

def calculate_score(sq, rt, ps):
    return round(0.4 * sq + 0.3 * (10 - rt) + 0.3 * ps)

# Add Feedback Score to base data
df = pd.DataFrame(base_data)
df["Feedback Score"] = df.apply(lambda row: calculate_score(row["Service Quality"], row["Response Time"], row["Product Satisfaction"]), axis=1)

# Train the model
X = df[["Service Quality", "Response Time", "Product Satisfaction"]]
y = df["Feedback Score"]
model = DecisionTreeClassifier()
model.fit(X, y)

# Store all customer entries
all_customers = []

# Loop to get customer feedback
while True:
    print("\n📥 Enter customer feedback:")
    try:
        sq = int(input("Service Quality (1-10): "))
        rt = int(input("Response Time (1-10): "))
        ps = int(input("Product Satisfaction (1-10): "))
        
        pred = model.predict([[sq, rt, ps]])[0]
        
        all_customers.append({
            "Service Quality": sq,
            "Response Time": rt,
            "Product Satisfaction": ps,
            "Predicted Score": pred
        })
        
        more = input("\n🌀 Do you want to add another customer? (yes/no): ").strip().lower()
        if more != "yes":
            break
            
    except ValueError:
        print("❌ Invalid input. Please enter numbers from 1 to 10.")

# Show data in GUI table
def show_gui(data):
    root = Tk()
    root.title("All Customer Feedback Data")

    Label(root, text="Predicted Feedback Results", font=("Arial", 14, "bold")).pack(pady=10)

    tree = ttk.Treeview(root)
    tree["columns"] = list(data[0].keys())
    tree["show"] = "headings"

    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    for row in data:
        tree.insert("", "end", values=list(row.values()))

    tree.pack(expand=True, fill="both", padx=10, pady=10)
    root.mainloop()

# If there's at least 1 customer, show the GUI
if all_customers:
    show_gui(all_customers)
else:
    msg.showinfo("No Data", "No customer data entered.")
