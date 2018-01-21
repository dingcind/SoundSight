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

class CameraViewController: ViewController {
    
  let session = AVCaptureSession()
  var camera : AVCaptureDevice?
  var cameraPreviewLayer : AVCaptureVideoPreviewLayer?
  var cameraCaptureOutput : AVCapturePhotoOutput?
    var ready = true;

    var textToSpeech: TextToSpeech!
    var player: AVAudioPlayer?
    
  override func viewDidLoad(){
    super.viewDidLoad()
    initializeCaptureSession()
    
    Timer.scheduledTimer(withTimeInterval: 5, repeats: true, block: {
        (timer) in
        if(self.ready) {
            self.takePicture()
        }
    })
    // additional setup
  }

  //this function is to display the photo captured
  func processCapturedPhoto(capturedPhoto : UIImage){
    let imageData = UIImageJPEGRepresentation(capturedPhoto, 1)
    let strBase64 = imageData?.base64EncodedString(options: .lineLength64Characters)
    ready = false
    let callback = ServerCalls.identifyImage(strBase64) as NSDictionary
    ready = true
    makeSound(data: callback)
  }
    
    func makeSound(data: NSDictionary) {
        // TODO: Sound off
        textToSpeech = TextToSpeech(
            username: "82fd2c0c-c897-4d91-af44-2d97e4fa3e5c",
            password: "Zep7qdsmC7yP"
        )
        
        let text = "Make America Great Again";
        let voice = "en-US_AllisonVoice";
        
        let failure = { (error: Error) in print(error) }
        textToSpeech.synthesize(
            text,
            voice: voice,
            audioFormat: .wav,
            failure: failure)
        {
            data in
            do {
                self.player = try AVAudioPlayer(data: data)
                self.player!.pan = -0.7;
                self.player!.volume = 1;
                self.player!.play()
            } catch {
                print("Failed to create audio player.")
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

    cameraPreviewLayer = AVCaptureVideoPreviewLayer(session: session)
//    cameraPreviewLayer?.videoGravity = AVLayerVideoGravityAspectFill
    cameraPreviewLayer?.frame = view.bounds
    
    cameraPreviewLayer?.connection.videoOrientation = AVCaptureVideoOrientation.portrait

    view.layer.insertSublayer(cameraPreviewLayer!, at: 0)

    session.startRunning()

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
