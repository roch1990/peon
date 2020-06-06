import sys

from peon.src.lint.report.report_channels import ReportChannels


class Report:

    NOTHING = ''

    def __init__(self, text: str, channel: str):
        self.text = text
        self.channel = channel

    def send(self):
        if self.channel == ReportChannels.stdout:
            self.to_stdout()
        elif self.channel == ReportChannels.file:
            self.to_file()

    def to_stdout(self):
        if not self.text:
            return
        print(self.text, file=sys.stdout)

    def to_file(self):
        if not self.text:
            return
        with open(ReportChannels.file, 'w') as result:
            result.write(self.text)
