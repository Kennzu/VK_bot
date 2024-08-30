from vkbottle import Keyboard, KeyboardButtonColor, Callback, Text

def start_button():
    start_btn = Keyboard(one_time=True, inline=False)
    start_btn.add(Text("О нас"))
    start_btn.row()
    start_btn.add(Text("Наш сайт"))
    start_btn.add(Text("Контакты"))
    start_btn.row()
    start_btn.add(Text("Презентация компании"))
    return start_btn

def back_menu():
    menu_btn = Keyboard(one_time=False, inline=False)
    menu_btn.add(Text('Вернуться к главному меню'))
    menu_btn.row()
    menu_btn.add(Text('Закончить знакомство с компанией'))
    return menu_btn

def out_start():
    start_o_btn = Keyboard(one_time=True, inline=False)
    start_o_btn.add(Text('Начать'))
    return start_o_btn