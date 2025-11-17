ves, rost = map(float, input("Ваш вес(кг) и рост(м)").split())
imt = ves/(rost*rost)
print(f"индекс массы тела:{round(imt,1)}")