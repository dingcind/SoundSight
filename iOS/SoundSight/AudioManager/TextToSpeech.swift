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
    
    func speak(text: String, vol: Float, pos: Float){
        let speechSynthesizer = AVSpeechSynthesizer()
        let speechUtterance = AVSpeechUtterance(string: text)
        speechUtterance.volume = vol
        
        let channels = AVAudioSession.sharedInstance().currentRoute.outputs[0].channels
        print(type(of: channels![0]))
        
//        SetSpeechProperty(,kSpeechVolumeProperty)
//        speechSynthesizer.speak(speechUtterance)
        let alertSound = URL(fileURLWithPath: Bundle.main.path(forResource: "sample", ofType: "mp3")!)
        print(alertSound)
        
        try! AVAudioSession.sharedInstance().setCategory(AVAudioSessionCategoryPlayback)
        try! AVAudioSession.sharedInstance().setActive(true)
        
        do {
            let audioPlayer = try AVAudioPlayer(contentsOf: alertSound)
            audioPlayer.prepareToPlay()
            audioPlayer.play()
        } catch {
            print(error)
        }
    }
    
}
