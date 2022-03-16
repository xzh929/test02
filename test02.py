place = ['chengdu', 'beijing', 'xianggang', 'shanghai', 'shenzhen']
for i in place:
    print(i)
print(sorted(place))
print(place)
print(sorted(place,reverse=True))
print(place)
place.reverse()
print(place)
place.reverse()
print(place)
place.sort()
print(place)
place.sort(reverse=True)
print(place)

language = ['Chinese', 'English', 'French', 'German', 'Japanese']
for i in language:
    print(i)
language_pop = language.pop(2)#删除项
print(language_pop)
print(language)