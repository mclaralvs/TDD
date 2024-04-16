def triangulo(l1, l2, l3):
    if l1 <= 0 or l2 <= 0 or l3 <= 0:
        return "Não é um triângulo."
    elif l1 + l2 <= l3 or l1 + l3 <= l2 or l2 + l3 <= l1:
        return "Não é um triângulo."
    elif l1 == l2 == l3:
        return "Triângulo equilátero."
    elif l1 == l2 or l1 == l3 or l2 == l3:
        return "Triângulo isósceles."
    else:
        return "Triângulo escaleno."