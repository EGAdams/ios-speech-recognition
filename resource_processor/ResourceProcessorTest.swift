import Foundation

class RequestManager {
    func sendRequest(url: URL, completion: @escaping (Result<Data?, Error>) -> Void) {
        let session = URLSession(configuration: .default)
        let task = session.dataTask(with: url) { (data, response, error) in
            if let error = error {
                completion(.failure(error))
                return
            }
            
            guard let httpResponse = response as? HTTPURLResponse,
                  (200...299).contains(httpResponse.statusCode) else {
                let statusCode = (response as? HTTPURLResponse)?.statusCode ?? -1
                completion(.failure(NSError(domain: "HTTPError", code: statusCode)))
                return
            }
            
            completion(.success(data))
        }
        
        task.resume()
    }
}

class TestFramework {
    var tests: [() -> Bool] = []
    
    func addTest(_ test: @escaping () -> Bool) {
        tests.append(test)
    }
    
    func runTests() {
        var passed = 0
        var failed = 0
        
        for test in tests {
            if test() {
                passed += 1
            } else {
                failed += 1
            }
        }
        
        print("Tests run: \(passed + failed), Passed: \(passed), Failed: \(failed)")
    }
}

class RequestManagerTests {
    let requestManager = RequestManager()
    
    func testRequestManager() -> Bool {
        let url = URL(string: "https://www.google.com")!
        
        var success = false
        requestManager.sendRequest(url: url) { (result) in
            switch result {
            case .success(let data):
                if data != nil {
                    success = true
                }
            case .failure(let error):
                print("Request failed with error: \(error.localizedDescription)")
            }
        }
        return success
    }
}

let testFramework = TestFramework()
let requestManagerTests = RequestManagerTests()

testFramework.addTest(requestManagerTests.testRequestManager)

testFramework.runTests()
