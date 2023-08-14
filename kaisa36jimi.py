def custom_key_decrypt(encrypted_text, key):
    original_alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"

    decrypted_text = ""
    for char in encrypted_text:
        if char in key:
            index = key.index(char)
            decrypted_text += original_alphabet[index]
        else:
            decrypted_text += char

    return decrypted_text

# 输入要解密的文本
encrypted_text = input("请输入要解密的文本：")
custom_key = input("请输入自定义的密钥：")

decrypted_text = custom_key_decrypt(encrypted_text, custom_key)
print("解密后的文本：", decrypted_text)
