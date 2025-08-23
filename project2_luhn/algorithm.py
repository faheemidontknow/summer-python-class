def verify_card_number(card_number):
    # Initialize a variable to hold the sum of digits in odd positions (from the right)
    sum_of_odd_digits = 0

    # Reverse the card number string (since Luhn algorithm works from right to left)
    card_number_reversed = card_number[::-1]

    # Extract every other digit starting from index 0 (i.e., the odd positions in the original number)
    odd_digits = card_number_reversed[::2]

    # Loop through each odd-positioned digit
    for digit in odd_digits:
        # Convert the digit from string to integer and add it to the odd digits sum
        sum_of_odd_digits += int(digit)

    # Initialize a variable to hold the sum of digits in even positions (from the right)
    sum_of_even_digits = 0

    # Extract every other digit starting from index 1 (i.e., the even positions in the original number)
    even_digits = card_number_reversed[1::2]

    # Loop through each even-positioned digit
    for digit in even_digits:
        # Double the digit (as per Luhn algorithm)
        number = int(digit) * 2

        # If the doubled value is two digits (10 or more), split and sum them
        # Example: 12 → 1 + 2 = 3
        if number >= 10:
            number = (number // 10) + (number % 10)

        # Add the processed number to the even digits sum
        sum_of_even_digits += number

    # Calculate the total checksum by adding both odd and even digit sums
    total = sum_of_odd_digits + sum_of_even_digits

    # Print the total (for debugging or verification purposes)
    print(total)

    # A valid card number will make the total divisible by 10 (Luhn algorithm rule)
    return total % 10 == 0


def main():
    # Example card number (with dashes, like real card formatting)
    card_number = '4111-1111-4555-1141'

    # Create a translation table to remove dashes (-) and spaces ( )
    card_translation = str.maketrans({'-': '', ' ': ''})

    # Apply the translation to get only the digits of the card number
    translated_card_number = card_number.translate(card_translation)

    # Call the verifier function to check if the card number is valid
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')


# Run the program
main()
