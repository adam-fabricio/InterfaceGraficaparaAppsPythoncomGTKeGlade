# coding-utf-8
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class User():
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

class Manipulador(object):
    def __init__(self):
        self.stack = Builder.get_object('stack')
        self.bancoDeDados = []
        self.modeloArmazenamento = Builder.get_object('liststore1')
    
    def on_mainWindow_destroy(self, window):
        Gtk.main_quit()
      
    def on_buttonLogin_clicked(self, button):
        email = Builder.get_object("email").get_text()
        senha = Builder.get_object("senha").get_text()
        lembrar = Builder.get_object('lembrar').get_active()
        self.login(email, senha, lembrar)
    
    def login(self, email, senha, lembrar):
        if email == 'admin' and senha == 'admin':
            self.mensagem('Bem-vindo', "Usuário logado com sucesso!", 
                          "emblem-default")
            self.stack.set_visible_child_name('viewInicial')
            window.props.icon_name = 'avatar-default'
            
        else:
            self.mensagem("Aviso", "Email ou senha incorreto", 
                          "dialog-error")
        
    def mensagem(self, tipo, texto, icone):
        mensagem = Builder.get_object("mensagem")
        mensagem.props.text = tipo
        mensagem.props.secondary_text = texto
        mensagem.props.icon_name = icone
        mensagem.show_all()
        mensagem.run()
        mensagem.hide()
    
    def on_buttonCadastrarInicial_clicked(self, button):
        self.stack.set_visible_child_name('viewCadastro')

    def on_buttonCadastrarVoltar_clicked(self, button):
        self.stack.set_visible_child_name('viewInicial')

    def on_buttonListarVoltar_clicked(self, button):
        self.stack.set_visible_child_name('viewInicial')
        
    def on_buttonListarInicial_clicked(self, button):
        self.stack.set_visible_child_name('viewListar')
        
    def on_botaoSairInicial_clicked(self, button):
        self.stack.set_visible_child_name('viewLogin')
        
    def on_buttonCadastrar_clicked(self, button):
        nome = Builder.get_object("cadNome").get_text()
        email = Builder.get_object("cadEmail").get_text()
        
        if nome != '':
            self.bancoDeDados.append(User(len(self.bancoDeDados),
                                          nome, email))
            self.mensagem('Aviso', 'Usuário ' + nome + ' cadastrado!',
                          "emblem-default")
        else:
            self.mensagem('Aviso', 'Campo nome é obrigatório',
                          'dialog-error')
    
    def on_buttonListar_clicked(self, button):
        self.modeloArmazenamento.clear()
        for user in self.bancoDeDados:
            self.modeloArmazenamento.append((user.id, user.nome,
                                             user.email))
    
    
Builder = Gtk.Builder()
Builder.add_from_file("user_interface.glade")
Builder.connect_signals(Manipulador())
window = Builder.get_object("mainWindow")
window.show_all()
Gtk.main()