agenda = {
    'samanta': {
        'tel': '99999-8888',
        'email': 'samanta@gmail.com',
        'endereço': 'Avenida 01'
    },
    'juliana': {
        'tel': '99999-8888',
        'email': 'samanta@gmail.com',
        'endereço': 'Avenida 01'
    },
   'joao': {
        'tel': '99999-8888',
        'email': 'samanta@gmail.com',
        'endereço': 'Avenida 01'
    },

}

agenda['samanta'] ['endereço'] = 'Avenida 04' #ALTERAR DADOS

agenda ['iury'] = {
        'tel': '99999-8555',
        'email': 'iury@gmail.com', #INCLUIR CONTATOS
        'endereço': 'Avenida 05'
}

agenda.pop('joão') #REMOVER CONTATO

for contato in agenda: #MOSTRAR TODOS
    print(contato)

print(agenda['samanta']['endereço']) #MOSTRAR ITEM ESPECIFICO



