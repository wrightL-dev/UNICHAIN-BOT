import os
import time
import random
import requests
from web3 import Web3
from dotenv import load_dotenv
from colorama import Fore, init

init(autoreset=True)

load_dotenv()

web3_sepolia = Web3(Web3.HTTPProvider(os.getenv("SEPOLIA_RPC_URL")))
web3_unichain = Web3(Web3.HTTPProvider(os.getenv("UNICHAIN_RPC_URL")))

sender_address = os.getenv("SENDER_ADDRESS")
private_key = os.getenv("PRIVATE_KEY")

print(Fore.MAGENTA + "===============================")
print(Fore.CYAN + "UNICHAIN TESTNET")
print(Fore.GREEN + "BY: wrightL")
print(Fore.YELLOW + "GITHUB: https://github.com/wrightL-dev")
print(Fore.RED + "TELEGRAM CHANNEL: t.me/tahuri01")
print(Fore.LIGHTYELLOW_EX + "USDT/TRX: TUSnNMKkL8RvLTWmv7pCPUFSupy6apAbvT")
print(Fore.MAGENTA + "===============================")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to fetch transaction count from Unichain
def fetch_transaction_count():
    url = f'https://unichain-sepolia.blockscout.com/api/v2/addresses/{sender_address}/counters'
    
    headers = {
        'accept': '*/*',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'Referer': f'https://unichain-sepolia.blockscout.com/address/{sender_address}?tab=txs',
        'Referrer-Policy': 'origin-when-cross-origin'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses

        # Extract transactions_count from the response if it exists
        data = response.json()
        transactions_count = data.get('transactions_count', 'N/A')

        print(Fore.GREEN + f'Total Transaksi: {transactions_count}')

    except requests.exceptions.RequestException as e:
        print(f'Error fetching data: {e}')

def bridge_sepolia_to_unichain(amount_to_bridge):
    clear_console()
    try:
        print('Memulai proses bridge dari Sepolia ke Unichain...')

        nonce = web3_sepolia.eth.getTransactionCount(sender_address)
        gas_price = web3_sepolia.eth.gas_price

        tx_sepolia = {
            'from': sender_address,
            'to': sender_address,  
            'value': web3_sepolia.toWei(amount_to_bridge, 'ether'),
            'gas': 21000,
            'gasPrice': gas_price,
            'nonce': nonce,
            'chainId': 11155111  
        }

        signed_tx_sepolia = web3_sepolia.eth.account.signTransaction(tx_sepolia, private_key)
        tx_hash = web3_sepolia.eth.sendRawTransaction(signed_tx_sepolia.rawTransaction)
        
        print(Fore.GREEN + 'Transaksi Sepolia berhasil!\n')
        print(Fore.MAGENTA + '=====================================================================================')
        print(Fore.LIGHTYELLOW_EX + 'BUKTI TRANSAKSI\n')
        print(Fore.LIGHTYELLOW_EX + f'TX HASH ID: {tx_hash.hex()}')
        print(Fore.LIGHTYELLOW_EX + f'LINK: https://sepolia.etherscan.io/tx/{tx_hash.hex()}')
        print(Fore.LIGHTYELLOW_EX + f'JUMLAH: {amount_to_bridge:.8f} ETH')
        print(Fore.MAGENTA + '=====================================================================================')
        print(Fore.GREEN + 'Bridge selesai dari Sepolia ETH ke Unichain!')
    except Exception as e:
        print(f'Terjadi kesalahan saat proses bridge: {e}')


def bridge_unichain_to_sepolia(to_address, amount_to_bridge):
    clear_console()
    try:
        print('Memulai proses bridge dari Unichain ke Sepolia...')

        nonce = web3_unichain.eth.getTransactionCount(sender_address)
        gas_price = web3_unichain.eth.gas_price

        tx_unichain = {
            'from': sender_address,
            'to': to_address,
            'value': web3_unichain.toWei(amount_to_bridge, 'ether'),
            'gas': 21000,
            'gasPrice': gas_price,
            'nonce': nonce,
            'chainId': 1301  
        }

        signed_tx_unichain = web3_unichain.eth.account.signTransaction(tx_unichain, private_key)
        tx_hash = web3_unichain.eth.sendRawTransaction(signed_tx_unichain.rawTransaction)
        
        print(Fore.GREEN + 'Transaksi Unichain berhasil!\n')
        print(Fore.MAGENTA + '=====================================================================================')
        print(Fore.LIGHTYELLOW_EX + 'BUKTI TRANSAKSI\n')
        print(Fore.LIGHTYELLOW_EX + f'TX HASH ID: {tx_hash.hex()}')
        print(Fore.LIGHTYELLOW_EX + f'LINK: https://unichain-sepolia.blockscout.com/tx/{tx_hash.hex()}')
        print(Fore.LIGHTYELLOW_EX + f'JUMLAH: {amount_to_bridge:.8f} ETH')
        print(Fore.MAGENTA + '=====================================================================================')
        print(Fore.GREEN + 'Bridge selesai dari Unichain ke Sepolia!')
    except Exception as e:
        print(f'Terjadi kesalahan saat proses bridge: {e}')


def send_eth(to_address, amount_to_send):
    clear_console()
    try:
        print('Memulai pengiriman ETH...')

        nonce = web3_unichain.eth.getTransactionCount(sender_address)
        gas_price = web3_unichain.eth.gas_price

        tx = {
            'from': sender_address,
            'to': to_address,
            'value': web3_unichain.toWei(amount_to_send, 'ether'),
            'gas': 21000,
            'gasPrice': gas_price,
            'nonce': nonce,
            'chainId': 1301
        }

        signed_tx = web3_unichain.eth.account.signTransaction(tx, private_key)
        tx_hash = web3_unichain.eth.sendRawTransaction(signed_tx.rawTransaction)
        
        print(Fore.GREEN + 'Transaksi berhasil!\n')
        print(Fore.MAGENTA + '=====================================================================================')
        print(Fore.LIGHTYELLOW_EX + 'BUKTI TRANSAKSI\n')
        print(Fore.LIGHTYELLOW_EX + f'TX HASH ID: {tx_hash.hex()}')
        print(Fore.LIGHTYELLOW_EX + f'LINK: https://unichain-sepolia.blockscout.com/tx/{tx_hash.hex()}')
        print(Fore.LIGHTYELLOW_EX + f'JUMLAH: {amount_to_send:.18f} ETH')
        print(Fore.MAGENTA + '=====================================================================================')
    except Exception as e:
        print(f'Terjadi kesalahan saat pengiriman: {e}')

def main():
    while True:
        print(Fore.MAGENTA + "\n===============================")
        print(Fore.YELLOW + "\nPilih opsi:")
        print(Fore.YELLOW + "1. Bridge Sepolia ETH > Unichain")
        print(Fore.YELLOW + "2. Bridge Unichain > Sepolia ETH")
        print(Fore.YELLOW + "3. Kirim Unichain Ke Wallet Orang Lain")
        print(Fore.YELLOW + "4. Cek Total Transaksi")
        print(Fore.YELLOW + "5. Keluar")

        choice = input("Masukkan pilihan (1/2/3/4/5): ")

        if choice == '1':
            amount = input("Masukkan jumlah ETH yang akan di-bridge (default 0.01): ")
            if amount == "":
                amount = 0.01
            else:
                amount = float(amount)

            bridge_count = input("Ingin berapa kali bridge? ")
            if bridge_count.isdigit():
                bridge_count = int(bridge_count)
            else:
                print("Jumlah yang dimasukkan tidak valid, menggunakan 1 sebagai default.")
                bridge_count = 1

            for i in range(bridge_count):
                bridge_sepolia_to_unichain(amount)
                if i < bridge_count - 1:
                    print("Menunggu 15 detik sebelum transaksi berikutnya...")
                    time.sleep(15)

        elif choice == '2':
            amount = input("Masukkan jumlah ETH yang akan di-bridge (default 0.01): ")
            if amount == "":
                amount = 0.01
            else:
                amount = float(amount)

            bridge_count = input("Ingin berapa kali bridge? ")
            if bridge_count.isdigit():
                bridge_count = int(bridge_count)
            else:
                print("Jumlah yang dimasukkan tidak valid, menggunakan 1 sebagai default.")
                bridge_count = 1

            for i in range(bridge_count):
                bridge_unichain_to_sepolia(sender_address, amount)
                if i < bridge_count - 1:
                    print("Menunggu 15 detik sebelum transaksi berikutnya...")
                    time.sleep(15)
        elif choice == '3':
            solo_or_file = input("Apakah Anda ingin memasukkan alamat wallet satu per satu (s) atau menggunakan file (f)? (s/f): ")

            if solo_or_file.lower() == 's':
                to_address = input("Masukkan alamat wallet tujuan: ")
                if Web3.isAddress(to_address):
                    random_amount = random.uniform(0.00000005, 0.00000010)
                    print(f'Mengirim jumlah ETH acak: {random_amount:.18f} ETH')
                    send_eth(to_address, random_amount)
                    print("Menunggu 15 detik sebelum melanjutkan...")
                    time.sleep(15)
                else:
                    print("Alamat wallet tidak valid.")

            elif solo_or_file.lower() == 'f':
                file_name = input("Masukkan nama file yang berisi alamat wallet (contoh: wallets.txt): ")
                try:
                    with open(file_name, 'r') as file:
                        addresses = file.readlines()

                        for address in addresses:
                            address = address.strip()
                            if Web3.isAddress(address):
                                random_amount = random.uniform(0.000000001, 0.00000002)
                                print(f'Mengirim {random_amount:.18f} ETH ke {address}')
                                send_eth(address, random_amount)
                                print("Menunggu 15 detik sebelum melanjutkan ke wallet berikutnya...")
                                time.sleep(15)
                            else:
                                print(f'Alamat tidak valid: {address}')
                except FileNotFoundError:
                    print(f'File {file_name} tidak ditemukan.')
            else:
                print('Pilihan tidak valid.')

        elif choice == '4':
            print("Cek Total Transaksi:")
            fetch_transaction_count()

        elif choice == '5':
            print("Keluar dari program.")
            break

        else:
            print('Pilihan tidak valid.')


if __name__ == "__main__":
    main()
