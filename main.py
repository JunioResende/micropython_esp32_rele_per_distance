import machine
import time

# Pinagem
rele = machine.Pin(13, machine.Pin.OUT)
trig_pin = machine.Pin(12, machine.Pin.OUT)
echo_pin = machine.Pin(14, machine.Pin.IN)


# Função para medir a distância
def measure_distance():
    trig_pin.off()
    time.sleep_us(2)
    trig_pin.on()
    time.sleep_us(10)
    trig_pin.off()

    pulse_duration = machine.time_pulse_us(echo_pin, 1, 30000)
    distance = (pulse_duration / 2) * 34300 / 1000000

    return distance


while True:
    # Faz a leitura da distância e imprime no terminal
    print("Distancia:", measure_distance(), "cm")
    time.sleep(0.5)

    # aciona um rele se a distância for menor que 20cm
    if measure_distance() < 20:
        rele.on()
    else:
        rele.off()
