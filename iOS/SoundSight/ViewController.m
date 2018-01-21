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
    NSString *path = [NSString stringWithFormat:@"%@/cena.mp3", [[NSBundle mainBundle] resourcePath]];
    NSURL *soundUrl = [NSURL fileURLWithPath:path];
    
    // Create audio player object and initialize with URL to sound
    _audioPlayer = [[AVAudioPlayer alloc] initWithContentsOfURL:soundUrl error:nil];
}


- (void) didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (BOOL) prefersStatusBarHidden {
    return YES;
}

- (void) playWithPan:(CGFloat)pan {
    [_audioPlayer stop];
    [_audioPlayer setPan:pan];
    [_audioPlayer prepareToPlay];
    _audioPlayer.currentTime = 0;
    [_audioPlayer play];
}

@end
