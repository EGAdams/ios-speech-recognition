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
        let mockRecorder = MockAVAudioRecorder()
        audioRecorder.audioRecorder = mockRecorder
        audioRecorder.startRecording()
        XCTAssertTrue(mockRecorder.isRecording)
    }
    
    func testStopRecording() throws {
        let mockRecorder = MockAVAudioRecorder()
        audioRecorder.audioRecorder = mockRecorder
        audioRecorder.stopRecording()
        XCTAssertFalse(mockRecorder.isRecording)
    }

}

class MockAVAudioRecorder: AVAudioRecorder {
    
    var isRecording = false
    
    override func record() -> Bool {
        isRecording = true
        return true
    }
    
    override func stop() {
        isRecording = false
    }
    
}
