def caesar_custom_key_encrypt(text, key):
    key_mapping = {chr(65 + i): key[i].upper() for i in range(26)}
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            encrypted_char = key_mapping[char.upper()]
            encrypted_text += encrypted_char if is_upper else encrypted_char.lower()
        else:
            encrypted_text += char
    return encrypted_text

# 输入要加密的文本和自定义的密钥（26个字母的排列）
plaintext = input("请输入要加密的文本：")
custom_key = input("请输入自定义的密钥：")

encrypted_text = caesar_custom_key_encrypt(plaintext, custom_key)
print("加密后的文本：", encrypted_text)
