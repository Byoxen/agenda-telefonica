import tkinter as tk
from tkinter import END, font, messagebox, ttk
import sqlite3

branco = '#FFFFFF'
roxo = '#676be0'
cinza = '#E5E5E5'
preto = '#000000'


class tela_bv:
    def __init__(self):
        self.tudo()

    def tudo(self):
        self.janela()
        self.frames()
        self.labels()
        self.botoes()

    def janela(self):
        self.master = tk.Tk()
        self.master.title('Agenda Telefônia')
        self.master.geometry('900x500+300+150')
        self.master.config(bg=roxo)
        self.master.resizable(False, False)

    def frames(self):
        self.frame_bv = tk.Frame(self.master, width=400, height=300, bg=branco)
        self.frame_bvborda = tk.Frame(self.frame_bv, width=210, height=60, highlightbackground=roxo,
                                      highlightthickness=1)
        self.frame_bvborda.place(x=95, y=122)
        self.frame_bv.place(x=250, y=100)

    def labels(self):
        self.label_bemvindo = tk.Label(
            self.frame_bv, text='Bem-vindo!', font='Radley 25 "bold"', bg=branco)
        self.label_bemvindo.place(x=105, y=30)

    def botoes(self):
        self.botao1 = tk.Button(self.frame_bvborda, cursor='hand2', command=self.trocar_janela, bg=branco,
                                relief=tk.FLAT, padx=56, text='Entrar', font='Radley 20', borderwidth=1, border=0)
        self.botao1.place(x=0, y=0)

    def trocar_janela(self):
        self.master.destroy()
        agenda()

    def run(self):
        self.master.mainloop()


class agenda():
    def __init__(self):
        self.tudo()

    def tudo(self):
        self.criar_db()
        self.janela()
        self.frames()
        self.labels()
        self.entradas()
        self.botoes()
        self.binds()
        self.treeviews()
        

    def criar_db(self):
        self.database = sqlite3.connect('Contatos.db')
        self.cursor = self.database.cursor()
        self.database.execute(
            'CREATE TABLE IF NOT EXISTS CONTATOS(NOME TEXT, NUMERO1 INTEGER, NUMERO2 INTEGER, NUMERO3 INTEGER)')
        self.database.commit()
        self.database.close()

    def janela(self):
        self.master = tk.Tk()
        self.master.title('Agenda Telefônia')
        self.master.geometry('900x500+300+150')
        self.master.config(bg=roxo)
        self.master.resizable(False, False)

    def treeviews(self):

        self.treeview = ttk.Treeview(self.frame2,
                                     columns=('nome', 'primero número',
                                              'segundo número', 'terceiro número'),
                                     show='headings')
        self.treeview.column('nome', minwidth=90, width=50)
        self.treeview.column('primero número', minwidth=90, width=50)
        self.treeview.column('segundo número', minwidth=90, width=50)
        self.treeview.column('terceiro número', minwidth=90, width=50)
        self.treeview.heading('nome', text='Nome')
        self.treeview.heading('primero número', text='Número 1')
        self.treeview.heading('segundo número', text='Número 2')
        self.treeview.heading('terceiro número', text='Número 3')
        self.treeview.place(x=0, y=70, w=500, h=330)

        self.database = sqlite3.connect('Contatos.db')
        self.cursor = self.database.cursor()
        self.cursor.execute("SELECT * FROM CONTATOS")
        rows = self.cursor.fetchall()
        global count
        count = 0
        global dados
        for dados in rows:
            if count % 2 == 0:
                self.treeview.insert('', 'end', values=(
                    dados[0], dados[1], dados[2], dados[3]))
            else:
                self.treeview.insert('', 'end', values=(
                    dados[0], dados[1], dados[2], dados[3]))

            count += 1
        self.database.commit()
        self.database.close()

    def frames(self):
        self.frame1 = tk.Frame(self.master, bg=branco, width=300, height=400)
        self.frame2 = tk.Frame(self.master, bg=branco, width=500, height=400)
        self.frame_borda = tk.Frame(
            self.frame1, width=158, height=52, highlightbackground=roxo, highlightthickness=1)
        self.frame_barra1 = tk.Frame(
            self.frame1, bg=preto, width=250, height=2)
        self.frame_barra2 = tk.Frame(
            self.frame1, bg=preto, width=250, height=2)
        self.frame_barra3 = tk.Frame(
            self.frame1, bg=preto, width=250, height=2)
        self.frame_barra4 = tk.Frame(
            self.frame1, bg=preto, width=250, height=2)
        self.frame_fundo = tk.Frame(
            self.frame1, bg=cinza, width=300, height=55)

        self.frame1.place(x=33, y=50)
        self.frame2.place(x=375, y=50)
        self.frame_borda.place(x=70, y=278)
        self.frame_barra1.place(x=25, y=110)
        self.frame_barra2.place(x=25, y=160)
        self.frame_barra3.place(x=25, y=210)
        self.frame_barra4.place(x=25, y=260)
        self.frame_fundo.place(x=0, y=345)

    def labels(self):
        self.label1 = tk.Label(
            self.frame1, bg=branco, text='Adicionar Contato', font='RadHatDisplay 20')
        self.label2 = tk.Label(
            self.frame2, bg=branco, text='Lista de Contatos', font='RadHatDisplay 20')
        self.label3 = tk.Label(self.frame_fundo, bg=cinza,
                               text='Quer editar um contato?', font='RadHatDisplay 12')
        self.label4 = tk.Label(self.frame_fundo, bg=cinza, text='Clique aqui!', font='RadHatDisplay 12', fg=roxo,
                               cursor='hand2')
        self.label1.place(x=40, y=23)
        self.label2.place(x=155, y=23)
        self.label3.place(x=16, y=15)
        self.label4.place(x=190, y=15)

    def entradas(self):
        self.entrada_nome = tk.Entry(
            self.frame1, width=25, borderwidth=0, bg=branco, font='RadHatDisplay 12')
        self.entrada_nome.insert(0, 'Nome')
        self.validacao = self.master.register(self.onlyletters)
        self.entrada_nome.config(
            validate='key', validatecommand=(self.validacao, '%P'))
        self.entrada_numero1 = tk.Entry(
            self.frame1, width=25, borderwidth=0, bg=branco, font='RadHatDisplay 12')
        self.entrada_numero1.insert(0, 'Número 1')
        self.entrada_numero2 = tk.Entry(
            self.frame1, width=25, borderwidth=0, bg=branco, font='RadHatDisplay 12')
        self.entrada_numero2.insert(0, 'Número 2')
        self.entrada_numero3 = tk.Entry(
            self.frame1, width=25, borderwidth=0, bg=branco, font='RadHatDisplay 12')
        self.entrada_numero3.insert(0, 'Número 3')
        self.entrada_nome.place(x=28, y=90)
        self.entrada_numero1.place(x=28, y=140)
        self.entrada_numero2.place(x=28, y=190)
        self.entrada_numero3.place(x=28, y=240)

    def insert(self):
        if self.entrada_numero2.get() == '' or self.entrada_numero2.get() == 'Número 2':
            self.entrada_numero2.delete(0, END)
            self.entrada_numero2.insert(0, 'S/N')
        else:
            pass
        if self.entrada_numero3.get() == '' or self.entrada_numero3.get() == 'Número 3':
            self.entrada_numero3.delete(0, END)
            self.entrada_numero3.insert(0, 'S/N')
        else:
            pass
        if self.entrada_nome.get() == '' or self.entrada_nome == 'Nome' and self.entrada_numero1.get() == '' or self.entrada_numero1.get() == 'Número 1':
            messagebox.showerror('Agenda Telefônica', 'Há dados faltando.')
            self.entrada_nome.delete(0, END)
            self.entrada_numero1.delete(0, END)
            self.entrada_numero2.delete(0, END)
            self.entrada_numero3.delete(0, END)
            self.entrada_nome.insert(0, 'Nome')
            self.entrada_numero1.insert(0, 'Número 1')
            self.entrada_numero2.insert(0, 'Número 2')
            self.entrada_numero3.insert(0, 'Número 3')

        else:
            self.database = sqlite3.connect('Contatos.db')
            self.cursor = self.database.cursor()
            self.database.execute(
                'CREATE TABLE IF NOT EXISTS CONTATOS(NOME TEXT UNIQUE, NUMERO1 INTEGER, NUMERO2 INTEGER, NUMERO3 INTEGER)')
            self.database.execute(
                'INSERT INTO CONTATOS VALUES(:entry_nome, :entry_numero1, :entry_numero2, :entry_numero3)',
                {
                    'entry_nome': self.entrada_nome.get(),
                    'entry_numero1': self.entrada_numero1.get(),
                    'entry_numero2': self.entrada_numero2.get(),
                    'entry_numero3': self.entrada_numero3.get()
                })
            messagebox.showinfo('Agenda Telefônica', 'Contato criado.')
            self.database.commit()
            self.entrada_nome.delete(0, END)
            self.entrada_numero1.delete(0, END)
            self.entrada_numero2.delete(0, END)
            self.entrada_numero3.delete(0, END)
            self.entrada_nome.insert(0, 'Nome')
            self.entrada_numero1.insert(0, 'Número 1')
            self.entrada_numero2.insert(0, 'Número 2')
            self.entrada_numero3.insert(0, 'Número 3')
            self.master.focus()
            self.treeviews()

    def select(self, event):
        global valor_one
        global valor_two

        self.entrada_nome.delete(0, END)
        self.entrada_numero1.delete(0, END)
        self.entrada_numero2.delete(0, END)
        self.entrada_numero3.delete(0, END)

        self.selecionado = self.treeview.focus()
        values = self.treeview.item(self.selecionado, 'values')

        self.entrada_nome.insert(0, values[0])
        self.entrada_numero1.insert(0, values[1])
        self.entrada_numero2.insert(0, values[2])
        self.entrada_numero3.insert(0, values[3])
        self.original = self.entrada_nome.get()

        valor_one = values[0]
        valor_two = values[1]

    def editar(self):
        self.frames()
        self.entradas()
        self.binds()
        self.treeviews()

        self.label5 = tk.Label(
            self.frame_fundo, text='Quer adicionar um contato?', font='RadHatDisplay 12', bg=cinza)
        self.label6 = tk.Label(self.frame_fundo, text='Clique aqui!', font='RadHatDisplay 12', bg=cinza, fg=roxo,
                               cursor='hand2')
        self.label7 = tk.Label(self.frame1, bg=branco,
                               text='Editar contato', font='RadHatDisplay 20')
        self.label9 = tk.Label(self.frame1, text = '(Clique em cima de um contato)', font = 'RadHatDisplay 10', bg = branco, fg = roxo)
        self.label8 = tk.Label(
            self.frame2, bg=branco, text='Lista de Contatos', font='RadHatDisplay 20')

        self.label6.bind("<Button-1>", lambda e: self.trocar())
        self.treeview.bind("<ButtonRelease-1>", lambda e: self.select(e))

        self.botao_editar = tk.Button(self.frame_borda, font='RadHatDisplay 17 ', text='Editar Dados', relief=tk.FLAT,
                                      bg=branco, padx=2, pady=3, command=lambda: self.trocar_contato())
        self.botaoexcluir = tk.Button(
            self.frame1, text='Excluir', command=self.delete, relief='flat', bg=branco, fg='red')
        self.botaoexcluir.place(x=230, y=290)
        self.botao_editar.place(x=0, y=0)

        self.label5.place(x=5, y=15)
        self.label6.place(x=200, y=15)
        self.label7.place(x=60, y=23)
        self.label9.place(x=53, y=57)
        self.label8.place(x=155, y=23)

    def onlyletters(self, input):
        if input.isalpha():
            return True
        elif input == '':
            return True
        else:
            return False

    def nome_focusin(self):
        if self.entrada_nome.get() == "Nome":
            self.entrada_nome.delete(0, END)
        else:
            pass

    def nome_focusout(self):
        if self.entrada_nome.get() == "":
            self.entrada_nome.insert(0, "Nome")
        else:
            pass

    def numero1_focusin(self):
        if self.entrada_numero1.get() == 'Número 1':
            self.entrada_numero1.delete(0, END)
        else:
            pass

    def numero1_focusout(self):
        if self.entrada_numero1.get() == '':
            self.entrada_numero1.insert(0, "Número 1")

    def numero2_focusin(self):
        if self.entrada_numero2.get() == 'Número 2':
            self.entrada_numero2.delete(0, END)
        else:
            pass

    def numero2_focusout(self):
        if self.entrada_numero2.get() == '':
            self.entrada_numero2.insert(0, "Número 2")

    def numero3_focusin(self):
        if self.entrada_numero3.get() == 'Número 3':
            self.entrada_numero3.delete(0, END)
        else:
            pass

    def numero3_focusout(self):
        if self.entrada_numero3.get() == '':
            self.entrada_numero3.insert(0, "Número 3")

    def trocar_contato(self):
        self.database = sqlite3.connect('Contatos.db')
        self.cursor = self.database.cursor()
        self.database.execute('UPDATE CONTATOS SET NOME=?, NUMERO1=?, NUMERO2=?, NUMERO3=? WHERE NOME=? ', (self.entrada_nome.get(
        ), self.entrada_numero1.get(), self.entrada_numero2.get(), self.entrada_numero3.get(), self.original))
        self.database.commit()
        self.treeviews()
        messagebox.showinfo('Agenda Telefônica', 'Contato Atualizado.')
        self.entrada_nome.delete(0, END)
        self.entrada_numero1.delete(0, END)
        self.entrada_numero2.delete(0, END)
        self.entrada_numero3.delete(0, END)
        self.entrada_nome.insert(0, 'Nome')
        self.entrada_numero1.insert(0, 'Número 1')
        self.entrada_numero2.insert(0, 'Número 2')
        self.entrada_numero3.insert(0, 'Número 3')
        self.frame1.destroy()
        self.frames()
        self.labels()
        self.entradas()
        self.botoes()
        self.binds()
        self.treeviews()

    def trocar(self):
        self.frame1.destroy()
        self.frame2.destroy()
        self.frames()
        self.labels()
        self.botoes()
        self.entradas()
        self.binds()
        self.treeviews()

    def binds(self):
        self.label4.bind("<Button-1>", lambda e: self.editar())
        self.entrada_nome.bind("<FocusIn>", lambda e: self.nome_focusin())
        self.entrada_nome.bind("<FocusOut>", lambda e: self.nome_focusout())
        self.entrada_numero1.bind(
            "<FocusIn>", lambda e: self.numero1_focusin())
        self.entrada_numero1.bind(
            "<FocusOut>", lambda e: self.numero1_focusout())
        self.entrada_numero2.bind(
            "<FocusIn>", lambda e: self.numero2_focusin())
        self.entrada_numero2.bind(
            "<FocusOut>", lambda e: self.numero2_focusout())
        self.entrada_numero3.bind(
            "<FocusIn>", lambda e: self.numero3_focusin())
        self.entrada_numero3.bind(
            "<FocusOut>", lambda e: self.numero3_focusout())

    def botoes(self):
        self.botao1 = tk.Button(self.frame_borda, font='RadHatDisplay 17 ', text='Inserir Dados', relief=tk.FLAT,
                                bg=branco, padx=0, pady=3, command=self.insert)
        self.botao1.place(x=0, y=0)

    def delete(self):
        self.database = sqlite3.connect('Contatos.db')
        self.cursor = self.database.cursor()
        self.cursor.execute(
            'delete from Contatos where NOME=? and NUMERO1=?', (valor_one, valor_two))
        self.database.commit()
        messagebox.showinfo('Agenda Telefônica', 'Contato Excluído.')
        self.frame1.destroy()
        self.frames()
        self.labels()
        self.entradas()
        self.botoes()
        self.binds()
        self.treeviews()


if __name__ == "__main__":
    tela = tela_bv()
    tela.run()
