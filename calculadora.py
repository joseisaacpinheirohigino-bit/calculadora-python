import tkinter as tk 

expressao = ""
linha_padrao = 1

#def é uma função/metodo
def adicionar(valor):
    global expressao
   
    expressao += valor  # é a mesma coisa que expressao = expressao + valor
    tela.set(expressao)
    
def limpar():
    global expressao
    expressao = ""
    tela.set(expressao)
    
def calcular():
    global expressao
    
    #try -> Tratamento de erro pra cituações de calculos que pode gerar erro
    #eval -> ele pega uma expressao algebrica (15 + 25 / 3 * 7) irá resolver e me dá um resultado
    try:
        resultado = str(eval(expressao))
        tela.set(resultado)
        expressao = resultado
    #except -> Ele trata e zera minha expressão
    except:
        tela.set("ERROR!")
        expressao = ""
        
# Janela de aplicação
janela = tk.Tk()
janela.title("Calculadora python")
janela.geometry("340x430")
janela.resizable(False,False)

# Tela da calculadora
tela = tk.StringVar()

entrada = tk.Entry(janela, textvariable=tela,
                   font=("Impact",24) , justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10,
             pady=10, ipady=15, sticky="nsew")

# Matriz de botões
botoes = [
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    ["0",".","C","+"]
]

for linha in range(len(botoes)):
    for coluna in range(len(botoes[linha])):
        valor = botoes[linha][coluna]
        
        if valor == "C":
            botao = tk.Button(janela, text=valor, 
                              font=("Arial",16), command=limpar)
        else:
            botao = tk.Button(janela, text=valor, 
                              font=("Arial",16), command=lambda v = valor: adicionar(v)) 
            
        botao.grid(row=linha + 1, column=coluna, 
                   padx=3, pady=3, sticky="nsew")
    linha_padrao += 1    
# botão de calcular 

igual = tk.Button(janela, text="=", 
                font=("Arial",18), command=calcular)

igual.grid(row=linha_padrao, column=0, columnspan=4,
           padx=3, pady=5, sticky="nsew")

#ajustar tamanho das colunas

for coluna in range(4):
    janela.columnconfigure(
        coluna,weight=1
    )
    
for linha in range(1,linha_padrao+1):
    janela.rowconfigure(
        linha,weight=1
    )
    
janela.mainloop()