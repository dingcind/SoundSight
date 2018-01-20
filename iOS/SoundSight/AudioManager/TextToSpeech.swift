//
//  TextToSpeech.swift
//  SoundSight
//
//  Created by Morris Chen on 2018-01-20.
//  Copyright © 2018 Morris Chen. All rights reserved.
//

import Foundation
import AVFoundation

class TextToSpeech: NSObject{
    
    
    let speechSynthesizer = AVSpeechSynthesizer()
    
    func speak(text: String){
        let speechUtterance = AVSpeechUtterance(string: text)
        speechSynthesizer.speak(speechUtterance)
        
    }
    
}
