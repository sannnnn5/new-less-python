
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
#     print("youlose")    





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



# სწორი ფორმულა
# num1=int(input("enter: "))
# num2=int(input("enter: "))
# num3=int(input("enter: "))

# my_sum=0

# if num1 %2==1:
#   my_sum+=num1
# if num2 %2==1:
#   my_sum+=num2
# if num3 %2==1:
#   my_sum+=num3
#   print(my_sum)    

# მაგალითი

# my_sentency=input("enter: ")
# my_sentency2=input("enter 2: ")
# sum_1=0
# sum_2=0
# for i in my_sentency:
#    if i not in "aeiou":
#      sum_1+=1

# for i in my_sentency2:
#    if i not in "aeiou":
#      sum_2+=1
# if sum_1>sum_2:
#    print("my_sentency1-shi {} tanxmovania".format(sum_1))     
# if sum_2>sum_1:
#    print("my_sentency2-shi {} tanxmovania".format(sum_2))        


# ინდექსის მოძებნა"რომელ ინდექსზეა ობიექტი'



# a="aleksandre goguadze"
# indexes=0
# for i in range(0, len(a)):
#      if a [i] in "aeiou":
        
#       print(str(indexes)+a[i])
#      indexes+=1        
     



# x=0
# for i in range(5):
#     for j in range(4):
#         for j in range(3):
#          print(str(x)+ "sandro")
#          x+=1


# დავალება
# my_list=["xinkali","mwvadi","qababi"]
# price=["2","20","10"]
# # print(my_list[0]+"_"+ price[0])
# # print(my_list[1]+"_"+price[1])
# # print(my_list[2]+"_"+price[2])
# # print("{0} fasi {1} lari".format(my_list[0],price[0]))
# # print("{0} fasi {1} lari".format(my_list[1],price[1]))
# # print("{0} fasi {1} lari".format(my_list[2],price[2]))
# print("{0}-fasi: {1} lari ,{2}-fasi: {3} lari, {4}-fasi: {5} lari,".format(my_list[0],price[0],my_list[1],price[1],my_list[2],price[2]))



# მაქსიმალური რიცხვის ამოღება
# a=[1,2,3,4,20,6,7,8,9]
# max_num=a[0]
# for score in a:
#     if score>max_num:
#         max_num=score
# print(max_num)        


#ფუნქციის შექმნა
# def shekreba(num1,num2):
#     print(num1+num2)
# მაგალითი
# shekreba(50,25)

# სორტირება
# score=[20,10,56,89,54,82,90,97,56]

# score.sort()
# print(score)

#მაქსიმალური რიცხვის ამოღება 2
# score=[20,10,56,89,54,82,90,97,56]

# max_num=score[0]

# for num in score:
#     if num>max_num:
#         max_num=num
# print(max_num)    



#ფუნქციის შექმნის მაგალით
# def good_day(name,day):
#     print(name +" "+ "gisurveb karg" +" "+ str(day)+" "+"oqtombers")
# names=["sandro","natia","saba","kato","mariami"]
# for name in names:
#     good_day(name,"7")



# მინიმალური სიგრდზის ელემენტთან მიმართება
# def pair_sum(arr1,arr2):
#     for i in range(min([len(arr1),len(arr2)])):

#      print(arr1[i]+arr2[i])


# pair_sum([4,10,35],[30,75,89,91])


# score=[20,10,56,89,54,82,90,97,56]

# max_num=score[0]

# for num in score:
#     if num>max_num:
#         max_num=num
# print(max_num)    

# score=[20,10,56,89,54,82,90,97,56]

# max_num=score[0]

# for num in score:
#     if num>max_num:
#         max_num=num
# print(max_num)    

# score=[20,10,56,89,54,82,90,97,56]

# max_num=score[0]

# for num in score:
#     if num>max_num:
#         max_num=num
# print(max_num)    


#სიის უკუმიმართულებით ამოტანა
# student=["sandro","natia","saba","kato","mariami","nono"]
# # new_arr=[]
# # student[0]="aleksandre" #ეს ჩანაცვლებას აკეთებს
# # i=len(student)
# # while i>0:
# #     new_arr.append(student[i-1])
# #     i-=1
# # print(new_arr)

# def shekreba(num1,num2):
#     print(num1*num2)

#იგივე მაგალით სხვა მეთოდით
# student=["sandro","natia","saba","kato","mariami","nono"]
# print(student[::-1])



# shekreba(95,95)    

# scores=[20,30,40,50,60,21,31,41,51,61]



# ფუნქციის შექმნა აუტომატურად დიდი რიცხვის გამოტანაზე სიიდან
# def max_num(scores):
#     max_n=scores[0]

#     for score in scores:
#         if score>max_n:
#             max_n=score
#     print(max_n)        


# max_num([20,30,40,50,60,21,31,41,51,61])


# რევერსიით ამოღება
# n=["s","a","n","d","r","o"]
# new_arr=[]
# i=len(n)
# while i>0:
#     new_arr.append(n[i-1])
#     i-=1
# print(new_arr)


# a="sandro"
# print(a[::-1])


# on="sandro"
# result=""
# for i in range(len(on)-1,-1,-1):
#     result=result+on[i]
# print(result)

# student="sandro"
# reverse=""
# i=len(student)
# while i>0:
#     reverse=student[i-1]
#     i-=1
#     print(reverse)

