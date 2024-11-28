import base64

def decrypt(encoded_data):
    """
    تفك تشفير النص المشفر باستخدام Base64
    """
    try:
        return base64.b64decode(encoded_data).decode('utf-8')
    except Exception as e:
        return f"خطأ أثناء فك التشفير: {e}"
