import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style

app = ttk.Window('Formulario')
app.geometry('550x500')
style = Style('cyborg')

label = ttk.Label(app, text='Formulário de Inscrição')
label.pack(pady=35)
label.config(font=('Arial', 20, 'bold'))

Nome = ttk.Frame(app)
Nome.pack(pady=18, padx=10, fill='x')
ttk.Label(Nome, text='Nome').pack(side=LEFT, padx=5)
ttk.Entry(Nome).pack(side=LEFT, fill='x', expand=True, padx=5)

email = ttk.Frame(app)
email.pack(pady=18, padx=10, fill='x')
ttk.Label(email, text='Email').pack(side=LEFT, padx=5)
ttk.Entry(email).pack(side=LEFT, fill='x', expand=True, padx=5)

senha = ttk.Frame(app)
senha.pack(pady=18, padx=10, fill='x')
ttk.Label(senha, text='Senha').pack(side=LEFT, padx=5)
ttk.Entry(senha).pack(side=LEFT, fill='x', expand=True, padx=5)

checkbox = ttk.Frame(app)
checkbox.pack(pady=15, padx=10, fill='x')
ttk.Checkbutton(checkbox, bootstyle='round-toggle',
                text='Lembrar dados?').pack(side=LEFT, padx=15)

botao = ttk.Frame(app)
botao.pack(pady=30, padx=10, fill='x')
ttk.Button(botao, text='Enviar', bootstyle='SUCCESS').pack(side=LEFT, padx=15)
ttk.Button(botao, text='Cancelar', bootstyle='DANGER').pack(side=LEFT, padx=15)

app.mainloop()
