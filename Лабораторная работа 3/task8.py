money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение

while money_capital >= spend:
    money_capital += salary - spend
    spend *= (1 + increase)
    month += 1

print(month)

""" Судя по ответу, правильным условием является "money_capital >= spend",
но по факту можно прожить 5 месяцев, используя условие "money_capital >= spend - salary",
при этом будет отсутствовать финансовая подушка безопасности """
