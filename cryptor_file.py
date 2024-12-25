from cryptography.fernet import Fernet

# توليد المفتاح وتخزينه في ملف
def generate_key():
    key = Fernet.generate_key()  # توليد مفتاح عشوائي
    with open("key.key", "wb") as key_file:
        key_file.write(key)  # حفظ المفتاح في ملف
    print("Key generated and saved as 'key.key'")

# تشفير الملف باستخدام المفتاح الذي تم توليده
def encrypt_file(file_path):
    try:
        with open("key.key", "rb") as key_file:
            key = key_file.read()  # تحميل المفتاح من الملف
        fernet = Fernet(key)

        with open(file_path, "rb") as file:
            file_data = file.read()  # قراءة محتوى الملف

        encrypted_data = fernet.encrypt(file_data)  # تشفير البيانات

        with open(file_path, "wb") as file:
            file.write(encrypted_data)  # حفظ الملف المشفر

        print(f"File '{file_path}' has been encrypted successfully!")
    except Exception as e:
        print(f"Error occurred during encryption: {e}")

# فك تشفير الملف باستخدام المفتاح
def decrypt_file(file_path):
    try:
        with open("key.key", "rb") as key_file:
            key = key_file.read()  # تحميل المفتاح من الملف
        fernet = Fernet(key)

        with open(file_path, "rb") as file:
            encrypted_data = file.read()  # قراءة البيانات المشفرة

        decrypted_data = fernet.decrypt(encrypted_data)  # فك تشفير البيانات

        with open(file_path, "wb") as file:
            file.write(decrypted_data)  # حفظ البيانات المفكوكة

        print(f"File '{file_path}' has been decrypted successfully!")
    except Exception as e:
        print(f"Error occurred during decryption: {e}")

# واجهة تفاعلية للمستخدم
def interactive_menu():
    while True:
        print("\nFile Encryption and Decryption Tool")
        print("1. Generate Key (first-time use only)")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Exit")

        choice = input("Please choose an option (1/2/3/4): ")

        if choice == "1":
            generate_key()  # توليد المفتاح عند أول استخدام فقط
        elif choice == "2":
            file_path = input("Enter the file path to encrypt: ")
            encrypt_file(file_path)
        elif choice == "3":
            file_path = input("Enter the file path to decrypt: ")
            decrypt_file(file_path)
        elif choice == "4":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please try again.")

# بدء البرنامج
if __name__ == "__main__":
    interactive_menu()
