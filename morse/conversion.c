char* morseLetras[] = {
".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", // a-i 
".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", // j-r 
"...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.." // s-z
};

int retardoPunto = 200;
int retardoRaya  = retardoPunto*3;

void setup() {
  //Configurar pines de salida

  Serial.begin(9600);

}

void loop() {
  //Completar código adecuadamente
  char ch;
  String ch_morse;
  
  int ch_valor;
  
  if (Serial.available()){
    ch = Serial.read();

    ch_valor = ch;
    
    Serial.print(ch);
    Serial.print(" ");
    if(ch_valor == 32){
      Serial.println("Espacio");
    }
    else{
      ch_morse = morseLetras[ch_valor - 97];
      Serial.println(ch_morse);
    }

   
  }
}


void secuencia(char* secuenciaMorse){
  //Completar código adecuadamente


}

void parpadeoPuntoRaya(char puntoRaya){
  //Completar código adecuadamente
}

void parpadeoEspacio(){
  //Completar código adecuadamente
}
