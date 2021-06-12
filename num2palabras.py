def num2palabras(num):
    strNum = str(num)
    group1 = group1 = ['', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciseis', 'diecisiete', 'dieciocho', 'diecinueve', 'veinte', 'veintiuno', 'veintidos', 'veintitres', 'veinticuatro', 'veinticinco', 'veintiseis', 'veintisiete', 'veintiocho', 'veintinueve' ]
    group2 = ['', '', '', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']
    # print([int(strNum[1:])])

    if num == 0:
        return 'cero'
    elif num <= 29:
        return group1[num]
    elif len(strNum) == 2 and strNum[1] == '0':
        return group2[int(strNum[0])]
    elif len(strNum) == 2 and strNum[1] != '0':
        return group2[int(strNum[0])] + ' y ' + group1[int(strNum[1])]
    elif len(strNum) == 3:
        if strNum[0] == '1' and strNum[1] == '0' and strNum[2] == '0':
            return 'cien'
        elif int(strNum[1:]) <= 29:
            return group1[int(strNum[0])] + 'cientos' + group1[int(strNum[1:])]
        elif int(strNum[1:]) > 29 and strNum[-1] == '0':
            return group1[int(strNum[0])] + 'cientos' + group2[int(strNum[1])]
        elif int(strNum[1:]) > 29 and strNum[-1] != '0':
            return group1[int(strNum[0])] + 'cientos' + group2[int(strNum[1])] + ' y ' + group1[int(strNum[2])]

    else: return 'No implementado'
print(num2palabras(999))
