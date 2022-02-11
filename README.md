## ✅ **_Windows Server Status Checking System_**

+ Function
  1. Logging
  2. Parse log file (XML format)
  3. Insert data into DB

+ How to make ReadDailyCheck in executable program

  ```
  pyinstaller --onefile --add-data=conf\*;conf --name read_daily_check Main.py
  ```