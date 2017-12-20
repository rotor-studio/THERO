//
//  thero.hpp
//  THERO display
//
//  Created by Rotor on 30/11/2017.
//
//
#include "ofMain.h"
#include "ofxOsc.h"
#define NUM_MSG_STRINGS 2

class thero{

public:

void setup(string path, int _port, string _ip, int _id);
void update();
void draw();
    
    
    ofxOscReceiver receiver;
    int port;
    string ip;
    int id;
    
    int current_msg_string;
    string msg_strings[NUM_MSG_STRINGS];
    float timers[NUM_MSG_STRINGS];
    

    
    ofImage img[4];
    int mode;
    string state;
    ofColor col;

    ofTrueTypeFont	roboto;
    
};
