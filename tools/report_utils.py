# tools/report_utils.py
import shutil
import zipfile
from pathlib import Path
from datetime import datetime


class ReportManager:
    @staticmethod
    def archive_reports():
        """归档测试报告"""
        source_dir = Path(__file__).parent.parent / "log" / "allure-report"
        dest_dir = Path(__file__).parent.parent / "log" / "archive"
        dest_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        zip_path = dest_dir / f"report_{timestamp}.zip"

        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for file in source_dir.rglob('*'):
                zipf.write(file, arcname=file.relative_to(source_dir))

        print(f"报告已归档至：{zip_path}")

    @staticmethod
    def clean_history(days=30):
        """清理历史报告"""
        archive_dir = Path(__file__).parent.parent / "log" / "archive"
        cutoff = datetime.now().timestamp() - days * 86400

        for f in archive_dir.glob("*.zip"):
            if f.stat().st_mtime < cutoff:
                f.unlink()
                print(f"已删除过期报告：{f.name}")


if __name__ == "__main__":
    ReportManager.archive_reports()
    ReportManager.clean_history()