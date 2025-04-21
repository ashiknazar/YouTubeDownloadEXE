import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QLineEdit, QProgressBar, QLabel, QFileDialog
)
from PyQt5.QtCore import QThread, pyqtSignal
import yt_dlp


class DownloaderThread(QThread):
    progress = pyqtSignal(int)
    status = pyqtSignal(str)

    def __init__(self, url, save_path):
        super().__init__()
        self.url = url
        self.save_path = save_path

    def run(self):
        def hook(d):
            if d['status'] == 'downloading':
                total = d.get('total_bytes') or d.get('total_bytes_estimate')
                downloaded = d.get('downloaded_bytes', 0)
                if total:
                    percent = int(downloaded * 100 / total)
                    self.progress.emit(percent)
            elif d['status'] == 'finished':
                self.progress.emit(100)
                self.status.emit("✅ Download complete!")

        opts = {
            'outtmpl': f'{self.save_path}/%(title)s.%(ext)s',
            'progress_hooks': [hook],
        }

        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download([self.url])
        except Exception as e:
            self.status.emit(f"❌ Error: {str(e)}")


class YouTubeDownloader(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Downloader")
        self.setGeometry(200, 200, 400, 200)

        layout = QVBoxLayout()

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Paste YouTube URL here")
        layout.addWidget(self.url_input)

        self.download_btn = QPushButton("Download")
        self.download_btn.clicked.connect(self.start_download)
        layout.addWidget(self.download_btn)

        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)

        self.status_label = QLabel("")
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    def start_download(self):
        url = self.url_input.text().strip()
        if not url:
            self.status_label.setText("❗ Please enter a URL.")
            return

        # Ask user where to save
        save_path = QFileDialog.getExistingDirectory(self, "Select Download Folder")
        if not save_path:
            self.status_label.setText("❗ Download cancelled.")
            return

        self.download_btn.setEnabled(False)
        self.status_label.setText("⬇️ Downloading...")

        self.downloader = DownloaderThread(url, save_path)
        self.downloader.progress.connect(self.progress_bar.setValue)
        self.downloader.status.connect(self.show_status)
        self.downloader.start()

    def show_status(self, msg):
        self.status_label.setText(msg)
        self.download_btn.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YouTubeDownloader()
    window.show()
    sys.exit(app.exec_())
