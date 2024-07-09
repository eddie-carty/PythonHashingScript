import hashlib

def calculate_hash(file_path, hash_type):
    """Calculate hash of a file."""
    hash_algo = hashlib.new(hash_type)
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hash_algo.update(chunk)
    return hash_algo.hexdigest()

def main():
    file_path = input("Enter the path of the file: ")
    
    try:
        md5_hash = calculate_hash(file_path, "md5")
        sha1_hash = calculate_hash(file_path, "sha1")
        sha256_hash = calculate_hash(file_path, "sha256")
        
        print(f"MD5 Hash: {md5_hash}")
        print(f"SHA-1 Hash: {sha1_hash}")
        print(f"SHA-256 Hash: {sha256_hash}")
        
        # If we know the good hash values we can compare them using
        # known_md5 = "..."
        # known_sha1 = "..."
        # known_sha256 = "..."
        
        # Which would look like
        # if md5_hash == known_md5:
        #     print("MD5 Hash matches.")
        
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except PermissionError:
        print(f"Permission denied: {file_path}")

if __name__ == "__main__":
    main()