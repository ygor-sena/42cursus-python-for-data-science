def first_python_script():
	ft_list = ["Hello", "tata!"]
	ft_tuple = ("Hello", "toto!")
	ft_set = {"Hello", "tutu!"}
	ft_dict = {"Hello" : "titi!"}

	# Change list value
	ft_list[1] = "World!"

	# Change tuple value
	tmp = list(ft_tuple)
	tmp[1] = "Brazil!"
	ft_tuple = tuple(tmp)

	# Change set value
	ft_set.remove("tutu!")
	ft_set.update(["São Paulo!"])
	# Or use union to concatenate two sets:
	# ft_set |= {"São Paulo!"}

	# Change dict value
	ft_dict["Hello"] = "42SãoPaulo!"

	print(ft_list)
	print(ft_tuple)
	print(ft_set)
	print(ft_dict)

if __name__ == '__main__':
	first_python_script()