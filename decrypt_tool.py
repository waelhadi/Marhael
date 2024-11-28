import marshal

def فك_التشفير(البيانات_المشفرة):
    while isinstance(البيانات_المشفرة, bytes):
        البيانات_المشفرة = marshal.loads(البيانات_المشفرة)
    return البيانات_المشفرة

if __name__ == "__main__":
    try:
        # يتم تنفيذ الكود المشفر مباشرة إذا تم استدعاء الملف
        from sys import argv
        if len(argv) > 1:
            البيانات_المشفرة = eval(argv[1])  # يتم تمرير البيانات كأول وسيط
            الكود_الأصلي = فك_التشفير(البيانات_المشفرة)
            exec(الكود_الأصلي)
        else:
            print("لم يتم تمرير أي بيانات مشفرة.")
    except Exception as e:
        print(f"خطأ أثناء فك التشفير: {str(e)}")
