radio.set_group(69)
radio.set_transmit_power(7)
radio.set_transmit_serial_number(True)
my_serial = control.device_serial_number()

name= "vote"
name= "send"
number= 1
value= 0
list_of_votes= [0,0,0,0]
a = 0
b = 1
c = 2
d = 3
send_message = True

def dissable_client():
    if name == "send" and number == 0:
        radio.send_value("send", 1)
    else:
        radio.send_value("send", 0)
input.on_pin_pressed(TouchPin.P0, dissable_client)

def voting():
    global send_message
    basic.show_string("A")
    send_message = False
    basic.pause(100)
    send_message = True
    voted(0)
    basic.pause(500)
    basic.clear_screen()
input.on_button_pressed(Button.A, voting)

def voting_B():
    global send_message
    send_message = False
    basic.pause(100)
    send_message = True
    basic.show_string("B")
    voted(1)
    basic.pause(500)
    basic.clear_screen()
input.on_button_pressed(Button.B, voting_B)

def voting_C():
    global send_message
    send_message = False
    basic.pause(100)
    send_message = True
    basic.show_string("C")
    voted(2)
    basic.pause(500)
    basic.clear_screen()
input.on_logo_event(TouchButtonEvent.PRESSED, voting_C)

def voting_D():
    global send_message
    send_message = False
    basic.pause(100)
    send_message = True
    basic.show_string("D")
    voted(3)
    basic.pause(500)
    basic.clear_screen()
input.on_pin_pressed(TouchPin.P2, voting_D)

def voted(data):
    while send_message == True:
        global list_of_votes
        basic.pause(1500)
        radio.send_value("vote", data)
        list_of_votes[data] +=1
        print(list_of_votes)
        break

#list = [{"serial": "sériové číslo 1", "volba": 2},
#        {"serial": "sériové číslo 2", "volba": 1},
#        {"serial": "sériové číslo 1", "volba": 1},]
#list = [{"serial": 454, "volba": 2},
#        {"serial": "sériové číslo 2", "volba": 1},
#        {"serial": "sériové číslo 1", "volba": 1},]
#for vote in list:
#    def on_every(value, index):
#        return False
#    print(list.every(on_every))