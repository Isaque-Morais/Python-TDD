url = "https://twitter.com/search?q=alura&src=typed_query"
print(url)



indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
print(url_base)

# Propriedade do fatiamento de string você pode deixar
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)