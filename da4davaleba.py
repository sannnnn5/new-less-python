
# დიაპაზონის მითითება start,finish,step.
 #full_name="sandro goguadze"
# print(full_name[0:9:3])
# უკუ მიმართულებით ამოთვლა
# print(full_name[-1,-5,-2])  

#  ჩანაცვლება ასოსი ან სიმბოლოსი
# full_name="sandro goguadze"
# print(full_name.replace("o","#"))


# სტრიქონში შემოწმება გამოაქვს true or false
# full_name="sandro goguadze"
# print("s" in full_name)
# #ან
# print("s" not in full_name)



# სტრინგის გაზომვა რამდენი ერთეულია
# name= "sandro"
# print(len(name))

# my_sentency= """გრძელი სტრინგის შექმნა,როდესაც არ ეტევა 1 ხაზში ვამატებთ 3 ბრჭყალს 1 ის ნაცვლად"""


#სფეისების მოჭრა
# name2="   sandro   "
# print(name2.strip())

# ლოგიკური მნიშვნელობა 
# if 10<5:
#     print("hello")
# else:
#     print("goodbay")    

#my_name="sandro"
#if "s" in my_name:
# print("sheicavs s")
# else:
#     print("ar sheicavs")

#format ფუნქცია ...თანმიმდევრობა შეგვიძლია შევუცვალოთ ფიგურული ფრჩხილებიდან {0},{1},{2}.
# my_name="sandro"
# my_lastname="goguadze"
# my_age="32"
# my_sentency="name: {0} famele: {1} age: {2}".format( my_name, my_lastname, my_age)
# print(my_sentency)

# input მეთოდი -ით შემოტანილი ინფორმაცია ყოველთვის მიეკუთნება სტრინგს(წინადადებას)
# გასაციფრებლად წინ ეწერება int. მაგალითად my_name=int(input("chawere sheni saxeli: "))

# my_name=input("chawere sheni saxeli: ")
# my_lastname=input("chawere gvari")
# my_age=input("chawere asaki")
# print("chemi saxelia " + my_name)


# პატარა დავალება
# my_name="sandro"
# my_age=32
# my_info="gavida 3 weli da chemi asakia"
# my_age+=3
# my_sentency="name {} my ifno {} my age {} ".format(my_name , my_info , my_age)
# print(my_sentency)

# პატარა სავარჯიშო
# my_name=input("chawere sheni saxeli: ")
# my_lastname=input("chawere gvari: ")
# my_age=input("chawere asaki: ")
# my_sentency="name: {}. lastname: {}. age: {} ".format(my_name , my_lastname , my_age )
# print(my_sentency )
 



# სავარჯიშო
# my_age=int(input("enter age: "))
# my_name=input("enter your name: ")
# my_info="gavida 3 weli"
# print ("asaki: {}. saxeli: {}. info {}. " .format (my_age,my_name,my_info))

# year=int(input("enter year: "))
# new_age=(my_age)+(year)
# print("after {} year,now your age is {} year old".format(year,new_age))

 
# name="sandro  "
# name2="goguadze"
# name3=(name)+(name2)
# print(name3)

# დავალება
# num1=int(input("num: "))
# num2=int(input("num: "))
# num3=(num1)*(num2)
# if num3>100:
#     print(num3)
# else:
#     "youlose"    

# არასწორი ფორმულა
# num2=int(input("num: "))
# num3=int(input("num: "))
# product1=(num1)%2
# product2=(num2)%2
# product3=(num3)%2




# num1=int(input("num: "))
# product1=(num1)//2 %6
# if product1 :
#       print (product1 +1 )



# num1=int(input("num: "))
# product1=(num1)//2 
# num2=int(input("num: "))
# product2=(num2)//2
# num3=int(input("num: "))
# product3=(num3)//2

# if product1 % 6:
#     print (product1 +10 )


# სწორი მაგალითი
# num = int(input("Enter a number: "))
# if (num % 2) == 1:

#   num2 = int(input("Enter a number: "))
# if (num2 % 2) == 1:      
  

#    print((num)+(num2))
# else:
#    print("{0} is Odd".format(num))


num1=int(input("enter number: "))
if (num1 % 2) == 1:
 num2=int(input("enter number: "))
if (num2 % 2) == 1:
 num3=int(input("enter number: "))
if (num3 % 2) == 1:
      print((num1)+(num2)+(num3))
else :
      print("no")     

