# Card Number Validator (Luhn Algorithm)

This Python program validates a credit or debit card number using the **Luhn Algorithm**, which is widely used in payment systems to check whether a card number is valid.

---

## 📖 How It Works

1. **Input Card Number**  
   The program starts with a sample card number (`'4111-1111-4555-1141'`).  
   Any spaces or dashes are removed so only digits remain.

2. **Reversing the Number**  
   The card number string is reversed because the Luhn algorithm processes digits starting from the rightmost digit.

3. **Processing Digits**
   - **Odd positions (from the right):** Each digit is added directly to a running total.
   - **Even positions (from the right):** Each digit is doubled.  
     - If the result is greater than or equal to 10, the digits are added together (e.g., `12 → 1 + 2 = 3`).
     - The result is added to a second running total.

4. **Checksum Calculation**  
   The sum of odd-position and even-position totals is computed.  
   - If the total is divisible by `10`, the card number is considered **VALID**.  
   - Otherwise, it is **INVALID**.

---

## 🖥️ Example Output

```
VALID!
```

or

```
INVALID!
```

---

## 🛠️ Code Structure

- **`verify_card_number(card_number)`**  
  Implements the Luhn algorithm logic and returns `True` if valid, `False` otherwise.

- **`main()`**  
  - Formats the input card number (removes dashes/spaces).  
  - Calls the verifier function.  
  - Prints `VALID!` or `INVALID!`.

---

## 🔑 Notes About Encryption / Decryption

This program **does not encrypt or decrypt** data — it only validates numbers using the Luhn checksum.  
If you want to work with encryption/decryption (like in the **Vigenère cipher** example you had earlier), you’d need to tweak the code in these ways:

- **Encryption**:  
  Loop through characters of a message and shift them forward based on a key.

- **Decryption**:  
  Use the same logic, but shift characters **backward** instead of forward.

In other words:
- Change the arithmetic sign in the loop from `+` to `-` when processing characters to switch from **encryption** to **decryption**.

👉 For this Luhn algorithm specifically, there’s no encrypt/decrypt mode — it’s purely a validation check.

---

## 🚀 How to Run

1. Save the file as `card_validator.py`.
2. Run it in a terminal:

   ```bash
   python card_validator.py
   ```

3. Modify the `card_number` inside `main()` to test other numbers.

---

## ✅ Example Test Numbers

- `4111-1111-1111-1111` → Valid  
- `1234-5678-9012-3456` → Invalid  

---

## 📚 References

- [Luhn Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Luhn_algorithm)
- Payment card validation standards
