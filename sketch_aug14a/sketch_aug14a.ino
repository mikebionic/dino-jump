int jump_state = 0;
int jump_button = 7;

int led = 13;

void setup() {
  Serial.begin(9600);
  pinMode(jump_button, INPUT);
  pinMode(led, OUTPUT);
}

void loop() {
  jump_state = digitalRead(jump_button);
  if (jump_state == 1){
    Serial.print('1');
    digitalWrite(led, 1);
    delay(500);
  }
  digitalWrite(led, 0);
  //Serial.println(jump_state);
}
