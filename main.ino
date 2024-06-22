const int redPin = 9;
const int greenPin = 10;
const int bluePin = 11;

void setup() {
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  Serial.begin(9600); 
}

void loop() {
  if (Serial.available() >= 3) { 
    int redValue = Serial.read();
    int greenValue = Serial.read(); 
    int blueValue = Serial.read(); 
    
    setColor(redValue, greenValue, blueValue); 
  }
}


void setColor(int redValue, int greenValue, int blueValue) {
  analogWrite(redPin, redValue);
  analogWrite(greenPin, greenValue);
  analogWrite(bluePin, blueValue);
}
