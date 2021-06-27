from tkinter import *
from tkinter import ttk
from api import *
import _thread as thread

#As funções abaixo são responsáveis por transitar entre as telas, sendo acionadas pelos
#botões "Voltar" e "Avançar"

def pilotos_circuitos():
    screen2.pack_forget()
    screen5.pack()

def circuitos_pilotos():
    screen5.pack_forget()
    screen2.pack()


#Função responsável cadastrar carros no arquivo cars.json
#caso os dados tenham sido preenchidos corretamente
def cars():
    if(ec1.get()!='' and cc1.get()!='' and cc2.get()!=''):
        ret = a.checkCars(ec1.get())
        if(ret):
            print('Carro já existe')
        else:
            a.signupCars(ec1.get(), cc1.get(), cc2.get())
    else: 
        print('Preencha os campos corretamente!')

#Função responsável por cadastrar uma equipe no arquivo teams.json
#caso os dados tenham sido preenchidos corretamente
def teams():
    if(ee1.get()!=''):
        ret = a.checkTeams(ee1.get())
        if(ret):
            print('Equipe já existe')
        else:
            a.signupTeams(ee1.get(), ce1.get())
    else: 
        print('Preencha os campos corretamente!')

#Função responsável por cadastrar um piloto no arquivo pilots.json
#caso os dados tenham sido preenchidos corretamente
def pilots():
    if(ep1.get()!='' and ep2.get()!='' and ep3.get()!=''):
        ret = a.checkPilots(ep1.get())
        if(ret):
            print('Piloto já existe')
        else:
            a.signupPilots(ep1.get(), ep2.get(), ep3.get())
    else: 
        print('Preencha os campos corretamente!')

#Função responsável por cadastrar um circuito no arquivo circuits.json
#caso os dados tenham sido preenchidos corretamente
def circuits():
    if(e51.get()!='' and c51.get()!='' and e53.get()!=''):
        ret = a.checkCircuits(e51.get())
        if(ret):
            print('Pista já existe')
        else:
            a.signupCircuits(e51.get(), c51.get(), e53.get())
    else: 
        print('Preencha os campos corretamente!')

#Função responsável por cadastrar uma corrida no arquivo race.json
def races(): 
    if(e61.get()!='' and e62.get()!=''):
        a.signupRaces(e61.get(), e62.get(), c60.get(), c61.get(), c62.get(), c63.get(), c64.get())        
    else: 
        print('Preencha os campos corretamente!')

#Instancias da classe tk que é a biblioteca usada para desenvolver a interface, 
#da classe cliente e da classe api
s = Tk()
s.title('Autorama')
s.geometry('680x570')
a = api()

#As linhas de código abaixo em sua maioria dizem respeito a instâncias de componentes de tela,
#como botões, labels, inputs e etc, despensa explicações


#Elementos contidos na tela de carros

screen2 = Frame(s)
frame1 = Frame(screen2)
frame2 = Frame(screen2)
frame3 = Frame(screen2)

lc1 = Label(frame1, text = 'CARROS', font = 'verdana 16 bold', anchor='e')
lc1.pack()

lc2 = Label(frame2, text = 'Tag', font = 'verdana 11 bold')
lc2.grid(row = 0, column = 0)

ec1 = Entry(frame2, width = 25, font = 'verdana 10')
ec1.grid(row = 1, column = 0, pady = 8, padx = 20)


lc4 = Label(frame2, text = 'Marca', font = 'verdana 11 bold')
lc4.grid(row = 0, column = 1)

marcas = a.marcas
cc1 = ttk.Combobox(frame2, values = marcas, width = 10)
cc1.set(marcas[0])
cc1.grid(row = 1, column = 1, pady = 8, padx = 20)

lc5 = Label(frame2, text = 'Cor', font = 'verdana 11 bold')
lc5.grid(row = 0, column = 2)

cores = a.cores
cc2 = ttk.Combobox(frame2, values = cores, width = 10)
cc2.set(cores[0])
cc2.grid(row = 1, column = 2, pady = 8, padx = 20)

bc3 = Button(frame3, text = 'Cadastrar', width = 12, font = 'verdana 10 bold', command=cars)
bc3.pack(side = 'left')

frame1.pack(pady = 10)
frame2.pack(pady = 8)
frame3.pack(pady = 8)

#Componentes da tela de equipes

framee1 = Frame(screen2)
framee2 = Frame(screen2) 
framee3 = Frame(screen2)

le1 = Label(framee1, text = 'EQUIPES', font = 'verdana 16 bold', anchor='e', pady = 5)
le1.pack()

le2 = Label(framee2, text = 'Nome', font = 'verdana 11 bold')
le2.grid(row = 0, column = 0)

ee1 = Entry(framee2, font = 'verdana 10')
ee1.grid(row = 1, column = 0, pady = 8, padx=20)

le3 = Label(framee2, text = 'País', font = 'verdana 11 bold')
le3.grid(row = 0, column = 1)

paises = a.paises
ce1 = ttk.Combobox(framee2, values = paises)
ce1.set(paises[0])
ce1.grid(row = 1, column = 1, pady = 8, padx = 20)

be1 = Button(framee3, text = 'Cadastrar', width = 12, font = 'verdana 10 bold', command = teams)
be1.grid(row = 11, column = 1)

framee1.pack(pady = 10)
framee2.pack(pady = 8)
framee3.pack(pady = 5)

#Componentes da tela de pilotos


framep1 = Frame(screen2)
framep2 = Frame(screen2) 
framep3 = Frame(screen2)

lp1 = Label(framep1, text = 'PILOTOS', font = 'verdana 16 bold', anchor='e', pady = 5)
lp1.pack()

lp2 = Label(framep2, text = 'Nome', font = 'verdana 11 bold')
lp2.grid(row = 0, column = 0)

ep1 = Entry(framep2, font = 'verdana 10', width = 16)
ep1.grid(row = 1, column = 0, pady = 8, padx=20)

lp3 = Label(framep2, text = 'Equipe', font = 'verdana 11 bold')
lp3.grid(row = 0, column = 1)

ep2 = Entry(framep2, font = 'verdana 10', width = 16)
ep2.grid(row = 1, column = 1, pady = 1, padx=20)

lp4 = Label(framep2, text = 'Carro', font = 'verdana 11 bold')
lp4.grid(row = 0, column = 2)

ep3 = Entry(framep2, width = 26, font = 'verdana 10')
ep3.grid(row = 1, column = 2, pady = 8, padx=20)

bp1 = Button(framep3, text = 'Cadastrar', width = 12, font = 'verdana 10 bold', command = pilots)
bp1.grid(row = 11, column = 1)

bp2 = Button(framep3, text = 'Avançar', width = 12, font = 'verdana 10 bold', command = pilotos_circuitos)
bp2.grid(row =11, column = 2)

framep1.pack(pady = 10)
framep2.pack(pady = 8)
framep3.pack(pady = 5)

screen2.pack()

#Componente da tela de circuitos

screen5 = Frame(s)
frame51 = Frame(screen5)
frame52 = Frame(screen5)
frame53 = Frame(screen5)

l51 = Label(frame51, text = 'CIRCUITOS', font = 'verdana 16 bold', anchor='e')
l51.pack()

l52 = Label(frame52, text = 'Nome', font = 'verdana 11 bold')
l52.grid(row = 0, column = 0)

e51 = Entry(frame52, font = 'verdana 10')
e51.grid(row = 1, column = 0, pady = 8, padx = 15)

l53 = Label(frame52, text = 'Pais', font = 'verdana 11 bold')
l53.grid(row = 0, column = 1)

paises = a.paises
c51 = ttk.Combobox(frame52, values = paises, width = 10)
c51.set(paises[0])
c51.grid(row = 1, column = 1, padx = 15)

l54 = Label(frame52, text = 'Recorde', font = 'verdana 11 bold')
l54.grid(row = 0, column = 2)

e53 = Entry(frame52, font = 'verdana 10', width = 10)
e53.grid(row = 1, column = 2, padx = 15)

b51 = Button(frame53, text = 'Cadastrar', width = 12, font = 'verdana 10 bold', command = circuits)
b51.grid(row = 11, column = 1)

frame51.pack(pady = 10)
frame52.pack(pady = 8)
frame53.pack(pady = 8)

frame61 = Frame(screen5)
frame62 = Frame(screen5) 
frame63 = Frame(screen5)
frame64 = Frame(screen5)
frame65 = Frame(screen5)

l61 = Label(frame61, text = 'PARTIDA', font = 'verdana 16 bold', anchor='e')
l61.pack()

l62 = Label(frame62, text = 'Duração', font = 'verdana 11 bold')
l62.grid(row = 0, column = 0)

e61 = Entry(frame62, font = 'verdana 10', width = 10)
e61.grid(row = 1, column = 0, pady = 8, padx = 20)

l63 = Label(frame62, text = 'Voltas', font = 'verdana 11 bold')
l63.grid(row = 0, column = 1)

e62 = Entry(frame62, font = 'verdana 10', width = 10)
e62.grid(row = 1, column = 1, pady = 8, padx = 20)

l64 = Label(frame62, text = 'Pista', font = 'verdana 11 bold')
l64.grid(row = 0, column = 2)

circuitos = a.getCircuits()
c60 = ttk.Combobox(frame62, values = circuitos, width = 16)
c60.grid(row = 1, column = 2, pady = 10, padx = 20)

l66 = Label(frame62, text = 'Pilotos', font = 'verdana 11 bold')
l66.grid(row = 2, sticky = W)

pilotos = a.getPilots()
c61 = ttk.Combobox(frame62, values = pilotos, width = 10)
c61.grid(row = 3, sticky = W, pady = 10, column = 0)

c62 = ttk.Combobox(frame62, values = pilotos, width = 10)
c62.grid(row = 3, sticky = W, pady = 10, column = 1)

c63 = ttk.Combobox(frame62, values = pilotos, width = 10)
c63.grid(row = 3, sticky = W, pady = 10, column = 2)

c64 = ttk.Combobox(frame62, values = pilotos, width = 10)
c64.grid(row = 3, sticky = W, pady = 10, column = 3)

b50 = Button(frame63, text = 'Voltar', width = 12, font = 'verdana 10 bold', command = circuitos_pilotos)
b50.grid(row = 11, column = 0)

b61 = Button(frame63, text = 'Cadastrar', width = 12, font = 'verdana 10 bold', command = races)
b61.grid(row = 11, column = 1)

frame61.pack(pady = 10)
frame62.pack(pady = 8)
frame63.pack(pady = 10)
frame65.pack()
frame64.pack(pady = 4)

   

s.mainloop()