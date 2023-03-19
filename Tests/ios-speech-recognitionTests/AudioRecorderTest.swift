import XCTest
@testable import MyApp // Replace with your app's module name
import AVFoundation

class AudioRecorderTests: XCTestCase {
    
    var audioRecorder: AudioRecorder!
    var audioSession: AVAudioSession!
    
    override func setUpWithError() throws {
        audioRecorder = AudioRecorder()
        audioSession = AVAudioSession.sharedInstance()
        try audioSession.setCategory(.playAndRecord, mode: .default)
        try audioSession.setActive(true)
    }

    override func tearDownWithError() throws {
        audioRecorder = nil
        try audioSession.setActive(false)
    }

    func testStartRecording() throws {
        XCTAssertNil(audioRecorder.audioRecorder)
        audioRecorder.startRecording()
        XCTAssertNotNil(audioRecorder.audioRecorder)
        XCTAssertTrue(audioRecorder.audioRecorder!.isRecording)
    }
    
    func testStopRecording() throws {
        audioRecorder.startRecording()
        XCTAssertTrue(audioRecorder.audioRecorder!.isRecording)
        audioRecorder.stopRecording()
        XCTAssertFalse(audioRecorder.audioRecorder!.isRecording)
    }

}
