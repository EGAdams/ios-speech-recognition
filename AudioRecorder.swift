import AVFoundation

class AudioRecorder: NSObject, AVAudioRecorderDelegate {
    
    var audioRecorder: AVAudioRecorder?
    var audioURL: URL?
    
    func startRecording() {
        let audioSession = AVAudioSession.sharedInstance()
        do {
            try audioSession.setCategory(.playAndRecord, mode: .default)
            try audioSession.setActive(true)
            let documentsPath = NSSearchPathForDirectoriesInDomains(.documentDirectory, .userDomainMask, true)[0] as NSString
            let audioFilename = documentsPath.appendingPathComponent("recording.m4a")
            audioURL = URL(fileURLWithPath: audioFilename)
            let settings = [
                AVFormatIDKey: Int(kAudioFormatMPEG4AAC),
                AVSampleRateKey: 12000,
                AVNumberOfChannelsKey: 1,
                AVEncoderAudioQualityKey: AVAudioQuality.high.rawValue
            ]
            audioRecorder = try AVAudioRecorder(url: audioURL!, settings: settings)
            audioRecorder?.delegate = self
            audioRecorder?.record()
        } catch {
            print("Error starting recording: \(error.localizedDescription)")
        }
    }
    
    func stopRecording() {
        audioRecorder?.stop()
    }
    
    func audioRecorderDidFinishRecording(_ recorder: AVAudioRecorder, successfully flag: Bool) {
        if flag {
            print("Recording finished successfully!")
            // You can now pass the audio file URL to your speech recognition API for transcription
            // For example: sendAudioFileToSpeechRecognitionAPI(audioURL)
        } else {
            print("Recording failed.")
        }
    }
    
}
