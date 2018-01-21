//
//  ViewController.m
//  SoundSight
//
//  Created by Morris Chen on 2018-01-20.
//  Copyright © 2018 Morris Chen. All rights reserved.
//

#import <AVFoundation/AVFoundation.h>

#import "ViewController.h"

@interface ViewController () {
    AVAudioPlayer *_audioPlayer;
}
@end

@implementation ViewController

- (void) viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
    
    // Construct URL to sound file
    NSString *path = [NSString stringWithFormat:@"%@/sample.mp3", [[NSBundle mainBundle] resourcePath]];
    NSURL *soundUrl = [NSURL fileURLWithPath:path];
    
    // Create audio player object and initialize with URL to sound
    _audioPlayer = [[AVAudioPlayer alloc] initWithContentsOfURL:soundUrl error:nil];
    
    [self playWithPan:1.0f];
}


- (void) didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (BOOL) prefersStatusBarHidden {
    return YES;
}

- (void) playWithPan:(CGFloat)pan {
    [_audioPlayer setPan:pan];
    [_audioPlayer play];
}

@end
