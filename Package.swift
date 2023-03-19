// swift-tools-version: 5.7
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

// let package = Package(
//     name: "ios-speech-recognition",
//     dependencies: [
//         // Dependencies declare other packages that this package depends on.
//         // .package(url: /* package url */, from: "1.0.0"),
//     ],
//     targets: [
//         // Targets are the basic building blocks of a package. A target can define a module or a test suite.
//         // Targets can depend on other targets in this package, and on products in packages this package depends on.
//         .executableTarget(
//             name: "ios-speech-recognition",
//             dependencies: []),
//         .testTarget(
//             name: "ios-speech-recognitionTests",
//             dependencies: ["ios-speech-recognition"]),
//     ]
// )

let package = Package(
    name: "ios_speech_recognition",
    dependencies: [
        .package(url: "https://github.com/apple/swift-nio.git", from: "2.0.0"),
        .package(url: "https://github.com/apple/swift-log.git", from: "1.0.0"),
        .package(url: "https://github.com/apple/swift-argument-parser.git", from: "0.4.0"),
        .package(url: "https://github.com/apple/swift-tools-support-core.git", from: "0.2.0"),
        .package(url: "https://github.com/apple/swift-collections.git", from: "1.0.0"),
        .package(url: "https://github.com/apple/swift-algorithms.git", from: "0.0.4"),
        .package(url: "https://github.com/apple/swift-crypto.git", from: "2.0.0"),
        .package(url: "https://github.com/apple/swift-numerics.git", from: "0.1.0"),
        .package(url: "https://github.com/apple/swift-xctest.git", from: "1.0.0"),
    ],
    targets: [
        .target(
            name: "ios-speech-recognition",
            dependencies: [
                .product(name: "NIO", package: "swift-nio"),
                .product(name: "Logging", package: "swift-log"),
                .product(name: "ArgumentParser", package: "swift-argument-parser"),
                .product(name: "SwiftToolsSupport", package: "swift-tools-support-core"),
                .product(name: "Collections", package: "swift-collections"),
                .product(name: "Algorithms", package: "swift-algorithms"),
                .product(name: "Crypto", package: "swift-crypto"),
                .product(name: "Numerics", package: "swift-numerics"),
            ]
        ),
        .testTarget(
            name: "ios-speech-recognitionTests",
            dependencies: [
                .target(name: "ios-speech-recognition"),
                .product(name: "XCTest", package: "swift-xctest"),
            ]
        ),
    ]
)
