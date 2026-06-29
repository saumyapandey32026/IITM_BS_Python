# x = 'pytHon sTrIng mEthOdS'
# a = x.lower()
# print(a)         
# print(x)          #❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️  strings immutable hoti hain  

# # एक स्ट्रिंग बनाई
# my_string = "hello"

# # इसमें बदलाव करने की कोशिश की
# my_string.upper() 

# # पुरानी स्ट्रिंग अभी भी वैसी ही है!
# print(my_string)  # आउटपुट: hello


# # नए वेरिएबल में स्टोर करना
# new_string = my_string.upper()
# print(new_string)  # आउटपुट: HELLO

# # या पुराने वेरिएबल को अपडेट करना (यह भी बैकग्राउंड में नया ऑब्जेक्ट ही बनाता है)
# my_string = my_string.upper()
# print(my_string)  # आउटपुट: HELLO

# print(x.capitalize())      


# x = "-----Python---"

# print(x.strip("-"))  # आउटपुट: Python
# print(x.lstrip("-"))  # आउटपुट: Python---
# print(x.rstrip("-"))  # आउटपुट: -----Python

a = "Python is a programming language"

print(a.replace("Python", "Java"))  # आउटपुट: Java is a programming language
print(a)  # आउटपुट: Python is a programming language (मूल स्ट्रिंग अपरिवर्तित रहती है)
print(a.replace("a", "A"))  # आउटपुट: Python is A progrAmming lAnguAge
print(a.replace("a", "A", 2))  # आउटपुट: Python is A progrAmming language (केवल पहले दो 'a' को बदलता है)

print(a.index("programming"))  # आउटपुट: 10 (यह 'programming' शब्द की शुरुआत का इंडेक्स देता है)
print(a.find("programming"))  # आउटपुट: 10 (यह भी 'programming' शब्द की शुरुआत का इंडेक्स देता है)
print(a.find("Java"))  # आउटपुट: -1 (क्योंकि 'Java' स्ट्रिंग में नहीं है)
print(a.index("ython"))  # आउटपुट: 1 (यह 'ython' शब्द की शुरुआत का इंडेक्स देता है)
print(a.find("n"))  






