
// test framework here

protocol TextProcessor {
    func process(text: String) -> String
}

class MyTextProcessor: TextProcessor {
    func process(text: String) -> String {
        return text.lowercased()
    }
}

func assertEqual<T: Equatable>(_ actual: T, _ expected: T, _ message: String? = nil) {
    guard actual == expected else {
        print("Assertion failed: \(message ?? "") Expected: \(expected), but got: \(actual)")
        // exit program
        return
    }
}

func runTests() {
    let processor = MyTextProcessor()

    // Test 1: empty string
    assertEqual(processor.process(text: ""), "")

    // Test 2: lowercasing
    assertEqual(processor.process(text: "HELLO"), "hello")

    // Test 3: special characters
    assertEqual(processor.process(text: "#$^&"), "#$^&")

    // Test 4: mixed case and whitespace
    assertEqual(processor.process(text: "AbC dEf"), "abc def")

    print("All tests passed successfully!")
}

runTests()

    