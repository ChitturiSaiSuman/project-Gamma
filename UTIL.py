import base64, tkinter, tkinter.filedialog, os, sys, zipfile
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class UTIL:
    def pick_directory():
        root = tkinter.Tk()
        root.withdraw()

        directory_path = tkinter.filedialog.askdirectory(title="Select a Directory")
        return directory_path

    def zip_directory(directory_path, output_path):
        base_name = os.path.basename(directory_path)
        zip_file_path = os.path.join(output_path, f"{base_name}.zip")

        with zipfile.ZipFile(zip_file_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(directory_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arc_name = os.path.relpath(file_path, directory_path)
                    zipf.write(file_path, arc_name)

        return zip_file_path
    
    def read_bytes_from_file(path: str) -> bytes:
        try:
            with open(path, 'rb') as file:
                data = file.read()
            return data
        except Exception as e:
            print(f"Unable to read from file {path}. Exception: {e}")
            sys.exit(1)

class ENIGMA:
    def get_key(password: str) -> Fernet:
        salt = b'salt_'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000
        )
        key = Fernet(base64.urlsafe_b64encode(kdf.derive(password.encode())))
        return key
    
    def encrypt(raw_data: bytes, password: str) -> bytes:
        key = ENIGMA.get_key(password)
        encrypted_data = key.encrypt(raw_data)
        return encrypted_data
    
    def decrypt(encrypted_data: bytes, password: str) -> bytes:
        key = ENIGMA.get_key(password)
        raw_data = key.decrypt(encrypted_data)
        return raw_data


if __name__ == "__main__":
    selected_directory = UTIL.pick_directory()
    print("Selected Directory:", selected_directory)

    output_directory = "."

    zip_path = UTIL.zip_directory(selected_directory, output_directory)
    print("Zip file created:", zip_path)

    encryption_password = "hello"
    zip_bytes_raw = UTIL.read_bytes_from_file(zip_path)

    zip_bytes_encrypted = ENIGMA.encrypt(zip_bytes_raw, encryption_password)

    destination_file = 

    print("Encrypted zip file created:", encrypted_zip_path)

