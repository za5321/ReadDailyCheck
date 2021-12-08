from conf.config import Config
from func.Logger import Logger
l = Logger()
logger = l.logger
l.set_handler()


class LogFile:
    def __init__(self):
        self.path = Config().conf_file_path()

    def read_log(self):
        import os

        files: list = []
        #os.chdir(self.path)
        for i in next(os.walk(self.path))[2]:
            f = open(f"{self.path}\\{i}", 'r', encoding="UTF-8")
            try:
                files.append(f.read())
            except UnicodeDecodeError:
                logger.info(f.name[f.name.rindex("\\") + 1:] + "파일 읽기에 실패했습니다.")
                continue
            f.close()
        return files

    def delete_log(self):
        import os

        os.chdir(self.path)
        for i in next(os.walk(self.path))[2]:
            os.remove(i)
