frase = 'curso em vídeo'
print(frase[3])
print(frase[3:7])
print(frase[7:])
print(frase[::2])
print("""Lorem Ipsum é simplesmente uma simulação de texto da indústria
tipográfica e de impressos, e vem sendo utilizado desde o século XVI, quando um impressor
desconhecido pegou uma bandeja de tipos e os embaralhou para fazer um livro de modelos
de tipos. Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto
para a editoração eletrônica, permanecendo
essencialmente inalterado. Se popularizou na década de 60, quando a Letraset
lançou decalques contendo passagens de Lorem Ipsum, e mais recentemente quando
passou a ser integrado a softwares de editoração eletrônica como Aldus PageMaker.""")
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('curso', 'receba'))
print('curso' in frase)
print('receba' in frase)
print(frase.find('curso'))
dividido = frase.split()
print(dividido[0])
print(dividido[1][1])