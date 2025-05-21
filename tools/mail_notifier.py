# tools/mail_notifier.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
from common.config import ConfigLoader


class EmailSender:
    def __init__(self):
        config = ConfigLoader().get_interface_config()
        self.smtp_server = config.get("smtp_server", "smtp.example.com")
        self.smtp_port = config.get("smtp_port", 587)
        self.sender = config.get("email_user", "autotest@example.com")
        self.password = config.get("email_password", "your_password")

    def send_report(self, recipients, report_path=None):
        """发送测试报告邮件"""
        msg = MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = ", ".join(recipients)
        msg['Subject'] = "自动化测试报告"

        # 邮件正文
        body = "本次自动化测试执行已完成，报告详情请查看附件。"
        msg.attach(MIMEText(body, 'plain'))

        # 添加报告附件
        if report_path:
            with open(report_path, 'rb') as f:
                attach = MIMEText(f.read(), 'base64', 'utf-8')
                attach["Content-Type"] = 'application/octet-stream'
                attach["Content-Disposition"] = f'attachment; filename="{Path(report_path).name}"'
                msg.attach(attach)

        # 发送邮件
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.sender, self.password)
            server.sendmail(self.sender, recipients, msg.as_string())

        print("测试报告邮件已发送")


if __name__ == "__main__":
    # 示例用法
    sender = EmailSender()
    sender.send_report(
        recipients=["team@example.com"],
        report_path=Path(__file__).parent.parent / "log" / "allure-report" / "index.html"
    )