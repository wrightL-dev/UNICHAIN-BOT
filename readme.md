# Bridge antara Sepolia dan Unichain, Juga transaksi Unichain Ke Wallet Orang Lain

Proyek ini adalah skrip Python yang memungkinkan pengguna untuk melakukan transaksi antara jaringan Sepolia dan Unichain. Anda dapat melakukan bridging dari Sepolia ke Unichain dan sebaliknya, serta mengirim Unichain ke alamat wallet lain.

## Fitur

- **Bridge Sepolia ETH ke Unichain**
- **Bridge Unichain ke Sepolia ETH**
- **Kirim Unichain ke alamat wallet lain**
- **Pengaturan jumlah transaksi dan durasi**

## Persyaratan

Sebelum menjalankan proyek ini, pastikan Anda telah menginstal:

- Python 3.x
- pip (Python package installer)

## Instalasi

1. **Clone repository ini:**
   ```
   git clone https://github.com/wrightL-dev/UNICHAIN-BOT
   cd bridge-eth-sepolia-unichain

2. **Buat dan aktifkan virtual environment (opsional tetapi disarankan)**
   ```
    python -m venv venv
    source venv/bin/activate  # Untuk Linux/macOS
    venv\Scripts\activate  # Untuk Windows

3. **Instal paket yang diperlukan:**

   ```pip install web3 python-dotenv colorama```

4. **nano .env**
   ```
   SEPOLIA_RPC_URL=https://ethereum-sepolia-rpc.publicnode.com
   UNICHAIN_RPC_URL=https://sepolia.unichain.org/
   SENDER_ADDRESS=<ALAMAT_PENGIRIM>
   PRIVATE_KEY=<KUNCI_PRIVAT>

4. **python3 unichain.py**

5. Penggunaan
Setelah menjalankan skrip, Anda akan disajikan dengan menu untuk memilih opsi yang diinginkan:
```
Bridge Sepolia ETH > Unichain
Bridge Unichain > Sepolia ETH
Kirim Ke Wallet Orang Lain
Keluar
Ikuti petunjuk yang ada untuk melakukan transaksi yang diinginkan.

```
Dukungan
Jika Anda memiliki pertanyaan atau butuh bantuan lebih lanjut, silakan bergabung dengan saluran Telegram kami di t.me/tahuri01.

Lisensi
Proyek ini dilisensikan di bawah MIT License
