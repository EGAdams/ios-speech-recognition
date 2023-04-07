import AVFoundation
import Foundation

class MockAudioRecorderDelegate: NSObject, AVAudioRecorderDelegate {
    var didRecordSuccessfully = false
    
    func audioRecorderDidFinishRecording(_ recorder: AVAudioRecorder, successfully flag: Bool) {
        didRecordSuccessfully = flag
    }
}

func testAudioRecorder() {
    let mockDelegate = MockAudioRecorderDelegate()
    let audioRecorder = AudioRecorder()
    audioRecorder.audioRecorder?.delegate = mockDelegate
    audioRecorder.startRecording()
    Thread.sleep(forTimeInterval: 2)
    audioRecorder.stopRecording()
    
    if mockDelegate.didRecordSuccessfully {
        print("Audio recorded successfully!")
    } else {
        print("Error: Audio recording failed.")
    }
}

testAudioRecorder()