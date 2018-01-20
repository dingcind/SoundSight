//
//  NetworkManager.h
//  SoundSight
//
//  Created by Morris Chen on 2018-01-20.
//  Copyright © 2018 Morris Chen. All rights reserved.
//

#ifndef NetworkManager_h
#define NetworkManager_h

#import <UIKit/UIKit.h>

@protocol NetworkManager <NSObject>

@optional
- (void) data:(NSDictionary*)data;
- (void) videoData:(NSData*)data;
- (void) noConnection;
- (void) connectionError;

@end

@interface NetworkManager: NSObject {
    id delegate_;
}

+ (NSDictionary*) getDataFrom:(NSString*)url postData:(NSDictionary*)temp;
+ (NSDictionary*) getDataFrom:(NSString*)url;
+ (UIImage*) getPictureFrom:(NSString*)url;
+ (void) getAsyncData:(NSString*)url delegateParam:(id<NetworkManager>)delegate;
+ (void) getVideoAsyncData:(NSString*)url delegateParam:(id<NetworkManager>)delegate;
+ (void) getAsyncData:(NSString*)url withPostData:(NSDictionary*)data delegateParam:(id<NetworkManager>)delegate;

@end

#endif /* NetworkManager_h */
