#!/usr/bin/python3.6
from phe import paillier
import csv, time

def enc_median_housing_values(public_key, num_lst):
    return [public_key.encrypt(x) for x in num_lst]

def dec_median_housing_values(private_key, enc_lst):
    return [private_key.decrypt(x) for x in enc_lst]

def main():
    with open('housing.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        median_house_values = []
        for row in reader:
            median_house_values.append(float(row['median_house_value']))

    #Generate private and public keys
    public_key, private_key = paillier.generate_paillier_keypair()

    inp_size = int(input("First n median house values: "))
    secret_number_list = median_house_values[:inp_size]
    print(f"Numbers to be encrypted: {secret_number_list}")

    #Time the encrypt function with different input sizes
    start = time.perf_counter()
    encrypted_number_list = enc_median_housing_values(public_key, secret_number_list) #[public_key.encrypt(x) for x in secret_number_list]
    stop = time.perf_counter()
    print(f"Encrypted numbers: {encrypted_number_list}")
    print(f"Time to encrypt {inp_size} values: {stop - start:0.4f} seconds")

    #Time the decrypt func with different input sizes
    start = time.perf_counter()
    res = dec_median_housing_values(private_key, encrypted_number_list)
    stop = time.perf_counter()
    print(f"Decrypted numbers: {res}")
    print(f"Time to decrypt {inp_size} values: {stop - start:0.4f} seconds")

    #Calculate average of plaintext data
    start = time.perf_counter()
    unenc_avg = sum(secret_number_list) / len(secret_number_list)
    stop = time.perf_counter()
    print(f"Calculate average of plaintext data: {unenc_avg}")
    print(f"Time to calc avg on plaintext data: {stop - start:0.4f} seconds")

    #Calculate average of encrypted data
    start = time.perf_counter()
    average = sum(encrypted_number_list) / len(encrypted_number_list)
    stop = time.perf_counter()
    print(f"Time to calc avg on encrypted data: {stop - start:0.4f} seconds")

    #Decrypting the calculation result
    print(f"Decrypting the calculation result on the encrypted data: {private_key.decrypt(average)}")

main()
