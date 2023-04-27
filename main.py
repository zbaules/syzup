work=True
i=1
while work==True: #boucle infini (avec possibilité de on/off)
    temp= pins.analog_read_pin(AnalogPin.P2) #**** borne à trouver******# instancifie la variable analogique du capteur de température
    ishere= pins.digital_read_pin(DigitalPin.P8) #**** borne à trouver******# instancifie la variable digital/binaire du capteur de présence
    
    if i%2==0:
        basic.show_string(str(temp))
    else:
        if ishere==1:
            basic.show_icon(IconNames.YES)
        elif ishere==0:
            basic.show_icon(IconNames.NO)
    basic.pause(200)
    i+=1

    if temp >= 20 and ishere==1 :
         #si la température est supérieur ou égal à 20 et qu'il y a quelqu'un
        pins.digital_write_pin(DigitalPin.P0, 1) #**** borne à trouvée******# #ventilo on
    if ishere==0:
        pins.digital_write_pin(DigitalPin.P0, 0)


#système on/off (je suis pas sur du bouton donc faudra surement revoir)
    def on_button_pressed_a():
        if work==True:
            work==False
        else:
            work==True
        input.on_button_pressed(Button.A, on_button_pressed_a)

