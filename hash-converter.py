# Project: Hash Converter
# Description: Script converts input text into various hash formats using hashlib.

# Import modules.
import hashlib # hashlib for hashing functions
import sys # sys for system exit

# Define function.
def get_hashes(text_to_hash):
    
    try:
        text_bytes = text_to_hash.encode('utf-8')
        # Encodes string to bytes using UTF-8 encoding.
        # 'utf-8' is the most common and standard encoding.

    except Exception as e:
        print(f"Error encoding string: {e}")
        return

    print(f"\n--- Hashes for: '{text_to_hash}' ---")

    algorithms = sorted(hashlib.algorithms_guaranteed)
    # Use all algorithms guaranteed to be on the system
    # Using sorted() just makes the output cleaner

    for alg_name in algorithms:
        # Check algorithm is supported by this Python environment.
        if alg_name not in hashlib.algorithms_available:
            print(f"{alg_name.upper():<10}: Not available")
            continue
            
        # Create a new hash object using the algorithm's name.
        hash_obj = hashlib.new(alg_name)
        
        # Update the hash object with the bytes of our text.
        hash_obj.update(text_bytes)
        
        if "shake" in alg_name:
            # Check if the algorithm is an XOF (like SHAKE).
            # Requies a legnth argument for the digest.
            # 32 bytes (64 hex chars) to match SHA-256 is provided.
            hex_digest = hash_obj.hexdigest(32)
        else:
            hex_digest = hash_obj.hexdigest()
        
        print(f"{alg_name.upper():<12}: {hex_digest}")
        # Alignment space may be increased to 10 or 12.

# --- Main part of the script ---
if __name__ == "__main__":
    try:
        # Get user input
        user_input = input("Enter the text you want to hash: ")
        
        if not user_input:
            print("No input provided. Exiting.")
        else:
            get_hashes(user_input)
            
    except KeyboardInterrupt:
        print("\nOperation cancelled by user. Exiting.")
        sys.exit(0)