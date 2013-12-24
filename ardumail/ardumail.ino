int val = 0; //value that is stored from Serial monitor
byte led = 13; //pin the led is connected to

void setup(){
 Serial.begin(9600); //begins Serial monitor
 pinMode(led, OUTPUT); //set led as an output
}

void loop(){
  if(Serial.available()) //check to see if Serial data is available
    val = Serial.read() - '0'; //store the numerical value
  digitalWrite(led, val); //write the value to the led
}
