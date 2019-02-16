number_name = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',
               10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',
               16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
               20:'twenty', 30:'thirty', 40:'forty', 50:'fifty',
               60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}

numbers_list = []
for i in range(1001):
    numbers_list.append(number_name.get(i))
    if number_name.get(i) is None and i < 100:
        numbers_list[i] = numbers_list[i - i % 10] + ' ' + numbers_list[i % 10]
    if number_name.get(i) is None and i >= 100:
        if i % 100 == 0:
            numbers_list[i] = numbers_list[i//100] + ' hundred'
        else:
            numbers_list[i] = numbers_list[i//100] + ' hundred and ' + numbers_list[i % 100]
    if number_name.get(i) is None and i >= 1000:
        if i % 1000 == 0:
            numbers_list[i] = numbers_list[i//1000] + ' thousand'
        else:
            numbers_list[i] = numbers_list[i//1000] + ' thousand ' + numbers_list[i % 1000]

sum_of_letters = 0
for number in numbers_list[1:]:
    sum_of_letters += len(number) - number.count(' ')
print(sum_of_letters)
