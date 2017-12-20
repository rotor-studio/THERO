#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){
    

    ofBackground(0);
    //ofSetWindowShape(3840,1080);
    
   /* video.load("thero.mp4");
    video.setLoopState(OF_LOOP_NORMAL);
    video.play();*/
  
    full=true;
    
    ofHideCursor();

    //Objetos
    for(int i=0;i < 3;i++){
        object[i].setup("thero/", 4000+i,"  ",i);
    }
    
    //Roboto
    roboto.load("thero/font/Roboto-Bold.ttf", 20, true, true);
   
}

//--------------------------------------------------------------
void ofApp::update(){
    
  //  video.update();

    
    //Objetos
    for(int i=0;i < 3;i++){
    object[i].update();
    }
    
        
    
    ofSetFullscreen(full);
}

//--------------------------------------------------------------
void ofApp::draw(){
    
    ofSetColor(255);
    
    //video.draw(1920,0);
    
    
    ofPushMatrix();
    ofScale(0.7,0.7,0.7);
    ofTranslate(-object[0].img[0].getWidth()+120,ofGetWidth()/2- object[0].img[0].getHeight());
    
    for(int i=0;i < 3;i++){
    ofTranslate(object[0].img[0].getWidth()+100,0);
    object[i].draw();
    }
    
    ofPopMatrix();
    
    ofSetColor(255);
    //roboto.drawString("Puedes conectarte a cada una de los tres THEROS", 50,100);
    

}

//--------------------------------------------------------------
void ofApp::keyPressed(int key){
    
    if(key == 'f'){
        full=!full;
    }

}

//--------------------------------------------------------------
void ofApp::keyReleased(int key){

}

//--------------------------------------------------------------
void ofApp::mouseMoved(int x, int y ){

}

//--------------------------------------------------------------
void ofApp::mouseDragged(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mousePressed(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseReleased(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseEntered(int x, int y){

}

//--------------------------------------------------------------
void ofApp::mouseExited(int x, int y){

}

//--------------------------------------------------------------
void ofApp::windowResized(int w, int h){

}

//--------------------------------------------------------------
void ofApp::gotMessage(ofMessage msg){

}

//--------------------------------------------------------------
void ofApp::dragEvent(ofDragInfo dragInfo){ 

}
