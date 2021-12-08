from bs4 import BeautifulSoup


class SvrResult:
    def __init__(self, data):
        self.soup = BeautifulSoup(data, "lxml")

        self.ip, self.hostname = self.soup.find("ip").get_text(), self.soup.find("hostname").get_text()
        self.svr_id = self.get_svrid(self.hostname, self.ip)

    @staticmethod
    def get_svrid(hostname: str, ip: str) -> int:
        from func.GetSvrInfo import GetSvrInfo
        return GetSvrInfo(hostname, ip).svr_id

    def get_disk(self) -> dict:
        disk = self.soup.disk.contents
        disk_result: dict = {}
        if disk:
            for i, j in enumerate(disk):
                disk_result[j.name.replace(":", "")] = j.get_text()
        return disk_result

    def get_resource(self) -> tuple:
        return self.soup.cpu.get_text(), self.soup.memory.get_text()

    def get_svc(self) -> dict:
        svc = self.soup.service
        svc_result: dict = {}
        if svc:
            svc = svc.string
            for i, j in enumerate(svc):
                svc_result[j.name] = j.get_text()
        return svc_result

    def get_evt(self) -> dict:
        def get_evt_list(type) -> list:
            evt_list = []
            if not type:
                evt_list = None
            elif len(type) > 100:
                evt_list = ["ERROR"]
            else:
                for i in range(len(type)):
                    evt: dict = {"eventid": type.contents[i].eventid.get_text(),
                                 "level": type.contents[i].level.get_text(),
                                 "time": type.contents[i].timecreated.attrs.get('systemtime')}
                    evt_list.append(evt)
            return evt_list

        application = self.soup.eventlog.app
        security = self.soup.eventlog.secu
        system = self.soup.eventlog.sys

        evt_result: dict = {"application": get_evt_list(application),
                            "security": get_evt_list(security),
                            "system": get_evt_list(system)}

        return evt_result

    def get_task(self) -> dict:
        task = self.soup.tasklog
        task_result: dict = {}
        if task:
            task = self.soup.tasklog.contents
            for i, j in enumerate(task):
                task_result[j.name] = j.get_text()

        return task_result

    def get_wdef(self) -> str:
        wdef = self.soup.windefender
        if wdef:
            return wdef.string

