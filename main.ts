radio.setGroup(69)
radio.setTransmitPower(7)
radio.setTransmitSerialNumber(true)
let my_serial = control.deviceSerialNumber()
let name = "vote"
name = "send"
let number = 1
let value = 0
let list_of_votes = [0, 0, 0, 0]
let a = 0
let b = 1
let c = 2
let d = 3
let send_message = true
input.onPinPressed(TouchPin.P0, function dissable_client() {
    if (name == "send" && number == 0) {
        radio.sendValue("send", 1)
    } else {
        radio.sendValue("send", 0)
    }
    
})
input.onButtonPressed(Button.A, function voting() {
    
    basic.showString("A")
    send_message = false
    basic.pause(100)
    send_message = true
    voted(0)
    basic.pause(500)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function voting_B() {
    
    send_message = false
    basic.pause(100)
    send_message = true
    basic.showString("B")
    voted(1)
    basic.pause(500)
    basic.clearScreen()
})
input.onLogoEvent(TouchButtonEvent.Pressed, function voting_C() {
    
    send_message = false
    basic.pause(100)
    send_message = true
    basic.showString("C")
    voted(2)
    basic.pause(500)
    basic.clearScreen()
})
input.onPinPressed(TouchPin.P2, function voting_D() {
    
    send_message = false
    basic.pause(100)
    send_message = true
    basic.showString("D")
    voted(3)
    basic.pause(500)
    basic.clearScreen()
})
function voted(data: number) {
    while (send_message == true) {
        
        basic.pause(1500)
        radio.sendValue("vote", data)
        list_of_votes[data] += 1
        console.log(list_of_votes)
        break
    }
}

