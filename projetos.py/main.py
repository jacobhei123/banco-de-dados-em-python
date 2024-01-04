from database import db, Usuario, Anuncio 

db.connect()

db.create_tables((Usuario, Anuncio))

Usuario = Usuario.create(nome="ProgramadorPython", email="teste@teste.com", senha=123456)

print("Novo usuario:", usuario.id, usuario.nome, usuario.email)

Usuario.create(nome="Guilherme" , email="gui@teste.com", senha="123456")
Usuario.create(nome="Joao" , email="joao@teste.com", senha="123456")
Usuario.create(nome="Maria" , email="maria@teste.com", senha="123456")

lista_usuario = Usuario.select()
print("listando usuarios:")

for u in lista_usuario:
   print("-", u.id, u.nome, u.email)
    

usuario1 = Usuario.get(Usuario.id == 1)
print ("usuario pelo id", usuario1.id, usuario1.nome)

joao = Usuario.get( Usuario.email == "joao@teste.com")
print("usuario: " , joao.id, joao.nome, joao.email)

Maria = Usuario.get( Usuario.email == "maria@teste.com")
Maria.nome="Maria Python"
maria.save()

print("maria atualizada: ", maria.nome)

print("Tentando criar um usuario com e-mail duplicado")

try:
    usuario_duplicado = Usuario.create(nome = "Duplicado", email="teste@teste.com",senha="123456")
except:
    print("E-mail existente!")

usuario_deletado = Usuario.get ( Usuario.email == "teste@teste.com")
usuario_deletado.delete_instance()

try:
    Usuario.get(Usuario.email == "teste@teste.com")
except:
    print("Usuario deletado!")

maria = Usuario.get( Usuario.email == "maria@teste.com")

anuncio = Anuncio.create(
    usuario = maria,
   titulo = "Video de Banco de Dados", 
     descricao = "O projeto seria criar um video sobre banco de dados e ORM com phyton",
    valor = 500.0
)

print("Novo anuncio:", anuncio.id, anuncio.titulo)

Anuncio.create(usuario = maria, título = "Anuncio 1" , descricao = "Deixa o like", valor = 1000)
Anuncio.create(usuario = maria, título = "Anuncio 1" , descricao = "Deixa o like", valor = 1000)
Anuncio.create(usuario = maria, título = "Anuncio 1" , descricao = "Deixa o like", valor = 1000)

print("anuncios da maria:")
anuncios_maria = Anuncio.select().join(Usuario).where(Usuario.email == "maria@teste.com")
for a in anuncios_maria:
   print("_",a.id, a.titulo, a.valor)

Anuncio.delete().execute()

print("Quantidade de anuncios:", Anuncios.select().count())