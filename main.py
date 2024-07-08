import os
from customtkinter import *
import shutil

# إنشاء النافذة الرئيسية
app = CTk()
app.geometry("800x600")
app.title("منظم الملفات")

# إنشاء حقل إدخالي لأخذ المسار
path_entry = CTkEntry(app, font=('inter--semibold', 30), width=400)
path_entry.place(relx=0.5, rely=0.47, anchor=CENTER)

# إضافة رسالة للمستخدم
message_label = CTkLabel(app, text="", font=('inter--semibold', 20))
message_label.place(relx=0.5, rely=0.8, anchor=CENTER)  # تعديل الموضع لجعل الرسالة مرئية بوضوح

# تعريف دالة التنظيم
def organize():
    directory_path = path_entry.get()
    if os.path.exists(directory_path):
        files = os.listdir(directory_path)
        if files:  # التأكد من وجود ملفات في المجلد
            for file in files:
                name, extension = os.path.splitext(file)
                extension = extension[1:]  # إزالة النقطة من الامتداد
                if extension:  # تجاهل الملفات بدون امتداد
                    if not os.path.exists(os.path.join(directory_path, extension)):
                        os.makedirs(os.path.join(directory_path, extension))
                    shutil.move(os.path.join(directory_path, file), os.path.join(directory_path, extension, file))
            message_label.configure(text="تم تنظيم الملفات بنجاح.", text_color="green")
        else:
            message_label.configure(text="المجلد فارغ، لا توجد ملفات لتنظيمها.", text_color="orange")
    else:
        message_label.configure(text="المسار غير موجود.", text_color="red")

# إضافة عنوان التطبيق
CTkLabel(
    app,
    text="منظم الملفات",
    font=('inter--semibold', 30)
).place(relx=0.5, rely=0.2, anchor=CENTER)

# إضافة نص توضيحي
CTkLabel(
    app,
    text="ادخل مسار المجلد الذي ترغب بتنظيم ملفاته",
    font=('inter--semibold', 20)
).place(relx=0.5, rely=0.35, anchor=CENTER)

# إضافة زر التنظيم
organizeButton = CTkButton(
    app,
    text="تنظيم",
    font=('inter--semibold', 30),
    width=200,
    height=40,
    command=organize,
)
organizeButton.place(relx=0.5, rely=0.6, anchor=CENTER)

# منع تغيير حجم النافذة
app.resizable(True, True)

# تشغيل الحلقة الرئيسية للواجهة
app.mainloop()
