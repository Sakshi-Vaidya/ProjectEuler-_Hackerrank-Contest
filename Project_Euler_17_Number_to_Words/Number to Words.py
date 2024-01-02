d1 = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}

d2 = {10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}

d3 = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}

def number1(n):   # this fonction give the numbre with word with number between 0 nd 100
    if 1 <= n < 10:
        return d1[n]
    elif 10 <= n < 20:
        return d2[n]
    else:
        a = n % 10
        b = n // 10
        if a == 0:
            return d3[b]
        else:
            ch = d3[b] + " " + d1[a]
            return ch

def number2(n): # this fonction give the numbre with word with number between 0 nd 999
    if n < 100:
        return number1(n)
    else:
        a = n % 100
        b = n // 100
        if a == 0:
            return d1[b] + " Hundred"
        else:
            ch = d1[b] + " Hundred " + number1(a)
            return ch

d4 = {1: "Thousand", 2: "Million", 3: "Billion", 4: "Trillion"}

def number3(n): # this fonction give the numbre with word with number between 0 nd 9999..
    if n < 1000:
        return number2(n)
    else:
        ch1 = str(n)
        l = []
        for i in range(len(ch1), 0, -3):
            l.append(int(ch1[max(i - 3, 0):i]))
        ch2 = number2(l[0])
        for i in range(1, len(l)):
            if l[i] != 0:  
                ch2 = number2(l[i]) + " " + d4[i] + " " + ch2
        return ch2

for _ in range(int(input())):
    num = int(input())
    print(number3(num))