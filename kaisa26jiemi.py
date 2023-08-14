def caesar_custom_key_decrypt(encrypted_text, key):
    key_mapping = {key[i].upper(): chr(65 + i) for i in range(26)}
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            is_upper = char.isupper()
            decrypted_char = key_mapping[char.upper()]
            decrypted_text += decrypted_char if is_upper else decrypted_char.lower()
        else:
            decrypted_text += char
    return decrypted_text

# 输入要解密的加密文本和之前使用的自定义的密钥
encrypted_text = input("请输入要解密的文本：")
custom_key = input("请输入自定义的密钥：")

decrypted_text = caesar_custom_key_decrypt(encrypted_text, custom_key)
print("解密后的文本：", decrypted_text)
