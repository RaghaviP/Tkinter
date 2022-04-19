import winsound
r = 423 # hz, change this as needed
g = 2 ** (1.0 / 12.0)
Sa = r
Re_k = r * g
Re = r * g ** 2
Ga_k = r * g ** 3
Ga = r * g ** 4
Ma = r * g ** 5
Ma_t = r * g ** 6
pa = r * g ** 7
Ni_K = r * g ** 8
Dha_K = r * g ** 9
Ma_t = r * g ** 10
Dha_K= r * g ** 11

song_list =[Ni_K,Dha_K,Ma_t,Dha_K,Dha_K,Dha_K,Dha_K,]

for j in range(1):
    for i in song_list:
        #print(int(song_list[i]))
        winsound.Beep(int(i),1000)
