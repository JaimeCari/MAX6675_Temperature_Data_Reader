#include "max6675.h"
#include <Servo.h>

int SO_PIN = 10;
int CS_PIN = 11;
int SCK_PIN = 12;

MAX6675 termocupla(SCK_PIN, CS_PIN, SO_PIN);

int SERVO_PIN = 9;
Servo myservo;

const int SERVO_OPEN_POS = 0;
const int SERVO_CLOSE_POS = 90;

void setup() {
  Serial.begin(9600);
  myservo.attach(SERVO_PIN);
  myservo.write(SERVO_CLOSE_POS);
  Serial.println("Arduino listo para recibir comandos (T, O, C).");
}

void loop() {
  if (Serial.available()) {
    char command = Serial.read();
    if (command == 'T') {
      double temperaturaC = termocupla.readCelsius();
      if (isnan(temperaturaC)) {
        Serial.println("Error de lectura de termocupla!");
      } else {
        Serial.print("Temp:");
        Serial.println(temperaturaC, 2);
      }
    } else if (command == 'O') {
      myservo.write(SERVO_OPEN_POS);
    } else if (command == 'C') {
      myservo.write(SERVO_CLOSE_POS);
    }
  }
}
