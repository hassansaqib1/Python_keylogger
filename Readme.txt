
# Python Keylogger Script

## Description
This Python keylogger script captures keystrokes and stores them in a log file. Optionally, it can also send the log file to a specified email address when it reaches a certain size. The script is designed to run on Windows, Linux, and macOS without requiring elevated privileges.

---

## Features:
1. Logs all keystrokes in a hidden file.
2. Optionally sends keylogs via email when the log file exceeds a specified size.
3. Hides the script after running.
4. Runs without needing `sudo` or administrator rights.
5. Customizable email sending (optional) with a flag to enable or disable email.
6. Checks for network connectivity before attempting to send emails.
7. Platform-independent; works on Linux, Windows, and macOS.

---

## Requirements:
- **Python 3.x**
- **pynput library** for capturing keystrokes.
- **smtplib library** for sending emails (standard Python library).

---

## Installation:
1. **Install dependencies**:

    ```bash
    pip install pynput
    ```

2. **Configure Email Settings**:
   In the script, edit the following variables to match your configuration:

   - `EMAIL_ADDRESS`: Your email address.
   - `EMAIL_PASSWORD`: Your email password (app password recommended if using Gmail).
   - `RECIPIENT_EMAIL`: The email address to which the logs should be sent.

3. **Log File Path**:
   By default, the log file is stored in:
   
   - Linux/macOS: `~/.local/system32_keylog.txt`
   - Windows: `%USERPROFILE%\.local\system32_keylog.txt`
   
   You can change this path by editing the `LOG_FILE` variable in the script.

---

## Usage:
1. **Run the Script**:
   The script will automatically begin logging keystrokes after execution. It will hide itself (Windows only), and logs will be saved in the file specified by `LOG_FILE`.

2. **Enable/Disable Email Sending**:
   To control whether the logs are sent via email:
   - Set `EMAIL_FLAG = 1` to enable email sending.
   - Set `EMAIL_FLAG = 0` to disable email sending.

3. **Network Connectivity Check**:
   The script will check if the machine is connected to the internet before sending emails. If no network is detected, it will keep logging keystrokes and retry email sending once the file size limit is reached.

4. **File Size Trigger for Email**:
   By default, the script sends the log file once it exceeds **5 KB** in size. This limit can be changed by modifying the `LOG_SIZE_LIMIT` variable.

---

## Stopping the Script:
To stop the keylogger, you can use **Ctrl + C** in the terminal or kill the process in the task manager or activity monitor.

---

## Deleting the Keylogger:
1. **Linux/macOS**:
    - Delete the log file: `~/.local/system32_keylog.txt`
    - Delete the script file itself.

2. **Windows**:
    - Delete the log file: `%USERPROFILE%\.local\system32_keylog.txt`
    - Delete the script file, which may be hidden if it was executed.

---

## Ethical Use Warning:
This keylogger script is for **educational purposes** only. Unauthorized keylogging and data capture is illegal and unethical. Use this tool responsibly and with proper consent.

---

## Example Command:

```bash
python3 keylogger.py
```

---

## License:
This project is provided as-is, without any warranty. The creator is not responsible for any misuse of this script.

---

### END
