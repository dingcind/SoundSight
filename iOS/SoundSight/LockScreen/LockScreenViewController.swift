//
//  LockScreenViewController.swift
//  SpyderWeb
//
//  Created by Morris Chen on 2017-09-19.
//  Copyright © 2017 Morris Chen. All rights reserved.
//

import UIKit
import SpriteKit
import GameplayKit

class LockScreenViewController:ViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let skView = SKView.init(frame:self.view.frame)
        self.view = skView
        
        if let view = self.view as! SKView? {
            // Load the SKScene from 'LockScreenScene.sks'
            if let scene = SKScene(fileNamed:"LockScreenScene") {
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
        return true
    }
    
    override var supportedInterfaceOrientations: UIInterfaceOrientationMask {
        if UIDevice.current.userInterfaceIdiom == .phone {
            return .allButUpsideDown
        } else {
            return .all
        }
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Release any cached data, images, etc that aren't in use.
    }
    
    override var prefersStatusBarHidden: Bool {
        return true
    }
}
