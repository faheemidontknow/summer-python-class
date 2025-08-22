# 🔐 Vigenère Cipher (Python Implementation)

This project demonstrates a simple implementation of the **Vigenère Cipher** in Python.  
The Vigenère Cipher is a classic encryption technique that uses a **secret key** to shift letters of a message, making it unreadable without the key.

---

## 📂 Code Overview

### Files
- `main.py` → Contains the cipher logic and a working example.

---

## ⚙️ How the Code Works

1. **Inputs:**
   - `text` → The encrypted or plain message you want to process.  
   - `custom_key` → The secret keyword used to encrypt or decrypt the message.

2. **Functions:**
   - `vigenere(message, key, direction=1)`  
     Core function that shifts each character by an amount based on the key.  
     - `direction = 1` → Encrypt  
     - `direction = -1` → Decrypt  
   - `encrypt(message, key)`  
     Wrapper function that calls `vigenere()` with `direction = 1`.
   - `decrypt(message, key)`  
     Wrapper function that calls `vigenere()` with `direction = -1`.

3. **Output:**  
   The program prints:
   - The given encrypted text  
   - The key used  
   - The final decrypted text  

---

## 📜 Example Run

```python
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

# Decrypt the given text
decryption = decrypt(text, custom_key)

print(decryption)
```

✅ Output (Decrypted Text):

```
encryption is simple
```

---

## 🔄 Switching Between Encryption & Decryption

Right now, the code **separates encryption and decryption** using two wrapper functions:

```python
def encrypt(message, key):
    return vigenere(message, key)   # direction = 1 (default)

def decrypt(message, key):
    return vigenere(message, key, -1)   # direction = -1
```

### 🛠 How to Tweak It

If you want to **choose dynamically** whether to encrypt or decrypt, you can tweak the code like this:

```python
# Single function to handle both
def run_cipher(message, key, mode="encrypt"):
    if mode == "encrypt":
        return vigenere(message, key, 1)   # forward shift
    elif mode == "decrypt":
        return vigenere(message, key, -1)  # backward shift
```

Usage:

```python
# Encrypting
encrypted = run_cipher("encryption is simple", "happycoding", "encrypt")
print(encrypted)

# Decrypting
decrypted = run_cipher(encrypted, "happycoding", "decrypt")
print(decrypted)
```

---

## ✅ Summary

- This code shows how the **Vigenère Cipher** works in Python.  
- You can **encrypt** with `encrypt()` and **decrypt** with `decrypt()`.  
- By tweaking to a single `run_cipher()` function, you can control both operations by passing a **mode parameter**.  

---

🔥 With this setup, you can quickly switch between encrypting and decrypting messages just by changing one word (`"encrypt"` or `"decrypt"`).
