# MoneyTracker

This app takes the user's expenses and stores the data in a database. This app can send email to notify the user of expense report.

## Running Instructions
1. Clone the project using:
```git clone```
2. In a command line terminal, type:
```cd MoneyTracker``` 
``` python3 main.py```

For first time usage, uncomment ```dbmodule.make_table(conn, cret)``` in ```main()``` of main.py to initialize the table.
