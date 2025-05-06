def caesar_cipher(p_value, k_value, m_value):
    encrypted = ""
    for char in p_value:
        if char.isupper():
            # Calculate shifted position for uppercase letters
            shifted = (m_value *(ord(char) - ord('A')) + k_value) % 26
            encrypted = encrypted + chr(shifted + ord('A'))
        elif char.islower():
            shifted = (m_value *(ord(char) - ord('a')) + k_value) % 26
            encrypted = encrypted + chr(shifted + ord('a'))
        else:
            encrypted = encrypted + char

    return encrypted


# shifted = (ord(char) - ord(p_value) + k_value) % 26 instead right?

if __name__ == "__main__":
    p_value = input("Write your message for encryption")
    k_value = int(input("Write your constant"))
    m_value = int(input("Write a number for the given letters (No multiples of 2 or 13"))
    result = caesar_cipher(p_value, k_value, m_value)
    print(result)
