#Aula de dicionário

cadastro = {"CPF": '109.890.767.-74',"Nome": "Michele Bazana de Souza",
            "Data de nascimento": "13/09/1978"}

print(cadastro)
print(cadastro["CPF"])
print(cadastro["Nome"])
print(cadastro["Data de nascimento"])

cadastro["CPF"] = "454.984.458-86"
print(cadastro)

del cadastro["CPF"]
print(cadastro)

cadastro = {"CPF": ['109.890.767.-74','345.565.343-45'],
            "Nome": ["Michele Bazana de Souza","Kauan Sanhez"],
            "Data de nascimento": ["13/09/1978",'08/05/2005']}

cadastro["Data de nascimento"][1] = '12/04/2005'
print(cadastro)

print("telefone" in cadastro)
print("Nome" in cadastro)

print(cadastro.keys())
print(cadastro.values())
