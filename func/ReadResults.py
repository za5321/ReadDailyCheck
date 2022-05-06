import json


class SvrResult:
    def __init__(self, data):
        self.data = json.load(data)

        self.ip, self.hostname = self.data["ip"], self.data["hostname"]
        self.svr_id = self.get_svrid(self.hostname, self.ip)

    @staticmethod
    def get_svrid(hostname: str, ip: str) -> int:
        from func.GetSvrInfo import GetSvrInfo
        return GetSvrInfo(hostname, ip).svr_id

    def get_disk(self) -> dict:
        return self.data["disk"]

    def get_resource(self) -> tuple:
        return self.data["cpu"], self.data["memory"]

    def get_svc(self) -> dict:
        return self.data["service"]

    def get_evt(self) -> dict:
        def get_evt_list(event_type) -> list:
            from bs4 import BeautifulSoup

            soup = BeautifulSoup(event_type, "lxml")
            evt_list = []
            if not soup:
                evt_list = None
            elif len(soup) > 100:
                evt_list = ["ERROR"]
            else:
                for i in range(len(soup)):
                    evt: dict = {"eventid": soup.contents[i].eventid.get_text(),
                                 "level": soup.contents[i].level.get_text(),
                                 "time": soup.contents[i].timecreated.attrs.get('systemtime')}
                    evt_list.append(evt)
            return evt_list

        application = self.data["eventlog"]["app"]
        security = self.data["eventlog"]["secu"]
        system = self.data["eventlog"]["sys"]

        evt_result: dict = {"application": get_evt_list(application),
                            "security": get_evt_list(security),
                            "system": get_evt_list(system)}

        return evt_result

    def get_task(self) -> dict:
        return self.data["task"]

    def get_wdef(self) -> str:
        return self.data["windefender"]
