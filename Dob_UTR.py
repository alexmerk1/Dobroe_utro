privet = "Доброе утро, Дима!" 

Vopros1 = input("Вы - Дмитрий? (Ответ: Да/Нет) ")

Otvet1 = "Да"
Otvet0 = "Нет"
Otvet2 = "Это прекрасно!"

if Vopros1 == Otvet1:
  print(privet)
  Vopros2 = input("У тебя получилось выспаться? (Ответ: Да/Нет) ")
  
  if Vopros2 == Otvet1:
    print(Otvet2)
    print("Ты лучший! Хорошего дня тебе! ")
    Vopros3 = input("Ты уже покушал? (Ответ: Да/Нет) ")
    
    if Vopros3 == Otvet1:
      print(" Молодец, продуктивного дня! ")

    else:
      print(" Сходи обязательно, покушай! Не откладывай ")
      
  else:
    print("Мне тебя очень жаль. Поспи днём! ")
    
else:
  print("Это плохо! Пока!")

print("     P.s. Tvoi bro")
