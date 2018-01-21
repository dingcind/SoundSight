//
//  ServerCalls.m
//  SoundSight
//
//  Created by Morris Chen on 2018-01-20.
//  Copyright © 2018 Morris Chen. All rights reserved.
//

#import "NetworkManager.h"

#import "ServerCalls.h"

@implementation ServerCalls

+ (NSDictionary*) identifyImage:(NSString*)img {
    NSDictionary *inventory = @{
        @"img" : img
    };
    
    NSDictionary *data = [NetworkManager getDataFrom:@"http://34.214.105.118:80/main" postData:inventory];
//    NSString *callback = [data objectForKey:@"Callback"];
    
    NSLog(@"Callback: %@", data);
    
    return data;
}

@end
