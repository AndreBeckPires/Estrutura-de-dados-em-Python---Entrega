from classArvore import Nodo

# Criando as pastas
home = Nodo("Home", True, False)
user = Nodo("User", True, False)
admin = Nodo("Admin", True, False)
documentos = Nodo("Documentos", True, False)
imagens = Nodo("Imagens", True, False)
musicas = Nodo("Musicas", True, False)
configs = Nodo("Configs", True, False)

# Criando arquivos
relatorio = Nodo("relatorio.pdf", False, True)
tcc = Nodo("tcc.docx", False, True)
foto1 = Nodo("foto1.png", False, True)
foto2 = Nodo("foto2.png", False, True)
rock = Nodo("rock.mp3", False, True)
systemConfig = Nodo("system.cfg", False, True)

# Montando a árvore
home.setChildren(user)
home.setChildren(admin)
user.setChildren(documentos)
user.setChildren(imagens)
user.setChildren(musicas)
admin.setChildren(configs)

documentos.setChildren(relatorio)
documentos.setChildren(tcc)
imagens.setChildren(foto1)
imagens.setChildren(foto2)
musicas.setChildren(rock)
configs.setChildren(systemConfig)

# buscar arquivos 
def buscar_arquivos_por_extensao(nodo, extensao_desejada, caminho_atual="", resultados=None):
    if resultados is None:
        resultados = {}

    if nodo.isFolder:
        caminho_completo = f"{caminho_atual}/{nodo.getValue()}".strip("/")
        arquivos_encontrados = []

        for filho in nodo.getChildrens():
            if filho.isFile and filho.getValue().endswith(extensao_desejada):
                arquivos_encontrados.append(filho.getValue())
            elif filho.isFolder:
                buscar_arquivos_por_extensao(filho, extensao_desejada, caminho_completo, resultados)

        if arquivos_encontrados:
            resultados[caminho_completo] = arquivos_encontrados

    return resultados
# buscado na net
# Função principal de recomendação
def recomendar_pasta_por_extensao(raiz, extensao_desejada):
    resultados = buscar_arquivos_por_extensao(raiz, extensao_desejada)

    if not resultados:
        print("\n Nenhum arquivo encontrado com essa extensão.")
        return

    pasta_recomendada = max(resultados.items(), key=lambda item: len(item[1]))

    print(f"\n Pasta recomendada: /{pasta_recomendada[0]}")
    print(" Arquivos encontrados:")
    for arquivo in pasta_recomendada[1]:
        print(f" - {arquivo}")

# Execução interativa
if __name__ == "__main__":
    print(" Buscador de arquivos por tipo")
    extensao = input("Digite a extensão do arquivo (ex: .mp3, .pdf, .png): ").strip()
    recomendar_pasta_por_extensao(home, extensao)
    
