//
//  ViewController.swift
//  audio_stuff
//
//  Created by Anna on 2018-01-20.

import UIKit
import CoreMotion

class ViewController: UIViewController {
    let motionManager = CMMotionManager()
    var timer: Timer!
    
    struct Item : Codable {
        var name: String
        var pos: Float
        var size: Float
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        motionManager.startGyroUpdates()
        timer = Timer.scheduledTimer(timeInterval: 3.0, target: self, selector: #selector(ViewController.update), userInfo: nil, repeats: true)
    }
    
    @objc func update() {
        let environment = [Item]()
        let jsonString = """
[
    {
        "left": 1.3,
        "right": 8.9
    }
]
""".data(using: .utf8)!
        let urlString = URL(string: "http://34.214.105.118:80/get_example")
        if let url = urlString {
            let task = URLSession.shared.dataTask(with: url) { (data, response, error) in
                if error != nil {
                    print(error)
                } else {
                    if let usableData = data {
                        let string = String(data: usableData, encoding: String.Encoding.utf8)
                        print(string) //JSONSerialization
                    }
                }
            }
            task.resume()
        }
        
        if let gyroData = motionManager.gyroData {
            print("SOMETHING")
            print(gyroData)
        }
    }
}
