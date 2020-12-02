num1 = input('Type value: ')
unit1 = input('Convert from:  ')
unit2 = input('to: ')

if unit1 == "cm" and unit2 == "mm":
    ans = float(num1)*10
    print(ans)
elif unit1 == "mm" and unit2 == "cm":
    ans = float(num1)/10
    print(ans)
elif unit1 == "m" and unit2 == "cm":
    ans = float(num1)*100
    print(ans)
elif unit1 == "cm" and unit2 == "m":
    ans = float(num1)/100
    print(ans)
elif unit1 == "mm" and unit2 == "m":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "m" and unit2 == "mm":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "km" and unit2 == "m":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "m" and unit2 == "km":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "mm" and unit2 == "km":
    ans = float(num1)/1000000
    print(ans)
elif unit1 == "cm" and unit2 == "km":
    ans = float(num1)/100000
    print(ans)
elif unit1 == "km" and unit2 == "cm":
    ans = float(num1)*100000
    print(ans)
elif unit1 == "ms" and unit2 == "s":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "s" and unit2 == "ms":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "s" and unit2 == "min":
    ans = float(num1)/60
    print(ans)
elif unit1 == "min" and unit2 == "s":
    ans = float(num1)*60
    print(ans)
elif unit1 == "ms" and unit2 == "min":
    ans = float(num1)/60000
    print(ans)
elif unit1 == "min" and unit2 == "ms":
    ans = float(num1)*60000
    print(ans)
elif unit1 == "min" and unit2 == "hr":
    ans = float(num1)/60
    print(ans)
elif unit1 == "hr" and unit2 == "min":
    ans = float(num1)*60
    print(ans)
elif unit1 == "s" and unit2 == "hr":
    ans = float(num1)/3600
    print(ans)
elif unit1 == "hr" and unit2 == "s":
    ans = float(num1)*3600
    print(ans)
elif unit1 == "ms" and unit2 == "hr":
    ans = float(num1)/3600000
    print(ans)
elif unit1 == "hr" and unit2 == "ms":
    ans = float(num1)*3600000
    print(ans)
elif unit1 == "m³" and unit2 == "L":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "L" and unit2 == "m³":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "L" and unit2 == "mL":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "mL" and unit2 == "L":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "m³" and unit2 == "mL":
    ans = float(num1)*1000000
    print(ans)
elif unit1 == "mL" and unit2 == "m³":
    ans = float(num1)/1000000
    print(ans)
elif unit1 == "Hz" and unit2 == "KHz":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "KHz" and unit2 == "Hz":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "Hz" and unit2 == "MHz":
    ans = float(num1)/1000000
    print(ans)
elif unit1 == "MHz" and unit2 == "Hz":
    ans = float(num1)*1000000
    print(ans)
elif unit1 == "Hz" and unit2 == "GHz":
    ans = float(num1)/1000000000
    print(ans)
elif unit1 == "GHz" and unit2 == "Hz":
    ans = float(num1)*1000000
    print(ans)
elif unit1 == "KHz" and unit2 == "MHz":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "MHz" and unit2 == "KHz":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "KHz" and unit2 == "GHz":
    ans = float(num1)/1000000
    print(ans)
elif unit1 == "GHz" and unit2 == "KHz":
    ans = float(num1)*1000000
    print(ans)
elif unit1 == "MHz" and unit2 == "GHz":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "GHz" and unit2 == "MHz":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "mg" and unit2 == "g":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "g" and unit2 == "mg":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "g" and unit2 == "Kg":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "Kg" and unit2 == "g":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "mg" and unit2 == "Kg":
    ans = float(num1)/1000000
    print(ans)
elif unit1 == "Kg" and unit2 == "mg":
    ans = float(num1)*1000000
    print(ans)
elif unit1 == "b" and unit2 == "Kb":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "Kb" and unit2 == "b":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "b" and unit2 == "Mb":
    ans = float(num1)/1000000
    print(ans)
elif unit1 == "Mb" and unit2 == "b":
    ans = float(num1)*1000000
    print(ans)
elif unit1 == "Kb" and unit2 == "Mb":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "Mb" and unit2 == "Kb":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "b" and unit2 == "Gb":
    ans = float(num1)/1000000000
    print(ans)
elif unit1 == "Gb" and unit2 == "b":
    ans = float(num1)*1000000000
    print(ans)
elif unit1 == "Kb" and unit2 == "Gb":
    ans = float(num1)/1000000
    print(ans)
elif unit1 == "Gb" and unit2 == "Kb":
    ans = float(num1)*1000000
    print(ans)
elif unit1 == "Mb" and unit2 == "Gb":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "Gb" and unit2 == "Mb":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "b" and unit2 == "Tb":
    ans = float(num1)/1000000000000
    print(ans)
elif unit1 == "Tb" and unit2 == "b":
    ans = float(num1)*1000000000000
    print(ans)
elif unit1 == "Kb" and unit2 == "Tb":
    ans = float(num1)/1000000000
    print(ans)
elif unit1 == "Tb" and unit2 == "Kb":
    ans = float(num1)*1000000000
    print(ans)
elif unit1 == "Mb" and unit2 == "Tb":
    ans = float(num1)/1000000
    print(ans)
elif unit1 == "Tb" and unit2 == "Mb":
    ans = float(num1)*1000000
    print(ans)
elif unit1 == "Gb" and unit2 == "Tb":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "Tb" and unit2 == "Gb":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "b" and unit2 == "Pb":
    ans = float(num1)/1000000000000000
    print(ans)
elif unit1 == "Pb" and unit2 == "b":
    ans = float(num1)*1000000000000000
    print(ans)
elif unit1 == "Kb" and unit2 == "Pb":
    ans = float(num1)/1000000000000
    print(ans)
elif unit1 == "Pb" and unit2 == "Kb":
    ans = float(num1)*1000000000000
    print(ans)
elif unit1 == "Mb" and unit2 == "Pb":
    ans = float(num1)/1000000000
    print(ans)
elif unit1 == "Pb" and unit2 == "Mb":
    ans = float(num1)*1000000000
    print(ans)
elif unit1 == "Gb" and unit2 == "Pb":
    ans = float(num1)/1000000
    print(ans)
elif unit1 == "Pb" and unit2 == "Gb":
    ans = float(num1)*1000000
    print(ans)
elif unit1 == "Tb" and unit2 == "Pb":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "Pb" and unit2 == "Tb":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "b" and unit2 == "B":
    ans = float(num1)/8
    print(ans)
elif unit1 == "B" and unit2 == "b":
    ans = float(num1)*8
    print(ans)
elif unit1 == "B" and unit2 == "KB":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "KB" and unit2 == "B":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "B" and unit2 == "MB":
    ans = float(num1)/1000000
    print(ans)
elif unit1 == "MB" and unit2 == "B":
    ans = float(num1)*1000000
    print(ans)
elif unit1 == "KB" and unit2 == "MB":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "MB" and unit2 == "KB":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "B" and unit2 == "GB":
    ans = float(num1)/1000000000
    print(ans)
elif unit1 == "GB" and unit2 == "B":
    ans = float(num1)*1000000000
    print(ans)
elif unit1 == "KB" and unit2 == "GB":
    ans = float(num1)/1000000
    print(ans)
elif unit1 == "GB" and unit2 == "KB":
    ans = float(num1)*1000000
    print(ans)
elif unit1 == "MB" and unit2 == "GB":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "GB" and unit2 == "MB":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "B" and unit2 == "TB":
    ans = float(num1)/1000000000000
    print(ans)
elif unit1 == "TB" and unit2 == "B":
    ans = float(num1)*1000000000000
    print(ans)
elif unit1 == "KB" and unit2 == "TB":
    ans = float(num1)/1000000000
    print(ans)
elif unit1 == "Tb" and unit2 == "Kb":
    ans = float(num1)*1000000000
    print(ans)
elif unit1 == "MB" and unit2 == "TB":
    ans = float(num1)/1000000
    print(ans)
elif unit1 == "TB" and unit2 == "MB":
    ans = float(num1)*1000000
    print(ans)
elif unit1 == "GB" and unit2 == "TB":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "TB" and unit2 == "GB":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "B" and unit2 == "PB":
    ans = float(num1)/1000000000000000
    print(ans)
elif unit1 == "PB" and unit2 == "B":
    ans = float(num1)*1000000000000000
    print(ans)
elif unit1 == "KB" and unit2 == "PB":
    ans = float(num1)/1000000000000
    print(ans)
elif unit1 == "PB" and unit2 == "KB":
    ans = float(num1)*1000000000000
    print(ans)
elif unit1 == "MB" and unit2 == "PB":
    ans = float(num1)/1000000000
    print(ans)
elif unit1 == "PB" and unit2 == "MB":
    ans = float(num1)*1000000000
    print(ans)
elif unit1 == "GB" and unit2 == "PB":
    ans = float(num1)/1000000
    print(ans)
elif unit1 == "PB" and unit2 == "GB":
    ans = float(num1)*1000000
    print(ans)
elif unit1 == "TB" and unit2 == "PB":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "PB" and unit2 == "TB":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "Atm" and unit2 == "Bar":
    ans = float(num1)*1.013
    print(ans)
elif unit1 == "Bar" and unit2 == "Atm":
    ans = float(num1)/1.013
    print(ans)
elif unit1 == "Atm" and unit2 == "Pascal":
    ans = float(num1)*101325
    print(ans)
elif unit1 == "Pascal" and unit2 == "Atm":
    ans = float(num1)/101325
    print(ans)
elif unit1 == "Bar" and unit2 == "Pascal":
    ans = float(num1)*100000
    print(ans)
elif unit1 == "Pascal" and unit2 == "Bar":
    ans = float(num1)/100000
    print(ans)
elif unit1 == "C" and unit2 == "F":
    ans = float(num1)*9/5+32
    print(ans)
elif unit1 == "F" and unit2 == "C":
    ans = float(num1)*5/9-(32*5/9)
    print(ans)
elif unit1 == "C" and unit2 == "Kelivn":
    ans = float(num1)+273.15
    print(ans)
elif unit1 == "Kelvin" and unit2 == "C":
    ans = float(num1)-273.15
    print(ans)
elif unit1 == "F" and unit2 == "Kelvin":
    ans = float(num1)*5/9-(32*5/9)+273.15
    print(ans)
elif unit1 == "Kelvin" and unit2 == "F":
    ans = float(num1)*9/5-273.15*9/5+32
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
elif unit1 == "" and unit2 == "":
    ans = float(num1)
    print(ans)
 
