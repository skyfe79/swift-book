# 기본 연산자

값을 할당하거나, 산술 연산을 수행하거나, 비교하는 작업을 진행한다.

*연산자*는 값들을 확인하거나 변경하거나 결합할 때 사용하는 특수한 기호나 구문이다. 예를 들어, 덧셈 연산자(`+`)는 두 숫자를 더한다. `let i = 1 + 2`와 같이 사용한다. 그리고 논리 AND 연산자(`&&`)는 두 불리언 값을 결합한다. `if enteredDoorCode && passedRetinaScan`과 같이 활용한다.

Swift는 C 언어와 같은 프로그래밍 언어에서 이미 익숙할 수 있는 연산자를 지원하며, 일반적인 코딩 실수를 방지하기 위해 몇 가지 기능을 개선했다. 할당 연산자(`=`)는 값을 반환하지 않는다. 이는 등호 연산자(`==`)를 사용해야 할 때 실수로 할당 연산자를 사용하는 것을 방지하기 위함이다. 산술 연산자(`+`, `-`, `*`, `/`, `%` 등)는 값의 오버플로를 감지하고 이를 허용하지 않는다. 이는 저장 타입의 허용 범위를 벗어나는 크거나 작은 숫자를 다룰 때 예상치 못한 결과를 피하기 위함이다. Swift의 오버플로 연산자를 사용하면 값 오버플로 동작을 선택할 수 있다. 이는 <doc:AdvancedOperators#Overflow-Operators>에서 자세히 설명한다.

Swift는 또한 C 언어에는 없는 범위 연산자를 제공한다. `a..<b`와 `a...b` 같은 연산자는 값의 범위를 간단히 표현하는 단축어 역할을 한다.

이 장에서는 Swift의 일반적인 연산자들을 설명한다. <doc:AdvancedOperators>에서는 Swift의 고급 연산자를 다루고, 커스텀 연산자를 정의하는 방법과 자신만의 커스텀 타입에 표준 연산자를 구현하는 방법을 설명한다.


## 용어 정리

연산자는 단항, 이항, 삼항으로 구분한다:

- **단항 연산자**는 하나의 피연산자를 대상으로 동작한다. 예를 들어 `-a`가 있다.  
  단항 *접두사* 연산자는 피연산자 바로 앞에 위치한다(예: `!b`).  
  단항 *접미사* 연산자는 피연산자 바로 뒤에 위치한다(예: `c!`).

- **이항 연산자**는 두 개의 피연산자를 대상으로 동작한다. 예를 들어 `2 + 3`이 있다.  
  이항 연산자는 두 피연산자 사이에 위치하므로 *중위* 연산자라고 부른다.

- **삼항 연산자**는 세 개의 피연산자를 대상으로 동작한다.  
  C 언어와 마찬가지로 Swift에는 삼항 조건 연산자(`a ? b : c`) 하나만 존재한다.

연산자가 영향을 미치는 값을 *피연산자*라고 한다.  
예를 들어 `1 + 2` 표현식에서 `+` 기호는 중위 연산자이며, 두 피연산자는 `1`과 `2`이다.


## 할당 연산자

*할당 연산자* (`a = b`)는 `a`의 값을 `b`의 값으로 초기화하거나 업데이트한다:

```swift
let b = 10
var a = 5
a = b
// a는 이제 10과 같다
```

<!--
  - test: `assignmentOperator`

  ```swifttest
  -> let b = 10
  -> var a = 5
  -> a = b
  /> a is now equal to \(a)
  </ a is now equal to 10
  ```
-->

할당 연산자의 오른쪽이 여러 값을 가진 튜플이라면, 그 요소들을 여러 상수나 변수로 한 번에 분해할 수 있다:

```swift
let (x, y) = (1, 2)
// x는 1과 같고, y는 2와 같다
```

<!--
  - test: `assignmentOperator`

  ```swifttest
  -> let (x, y) = (1, 2)
  /> x is equal to \(x), and y is equal to \(y)
  </ x is equal to 1, and y is equal to 2
  ```
-->

<!--
  - test: `tuple-unwrapping-with-var`

  ```swifttest
  >> var (x, y) = (1, 2)
  ```
-->

<!--
  이 코드는 변수에 할당을 허용한다.
  var 패턴이 제거되었더라도,
  (x, y)가 패턴으로 해석되고,
  `var`가 패턴이 아닌 변수 선언 헤드에서 오기 때문이다.
-->

C와 Objective-C의 할당 연산자와 달리, Swift의 할당 연산자는 값을 반환하지 않는다. 따라서 다음 문장은 유효하지 않다:

```swift
if x = y {
    // 이 코드는 유효하지 않다. x = y가 값을 반환하지 않기 때문이다.
}
```

<!--
  - test: `assignmentOperatorInvalid`

  ```swifttest
  -> if x = y {
        // This isn't valid, because x = y doesn't return a value.
     }
  !$ error: cannot find 'x' in scope
  !! if x = y {
  !!    ^
  !$ error: cannot find 'y' in scope
  !! if x = y {
  !!        ^
  ```
-->

이 기능은 실수로 할당 연산자(`=`)를 사용하는 것을 방지한다. 실제로는 동등 연산자(`==`)를 사용하려는 경우에 말이다. `if x = y`를 유효하지 않게 함으로써, Swift는 코드에서 이런 종류의 오류를 피할 수 있게 도와준다.

<!--
  TODO: x = y = z도 유효하지 않다는 것을 언급해야 할까?
  그렇다면, 왜 이것이 좋은 것인지에 대한 설득력 있는 논거가 있는가?
-->


## 산술 연산자

Swift는 모든 숫자 타입에 대해 네 가지 기본 *산술 연산자*를 지원한다:

- 덧셈 (`+`)
- 뺄셈 (`-`)
- 곱셈 (`*`)
- 나눗셈 (`/`)

```swift
1 + 2       // 결과는 3
5 - 3       // 결과는 2
2 * 3       // 결과는 6
10.0 / 2.5  // 결과는 4.0
```

<!--
  - test: `arithmeticOperators`

  ```swifttest
  >> let r0 =
  -> 1 + 2       // 결과는 3
  >> assert(r0 == 3)
  >> let r1 =
  -> 5 - 3       // 결과는 2
  >> assert(r1 == 2)
  >> let r2 =
  -> 2 * 3       // 결과는 6
  >> assert(r2 == 6)
  >> let r3 =
  -> 10.0 / 2.5  // 결과는 4.0
  >> assert(r3 == 4.0)
  ```
-->

C와 Objective-C의 산술 연산자와 달리, Swift의 산술 연산자는 기본적으로 값이 오버플로우되는 것을 허용하지 않는다. Swift의 오버플로우 연산자(예: `a &+ b`)를 사용하면 오버플로우 동작을 선택할 수 있다. 자세한 내용은 <doc:AdvancedOperators#Overflow-Operators>를 참고한다.

덧셈 연산자는 `String` 연결에도 사용할 수 있다:

```swift
"hello, " + "world"  // 결과는 "hello, world"
```

<!--
  - test: `arithmeticOperators`

  ```swifttest
  >> let r4 =
  -> "hello, " + "world"  // 결과는 "hello, world"
  >> assert(r4 == "hello, world")
  ```
-->


### 나머지 연산자

*나머지 연산자*(`a % b`)는 `b`의 배수가 `a` 안에 몇 번 들어갈 수 있는지 계산하고, 남은 값을 반환한다. 이 남은 값을 *나머지*라고 부른다.

> 참고: 나머지 연산자(`%`)는 다른 언어에서 *모듈로 연산자*로 알려져 있다. 하지만 Swift에서는 음수에 대해 다르게 동작하기 때문에, 엄밀히 말하면 모듈로 연산이 아니라 나머지 연산이다.

<!--
  - test: `percentOperatorIsRemainderNotModulo`

  ```swifttest
  -> for i in -5...0 {
        print(i % 4)
     }
  << -1
  << 0
  << -3
  << -2
  << -1
  << 0
  ```
-->

나머지 연산자가 어떻게 동작하는지 살펴보자. `9 % 4`를 계산하려면, 먼저 `4`가 `9` 안에 몇 번 들어갈 수 있는지 알아본다:

![](remainderInteger)

`4`는 `9` 안에 두 번 들어갈 수 있고, 나머지는 `1`이다 (주황색으로 표시).

Swift에서는 다음과 같이 작성한다:

```swift
9 % 4    // 결과는 1
```

<!--
  - test: `arithmeticOperators`

  ```swifttest
  >> let r5 =
  -> 9 % 4    // equals 1
  >> assert(r5 == 1)
  ```
-->

`a % b`의 답을 구하기 위해, `%` 연산자는 다음 방정식을 계산하고 `remainder`를 결과로 반환한다:

`a` = (`b` x `some multiplier`) + `remainder`

여기서 `some multiplier`는 `b`의 배수 중 `a` 안에 들어갈 수 있는 가장 큰 수이다.

`9`와 `4`를 이 방정식에 대입하면 다음과 같다:

`9` = (`4` x `2`) + `1`

`a`가 음수일 때도 같은 방법을 적용한다:

```swift
-9 % 4   // 결과는 -1
```

<!--
  - test: `arithmeticOperators`

  ```swifttest
  >> let r6 =
  -> -9 % 4   // equals -1
  >> assert(r6 == -1)
  ```
-->

`-9`와 `4`를 방정식에 대입하면:

`-9` = (`4` x `-2`) + `-1`

나머지 값으로 `-1`이 나온다.

`b`가 음수인 경우, `b`의 부호는 무시된다. 즉, `a % b`와 `a % -b`는 항상 같은 결과를 반환한다.


### 단항 마이너스 연산자

숫자 값의 부호를 전환하려면 `-`를 접두사로 사용한다. 이를 *단항 마이너스 연산자*라고 부른다.

```swift
let three = 3
let minusThree = -three       // minusThree는 -3과 같다
let plusThree = -minusThree   // plusThree는 3과 같다. 즉, "마이너스 마이너스 3"이다
```

<!--
  - test: `arithmeticOperators`

  ```swifttest
  -> let three = 3
  -> let minusThree = -three       // minusThree equals -3
  -> let plusThree = -minusThree   // plusThree equals 3, or "minus minus three"
  ```
-->

단항 마이너스 연산자(`-`)는 연산 대상 값 바로 앞에 공백 없이 붙여 사용한다.


### 단항 플러스 연산자

단항 플러스 연산자(`+`)는 단순히 피연산자의 값을 그대로 반환한다. 값에 아무런 변화를 주지 않는다:

```swift
let minusSix = -6
let alsoMinusSix = +minusSix  // alsoMinusSix는 -6과 같다
```

<!--
  - test: `arithmeticOperators`

  ```swifttest
  -> let minusSix = -6
  -> let alsoMinusSix = +minusSix  // alsoMinusSix equals -6
  >> assert(alsoMinusSix == minusSix)
  ```
-->

단항 플러스 연산자는 실제로 아무런 동작을 하지 않지만, 음수에 단항 마이너스 연산자를 사용할 때 양수에 대칭성을 제공하기 위해 활용할 수 있다.


## 복합 할당 연산자

C 언어와 마찬가지로, Swift는 할당(`=`)을 다른 연산과 결합한 *복합 할당 연산자*를 제공한다. 예를 들어 *덧셈 할당 연산자*(`+=`)는 다음과 같이 사용한다:

```swift
var a = 1
a += 2
// a는 이제 3과 같다
```

<!--
  - test: `compoundAssignment`

  ```swifttest
  -> var a = 1
  -> a += 2
  /> a is now equal to \(a)
  </ a is now equal to 3
  ```
-->

`a += 2`라는 표현은 `a = a + 2`의 축약형이다. 이 연산자는 덧셈과 할당을 동시에 수행한다.

> 주의: 복합 할당 연산자는 값을 반환하지 않는다. 예를 들어, `let b = a += 2`와 같이 작성할 수 없다.

Swift 표준 라이브러리에서 제공하는 연산자에 대한 자세한 정보는 [Operator Declarations](https://developer.apple.com/documentation/swift/operator_declarations)를 참고한다.


## 비교 연산자

Swift는 다음과 같은 비교 연산자를 지원한다:

- 같음 (`a == b`)
- 같지 않음 (`a != b`)
- 큼 (`a > b`)
- 작음 (`a < b`)
- 크거나 같음 (`a >= b`)
- 작거나 같음 (`a <= b`)

> 참고: Swift는 또한 두 객체 참조가 동일한 객체 인스턴스를 가리키는지 테스트하는 두 개의 *식별 연산자* (`===`와 `!==`)를 제공한다. 자세한 내용은 <doc:ClassesAndStructures#Identity-Operators>를 참조한다.

각 비교 연산자는 해당 문장이 참인지 여부를 나타내는 `Bool` 값을 반환한다:

```swift
1 == 1   // 1이 1과 같으므로 true
2 != 1   // 2가 1과 같지 않으므로 true
2 > 1    // 2가 1보다 크므로 true
1 < 2    // 1이 2보다 작으므로 true
1 >= 1   // 1이 1보다 크거나 같으므로 true
2 <= 1   // 2가 1보다 작거나 같지 않으므로 false
```

<!--
  - test: `comparisonOperators`

  ```swifttest
  >> assert(
  -> 1 == 1   // true because 1 is equal to 1
  >> )
  >> assert(
  -> 2 != 1   // true because 2 isn't equal to 1
  >> )
  >> assert(
  -> 2 > 1    // true because 2 is greater than 1
  >> )
  >> assert(
  -> 1 < 2    // true because 1 is less than 2
  >> )
  >> assert(
  -> 1 >= 1   // true because 1 is greater than or equal to 1
  >> )
  >> assert( !(
  -> 2 <= 1   // false because 2 isn't less than or equal to 1
  >> ) )
  ```
-->

비교 연산자는 주로 `if` 문과 같은 조건문에서 사용된다:

```swift
let name = "world"
if name == "world" {
    print("hello, world")
} else {
    print("I'm sorry \(name), but I don't recognize you")
}
// name이 "world"와 같으므로 "hello, world"를 출력한다.
```

<!--
  - test: `comparisonOperators`

  ```swifttest
  -> let name = "world"
  -> if name == "world" {
        print("hello, world")
     } else {
        print("I'm sorry \(name), but I don't recognize you")
     }
  << hello, world
  // Prints "hello, world", because name is indeed equal to "world".
  ```
-->

`if` 문에 대한 자세한 내용은 <doc:ControlFlow>를 참조한다.

같은 타입과 같은 수의 값을 가진 두 튜플을 비교할 수 있다. 튜플은 왼쪽에서 오른쪽으로 한 번에 하나의 값을 비교하며, 서로 다른 두 값을 찾을 때까지 비교를 진행한다. 이 두 값을 비교한 결과가 튜플 비교의 전체 결과를 결정한다. 모든 요소가 같으면 튜플 자체가 같다고 판단한다. 예를 들어:

```swift
(1, "zebra") < (2, "apple")   // 1이 2보다 작으므로 true; "zebra"와 "apple"은 비교하지 않음
(3, "apple") < (3, "bird")    // 3이 3과 같고, "apple"이 "bird"보다 작으므로 true
(4, "dog") == (4, "dog")      // 4가 4와 같고, "dog"가 "dog"와 같으므로 true
```

<!--
  - test: `tuple-comparison-operators`

  ```swifttest
  >> let a =
  -> (1, "zebra") < (2, "apple")   // true because 1 is less than 2; "zebra" and "apple" aren't compared
  >> let b =
  -> (3, "apple") < (3, "bird")    // true because 3 is equal to 3, and "apple" is less than "bird"
  >> let c =
  -> (4, "dog") == (4, "dog")      // true because 4 is equal to 4, and "dog" is equal to "dog"
  >> print(a, b, c)
  << true true true
  ```
-->

위 예제에서 첫 번째 줄의 왼쪽에서 오른쪽으로의 비교 동작을 확인할 수 있다. `1`이 `2`보다 작기 때문에, 튜플의 다른 값과 관계없이 `(1, "zebra")`는 `(2, "apple")`보다 작다고 판단한다. `"zebra"`가 `"apple"`보다 작지 않다는 사실은 중요하지 않다. 왜냐하면 비교는 이미 튜플의 첫 번째 요소에 의해 결정되었기 때문이다. 그러나 튜플의 첫 번째 요소가 같을 때는 두 번째 요소를 비교한다. 이는 두 번째와 세 번째 줄에서 볼 수 있다.

튜플은 해당 연산자가 각 튜플의 모든 값에 적용될 수 있는 경우에만 비교할 수 있다. 예를 들어, 아래 코드에서 보여주듯이 `<` 연산자를 사용해 `(String, Int)` 타입의 두 튜플을 비교할 수 있다. 이는 `String`과 `Int` 값 모두 `<` 연산자로 비교할 수 있기 때문이다. 반대로, `<` 연산자는 `Bool` 값에 적용할 수 없으므로 `(String, Bool)` 타입의 두 튜플은 `<` 연산자로 비교할 수 없다.

```swift
("blue", -1) < ("purple", 1)        // OK, true로 평가됨
("blue", false) < ("purple", true)  // < 연산자가 Boolean 값을 비교할 수 없으므로 에러
```

<!--
  - test: `tuple-comparison-operators-err`

  ```swifttest
  >> _ =
  -> ("blue", -1) < ("purple", 1)        // OK, evaluates to true
  >> _ =
  -> ("blue", false) < ("purple", true)  // Error because < can't compare Boolean values
  !$ error: type '(String, Bool)' cannot conform to 'Comparable'
  !! ("blue", false) < ("purple", true)  // Error because < can't compare Boolean values
  !!                 ^
  !$ note: only concrete types such as structs, enums and classes can conform to protocols
  !! ("blue", false) < ("purple", true)  // Error because < can't compare Boolean values
  !!                 ^
  !$ note: required by referencing operator function '<' on 'Comparable' where 'Self' = '(String, Bool)'
  !! ("blue", false) < ("purple", true)  // Error because < can't compare Boolean values
  !!                 ^
  ```
-->

<!--
  - test: `tuple-comparison-operators-ok`

  ```swifttest
  >> let x = ("blue", -1) < ("purple", 1)        // OK, evaluates to true
  >> print(x)
  << true
  ```
-->

> 참고: Swift 표준 라이브러리는 7개 미만의 요소를 가진 튜플에 대한 비교 연산자를 포함한다. 7개 이상의 요소를 가진 튜플을 비교하려면 직접 비교 연산자를 구현해야 한다.

<!--
  TODO: which types do these operate on by default?
  How do they work with strings?
  How about with your own types?
-->


## 삼항 조건 연산자

*삼항 조건 연산자*는 세 부분으로 이루어진 특별한 연산자로, `question ? answer1 : answer2` 형태를 가진다. 이 연산자는 `question`이 참인지 거짓인지에 따라 두 표현식 중 하나를 평가하는 간단한 방법을 제공한다. `question`이 참이면 `answer1`을 평가하고 그 값을 반환하며, 거짓이면 `answer2`를 평가하고 그 값을 반환한다.

삼항 조건 연산자는 아래 코드를 간략하게 표현한 것이다:

```swift
if question {
    answer1
} else {
    answer2
}
```

<!--
  - test: `ternaryConditionalOperatorOutline`

  ```swifttest
  >> let question = true
  >> let answer1 = true
  >> let answer2 = true
  -> if question {
        answer1
     } else {
        answer2
     }
  !! /tmp/swifttest.swift:5:4: warning: expression of type 'Bool' is unused
  !! answer1
  !! ^~~~~~~
  !! /tmp/swifttest.swift:7:4: warning: expression of type 'Bool' is unused
  !! answer2
  !! ^~~~~~~
  ```
-->

<!--
  FIXME This example has too much hand waving.
  Swift doesn't have 'if' expressions.
-->

다음은 테이블 행의 높이를 계산하는 예제이다. 행에 헤더가 있다면 콘텐츠 높이보다 50 포인트 더 높게 설정하고, 헤더가 없다면 20 포인트 더 높게 설정한다:

```swift
let contentHeight = 40
let hasHeader = true
let rowHeight = contentHeight + (hasHeader ? 50 : 20)
// rowHeight is equal to 90
```

<!--
  - test: `ternaryConditionalOperatorPart1`

  ```swifttest
  -> let contentHeight = 40
  -> let hasHeader = true
  -> let rowHeight = contentHeight + (hasHeader ? 50 : 20)
  /> rowHeight is equal to \(rowHeight)
  </ rowHeight is equal to 90
  ```
-->

위 예제는 아래 코드를 간략하게 표현한 것이다:

```swift
let contentHeight = 40
let hasHeader = true
let rowHeight: Int
if hasHeader {
    rowHeight = contentHeight + 50
} else {
    rowHeight = contentHeight + 20
}
// rowHeight is equal to 90
```

<!--
  - test: `ternaryConditionalOperatorPart2`

  ```swifttest
  -> let contentHeight = 40
  -> let hasHeader = true
  -> let rowHeight: Int
  -> if hasHeader {
        rowHeight = contentHeight + 50
     } else {
        rowHeight = contentHeight + 20
     }
  /> rowHeight is equal to \(rowHeight)
  </ rowHeight is equal to 90
  ```
-->

첫 번째 예제에서 삼항 조건 연산자를 사용하면 `rowHeight`를 한 줄의 코드로 올바른 값으로 설정할 수 있다. 이는 두 번째 예제에서 사용된 코드보다 더 간결하다.

삼항 조건 연산자는 두 표현식 중 어느 것을 고를지 결정하는 효율적인 방법을 제공한다. 하지만 삼항 조건 연산자를 사용할 때는 주의가 필요하다. 과도하게 사용하면 코드를 이해하기 어려워질 수 있다. 여러 삼항 조건 연산자를 하나의 복합문으로 결합하는 것은 피하는 것이 좋다.


## Nil-Coalescing 연산자

*nil-coalescing 연산자* (`a ?? b`)는 옵셔널 `a`에 값이 있으면 그 값을 언래핑하고, `a`가 `nil`이면 기본값 `b`를 반환한다. 표현식 `a`는 항상 옵셔널 타입이어야 하며, 표현식 `b`는 `a`에 저장된 타입과 일치해야 한다.

nil-coalescing 연산자는 아래 코드를 간결하게 표현한 것이다:

```swift
a != nil ? a! : b
```

<!--
  - test: `nilCoalescingOperatorOutline`

  ```swifttest
  >> var a: Int?
  >> let b = 42
  >> let c =
  -> a != nil ? a! : b
  >> print(c)
  << 42
  ```
-->

위 코드는 삼항 조건 연산자와 강제 언래핑(`a!`)을 사용해 `a`가 `nil`이 아닐 때 내부에 감싸진 값을 접근하고, 그렇지 않으면 `b`를 반환한다. nil-coalescing 연산자는 이러한 조건 검사와 언래핑을 간결하고 가독성 좋은 형태로 캡슐화한다.

> 참고: `a`의 값이 `nil`이 아닌 경우, `b`는 평가되지 않는다. 이를 *단락 평가(short-circuit evaluation)*라고 한다.

아래 예제는 nil-coalescing 연산자를 사용해 기본 색상 이름과 옵셔널 사용자 정의 색상 이름 중 하나를 선택한다:

```swift
let defaultColorName = "red"
var userDefinedColorName: String?   // 기본값은 nil

var colorNameToUse = userDefinedColorName ?? defaultColorName
// userDefinedColorName이 nil이므로 colorNameToUse는 기본값 "red"로 설정된다
```

<!--
  - test: `nilCoalescingOperator`

  ```swifttest
  -> let defaultColorName = "red"
  -> var userDefinedColorName: String?   // defaults to nil

  -> var colorNameToUse = userDefinedColorName ?? defaultColorName
  /> userDefinedColorName is nil, so colorNameToUse is set to the default of \"\(colorNameToUse)\"
  </ userDefinedColorName is nil, so colorNameToUse is set to the default of "red"
  ```
-->

`userDefinedColorName` 변수는 옵셔널 `String`으로 정의되며, 기본값은 `nil`이다. `userDefinedColorName`이 옵셔널 타입이므로 nil-coalescing 연산자를 사용해 그 값을 확인할 수 있다. 위 예제에서 이 연산자는 `colorNameToUse`라는 `String` 변수의 초기값을 결정하는 데 사용된다. `userDefinedColorName`이 `nil`이므로 `userDefinedColorName ?? defaultColorName` 표현식은 `defaultColorName`의 값인 `"red"`를 반환한다.

`userDefinedColorName`에 `nil`이 아닌 값을 할당하고 nil-coalescing 연산자 검사를 다시 수행하면, 기본값 대신 `userDefinedColorName`에 감싸진 값이 사용된다:

```swift
userDefinedColorName = "green"
colorNameToUse = userDefinedColorName ?? defaultColorName
// userDefinedColorName이 nil이 아니므로 colorNameToUse는 "green"으로 설정된다
```

<!--
  - test: `nilCoalescingOperator`

  ```swifttest
  -> userDefinedColorName = "green"
  -> colorNameToUse = userDefinedColorName ?? defaultColorName
  /> userDefinedColorName isn't nil, so colorNameToUse is set to \"\(colorNameToUse)\"
  </ userDefinedColorName isn't nil, so colorNameToUse is set to "green"
  ```
-->


## 범위 연산자

Swift는 여러 가지 *범위 연산자*를 제공한다. 이 연산자들은 값의 범위를 간결하게 표현할 수 있는 편의 기능이다.


### 닫힌 범위 연산자

*닫힌 범위 연산자*(`a...b`)는 `a`부터 `b`까지의 범위를 정의하며, `a`와 `b` 값을 모두 포함한다. `a` 값은 `b`보다 크지 않아야 한다.

<!--
  - test: `closedRangeStartCanBeLessThanEnd`

  ```swifttest
  -> let range = 1...2
  >> print(type(of: range))
  << ClosedRange<Int>
  ```
-->

<!--
  - test: `closedRangeStartCanBeTheSameAsEnd`

  ```swifttest
  -> let range = 1...1
  ```
-->

<!--
  - test: `closedRangeStartCannotBeGreaterThanEnd`

  ```swifttest
  -> let range = 1...0
  xx assertion
  ```
-->

닫힌 범위 연산자는 `for`-`in` 루프와 같이 모든 값을 사용하고자 할 때 유용하다.

```swift
for index in 1...5 {
    print("\(index) times 5 is \(index * 5)")
}
// 1 times 5 is 5
// 2 times 5 is 10
// 3 times 5 is 15
// 4 times 5 is 20
// 5 times 5 is 25
```

<!--
  - test: `rangeOperators`

  ```swifttest
  -> for index in 1...5 {
        print("\(index) times 5 is \(index * 5)")
     }
  </ 1 times 5 is 5
  </ 2 times 5 is 10
  </ 3 times 5 is 15
  </ 4 times 5 is 20
  </ 5 times 5 is 25
  ```
-->

`for`-`in` 루프에 대한 자세한 내용은 <doc:ControlFlow>를 참고한다.


### 반개방 범위 연산자

*반개방 범위 연산자*(`a..<b`)는 `a`부터 `b`까지의 범위를 정의하지만, `b`는 포함하지 않는다. 이 연산자는 첫 번째 값은 포함하지만 마지막 값은 포함하지 않기 때문에 *반개방*이라고 부른다. 닫힌 범위 연산자와 마찬가지로, `a`의 값은 `b`보다 크지 않아야 한다. 만약 `a`와 `b`의 값이 같다면, 결과 범위는 비어 있게 된다.

<!--
  - test: `halfOpenRangeStartCanBeLessThanEnd`

  ```swifttest
  -> let range = 1..<2
  >> print(type(of: range))
  << Range<Int>
  ```
-->

<!--
  - test: `halfOpenRangeStartCanBeTheSameAsEnd`

  ```swifttest
  -> let range = 1..<1
  ```
-->

<!--
  - test: `halfOpenRangeStartCannotBeGreaterThanEnd`

  ```swifttest
  -> let range = 1..<0
  xx assertion
  ```
-->

반개방 범위는 배열과 같이 0부터 시작하는 리스트를 다룰 때 특히 유용하다. 리스트의 길이까지 (하지만 포함하지 않고) 세는 데 적합하다:

```swift
let names = ["Anna", "Alex", "Brian", "Jack"]
let count = names.count
for i in 0..<count {
    print("Person \(i + 1) is called \(names[i])")
}
// Person 1 is called Anna
// Person 2 is called Alex
// Person 3 is called Brian
// Person 4 is called Jack
```

<!--
  - test: `rangeOperators`

  ```swifttest
  -> let names = ["Anna", "Alex", "Brian", "Jack"]
  -> let count = names.count
  >> assert(count == 4)
  -> for i in 0..<count {
        print("Person \(i + 1) is called \(names[i])")
     }
  </ Person 1 is called Anna
  </ Person 2 is called Alex
  </ Person 3 is called Brian
  </ Person 4 is called Jack
  ```
-->

배열에는 네 개의 항목이 있지만, `0..<count`는 마지막 항목의 인덱스인 `3`까지만 세는 것을 주목하자. 이는 반개방 범위이기 때문이다. 배열에 대한 더 자세한 내용은 <doc:CollectionTypes#Arrays>를 참고하자.


### 단방향 범위

닫힌 범위 연산자는 한쪽 방향으로 끝까지 계속되는 범위를 표현하는 대체 형태를 제공한다. 예를 들어, 배열의 인덱스 2부터 배열의 끝까지 모든 요소를 포함하는 범위를 들 수 있다. 이런 경우 범위 연산자의 한쪽 값을 생략할 수 있다. 이렇게 한쪽에만 값이 있는 범위를 *단방향 범위*라고 부른다. 예를 들어:

```swift
for name in names[2...] {
    print(name)
}
// Brian
// Jack

for name in names[...2] {
    print(name)
}
// Anna
// Alex
// Brian
```

<!--
  - test: `rangeOperators`

  ```swifttest
  -> for name in names[2...] {
         print(name)
     }
  </ Brian
  </ Jack

  -> for name in names[...2] {
         print(name)
     }
  </ Anna
  </ Alex
  </ Brian
  ```
-->

반열린 범위 연산자도 마지막 값만 지정하는 단방향 형태가 있다. 양쪽에 값을 포함할 때와 마찬가지로, 마지막 값은 범위에 포함되지 않는다. 예를 들어:

```swift
for name in names[..<2] {
    print(name)
}
// Anna
// Alex
```

<!--
  - test: `rangeOperators`

  ```swifttest
  -> for name in names[..<2] {
         print(name)
     }
  </ Anna
  </ Alex
  ```
-->

단방향 범위는 서브스크립트 외의 다른 상황에서도 사용할 수 있다. 시작 값을 생략한 단방향 범위는 반복을 시작할 위치가 명확하지 않기 때문에 반복할 수 없다. 하지만 마지막 값을 생략한 단방향 범위는 반복할 수 있다. 다만, 범위가 무한히 계속되므로 반드시 루프에 명시적인 종료 조건을 추가해야 한다. 또한 특정 값이 단방향 범위에 포함되는지 확인할 수도 있다. 아래 코드에서 이를 확인할 수 있다.

```swift
let range = ...5
range.contains(7)   // false
range.contains(4)   // true
range.contains(-1)  // true
```

<!--
  - test: `rangeOperators`

  ```swifttest
  -> let range = ...5
  >> print(type(of: range))
  << PartialRangeThrough<Int>
  >> let a =
  -> range.contains(7)   // false
  >> let b =
  -> range.contains(4)   // true
  >> let c =
  -> range.contains(-1)  // true
  >> print(a, b, c)
  << false true true
  ```
-->


## 논리 연산자

*논리 연산자*는 불리언(Boolean) 논리 값인 `true`와 `false`를 수정하거나 결합한다. Swift는 C 기반 언어에서 사용하는 세 가지 표준 논리 연산자를 지원한다:

- 논리 NOT (`!a`)
- 논리 AND (`a && b`)
- 논리 OR (`a || b`)


### 논리적 NOT 연산자

*논리적 NOT 연산자*(`!a`)는 불리언 값을 반전시킨다. `true`는 `false`가 되고, `false`는 `true`가 된다.

논리적 NOT 연산자는 접두사 연산자로, 연산 대상 값 바로 앞에 공백 없이 위치한다. 이 연산자는 "`a`가 아니다"로 읽을 수 있으며, 다음 예제에서 확인할 수 있다:

```swift
let allowedEntry = false
if !allowedEntry {
    print("ACCESS DENIED")
}
// Prints "ACCESS DENIED"
```

<!--
  - test: `logicalOperators`

  ```swifttest
  -> let allowedEntry = false
  -> if !allowedEntry {
        print("ACCESS DENIED")
     }
  <- ACCESS DENIED
  ```
-->

`if !allowedEntry`라는 구문은 "만약 입장이 허용되지 않았다면"으로 해석할 수 있다. 이어지는 코드는 "입장이 허용되지 않았다"가 참일 때, 즉 `allowedEntry`가 `false`일 때만 실행된다.

이 예제에서 볼 수 있듯이, 불리언 상수와 변수의 이름을 신중하게 선택하면 코드의 가독성과 간결성을 높일 수 있다. 또한 이중 부정이나 혼란스러운 논리문을 피하는 데도 도움이 된다.


### 논리 AND 연산자

*논리 AND 연산자* (`a && b`)는 두 값이 모두 `true`여야 전체 표현식도 `true`가 되는 논리 표현식을 만든다.

두 값 중 하나라도 `false`라면, 전체 표현식도 `false`가 된다. 사실, *첫 번째* 값이 `false`라면 두 번째 값은 평가조차 되지 않는다. 왜냐하면 두 번째 값이 무엇이든 전체 표현식을 `true`로 만들 수 없기 때문이다. 이를 *단락 평가(short-circuit evaluation)*라고 한다.

다음 예제는 두 개의 `Bool` 값을 확인하고, 두 값이 모두 `true`일 때만 접근을 허용한다:

```swift
let enteredDoorCode = true
let passedRetinaScan = false
if enteredDoorCode && passedRetinaScan {
    print("Welcome!")
} else {
    print("ACCESS DENIED")
}
// Prints "ACCESS DENIED"
```

<!--
  - test: `logicalOperators`

  ```swifttest
  -> let enteredDoorCode = true
  -> let passedRetinaScan = false
  -> if enteredDoorCode && passedRetinaScan {
        print("Welcome!")
     } else {
        print("ACCESS DENIED")
     }
  <- ACCESS DENIED
  ```
-->


### 논리 OR 연산자

*논리 OR 연산자* (`a || b`)는 두 개의 파이프 문자를 연속해서 사용하는 중위 연산자이다. 이 연산자를 사용하면 두 값 중 *하나*만 `true`여도 전체 표현식이 `true`가 되는 논리 표현식을 만들 수 있다.

앞서 설명한 논리 AND 연산자와 마찬가지로, 논리 OR 연산자도 단락 평가(short-circuit evaluation)를 사용해 표현식을 평가한다. 논리 OR 표현식의 왼쪽이 `true`라면 오른쪽은 평가하지 않는다. 왜냐하면 오른쪽을 평가해도 전체 표현식의 결과가 바뀌지 않기 때문이다.

아래 예제에서 첫 번째 `Bool` 값 (`hasDoorKey`)은 `false`지만, 두 번째 값 (`knowsOverridePassword`)은 `true`이다. 두 값 중 하나가 `true`이므로 전체 표현식도 `true`로 평가되며, 접근이 허용된다:

```swift
let hasDoorKey = false
let knowsOverridePassword = true
if hasDoorKey || knowsOverridePassword {
    print("Welcome!")
} else {
    print("ACCESS DENIED")
}
// Prints "Welcome!"
```

<!--
  - test: `logicalOperators`

  ```swifttest
  -> let hasDoorKey = false
  -> let knowsOverridePassword = true
  -> if hasDoorKey || knowsOverridePassword {
        print("Welcome!")
     } else {
        print("ACCESS DENIED")
     }
  <- Welcome!
  ```
-->


### 논리 연산자 결합하기

여러 논리 연산자를 결합해 더 긴 복합 표현식을 만들 수 있다:

```swift
if enteredDoorCode && passedRetinaScan || hasDoorKey || knowsOverridePassword {
    print("Welcome!")
} else {
    print("ACCESS DENIED")
}
// Prints "Welcome!"
```

<!--
  - test: `logicalOperators`

  ```swifttest
  -> if enteredDoorCode && passedRetinaScan || hasDoorKey || knowsOverridePassword {
        print("Welcome!")
     } else {
        print("ACCESS DENIED")
     }
  <- Welcome!
  ```
-->

이 예제는 여러 `&&`와 `||` 연산자를 사용해 더 긴 복합 표현식을 만든다. 하지만 `&&`와 `||` 연산자는 여전히 두 개의 값에 대해 작동하므로, 이 예제는 사실 세 개의 작은 표현식이 연결된 것이다. 이 예제를 다음과 같이 해석할 수 있다:

만약 올바른 도어 코드를 입력하고 망막 스캔을 통과했거나, 유효한 도어 키를 가지고 있거나, 긴급 재정 비밀번호를 알고 있다면 접근을 허용한다.

`enteredDoorCode`, `passedRetinaScan`, `hasDoorKey`의 값에 따라 처음 두 하위 표현식은 `false`다. 하지만 긴급 재정 비밀번호를 알고 있으므로 전체 복합 표현식은 여전히 `true`로 평가된다.

> 참고: Swift의 논리 연산자 `&&`와 `||`는 왼쪽 결합성을 가진다. 즉, 여러 논리 연산자가 포함된 복합 표현식은 가장 왼쪽의 하위 표현식부터 먼저 평가한다.


### 명시적 괄호 사용

복잡한 표현식의 의도를 더 명확히 전달하기 위해 괄호를 사용하는 것이 유용할 때가 있다. 괄호가 반드시 필요하지 않더라도, 코드의 가독성을 높이는 데 도움이 된다. 위의 문 접근 예제에서, 복합 표현식의 첫 부분에 괄호를 추가하면 의도가 더 명확해진다:

```swift
if (enteredDoorCode && passedRetinaScan) || hasDoorKey || knowsOverridePassword {
    print("Welcome!")
} else {
    print("ACCESS DENIED")
}
// Prints "Welcome!"
```

<!--
  - test: `logicalOperators`

  ```swifttest
  -> if (enteredDoorCode && passedRetinaScan) || hasDoorKey || knowsOverridePassword {
        print("Welcome!")
     } else {
        print("ACCESS DENIED")
     }
  <- Welcome!
  ```
-->

괄호를 사용하면 처음 두 값이 전체 논리에서 별도의 가능한 상태로 간주된다는 점을 명확히 할 수 있다. 복합 표현식의 결과는 변하지 않지만, 전체 의도가 독자에게 더 명확해진다. 간결함보다는 가독성을 우선시하라. 의도를 명확히 하는 데 도움이 된다면 괄호를 사용한다.

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


