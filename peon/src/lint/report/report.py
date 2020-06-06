import sys

from peon.src.lint.report.report_channels import ReportChannels


class Report:

    NOTHING = ''

    def __init__(self, text: str, channel: str):
        self.text = text
        self.channel = channel

    def send(self):
        if self.channel == ReportChannels.stdout:
            return self.to_stdout()
        elif self.channel == ReportChannels.file:
            return self.to_file()

    def to_stdout(self) -> bool:
        if not self.text:
            return False
        print(self.text, file=sys.stdout)
        return True

    def to_file(self) -> bool:
        if not self.text:
            return False
        with open(ReportChannels.file, 'w') as result:
            result.write(self.text)
        return True
