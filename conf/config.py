import json


class Config:
    def __init__(self):
        with open('conf\config.json', 'r', encoding='UTF-8') as file:
            self.conf = json.load(file)

    def conf_db_connection(self):
        import pymssql
        import decimal
        return pymssql.connect(self.conf['Database']['ip'], self.conf['Database']['id'],
                               self.conf['Database']['password'], self.conf['Database']['name'])

    def conf_file_path(self) -> str:
        return self.conf["FilePath"]["ResultFile"]

    def logging(self, flag: str):
        return self.conf["Logging"][flag]
