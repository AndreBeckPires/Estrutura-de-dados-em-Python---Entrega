from classArvore import Nodo


#Criando as pastas
home = Nodo("Home", True, False)
user = Nodo("User", True, False)
admin = Nodo("Admin", True, False)
documentos = Nodo("Documentos", True, False)
imagens = Nodo("Imagens", True, False)
musicas = Nodo("Musicas", True, False)
configs = Nodo("Configs", True, False)

#Criando arquivos
relatorio = Nodo("relatorio.pdf", False, True)
tcc = Nodo("tcc.docx", False, True)

foto1 = Nodo("foto1.png", False, True)
foto2 = Nodo("foto2.png", False, True)

rock =  Nodo("rock.mp3", False, True)

systemConfig =  Nodo("system.cfg", False, True)

#Atribuindo relaçoes das pastas
home.setChildren(user)
home.setChildren(admin)
user.setChildren(documentos)
user.setChildren(imagens)
user.setChildren(musicas)
admin.setChildren(configs)

#Atribuindo relaçoes dos arquivos
documentos.setChildren(relatorio)
documentos.setChildren(tcc)

imagens.setChildren(foto1)
imagens.setChildren(foto2)

musicas.setChildren(rock)

configs.setChildren(systemConfig)

