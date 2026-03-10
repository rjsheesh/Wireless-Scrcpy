# Auto Wireless Scrcpy Connector
**Developed By: fabiTECH**

A smart and automated GUI tool built with Python (PySide6) to easily connect your Android device to your PC via Wi-Fi using `scrcpy`. Forget about manually typing IP addresses or running CMD commands—this tool does everything for you with a single click!

---

## ✨ Features
* **Automated IP Detection:** Automatically finds your phone's Wi-Fi IP address.
* **One-Click Wireless Connection:** Seamlessly switches your adb connection from USB to TCP/IP.
* **Sleek GUI:** A beautiful, dark-themed hacker-style interface built with PySide6.
* **Real-time Logs:** See exactly what is happening in the background through the log console.
* **No UI Freezing:** Uses multi-threading (`QThread`) to ensure the app runs smoothly without hanging.

---

## 📥 Download & Installation

1. **Download Scrcpy:** First, you need the official `scrcpy` files. Download the Windows version from the link below:
   👉 [Download scrcpy-win64-v3.3.4.zip](https://github.com/Genymobile/scrcpy/releases/download/v3.3.4/scrcpy-win64-v3.3.4.zip)

2. **Extract the Files:**
   Extract the downloaded `.zip` file into a folder on your PC.

3. **Place the Script:**
   Put the `scrcpy_gui.exe` file directly inside the extracted `scrcpy` folder (it must be in the same location as `scrcpy.exe` and `adb.exe`).

4. **Install Requirements:**

## 🚀 How to Connect

Follow these simple steps to mirror your phone wirelessly:

* **Step 1:** Enable **USB Debugging** from the Developer Options on your Android phone.
* **Step 2:** Connect your phone and your PC to the same Wi-Fi network.
* **Step 3:** Connect your phone to the PC using a USB Cable (This is only required for the initial handshake).
    * *Note: If a prompt appears on your phone asking to "Allow USB debugging", tap **OK/Allow**.*
* **Step 4:** Run the Python script:
    ```bash
    fabi_scrcpy_gui.py
    ```
* **Step 5:** Click the **"Connect & Start Scrcpy"** button on the application.
* **Step 6:** Wait for the success message in the log box. Once connected, you can disconnect the USB cable! `scrcpy` will launch automatically over Wi-Fi.

---

## ⚠️ Troubleshooting

* **"IP not found" error:** Ensure your phone is not asleep and is properly connected to the Wi-Fi.
* **"adb.exe not found":** Make sure you placed the Python script in the exact same folder as the extracted `scrcpy` files.
* **Connection Timeout:** Turn your phone's Wi-Fi off and on again, then retry.

---
*Created with ❤️ by **fabiTECH***
