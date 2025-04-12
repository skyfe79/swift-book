# Swift 둘러보기

Swift의 기능과 문법을 탐구한다.

새로운 언어를 배울 때 첫 번째 프로그램은 화면에 "Hello, world!"를 출력하는 것이 전통이다. Swift에서는 이를 단 한 줄로 구현할 수 있다.

```swift
print("Hello, world!")
// Prints "Hello, world!"
```

다른 언어를 알고 있다면 이 구문이 익숙할 것이다. Swift에서는 이 한 줄이 완전한 프로그램이다. 텍스트를 출력하거나 문자열을 처리하는 기능을 위해 별도의 라이브러리를 임포트할 필요가 없다. 전역 범위에 작성된 코드가 프로그램의 시작점으로 사용되므로 `main()` 함수가 필요하지 않다. 또한 모든 문장 끝에 세미콜론을 작성할 필요도 없다.

이 둘러보기는 다양한 프로그래밍 작업을 수행하는 방법을 보여줌으로써 Swift로 코드를 작성하기에 충분한 정보를 제공한다. 이해가 되지 않는 부분이 있어도 걱정하지 말자. 이 둘러보기에서 소개된 모든 내용은 이 책의 나머지 부분에서 자세히 설명된다.


## 간단한 값

상수를 만들 때는 `let`을, 변수를 만들 때는 `var`를 사용한다. 상수의 값은 컴파일 시점에 알 필요가 없지만, 반드시 한 번만 값을 할당해야 한다. 즉, 한 번 결정한 값을 여러 곳에서 사용할 때 상수를 활용할 수 있다.

```swift
var myVariable = 42
myVariable = 50
let myConstant = 42
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> var myVariable = 42
  -> myVariable = 50
  -> let myConstant = 42
  ```
-->

상수나 변수는 할당하려는 값과 같은 타입이어야 한다. 하지만 항상 타입을 명시적으로 작성할 필요는 없다. 상수나 변수를 생성할 때 값을 제공하면 컴파일러가 타입을 추론한다. 위 예제에서 컴파일러는 `myVariable`이 정수 타입임을 추론한다. 초기 값이 정수이기 때문이다.

초기 값이 충분한 정보를 제공하지 않거나 초기 값이 없는 경우, 변수 뒤에 콜론을 붙이고 타입을 명시한다.

```swift
let implicitInteger = 70
let implicitDouble = 70.0
let explicitDouble: Double = 70
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> let implicitInteger = 70
  -> let implicitDouble = 70.0
  -> let explicitDouble: Double = 70
  ```
-->

> 실험: `Float` 타입으로 명시적으로 지정된 상수를 만들고 값을 4로 설정해 보자.

값은 절대 암시적으로 다른 타입으로 변환되지 않는다. 값을 다른 타입으로 변환해야 한다면, 원하는 타입의 인스턴스를 명시적으로 생성한다.

```swift
let label = "The width is "
let width = 94
let widthLabel = label + String(width)
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> let label = "The width is "
  -> let width = 94
  -> let widthLabel = label + String(width)
  >> print(widthLabel)
  << The width is 94
  ```
-->

> 실험: 마지막 줄에서 `String`으로의 변환을 제거해 보자. 어떤 오류가 발생하는가?

문자열에 값을 포함하는 더 간단한 방법도 있다. 값을 괄호 안에 넣고, 괄호 앞에 백슬래시(`\`)를 작성한다. 예를 들어:

```swift
let apples = 3
let oranges = 5
let appleSummary = "I have \(apples) apples."
let fruitSummary = "I have \(apples + oranges) pieces of fruit."
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> let apples = 3
  -> let oranges = 5
  -> let appleSummary = "I have \(apples) apples."
  >> print(appleSummary)
  << I have 3 apples.
  -> let fruitSummary = "I have \(apples + oranges) pieces of fruit."
  >> print(fruitSummary)
  << I have 8 pieces of fruit.
  ```
-->

> 실험: `\()`를 사용해 부동소수점 계산을 문자열에 포함시키고, 누군가의 이름을 인사말에 포함시켜 보자.

여러 줄에 걸친 문자열은 세 개의 큰따옴표(`"""`)를 사용한다. 각 줄의 시작 부분에 있는 들여쓰기는 닫는 따옴표의 들여쓰기와 일치하는 한 제거된다. 예를 들어:

```swift
let quotation = """
        Even though there's whitespace to the left,
        the actual lines aren't indented.
            Except for this line.
        Double quotes (") can appear without being escaped.

        I still have \(apples + oranges) pieces of fruit.
        """
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> let quotation = """
     I said "I have \(apples) apples."
     And then I said "I have \(apples + oranges) pieces of fruit."
     """
  ```
-->

배열과 딕셔너리는 대괄호(`[]`)를 사용해 생성하고, 인덱스나 키를 대괄호 안에 작성해 요소에 접근한다. 마지막 요소 뒤에 쉼표를 사용할 수 있다.

```swift
var fruits = ["strawberries", "limes", "tangerines"]
fruits[1] = "grapes"

var occupations = [
    "Malcolm": "Captain",
    "Kaylee": "Mechanic",
 ]
occupations["Jayne"] = "Public Relations"
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> var fruits = ["strawberries", "limes", "tangerines"]
  -> fruits[1] = "grapes"

  -> var occupations = [
         "Malcolm": "Captain",
         "Kaylee": "Mechanic",
      ]
  -> occupations["Jayne"] = "Public Relations"
  ```
-->

배열은 요소를 추가하면 자동으로 크기가 늘어난다.

```swift
fruits.append("blueberries")
print(fruits)
// Prints "["strawberries", "grapes", "tangerines", "blueberries"]"
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> fruits.append("blueberries")
  -> print(fruits)
  <- ["strawberries", "grapes", "tangerines", "blueberries"]
  ```
-->

빈 배열이나 딕셔너리를 생성할 때도 대괄호를 사용한다. 배열은 `[]`, 딕셔너리는 `[:]`로 작성한다.

```swift
fruits = []
occupations = [:]
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> fruits = []
  -> occupations = [:]
  ```
-->

빈 배열이나 딕셔너리를 새로운 변수에 할당하거나 타입 정보가 없는 곳에 할당할 때는 타입을 명시해야 한다.

```swift
let emptyArray: [String] = []
let emptyDictionary: [String: Float] = [:]
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> let emptyArray: [String] = []
  -> let emptyDictionary: [String: Float] = [:]

  -> let anotherEmptyArray = [String]()
  -> let emptyDictionary = [String: Float]()
  ```
-->


## 제어 흐름

조건문을 만들 때 `if`와 `switch`를 사용하고, 반복문을 만들 때 `for`-`in`, `while`, `repeat`-`while`을 사용한다. 조건이나 반복 변수를 감싸는 괄호는 선택 사항이지만, 본문을 감싸는 중괄호는 필수이다.

```swift
let individualScores = [75, 43, 103, 87, 12]
var teamScore = 0
for score in individualScores {
    if score > 50 {
        teamScore += 3
    } else {
        teamScore += 1
    }
}
print(teamScore)
// Prints "11"
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> let individualScores = [75, 43, 103, 87, 12]
  -> var teamScore = 0
  -> for score in individualScores {
         if score > 50 {
             teamScore += 3
         } else {
             teamScore += 1
         }
     }
  -> print(teamScore)
  <- 11
  ```
-->

<!--
  REFERENCE
  Jelly babies are a candy/sweet that was closely associated
  with past incarnations of the Doctor in Dr. Who.
-->

<!--
  -> let haveJellyBabies = true
  -> if haveJellyBabies {
     }
  << Would you like a jelly baby?
-->

`if` 문에서 조건은 반드시 불리언(Boolean) 표현식이어야 한다. 예를 들어 `if score { ... }`와 같은 코드는 에러를 발생시키며, 암시적으로 0과 비교하지 않는다.

`if`나 `switch`를 할당 연산자(`=`) 뒤나 `return` 뒤에 사용하여 조건에 따라 값을 선택할 수 있다.

```swift
let scoreDecoration = if teamScore > 10 {
    "🎉"
} else {
    ""
}
print("Score:", teamScore, scoreDecoration)
// Prints "Score: 11 🎉"
```

`if`와 `let`을 함께 사용하여 값이 없을 수도 있는 상황을 처리할 수 있다. 이러한 값은 옵셔널로 표현된다. 옵셔널 값은 값을 포함하거나, 값이 없음을 나타내는 `nil`을 포함한다. 값의 타입 뒤에 물음표(`?`)를 붙여 옵셔널로 표시한다.

```swift
var optionalString: String? = "Hello"
print(optionalString == nil)
// Prints "false"

var optionalName: String? = "John Appleseed"
var greeting = "Hello!"
if let name = optionalName {
    greeting = "Hello, \(name)"
}
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> var optionalString: String? = "Hello"
  -> print(optionalString == nil)
  <- false

  -> var optionalName: String? = "John Appleseed"
  -> var greeting = "Hello!"
  -> if let name = optionalName {
         greeting = "Hello, \(name)"
     }
  >> print(greeting)
  << Hello, John Appleseed
  ```
-->

> 실험: `optionalName`을 `nil`로 변경해 보자. 어떤 인사말이 나오는가? `optionalName`이 `nil`일 때 다른 인사말을 설정하는 `else` 절을 추가해 보자.

옵셔널 값이 `nil`이면 조건은 `false`가 되고 중괄호 안의 코드는 실행되지 않는다. 그렇지 않으면 옵셔널 값이 언래핑되어 `let` 뒤의 상수에 할당되며, 이 언래핑된 값은 코드 블록 내에서 사용할 수 있다.

옵셔널 값을 처리하는 또 다른 방법은 `??` 연산자를 사용해 기본값을 제공하는 것이다. 옵셔널 값이 없으면 대신 기본값이 사용된다.

```swift
let nickname: String? = nil
let fullName: String = "John Appleseed"
let informalGreeting = "Hi \(nickname ?? fullName)"
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> let nickname: String? = nil
  -> let fullName: String = "John Appleseed"
  -> let informalGreeting = "Hi \(nickname ?? fullName)"
  >> print(informalGreeting)
  << Hi John Appleseed
  ```
-->

같은 이름을 사용하여 값을 더 짧게 언래핑할 수도 있다.

```swift
if let nickname {
    print("Hey, \(nickname)")
}
// Doesn't print anything, because nickname is nil.
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> if let nickname {
         print("Hey, \(nickname)")
     }
  ```
-->

`switch`는 다양한 종류의 데이터와 비교 연산을 지원한다. 정수와 동등성 테스트에만 제한되지 않는다.

```swift
let vegetable = "red pepper"
switch vegetable {
case "celery":
    print("Add some raisins and make ants on a log.")
case "cucumber", "watercress":
    print("That would make a good tea sandwich.")
case let x where x.hasSuffix("pepper"):
    print("Is it a spicy \(x)?")
default:
    print("Everything tastes good in soup.")
}
// Prints "Is it a spicy red pepper?"
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> let vegetable = "red pepper"
  -> switch vegetable {
         case "celery":
             print("Add some raisins and make ants on a log.")
         case "cucumber", "watercress":
             print("That would make a good tea sandwich.")
         case let x where x.hasSuffix("pepper"):
             print("Is it a spicy \(x)?")
         default:
             print("Everything tastes good in soup.")
     }
  <- Is it a spicy red pepper?
  ```
-->

> 실험: `default` 케이스를 제거해 보자. 어떤 에러가 발생하는가?

패턴에서 `let`을 사용하여 패턴에 일치하는 값을 상수에 할당할 수 있다.

`switch` 케이스 내부의 코드를 실행한 후, 프로그램은 `switch` 문을 빠져나간다. 다음 케이스로 실행이 이어지지 않으므로 각 케이스의 코드 끝에서 명시적으로 `break`를 사용할 필요가 없다.

`for`-`in`을 사용하여 딕셔너리의 항목을 반복할 때 각 키-값 쌍에 사용할 이름 쌍을 제공한다. 딕셔너리는 순서가 없는 컬렉션이므로 키와 값은 임의의 순서로 반복된다.

```swift
let interestingNumbers = [
    "Prime": [2, 3, 5, 7, 11, 13],
    "Fibonacci": [1, 1, 2, 3, 5, 8],
    "Square": [1, 4, 9, 16, 25],
]
var largest = 0
for (_, numbers) in interestingNumbers {
    for number in numbers {
        if number > largest {
            largest = number
        }
    }
}
print(largest)
// Prints "25"
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> let interestingNumbers = [
         "Prime": [2, 3, 5, 7, 11, 13],
         "Fibonacci": [1, 1, 2, 3, 5, 8],
         "Square": [1, 4, 9, 16, 25],
     ]
  -> var largest = 0
  -> for (_, numbers) in interestingNumbers {
         for number in numbers {
             if number > largest {
                 largest = number
             }
         }
     }
  -> print(largest)
  <- 25
  ```
-->

> 실험: `_`를 변수 이름으로 바꾸고, 어떤 종류의 숫자가 가장 큰지 추적해 보자.

`while`을 사용하여 조건이 변경될 때까지 코드 블록을 반복한다. 루프의 조건을 끝에 두면 루프가 최소한 한 번은 실행되도록 보장할 수 있다.

```swift
var n = 2
while n < 100 {
    n *= 2
}
print(n)
// Prints "128"

var m = 2
repeat {
    m *= 2
} while m < 100
print(m)
// Prints "128"
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> var n = 2
  -> while n < 100 {
         n *= 2
     }
  -> print(n)
  <- 128

  -> var m = 2
  -> repeat {
         m *= 2
     } while m < 100
  -> print(m)
  <- 128
  ```
-->

> 실험: 조건을 `m < 100`에서 `m < 0`으로 변경하여 `while`과 `repeat`-`while`이 루프 조건이 이미 거짓일 때 어떻게 다르게 동작하는지 확인해 보자.

`..<`를 사용하여 인덱스 범위를 만들고 루프에서 인덱스를 유지할 수 있다.

```swift
var total = 0
for i in 0..<4 {
    total += i
}
print(total)
// Prints "6"
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> var total = 0
  -> for i in 0..<4 {
         total += i
     }
  -> print(total)
  <- 6
  ```
-->

`..<`는 상한 값을 제외한 범위를 만들고, `...`는 상한 값을 포함한 범위를 만든다.


## 함수와 클로저

`func` 키워드를 사용해 함수를 선언한다. 함수를 호출할 때는 함수 이름 뒤에 괄호 안에 인자를 나열한다. `->`를 사용해 매개변수 이름과 타입을 함수의 반환 타입과 구분한다.

```swift
func greet(person: String, day: String) -> String {
    return "Hello \(person), today is \(day)."
}
greet(person: "Bob", day: "Tuesday")
```

> 실험: `day` 매개변수를 제거하고, 오늘의 점심 특선을 포함하는 매개변수를 추가해 보자.

기본적으로 함수는 매개변수 이름을 인자 레이블로 사용한다. 매개변수 이름 앞에 커스텀 인자 레이블을 작성하거나, `_`를 사용해 인자 레이블을 생략할 수 있다.

```swift
func greet(_ person: String, on day: String) -> String {
    return "Hello \(person), today is \(day)."
}
greet("John", on: "Wednesday")
```

튜플을 사용해 복합 값을 만들 수 있다. 예를 들어, 함수에서 여러 값을 반환할 때 유용하다. 튜플의 요소는 이름이나 숫자로 참조할 수 있다.

```swift
func calculateStatistics(scores: [Int]) -> (min: Int, max: Int, sum: Int) {
    var min = scores[0]
    var max = scores[0]
    var sum = 0

    for score in scores {
        if score > max {
            max = score
        } else if score < min {
            min = score
        }
        sum += score
    }

    return (min, max, sum)
}
let statistics = calculateStatistics(scores: [5, 3, 100, 3, 9])
print(statistics.sum)
// "120" 출력
print(statistics.2)
// "120" 출력
```

함수는 중첩될 수 있다. 중첩 함수는 외부 함수에서 선언된 변수에 접근할 수 있다. 중첩 함수를 사용해 길거나 복잡한 함수의 코드를 정리할 수 있다.

```swift
func returnFifteen() -> Int {
    var y = 10
    func add() {
        y += 5
    }
    add()
    return y
}
returnFifteen()
```

함수는 퍼스트클래스 타입이다. 이는 함수가 다른 함수를 반환 값으로 가질 수 있음을 의미한다.

```swift
func makeIncrementer() -> ((Int) -> Int) {
    func addOne(number: Int) -> Int {
        return 1 + number
    }
    return addOne
}
var increment = makeIncrementer()
increment(7)
```

함수는 다른 함수를 인자로 받을 수 있다.

```swift
func hasAnyMatches(list: [Int], condition: (Int) -> Bool) -> Bool {
    for item in list {
        if condition(item) {
            return true
        }
    }
    return false
}
func lessThanTen(number: Int) -> Bool {
    return number < 10
}
var numbers = [20, 19, 7, 12]
hasAnyMatches(list: numbers, condition: lessThanTen)
```

함수는 클로저의 특수한 경우다. 클로저는 나중에 호출할 수 있는 코드 블록이다. 클로저 내부의 코드는 클로저가 생성된 스코프에서 사용 가능한 변수와 함수에 접근할 수 있다. 클로저가 실행될 때 다른 스코프에 있더라도 접근이 가능하다. 중첩 함수에서 이미 이 예를 보았다. 이름 없는 클로저를 작성하려면 코드를 중괄호(`{}`)로 감싼다. `in`을 사용해 인자와 반환 타입을 본문과 구분한다.

```swift
numbers.map({ (number: Int) -> Int in
    let result = 3 * number
    return result
})
```

> 실험: 모든 홀수에 대해 0을 반환하도록 클로저를 다시 작성해 보자.

클로저를 더 간결하게 작성하는 여러 방법이 있다. 클로저의 타입이 이미 알려져 있을 때, 예를 들어 델리게이트의 콜백인 경우, 매개변수 타입, 반환 타입 또는 둘 다 생략할 수 있다. 단일 문장 클로저는 암시적으로 해당 문장의 값을 반환한다.

```swift
let mappedNumbers = numbers.map({ number in 3 * number })
print(mappedNumbers)
// "[60, 57, 21, 36]" 출력
```

매개변수를 이름 대신 숫자로 참조할 수 있다. 이 방법은 매우 짧은 클로저에서 특히 유용하다. 함수의 마지막 인자로 전달된 클로저는 괄호 바로 뒤에 나타낼 수 있다. 클로저가 함수의 유일한 인자라면 괄호를 완전히 생략할 수 있다.

```swift
let sortedNumbers = numbers.sorted { $0 > $1 }
print(sortedNumbers)
// "[20, 19, 12, 7]" 출력
```


## 객체와 클래스

클래스를 생성하려면 `class` 키워드 뒤에 클래스 이름을 작성한다. 클래스 내부의 프로퍼티 선언은 상수나 변수 선언과 동일하지만, 클래스의 컨텍스트 안에서 이루어진다. 마찬가지로 메서드와 함수 선언도 같은 방식으로 작성한다.

<!--
  REFERENCE
  도형을 예제 객체로 사용하는 이유는 익숙하고 프로퍼티와 상속/하위 분류 개념이 잘 드러나기 때문이다.
  완벽한 예제는 아니지만, 구조체로 모델링하면 행동을 상속할 수 없기 때문에 클래스로 구현한다.
-->

```swift
class Shape {
    var numberOfSides = 0
    func simpleDescription() -> String {
        return "A shape with \(numberOfSides) sides."
    }
}
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> class Shape {
         var numberOfSides = 0
         func simpleDescription() -> String {
             return "A shape with \(numberOfSides) sides."
         }
     }
  >> print(Shape().simpleDescription())
  << A shape with 0 sides.
  ```
-->

> 실험: `let`을 사용해 상수 프로퍼티를 추가하고, 인자를 받는 메서드를 하나 더 만들어 보자.

클래스의 인스턴스를 생성하려면 클래스 이름 뒤에 괄호를 붙인다. 점 표기법을 사용해 인스턴스의 프로퍼티와 메서드에 접근한다.

```swift
var shape = Shape()
shape.numberOfSides = 7
var shapeDescription = shape.simpleDescription()
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> var shape = Shape()
  -> shape.numberOfSides = 7
  -> var shapeDescription = shape.simpleDescription()
  >> print(shapeDescription)
  << A shape with 7 sides.
  ```
-->

이 `Shape` 클래스는 중요한 것을 빠뜨렸다. 인스턴스가 생성될 때 클래스를 설정하는 초기화 메서드다. `init`을 사용해 초기화 메서드를 만든다.

```swift
class NamedShape {
    var numberOfSides: Int = 0
    var name: String

    init(name: String) {
       self.name = name
    }

    func simpleDescription() -> String {
       return "A shape with \(numberOfSides) sides."
    }
}
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> class NamedShape {
         var numberOfSides: Int = 0
         var name: String

         init(name: String) {
            self.name = name
         }

         func simpleDescription() -> String {
            return "A shape with \(numberOfSides) sides."
         }
     }
  >> print(NamedShape(name: "test name").name)
  << test name
  >> print(NamedShape(name: "test name").simpleDescription())
  << A shape with 0 sides.
  ```
-->

초기화 메서드의 인자와 프로퍼티를 구분하기 위해 `self`를 사용한다. 클래스의 인스턴스를 생성할 때 초기화 메서드의 인자를 함수 호출처럼 전달한다. 모든 프로퍼티는 선언 시(`numberOfSides`처럼) 또는 초기화 메서드 안에서(`name`처럼) 값을 할당해야 한다.

객체가 해제되기 전에 정리 작업이 필요하다면 `deinit`을 사용해 소멸자를 만들 수 있다.

서브클래스는 클래스 이름 뒤에 콜론을 붙이고 슈퍼클래스 이름을 적는다. 모든 클래스가 표준 루트 클래스를 상속해야 하는 것은 아니므로, 필요에 따라 슈퍼클래스를 포함하거나 생략할 수 있다.

서브클래스에서 슈퍼클래스의 메서드를 재정의할 때는 `override`를 사용한다. 실수로 `override` 없이 메서드를 재정의하면 컴파일러가 오류로 인식한다. 또한 슈퍼클래스에서 실제로 재정의할 메서드가 없는데 `override`를 사용하면 컴파일러가 이를 감지한다.

```swift
class Square: NamedShape {
    var sideLength: Double

    init(sideLength: Double, name: String) {
        self.sideLength = sideLength
        super.init(name: name)
        numberOfSides = 4
    }

    func area() -> Double {
        return sideLength * sideLength
    }

    override func simpleDescription() -> String {
        return "A square with sides of length \(sideLength)."
    }
}
let test = Square(sideLength: 5.2, name: "my test square")
test.area()
test.simpleDescription()
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> class Square: NamedShape {
         var sideLength: Double

         init(sideLength: Double, name: String) {
             self.sideLength = sideLength
             super.init(name: name)
             numberOfSides = 4
         }

         func area() -> Double {
             return sideLength * sideLength
         }

         override func simpleDescription() -> String {
             return "A square with sides of length \(sideLength)."
         }
     }
  -> let test = Square(sideLength: 5.2, name: "my test square")
  >> let testArea =
  -> test.area()
  >> print(testArea)
  << 27.040000000000003
  >> let testDesc =
  -> test.simpleDescription()
  >> print(testDesc)
  << A square with sides of length 5.2.
  ```
-->

> 실험: `NamedShape`의 서브클래스인 `Circle`을 만들어 보자. 반지름과 이름을 초기화 메서드의 인자로 받고, `area()`와 `simpleDescription()` 메서드를 구현한다.

단순히 저장되는 프로퍼티 외에도, 프로퍼티에 게터와 세터를 추가할 수 있다.

```swift
class EquilateralTriangle: NamedShape {
    var sideLength: Double = 0.0

    init(sideLength: Double, name: String) {
        self.sideLength = sideLength
        super.init(name: name)
        numberOfSides = 3
    }

    var perimeter: Double {
        get {
             return 3.0 * sideLength
        }
        set {
            sideLength = newValue / 3.0
        }
    }

    override func simpleDescription() -> String {
        return "An equilateral triangle with sides of length \(sideLength)."
    }
}
var triangle = EquilateralTriangle(sideLength: 3.1, name: "a triangle")
print(triangle.perimeter)
// Prints "9.3"
triangle.perimeter = 9.9
print(triangle.sideLength)
// Prints "3.3000000000000003"
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> class EquilateralTriangle: NamedShape {
         var sideLength: Double = 0.0

         init(sideLength: Double, name: String) {
             self.sideLength = sideLength
             super.init(name: name)
             numberOfSides = 3
         }

         var perimeter: Double {
             get {
                  return 3.0 * sideLength
             }
             set {
                 sideLength = newValue / 3.0
             }
         }

         override func simpleDescription() -> String {
             return "An equilateral triangle with sides of length \(sideLength)."
         }
     }
  -> var triangle = EquilateralTriangle(sideLength: 3.1, name: "a triangle")
  -> print(triangle.perimeter)
  <- 9.3
  -> triangle.perimeter = 9.9
  -> print(triangle.sideLength)
  <- 3.3000000000000003
  ```
-->

`perimeter`의 세터에서 새 값은 암시적으로 `newValue`라는 이름을 가진다. `set` 뒤에 괄호를 붙여 명시적인 이름을 제공할 수도 있다.

`EquilateralTriangle` 클래스의 초기화 메서드는 세 단계로 이루어진다:

1. 서브클래스가 선언한 프로퍼티의 값을 설정한다.
2. 슈퍼클래스의 초기화 메서드를 호출한다.
3. 슈퍼클래스에서 정의한 프로퍼티의 값을 변경한다. 이 시점에서 메서드, 게터, 세터를 사용해 추가 설정 작업을 할 수도 있다.

프로퍼티를 계산할 필요는 없지만, 새 값을 설정하기 전후에 실행할 코드가 필요하다면 `willSet`과 `didSet`을 사용한다. 이 코드는 초기화 메서드 외부에서 값이 변경될 때마다 실행된다. 예를 들어, 아래 클래스는 삼각형의 변 길이가 항상 정사각형의 변 길이와 같도록 보장한다.

<!--
  삼각형 + 정사각형 예제는 개선이 필요하다.
  willSet을 사용하는 이유를 보여주려는 목적이지만,
  기하 도형이라는 컨텍스트에 제약을 받았다.
-->

```swift
class TriangleAndSquare {
    var triangle: EquilateralTriangle {
        willSet {
            square.sideLength = newValue.sideLength
        }
    }
    var square: Square {
        willSet {
            triangle.sideLength = newValue.sideLength
        }
    }
    init(size: Double, name: String) {
        square = Square(sideLength: size, name: name)
        triangle = EquilateralTriangle(sideLength: size, name: name)
    }
}
var triangleAndSquare = TriangleAndSquare(size: 10, name: "another test shape")
print(triangleAndSquare.square.sideLength)
// Prints "10.0"
print(triangleAndSquare.triangle.sideLength)
// Prints "10.0"
triangleAndSquare.square = Square(sideLength: 50, name: "larger square")
print(triangleAndSquare.triangle.sideLength)
// Prints "50.0"
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> class TriangleAndSquare {
         var triangle: EquilateralTriangle {
             willSet {
                 square.sideLength = newValue.sideLength
             }
         }
         var square: Square {
             willSet {
                 triangle.sideLength = newValue.sideLength
             }
         }
         init(size: Double, name: String) {
             square = Square(sideLength: size, name: name)
             triangle = EquilateralTriangle(sideLength: size, name: name)
         }
     }
  -> var triangleAndSquare = TriangleAndSquare(size: 10, name: "another test shape")
  -> print(triangleAndSquare.square.sideLength)
  <- 10.0
  -> print(triangleAndSquare.triangle.sideLength)
  <- 10.0
  -> triangleAndSquare.square = Square(sideLength: 50, name: "larger square")
  -> print(triangleAndSquare.triangle.sideLength)
  <- 50.0
  ```
-->

<!--
  문법적으로, 이 절은 변수에 일반적으로 적용된다.
  클래스나 구조체 외부에서 사용할 수 있는지,
  그리고 어떤 모습일지는 확실하지 않다.
-->

옵셔널 값을 다룰 때는 메서드, 프로퍼티, 서브스크립팅 같은 작업 앞에 `?`를 붙일 수 있다. `?` 앞의 값이 `nil`이면 `?` 뒤의 모든 작업은 무시되고 전체 표현식의 값은 `nil`이 된다. 그렇지 않으면 옵셔널 값이 언래핑되고, `?` 뒤의 모든 작업은 언래핑된 값에 대해 수행된다. 두 경우 모두 전체 표현식의 값은 옵셔널 값이다.

```swift
let optionalSquare: Square? = Square(sideLength: 2.5, name: "optional square")
let sideLength = optionalSquare?.sideLength
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> let optionalSquare: Square? = Square(sideLength: 2.5, name: "optional square")
  -> let sideLength = optionalSquare?.sideLength
  ```
-->


## 열거형과 구조체

`enum`을 사용해 열거형을 정의한다. 클래스와 다른 이름 있는 타입들처럼 열거형도 메서드를 가질 수 있다.

<!--
  참고
  카드는 열거형을 설명하기에 적합하다. 카드는 슈트와 랭크라는 두 가지 속성을 가지며,
  둘 다 작고 제한된 집합에서 나온다. 여기서 사용한 덱은 유럽과 아메리카에서 가장 흔히 쓰이는 것이다.
  하지만 지역에 따라 다양한 변형이 존재한다.
-->

```swift
enum Rank: Int {
    case ace = 1
    case two, three, four, five, six, seven, eight, nine, ten
    case jack, queen, king

    func simpleDescription() -> String {
        switch self {
        case .ace:
            return "ace"
        case .jack:
            return "jack"
        case .queen:
            return "queen"
        case .king:
            return "king"
        default:
            return String(self.rawValue)
        }
    }
}
let ace = Rank.ace
let aceRawValue = ace.rawValue
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> enum Rank: Int {
         case ace = 1
         case two, three, four, five, six, seven, eight, nine, ten
         case jack, queen, king

         func simpleDescription() -> String {
             switch self {
                 case .ace:
                     return "ace"
                 case .jack:
                     return "jack"
                 case .queen:
                     return "queen"
                 case .king:
                     return "king"
                 default:
                     return String(self.rawValue)
             }
         }
     }
  -> let ace = Rank.ace
  -> let aceRawValue = ace.rawValue
  >> print(aceRawValue)
  << 1
  ```
-->

> 실험: 두 `Rank` 값을 비교하는 함수를 작성해 보자. 비교는 각각의 원시 값을 기준으로 한다.

스위프트는 기본적으로 원시 값을 0부터 시작해 1씩 증가시키지만, 명시적으로 값을 지정해 이 동작을 변경할 수 있다. 위 예제에서는 `Ace`에 원시 값 `1`을 명시적으로 할당했고, 나머지 원시 값은 순서대로 지정되었다. 문자열이나 부동소수점 숫자를 열거형의 원시 타입으로 사용할 수도 있다. `rawValue` 프로퍼티를 사용해 열거형 케이스의 원시 값에 접근한다.

`init?(rawValue:)` 이니셜라이저를 사용해 원시 값으로부터 열거형 인스턴스를 생성한다. 이 이니셜라이저는 원시 값과 일치하는 열거형 케이스를 반환하거나, 일치하는 `Rank`가 없으면 `nil`을 반환한다.

```swift
if let convertedRank = Rank(rawValue: 3) {
    let threeDescription = convertedRank.simpleDescription()
}
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> if let convertedRank = Rank(rawValue: 3) {
         let threeDescription = convertedRank.simpleDescription()
  >> print(threeDescription)
  << 3
  -> }
  ```
-->

열거형의 케이스 값은 실제 값이며, 단순히 원시 값을 나타내는 또 다른 방식이 아니다. 사실, 의미 있는 원시 값이 없는 경우에는 원시 값을 제공하지 않아도 된다.

```swift
enum Suit {
    case spades, hearts, diamonds, clubs

    func simpleDescription() -> String {
        switch self {
        case .spades:
            return "spades"
        case .hearts:
            return "hearts"
        case .diamonds:
            return "diamonds"
        case .clubs:
            return "clubs"
        }
    }
}
let hearts = Suit.hearts
let heartsDescription = hearts.simpleDescription()
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> enum Suit {
         case spades, hearts, diamonds, clubs

         func simpleDescription() -> String {
             switch self {
                 case .spades:
                     return "spades"
                 case .hearts:
                     return "hearts"
                 case .diamonds:
                     return "diamonds"
                 case .clubs:
                     return "clubs"
             }
         }
     }
  -> let hearts = Suit.hearts
  -> let heartsDescription = hearts.simpleDescription()
  >> print(heartsDescription)
  << hearts
  ```
-->

> 실험: `Suit`에 `color()` 메서드를 추가해 보자. 스페이드와 클럽은 "black"을, 하트와 다이아몬드는 "red"를 반환한다.

열거형의 `hearts` 케이스를 참조하는 두 가지 방식을 주목하자. `hearts` 상수에 값을 할당할 때는 열거형 케이스 `Suit.hearts`를 전체 이름으로 참조한다. 상수에 명시적 타입이 지정되지 않았기 때문이다. 스위치 내부에서는 열거형 케이스를 축약형 `.hearts`로 참조한다. `self`의 값이 이미 `Suit` 타입임이 알려져 있기 때문이다. 값의 타입이 이미 알려진 경우에는 언제나 축약형을 사용할 수 있다.

열거형이 원시 값을 가지면, 그 값은 선언의 일부로 결정된다. 즉, 특정 열거형 케이스의 모든 인스턴스는 항상 동일한 원시 값을 가진다. 열거형 케이스에 값을 연관시킬 수도 있다. 이 값은 인스턴스를 생성할 때 결정되며, 열거형 케이스의 각 인스턴스마다 다를 수 있다. 연관된 값은 열거형 케이스 인스턴스의 저장 프로퍼티처럼 동작한다고 볼 수 있다. 예를 들어, 서버에 일출과 일몰 시간을 요청하는 경우를 생각해 보자. 서버는 요청한 정보를 응답하거나, 무엇이 잘못되었는지 설명하는 메시지를 응답한다.

```swift
enum ServerResponse {
    case result(String, String)
    case failure(String)
}

let success = ServerResponse.result("6:00 am", "8:09 pm")
let failure = ServerResponse.failure("Out of cheese.")

switch success {
case let .result(sunrise, sunset):
    print("Sunrise is at \(sunrise) and sunset is at \(sunset).")
case let .failure(message):
    print("Failure...  \(message)")
}
// Prints "Sunrise is at 6:00 am and sunset is at 8:09 pm."
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> enum ServerResponse {
         case result(String, String)
         case failure(String)
     }

  -> let success = ServerResponse.result("6:00 am", "8:09 pm")
  -> let failure = ServerResponse.failure("Out of cheese.")

  -> switch success {
         case let .result(sunrise, sunset):
             print("Sunrise is at \(sunrise) and sunset is at \(sunset).")
         case let .failure(message):
             print("Failure...  \(message)")
     }
  <- Sunrise is at 6:00 am and sunset is at 8:09 pm.
  ```
-->

> 실험: `ServerResponse`에 세 번째 케이스를 추가하고, 스위치에도 이를 반영해 보자.

일출과 일몰 시간이 어떻게 `ServerResponse` 값에서 추출되는지 주목하자. 이 값은 스위치 케이스와 매치되는 과정에서 추출된다.

`struct`를 사용해 구조체를 정의한다. 구조체는 클래스와 많은 동작을 공유한다. 메서드와 이니셜라이저를 포함한다. 구조체와 클래스의 가장 중요한 차이점 중 하나는 구조체는 코드에서 전달될 때 항상 복사되지만, 클래스는 참조로 전달된다는 점이다.

```swift
struct Card {
    var rank: Rank
    var suit: Suit
    func simpleDescription() -> String {
        return "The \(rank.simpleDescription()) of \(suit.simpleDescription())"
    }
}
let threeOfSpades = Card(rank: .three, suit: .spades)
let threeOfSpadesDescription = threeOfSpades.simpleDescription()
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> struct Card {
         var rank: Rank
         var suit: Suit
         func simpleDescription() -> String {
             return "The \(rank.simpleDescription()) of \(suit.simpleDescription())"
         }
     }
  -> let threeOfSpades = Card(rank: .three, suit: .spades)
  -> let threeOfSpadesDescription = threeOfSpades.simpleDescription()
  >> print(threeOfSpadesDescription)
  << The 3 of spades
  ```
-->

> 실험: 각 랭크와 슈트의 조합으로 이루어진 카드 한 벌을 담은 배열을 반환하는 함수를 작성해 보자.


## 동시성

비동기적으로 실행되는 함수를 표시하려면 `async`를 사용한다.

```swift
func fetchUserID(from server: String) async -> Int {
    if server == "primary" {
        return 97
    }
    return 501
}
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> func fetchUserID(from server: String) async -> Int {
         if server == "primary" {
             return 97
         }
         return 501
     }
  ```
-->

비동기 함수를 호출할 때는 앞에 `await`를 붙인다.

```swift
func fetchUsername(from server: String) async -> String {
    let userID = await fetchUserID(from: server)
    if userID == 501 {
        return "John Appleseed"
    }
    return "Guest"
}
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> func fetchUsername(from server: String) async -> String {
         let userID = await fetchUserID(from: server)
         if userID == 501 {
             return "John Appleseed"
         }
         return "Guest"
     }
  ```
-->

`async let`을 사용하면 비동기 함수를 호출하고 다른 비동기 코드와 병렬로 실행할 수 있다. 반환된 값을 사용할 때는 `await`를 붙인다.

```swift
func connectUser(to server: String) async {
    async let userID = fetchUserID(from: server)
    async let username = fetchUsername(from: server)
    let greeting = await "Hello \(username), user ID \(userID)"
    print(greeting)
}
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> func connectUser(to server: String) async {
         async let userID = fetchUserID(from: server)
         async let username = fetchUsername(from: server)
         let greeting = await "Hello \(username), user ID \(userID)"
         print(greeting)
     }
  ```
-->

`Task`를 사용하면 동기 코드에서 비동기 함수를 호출하고 결과를 기다리지 않을 수 있다.

```swift
Task {
    await connectUser(to: "primary")
}
// Prints "Hello Guest, user ID 97"
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> Task {
         await connectUser(to: "primary")
     }
  >> import Darwin; sleep(1)  // Pause for task to run
  <- Hello Guest, user ID 97
  ```
-->

태스크 그룹을 사용하면 동시성 코드를 구조화할 수 있다.

```swift
let userIDs = await withTaskGroup(of: Int.self) { group in
    for server in ["primary", "secondary", "development"] {
        group.addTask {
            return await fetchUserID(from: server)
        }
    }

    var results: [Int] = []
    for await result in group {
        results.append(result)
    }
    return results
}
```

액터는 클래스와 유사하지만, 서로 다른 비동기 함수가 동일한 액터의 인스턴스와 안전하게 상호작용할 수 있도록 보장한다.

```swift
actor ServerConnection {
    var server: String = "primary"
    private var activeUsers: [Int] = []
    func connect() async -> Int {
        let userID = await fetchUserID(from: server)
        // ... 서버와 통신 ...
        activeUsers.append(userID)
        return userID
    }
}
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> actor Oven {
         var contents: [String] = []
         func bake(_ food: String) -> String {
             contents.append(food)
             // ... 음식이 익을 때까지 기다림 ...
             return contents.removeLast()
         }
     }
  ```
-->

액터의 메서드를 호출하거나 프로퍼티에 접근할 때는 `await`를 사용해 해당 코드가 액터에서 이미 실행 중인 다른 코드가 끝날 때까지 기다려야 할 수 있음을 표시한다.

```swift
let server = ServerConnection()
let userID = await server.connect()
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> let oven = Oven()
  -> let biscuits = await oven.bake("biscuits")
  ```
-->


## 프로토콜과 확장

`protocol`을 사용해 프로토콜을 정의한다.

```swift
protocol ExampleProtocol {
     var simpleDescription: String { get }
     mutating func adjust()
}
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> protocol ExampleProtocol {
          var simpleDescription: String { get }
          mutating func adjust()
     }
  ```
-->

클래스, 열거형, 구조체 모두 프로토콜을 채택할 수 있다.

<!--
  REFERENCE
  The use of adjust() is totally a placeholder
  for some more interesting operation.
  Likewise for the struct and classes -- placeholders
  for some more interesting data structure.
-->

```swift
class SimpleClass: ExampleProtocol {
     var simpleDescription: String = "A very simple class."
     var anotherProperty: Int = 69105
     func adjust() {
          simpleDescription += "  Now 100% adjusted."
     }
}
var a = SimpleClass()
a.adjust()
let aDescription = a.simpleDescription

struct SimpleStructure: ExampleProtocol {
     var simpleDescription: String = "A simple structure"
     mutating func adjust() {
          simpleDescription += " (adjusted)"
     }
}
var b = SimpleStructure()
b.adjust()
let bDescription = b.simpleDescription
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> class SimpleClass: ExampleProtocol {
          var simpleDescription: String = "A very simple class."
          var anotherProperty: Int = 69105
          func adjust() {
               simpleDescription += "  Now 100% adjusted."
          }
     }
  -> var a = SimpleClass()
  -> a.adjust()
  -> let aDescription = a.simpleDescription
  >> print(aDescription)
  << A very simple class.  Now 100% adjusted.

  -> struct SimpleStructure: ExampleProtocol {
          var simpleDescription: String = "A simple structure"
          mutating func adjust() {
               simpleDescription += " (adjusted)"
          }
     }
  -> var b = SimpleStructure()
  -> b.adjust()
  -> let bDescription = b.simpleDescription
  >> print(bDescription)
  << A simple structure (adjusted)
  ```
-->

> 실험: `ExampleProtocol`에 새로운 요구사항을 추가해 보자. `SimpleClass`와 `SimpleStructure`가 여전히 프로토콜을 준수하려면 어떤 변경이 필요한가?

`SimpleStructure`의 선언에서 `mutating` 키워드를 사용해 구조체를 수정하는 메서드를 표시한다. `SimpleClass`의 선언에서는 클래스의 메서드가 항상 클래스를 수정할 수 있기 때문에 `mutating` 키워드가 필요하지 않다.

`extension`을 사용해 기존 타입에 새로운 메서드나 계산된 속성과 같은 기능을 추가할 수 있다. 확장을 통해 다른 곳에서 선언된 타입이나 라이브러리나 프레임워크에서 임포트한 타입에 프로토콜 준수를 추가할 수도 있다.

```swift
extension Int: ExampleProtocol {
    var simpleDescription: String {
        return "The number \(self)"
    }
    mutating func adjust() {
        self += 42
    }
 }
print(7.simpleDescription)
// Prints "The number 7"
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> extension Int: ExampleProtocol {
         var simpleDescription: String {
             return "The number \(self)"
         }
         mutating func adjust() {
             self += 42
         }
      }
  -> print(7.simpleDescription)
  <- The number 7
  ```
-->

> 실험: `Double` 타입에 `absoluteValue` 속성을 추가하는 확장을 작성해 보자.

프로토콜 이름을 다른 이름 있는 타입처럼 사용할 수 있다. 예를 들어, 서로 다른 타입이지만 모두 하나의 프로토콜을 준수하는 객체 컬렉션을 만들 수 있다. 프로토콜 타입으로 박싱된 값을 다룰 때는 프로토콜 정의 외부의 메서드를 사용할 수 없다.

```swift
let protocolValue: any ExampleProtocol = a
print(protocolValue.simpleDescription)
// Prints "A very simple class.  Now 100% adjusted."
// print(protocolValue.anotherProperty)  // Uncomment to see the error
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> let protocolValue: ExampleProtocol = a
  -> print(protocolValue.simpleDescription)
  <- A very simple class.  Now 100% adjusted.
  // print(protocolValue.anotherProperty)  // Uncomment to see the error
  ```
-->

`protocolValue` 변수의 런타임 타입이 `SimpleClass`임에도 불구하고, 컴파일러는 이를 `ExampleProtocol` 타입으로 간주한다. 이는 클래스가 프로토콜 준수 외에 추가로 구현한 메서드나 속성에 실수로 접근할 수 없음을 의미한다.


## 에러 처리

`Error` 프로토콜을 채택한 타입을 사용해 에러를 표현한다.

```swift
enum PrinterError: Error {
    case outOfPaper
    case noToner
    case onFire
}
```

에러를 던질 때는 `throw`를 사용하고, 에러를 던질 수 있는 함수는 `throws`로 표시한다. 함수 내에서 에러를 던지면, 함수는 즉시 반환되고 호출한 코드가 에러를 처리한다.

```swift
func send(job: Int, toPrinter printerName: String) throws -> String {
    if printerName == "Never Has Toner" {
        throw PrinterError.noToner
    }
    return "Job sent"
}
```

에러를 처리하는 방법은 여러 가지다. `do`-`catch`를 사용하는 방법이 그 중 하나다. `do` 블록 안에서 에러를 던질 수 있는 코드 앞에 `try`를 붙인다. `catch` 블록 안에서는 에러가 자동으로 `error`라는 이름으로 주어지며, 다른 이름을 지정할 수도 있다.

```swift
do {
    let printerResponse = try send(job: 1040, toPrinter: "Bi Sheng")
    print(printerResponse)
} catch {
    print(error)
}
// Prints "Job sent"
```

> 실험: 프린터 이름을 `"Never Has Toner"`로 바꿔서 `send(job:toPrinter:)` 함수가 에러를 던지도록 해보자.

특정 에러를 처리하기 위해 여러 개의 `catch` 블록을 제공할 수 있다. `catch` 뒤에 패턴을 작성하는 방식은 `switch` 문의 `case`와 유사하다.

```swift
do {
    let printerResponse = try send(job: 1440, toPrinter: "Gutenberg")
    print(printerResponse)
} catch PrinterError.onFire {
    print("I'll just put this over here, with the rest of the fire.")
} catch let printerError as PrinterError {
    print("Printer error: \(printerError).")
} catch {
    print(error)
}
// Prints "Job sent"
```

> 실험: `do` 블록 안에 에러를 던지는 코드를 추가해보자. 첫 번째 `catch` 블록에서 처리될 에러는 어떤 종류인가? 두 번째와 세 번째 블록에서는 어떤 에러가 처리되는가?

에러를 처리하는 또 다른 방법은 `try?`를 사용해 결과를 옵셔널로 변환하는 것이다. 함수가 에러를 던지면 특정 에러는 버려지고 결과는 `nil`이 된다. 그렇지 않으면 함수가 반환한 값을 포함한 옵셔널이 결과로 나온다.

```swift
let printerSuccess = try? send(job: 1884, toPrinter: "Mergenthaler")
let printerFailure = try? send(job: 1885, toPrinter: "Never Has Toner")
```

`defer`를 사용해 함수 내의 다른 코드가 모두 실행된 후, 함수가 반환되기 직전에 실행될 코드 블록을 작성할 수 있다. 이 코드는 함수가 에러를 던지더라도 실행된다. `defer`를 사용하면 설정 코드와 정리 코드를 서로 가까이 배치할 수 있으며, 이 코드들은 서로 다른 시점에 실행된다.

```swift
var fridgeIsOpen = false
let fridgeContent = ["milk", "eggs", "leftovers"]

func fridgeContains(_ food: String) -> Bool {
    fridgeIsOpen = true
    defer {
        fridgeIsOpen = false
    }

    let result = fridgeContent.contains(food)
    return result
}
if fridgeContains("banana") {
    print("Found a banana")
}
print(fridgeIsOpen)
// Prints "false"
```


## 제네릭

제네릭 함수나 타입을 만들려면 꺾쇠 괄호 안에 이름을 작성한다.

<!--
  REFERENCE
  The four knocks is a reference to Dr Who series 4,
  in which knocking four times is a running aspect
  of the season's plot.
-->

```swift
func makeArray<Item>(repeating item: Item, numberOfTimes: Int) -> [Item] {
    var result: [Item] = []
    for _ in 0..<numberOfTimes {
         result.append(item)
    }
    return result
}
makeArray(repeating: "knock", numberOfTimes: 4)
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> func makeArray<Item>(repeating item: Item, numberOfTimes: Int) -> [Item] {
         var result: [Item] = []
         for _ in 0..<numberOfTimes {
              result.append(item)
         }
         return result
     }
  >> let fourKnocks =
  -> makeArray(repeating: "knock", numberOfTimes: 4)
  >> print(fourKnocks)
  << ["knock", "knock", "knock", "knock"]
  ```
-->

함수와 메서드뿐만 아니라 클래스, 열거형, 구조체도 제네릭으로 만들 수 있다.

```swift
// Swift 표준 라이브러리의 옵셔널 타입을 재구현
enum OptionalValue<Wrapped> {
    case none
    case some(Wrapped)
}
var possibleInteger: OptionalValue<Int> = .none
possibleInteger = .some(100)
```

<!--
  - test: `guided-tour`

  ```swifttest
  // Reimplement the Swift standard library's optional type
  -> enum OptionalValue<Wrapped> {
         case none
         case some(Wrapped)
     }
  -> var possibleInteger: OptionalValue<Int> = .none
  -> possibleInteger = .some(100)
  ```
-->

본문 바로 앞에 `where`를 사용해 요구사항 목록을 지정할 수 있다. 예를 들어, 타입이 특정 프로토콜을 구현하도록 요구하거나, 두 타입이 동일하도록 요구하거나, 클래스가 특정 슈퍼클래스를 가지도록 요구할 수 있다.

```swift
func anyCommonElements<T: Sequence, U: Sequence>(_ lhs: T, _ rhs: U) -> Bool
    where T.Element: Equatable, T.Element == U.Element
{
    for lhsItem in lhs {
        for rhsItem in rhs {
            if lhsItem == rhsItem {
                return true
            }
        }
    }
   return false
}
anyCommonElements([1, 2, 3], [3])
```

<!--
  - test: `guided-tour`

  ```swifttest
  -> func anyCommonElements<T: Sequence, U: Sequence>(_ lhs: T, _ rhs: U) -> Bool
         where T.Element: Equatable, T.Element == U.Element
     {
         for lhsItem in lhs {
             for rhsItem in rhs {
                 if lhsItem == rhsItem {
                     return true
                 }
             }
         }
        return false
     }
  >> let hasAnyCommon =
  -> anyCommonElements([1, 2, 3], [3])
  >> print(hasAnyCommon)
  << true
  ```
-->

> 실험: `anyCommonElements(_:_:)` 함수를 수정해 두 시퀀스가 공통으로 가지는 엘리먼트를 배열로 반환하는 함수를 만들어 보자.

`<T: Equatable>`은 `<T> ... where T: Equatable`과 동일하다.

<!--
이 소스 파일은 Swift.org 오픈 소스 프로젝트의 일부입니다.

Copyright (c) 2014 - 2022 Apple Inc. 및 Swift 프로젝트 기여자
Apache License v2.0 및 Runtime Library Exception에 따라 라이선스가 부여됨

라이선스 정보는 https://swift.org/LICENSE.txt에서 확인할 수 있습니다.
Swift 프로젝트 기여자 목록은 https://swift.org/CONTRIBUTORS.txt에서 확인할 수 있습니다.
-->


