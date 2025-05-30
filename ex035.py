print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
primseg = float(input('Primeiro segmento: '))
segseg = float(input('Segundo segmento: '))
terseg = float(input('Terceiro segmento: '))
if primseg < segseg + terseg and segseg < primseg + terseg and terseg < primseg + segseg:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
