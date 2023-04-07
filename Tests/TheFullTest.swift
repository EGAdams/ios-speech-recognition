class AudioRecorderTests {
    
    var audioRecorder: AudioRecorder!
    var audioSession: AudioSession!
    
    init() {
        audioRecorder = AudioRecorder()
        audioSession = AudioSession()
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
        try audioSession.setCategory(/*.playAndRecord, mode: .default */)
        try audioSession.setActive(true)
    }
    
    func tearDown() throws {
        audioRecorder = nil
        try audioSession.setActive(false)
    }
    
    func testStartRecording() throws {
        let mockRecorder = MockAudioRecorder()
        audioRecorder.audioRecorder = mockRecorder
        audioRecorder.startRecording()
        if !mockRecorder.isRecording {
            throw TestError(message: "Recording did not start.")
        }
    }
    
    func testStopRecording() throws {
        let mockRecorder = MockAudioRecorder()
        audioRecorder.audioRecorder = mockRecorder
        audioRecorder.stopRecording()
        if mockRecorder.isRecording {
            throw TestError(message: "Recording did not stop.")
        }
    }
}

class AudioSession {
    
    enum Category {
        case playAndRecord
    }
    
    func setCategory( /* _ category: Category, mode: Any */ ) throws {
        // Implementation details
        print ( "setting catagory..." )
    }
    
    func setActive(_ active: Bool) throws {
        // print active value
        print ( "setting active to: \(active)")
    }
}

class AudioRecorder {
    
    var audioRecorder: Any?
    
    func startRecording() {
        if let recorder = audioRecorder as? MockAudioRecorder {
            recorder.record()
        }
    }
    
    func stopRecording() {
        if let recorder = audioRecorder as? MockAudioRecorder {
            recorder.stop()
        }
    }
}

class MockAudioRecorder {
    
    var isRecording = false
    
    func record() {
        isRecording = true
    }
    
    func stop() {
        isRecording = false
    }
}

struct TestError: Error {
    let message: String
}

let recorderTests = AudioRecorderTests()
recorderTests.run()
