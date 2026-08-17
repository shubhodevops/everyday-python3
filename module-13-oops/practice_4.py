class Student:
    # 1. Class Variable (ক্লাস ভেরিয়েবল) - সব অবজেক্টের জন্য এটি একই থাকে
    school_name = "Dhaka High School"

    def __init__(self, name, score):
        # 2. Instance Variables (ইনস্ট্যান্স ভেরিয়েবল) - প্রতিটি অবজেক্টের জন্য আলাদা হয়
        self.name = name
        self._score = score  # প্রপার্টি মেথডের জন্য ব্যবহার করা হয়েছে

    # 3. Instance Method (ইনস্ট্যান্স মেথড) - self ব্যবহার করে অবজেক্টের ডাটা নিয়ে কাজ করে
    def display_info(self):
        # Local Variable (লোকাল ভেরিয়েবল) - এটি কেবল এই মেথডের ভেতরেই কাজ করবে
        status = "Passed" if self._score >= 40 else "Failed"
        print(f"Student: {self.name}, Score: {self._score}, Status: {status}")

    # 4. Class Method (ক্লাস মেথড) - cls ব্যবহার করে ক্লাস ভেরিয়েবল পরিবর্তন বা অ্যাক্সেস করে
    @classmethod
    def change_school(cls, new_school_name):
        cls.school_name = new_school_name  # ক্লাস ভেরিয়েবল পরিবর্তন করা হচ্ছে

    # 5. Static Method (স্ট্যাটিক মেথড) - self বা cls কোনোটিই লাগে না, এটি একটি সাধারণ ফাংশনের মতো
    @staticmethod
    def is_holiday(day):
        # কোনো অবজেক্টের ডাটা ছাড়াই এটি সিদ্ধান্ত নিতে পারে
        if day.lower() == "friday":
            return True
        return False

    # 6. Property Method (প্রপার্টি মেথড) - মেথডকে ভেরিয়েবলের মতো ব্র্যাকেট () ছাড়া অ্যাক্সেস করার জন্য
    @property
    def student_score(self):
        return f"{self._score} Marks"


# --- কোডটি কীভাবে কাজ করছে তা নিচে দেখানো হলো ---

# ক. ইনস্ট্যান্স তৈরি করা এবং ইনস্ট্যান্স মেথড ব্যবহার করা
student1 = Student("Arif", 85)
student2 = Student("Nadia", 35)

student1.display_info()  # আউটপুট: Student: Arif, Score: 85, Status: Passed
student2.display_info()  # আউটপুট: Student: Nadia, Score: 35, Status: Failed

# খ. প্রপার্টি মেথড ব্যবহার করা (ব্র্যাকেট ছাড়াই ভেরিয়েবলের মতো কল করা হচ্ছে)
print(f"{student1.name}'s Score: {student1.student_score}")  # আউটপুট: Arif's Score: 85 Marks

# গ. ক্লাস ভেরিয়েবল এবং ক্লাস মেথড ব্যবহার করা
print(f"Old School Name: {Student.school_name}")  # আউটপুট: Dhaka High School

# ক্লাস মেথড কল করে স্কুলের নাম পরিবর্তন করা হলো (এটি সরাসরি ক্লাস নাম দিয়ে কল করা যায়)
Student.change_school("Chattogram Academy")
print(f"New School Name for student1: {student1.school_name}")  # আউটপুট: Chattogram Academy

# ঘ. স্ট্যাটিক মেথড ব্যবহার করা (কোনো অবজেক্ট বা ক্লাসের ডাটা ছাড়াই সরাসরি কাজ করে)
check_day = "Friday"
if Student.is_holiday(check_day):
    print(f"Yes, {check_day} is a holiday!")  # এটি প্রিন্ট হবে
