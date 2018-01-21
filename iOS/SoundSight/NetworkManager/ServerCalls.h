//
//  ServerCalls.h
//  SoundSight
//
//  Created by Morris Chen on 2018-01-20.
//  Copyright © 2018 Morris Chen. All rights reserved.
//

#ifndef ServerCalls_h
#define ServerCalls_h

@interface ServerCalls: NSObject

+ (NSDictionary*) identifyImage:(NSString*)img angle:(CGFloat)theta;
+ (NSDictionary*) voiceOutput:(NSString*)str;

@end

#endif /* ServerCalls_h */
