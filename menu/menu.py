menu_options = {
    0: 'No AFK',
    1: 'AFK Mode',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

