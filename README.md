  ## ✅ **_Windows Server Monitoring System_**
***
ReadDailyCheck __analyzes the log__ files created from _[DailyCheck](https://github.com/za5321/DailyCheck)_ and inserts data into DB without installing python by running an __executable program__ with extension exe. <br/>In order to build the exe file, please refer to _'How to execute ReadDailyCheck'_ at the below.<br/><br/>

📝 ReadDailyCheck is able to:<br/>
* __Parse XML data__ (For json version _DailyCheck_, check _branch json_ out.)
* __Insert data into DB__

🔧 For the project ReadDailyCheck, you should install:<br/>
* BeautifulSoup4: To parse xml<br/>
`pip install beautifulsoup4`
* Pymssql: To connect Database - SQL Server (MS-SQL). My MS-SQL version is 2019.<br/>
`pip install pymssql`

🔧 How to execute ReadDailyCheck:<br/>
>   1. Install Pyinstaller - It helps build python project into exe file easily.<br/>
    `pip install pyinstaller`
>   2.  Type the command line below. <br/>
    `pyinstaller --onefile --add-data=conf\*;conf --name read_daily_check Main.py`<br/>
    These options are:<br/>
    --onefile: Should you need a neat single exe file, this option is going to help you.<br/>
    --add-data: The option must be added in order to apply configuration to your executable program.<br/>
    --name: You can set the name of exe file.<br/>
>   3. After building, you can find **_'read_daily_check.exe'_** at **_'dist'_** folder.
>   4. Upload **_'read_daily_check.exe'_** to the FTP server.

🕑 If you want to run **_'read_daily_check.exe'_** with regularity:<br/>
>   1. Run **_Windows Task Scheduler_**
>   2. Open _'Create Task'_ and set _'General'_ and _'Triggers'_.
>   3. Go to _'Actions'_ and create new.
>   4. Add _read_daily_check_ to the _'Program/Script'_.
