
# #  = """[
# # {
# # "nome_serie":"stranger things",
# # "ano": "2016/2025",
# # "episodios":"160",
# # "genero": "ficçao/terror",
# # "temporadas": "4"
# # },
# # {
# # "nome_serie":outer banks",
# # "ano": "2020".,
# # "episodios": "40",
# # "genero": "aventura",
# # "temporadas": 

# # }

# # ]


# # }






# # """



# import json

# dados = { 'nome': 'joao silva', 'idade': 30,
#          'cidade': 'sao paulo', 'seviço': 'premium'}
# json_string = json.dumps (dados)

# #imprimido o dicionario inteiro com uma string json

# print(json_string)
# #im´primindo o dicionario inteiro com uma string json

import json
frutas ={
      'frutas':[
          
      "fruta1": "maça"
      "preço" 2.34,

      "fruta" "pera",
      "preço": 3.45,

      "fruta1": "banana",
      "preço":1,23,
          
      "futa#": "laranja",
      "preço": 4.56,
}
     ##escrever json
     # with open('frutas. json', 'w', encoding='utf-8')as arquivo:
     json.dump(frutas, arquivo, indent=8, ensure_ascii=false)   




























