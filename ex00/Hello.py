# python_piscine/ex00/Hello.py

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"
ft_tuple = ("Hello", "UAE!")
ft_set.remove("tutu!")
ft_set.add("Abu Dhabi!")
ft_dict["Hello"] = "42AbuDhabi!"

print(ft_list)    # ['Hello', 'World!']
print(ft_tuple)   # ('Hello', 'UAE!')
print(ft_set)     # {'Hello', 'Abu Dhabi!'}
print(ft_dict)    # {'Hello': '42AbuDhabi!'}