# --------------------------------------------------------------
# বাংলায় ব্যাখ্যা (Explanation in Bengali)
# --------------------------------------------------------------
# এই প্রোজেক্টে আমরা ব্যবহারকারীর কাছ থেকে ইনপুট নেব input() ফাংশনের মাধ্যমে।
# আমরা ডাটা সংরক্ষণ করব Python List-এর মধ্যে, যেখানে প্রতিটি ছাত্র হবে একটি Dictionary।
# Loop (while/for) ব্যবহার করে বারবার কাজ করতে পারব, এবং Conditional Logic (if-elif-else)
# ব্যবহার করে বিভিন্ন অপশন নির্বাচন করব।
# --------------------------------------------------------------

# শিক্ষার্থীদের তথ্য রাখার জন্য একটি খালি লিস্ট
students = []


def show_menu():
    print("\n===== শিক্ষার্থী তথ্য ব্যবস্থাপনা =====")
    print("1. নতুন ছাত্র/ছাত্রী যোগ করুন")
    print("2. সকল ছাত্র/ছাত্রীর তালিকা দেখুন")
    print("3. নাম অনুসারে খুঁজুন")
    print("4. ছাত্র/ছাত্রীর তথ্য হালনাগাদ করুন")
    print("5. ছাত্র/ছাত্রী মুছুন")
    print("6. প্রোগ্রাম বন্ধ করুন")


def add_student():
    print("\n--- নতুন ছাত্র/ছাত্রী যোগ করুন ---")
    name = input("নাম: ")
    age = input("বয়স: ")
    grade = input("গ্রেড (যেমন A+, B): ")

    # একটি ডিকশনারি তৈরি করা হচ্ছে
    student = {
        "name": name,
        "age": age,
        "grade": grade
    }
    # লিস্টে ডিকশনারিটি যোগ করা হচ্ছে
    students.append(student)
    print(f"{name} সফলভাবে যোগ করা হয়েছে!")


def view_all():
    print("\n--- সকল ছাত্র/ছাত্রীর তালিকা ---")
    if not students:  # কন্ডিশনাল লজিক: লিস্ট খালি কিনা পরীক্ষা করা
        print("কোনো ছাত্র/ছাত্রী নেই।")
    else:
        # লুপ ব্যবহার করে প্রতিটি ছাত্রের তথ্য দেখানো
        for idx, student in enumerate(students, start=1):
            print(f"{idx}. নাম: {student['name']}, বয়স: {student['age']}, গ্রেড: {student['grade']}")


def search_student():
    print("\n--- নাম অনুসারে খুঁজুন ---")
    search_name = input("যে নাম খুঁজতে চান: ")
    found = False
    for student in students:
        if student['name'].lower() == search_name.lower():  # কন্ডিশনাল লজিক
            print(f"পাওয়া গেছে: নাম: {student['name']}, বয়স: {student['age']}, গ্রেড: {student['grade']}")
            found = True
            break
    if not found:
        print("এই নামের কোনো ছাত্র/ছাত্রী পাওয়া যায়নি।")


def update_student():
    print("\n--- ছাত্র/ছাত্রীর তথ্য হালনাগাদ করুন ---")
    search_name = input("যার তথ্য পরিবর্তন করবেন তার নাম: ")
    for student in students:
        if student['name'].lower() == search_name.lower():
            print("বর্তমান তথ্য:", student)
            new_name = input("নতুন নাম (এন্টার করলে অপরিবর্তিত): ")
            new_age = input("নতুন বয়স (এন্টার করলে অপরিবর্তিত): ")
            new_grade = input("নতুন গ্রেড (এন্টার করলে অপরিবর্তিত): ")

            # কন্ডিশনাল লজিক: যদি ব্যবহারকারী কিছু টাইপ করে তবে সেটা পরিবর্তন করবে
            if new_name:
                student['name'] = new_name
            if new_age:
                student['age'] = new_age
            if new_grade:
                student['grade'] = new_grade
            print("তথ্য হালনাগাদ করা হয়েছে!")
            return
    print("এই নামের কোনো ছাত্র/ছাত্রী পাওয়া যায়নি।")


def delete_student():
    print("\n--- ছাত্র/ছাত্রী মুছুন ---")
    search_name = input("যাকে মুছবেন তার নাম: ")
    for student in students:
        if student['name'].lower() == search_name.lower():
            students.remove(student)
            print(f"{search_name} কে মুছে ফেলা হয়েছে।")
            return
    print("এই নামের কোনো ছাত্র/ছাত্রী পাওয়া যায়নি।")


# মেইন প্রোগ্রাম লুপ
while True:
    show_menu()
    choice = input("আপনার পছন্দের নম্বর দিন: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_all()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("প্রোগ্রাম বন্ধ হচ্ছে। ধন্যবাদ!")
        break
    else:
        print("ভুল ইনপুট! দয়া করে ১ থেকে ৬ এর মধ্যে একটি নম্বর দিন।")