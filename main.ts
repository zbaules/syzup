let temp: number;
let ishere: number;
let work = true
let i = 1
while (work == true) {
    // boucle infini (avec possibilité de on/off)
    temp = pins.analogReadPin(AnalogPin.P2)
    // **** borne à trouver******# instancifie la variable analogique du capteur de température
    ishere = pins.digitalReadPin(DigitalPin.P8)
    // **** borne à trouver******# instancifie la variable digital/binaire du capteur de présence
    if (i % 2 == 0) {
        basic.showString("" + temp)
    } else if (ishere == 1) {
        basic.showIcon(IconNames.Yes)
    } else if (ishere == 0) {
        basic.showIcon(IconNames.No)
    }
    
    basic.pause(200)
    i += 1
    if (temp >= 20 && ishere == 1) {
        // si la température est supérieur ou égal à 20 et qu'il y a quelqu'un
        pins.digitalWritePin(DigitalPin.P0, 1)
    }
    
    // **** borne à trouvée******# #ventilo on
    if (ishere == 0) {
        pins.digitalWritePin(DigitalPin.P0, 0)
    }
    
    // système on/off (je suis pas sur du bouton donc faudra surement revoir)
}
