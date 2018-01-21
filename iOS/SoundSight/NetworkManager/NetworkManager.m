//
//  NetworkManager.m
//  SoundSight
//
//  Created by Morris Chen on 2018-01-20.
//  Copyright © 2018 Morris Chen. All rights reserved.
//

#import <Foundation/Foundation.h>

#import "NetworkManager.h"

@implementation NetworkManager

+ (NSDictionary *) getDataFrom:(NSString *)url postData:(NSDictionary*)temp {
    
    NSError *error = [[NSError alloc] init];
    NSData *postData = [NSJSONSerialization dataWithJSONObject:temp options:0 error:&error];
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc] init];
    [request setHTTPMethod:@"POST"];
    [request setHTTPBody:postData];
    [request setURL:[NSURL URLWithString:url]];
    
    NSHTTPURLResponse *responseCode = nil;
    
    NSData *oResponseData = [NSURLConnection sendSynchronousRequest:request returningResponse:&responseCode error:&error];
    
    if([responseCode statusCode] != 200){
        NSDictionary *dict = [[NSDictionary alloc] initWithObjectsAndKeys:@"No connection", @"Callback", nil];
        
        return dict;
    }
    //    //nslog([[NSString alloc] initWithData:oResponseData encoding:NSUTF8StringEncoding]);
    //    NSError *jsonError = nil;
    
    NSDictionary *res = [NSJSONSerialization JSONObjectWithData:oResponseData options:NSJSONReadingMutableLeaves || NSJSONReadingMutableContainers error:nil];
    
    //    [NSString stringWithFormat:@"%d", (int)[responseCode statusCode]]
    //    add key to dictionary
    
    //    id jsonObject = [NSJSONSerialization JSONObjectWithData:jsonData options:kNilOptions error:&jsonError];
    
    return res;
}

+ (NSDictionary *) getDataFrom:(NSString *)url postData:(NSDictionary*)temp {
    
    NSError *error = [[NSError alloc] init];
    NSData *postData = [NSJSONSerialization dataWithJSONObject:temp options:0 error:&error];
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc] init];
    [request setHTTPMethod:@"POST"];
    [request setHTTPBody:postData];
    [request setURL:[NSURL URLWithString:url]];
    
    NSHTTPURLResponse *responseCode = nil;
    
    NSData *oResponseData = [NSURLConnection sendSynchronousRequest:request returningResponse:&responseCode error:&error];
    
    if([responseCode statusCode] != 200){
        NSDictionary *dict = [[NSDictionary alloc] initWithObjectsAndKeys:@"No connection", @"Callback", nil];
        
        return dict;
    }
    //    //nslog([[NSString alloc] initWithData:oResponseData encoding:NSUTF8StringEncoding]);
    //    NSError *jsonError = nil;
    
    NSDictionary *res = [NSJSONSerialization JSONObjectWithData:oResponseData options:NSJSONReadingMutableLeaves || NSJSONReadingMutableContainers error:nil];
    
    //    [NSString stringWithFormat:@"%d", (int)[responseCode statusCode]]
    //    add key to dictionary
    
    //    id jsonObject = [NSJSONSerialization JSONObjectWithData:jsonData options:kNilOptions error:&jsonError];
    
    return res;
}

+ (NSDictionary*) getDataFrom:(NSString*)url {
    //nslog(@"whyyyy");
    NSMutableDictionary *temp = [[NSMutableDictionary alloc]init];
    
    NSError *error = [[NSError alloc] init];
    NSData *postData = [NSJSONSerialization dataWithJSONObject:temp options:0 error:&error];
    
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc] init];
    [request setHTTPMethod:@"GET"];
    //    [request setHTTPBody:postData];
    [request setURL:[NSURL URLWithString:url]];
    
    NSHTTPURLResponse *responseCode = nil;
    
    NSData *oResponseData = [NSURLConnection sendSynchronousRequest:request returningResponse:&responseCode error:&error];
    
    if([responseCode statusCode] != 200){
        return nil;
    }
    
    //NSError *jsonError = nil;
    
    NSDictionary *res  = [NSJSONSerialization JSONObjectWithData:oResponseData options:NSJSONReadingMutableLeaves|| NSJSONReadingMutableContainers error:nil];
    //id jsonObject = [NSJSONSerialization JSONObjectWithData:jsonData options:kNilOptions error:&jsonError];
    
    return res;
}

+ (UIImage *) getPictureFrom:(NSString *)url {
    NSMutableURLRequest *request = [NSMutableURLRequest requestWithURL:[NSURL URLWithString:url]];
    NSData *imageData = [NSURLConnection sendSynchronousRequest:request returningResponse:nil error:nil];
    NSError *error = [[NSError alloc] init];
    NSHTTPURLResponse *responseCode = nil;
    
    //NSData *imageData = [NetworkManager sendSynchronousRequest:request returningResponse:&responseCode error:&error];
    
    UIImage *image = [UIImage imageWithData:imageData];
    /*NSURL *imageURL = [NSURL URLWithString:url];
     NSData *imageData = [NSData dataWithContentsOfURL:imageURL];
     UIImage *profileImage = [UIImage imageWithData:imageData];*/
    
    return image;
}


+ (void) getAsyncData:(NSString *)url delegateParam:(id<NetworkManager>)delegate {
    
    NSMutableURLRequest *request = [NSMutableURLRequest requestWithURL:[NSURL URLWithString:url]];
    
    NSURLSessionDataTask *task =
    [[NSURLSession sharedSession] dataTaskWithRequest:request
                                    completionHandler:^(NSData *data,
                                                        NSURLResponse *response,
                                                        NSError *error) {
                                        
                                        if(!response){
                                            NSLog(@"%@",data);
                                            if ([delegate respondsToSelector:@selector(noConnection)]) {
                                                [delegate noConnection];
                                            }
                                        }
                                        
                                        NSHTTPURLResponse * httpResponse = (NSHTTPURLResponse *) response;
                                        if([httpResponse statusCode] == 200){
                                            NSDictionary * result = [NSJSONSerialization JSONObjectWithData:data options:NSJSONReadingMutableLeaves|| NSJSONReadingMutableContainers error:nil];
                                            if ([delegate respondsToSelector:@selector(data:)]) {
                                                [delegate data: result];
                                            }
                                            
                                        }else{
                                            if ([delegate respondsToSelector:@selector(connectionError)]) {
                                                [delegate connectionError];
                                            }
                                        }
                                    }];
    [task resume];
}

+ (void) getAsyncData:(NSString *)url withPostData: (NSDictionary *) data delegateParam:(id<NetworkManager>)delegate {
    NSMutableURLRequest *request = [NSMutableURLRequest requestWithURL:[NSURL URLWithString:url]];
    request.HTTPMethod = @"POST";
    NSError *error = nil;
    NSData *postData = [NSJSONSerialization dataWithJSONObject:data options:kNilOptions error:&error];
    
    NSURLSessionUploadTask *task = [[NSURLSession sharedSession] uploadTaskWithRequest:request fromData:postData completionHandler:^(NSData *data, NSURLResponse *response, NSError *error) {
        if(!response){
            [delegate noConnection];
        }
        
        NSHTTPURLResponse *httpResponse = (NSHTTPURLResponse*) response;
        if([httpResponse statusCode] == 200) {
            NSDictionary *result = [NSJSONSerialization JSONObjectWithData:data options:NSJSONReadingMutableLeaves || NSJSONReadingMutableContainers error:nil];
            [delegate data: result];
        } else {
            [delegate connectionError];
        }
        
        
    }];
    [task resume];
}


+ (void) getVideoAsyncData:(NSString *)url  delegateParam:(id<NetworkManager>)delegate{
    
    NSMutableURLRequest *request = [NSMutableURLRequest requestWithURL:[NSURL URLWithString:url]];
    
    NSURLSessionDataTask *task =
    [[NSURLSession sharedSession] dataTaskWithRequest:request
                                    completionHandler:^(NSData *data,
                                                        NSURLResponse *response,
                                                        NSError *error) {
                                        [delegate videoData: data];
                                    }];
    
    [task resume];
}

/** === iOS9 update for deprecated [NSURLConnection sendSynchronousRequest:returningResponse:error:] === */
+ (NSData*) sendSynchronousRequest:(NSMutableURLRequest*)request returningResponse:(NSURLResponse**)response error:(NSError**)error {
    NSError __block *err = NULL;
    NSData __block *data;
    BOOL __block reqProcessed = false;
    NSURLResponse __block *resp;
    
    [[[NSURLSession sharedSession] dataTaskWithRequest:request completionHandler:^(NSData * _Nullable _data, NSURLResponse * _Nullable _response, NSError * _Nullable _error) {
        resp = _response;
        err = _error;
        data = _data;
        reqProcessed = true;
    }] resume];
    
    while(!reqProcessed) {
        [NSThread sleepForTimeInterval:0];
    }
    
    if(response) *response = resp;
    if(error) *error = err;
    
    return data;
}

@end

