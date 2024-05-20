# rsa_decryption_simulation.py

from Crypto.Cipher import PKCS1_OAEP
import time
import logging
from tqdm import tqdm

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] - %(levelname)s - %(message)s')

class TqdmPeriods(tqdm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, bar_format="[{bar}]", ascii="." * 10)

def decrypt(private_key, encrypted_data):
    """
    Simulates the decryption process and logs the decryption time.
    s
    :param private_key: RSA private key used for decryption
    :param encrypted_data: Data to be decrypted
    :return: Decrypted data
    """
    logging.info("Starting decryption process")
    
    # Start timing the decryption process
    start_time = time.time()
    
    # Create a PKCS1_OAEP cipher object with the private key for decryption
    cipher_rsa = PKCS1_OAEP.new(private_key)
    

    for _ in TqdmPeriods(range(100), desc="Decrypting", ncols=75):
        time.sleep(0.01)
    
    decrypted_data = cipher_rsa.decrypt(encrypted_data)
  
    end_time = time.time()
    
    # Calculate the time taken for decryption
    decryption_time = end_time - start_time
    logging.info(f"Decryption took {decryption_time:.6f} seconds")
    
    return decrypted_data
