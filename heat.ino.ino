#include "dht.h"
#include <Arduino.h>
#define dht_apin A0 // Analog Pin sensor is connected to 
dht DHT;

int A_1 = 1;
 
void setup(){
 
  Serial.begin(9600);
  delay(500);//Delay to let system boot
  Serial.println("DHT11 Humidity & temperature Sensor\n\n");
  delay(1000);//Wait before accessing Sensor 
}//end "setup()"



 
void loop(){
  //Start of Program 

    int voltagePin = analogRead(1);
    //Serial.println(voltagePin);
    float voltage = voltagePin*(5/1024);
    float v1 = voltagePin*5;
    //Serial.println(v1);
    float v2 = v1/1024;
    Serial.println(v2);
    Serial.print("Voltage: ");
    Serial.print(v2);
    Serial.print("V ");
    //Serial.println(voltage);

 
    DHT.read11(dht_apin);
    
    Serial.print("Current humidity = ");
    Serial.print(DHT.humidity);
    Serial.print("%  ");
    Serial.print("temperature = ");
    Serial.print(DHT.temperature); 
    Serial.println("C  ");
    
    delay(1000);//Wait a seconds before accessing sensor again.
  //Fastest should be once every two seconds.
 
}// end loop()
