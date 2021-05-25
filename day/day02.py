id1 = '01'
idName1 = "羽绒服"
brand1 = "A"
price1 = 100
discount1 = 7
story1 = 120
size1 = "均码"

id2 = '02'
idName2 = "T恤衫"
brand2 = "B"
price2 = 110
discount2 = 8
story2 = 110
size2 = "均码"

id3 = '03'
idName3 = "风衣"
brand3 = "C"
price3 = 120
discount3 = 7
story3 = 120
size3 = "均码"

id4 = '04'
idName4 = "卫衣"
brand4 = "D"
price4 = 130
discount4 = 8
story4 = 110
size4 = "均码"

id5 = '05'
idName5 = "牛仔"
brand5 = "E"
price5 = 140
discount5 = 7
story5 = 110
size5 = "均码"

id6 = '06'
idName6 = "夹克"
brand6 = "F"
price6 = 150
discount6 = 8
story6 = 120
size6 = "均码"

print("===========================服装商店============================")
print("编号      名称      品牌      价格      折扣      库存      大小")
print("----------------------------------------------------------------")
print(id1, "     ", idName1, "  ", brand1, "     ", price1, "      ", discount1, "    ", story1, "     ", size1)
print(id2, "     ", idName2, "   ", brand2, "     ", price2, "      ", discount2, "    ", story2, "     ", size2)
print(id3, "     ", idName3, "    ", brand3, "     ", price3, "      ", discount3, "    ", story3, "     ", size3)
print(id4, "     ", idName4, "    ", brand4, "     ", price4, "      ", discount4, "    ", story4, "     ", size4)
print(id5, "     ", idName5, "    ", brand5, "     ", price5, "      ", discount5, "    ", story5, "     ", size5)
print(id6, "     ", idName6, "    ", brand6, "     ", price6, "      ", discount6, "    ", story6, "     ", size6)
print("----------------------------------------------------------------")
print("总金额￥ ", price1*discount1*0.1*story1+price2*discount2*0.1*story2+price3*discount3*0.1*story3+price4*discount4*0.1*story4+price5*discount5*0.1*story5+price6*discount6*0.1*story6)
