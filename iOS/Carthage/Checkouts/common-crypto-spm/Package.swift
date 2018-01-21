// swift-tools-version:3.1

import PackageDescription

let package = Package(
    name: "SSCommonCrypto",
    dependencies: [
        .Package(url: "https://github.com/watson-developer-cloud/swift-sdk", majorVersion: 0)
    ]
)

