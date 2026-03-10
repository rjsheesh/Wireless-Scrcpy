import sys
import subprocess
import time
import re
import os
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtGui import QFont

# Using QThread class for background tasks
class WorkerThread(QThread):
    log_signal = Signal(str)

    def run(self):
        self.log_signal.emit("[!] Ensure your phone is connected to the PC via USB first!\n")
        
        def get_device_ip():
            try:
                # Using CREATE_NO_WINDOW to prevent black CMD popup in Windows
                result = subprocess.run(['adb', 'shell', 'ip', 'route'], capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
                match = re.search(r'src\s+(\d+\.\d+\.\d+\.\d+)', result.stdout)
                if match:
                    return match.group(1)
            except Exception as e:
                self.log_signal.emit(f"[-] Error finding IP: {e}")
            return None

        self.log_signal.emit("[+] Enabling TCP/IP port 5555...")
        subprocess.run(['adb', 'tcpip', '5555'], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
        time.sleep(3)

        self.log_signal.emit("[+] Searching for phone's Wi-Fi IP...")
        device_ip = get_device_ip()

        if device_ip:
            self.log_signal.emit(f"[+] Phone IP found: {device_ip}")
            self.log_signal.emit(f"[+] Connecting to {device_ip}...")
            
            subprocess.run(['adb', 'connect', f'{device_ip}:5555'], capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
            time.sleep(2)
            
            self.log_signal.emit("\n[!] Connection successful! You can now disconnect the USB cable.")
            self.log_signal.emit("[+] Starting Scrcpy...\n")
            
            # Opening Scrcpy
            subprocess.Popen(['scrcpy'], creationflags=subprocess.CREATE_NO_WINDOW)
        else:
            self.log_signal.emit("\n[-] Phone IP not found! Is the phone connected to the same Wi-Fi as the PC?")

# Main GUI class
class ScrcpyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Auto Wireless Scrcpy - fabiTECH")
        self.resize(550, 450)

        # UI design and color setup
        self.setStyleSheet("""
            /* Developed By: fabiTECH */
            QWidget {
                background-color: #121212;
            }
            QTextEdit {
                background-color: #000000;
                color: #00ff00;
                font-family: Consolas;
                font-size: 14px;
                border: 2px solid #333;
                padding: 5px;
            }
            QPushButton {
                background-color: #1e88e5;
                color: #ffffff;
                padding: 12px;
                font-size: 16px;
                font-weight: bold;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #1565c0;
            }
            QPushButton:disabled {
                background-color: #555555;
                color: #aaaaaa;
            }
        """)

        layout = QVBoxLayout()

        # Title label
        self.title_label = QLabel("Auto Wireless Scrcpy Connector\nDeveloped By: fabiTECH")
        self.title_label.setFont(QFont("Arial", 16, QFont.Bold))
        self.title_label.setStyleSheet("color: white;")
        self.title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title_label)

        # Text box to show logs
        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)
        layout.addWidget(self.log_box)

        # Connect button
        self.btn_connect = QPushButton("Connect & Start Scrcpy")
        self.btn_connect.clicked.connect(self.start_connection)
        layout.addWidget(self.btn_connect)

        self.setLayout(layout)

        # Thread setup
        self.worker = WorkerThread()
        self.worker.log_signal.connect(self.append_log)
        self.worker.finished.connect(self.on_finished)

    def start_connection(self):
        self.log_box.clear()
        self.btn_connect.setEnabled(False)
        self.btn_connect.setText("Processing... Please Wait")
        self.worker.start()

    def append_log(self, text):
        self.log_box.append(text)
        # For automatic scrolling to the bottom
        scrollbar = self.log_box.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def on_finished(self):
        self.btn_connect.setEnabled(True)
        self.btn_connect.setText("Connect & Start Scrcpy")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ScrcpyApp()
    window.show()
    sys.exit(app.exec())