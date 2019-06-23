'''-23º 0” 00.00’;-46º 0” 00.00’
37º 5’ 24.72”;-95º 42’ 46.44”
0º 0” 00.00’,-10º 0” 00.00’
20º 0” 00.00’;0º 0” 00.00’
0'''
coor = []
a = 1
while a != '0':
    a = str(input())
    coor.append(a)

linhas = coor

for i in range(0, len(linhas)):
    if linhas[i] != '0':
        if linhas[i].find(';') != -1:
            coordenadas = linhas[i].split(';')

        if linhas[i].find(',') != -1:
            coordenadas = linhas[i].split((','))

        latitude = coordenadas[0]
        longitude = coordenadas[1]

        #Separa graus, minutos e segundos
        lat_grau = latitude.split(' ')[0]
        long_grau = longitude.split(' ')[0]

        lat_min = latitude.split(' ')[1]
        long_min = longitude.split(' ')[1]

        lat_seg = latitude.split(' ')[2]
        long_seg = longitude.split(' ')[2]

        if lat_min.find('’') != -1:
            lat_aux = lat_min
            lat_min = lat_seg
            lat_seg = lat_aux

        if long_min.find('’') != -1:
            long_aux = long_min
            long_min = long_seg
            long_seg = long_aux

        #Tira º ' " do grau
        lat_grau = int(lat_grau[0:len(lat_grau)-1])
        long_grau = int(long_grau[0:len(long_grau)-1])

        lat_min = float(lat_min[0:len(lat_min)-1])
        long_min = float(long_min[0:len(long_min) - 1])

        lat_seg = float(lat_seg[0:len(lat_seg) - 1])
        long_seg = float(long_seg[0:len(long_seg) - 1])

        #Soma e conversão dos minutos e segundos

        lat_grau = lat_grau + ((lat_min*-1)/60) + ((lat_seg*-1)/3600)
        long_grau = long_grau + ((lat_min*-1)/60) + ((lat_seg*-1)/3600)

        #Compara o quadrante
        if lat_grau < 0:
            lat_grau = 'Sul'
        elif lat_grau > 0:
            lat_grau = 'Norte'
        elif lat_grau == 0:
            lat_grau = 'Equador'

        if long_grau > 0:
            long_grau = 'Leste'
        elif long_grau < 0:
            long_grau = 'Oeste'
        elif long_grau == 0:
            long_grau = 'Greenwich'

        print(lat_grau, end=' ')
        print(long_grau)
