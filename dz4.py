# Задача 4. Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

print("Введите общее количество журавликов: ")
sum = int(input())
p = sum // 6
k = p * 4
print("Катя сделала", k, "журавликов, а Петя и Сережа по", p, "журавликов")