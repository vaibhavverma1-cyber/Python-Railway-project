# Railway Reservation Analyzer (PS No. 84)
# Reads bookings.csv and shows bookings, revenue and ticket status per train.

import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = "bookings.csv"


def load_data():
    """Read the CSV file and remove rows that have an invalid fare."""
    # Step 1: read the file (show an error if it does not exist)
    try:
        df = pd.read_csv(FILE_NAME)
    except FileNotFoundError:
        print("Error: File '" + FILE_NAME + "' not found.")
        return None

    # Step 2: change the Fare column to numbers.
    # Wrong values like "abc" become NaN (empty).
    df["Fare"] = pd.to_numeric(df["Fare"], errors="coerce")

    # Step 3: show a warning for every row with a wrong fare
    for index, row in df.iterrows():
        if pd.isna(row["Fare"]):
            
            print("Warning: Row with PNR " + str(row["PNR"]) + " skipped - invalid fare.")

    # Step 4: remove the wrong rows
    df = df.dropna(subset=["Fare"])

    print("Valid records analysed:", len(df))
    return df


def draw_bar_chart(data, title, y_label):
    """Draw a bar chart. 'data' has train names and their values."""
    plt.bar(data.index, data.values)
    plt.title(title)
    plt.xlabel("Train")
    plt.ylabel(y_label)
    plt.show()


def bookings_per_train(df):
    """Option 1: count the bookings of each train."""
    counts = df.groupby("Train").size()

    for train, number in counts.items():
        print(train, ":", number)
    print("Total bookings:", counts.sum())

    draw_bar_chart(counts, "Bookings per Train", "Number of bookings")


def revenue_per_train(df):
    """Option 2: add the fares of Confirmed tickets for each train."""
    confirmed = df[df["Status"] == "Confirmed"]
    revenue = confirmed.groupby("Train")["Fare"].sum()
    revenue = revenue.sort_values(ascending=False)   # biggest first

    for train, amount in revenue.items():
        print(train, ": Rs.", int(amount))
    print("Total confirmed revenue: Rs.", int(revenue.sum()))

    draw_bar_chart(revenue, "Revenue per Train (Confirmed only)", "Revenue (Rs.)")


def tickets_by_status(df):
    """Option 3: count Confirmed, Waiting and Cancelled tickets."""
    print("--- All trains ---")
    for status in ["Confirmed", "Waiting", "Cancelled"]:
        count = len(df[df["Status"] == status])
        print(status, ":", count)

    print("--- Each train ---")
    for train in sorted(df["Train"].unique()):
        train_data = df[df["Train"] == train]
        confirmed = len(train_data[train_data["Status"] == "Confirmed"])
        waiting = len(train_data[train_data["Status"] == "Waiting"])
        cancelled = len(train_data[train_data["Status"] == "Cancelled"])
        print(train, ": Confirmed", confirmed, ", Waiting", waiting, ", Cancelled", cancelled)


def main():
    df = load_data()
    if df is None:        # file was not found, so stop
        return

    while True:
        print("\n===== Railway Reservation Analyzer =====")
        print("1. Bookings per train")
        print("2. Revenue per train (Confirmed only)")
        print("3. Tickets by status")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            bookings_per_train(df)
        elif choice == "2":
            revenue_per_train(df)
        elif choice == "3":
            tickets_by_status(df)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")


main()
