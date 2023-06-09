import Foundation
import AVFoundation

class AudioRecorderTests {
    
    var audioRecorder: AudioRecorder!
    var audioSession: AVAudioSession!
    
    init() {
        audioRecorder = AudioRecorder()
        audioSession = AVAudioSession.sharedInstance()
    }
    
    func run() {
        do {
            try setUp()
            try testStartRecording()
            try testStopRecording()
            try tearDown()
            print("All tests passed.")
        } catch {
            print("Test failed: \(error)")
        }
    }
    
    func setUp() throws {
        try audioSession.setCategory(.playAndRecord, mode: .default)
        try audioSession.setActive(true)
    }
    
    func tearDown() throws {
        audioRecorder = nil
        try audioSession.setActive(false)
    }
    
    func testStartRecording() throws {
        let mockRecorder = MockAVAudioRecorder()
        audioRecorder.audioRecorder = mockRecorder
        audioRecorder.startRecording()
        if !mockRecorder.isRecording {
            throw TestError(message: "Recording did not start.")
        }
    }
    
    func testStopRecording() throws {
        let mockRecorder = MockAVAudioRecorder()
        audioRecorder.audioRecorder = mockRecorder
        audioRecorder.stopRecording()
        if mockRecorder.isRecording {
            throw TestError(message: "Recording did not stop.")
        }
    }
}

class MockAVAudioRecorder {
    
    var isRecording = false
    
    func record() -> Bool {
        isRecording = true
        return true
    }
    
    func stop() {
        isRecording = false
    }
}

struct TestError: Error {
    let message: String
}
