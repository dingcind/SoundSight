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

class CameraViewController: UIViewController{

  let session = AVCaptureSession()
  var camera : AVCaptureDevice?
  var cameraPreviewLayer : AVCaptureVideoPreviewLayer?
  var cameraCaptureOutput : AVCapturePhotoOutput?


  override func viewDidLoad(){
    super.viewDidLoad()
    initializeCaptureSession()
    // additional setup
  }

  //this function is to display the photo captured
  func displayCapturedPhoto(capturedPhoto : UIImage){
    
  }

  func initializeCaptureSession(){
    session.sessionPreset = AVCaptureSessionPresetHigh
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

  func takePicture(){

    let settings = AVCapturePhotoSettings()
    settings.flashMode = .off //if this fails check camera settings for flash off


    cameraCaptureOutput?.capturePhoto(with: settings, delegate: self)

  }

  override func didReceiveMemoryWarning(){
    super.didReceiveMemoryWarning()

  }
}

extension ViewController : AVCapturePhotoCaptureDelegate{

  func capture(_ captureOutput: AVCapturePhotoOutput, didFinishProcessingPhotoSampleBuffer photoSampleBuffer: CMSampleBuffer?,
    previewPhotoSampleBuffer: CMSampleBuffer?, resolvedSettings: AVCaptureResolvedPhotoSettings, bracketSettings: AVCapureBracketedStillImageSettings?，error: Error?){

    if let unwrappedError = error {
      print(unwrappedError.localizedDescription)
    }
    else {

      if let sampleBuffer = photoSampleBuffer, let dataImage = AVCapturePhotoOutput.jpegPhotoDataRepresentation(forJPEGSampleBugger: sampleBuffer, previewPhotoSampleBuffer: previewPhotoSampleBuffer)
      {
        if let finalImage = UIImage(data: dataImage){

          //to do whatever with photo capture (aka send to quin)
          displayCapturedPhoto(capturedPhoto: finalImage)

        }
      }
    }
  }
}
