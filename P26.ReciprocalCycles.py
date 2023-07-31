def recurring_decimal(divisor):
    if divisor < 10:
        divident = 10
    elif 10 <= divisor < 100:
        divident = 100
    elif divisor < 1000:
        divident = 1000
    else:
        return 'divisor should be less than 10.'
    value_to_check = divident
    recurring_seg = ''
    for i in range(divisor):
        recurring_seg += str(divident // divisor)
        divident = divident % divisor
        if divident < divisor:
            divident = divident * 10
            if divident < divisor:
                divident = divident * 10
                recurring_seg += '0'
                if divident < divisor:
                    divident = divident * 10
                    recurring_seg += '0'
        if divident == value_to_check:
            return recurring_seg


print(recurring_decimal(7))
print(1 / 7)
