"""
1. Maxsus isalpha funktsiyasi:
- “my_isalpha” funksiyasini bajaring, u satrni kiritish sifatida qabul qiladi va agar satrdagi barcha
  belgilar alifbo tartibida bo‘lsa, “True” qiymatini qaytaradi, aks holda “False” qiymatini qaytaradi.
- Alfavit va alifbo bo'lmagan belgilarni o'z ichiga olgan turli qatorlar bilan funksiyangizni sinab ko'ring.
"""
# def my_isalpha(satr):
#     for belgi in satr:
#         if not ('A' <= belgi <= 'Z' or 'a' <= belgi <= 'z'):
#             return False
#     return True

# print(my_isalpha("hello"))
# print(my_isalpha("Pyth0n"))
# print(my_isalpha("dasturlash Judayam osson ekan"))
# print(my_isalpha("12345"))
"""
2. Maxsus pastki funksiya:
- “my_lower” deb nomlangan funktsiyani yozing, u qatorni kiritish sifatida qabul qiladi va barcha alifbo
  belgilari kichik harfga aylantirilgan holda yangi qatorni qaytaradi.
- Funksiyangizni katta va kichik harflardan iborat satrlar bilan sinab ko'ring.
"""
# def my_lower(satr):
#     yangi_satr = ""
#     for belgi in satr:
#         if 'A' <= belgi <= 'Z':
#             yangi_satr += chr(ord(belgi) + 32)
#         else:
#             yangi_satr += belgi
#     return yangi_satr
#
# print(my_lower("PYTHON"))
# print(my_lower("C++"))
# print(my_lower("dasturlash Judayam qiyin ekan"))
# print(my_lower("Hello World!"))

"""
3. Maxsus yuqori funksiya:
- “my_upper” nomli funktsiyani amalga oshiring, u qatorni kirish sifatida qabul qiladi va barcha alifbo
  belgilari bosh harfga aylantirilgan holda yangi qatorni qaytaradi.
- Katta va kichik harflarni o'z ichiga olgan satrlar bilan sinab ko'rish orqali funktsiyangizning
  to'g'riligini tekshiring.
"""
# def my_upper(satr):
#     yangi_satr = ""
#     for belgi in satr:
#         if 'a' <= belgi <= 'z':
#             yangi_satr += chr(ord(belgi) - 32)
#         else:
#             yangi_satr += belgi
#     return yangi_satr
#
# print(my_upper("salom"))
# print(my_upper("Python"))
# print(my_upper("12345"))
# print(my_upper("dasturlash"))
# print(my_upper("Hello World!"))
"""
4. Maxsus sarlavha ishi funksiyasi:
- Berilgan satrdagi har bir so‘zning birinchi harfini bosh harf bilan yozadigan, qolgan barcha harflarni
  kichik harflarga o‘zgartiradigan “mening_sarlavham” funksiyasini yarating.
- Funktsiyangizni bir nechta so'zlarni va turli xil bosh harflarni o'z ichiga olgan satrlar bilan sinab ko'ring.
"""
# def mening_sarlavham(satr):
#     sarlavha = ""
#     bosh_harf = True
#     for harf in satr:
#         if harf.isspace():
#             sarlavha += harf
#             bosh_harf = True
#         else:
#             if bosh_harf:
#                 sarlavha += harf.upper()
#                 bosh_harf = False
#             else:
#                 sarlavha += harf.lower()

#     return sarlavha

# print(mening_sarlavham("xush kelibsiz DASTURlash OlaMiga!"))
# print(mening_sarlavham("uSToz shU vAzIfaLARni aVVAlroq BAJarsaM bo'LAR ekAn"))

"""
5. Maxsus chiziq funksiyasi:
- Berilgan satrdan bosh va keyingi boʻshliq belgilarni (boʻshliqlar, yorliqlar, yangi satrlar) olib tashlaydigan
  “mening_strip” funksiyasini yozing.
- Turli pozitsiyalarda bo'sh joyni o'z ichiga olgan satrlar bilan funksiyangizning funksionalligini tekshiring.
"""

"""
6. Maxsus almashtirish funksiyasi:
- “mening_almashtirish” funksiyasini amalga oshiring, u uchta parametrni oladi: qator, izlash uchun pastki qator
  va almashtirish qatori.
- Funktsiya berilgan satrdagi pastki satrning barcha takrorlanishini almashtirish satri bilan almashtirishi kerak.
- Funktsiyangizni turli qatorlar va almashtirish naqshlari bilan sinab ko'ring.
"""
# def my_replace(word):
#     return word.replace('python', 'osson')

# words = 'salom dasturlash osson'
# modified_words = my_replace(words)

# print(modified_words)
