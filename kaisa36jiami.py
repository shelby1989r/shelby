def custom_key_encrypt(text, key):
    original_alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"

    encrypted_text = ""
    for char in text:
        if char in original_alphabet:
            index = original_alphabet.index(char)
            encrypted_text += key[index]
        else:
            encrypted_text += char

    return encrypted_text


# 输入要加密的文本
plaintext = input("请输入要加密的文本：")
custom_key = input("请输入自定义的密钥：")

encrypted_text = custom_key_encrypt(plaintext, custom_key)
print("加密后的文本：", encrypted_text)

