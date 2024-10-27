salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов


mcount = 0
saved = 0
while mcount is not months:
    saved = saved + salary - spend
    mcount += 1
    spend = spend * (1 + increase)
    #print(saved)
saved = -round(saved)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", saved)