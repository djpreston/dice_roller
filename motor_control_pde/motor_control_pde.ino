/*
 Dice Roller 
 */

const int motorSpeed = 3;      // the pin that controls motor A speed
String inString = "";    // string to hold input
void setup()
{
  // initialize the serial communication:
  Serial.begin(9600);
  pinMode(12, OUTPUT); //Initiates Motor Channel A pin
  pinMode(9, OUTPUT); //Initiates Brake Channel A pin
  analogWrite(motorSpeed, 0);
}

void loop() {
  int speedCommand;
   // Read serial input:
  while (Serial.available() > 0) {
    int inChar = Serial.read();
    if (isDigit(inChar)) {
      // convert the incoming byte to a char 
      // and add it to the string:
      inString += (char)inChar; 
    }
    // if you get a newline, print the string,
    // then the string's value:
    if (inChar == '\n') {
      Serial.print("Value:");
      Serial.println(inString.toInt());
      speedCommand = inString.toInt();
      Serial.print("String: ");
      Serial.println(inString);
      // clear the string for new input:
      inString = ""; 
      // set the motor speed:
      analogWrite(motorSpeed, speedCommand);
    }
  }
    
  }

