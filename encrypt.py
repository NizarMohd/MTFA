from cryptography.fernet import Fernet
# do for each week

def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        file_data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(file_data)

    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

# Generate a random encryption key
key = Fernet.generate_key()
print(key)

# Specify the input and output file paths
input_file = 'week1.py'
output_file = 'C:/Users/User/Documents/tutorial/venv/WeeklyFolders/week1/data.py'

# Encrypt the file
encrypt_file(input_file, output_file, key)