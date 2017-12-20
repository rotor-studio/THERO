//
//  thero.cpp
//  THERO display
//
//  Created by Rotor on 30/11/2017.
//
//

#include "thero.h"


void thero::setup(string path, int _port, string _ip, int _id){
    
    port=_port;
    ip=_ip;
    id=_id;
    
    receiver.setup(port);
    
    for(int i=0;i < 4;i++){
        img[i].load(path+ofToString(i)+".jpg");
     
    }
    mode=0;
    state= "ESPERANDO...";
    
    
    //Roboto
    roboto.load(path+"/font/Roboto-Bold.ttf", 30, true, true);
    
}
void thero::update(){
    
    
    
    // hide old messages
    for(int i = 0; i < NUM_MSG_STRINGS; i++){
        if(timers[i] < ofGetElapsedTimef()){
            msg_strings[i] = "";
        }
    }
    
    // check for waiting messages
    while(receiver.hasWaitingMessages()){
        
        ofxOscMessage m;
        receiver.getNextMessage(m);
        
        
        //THERO
        if(m.getAddress() == "/THERO/"+ofToString(id)+"/INIT"){
            mode=0;
        }
        else if(m.getAddress() == "/THERO/"+ofToString(id)+"/ROJO"){
            mode=1;
        }
        else if(m.getAddress() == "/THERO/"+ofToString(id)+"/AZUL"){
            mode=2;
        }
        else if(m.getAddress() == "/THERO/"+ofToString(id)+"/VERDE" ){
            mode=3;
        }
        
        else{
            // unrecognized message: display on the bottom of the screen
            string msg_string;
            msg_string = m.getAddress();
            msg_string += ": ";
            for(int i = 0; i < m.getNumArgs(); i++){
                // get the argument type
                msg_string += m.getArgTypeName(i);
                msg_string += ":";
                // display the argument - make sure we get the right type
                if(m.getArgType(i) == OFXOSC_TYPE_INT32){
                    msg_string += ofToString(m.getArgAsInt32(i));
                }
                else if(m.getArgType(i) == OFXOSC_TYPE_FLOAT){
                    msg_string += ofToString(m.getArgAsFloat(i));
                }
                else if(m.getArgType(i) == OFXOSC_TYPE_STRING){
                    msg_string += m.getArgAsString(i);
                }
                else{
                    msg_string += "unknown";
                }
            }
            // add to the list of strings to display
            msg_strings[current_msg_string] = msg_string;
            timers[current_msg_string] = ofGetElapsedTimef() + 5.0f;
            current_msg_string = (current_msg_string + 1) % NUM_MSG_STRINGS;
            // clear the next line
            msg_strings[current_msg_string] = "";
        }
        
    }
    
    if(mode==0){
       state= "ESPERANDO...";
        col= ofColor(0,255,255);
    }
    if(mode==1){
        state= "SIN ENCRIPTACION";
        col= ofColor(255,0,0);
    }
    if(mode==2){
        state= "CONECTADO A LA RED TOR";
        col= ofColor(90,90,255);
    }
    if(mode==3){
        state= "BLACKOUT";
        col= ofColor(0,255,0);
    }
    

}
void thero::draw(){
    
    
    ofSetColor(255);
    img[mode].draw(0,100);
    
    ofSetColor(255);
    
    
    string puf;
    puf = "THERO_0"+ofToString(id)+" / ESTADO: "+state;
    ofDrawBitmapString(puf,50, img[mode].getHeight()+160);
    
    string buf;
    buf = "THERO_0"+ofToString(id)+" Esta enviando mensajes por el puerto " + ofToString(port);
    ofDrawBitmapString(buf, 50, img[mode].getHeight()+210);
    
    ofSetColor(col);
    for(int i = 0; i < NUM_MSG_STRINGS; i++){
        ofDrawBitmapString(msg_strings[i], 50, (img[mode].getHeight()+260)+ 12 * i);
    }

   ofSetColor(200);
   roboto.drawString("WIFI: THERO_0"+ofToString(id), 50,-50);
   roboto.drawString("PASSWORD: thero1010", 50,25);
    

}
