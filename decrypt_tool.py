import base64
import lzma
import pickle
import hmac
import hashlib

def فك_التشفير(البيانات_المشفرة, التوقيع, المفتاح):
    """
    فك التشفير عن الكود المشفر باستخدام HMAC وLZMA وpickle.
    البيانات_المشفرة: البيانات المشفرة (Base64).
    التوقيع: HMAC للتأكد من صحة البيانات.
    المفتاح: مفتاح HMAC المستخدم لتوقيع البيانات.
    """
    try:
        # فك تشفير Base64
        compressed_data = base64.b64decode(البيانات_المشفرة)

        # التحقق من صحة البيانات باستخدام HMAC
        if not hmac.compare_digest(التوقيع, hmac.new(المفتاح, compressed_data, hashlib.sha256).hexdigest()):
            raise ValueError("توقيع HMAC غير صالح. تم تعديل البيانات.")

        # فك الضغط باستخدام LZMA
        decompressed_data = lzma.decompress(compressed_data)

        # تحميل الكود باستخدام pickle
        code = pickle.loads(decompressed_data)

        # تنفيذ الكود
        exec(compile(code, filename="<string>", mode="exec"))

    except Exception as e:
        print(f"خطأ أثناء فك التشفير: {e}")
