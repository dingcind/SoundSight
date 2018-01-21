//
//  CameraViewController.swift
//  SoundSight
//
//  Created by Morris Chen on 2018-01-20.
//  Copyright © 2018 Morris Chen. All rights reserved.
//
import Foundation

import UIKit
import AVFoundation
import TextToSpeechV1
import CoreMotion

class CameraViewController: ViewController {
    
    let session = AVCaptureSession()
    var camera : AVCaptureDevice?
    var cameraPreviewLayer : AVCaptureVideoPreviewLayer?
    var cameraCaptureOutput : AVCapturePhotoOutput?
    var ready = true;
    var scene : LockScreenScene?
    
    var textToSpeech: TextToSpeech!
    var player: AVAudioPlayer?
    
    override func viewDidLoad(){
        super.viewDidLoad()
        initializeCaptureSession()
        
        Timer.scheduledTimer(withTimeInterval: 3, repeats: true, block: { //was 5
            (timer) in
            if(self.ready) {
                self.takePicture()
            }
        })
        // additional setup
        self.takePicture()
        gyroScope()
        
        
        let skView = SKView.init(frame:self.view.frame)
        self.view = skView
        
        if let view = self.view as! SKView? {
            // Load the SKScene from 'LockScreenScene.sks'
            if let scene = SKScene(fileNamed:"LockScreenScene") {
                self.scene = scene as! LockScreenScene
                // Set the scale mode to scale to fit the window
                scene.scaleMode = .aspectFill
                
                // Present the scene
                view.presentScene(scene)
            }
            
            view.ignoresSiblingOrder = true
            
            view.showsFPS = false
            view.showsNodeCount = false
        }
    }
    
    override var shouldAutorotate: Bool {
        return false
    }
    
    //this function is to display the photo captured
    func processCapturedPhoto(capturedPhoto : UIImage){
        let imageData = UIImageJPEGRepresentation(capturedPhoto, 1)
        let strBase64 = imageData?.base64EncodedString(options: .lineLength64Characters)
        ready = false
        let callback = ServerCalls.identifyImage(strBase64,angle:CGFloat(self.deltaTheta)) as NSDictionary
        self.deltaTheta = 0.0
        ready = true
        makeSound(data: callback)
    }
    
    func makeSound(data: NSDictionary) {
        // TODO: Sound off
        
        textToSpeech = TextToSpeech(
            username: "82fd2c0c-c897-4d91-af44-2d97e4fa3e5c",
            password: "Zep7qdsmC7yP"
        )
        
        if(data.object(forKey: "data") == nil) {
            return
        }
        
        let arr = data.object(forKey: "data") as! NSArray
        
        for item in arr {
            let dict = item as! NSDictionary
            print(dict)
            let name = dict.object(forKey: "name") as! String
            
            self.scene?.setLabel(text: name);
            
            print(name)
            var pos = dict.object(forKey: "pos") as! Float
            //print(pos)
            let size = dict.object(forKey: "size") as! Float
            //print(size)
            
            let voice = "en-US_AllisonVoice";
            
            let failure = { (error: Error) in print(error) }
            textToSpeech.synthesize(
                name,
                voice: voice,
                audioFormat: .wav,
                failure: failure)
            {
                data in
                do {
                    self.player = try AVAudioPlayer(data: data)
                    self.player!.rate = 2
                    if pos > 0 {pos = min(2*pos,1)}
                    else {pos = max(2*pos,-1)}
                    self.player!.pan = pos
                    print(self.player!.pan)
                    self.player!.volume = 0.7*size+0.3
                    self.player!.play()
                    while(self.player!.isPlaying){
                    }
                    
                } catch {
                    print("Failed to create audio player.")
                }
            }
        }
        
    }
    
    func initializeCaptureSession(){
        session.sessionPreset = AVCaptureSessionPresetMedium
        camera = AVCaptureDevice.defaultDevice(withMediaType: AVMediaTypeVideo)
        
        do{
            let cameraCaptureInput = try AVCaptureDeviceInput(device: camera!)
            cameraCaptureOutput = AVCapturePhotoOutput()
            
            session.addInput(cameraCaptureInput)
            session.addOutput(cameraCaptureOutput)
            
        } catch {
            print(error.localizedDescription)
        }
        
        //cameraPreviewLayer = AVCaptureVideoPreviewLayer(session: session)
        //    cameraPreviewLayer?.videoGravity = AVLayerVideoGravityAspectFill
        //cameraPreviewLayer?.frame = view.bounds
        
        //cameraPreviewLayer?.connection.videoOrientation = AVCaptureVideoOrientation.portrait
        
        //view.layer.insertSublayer(cameraPreviewLayer!, at: 0)
        
        session.startRunning()
        
    }
    
    var motionManager = CMMotionManager()
    var prevY = 0.0
    var deltaTheta = 0.0
    
    func gyroScope(){
        motionManager.gyroUpdateInterval = 1.0/60.0
        motionManager.startGyroUpdates(to: OperationQueue.current!){(data, error) in
            if let myData = data{
                let y = myData.rotationRate.y
                self.deltaTheta += (self.prevY+y)/120
                self.prevY = y
//                print(self.deltaTheta)
            }
            
        }
        
    }
    
    func takePicture() {
        let settings = AVCapturePhotoSettings()
        settings.flashMode = .off //if this fails check camera settings for flash off
        cameraCaptureOutput?.capturePhoto(with: settings, delegate: self)
        
    }
    
    override func didReceiveMemoryWarning(){
        super.didReceiveMemoryWarning()
        
    }
}

extension CameraViewController : AVCapturePhotoCaptureDelegate{
    
    func capture(_ captureOutput: AVCapturePhotoOutput, didFinishProcessingPhotoSampleBuffer photoSampleBuffer: CMSampleBuffer?, previewPhotoSampleBuffer: CMSampleBuffer?, resolvedSettings: AVCaptureResolvedPhotoSettings, bracketSettings: AVCaptureBracketedStillImageSettings?,error: Error?){
        
        if let unwrappedError = error {
            print(unwrappedError.localizedDescription)
        }
        else {
            
            if let sampleBuffer = photoSampleBuffer, let dataImage = AVCapturePhotoOutput.jpegPhotoDataRepresentation(forJPEGSampleBuffer: sampleBuffer, previewPhotoSampleBuffer: previewPhotoSampleBuffer)
            {
                if let finalImage = UIImage(data: dataImage){
                    
                    //to do whatever with photo capture (aka send to quin)
                    processCapturedPhoto(capturedPhoto: finalImage)
                    
                }
            }
        }
    }
}

////
////  CameraViewController.swift
////  SoundSight
////
////  Created by Morris Chen on 2018-01-20.
////  Copyright © 2018 Morris Chen. All rights reserved.
////
//
//import Foundation
//
//import UIKit
//import AVFoundation
//import TextToSpeechV1
//import CoreMotion
//
//class CameraViewController: ViewController{
//
//  let session = AVCaptureSession()
//  var camera : AVCaptureDevice?
//  var cameraPreviewLayer : AVCaptureVideoPreviewLayer?
//  var cameraCaptureOutput : AVCapturePhotoOutput?
//    var ready = true;
//
//    var textToSpeech: TextToSpeech!
//    var player: AVAudioPlayer?
//
//  override func viewDidLoad(){
//    super.viewDidLoad()
//    initializeCaptureSession()
//    // additional setup
//  }
//
//  //this function is to display the photo captured
//  func processCapturedPhoto(capturedPhoto : UIImage){
//    let imageData = UIImageJPEGRepresentation(capturedPhoto, 1)
//    let strBase64 = imageData?.base64EncodedString(options: .lineLength64Characters)
//    ready = false
//    let callback = ServerCalls.identifyImage(strBase64) as NSDictionary
//    ready = true
//    makeSound(data: callback)
//  }
//
//    func makeSound(data: NSDictionary) {
//        // TODO: Sound off
//        textToSpeech = TextToSpeech(
//            username: "82fd2c0c-c897-4d91-af44-2d97e4fa3e5c",
//            password: "Zep7qdsmC7yP"
//        )
//
//        let text = "Make America Great Again";
//        let voice = "en-US_AllisonVoice";
//
//        let failure = { (error: Error) in print(error) }
//        textToSpeech.synthesize(
//            text,
//            voice: voice,
//            audioFormat: .wav,
//            failure: failure)
//        {
//            data in
//            do {
//                self.player = try AVAudioPlayer(data: data)
//                self.player!.pan = -0.7;
//                self.player!.volume = 1;
//                self.player!.play()
//            } catch {
//                print("Failed to create audio player.")
//            }
//        }
//
//  }
//
//  func initializeCaptureSession(){
//    session.sessionPreset = AVCaptureSessionPresetHigh
//    camera = AVCaptureDevice.defaultDevice(withMediaType: AVMediaTypeVideo)
//
//    do{
//      let cameraCaptureInput = try AVCaptureDeviceInput(device: camera!)
//      cameraCaptureOutput = AVCapturePhotoOutput()
//
//      session.addInput(cameraCaptureInput)
//      session.addOutput(cameraCaptureOutput)
//
//    } catch {
//      print(error.localizedDescription)
//    }
//
//    cameraPreviewLayer = AVCaptureVideoPreviewLayer(session: session)
////    cameraPreviewLayer?.videoGravity = AVLayerVideoGravityAspectFill
//    cameraPreviewLayer?.frame = view.bounds
//    cameraPreviewLayer?.connection.videoOrientation = AVCaptureVideoOrientation.portrait
//
//    view.layer.insertSublayer(cameraPreviewLayer!, at: 0)
//
//    session.startRunning()
//
//  }
//
//  func takePicture(){
//
//    let settings = AVCapturePhotoSettings()
//    settings.flashMode = .off //if this fails check camera settings for flash off
//    settings
//
//
//    cameraCaptureOutput?.capturePhoto(with: settings, delegate: self)
//
//  }
//
//  var deltaTheta = 0.0
//  var previousY = 0.0
//
//  var motionManager = CMMotionManager()
//
//  func startGyros() {
//    deltaTheta = 0.0
//    previousY = 0.0
//
//     if motionManager.isGyroAvailable {
//        motionManager.gyroUpdateInterval = 1.0 / 60.0
//        motionManager.startGyroUpdates(to: OperationQueue.current!){ (data, error) in
//            if let myData = data{
//                print(myData.rotationRate)
//            }
///*
//            }
//
//        // Configure a timer to fetch the accelerometer data.
//        .timer = Timer(fire: Date(), interval: (1.0/60.0),
//               repeats: true, block: { (timer) in
//           // Get the gyro data.
//           if let data = self.motion.gyroData {
//              let y = data.rotationRate.y
//
//              // integrate y to get delta theta
//              deltaTheta += (y+previousY)/2*60
//              previousY = y
//           }
//        })
//
//        // Add the timer to the current run loop.
//        RunLoop.current.add(self.timer!, forMode: .defaultRunLoopMode)*/
//     }
//  }
///*
//  func stopGyros() {
//     if self.timer != nil {
//        self.timer?.invalidate()
//        self.timer = nil
//
//        self.motion.stopGyroUpdates()
//     }
//  }
//*/
//  override func didReceiveMemoryWarning(){
//    super.didReceiveMemoryWarning()
//
//  }
//}
//
//extension CameraViewController : AVCapturePhotoCaptureDelegate{
//
//  func capture(_ captureOutput: AVCapturePhotoOutput, didFinishProcessingPhotoSampleBuffer photoSampleBuffer: CMSampleBuffer?,
//    previewPhotoSampleBuffer: CMSampleBuffer?, resolvedSettings: AVCaptureResolvedPhotoSettings, bracketSettings: AVCapureBracketedStillImageSettings?，error: Error?){
//
//    if let unwrappedError = error {
//      print(unwrappedError.localizedDescription)
//    }
//    else {
//
//      if let sampleBuffer = photoSampleBuffer, let dataImage = AVCapturePhotoOutput.jpegPhotoDataRepresentation(forJPEGSampleBugger: sampleBuffer, previewPhotoSampleBuffer: previewPhotoSampleBuffer)
//      {
//        if let finalImage = UIImage(data: dataImage){
//
//          //to do whatever with photo capture (aka send to quin)
//          displayCapturedPhoto(capturedPhoto: finalImage)
//
//        }
//      }
//    }
//  }
//}

