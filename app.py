import json
import os

APP_TITLE = "Karvand JSON Manager"

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "karvands.json")


def load_karvands():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_karvands(karvands):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(karvands, file, ensure_ascii=False, indent=4)


def add_karvand():
    karvands = load_karvands()

    fullname = input("نام کامل: ")
    email = input("ایمیل: ")
    city = input("شهر: ")
    education = input("تحصیلات: ")
    skills_input = input("مهارت‌ها را با کاما جدا کنید: ")

    skills = [
        skill.strip()
        for skill in skills_input.split(",")
        if skill.strip()
    ]

    new_id = 1

    if karvands:
        new_id = max(
            karvand["id"]
            for karvand in karvands
        ) + 1

    karvand = {
        "id": new_id,
        "personal_info": {
            "fullname": fullname,
            "email": email,
            "city": city
        },
        "education": education,
        "skills": skills
    }

    karvands.append(karvand)
    save_karvands(karvands)

    print("کاروند با موفقیت اضافه شد.")


def show_karvands():
    karvands = load_karvands()

    if not karvands:
        print("هیچ کاروندی ثبت نشده است.")
        return

    for karvand in karvands:
        print("-" * 40)
        print(f"ID: {karvand['id']}")
        print(f"نام: {karvand['personal_info']['fullname']}")
        print(f"ایمیل: {karvand['personal_info']['email']}")
        print(f"شهر: {karvand['personal_info']['city']}")
        print(f"تحصیلات: {karvand['education']}")
        print(f"مهارت‌ها: {', '.join(karvand['skills'])}")


def find_karvand(karvand_id):
    karvands = load_karvands()

    for karvand in karvands:
        if karvand["id"] == karvand_id:
            return karvand

    return None


def edit_karvand():
    karvands = load_karvands()

    try:
        karvand_id = int(input("شناسه کاروند: "))
    except ValueError:
        print("شناسه باید عدد باشد.")
        return

    karvand = find_karvand(karvand_id)

    if karvand is None:
        print("کاروند پیدا نشد.")
        return

    print("برای تغییر هر فیلد، مقدار جدید را وارد کنید.")
    print("اگر نمی‌خواهید تغییر کند، Enter بزنید.")

    fullname = input("نام کامل: ")
    email = input("ایمیل: ")
    city = input("شهر: ")
    education = input("تحصیلات: ")
    skills_input = input("مهارت‌ها: ")

    if fullname:
        karvand["personal_info"]["fullname"] = fullname

    if email:
        karvand["personal_info"]["email"] = email

    if city:
        karvand["personal_info"]["city"] = city

    if education:
        karvand["education"] = education

    if skills_input:
        karvand["skills"] = [
            skill.strip()
            for skill in skills_input.split(",")
            if skill.strip()
        ]

    save_karvands(karvands)

    print("اطلاعات کاروند ویرایش شد.")


def delete_karvand():
    karvands = load_karvands()

    try:
        karvand_id = int(input("شناسه کاروند: "))
    except ValueError:
        print("شناسه باید عدد باشد.")
        return

    for index, karvand in enumerate(karvands):
        if karvand["id"] == karvand_id:
            karvands.pop(index)
            save_karvands(karvands)
            print("کاروند حذف شد.")
            return

    print("کاروند پیدا نشد.")


def show_report():
    karvands = load_karvands()

    print("-" * 40)
    print("گزارش کلی")
    print(f"تعداد کل کاروندها: {len(karvands)}")


def main():
    while True:
        print("\n===== Karvand Manager =====")
        print("1. افزودن کاروند")
        print("2. نمایش کاروندها")
        print("3. ویرایش کاروند")
        print("4. حذف کاروند")
        print("5. گزارش کلی")
        print("6. خروج")

        choice = input("انتخاب شما: ")

        if choice == "1":
            add_karvand()

        elif choice == "2":
            show_karvands()

        elif choice == "3":
            edit_karvand()

        elif choice == "4":
            delete_karvand()

        elif choice == "5":
            show_report()

        elif choice == "6":
            print("برنامه پایان یافت.")
            break

        else:
            print("گزینه نامعتبر است.")


if __name__ == "__main__":
    main()