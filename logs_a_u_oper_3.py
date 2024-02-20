summa_min = int(input("Минимальная сумма инвестиций - "))
Maikal = int(input("Сколько $ у Майкла - "))
Ivan = int(input("Сколько $ у Ивана - "))
if (Maikal > summa_min) and (Ivan > summa_min):
    print (2)
elif (Maikal>
      summa_min) and (Ivan<summa_min):
    print ("Maikal")
elif (Maikal<summa_min) and (Ivan>summa_min):
    print ("Ivan")
elif (Maikal<=summa_min) and (Ivan<=summa_min) and ((Maikal+Ivan)>=summa_min):
    print (1)
elif (Maikal<=summa_min) and (Ivan<=summa_min) and ((Maikal+Ivan)<=summa_min):
    print (0)