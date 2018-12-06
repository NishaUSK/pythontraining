dict = {'name': 'ganesha', 'country': 'india', 'fav_numbers': [18, 28, 16],'fav_language': 'python'}
print(dict)
print("--------------------------------")

dict['Drew'] = 'squidly'
print(dict)
print("--------------------------------")

dict.update({'flower': 'Red'})
print(dict)
print("--------------------------------")

del dict['fav_numbers']
print(dict)
print("--------------------------------")
