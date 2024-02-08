metros = ['Meguro','Shirokanedai','Shirkane-Takanawa','Mita','Shiba-Koen',
          'Oniramon','Uchi-Saiwaicho','Hibiva','Otemachi','Jimbocho','Siudobashi',
          'Kasuga','Hakusan','Sengoku','Sugamo','Nishi-Sugamo','Shin- Itabashi',
          'Itabashe-Kuyakushomae','Itabashi-Honcho','Motohasunuma','Shimura-Sakaue',
          'Shimura-Sanchome','Hasune','Nishidai','Takashimadeira','Shin-Takashimadaira']
ids = ['A-91','B-82','C-73','D-64','E-55','F-46','G-37','H-28','I-19','J-50','K-41',
       'L-32','M-23','N-14','O-65','P-76','Q-87','R-98','S-09','T-26','U-27','V-28',
       'W-29','X-20','Y-21','Z-22']

id = list(map(int,input().split('-')))

estacao = ids[id[0]-1]
metro = metros[id[0]-1]
print(f'Nós estamos indo para estação {estacao}, cujo nome é {metro}.')