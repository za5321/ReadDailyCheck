  ## ✅ **_Windows Server Monitoring System_**
***


ReadDailyCheck analyzes the log files created from _DailyCheck_ and insert data into DB without installling python by running an __executable program__. <br/>In order to build the exe file, please refer to _'How to execute ReadDailyCheck'_ at the below.<br/><br/>

📝 ReadDailyCheck is able to:<br/>
* __Parse XML data__ 
* __Database connection: Insert__

🔧 For the project DailyCheck, you should install:<br/>
* BeautifulSoup4: To parse xml<br/>
`pip install beautifulsoup4`
* Pymssql: Database - SQL Server (MS-SQL) 2019.<br/>
`pip install pymssql`

🔧 How to execute ReadDailyCheck:<br/>
>   1. Install Pyinstaller - It helps build python project into exe file easily.<br/>
    `pip install pyinstaller`
>   2.  Type the command line below. <br/>
    ``<br/>
    These options are:<br/>
    --onefile: Should you need a neat single exe file, this option is going to help you.<br/>
    --add-data: The option must be added in order to apply configuration to your executable program.<br/>
    --name: You can set the name of exe file.<br/>
>   3. After building, you can find **_'read_daily_check.exe'_** at **_'dist'_** folder.
