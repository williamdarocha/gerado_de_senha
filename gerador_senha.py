import tkinter
from random import randint
from customtkinter import *

janela = CTk()
janela.resizable(width=False,height=False)
janela.geometry("500x450")
janela.title("Gerador de senha")

def senhagera():
    numeros = [0,1,2,3,4,5,6,7,8,9]
    maiuscula = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','X','Y','Z']
    minusculo = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z']
    quanmai = len(maiuscula) - 1
    quanmin = len(minusculo) - 1
    quannum = len(numeros) -1

    senha = []
    opcao = opc.get()
    opcao = int(opcao)
    cara = e_carac.get()

    if cara.isnumeric():
        cara = int(cara)
        if cara <= 180:
            match(opcao):
            #criar senhar com caracteres maiusculos e minusculos
                case 1:
                    for quan in range(0,cara):
                        sort = randint(0,1)
                        match(sort):
                            case 0:
                                sor = randint(0,quanmai)
                                senha.append(maiuscula[sor])
                            case 1:
                                sorte = randint(0, quanmin)
                                senha.append(minusculo[sorte])



                #criar senha com caracteres maiusculos e numeros
                case 2:
                    for quan in range(0,cara):
                        sort = randint(0,1)
                        match(sort):
                            case 0:
                                sor = randint(0,quanmai)
                                senha.append(maiuscula[sor])
                            case 1:
                                sorte = randint(0, quannum)
                                senha.append(numeros[sorte])


                #criar senha com caracteres miniusculo e numero
                case 3:
                    for quan in range(0,cara):
                        sort = randint(0,1)
                        match(sort):
                            case 0:
                                sor = randint(0,quanmin)
                                senha.append(minusculo[sor])
                            case 1:
                                sorte = randint(0, quannum)
                                senha.append(numeros[sorte])


                #criar senha com caracteres maiusculos minusculo e numeros
                case 4:
                    for quan in range(0,cara):
                        sort = randint(0,2)
                        match(sort):
                            case 0:
                                sor = randint(0,quanmai)
                                senha.append(maiuscula[sor])
                            case 1:
                                sorte = randint(0, quannum)
                                senha.append(numeros[sorte])
                            case 2:
                                sorte = randint(0,quanmin)
                                senha.append(minusculo[sorte])
        else:
            senha = "LIMITE DE 180 CARACTERIOS"

    else:
        senha = "ISSO NÃO E UM NUMERO"

    texto_gra.delete("0.1","end")
    texto_gra.insert("0.1",text=senha)



frame_cima = CTkFrame(janela,width=500,height=100)
frame_cima.place(x=0,y=0)

mensa = CTkLabel(frame_cima,text="GERADOR DE SENHA")
mensa.place(x=200,y=50)

texto_gra = CTkTextbox(janela)

texto_gra.insert("0.0","")
texto_gra.place(x=260,y=120)

#opções para criar a senha
opc = tkinter.IntVar(value=0)
opcao1 = CTkRadioButton(janela,text="letra maiuscula e letra minuscula", variable=opc,value= 1)
opcao2 = CTkRadioButton(janela,text="numeros e letras maiuscula", variable=opc,value= 2)
opcao3 = CTkRadioButton(janela,text="numeros e letras minuscula", variable=opc,value= 3)
opcao4 = CTkRadioButton(janela,text="numeros,maiusculas e minuscula", variable=opc,value= 4)

#posisoes das opções
opcao1.place(x=30,y=120)
opcao2.place(x=30,y=150)
opcao3.place(x=30,y=180)
opcao4.place(x=30,y=210)

#label para informa o usuario quantidade de caracterio
l_carac = CTkLabel(janela,text="Quantidade de caractere,max 180 ")
l_carac.place(x=30,y=260)

#quantidade de caracterios da senha
e_carac = CTkEntry(janela,width=50)
e_carac.place(x=30,y=290)

#botão para chamar a função criar
botao = CTkButton(janela,command=senhagera,text="gerar senha")
botao.place(x=30,y=350)

janela.mainloop()