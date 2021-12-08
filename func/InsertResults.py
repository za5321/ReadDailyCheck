class InsertResults:
    def __init__(self, svr_id):
        from conf.config import Config
        import datetime

        self.today = datetime.datetime.now()
        self.con = Config().conf_db_connection()
        self.svr_id = svr_id

    def insert_disk(self, name, capacity):
        cursor = self.con.cursor()
        sql = f"INSERT INTO DISK_LOG VALUES ('{str(self.svr_id)}', '{name}', '{capacity}', '{str(self.today)}')"
        cursor.execute(sql)
        self.con.commit()

    def insert_resource(self, cpu, mem):
        cursor = self.con.cursor()
        sql = f"INSERT INTO RESOURCE_LOG VALUES ('{str(self.svr_id)}', '{cpu}', '{mem}', '{str(self.today)}')"
        cursor.execute(sql)
        self.con.commit()

    def insert_svc(self, name, status):
        cursor = self.con.cursor()
        sql = f"INSERT INTO SERVICE_LOG VALUES ('{str(self.svr_id)}', '{name}', '{status}', '{str(self.today)}')"
        cursor.execute(sql)
        self.con.commit()

    def insert_evt(self, type: str, id: str, level: str, time: str):
        def check_evt_cnt(id: str, time: str) -> int:
            cursor = self.con.cursor()
            sql = f"SELECT COUNT(*) FROM EVENT_LOG WITH(NOLOCK) WHERE EVTID = '{id}' AND EVTTIME = '{time}'"
            cursor.execute(sql)
            row = cursor.fetchone()
            return row[0]

        if check_evt_cnt(id, time) == 0:
            cursor = self.con.cursor()
            sql = f"INSERT INTO EVENT_LOG VALUES ('{str(self.svr_id)}', '{type}', '{id}', '{level}', '{time}', '{str(self.today)}')"
            cursor.execute(sql)
            self.con.commit()

    def insert_task(self, name: str, status: str):
        cursor = self.con.cursor()
        sql = f"INSERT INTO TASK_LOG VALUES ('{str(self.svr_id)}', '{name}', '{status}', '{str(self.today)}')"
        cursor.execute(sql)
        self.con.commit()

    def insert_wdef(self, status: str):
        cursor = self.con.cursor()
        sql = f"INSERT INTO WINDEFENDER_LOG VALUES ('{str(self.svr_id)}', '{status}', '{str(self.today)}')"
        cursor.execute(sql)
        self.con.commit()
