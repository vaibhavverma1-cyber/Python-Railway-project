[README.md](https://github.com/user-attachments/files/34900900/README.md)
# Railway Reservation Analyzer (PS No. 84)

A Python 3 console program that reads railway ticket bookings from a CSV file and reports
bookings per train, revenue per train (Confirmed tickets only) and ticket status counts.
Results are also shown as Matplotlib bar charts. Rows with an invalid fare are skipped
with a warning, and a missing file is reported without crashing.

**Student:** Vaibhav
**Course:** B.Tech 1st Sem, IBM, Rungta International Skills University
**Submitted to:** Mr. Priyanshu, IBM SME

## Features

- Reads `bookings.csv` with Pandas and shows the number of valid records
- **Option 1:** bookings per train, with a total and a bar chart
- **Option 2:** revenue per train from Confirmed tickets only, with a total and a bar chart
- **Option 3:** ticket counts by status (Confirmed, Waiting, Cancelled), for all trains and for each train
- Skips rows with an invalid fare (not a number, or not positive) and prints a warning
- Prints a clear error if the file does not exist

## Concepts used

Pandas DataFrame, CSV reading, `groupby`, filtering, `to_numeric`, `try / except`,
functions, loops, Matplotlib bar charts.

## Project files

| File | Purpose |
|------|---------|
| `railway_analyzer.py` | The program |
| `bookings.csv` | Sample booking data |
| `README.md` | This file |

## Requirements

- Python 3
- Pandas and Matplotlib

```
pip install pandas matplotlib
```

## How to run

1. Keep `railway_analyzer.py` and `bookings.csv` in the same folder.
2. Open a terminal in that folder and run:

```
python railway_analyzer.py
```

3. Choose an option from the menu:

```
===== Railway Reservation Analyzer =====
1. Bookings per train
2. Revenue per train (Confirmed only)
3. Tickets by status
4. Exit
Enter your choice (1-4):
```

Close the chart window to return to the menu. Choose `4` to exit.

## Data format

`bookings.csv` has five columns:

| Column | Meaning |
|--------|---------|
| PNR | Unique ticket number |
| Train | Train name (spell it the same way every time) |
| Class | Coach class, for example CC, EC, 3A, 2A, SL |
| Fare | Ticket price in Rs. Must be a positive number |
| Status | `Confirmed`, `Waiting` or `Cancelled` (exact spelling) |

Sample data:

```
PNR,Train,Class,Fare,Status
1001,Shatabdi,CC,950,Confirmed
1002,Shatabdi,CC,950,Confirmed
1003,Shatabdi,EC,1800,Waiting
1004,Rajdhani,3A,1700,Confirmed
1005,Rajdhani,3A,1700,Cancelled
1006,Rajdhani,2A,2400,Confirmed
1007,Gondwana,SL,520,Confirmed
1008,Gondwana,SL,520,Waiting
1009,Gondwana,3A,1500,Confirmed
1010,Gondwana,SL,520,Confirmed
```

### Adding a new train or booking

Add a new line at the bottom of `bookings.csv` with all five values, for example
`1011,Duronto,SL,640,Confirmed`. Save the file and run the program again, because the
file is read once at start. A new train appears automatically in the results and charts.

## How it works

1. **Read:** `pd.read_csv` loads the file. A missing file prints an error and the program stops.
2. **Validate:** `pd.to_numeric(errors="coerce")` turns a bad fare such as `abc` into an empty
   value. A warning is printed for each such row and the row is dropped.
3. **Group:** `groupby("Train")` counts bookings and adds up fares; status counts use the Status column.
4. **Menu:** a `while` loop shows the options until the user chooses Exit.
5. **Report:** results are printed and a bar chart is drawn with Matplotlib.

## Test cases

All four test cases from the problem statement pass.

| # | Input | Output |
|---|-------|--------|
| 1 | Sample file, option 1 | `Gondwana : 4`, `Rajdhani : 3`, `Shatabdi : 3`, `Total bookings: 10`, bar chart with three bars |
| 2 | Only `1001,Shatabdi,CC,950,Confirmed`, option 2 | `Shatabdi : Rs. 950`, `Total confirmed revenue: Rs. 950`, bar chart with one bar |
| 3a | File `missing.csv` does not exist | `Error: File 'missing.csv' not found.` |
| 3b | Sample rows plus `1011,Gondwana,SL,abc,Confirmed` | `Warning: Row with PNR 1011 skipped - invalid fare.` then `Valid records analysed: 10` |
| 4 | Sample file, option 2 | `Rajdhani : Rs. 4100`, `Gondwana : Rs. 2540`, `Shatabdi : Rs. 1900`, `Total confirmed revenue: Rs. 8540` |

To run test case 3a, change `FILE_NAME = "bookings.csv"` to `FILE_NAME = "missing.csv"` in the
code, run the program, then change it back.

## Troubleshooting

- **New rows do not show up:** save `bookings.csv` and restart the program.
- **`ModuleNotFoundError`:** run `python -m pip install pandas matplotlib`.
- **"Application Control policy has blocked this file" on Windows:** the security policy of the
  computer is blocking Pandas. Run the program in Google Colab (upload `bookings.csv` and paste
  the code), or on another computer.

## Future scope

- Add new bookings from the menu and save them to the CSV
- Export reports to Excel or PDF
- Revenue by class and by date
- A web dashboard and a database instead of a CSV file
