from conf.config import Config


class GetSvrInfo:
    def __init__(self, hostname: str, ip: str):
        from conf.config import Config
        self.con = Config().conf_db_connection()
        self.hostname, self.ip = hostname, ip
        self.svr_id = self.get_svr_id()

    def get_svr_id(self) -> int:
        cursor = self.con.cursor()
        sql = f"SELECT SERVERID FROM SERVER_LIST WITH(NOLOCK) WHERE HOSTNAME = '{self.hostname}' AND IP = '{self.ip}'"
        cursor.execute(sql)
        row = cursor.fetchone()
        return row[0] if row else -1
