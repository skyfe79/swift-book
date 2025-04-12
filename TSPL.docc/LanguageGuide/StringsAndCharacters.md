# 문자열과 문자

텍스트를 저장하고 조작한다.

*문자열*은 `"hello, world"`나 `"albatross"`와 같은 일련의 문자를 의미한다. Swift에서 문자열은 `String` 타입으로 표현된다. `String`의 내용은 `Character` 값의 컬렉션을 포함한 다양한 방식으로 접근할 수 있다.

Swift의 `String`과 `Character` 타입은 코드에서 텍스트를 다루는 빠르고 유니코드 호환 방식이다. 문자열 생성과 조작을 위한 문법은 가볍고 읽기 쉬우며, C 언어와 유사한 문자열 리터럴 문법을 사용한다. 문자열 연결은 `+` 연산자를 사용해 두 문자열을 결합하는 것만큼 간단하다. 문자열의 가변성은 상수와 변수 중 하나를 선택해 관리하며, 이는 Swift의 다른 값들과 동일한 방식이다. 또한 문자열 보간(string interpolation)이라는 프로세스를 통해 상수, 변수, 리터럴, 표현식을 더 긴 문자열에 삽입할 수 있다. 이를 통해 화면 표시, 저장, 출력을 위한 커스텀 문자열 값을 쉽게 만들 수 있다.

이렇게 간단한 문법에도 불구하고, Swift의 `String` 타입은 빠르고 현대적인 문자열 구현이다. 모든 문자열은 인코딩에 독립적인 유니코드 문자로 구성되며, 다양한 유니코드 표현으로 문자에 접근하는 기능을 제공한다.

> 참고: Swift의 `String` 타입은 Foundation의 `NSString` 클래스와 연결되어 있다. Foundation은 `String`을 확장해 `NSString`에 정의된 메서드를 노출한다. 즉, Foundation을 임포트하면 `String`에서 `NSString` 메서드를 캐스팅 없이 사용할 수 있다.
>
> Foundation과 Cocoa에서 `String`을 사용하는 방법에 대한 자세한 내용은 [Bridging Between String and NSString](https://developer.apple.com/documentation/swift/string#2919514)을 참고한다.


## 문자열 리터럴

코드 안에 미리 정의된 `String` 값을 *문자열 리터럴*로 포함할 수 있다.  
문자열 리터럴은 쌍따옴표(`"`)로 둘러싸인 문자들의 연속이다.

상수나 변수의 초기값으로 문자열 리터럴을 사용한다:

```swift
let someString = "Some string literal value"
```

<!--
  - test: `stringLiterals`

  ```swifttest
  -> let someString = "Some string literal value"
  ```
-->

Swift는 `someString` 상수의 타입을 `String`으로 추론한다.  
이 상수가 문자열 리터럴 값으로 초기화되었기 때문이다.


### 여러 줄 문자열 리터럴

여러 줄에 걸친 문자열이 필요하다면, 여러 줄 문자열 리터럴을 사용한다. 이는 세 개의 큰따옴표로 둘러싸인 문자 시퀀스다.

<!--
  이 인용문은 "Alice's Adventures in Wonderland"에서 가져왔으며,
  1907년부터 퍼블릭 도메인으로 전환되었다.
-->

```swift
let quotation = """
The White Rabbit put on his spectacles.  "Where shall I begin,
please your Majesty?" he asked.

"Begin at the beginning," the King said gravely, "and go on
till you come to the end; then stop."
"""
```

<!--
  - test: `multiline-string-literals`

  ```swifttest
  -> let quotation = """
     The White Rabbit put on his spectacles.  "Where shall I begin,
     please your Majesty?" he asked.

     "Begin at the beginning," the King said gravely, "and go on
     till you come to the end; then stop."
     """
  >> let newlines = quotation.filter { $0 == "\n" }
  >> print(newlines.count)
  << 4
  ```
-->

여러 줄 문자열 리터럴은 여는 따옴표(`"""`)와 닫는 따옴표 사이의 모든 줄을 포함한다. 문자열은 여는 따옴표 바로 다음 줄에서 시작하고, 닫는 따옴표 바로 전 줄에서 끝난다. 따라서 아래의 문자열은 줄바꿈으로 시작하거나 끝나지 않는다.

```swift
let singleLineString = "These are the same."
let multilineString = """
These are the same.
"""
```

<!--
  - test: `multiline-string-literals`

  ```swifttest
  -> let singleLineString = "These are the same."
  -> let multilineString = """
     These are the same.
     """
  >> print(singleLineString == multilineString)
  << true
  ```
-->

소스 코드에서 여러 줄 문자열 리터럴 안에 줄바꿈이 포함되어 있다면, 그 줄바꿈도 문자열 값에 포함된다. 소스 코드를 더 읽기 쉽게 만들기 위해 줄바꿈을 사용하지만, 그 줄바꿈이 문자열 값에 포함되지 않게 하려면 해당 줄 끝에 백슬래시(`\`)를 추가한다.

```swift
let softWrappedQuotation = """
The White Rabbit put on his spectacles.  "Where shall I begin, \
please your Majesty?" he asked.

"Begin at the beginning," the King said gravely, "and go on \
till you come to the end; then stop."
"""
```

<!--
  - test: `multiline-string-literals`

  ```swifttest
  -> let softWrappedQuotation = """
     The White Rabbit put on his spectacles.  "Where shall I begin, \
     please your Majesty?" he asked.

     "Begin at the beginning," the King said gravely, "and go on \
     till you come to the end; then stop."
     """
  >> let softNewlines = softWrappedQuotation.filter { $0 == "\n" }
  >> print(softNewlines.count)
  << 2
  ```
-->

여러 줄 문자열 리터럴이 줄바꿈으로 시작하거나 끝나게 하려면, 첫 번째 또는 마지막 줄을 비워둔다. 예를 들어:

```swift
let lineBreaks = """

This string starts with a line break.
It also ends with a line break.

"""
```

<!--
  - test: `multiline-string-literals`

  ```swifttest
  -> let lineBreaks = """

     This string starts with a line break.
     It also ends with a line break.

     """
  ```
-->

<!--
  이 줄들은 잘 먹고 있습니다!
-->

여러 줄 문자열은 주변 코드와 일치하도록 들여쓸 수 있다. 닫는 따옴표(`"""`) 앞의 공백은 Swift에게 다른 모든 줄 앞의 공백을 무시하라고 알려준다. 그러나 닫는 따옴표 앞의 공백보다 더 많은 공백을 줄의 시작 부분에 추가하면, 그 공백은 문자열에 포함된다.

![](multilineStringWhitespace)

<!--
  여기서 이미지를 사용하는 것이 코드 목록보다 조금 더 명확하다.
  왜냐하면 어떤 공백이 "카운트"되는지 표시할 수 있기 때문이다.
-->

<!--
  - test: `multiline-string-literal-whitespace`

  ```swifttest
  -> let linesWithIndentation = """
         This line doesn't begin with whitespace.
             This line begins with four spaces.
         This line doesn't begin with whitespace.
         """
  ```
-->

위 예제에서, 여러 줄 문자열 리터럴 전체가 들여쓰기 되어 있더라도, 문자열의 첫 번째와 마지막 줄은 공백으로 시작하지 않는다. 중간 줄은 닫는 따옴표보다 더 많은 들여쓰기가 되어 있으므로, 추가로 네 칸의 들여쓰기가 포함된다.


### 문자열 리터럴의 특수 문자

문자열 리터럴에는 다음과 같은 특수 문자를 포함할 수 있다:

- 이스케이프된 특수 문자: `\0` (널 문자), `\\` (역슬래시), `\t` (수평 탭), `\n` (줄 바꿈), `\r` (캐리지 리턴), `\"` (쌍따옴표), `\'` (홑따옴표)
- 임의의 유니코드 스칼라 값: `\u{`*n*`}` 형식으로 작성하며, 여기서 *n*은 1~8자리의 16진수 숫자 (유니코드에 대한 자세한 내용은 아래 <doc:StringsAndCharacters#Unicode>에서 다룬다)

<!--
  - test: `stringLiteralUnicodeScalar`

  ```swifttest
  >> _ = "\u{0}"
  >> _ = "\u{00000000}"
  >> _ = "\u{000000000}"
  !$ error: \u{...} escape sequence expects between 1 and 8 hex digits
  !! _ = "\u{000000000}"
  !!      ^
  >> _ = "\u{10FFFF}"
  >> _ = "\u{110000}"
  !$ error: invalid unicode scalar
  !! _ = "\u{110000}"
  !!      ^
  ```
-->

아래 코드는 이러한 특수 문자를 사용한 네 가지 예제를 보여준다. `wiseWords` 상수에는 두 개의 이스케이프된 쌍따옴표가 포함되어 있다. `dollarSign`, `blackHeart`, `sparklingHeart` 상수는 유니코드 스칼라 형식을 보여준다:

```swift
let wiseWords = "\"Imagination is more important than knowledge\" - Einstein"
// "Imagination is more important than knowledge" - Einstein
let dollarSign = "\u{24}"        // $,  Unicode scalar U+0024
let blackHeart = "\u{2665}"      // ♥,  Unicode scalar U+2665
let sparklingHeart = "\u{1F496}" // 💖, Unicode scalar U+1F496
```

<!--
  - test: `specialCharacters`

  ```swifttest
  -> let wiseWords = "\"Imagination is more important than knowledge\" - Einstein"
  >> print(wiseWords)
  </ "Imagination is more important than knowledge" - Einstein
  -> let dollarSign = "\u{24}"        // $,  Unicode scalar U+0024
  >> assert(dollarSign == "$")
  -> let blackHeart = "\u{2665}"      // ♥,  Unicode scalar U+2665
  >> assert(blackHeart == "♥")
  -> let sparklingHeart = "\u{1F496}" // 💖, Unicode scalar U+1F496
  >> assert(sparklingHeart == "💖")
  ```
-->

여러 줄 문자열 리터럴은 단일 쌍따옴표 대신 세 개의 쌍따옴표를 사용하기 때문에, 여러 줄 문자열 리터럴 내부에 쌍따옴표(`"`)를 이스케이프 없이 포함할 수 있다. 여러 줄 문자열에 `"""` 텍스트를 포함하려면, 적어도 하나의 따옴표를 이스케이프해야 한다. 예를 들어:

```swift
let threeDoubleQuotationMarks = """
Escaping the first quotation mark \"""
Escaping all three quotation marks \"\"\"
"""
```

<!--
  - test: `multiline-string-literals`

  ```swifttest
  -> let threeDoubleQuotationMarks = """
     Escaping the first quotation mark \"""
     Escaping all three quotation marks \"\"\"
     """
  >> print(threeDoubleQuotationMarks)
  << Escaping the first quotation mark """
  << Escaping all three quotation marks """
  ```
-->


### 확장된 문자열 구분자

특수 문자를 그 효과를 발휘하지 않고 문자열에 포함시키기 위해 *확장된 구분자* 안에 문자열 리터럴을 넣을 수 있다. 문자열을 따옴표(`"`)로 감싸고 그 주위를 숫자 기호(`#`)로 둘러싸면 된다. 예를 들어, `#"Line 1\nLine 2"#` 문자열 리터럴을 출력하면 줄바꿈 이스케이프 시퀀스(`\n`)가 그대로 출력되며, 두 줄로 나뉘어 출력되지 않는다.

만약 문자열 리터럴에서 특수 문자의 효과를 사용하고 싶다면, 이스케이프 문자(`\`) 뒤에 오는 문자와 동일한 수의 숫자 기호를 문자열 내에 일치시켜야 한다. 예를 들어, 문자열이 `#"Line 1\nLine 2"#`이고 줄을 바꾸고 싶다면, `#"Line 1\#nLine 2"#`를 사용하면 된다. 마찬가지로, `###"Line1\###nLine2"###`도 줄을 바꾼다.

확장된 구분자를 사용해 생성한 문자열 리터럴은 여러 줄 문자열 리터럴이 될 수도 있다. 확장된 구분자를 사용하면 여러 줄 문자열에 `"""` 텍스트를 포함시킬 수 있으며, 이는 리터럴을 종료하는 기본 동작을 재정의한다. 예를 들어:

```swift
let threeMoreDoubleQuotationMarks = #"""
Here are three more double quotes: """
"""#
```

<!--
  - test: `extended-string-delimiters`

  ```swifttest
  -> let threeMoreDoubleQuotationMarks = #"""
     Here are three more double quotes: """
     """#
  >> print(threeMoreDoubleQuotationMarks)
  << Here are three more double quotes: """
  ```
-->


## 빈 문자열 초기화

더 긴 문자열을 만들기 위한 시작점으로 빈 `String` 값을 생성하려면, 빈 문자열 리터럴을 변수에 할당하거나 초기화 구문을 사용해 새로운 `String` 인스턴스를 생성한다:

```swift
var emptyString = ""               // 빈 문자열 리터럴
var anotherEmptyString = String()  // 초기화 구문
// 이 두 문자열은 모두 비어 있으며, 서로 동등하다
```

<!--
  - test: `emptyStrings`

  ```swifttest
  -> var emptyString = ""               // 빈 문자열 리터럴
  -> var anotherEmptyString = String()  // 초기화 구문
  // 이 두 문자열은 모두 비어 있으며, 서로 동등하다
  >> assert(emptyString == anotherEmptyString)
  ```
-->

`String` 값이 비어 있는지 확인하려면 불리언 `isEmpty` 프로퍼티를 사용한다:

```swift
if emptyString.isEmpty {
    print("여기 볼 게 없습니다")
}
// "여기 볼 게 없습니다" 출력
```

<!--
  - test: `emptyStrings`

  ```swifttest
  -> if emptyString.isEmpty {
        print("여기 볼 게 없습니다")
     }
  <- 여기 볼 게 없습니다
  ```
-->

<!--
  TODO: init(size, character)
-->


## 문자열의 변경 가능성

특정 `String`이 수정 가능한지 여부를 변수에 할당할지 상수에 할당할지로 결정한다. 변수에 할당하면 수정이 가능하고, 상수에 할당하면 수정이 불가능하다.

```swift
var variableString = "Horse"
variableString += " and carriage"
// variableString은 이제 "Horse and carriage"가 된다.

let constantString = "Highlander"
constantString += " and another Highlander"
// 이 코드는 컴파일 시 오류를 발생시킨다 - 상수 문자열은 수정할 수 없다.
```

<!--
  - test: `stringMutability`

  ```swifttest
  -> var variableString = "Horse"
  -> variableString += " and carriage"
  // variableString은 이제 "Horse and carriage"가 된다.

  -> let constantString = "Highlander"
  -> constantString += " and another Highlander"
  !$ error: left side of mutating operator isn't mutable: 'constantString' is a 'let' constant
  !! constantString += " and another Highlander"
  !! ~~~~~~~~~~~~~~ ^
  !$ note: change 'let' to 'var' to make it mutable
  !! let constantString = "Highlander"
  !! ^~~
  !! var
  // 이 코드는 컴파일 시 오류를 발생시킨다 - 상수 문자열은 수정할 수 없다.
  ```
-->

<!--
  - test: `stringMutability-ok`

  ```swifttest
  -> var variableString = "Horse"
  -> variableString += " and carriage"
  /> variableString은 이제 \"\(variableString)\"가 된다.
  </ variableString은 이제 "Horse and carriage"가 된다.
  ```
-->

> 참고: 이 방식은 Objective-C와 Cocoa에서의 문자열 뮤테이션과 다르다. Objective-C와 Cocoa에서는 두 클래스(`NSString`과 `NSMutableString`) 중 하나를 선택해 문자열이 수정 가능한지 여부를 결정한다.


## 문자열은 값 타입이다

Swift의 `String` 타입은 *값 타입*이다.  
새로운 `String` 값을 생성하면, 이 값은 함수나 메서드에 전달되거나 상수나 변수에 할당될 때 *복사*된다.  
각 경우에 기존 `String` 값의 새 복사본이 생성되고, 원본이 아닌 새 복사본이 전달되거나 할당된다.  
값 타입에 대한 자세한 설명은 <doc:ClassesAndStructures#Structures-and-Enumerations-Are-Value-Types>에서 확인할 수 있다.

Swift의 기본 복사 방식은 함수나 메서드가 `String` 값을 전달할 때,  
해당 `String` 값이 어디에서 왔는지와 상관없이 정확히 그 값을 소유한다는 것을 명확히 보장한다.  
여러분에게 전달된 문자열은 직접 수정하지 않는 한 변경되지 않을 것이라는 확신을 가질 수 있다.

Swift 컴파일러는 문자열 사용을 최적화하여 실제 복사가 꼭 필요한 경우에만 발생하도록 한다.  
이를 통해 문자열을 값 타입으로 다룰 때 항상 뛰어난 성능을 얻을 수 있다.


## 문자 다루기

`String`의 개별 `Character` 값에 접근하려면 `for`-`in` 루프를 사용해 문자열을 순회할 수 있다:

```swift
for character in "Dog!🐶" {
    print(character)
}
// D
// o
// g
// !
// 🐶
```

<!--
  - test: `characters`

  ```swifttest
  -> for character in "Dog!🐶" {
        print(character)
     }
  </ D
  </ o
  </ g
  </ !
  </ 🐶
  ```
-->

`for`-`in` 루프에 대한 자세한 설명은 <doc:ControlFlow#For-In-Loops>에서 확인할 수 있다.

또는 단일 문자 문자열 리터럴에서 `Character` 타입 어노테이션을 제공해 독립적인 `Character` 상수나 변수를 생성할 수 있다:

```swift
let exclamationMark: Character = "!"
```

<!--
  - test: `characters`

  ```swifttest
  -> let exclamationMark: Character = "!"
  ```
-->

`Character` 값의 배열을 초기화 인자로 전달해 `String` 값을 생성할 수도 있다:

```swift
let catCharacters: [Character] = ["C", "a", "t", "!", "🐱"]
let catString = String(catCharacters)
print(catString)
// Prints "Cat!🐱"
```

<!--
  - test: `characters`

  ```swifttest
  -> let catCharacters: [Character] = ["C", "a", "t", "!", "🐱"]
  -> let catString = String(catCharacters)
  -> print(catString)
  <- Cat!🐱
  ```
-->


## 문자열과 문자 연결하기

`String` 값은 덧셈 연산자(`+`)를 사용해 서로 더하거나(또는 *연결하여*) 새로운 `String` 값을 만들 수 있다:

```swift
let string1 = "hello"
let string2 = " there"
var welcome = string1 + string2
// welcome now equals "hello there"
```

<!--
  - test: `concatenation`

  ```swifttest
  -> let string1 = "hello"
  -> let string2 = " there"
  -> var welcome = string1 + string2
  /> welcome now equals \"\(welcome)\"
  </ welcome now equals "hello there"
  ```
-->

덧셈 할당 연산자(`+=`)를 사용해 기존 `String` 변수에 `String` 값을 추가할 수도 있다:

```swift
var instruction = "look over"
instruction += string2
// instruction now equals "look over there"
```

<!--
  - test: `concatenation`

  ```swifttest
  -> var instruction = "look over"
  -> instruction += string2
  /> instruction now equals \"\(instruction)\"
  </ instruction now equals "look over there"
  ```
-->

`String` 타입의 `append()` 메서드를 사용해 `Character` 값을 `String` 변수에 추가할 수도 있다:

```swift
let exclamationMark: Character = "!"
welcome.append(exclamationMark)
// welcome now equals "hello there!"
```

<!--
  - test: `concatenation`

  ```swifttest
  -> let exclamationMark: Character = "!"
  -> welcome.append(exclamationMark)
  /> welcome now equals \"\(welcome)\"
  </ welcome now equals "hello there!"
  ```
-->

> 참고: `Character` 변수에는 `String`이나 `Character`를 추가할 수 없다. `Character` 값은 반드시 단일 문자만 포함해야 하기 때문이다.

여러 줄 문자열 리터럴을 사용해 긴 문자열의 각 줄을 구성할 때는, 마지막 줄을 포함해 모든 줄이 줄바꿈으로 끝나도록 해야 한다. 예를 들어:

```swift
let badStart = """
    one
    two
    """
let end = """
    three
    """
print(badStart + end)
// Prints two lines:
// one
// twothree

let goodStart = """
    one
    two

    """
print(goodStart + end)
// Prints three lines:
// one
// two
// three
```

<!--
  - test: `concatenate-multiline-string-literals`

  ```swifttest
  -> let badStart = """
         one
         two
         """
  -> let end = """
         three
         """
  -> print(badStart + end)
  // Prints two lines:
  </ one
  </ twothree

  -> let goodStart = """
         one
         two

         """
  -> print(goodStart + end)
  // Prints three lines:
  </ one
  </ two
  </ three
  ```
-->

위 코드에서 `badStart`와 `end`를 연결하면 두 줄짜리 문자열이 생성된다. 이는 원하는 결과가 아니다. `badStart`의 마지막 줄이 줄바꿈으로 끝나지 않기 때문에, 해당 줄이 `end`의 첫 번째 줄과 합쳐진다. 반면, `goodStart`의 두 줄 모두 줄바꿈으로 끝나므로, `end`와 연결했을 때 예상대로 세 줄짜리 문자열이 생성된다.


## 문자열 보간법

*문자열 보간법*은 상수, 변수, 리터럴, 표현식을 문자열 리터럴 안에 포함시켜 새로운 `String` 값을 생성하는 방법이다. 문자열 보간법은 한 줄짜리 문자열과 여러 줄짜리 문자열 리터럴 모두에서 사용할 수 있다. 문자열 리터럴 안에 삽입할 각 항목은 백슬래시(`\`)로 시작하고 괄호 쌍으로 감싼다:

```swift
let multiplier = 3
let message = "\(multiplier) times 2.5 is \(Double(multiplier) * 2.5)"
// message is "3 times 2.5 is 7.5"
```

<!--
  - test: `stringInterpolation`

  ```swifttest
  -> let multiplier = 3
  -> let message = "\(multiplier) times 2.5 is \(Double(multiplier) * 2.5)"
  /> message is \"\(message)\"
  </ message is "3 times 2.5 is 7.5"
  ```
-->

위 예제에서 `multiplier`의 값은 `\(multiplier)`로 문자열 리터럴 안에 삽입된다. 이 자리 표시자는 문자열 보간법이 평가되어 실제 문자열을 생성할 때 `multiplier`의 실제 값으로 대체된다.

`multiplier`의 값은 문자열의 뒷부분에서 더 큰 표현식의 일부로도 사용된다. 이 표현식은 `Double(multiplier) * 2.5` 값을 계산하고 그 결과(`7.5`)를 문자열에 삽입한다. 이 경우 표현식은 문자열 리터럴 안에 포함될 때 `\(Double(multiplier) * 2.5)`로 작성된다.

확장된 문자열 구분자를 사용하면 문자열 보간법으로 처리될 수 있는 문자를 포함하는 문자열을 생성할 수 있다. 예를 들어:

```swift
print(#"Write an interpolated string in Swift using \(multiplier)."#)
// Prints "Write an interpolated string in Swift using \(multiplier)."
```

<!--
  - test: `stringInterpolation`

  ```swifttest
  -> print(#"Write an interpolated string in Swift using \(multiplier)."#)
  <- Write an interpolated string in Swift using \(multiplier).
  ```
-->

확장된 구분자를 사용하는 문자열 안에서 문자열 보간법을 사용하려면 백슬래시 뒤의 숫자 기호(#) 개수를 문자열의 시작과 끝에 있는 숫자 기호 개수와 일치시켜야 한다. 예를 들어:

```swift
print(#"6 times 7 is \#(6 * 7)."#)
// Prints "6 times 7 is 42."
```

<!--
  - test: `stringInterpolation`

  ```swifttest
  -> print(#"6 times 7 is \#(6 * 7)."#)
  <- 6 times 7 is 42.
  ```
-->

> 참고: 보간된 문자열 안의 괄호 안에 작성하는 표현식은 이스케이프되지 않은 백슬래시(`\`), 캐리지 리턴, 줄 바꿈을 포함할 수 없다. 하지만 다른 문자열 리터럴은 포함할 수 있다.


## 유니코드

**유니코드**는 다양한 문자 체계에서 텍스트를 인코딩하고 표현하며 처리하기 위한 국제 표준이다. 유니코드는 거의 모든 언어의 문자를 표준화된 형태로 표현할 수 있게 해준다. 또한 텍스트 파일이나 웹 페이지와 같은 외부 소스로부터 이러한 문자를 읽고 쓸 수 있도록 지원한다. Swift의 `String`과 `Character` 타입은 이 절에서 설명하는 대로 완전히 유니코드를 준수한다.


### 유니코드 스칼라 값

Swift의 기본 `String` 타입은 *유니코드 스칼라 값*으로 구성된다. 유니코드 스칼라 값은 문자나 수정자를 나타내는 고유한 21비트 숫자다. 예를 들어, `LATIN SMALL LETTER A` (`"a"`)는 `U+0061`로, `FRONT-FACING BABY CHICK` (`"🐥"`)는 `U+1F425`로 표현된다.

모든 21비트 유니코드 스칼라 값이 문자에 할당된 것은 아니다. 일부 스칼라 값은 미래에 할당되거나 UTF-16 인코딩에서 사용하기 위해 예약되어 있다. 문자에 할당된 스칼라 값은 일반적으로 이름도 가지고 있다. 위 예시에서 `LATIN SMALL LETTER A`와 `FRONT-FACING BABY CHICK`가 그렇다.


### 확장된 그래프 클러스터

Swift의 `Character` 타입은 각각 하나의 *확장된 그래프 클러스터*를 나타낸다. 확장된 그래프 클러스터는 하나 이상의 유니코드 스칼라로 이루어진 시퀀스로, 이들이 결합되면 사람이 읽을 수 있는 단일 문자를 생성한다.

예를 들어, 문자 `é`는 단일 유니코드 스칼라 `é`(`LATIN SMALL LETTER E WITH ACUTE`, 또는 `U+00E9`)로 표현할 수 있다. 하지만 동일한 문자를 두 개의 스칼라로도 표현할 수 있다. 일반 문자 `e`(`LATIN SMALL LETTER E`, 또는 `U+0065`)에 `COMBINING ACUTE ACCENT` 스칼라(`U+0301`)가 뒤따르는 방식이다. `COMBINING ACUTE ACCENT` 스칼라는 앞에 오는 스칼라에 그래픽적으로 적용되어, 유니코드를 지원하는 텍스트 렌더링 시스템에서 `e`를 `é`로 변환한다.

두 경우 모두, 문자 `é`는 Swift의 단일 `Character` 값으로 표현되며, 이는 확장된 그래프 클러스터를 나타낸다. 첫 번째 경우에는 클러스터가 단일 스칼라로 구성되고, 두 번째 경우에는 두 개의 스칼라로 구성된다:

```swift
let eAcute: Character = "\u{E9}"                         // é
let combinedEAcute: Character = "\u{65}\u{301}"          // e followed by ́
// eAcute는 é, combinedEAcute는 é
```

<!--
  - test: `graphemeClusters1`

  ```swifttest
  -> let eAcute: Character = "\u{E9}"                         // é
  >> assert(eAcute == "é")
  -> let combinedEAcute: Character = "\u{65}\u{301}"          // e followed by ́
  >> assert(combinedEAcute == "é")
  /> eAcute is \(eAcute), combinedEAcute is \(combinedEAcute)
  </ eAcute is é, combinedEAcute is é
  >> assert(eAcute == combinedEAcute)
  ```
-->

확장된 그래프 클러스터는 복잡한 스크립트 문자를 단일 `Character` 값으로 표현할 수 있는 유연한 방법을 제공한다. 예를 들어, 한글 음절은 미리 조합된(precomposed) 형태나 분해된(decomposed) 시퀀스로 표현할 수 있다. 두 표현 모두 Swift에서 단일 `Character` 값으로 인정된다:

```swift
let precomposed: Character = "\u{D55C}"                  // 한
let decomposed: Character = "\u{1112}\u{1161}\u{11AB}"   // ᄒ, ᅡ, ᆫ
// precomposed는 한, decomposed는 한
```

<!--
  - test: `graphemeClusters2`

  ```swifttest
  -> let precomposed: Character = "\u{D55C}"                  // 한
  >> assert(precomposed == "한")
  -> let decomposed: Character = "\u{1112}\u{1161}\u{11AB}"   // ᄒ, ᅡ, ᆫ
  >> assert(decomposed == "한")
  /> precomposed is \(precomposed), decomposed is \(decomposed)
  </ precomposed is 한, decomposed is 한
  ```
-->

확장된 그래프 클러스터는 `COMBINING ENCLOSING CIRCLE`(`U+20DD`)와 같은 감싸는 표시를 위한 스칼라가 다른 유니코드 스칼라를 감싸서 단일 `Character` 값의 일부로 만들 수 있게 한다:

```swift
let enclosedEAcute: Character = "\u{E9}\u{20DD}"
// enclosedEAcute는 é⃝
```

<!--
  - test: `graphemeClusters3`

  ```swifttest
  -> let enclosedEAcute: Character = "\u{E9}\u{20DD}"
  >> assert(enclosedEAcute == "é⃝")
  /> enclosedEAcute is \(enclosedEAcute)
  </ enclosedEAcute is é⃝
  ```
-->

지역 표시 기호를 위한 유니코드 스칼라는 쌍으로 결합하여 단일 `Character` 값을 만들 수 있다. 예를 들어, `REGIONAL INDICATOR SYMBOL LETTER U`(`U+1F1FA`)와 `REGIONAL INDICATOR SYMBOL LETTER S`(`U+1F1F8`)의 조합이 있다:

```swift
let regionalIndicatorForUS: Character = "\u{1F1FA}\u{1F1F8}"
// regionalIndicatorForUS는 🇺🇸
```

<!--
  - test: `graphemeClusters4`

  ```swifttest
  -> let regionalIndicatorForUS: Character = "\u{1F1FA}\u{1F1F8}"
  >> assert(regionalIndicatorForUS == "🇺🇸")
  /> regionalIndicatorForUS is \(regionalIndicatorForUS)
  </ regionalIndicatorForUS is 🇺🇸
  ```
-->


## 문자 수 세기

문자열에 있는 `Character` 값의 개수를 확인하려면 문자열의 `count` 프로퍼티를 사용한다:

```swift
let unusualMenagerie = "Koala 🐨, Snail 🐌, Penguin 🐧, Dromedary 🐪"
print("unusualMenagerie has \(unusualMenagerie.count) characters")
// Prints "unusualMenagerie has 40 characters"
```

<!--
  - test: `characterCount`

  ```swifttest
  -> let unusualMenagerie = "Koala 🐨, Snail 🐌, Penguin 🐧, Dromedary 🐪"
  -> print("unusualMenagerie has \(unusualMenagerie.count) characters")
  <- unusualMenagerie has 40 characters
  ```
-->

Swift는 `Character` 값을 확장된 그래핏 클러스터로 처리하기 때문에, 문자열을 연결하거나 수정해도 항상 문자 수가 바뀌지는 않는다.

예를 들어, 네 글자 단어인 `cafe`로 새로운 문자열을 초기화한 후, 문자열 끝에 `COMBINING ACUTE ACCENT` (`U+0301`)를 추가해도 결과 문자열의 문자 수는 여전히 `4`가 된다. 네 번째 문자는 `e`가 아니라 `é`가 된다:

```swift
var word = "cafe"
print("the number of characters in \(word) is \(word.count)")
// Prints "the number of characters in cafe is 4"

word += "\u{301}"    // COMBINING ACUTE ACCENT, U+0301

print("the number of characters in \(word) is \(word.count)")
// Prints "the number of characters in café is 4"
```

<!--
  - test: `characterCount`

  ```swifttest
  -> var word = "cafe"
  -> print("the number of characters in \(word) is \(word.count)")
  <- the number of characters in cafe is 4

  -> word += "\u{301}"    // COMBINING ACUTE ACCENT, U+0301

  -> print("the number of characters in \(word) is \(word.count)")
  <- the number of characters in café is 4
  ```
-->

> 참고: 확장된 그래핏 클러스터는 여러 유니코드 스칼라로 구성될 수 있다. 이는 서로 다른 문자나 동일한 문자의 다른 표현이 저장에 필요한 메모리 양이 다를 수 있다는 것을 의미한다. 따라서 Swift에서 문자열 내의 각 문자는 동일한 양의 메모리를 차지하지 않는다. 결과적으로, 문자열의 문자 수는 확장된 그래핏 클러스터 경계를 결정하기 위해 문자열을 순회하지 않고는 계산할 수 없다. 특히 긴 문자열 값을 다룰 때는, `count` 프로퍼티가 해당 문자열의 문자를 결정하기 위해 전체 문자열의 유니코드 스칼라를 순회해야 한다는 점을 유의해야 한다.
>
> `count` 프로퍼티가 반환하는 문자 수는 동일한 문자를 포함하는 `NSString`의 `length` 프로퍼티와 항상 일치하지 않는다. `NSString`의 길이는 문자열의 UTF-16 표현 내의 16비트 코드 단위 수를 기반으로 하며, 문자열 내의 유니코드 확장 그래핏 클러스터 수를 기반으로 하지 않는다.


## 문자열 접근 및 수정

문자열에 접근하고 수정하려면 메서드와 프로퍼티를 사용하거나, 서브스크립트 문법을 활용한다.


### 문자열 인덱스

각 `String` 값은 *인덱스 타입*인 `String.Index`와 연결된다. 이 인덱스는 문자열 내 각 `Character`의 위치에 해당한다.

앞서 언급했듯이, 서로 다른 문자는 저장하기 위해 서로 다른 양의 메모리를 요구할 수 있다. 따라서 특정 위치에 있는 `Character`를 확인하려면 해당 `String`의 시작 또는 끝부터 각 유니코드 스칼라를 순회해야 한다. 이러한 이유로 Swift 문자열은 정수 값으로 인덱싱할 수 없다.

`startIndex` 프로퍼티를 사용해 문자열의 첫 번째 `Character`의 위치에 접근한다. `endIndex` 프로퍼티는 문자열의 마지막 문자 다음 위치를 나타낸다. 따라서 `endIndex` 프로퍼티는 문자열의 서브스크립트 인자로 유효하지 않다. 만약 `String`이 비어 있다면, `startIndex`와 `endIndex`는 동일한 값을 가진다.

주어진 인덱스의 앞뒤에 있는 인덱스에 접근하려면 `String`의 `index(before:)`와 `index(after:)` 메서드를 사용한다. 주어진 인덱스에서 더 멀리 떨어진 인덱스에 접근하려면, 이러한 메서드를 여러 번 호출하는 대신 `index(_:offsetBy:)` 메서드를 사용할 수 있다.

서브스크립트 문법을 사용해 특정 `String` 인덱스의 `Character`에 접근할 수 있다.

```swift
let greeting = "Guten Tag!"
greeting[greeting.startIndex]
// G
greeting[greeting.index(before: greeting.endIndex)]
// !
greeting[greeting.index(after: greeting.startIndex)]
// u
let index = greeting.index(greeting.startIndex, offsetBy: 7)
greeting[index]
// a
```

<!--
  - test: `stringIndex`

  ```swifttest
  -> let greeting = "Guten Tag!"
  >> print(
  -> greeting[greeting.startIndex]
  >> )
  << G
  // G
  >> print(
  -> greeting[greeting.index(before: greeting.endIndex)]
  >> )
  << !
  // !
  >> print(
  -> greeting[greeting.index(after: greeting.startIndex)]
  >> )
  << u
  // u
  -> let index = greeting.index(greeting.startIndex, offsetBy: 7)
  >> print(
  -> greeting[index]
  >> )
  << a
  // a
  ```
-->

문자열의 범위를 벗어나는 인덱스에 접근하거나, 문자열의 범위를 벗어나는 인덱스의 `Character`에 접근하려고 하면 런타임 오류가 발생한다.

```swift
greeting[greeting.endIndex] // Error
greeting.index(after: greeting.endIndex) // Error
```

<!--
  The code above triggers an assertion failure in the stdlib, causing a stack
  trace, which makes it a poor candidate for being tested.
-->

<!--
  - test: `emptyStringIndices`

  ```swifttest
  -> let emptyString = ""
  -> assert(
  -> emptyString.isEmpty && emptyString.startIndex == emptyString.endIndex
  -> )
  ```
-->

`indices` 프로퍼티를 사용해 문자열 내 모든 개별 문자의 인덱스에 접근할 수 있다.

```swift
for index in greeting.indices {
    print("\(greeting[index]) ", terminator: "")
}
// Prints "G u t e n   T a g ! "
```

<!--
  - test: `stringIndex`

  ```swifttest
  -> for index in greeting.indices {
        print("\(greeting[index]) ", terminator: "")
     }
  >> print("")
  << G u t e n   T a g !
  // Prints "G u t e n   T a g ! "
  ```
-->

<!--
  Workaround for rdar://26016325
-->

> 참고: `startIndex`와 `endIndex` 프로퍼티, 그리고 `index(before:)`, `index(after:)`, `index(_:offsetBy:)` 메서드는 `Collection` 프로토콜을 준수하는 모든 타입에서 사용할 수 있다. 이는 여기서 보여준 `String`뿐만 아니라 `Array`, `Dictionary`, `Set`과 같은 컬렉션 타입도 포함한다.


### 문자열 삽입과 삭제

특정 인덱스에 단일 문자를 삽입하려면 `insert(_:at:)` 메서드를 사용하고, 다른 문자열의 내용을 특정 인덱스에 삽입하려면 `insert(contentsOf:at:)` 메서드를 사용한다.

```swift
var welcome = "hello"
welcome.insert("!", at: welcome.endIndex)
// welcome은 이제 "hello!"와 같다.

welcome.insert(contentsOf: " there", at: welcome.index(before: welcome.endIndex))
// welcome은 이제 "hello there!"와 같다.
```

<!--
  - test: `stringInsertionAndRemoval`

  ```swifttest
  -> var welcome = "hello"
  -> welcome.insert("!", at: welcome.endIndex)
  /> welcome now equals \"\(welcome)\"
  </ welcome now equals "hello!"

  -> welcome.insert(contentsOf: " there", at: welcome.index(before: welcome.endIndex))
  /> welcome now equals \"\(welcome)\"
  </ welcome now equals "hello there!"
  ```
-->

특정 인덱스에서 단일 문자를 삭제하려면 `remove(at:)` 메서드를 사용하고, 특정 범위의 부분 문자열을 삭제하려면 `removeSubrange(_:)` 메서드를 사용한다:

```swift
welcome.remove(at: welcome.index(before: welcome.endIndex))
// welcome은 이제 "hello there"와 같다.

let range = welcome.index(welcome.endIndex, offsetBy: -6)..<welcome.endIndex
welcome.removeSubrange(range)
// welcome은 이제 "hello"와 같다.
```

<!--
  - test: `stringInsertionAndRemoval`

  ```swifttest
  -> welcome.remove(at: welcome.index(before: welcome.endIndex))
  /> welcome now equals \"\(welcome)\"
  </ welcome now equals "hello there"

  -> let range = welcome.index(welcome.endIndex, offsetBy: -6)..<welcome.endIndex
  -> welcome.removeSubrange(range)
  /> welcome now equals \"\(welcome)\"
  </ welcome now equals "hello"
  ```
-->

<!--
  TODO: Find and Replace section, once the Swift standard library supports finding substrings
-->

> 참고: `insert(_:at:)`, `insert(contentsOf:at:)`, `remove(at:)`, `removeSubrange(_:)` 메서드는 `RangeReplaceableCollection` 프로토콜을 준수하는 모든 타입에서 사용할 수 있다. 여기서 보여준 `String`뿐만 아니라 `Array`, `Dictionary`, `Set`과 같은 컬렉션 타입도 포함된다.


## 부분 문자열

문자열에서 부분 문자열을 가져올 때, 예를 들어 서브스크립트나 `prefix(_:)` 같은 메서드를 사용하면, 그 결과는 [`Substring`](https://developer.apple.com/documentation/swift/substring)의 인스턴스가 된다. Swift에서 부분 문자열은 문자열과 거의 동일한 메서드를 가지고 있기 때문에, 부분 문자열을 다루는 방식도 문자열과 크게 다르지 않다. 그러나 부분 문자열은 문자열과 달리, 문자열에 대한 작업을 수행하는 동안 짧은 시간 동안만 사용한다. 결과를 오랜 시간 동안 저장하려면, 부분 문자열을 `String` 인스턴스로 변환해야 한다. 예를 들어:

```swift
let greeting = "Hello, world!"
let index = greeting.firstIndex(of: ",") ?? greeting.endIndex
let beginning = greeting[..<index]
// beginning은 "Hello"

// 결과를 String으로 변환하여 장기 저장.
let newString = String(beginning)
```

<!--
  - test: `string-and-substring`

  ```swifttest
  -> let greeting = "Hello, world!"
  -> let index = greeting.firstIndex(of: ",") ?? greeting.endIndex
  -> let beginning = greeting[..<index]
  /> beginning is \"\(beginning)\"
  </ beginning is "Hello"

  // Convert the result to a String for long-term storage.
  -> let newString = String(beginning)
  ```
-->

문자열과 마찬가지로, 각 부분 문자열은 해당 문자를 저장하는 메모리 영역을 가지고 있다. 문자열과 부분 문자열의 차이점은, 성능 최적화를 위해 부분 문자열은 원본 문자열이 사용하는 메모리의 일부를 재사용할 수 있다는 점이다. (문자열도 비슷한 최적화를 지원하지만, 두 문자열이 메모리를 공유한다면 두 문자열은 동일하다.) 이 성능 최적화는 문자열이나 부분 문자열을 수정할 때까지 메모리 복사 비용을 지불하지 않아도 된다는 것을 의미한다. 앞서 언급했듯이, 부분 문자열은 장기 저장에 적합하지 않다. 원본 문자열의 저장 공간을 재사용하기 때문에, 부분 문자열이 사용되는 동안 원본 문자열 전체가 메모리에 유지되어야 한다.

위 예제에서 `greeting`은 문자열이며, 이 문자열을 구성하는 문자를 저장하는 메모리 영역을 가지고 있다. `beginning`은 `greeting`의 부분 문자열이기 때문에, `greeting`이 사용하는 메모리를 재사용한다. 반면에 `newString`은 문자열로, 부분 문자열에서 생성될 때 자신만의 저장 공간을 가진다. 아래 그림은 이러한 관계를 보여준다:

![](stringSubstring)

> 참고: `String`과 `Substring`은 모두 [`StringProtocol`](https://developer.apple.com/documentation/swift/stringprotocol) 프로토콜을 준수한다. 이는 문자열 조작 함수가 `StringProtocol` 값을 받아들이는 것이 편리하다는 것을 의미한다. 따라서 `String`이나 `Substring` 값으로 이러한 함수를 호출할 수 있다.


## 문자열 비교하기

Swift는 텍스트 값을 비교하는 세 가지 방법을 제공한다: 문자열과 문자 동등성 비교, 접두사 동등성 비교, 접미사 동등성 비교다.


### 문자열과 문자 동등성 비교

문자열과 문자의 동등성은 "같음" 연산자(`==`)와 "같지 않음" 연산자(`!=`)를 사용해 확인한다. 이는 <doc:BasicOperators#Comparison-Operators>에서 설명한 바와 같다:

```swift
let quotation = "We're a lot alike, you and I."
let sameQuotation = "We're a lot alike, you and I."
if quotation == sameQuotation {
    print("These two strings are considered equal")
}
// Prints "These two strings are considered equal"
```

<!--
  - test: `stringEquality`

  ```swifttest
  -> let quotation = "We're a lot alike, you and I."
  -> let sameQuotation = "We're a lot alike, you and I."
  -> if quotation == sameQuotation {
        print("These two strings are considered equal")
     }
  <- These two strings are considered equal
  ```
-->

두 `String` 값(또는 두 `Character` 값)은 확장 그래핌 클러스터가 *정규적으로 동등*할 경우 동일한 것으로 간주한다. 확장 그래핌 클러스터는 언어적 의미와 외관이 동일하면 정규적으로 동등하다. 이는 내부적으로 다른 유니코드 스칼라로 구성된 경우에도 마찬가지다.

<!--
  - test: `characterComparisonUsesCanonicalEquivalence`

  ```swifttest
  -> let eAcute: Character = "\u{E9}"
  -> let combinedEAcute: Character = "\u{65}\u{301}"
  -> if eAcute != combinedEAcute {
        print("not equivalent, which isn't expected")
     } else {
        print("equivalent, as expected")
     }
  <- equivalent, as expected
  ```
-->

<!--
  - test: `stringComparisonUsesCanonicalEquivalence`

  ```swifttest
  -> let cafe1 = "caf\u{E9}"
  -> let cafe2 = "caf\u{65}\u{301}"
  -> if cafe1 != cafe2 {
        print("not equivalent, which isn't expected")
     } else {
        print("equivalent, as expected")
     }
  <- equivalent, as expected
  ```
-->

예를 들어, `LATIN SMALL LETTER E WITH ACUTE` (`U+00E9`)는 `LATIN SMALL LETTER E` (`U+0065`)와 `COMBINING ACUTE ACCENT` (`U+0301`)의 조합과 정규적으로 동등하다. 이 두 확장 그래핌 클러스터는 모두 `é` 문자를 나타내는 유효한 방법이며, 따라서 정규적으로 동등하다고 간주된다:

```swift
// "Voulez-vous un café?" using LATIN SMALL LETTER E WITH ACUTE
let eAcuteQuestion = "Voulez-vous un caf\u{E9}?"

// "Voulez-vous un café?" using LATIN SMALL LETTER E and COMBINING ACUTE ACCENT
let combinedEAcuteQuestion = "Voulez-vous un caf\u{65}\u{301}?"

if eAcuteQuestion == combinedEAcuteQuestion {
    print("These two strings are considered equal")
}
// Prints "These two strings are considered equal"
```

<!--
  - test: `stringEquality`

  ```swifttest
  // "Voulez-vous un café?" using LATIN SMALL LETTER E WITH ACUTE
  -> let eAcuteQuestion = "Voulez-vous un caf\u{E9}?"

  // "Voulez-vous un café?" using LATIN SMALL LETTER E and COMBINING ACUTE ACCENT
  -> let combinedEAcuteQuestion = "Voulez-vous un caf\u{65}\u{301}?"

  -> if eAcuteQuestion == combinedEAcuteQuestion {
        print("These two strings are considered equal")
     }
  <- These two strings are considered equal
  ```
-->

반대로, 영어에서 사용되는 `LATIN CAPITAL LETTER A` (`U+0041`, 또는 `"A"`)는 러시아어에서 사용되는 `CYRILLIC CAPITAL LETTER A` (`U+0410`, 또는 `"А"`)와 동등하지 않다. 두 문자는 시각적으로 유사하지만, 언어적 의미가 다르다:

```swift
let latinCapitalLetterA: Character = "\u{41}"

let cyrillicCapitalLetterA: Character = "\u{0410}"

if latinCapitalLetterA != cyrillicCapitalLetterA {
    print("These two characters aren't equivalent.")
}
// Prints "These two characters aren't equivalent."
```

<!--
  - test: `stringEquality`

  ```swifttest
  -> let latinCapitalLetterA: Character = "\u{41}"
  >> assert(latinCapitalLetterA == "A")

  -> let cyrillicCapitalLetterA: Character = "\u{0410}"
  >> assert(cyrillicCapitalLetterA == "А")

  -> if latinCapitalLetterA != cyrillicCapitalLetterA {
        print("These two characters aren't equivalent.")
     }
  <- These two characters aren't equivalent.
  ```
-->

> 참고: Swift에서 문자열과 문자 비교는 로캘에 영향을 받지 않는다.

<!--
  TODO: Add a cross reference to NSString.localizedCompare and
  NSString.localizedCaseInsensitiveCompare.  See also
  https://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/Strings/Articles/SearchingStrings.html#//apple_ref/doc/uid/20000149-SW4
-->


### 접두사와 접미사 비교

특정 문자열이 특정 접두사나 접미사를 가지고 있는지 확인하려면, 문자열의 `hasPrefix(_:)`와 `hasSuffix(_:)` 메서드를 사용한다. 이 두 메서드는 모두 `String` 타입의 단일 인자를 받고, Boolean 값을 반환한다.

<!--
  - test: `prefixComparisonUsesCharactersNotScalars`

  ```swifttest
  -> let ecole = "\u{E9}cole"
  -> if ecole.hasPrefix("\u{E9}") {
        print("Has U+00E9 prefix, as expected.")
     } else {
        print("Does not have U+00E9 prefix, which is unexpected.")
     }
  <- Has U+00E9 prefix, as expected.
  -> if ecole.hasPrefix("\u{65}\u{301}") {
        print("Has U+0065 U+0301 prefix, as expected.")
     } else {
        print("Does not have U+0065 U+0301 prefix, which is unexpected.")
     }
  <- Has U+0065 U+0301 prefix, as expected.
  ```
-->

<!--
  - test: `suffixComparisonUsesCharactersNotScalars`

  ```swifttest
  -> let cafe = "caf\u{E9}"
  -> if cafe.hasSuffix("\u{E9}") {
        print("Has U+00E9 suffix, as expected.")
     } else {
        print("Does not have U+00E9 suffix, which is unexpected.")
     }
  <- Has U+00E9 suffix, as expected.
  -> if cafe.hasSuffix("\u{65}\u{301}") {
        print("Has U+0065 U+0301 suffix, as expected.")
     } else {
        print("Does not have U+0065 U+0301 suffix, which is unexpected.")
     }
  <- Has U+0065 U+0301 suffix, as expected.
  ```
-->

아래 예제는 셰익스피어의 *로미오와 줄리엣*의 첫 두 막에서 나오는 장면의 위치를 나타내는 문자열 배열을 사용한다:

```swift
let romeoAndJuliet = [
    "Act 1 Scene 1: Verona, A public place",
    "Act 1 Scene 2: Capulet's mansion",
    "Act 1 Scene 3: A room in Capulet's mansion",
    "Act 1 Scene 4: A street outside Capulet's mansion",
    "Act 1 Scene 5: The Great Hall in Capulet's mansion",
    "Act 2 Scene 1: Outside Capulet's mansion",
    "Act 2 Scene 2: Capulet's orchard",
    "Act 2 Scene 3: Outside Friar Lawrence's cell",
    "Act 2 Scene 4: A street in Verona",
    "Act 2 Scene 5: Capulet's mansion",
    "Act 2 Scene 6: Friar Lawrence's cell"
]
```

<!--
  - test: `prefixesAndSuffixes`

  ```swifttest
  -> let romeoAndJuliet = [
        "Act 1 Scene 1: Verona, A public place",
        "Act 1 Scene 2: Capulet's mansion",
        "Act 1 Scene 3: A room in Capulet's mansion",
        "Act 1 Scene 4: A street outside Capulet's mansion",
        "Act 1 Scene 5: The Great Hall in Capulet's mansion",
        "Act 2 Scene 1: Outside Capulet's mansion",
        "Act 2 Scene 2: Capulet's orchard",
        "Act 2 Scene 3: Outside Friar Lawrence's cell",
        "Act 2 Scene 4: A street in Verona",
        "Act 2 Scene 5: Capulet's mansion",
        "Act 2 Scene 6: Friar Lawrence's cell"
     ]
  ```
-->

`hasPrefix(_:)` 메서드를 사용해 `romeoAndJuliet` 배열에서 1막에 나오는 장면의 수를 세어볼 수 있다:

```swift
var act1SceneCount = 0
for scene in romeoAndJuliet {
    if scene.hasPrefix("Act 1 ") {
        act1SceneCount += 1
    }
}
print("There are \(act1SceneCount) scenes in Act 1")
// Prints "There are 5 scenes in Act 1"
```

<!--
  - test: `prefixesAndSuffixes`

  ```swifttest
  -> var act1SceneCount = 0
  -> for scene in romeoAndJuliet {
        if scene.hasPrefix("Act 1 ") {
           act1SceneCount += 1
        }
     }
  -> print("There are \(act1SceneCount) scenes in Act 1")
  <- There are 5 scenes in Act 1
  ```
-->

마찬가지로 `hasSuffix(_:)` 메서드를 사용해 Capulet의 저택과 Friar Lawrence의 방에서 일어나는 장면의 수를 세어볼 수 있다:

```swift
var mansionCount = 0
var cellCount = 0
for scene in romeoAndJuliet {
    if scene.hasSuffix("Capulet's mansion") {
        mansionCount += 1
    } else if scene.hasSuffix("Friar Lawrence's cell") {
        cellCount += 1
    }
}
print("\(mansionCount) mansion scenes; \(cellCount) cell scenes")
// Prints "6 mansion scenes; 2 cell scenes"
```

<!--
  - test: `prefixesAndSuffixes`

  ```swifttest
  -> var mansionCount = 0
  -> var cellCount = 0
  -> for scene in romeoAndJuliet {
        if scene.hasSuffix("Capulet's mansion") {
           mansionCount += 1
        } else if scene.hasSuffix("Friar Lawrence's cell") {
           cellCount += 1
        }
     }
  -> print("\(mansionCount) mansion scenes; \(cellCount) cell scenes")
  <- 6 mansion scenes; 2 cell scenes
  ```
-->

> 참고: `hasPrefix(_:)`와 `hasSuffix(_:)` 메서드는 각 문자열의 확장 문자 클러스터 간에 문자 단위의 정규화된 동등성을 비교한다. 이에 대한 자세한 내용은 <doc:StringsAndCharacters#String-and-Character-Equality>에서 확인할 수 있다.


## 문자열의 유니코드 표현

유니코드 문자열을 텍스트 파일이나 다른 저장소에 기록할 때, 해당 문자열의 유니코드 스칼라는 여러 유니코드 정의 *인코딩 형식* 중 하나로 인코딩된다. 각 형식은 문자열을 *코드 단위*라는 작은 단위로 인코딩한다. 이에는 UTF-8 인코딩 형식(문자열을 8비트 코드 단위로 인코딩), UTF-16 인코딩 형식(문자열을 16비트 코드 단위로 인코딩), 그리고 UTF-32 인코딩 형식(문자열을 32비트 코드 단위로 인코딩)이 포함된다.

Swift는 문자열의 유니코드 표현에 접근하는 여러 방법을 제공한다. `for`-`in` 문을 사용하여 문자열을 반복하면서 개별 `Character` 값을 유니코드 확장 그래핀 클러스터로 접근할 수 있다. 이 과정은 <doc:StringsAndCharacters#Working-with-Characters>에서 설명한다.

또는, `String` 값을 세 가지 다른 유니코드 호환 표현 중 하나로 접근할 수 있다:

- UTF-8 코드 단위의 컬렉션(문자열의 `utf8` 프로퍼티로 접근)
- UTF-16 코드 단위의 컬렉션(문자열의 `utf16` 프로퍼티로 접근)
- 21비트 유니코드 스칼라 값의 컬렉션, 문자열의 UTF-32 인코딩 형식과 동일(문자열의 `unicodeScalars` 프로퍼티로 접근)

아래 예제는 각각 다른 표현으로 다음 문자열을 보여준다. 이 문자열은 `D`, `o`, `g`, `‼` (`DOUBLE EXCLAMATION MARK`, 유니코드 스칼라 `U+203C`), 그리고 🐶 문자(`DOG FACE`, 유니코드 스칼라 `U+1F436`)로 구성된다:

```swift
let dogString = "Dog‼🐶"
```

<!--
  - test: `unicodeRepresentations`

  ```swifttest
  -> let dogString = "Dog‼🐶"
  ```
-->


### UTF-8 표현

`String`의 UTF-8 표현에 접근하려면 `utf8` 프로퍼티를 통해 반복하면 된다. 이 프로퍼티는 `String.UTF8View` 타입으로, 문자열의 UTF-8 표현에서 각 바이트에 해당하는 부호 없는 8비트(`UInt8`) 값의 컬렉션이다:

![](UTF8)

```swift
for codeUnit in dogString.utf8 {
    print("\(codeUnit) ", terminator: "")
}
print("")
// Prints "68 111 103 226 128 188 240 159 144 182 "
```

<!--
  - test: `unicodeRepresentations`

  ```swifttest
  -> for codeUnit in dogString.utf8 {
        print("\(codeUnit) ", terminator: "")
     }
  -> print("")
  << 68 111 103 226 128 188 240 159 144 182
  // Prints "68 111 103 226 128 188 240 159 144 182 "
  ```
-->

<!--
  Workaround for rdar://26016325
-->

위 예제에서 처음 세 개의 10진수 `codeUnit` 값(`68`, `111`, `103`)은 `D`, `o`, `g` 문자를 나타내며, 이들의 UTF-8 표현은 ASCII 표현과 동일하다. 다음 세 개의 10진수 `codeUnit` 값(`226`, `128`, `188`)은 `DOUBLE EXCLAMATION MARK` 문자의 3바이트 UTF-8 표현이다. 마지막 네 개의 `codeUnit` 값(`240`, `159`, `144`, `182`)은 `DOG FACE` 문자의 4바이트 UTF-8 표현이다.

<!--
  TODO: contiguousUTF8()
-->

<!--
  TODO: nulTerminatedUTF8()
  (which returns a NativeArray, but handwave this for now)
-->


### UTF-16 표현

`String`의 UTF-16 표현은 `utf16` 프로퍼티를 통해 접근할 수 있다. 이 프로퍼티는 `String.UTF16View` 타입으로, 문자열의 UTF-16 표현에서 각 16비트 코드 유닛에 해당하는 부호 없는 16비트(`UInt16`) 값의 컬렉션이다:

![](UTF16)

```swift
for codeUnit in dogString.utf16 {
    print("\(codeUnit) ", terminator: "")
}
print("")
// Prints "68 111 103 8252 55357 56374 "
```

<!--
  - test: `unicodeRepresentations`

  ```swifttest
  -> for codeUnit in dogString.utf16 {
        print("\(codeUnit) ", terminator: "")
     }
  -> print("")
  << 68 111 103 8252 55357 56374
  // Prints "68 111 103 8252 55357 56374 "
  ```
-->

<!--
  Workaround for rdar://26016325
-->

첫 세 개의 `codeUnit` 값(`68`, `111`, `103`)은 각각 `D`, `o`, `g` 문자를 나타낸다. 이 값들은 문자열의 UTF-8 표현과 동일한 값을 가지는데, 이 유니코드 스칼라가 ASCII 문자를 나타내기 때문이다.

네 번째 `codeUnit` 값(`8252`)은 16진수 값 `203C`의 10진수 표현으로, `DOUBLE EXCLAMATION MARK` 문자에 해당하는 유니코드 스칼라 `U+203C`를 나타낸다. 이 문자는 UTF-16에서 단일 코드 유닛으로 표현될 수 있다.

다섯 번째와 여섯 번째 `codeUnit` 값(`55357`과 `56374`)은 `DOG FACE` 문자의 UTF-16 서로게이트 쌍 표현이다. 이 값들은 상위 서로게이트 값 `U+D83D`(10진수 값 `55357`)과 하위 서로게이트 값 `U+DC36`(10진수 값 `56374`)로 구성된다.


### 유니코드 스칼라 표현

`String` 값의 유니코드 스칼라 표현에 접근하려면 `unicodeScalars` 프로퍼티를 통해 반복하면 된다. 이 프로퍼티는 `UnicodeScalarView` 타입으로, `UnicodeScalar` 타입의 값들을 담고 있는 컬렉션이다.

각 `UnicodeScalar`는 `value` 프로퍼티를 가지고 있으며, 이는 스칼라의 21비트 값을 `UInt32` 값으로 반환한다:

![](UnicodeScalar)

```swift
for scalar in dogString.unicodeScalars {
    print("\(scalar.value) ", terminator: "")
}
print("")
// Prints "68 111 103 8252 128054 "
```

<!--
  - test: `unicodeRepresentations`

  ```swifttest
  -> for scalar in dogString.unicodeScalars {
        print("\(scalar.value) ", terminator: "")
     }
  -> print("")
  << 68 111 103 8252 128054
  // Prints "68 111 103 8252 128054 "
  ```
-->

<!--
  Workaround for rdar://26016325
-->

첫 세 개의 `UnicodeScalar` 값(`68`, `111`, `103`)은 각각 `D`, `o`, `g` 문자를 나타낸다.

네 번째 `codeUnit` 값(`8252`)은 16진수 값 `203C`의 십진수 표현으로, `DOUBLE EXCLAMATION MARK` 문자를 나타내는 유니코드 스칼라 `U+203C`에 해당한다.

다섯 번째이자 마지막 `UnicodeScalar`의 `value` 프로퍼티 값인 `128054`은 16진수 값 `1F436`의 십진수 표현으로, `DOG FACE` 문자를 나타내는 유니코드 스칼라 `U+1F436`에 해당한다.

`value` 프로퍼티를 조회하는 대신, 각 `UnicodeScalar` 값을 사용해 새로운 `String` 값을 생성할 수도 있다. 예를 들어 문자열 보간을 사용하는 방법이 있다:

```swift
for scalar in dogString.unicodeScalars {
    print("\(scalar) ")
}
// D
// o
// g
// ‼
// 🐶
```

<!--
  - test: `unicodeRepresentations`

  ```swifttest
  -> for scalar in dogString.unicodeScalars {
        print("\(scalar) ")
     }
  </ D
  </ o
  </ g
  </ ‼
  </ 🐶
  ```
-->

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


