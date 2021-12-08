from func.LogFile import logger


class ReadDailyCheck:
    def __init__(self):
        from func.LogFile import LogFile
        self.log_file = LogFile()
        self.file_list: list = self.log_file.read_log()

    def read_result(self):
        from func.ReadResults import SvrResult
        from func.InsertResults import InsertResults
        for file in self.file_list:
            result = SvrResult(file)
            insert = InsertResults(result.svr_id)

            disk: dict = result.get_disk()
            for name, capacity in disk.items():
                insert.insert_disk(name, capacity)
                logger.info(f"{name}드라이브: {capacity}")

            res: tuple = result.get_resource()
            insert.insert_resource(res[0], res[1])
            logger.info(f"CPU: {res[0]}")
            logger.info(f"메모리: {res[1]}")

            svc: dict = result.get_svc()
            for name, status in svc.items():
                insert.insert_svc(name, status)
                logger.info(f"{name} 서비스: {status}")

            evt: dict = result.get_evt()
            for type, evt_list in evt.items():
                if evt_list == ["ERROR"]:
                    insert.insert_evt("ERROR", "ERROR", "ERROR", "ERROR")
                    logger.error(f"{type} 이벤트 100건 초과")
                else:
                    for evt in evt_list:
                        insert.insert_evt(type, evt["eventid"], evt["level"], evt["time"])
                    logger.info(f"{type} 이벤트 {len(evt_list)}건")

            task: dict = result.get_task()
            for name, status in task.items():
                insert.insert_task(name, status)
                logger.info(f"{name} 작업: {status}")

            wdef: str = result.get_wdef()
            if wdef:
                insert.insert_wdef(wdef)
                logger.info(f"윈도우 디펜더: {wdef}")

    def delete_log(self):
        self.log_file.delete_log()


if __name__ == "__main__":
    logger.info("=========================================================================")
    logger.info("DAILY CHECK STARTED")
    r = ReadDailyCheck()
    r.read_result()
    r.delete_log()
    logger.info("=========================================================================")
