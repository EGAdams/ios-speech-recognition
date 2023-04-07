protocol FileWriter {
    func createFile(atPath path: String, format: AudioFormat) throws
    func writeData(_ data: Data) throws
    func closeFile() throws
}

struct AudioFormat {
    let sampleRate: Double
    let bitDepth: Int
    let channels: Int
}

class AudioRecorder {
    
    var format: AudioFormat
    var isRecording: Bool = false
    
    private var writer: FileWriter?
    private var data = Data()
    
    init(format: AudioFormat) {
        self.format = format
    }
    
    func startRecording(withWriter writer: FileWriter) throws {
        guard !isRecording else {
            throw RecorderError.alreadyRecording
        }
        self.writer = writer
        try writer.createFile(atPath: "recording.wav", format: format)
        isRecording = true
    }
    
    func stopRecording() throws {
        guard isRecording else {
            throw RecorderError.notRecording
        }
        try writer?.writeData(data)
        try writer?.closeFile()
        writer = nil
        isRecording = false
    }
    
    func record(_ buffer: [Int16]) throws {
        guard isRecording else {
            throw RecorderError.notRecording
        }
        var data = Data()
        for sample in buffer {
            var sample = sample.bigEndian
            data.append(&sample, count: MemoryLayout<Int16>.size)
        }
        self.data.append(data)
        try writer?.writeData(data)
    }
    
}

enum RecorderError: Error {
    case alreadyRecording
    case notRecording
}
