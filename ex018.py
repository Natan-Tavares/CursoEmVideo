from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))
rad = radians(ang)
sen = sin(rad)
cos = cos(rad)
tan = tan(rad)
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, cos))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(ang, tan))
