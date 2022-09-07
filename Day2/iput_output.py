a=input("hey give me something ")
b=input("mujhe b kuch input dena ")

print(f"ye a ka output {a} aur b ka output {b}")
print(f"input to le liya but uska type dekhoge chalo dekhte hai")
print(f"a ka type hai {type(a)} aur b ka type hai {type(b)} ")
# sahi pehchan gaye wo input se  input loge to string hi lega to use eval()

c =eval(input("ab mujhe input do :"))
d =eval(input("mujhe b kuch dedo : "))

print(f"ab dekho c ka type : {type(c)} and d ka {type(d)}")
print("aur eval me jab string pass kroge to '' double quote lena")