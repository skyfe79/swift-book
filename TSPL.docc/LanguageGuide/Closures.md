# 클로저

클로저는 이름 없는 함수를 만들지 않고도 함께 실행되는 코드를 그룹화한다. 클로저는 코드에서 전달하고 사용할 수 있는 독립적인 기능 블록이다. Swift의 클로저는 다른 프로그래밍 언어의 클로저, 익명 함수, 람다, 블록과 유사하다.

클로저는 정의된 문맥에서 상수와 변수에 대한 참조를 캡처하고 저장할 수 있다. 이를 클로저가 해당 상수와 변수를 *캡처*한다고 한다. Swift는 캡처와 관련된 모든 메모리 관리를 자동으로 처리한다.

> 참고: 캡처 개념이 익숙하지 않더라도 걱정하지 말자. 아래 <doc:Closures#Capturing-Values>에서 자세히 설명한다.

<doc:Functions>에서 소개한 전역 함수와 중첩 함수는 사실 클로저의 특수한 형태다. 클로저는 세 가지 형태로 나타난다:

- 전역 함수는 이름이 있고 어떤 값도 캡처하지 않는 클로저다.
- 중첩 함수는 이름이 있고 자신을 감싸는 함수로부터 값을 캡처할 수 있는 클로저다.
- 클로저 표현식은 가벼운 문법으로 작성된 이름 없는 클로저로, 주변 문맥에서 값을 캡처할 수 있다.

Swift의 클로저 표현식은 깔끔하고 명확한 스타일을 가지며, 일반적인 시나리오에서 간결하고 복잡하지 않은 문법을 장려하는 최적화를 포함한다. 이러한 최적화는 다음과 같다:

- 문맥에서 매개변수와 반환 값 타입을 유추
- 단일 표현식 클로저에서 암시적 반환
- 짧은 인수 이름
- 후행 클로저 문법


## 클로저 표현식

<doc:Functions#Nested-Functions>에서 소개한 중첩 함수는 
더 큰 함수의 일부로 독립적인 코드 블록에 이름을 붙이고 정의하는 편리한 방법이다. 
하지만 때로는 완전한 선언과 이름 없이 함수와 유사한 구조를 짧게 작성하는 것이 유용할 때가 있다. 
이러한 경우는 특히 함수나 메서드가 인자로 함수를 하나 이상 받을 때 더욱 두드러진다.

*클로저 표현식*은 간결하고 명확한 문법으로 인라인 클로저를 작성하는 방법이다. 
클로저 표현식은 명확성이나 의도를 잃지 않으면서도 짧은 형태로 클로저를 작성할 수 있는 여러 문법 최적화를 제공한다. 
아래의 클로저 표현식 예제들은 `sorted(by:)` 메서드의 단일 예제를 여러 번 반복하며 점점 더 간결하게 
동일한 기능을 표현하는 방식으로 이러한 최적화를 보여준다.


### `sorted(by:)` 메서드

Swift 표준 라이브러리는 `sorted(by:)`라는 메서드를 제공한다. 이 메서드는 특정 타입의 값으로 이루어진 배열을 정렬하며, 사용자가 제공한 클로저를 기준으로 정렬을 수행한다. 정렬이 완료되면, `sorted(by:)` 메서드는 원본 배열과 동일한 타입과 크기를 가진 새로운 배열을 반환한다. 이때 원본 배열은 수정되지 않는다.

아래 클로저 표현 예제는 `sorted(by:)` 메서드를 사용해 `String` 타입의 배열을 알파벳 역순으로 정렬한다. 다음은 정렬할 초기 배열이다:

```swift
let names = ["Chris", "Alex", "Ewa", "Barry", "Daniella"]
```

`sorted(by:)` 메서드는 배열의 요소와 동일한 타입의 두 인자를 받는 클로저를 인자로 받는다. 이 클로저는 정렬 후 첫 번째 값이 두 번째 값보다 앞에 위치해야 하는지 여부를 나타내는 `Bool` 값을 반환한다. 첫 번째 값이 두 번째 값보다 앞에 위치해야 한다면 클로저는 `true`를 반환하고, 그렇지 않으면 `false`를 반환한다.

이 예제에서는 `String` 타입의 배열을 정렬하므로, 클로저는 `(String, String) -> Bool` 타입의 함수여야 한다.

클로저를 제공하는 한 가지 방법은 적절한 타입의 일반 함수를 작성한 후, 이를 `sorted(by:)` 메서드의 인자로 전달하는 것이다:

```swift
func backward(_ s1: String, _ s2: String) -> Bool {
    return s1 > s2
}
var reversedNames = names.sorted(by: backward)
// reversedNames는 ["Ewa", "Daniella", "Chris", "Barry", "Alex"]와 같다.
```

첫 번째 문자열(`s1`)이 두 번째 문자열(`s2`)보다 크다면, `backward(_:_:)` 함수는 `true`를 반환한다. 이는 정렬된 배열에서 `s1`이 `s2`보다 앞에 위치해야 함을 의미한다. 문자열의 문자에 대해 "크다"는 "알파벳 순서상 뒤에 위치한다"는 뜻이다. 따라서 `"B"`는 `"A"`보다 크고, `"Tom"`은 `"Tim"`보다 크다. 이렇게 하면 알파벳 역순으로 정렬되며, `"Barry"`가 `"Alex"`보다 앞에 위치하게 된다.

그러나 이는 단순히 `a > b`와 같은 단일 표현식 함수를 작성하는 데 비해 다소 장황한 방법이다. 이 예제에서는 클로저 표현식을 사용해 정렬 클로저를 인라인으로 작성하는 것이 더 적절하다.


### 클로저 표현식 문법

클로저 표현식 문법은 다음과 같은 일반적인 형태를 가진다:

```swift
{ (<#parameters#>) -> <#return type#> in
   <#statements#>
}
```

클로저 표현식 문법에서 *파라미터*는 in-out 파라미터를 사용할 수 있지만, 기본값을 가질 수는 없다. 가변 파라미터를 사용하려면 가변 파라미터에 이름을 지정해야 한다. 튜플도 파라미터 타입과 반환 타입으로 사용할 수 있다.

아래 예제는 앞서 설명한 `backward(_:_:)` 함수의 클로저 표현식 버전을 보여준다:

```swift
reversedNames = names.sorted(by: { (s1: String, s2: String) -> Bool in
    return s1 > s2
})
```

<!--
  - test: `closureSyntax`

  ```swifttest
  -> reversedNames = names.sorted(by: { (s1: String, s2: String) -> Bool in
        return s1 > s2
     })
  >> assert(reversedNames == ["Ewa", "Daniella", "Chris", "Barry", "Alex"])
  ```
-->

이 인라인 클로저의 파라미터와 반환 타입 선언은 `backward(_:_:)` 함수의 선언과 동일하다. 두 경우 모두 `(s1: String, s2: String) -> Bool`로 작성된다. 그러나 인라인 클로저 표현식에서는 파라미터와 반환 타입이 중괄호 *안쪽*에 작성되며, 바깥쪽에 있지 않다.

클로저의 본문은 `in` 키워드로 시작한다. 이 키워드는 클로저의 파라미터와 반환 타입 정의가 끝났음을 나타내며, 클로저의 본문이 시작될 것임을 알린다.

클로저의 본문이 매우 짧기 때문에, 심지어 한 줄로 작성할 수도 있다:

```swift
reversedNames = names.sorted(by: { (s1: String, s2: String) -> Bool in return s1 > s2 } )
```

<!--
  - test: `closureSyntax`

  ```swifttest
  -> reversedNames = names.sorted(by: { (s1: String, s2: String) -> Bool in return s1 > s2 } )
  >> assert(reversedNames == ["Ewa", "Daniella", "Chris", "Barry", "Alex"])
  ```
-->

이 예제는 `sorted(by:)` 메서드에 대한 전체 호출이 동일하게 유지됨을 보여준다. 메서드의 전체 인자를 감싸는 괄호 쌍은 여전히 존재한다. 그러나 이제 그 인자는 인라인 클로저가 된다.


### 문맥에서 타입 추론하기

정렬 클로저가 메서드의 인자로 전달되기 때문에, Swift는 클로저의 매개변수 타입과 반환 타입을 추론할 수 있다. `sorted(by:)` 메서드는 문자열 배열에 대해 호출되므로, 이 메서드의 인자는 `(String, String) -> Bool` 타입의 함수여야 한다. 이는 `(String, String)`과 `Bool` 타입을 클로저 표현식 정의에 명시적으로 작성할 필요가 없음을 의미한다. 모든 타입을 추론할 수 있기 때문에, 반환 화살표(`->`)와 매개변수 이름 주위의 괄호도 생략할 수 있다:

```swift
reversedNames = names.sorted(by: { s1, s2 in return s1 > s2 } )
```

<!--
  - test: `closureSyntax`

  ```swifttest
  -> reversedNames = names.sorted(by: { s1, s2 in return s1 > s2 } )
  >> assert(reversedNames == ["Ewa", "Daniella", "Chris", "Barry", "Alex"])
  ```
-->

인라인 클로저 표현식으로 함수나 메서드에 클로저를 전달할 때는 항상 매개변수 타입과 반환 타입을 추론할 수 있다. 따라서 클로저가 함수나 메서드의 인자로 사용될 때는 완전한 형태로 작성할 필요가 없다.

그러나 원한다면 타입을 명시적으로 작성할 수도 있으며, 코드를 읽는 사람에게 모호함을 피하기 위해 타입을 명시하는 것이 권장된다. `sorted(by:)` 메서드의 경우, 정렬이 이루어진다는 사실에서 클로저의 목적이 명확하며, 문자열 배열을 정렬하는 데 사용되므로 클로저가 `String` 값을 다룬다고 안전하게 추측할 수 있다.


### 단일 표현식 클로저의 암시적 반환

단일 표현식 클로저는 `return` 키워드를 생략하고 표현식의 결과를 암시적으로 반환할 수 있다. 이전 예제를 다음과 같이 간결하게 작성할 수 있다:

```swift
reversedNames = names.sorted(by: { s1, s2 in s1 > s2 } )
```

<!--
  - test: `closureSyntax`

  ```swifttest
  -> reversedNames = names.sorted(by: { s1, s2 in s1 > s2 } )
  >> assert(reversedNames == ["Ewa", "Daniella", "Chris", "Barry", "Alex"])
  ```
-->

여기서 `sorted(by:)` 메서드의 인자 타입은 클로저가 `Bool` 값을 반환해야 함을 명확히 한다. 클로저의 본문이 `Bool` 값을 반환하는 단일 표현식(`s1 > s2`)으로 구성되어 있기 때문에, `return` 키워드를 생략해도 모호함이 없다.


### 짧은 인자 이름

Swift는 인라인 클로저에 대해 자동으로 짧은 인자 이름을 제공한다. 이를 통해 클로저의 인자 값을 `$0`, `$1`, `$2` 등의 이름으로 참조할 수 있다.

클로저 표현식 내에서 이러한 짧은 인자 이름을 사용하면, 클로저의 인자 목록을 정의에서 생략할 수 있다. 짧은 인자 이름의 타입은 예상되는 함수 타입에서 추론되며, 사용된 가장 높은 번호의 짧은 인자 이름이 클로저가 받는 인자의 수를 결정한다. 또한 `in` 키워드도 생략할 수 있다. 클로저 표현식이 전체적으로 본문으로 구성되기 때문이다:

```swift
reversedNames = names.sorted(by: { $0 > $1 } )
```

<!--
  - test: `closureSyntax`

  ```swifttest
  -> reversedNames = names.sorted(by: { $0 > $1 } )
  >> assert(reversedNames == ["Ewa", "Daniella", "Chris", "Barry", "Alex"])
  ```
-->

여기서 `$0`과 `$1`은 클로저의 첫 번째와 두 번째 `String` 인자를 가리킨다. `$1`이 가장 높은 번호의 짧은 인자 이름이므로, 이 클로저는 두 개의 인자를 받는 것으로 이해된다. 또한 `sorted(by:)` 함수는 두 인자가 모두 문자열인 클로저를 기대하므로, `$0`과 `$1`은 모두 `String` 타입이다.

<!--
  - test: `closure-syntax-arity-inference`

  ```swifttest
  >> let a: [String: String] = [:]
  >> var b: [String: String] = [:]
  >> b.merge(a, uniquingKeysWith: { $1 })
  >> b.merge(a, uniquingKeysWith: { $0 })
  !$ error: contextual closure type '(String, String) throws -> String' expects 2 arguments, but 1 was used in closure body
  !! b.merge(a, uniquingKeysWith: { $0 })
  !! ^
  ```
-->


### 연산자 메서드

위의 클로저 표현식을 더 짧게 작성할 수 있는 방법이 있다. Swift의 `String` 타입은 '보다 큼' 연산자(`>`)에 대한 문자열 전용 구현을 메서드로 정의한다. 이 메서드는 두 개의 `String` 타입 매개변수를 받고 `Bool` 타입의 값을 반환한다. 이는 `sorted(by:)` 메서드에서 요구하는 메서드 타입과 정확히 일치한다. 따라서 '보다 큼' 연산자를 그대로 전달하면 Swift는 문자열 전용 구현을 사용하려는 의도를 자동으로 추론한다.

```swift
reversedNames = names.sorted(by: >)
```

<!--
  - test: `closureSyntax`

  ```swifttest
  -> reversedNames = names.sorted(by: >)
  >> assert(reversedNames == ["Ewa", "Daniella", "Chris", "Barry", "Alex"])
  ```
-->

연산자 메서드에 대한 더 자세한 내용은 <doc:AdvancedOperators#Operator-Methods>를 참고한다.


## 트레일링 클로저

함수의 마지막 인자로 클로저 표현식을 전달해야 하고, 그 클로저 표현식이 길다면 *트레일링 클로저*로 작성하는 것이 유용하다. 트레일링 클로저는 함수 호출의 괄호 뒤에 작성하며, 여전히 함수의 인자로 간주된다. 트레일링 클로저 구문을 사용할 때는 첫 번째 클로저의 인자 레이블을 함수 호출 부분에 작성하지 않는다. 함수 호출은 여러 개의 트레일링 클로저를 포함할 수 있지만, 아래 예제들은 단일 트레일링 클로저를 사용한다.

```swift
func someFunctionThatTakesAClosure(closure: () -> Void) {
    // 함수 본문
}

// 트레일링 클로저를 사용하지 않고 함수를 호출하는 방법:

someFunctionThatTakesAClosure(closure: {
    // 클로저 본문
})

// 트레일링 클로저를 사용하여 함수를 호출하는 방법:

someFunctionThatTakesAClosure() {
    // 트레일링 클로저 본문
}
```

<!--
  - test: `closureSyntax`

  ```swifttest
  -> func someFunctionThatTakesAClosure(closure: () -> Void) {
        // 함수 본문
     }

  -> // 트레일링 클로저를 사용하지 않고 함수를 호출하는 방법:

  -> someFunctionThatTakesAClosure(closure: {
        // 클로저 본문
     })

  -> // 트레일링 클로저를 사용하여 함수를 호출하는 방법:

  -> someFunctionThatTakesAClosure() {
        // 트레일링 클로저 본문
     }
  ```
-->

앞서 <doc:Closures#Closure-Expression-Syntax> 섹션에서 다룬 문자열 정렬 클로저는 `sorted(by:)` 메서드의 괄호 밖에 트레일링 클로저로 작성할 수 있다:

```swift
reversedNames = names.sorted() { $0 > $1 }
```

<!--
  - test: `closureSyntax`

  ```swifttest
  -> reversedNames = names.sorted() { $0 > $1 }
  >> assert(reversedNames == ["Ewa", "Daniella", "Chris", "Barry", "Alex"])
  ```
-->

클로저 표현식이 함수나 메서드의 유일한 인자로 제공되고, 이를 트레일링 클로저로 전달한다면 함수나 메서드 이름 뒤에 괄호 `()`를 작성할 필요가 없다:

```swift
reversedNames = names.sorted { $0 > $1 }
```

<!--
  - test: `closureSyntax`

  ```swifttest
  -> reversedNames = names.sorted { $0 > $1 }
  >> assert(reversedNames == ["Ewa", "Daniella", "Chris", "Barry", "Alex"])
  ```
-->

트레일링 클로저는 클로저가 충분히 길어서 한 줄에 인라인으로 작성하기 어려울 때 가장 유용하다. 예를 들어, Swift의 `Array` 타입은 `map(_:)` 메서드를 제공하는데, 이 메서드는 클로저 표현식을 단일 인자로 받는다. 이 클로저는 배열의 각 항목에 대해 한 번씩 호출되며, 해당 항목에 대한 변환된 값(다른 타입일 수도 있음)을 반환한다. `map(_:)`에 전달하는 클로저 내부에 코드를 작성하여 변환의 성격과 반환 값의 타입을 지정한다.

제공된 클로저를 각 배열 요소에 적용한 후, `map(_:)` 메서드는 원래 배열의 순서에 따라 모든 새로운 변환된 값을 포함하는 새 배열을 반환한다.

다음은 `map(_:)` 메서드를 트레일링 클로저와 함께 사용하여 `Int` 값 배열을 `String` 값 배열로 변환하는 예제다. 배열 `[16, 58, 510]`을 사용하여 새 배열 `["OneSix", "FiveEight", "FiveOneZero"]`를 생성한다:

```swift
let digitNames = [
    0: "Zero", 1: "One", 2: "Two",   3: "Three", 4: "Four",
    5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
]
let numbers = [16, 58, 510]
```

<!--
  - test: `arrayMap`

  ```swifttest
  -> let digitNames = [
        0: "Zero", 1: "One", 2: "Two",   3: "Three", 4: "Four",
        5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
     ]
  -> let numbers = [16, 58, 510]
  ```
-->

위 코드는 정수 숫자와 영어 이름 간의 매핑을 담은 딕셔너리를 생성한다. 또한 문자열로 변환할 준비가 된 정수 배열도 정의한다.

이제 `numbers` 배열을 사용하여 `String` 값 배열을 생성할 수 있다. 배열의 `map(_:)` 메서드에 클로저 표현식을 트레일링 클로저로 전달하면 된다:

```swift
let strings = numbers.map { (number) -> String in
    var number = number
    var output = ""
    repeat {
        output = digitNames[number % 10]! + output
        number /= 10
    } while number > 0
    return output
}
// strings는 [String] 타입으로 추론됨
// 값은 ["OneSix", "FiveEight", "FiveOneZero"]
```

<!--
  - test: `arrayMap`

  ```swifttest
  -> let strings = numbers.map { (number) -> String in
        var number = number
        var output = ""
        repeat {
           output = digitNames[number % 10]! + output
           number /= 10
        } while number > 0
        return output
     }
  // strings는 [String] 타입으로 추론됨
  /> 값은 [\"\(strings[0])\", \"\(strings[1])\", \"\(strings[2])\"]
  </ 값은 ["OneSix", "FiveEight", "FiveOneZero"]
  ```
-->

`map(_:)` 메서드는 배열의 각 항목에 대해 클로저 표현식을 한 번씩 호출한다. 클로저의 입력 매개변수 `number`의 타입을 명시할 필요는 없는데, 배열의 값으로부터 타입을 추론할 수 있기 때문이다.

이 예제에서 변수 `number`는 클로저의 `number` 매개변수 값으로 초기화되므로, 클로저 본문 내에서 값을 수정할 수 있다. (함수와 클로저의 매개변수는 항상 상수다.) 클로저 표현식은 또한 `String` 반환 타입을 지정하여, 변환된 출력 배열에 저장될 타입을 나타낸다.

클로저 표현식은 호출될 때마다 `output`이라는 문자열을 생성한다. 나머지 연산자(`number % 10`)를 사용해 `number`의 마지막 자릿수를 계산하고, 이 자릿수를 사용해 `digitNames` 딕셔너리에서 적절한 문자열을 찾는다. 이 클로저는 0보다 큰 정수의 문자열 표현을 생성하는 데 사용할 수 있다.

> 참고: `digitNames` 딕셔너리의 서브스크립트 호출 뒤에는 느낌표(`!`)가 붙는다. 딕셔너리 서브스크립트는 키가 존재하지 않을 경우 실패할 수 있음을 나타내기 위해 옵셔널 값을 반환하기 때문이다. 위 예제에서 `number % 10`은 항상 `digitNames` 딕셔너리의 유효한 서브스크립트 키가 되므로, 느낌표를 사용해 옵셔널 반환 값에 저장된 `String` 값을 강제로 언래핑한다.

`digitNames` 딕셔너리에서 검색된 문자열은 `output`의 *앞쪽*에 추가되며, 이는 숫자의 문자열 버전을 역순으로 생성하는 효과가 있다. (`number % 10` 표현식은 `16`에 대해 `6`, `58`에 대해 `8`, `510`에 대해 `0`을 반환한다.)

그런 다음 `number` 변수를 `10`으로 나눈다. 정수이므로 나눗셈 중에 버림이 발생하며, `16`은 `1`, `58`은 `5`, `510`은 `51`이 된다.

이 과정은 `number`가 `0`이 될 때까지 반복되며, 이 시점에서 `output` 문자열이 클로저에 의해 반환되고, `map(_:)` 메서드에 의해 출력 배열에 추가된다.

위 예제에서 트레일링 클로저 구문을 사용하면 클로저의 기능을 지원하는 함수 바로 뒤에 깔끔하게 캡슐화할 수 있으며, 전체 클로저를 `map(_:)` 메서드의 외부 괄호 안에 감쌀 필요가 없다.

함수가 여러 개의 클로저를 받는 경우, 첫 번째 트레일링 클로저의 인자 레이블을 생략하고 나머지 트레일링 클로저에 레이블을 붙인다. 예를 들어, 아래 함수는 사진 갤러리를 위해 사진을 로드한다:

```swift
func loadPicture(from server: Server, completion: (Picture) -> Void, onFailure: () -> Void) {
    if let picture = download("photo.jpg", from: server) {
        completion(picture)
    } else {
        onFailure()
    }
}
```

<!--
  - test: `multiple-trailing-closures`

  ```swifttest
  >> struct Server { }
  >> struct Picture { }
  >> func download(_ path: String, from server: Server) -> Picture? {
  >>     return Picture()
  >> }
  -> func loadPicture(from server: Server, completion: (Picture) -> Void, onFailure: () -> Void) {
         if let picture = download("photo.jpg", from: server) {
             completion(picture)
         } else {
             onFailure()
         }
     }
  ```
-->

이 함수를 호출하여 사진을 로드할 때 두 개의 클로저를 제공한다. 첫 번째 클로저는 성공적으로 다운로드한 후 사진을 표시하는 완료 핸들러다. 두 번째 클로저는 사용자에게 오류를 표시하는 오류 핸들러다.

```swift
loadPicture(from: someServer) { picture in
    someView.currentPicture = picture
} onFailure: {
    print("다음 사진을 다운로드할 수 없습니다.")
}
```

<!--
  - test: `multiple-trailing-closures`

  ```swifttest
  >> struct View {
  >>    var currentPicture = Picture() { didSet { print("사진 변경됨") } }
  >> }
  >> var someView = View()
  >> let someServer = Server()
  -> loadPicture(from: someServer) { picture in
         someView.currentPicture = picture
     } onFailure: {
         print("다음 사진을 다운로드할 수 없습니다.")
     }
  << 사진 변경됨
  ```
-->

이 예제에서 `loadPicture(from:completion:onFailure:)` 함수는 네트워크 작업을 백그라운드로 보내고, 네트워크 작업이 완료되면 두 완료 핸들러 중 하나를 호출한다. 이 방식으로 함수를 작성하면 네트워크 실패를 처리하는 코드와 성공적인 다운로드 후 사용자 인터페이스를 업데이트하는 코드를 깔끔하게 분리할 수 있으며, 두 상황을 모두 처리하는 단일 클로저를 사용하지 않아도 된다.

> 참고: 완료 핸들러는 특히 여러 핸들러를 중첩해야 할 경우 읽기 어려워질 수 있다. 대안으로 <doc:Concurrency>에서 설명한 비동기 코드를 사용할 수 있다.


## 값 캡처하기

클로저는 정의된 주변 컨텍스트에서 상수와 변수를 *캡처*할 수 있다. 클로저는 본문 내에서 이러한 상수와 변수를 참조하고 수정할 수 있으며, 원래 상수와 변수가 정의된 스코프가 더 이상 존재하지 않더라도 이를 사용할 수 있다.

Swift에서 값을 캡처할 수 있는 가장 간단한 형태의 클로저는 다른 함수 내부에 작성된 중첩 함수다. 중첩 함수는 외부 함수의 인자를 캡처할 수 있으며, 외부 함수 내부에서 정의된 상수와 변수도 캡처할 수 있다.

다음은 `makeIncrementer`라는 함수의 예시로, 이 함수는 `incrementer`라는 중첩 함수를 포함한다. 중첩 함수 `incrementer()`는 주변 컨텍스트에서 `runningTotal`과 `amount`라는 두 값을 캡처한다. 이 값을 캡처한 후, `incrementer`는 `makeIncrementer`에 의해 클로저로 반환되며, 호출될 때마다 `runningTotal`을 `amount`만큼 증가시킨다.

```swift
func makeIncrementer(forIncrement amount: Int) -> () -> Int {
    var runningTotal = 0
    func incrementer() -> Int {
        runningTotal += amount
        return runningTotal
    }
    return incrementer
}
```

`makeIncrementer`의 반환 타입은 `() -> Int`다. 이는 단순한 값이 아니라 *함수*를 반환한다는 의미다. 반환된 함수는 매개변수가 없으며, 호출될 때마다 `Int` 값을 반환한다. 함수가 다른 함수를 반환하는 방법에 대해 더 알아보려면 <doc:Functions#Function-Types-as-Return-Types>를 참고한다.

`makeIncrementer(forIncrement:)` 함수는 반환될 증분기의 현재 누적 값을 저장하기 위해 `runningTotal`이라는 정수 변수를 정의한다. 이 변수는 `0`으로 초기화된다.

`makeIncrementer(forIncrement:)` 함수는 `forIncrement`라는 인자 레이블과 `amount`라는 매개변수 이름을 가진 단일 `Int` 매개변수를 갖는다. 이 매개변수에 전달된 값은 반환된 증분기 함수가 호출될 때마다 `runningTotal`이 얼마나 증가해야 하는지를 지정한다. `makeIncrementer` 함수는 실제 증분을 수행하는 `incrementer`라는 중첩 함수를 정의한다. 이 함수는 단순히 `amount`를 `runningTotal`에 더하고 결과를 반환한다.

중첩 함수 `incrementer()`를 따로 보면 다소 특이해 보일 수 있다:

```swift
func incrementer() -> Int {
    runningTotal += amount
    return runningTotal
}
```

`incrementer()` 함수는 매개변수가 없지만, 함수 본문 내에서 `runningTotal`과 `amount`를 참조한다. 이는 주변 함수에서 `runningTotal`과 `amount`에 대한 *참조*를 캡처하고 이를 자신의 함수 본문 내에서 사용함으로써 가능하다. 참조로 캡처하면 `makeIncrementer` 호출이 끝나더라도 `runningTotal`과 `amount`가 사라지지 않으며, 다음에 `incrementer` 함수가 호출될 때 `runningTotal`을 사용할 수 있다.

> 참고: 최적화를 위해 Swift는 클로저가 값을 변경하지 않고, 클로저 생성 후 값이 변경되지 않는다면 값의 *복사본*을 캡처하고 저장할 수도 있다.
>
> 또한 Swift는 더 이상 필요하지 않은 변수를 처리할 때 관련된 모든 메모리 관리를 자동으로 처리한다.

다음은 `makeIncrementer`를 사용하는 예시다:

```swift
let incrementByTen = makeIncrementer(forIncrement: 10)
```

이 예시는 `incrementByTen`이라는 상수를 정의하며, 이 상수는 호출될 때마다 `runningTotal` 변수에 `10`을 더하는 증분기 함수를 참조한다. 이 함수를 여러 번 호출하면 다음과 같은 동작을 확인할 수 있다:

```swift
incrementByTen()
// 10을 반환
incrementByTen()
// 20을 반환
incrementByTen()
// 30을 반환
```

두 번째 증분기를 생성하면, 이 증분기는 새로운 `runningTotal` 변수에 대한 별도의 참조를 저장한다:

```swift
let incrementBySeven = makeIncrementer(forIncrement: 7)
incrementBySeven()
// 7을 반환
```

원래 증분기(`incrementByTen`)를 다시 호출하면, 이 증분기는 자신의 `runningTotal` 변수를 계속 증가시키며, `incrementBySeven`이 캡처한 변수에는 영향을 미치지 않는다:

```swift
incrementByTen()
// 40을 반환
```

> 참고: 클로저를 클래스 인스턴스의 프로퍼티에 할당하고, 클로저가 해당 인스턴스나 그 멤버를 참조하여 인스턴스를 캡처하면 클로저와 인스턴스 사이에 강한 참조 순환이 발생한다. Swift는 *캡처 리스트*를 사용해 이러한 강한 참조 순환을 끊는다. 더 자세한 내용은 <doc:AutomaticReferenceCounting#Strong-Reference-Cycles-for-Closures>를 참고한다.


## 클로저는 참조 타입이다

위 예제에서 `incrementBySeven`과 `incrementByTen`은 상수로 선언되었지만, 이 상수들이 참조하는 클로저는 여전히 캡처한 `runningTotal` 변수를 증가시킬 수 있다. 이는 함수와 클로저가 *참조 타입*이기 때문이다.

함수나 클로저를 상수나 변수에 할당할 때, 실제로는 해당 상수나 변수가 함수나 클로저를 *참조*하도록 설정하는 것이다. 위 예제에서 `incrementByTen`이 *참조하는* 클로저의 선택은 상수이지만, 클로저 자체의 내용은 상수가 아니다.

이는 또한 클로저를 두 개의 다른 상수나 변수에 할당하면, 두 상수나 변수 모두 동일한 클로저를 참조한다는 의미이기도 하다.

```swift
let alsoIncrementByTen = incrementByTen
alsoIncrementByTen()
// 50을 반환

incrementByTen()
// 60을 반환
```

<!--
  - test: `closures`

  ```swifttest
  -> let alsoIncrementByTen = incrementByTen
  >> let r5 =
  -> alsoIncrementByTen()
  /> returns a value of \(r5)
  </ returns a value of 50

  >> let r6 =
  -> incrementByTen()
  /> returns a value of \(r6)
  </ returns a value of 60
  ```
-->

위 예제는 `alsoIncrementByTen`을 호출하는 것이 `incrementByTen`을 호출하는 것과 동일함을 보여준다. 둘 다 동일한 클로저를 참조하기 때문에, 동일한 누적 합계를 증가시키고 반환한다.


## 탈출 클로저

클로저가 함수의 인자로 전달되지만, 함수가 반환된 후에 호출될 때 이를 *탈출*한다고 말한다. 클로저를 매개변수로 받는 함수를 선언할 때, 매개변수 타입 앞에 `@escaping`을 붙여 클로저가 탈출할 수 있음을 명시할 수 있다.

클로저가 탈출하는 한 가지 방법은 함수 외부에 정의된 변수에 저장되는 것이다. 예를 들어, 비동기 작업을 시작하는 많은 함수들은 완료 핸들러로 클로저를 인자로 받는다. 함수는 작업을 시작한 후 반환되지만, 클로저는 작업이 완료될 때까지 호출되지 않는다. 즉, 클로저는 나중에 호출되기 위해 탈출해야 한다. 예를 들어:

```swift
var completionHandlers: [() -> Void] = []
func someFunctionWithEscapingClosure(completionHandler: @escaping () -> Void) {
    completionHandlers.append(completionHandler)
}
```

`someFunctionWithEscapingClosure(_:)` 함수는 클로저를 인자로 받아 함수 외부에 선언된 배열에 추가한다. 만약 이 함수의 매개변수에 `@escaping`을 표시하지 않으면 컴파일 타임 오류가 발생한다.

`self`를 참조하는 탈출 클로저는 `self`가 클래스의 인스턴스를 가리킬 때 특별히 고려해야 한다. 탈출 클로저에서 `self`를 캡처하면 강한 참조 순환이 실수로 발생하기 쉽다. 참조 순환에 대한 자세한 내용은 <doc:AutomaticReferenceCounting>을 참고한다.

일반적으로 클로저는 본문에서 변수를 암시적으로 캡처하지만, 이 경우에는 명시적으로 처리해야 한다. `self`를 캡처하려면 사용할 때 `self`를 명시적으로 작성하거나 클로저의 캡처 목록에 `self`를 포함시킨다. `self`를 명시적으로 작성하면 의도를 명확히 표현할 수 있고, 참조 순환이 없는지 확인하도록 상기시켜 준다. 예를 들어, 아래 코드에서 `someFunctionWithEscapingClosure(_:)`에 전달된 클로저는 `self`를 명시적으로 참조한다. 반면, `someFunctionWithNonescapingClosure(_:)`에 전달된 클로저는 탈출하지 않는 클로저이므로 `self`를 암시적으로 참조할 수 있다.

```swift
func someFunctionWithNonescapingClosure(closure: () -> Void) {
    closure()
}

class SomeClass {
    var x = 10
    func doSomething() {
        someFunctionWithEscapingClosure { self.x = 100 }
        someFunctionWithNonescapingClosure { x = 200 }
    }
}

let instance = SomeClass()
instance.doSomething()
print(instance.x)
// "200" 출력

completionHandlers.first?()
print(instance.x)
// "100" 출력
```

다음은 클로저의 캡처 목록에 `self`를 포함시켜 `self`를 암시적으로 참조하는 `doSomething()`의 버전이다:

```swift
class SomeOtherClass {
    var x = 10
    func doSomething() {
        someFunctionWithEscapingClosure { [self] in x = 100 }
        someFunctionWithNonescapingClosure { x = 200 }
    }
}
```

`self`가 구조체나 열거형의 인스턴스라면 항상 `self`를 암시적으로 참조할 수 있다. 그러나 구조체나 열거형의 인스턴스인 `self`에 대한 변경 가능한 참조는 탈출 클로저에서 캡처할 수 없다. 구조체와 열거형은 공유 가능한 변경을 허용하지 않는다. 이에 대한 자세한 내용은 <doc:ClassesAndStructures#Structures-and-Enumerations-Are-Value-Types>에서 다룬다.

```swift
struct SomeStruct {
    var x = 10
    mutating func doSomething() {
        someFunctionWithNonescapingClosure { x = 200 }  // Ok
        someFunctionWithEscapingClosure { x = 100 }     // Error
    }
}
```

위 예제에서 `someFunctionWithEscapingClosure` 함수 호출은 오류를 발생시킨다. 이는 메서드가 변경 가능한 상태에 있기 때문에 `self`가 변경 가능하기 때문이다. 이는 구조체에 대해 탈출 클로저가 변경 가능한 `self` 참조를 캡처할 수 없다는 규칙을 위반한다.


## 자동 클로저(Autoclosures)

*자동 클로저*는 함수의 인자로 전달된 표현식을 자동으로 감싸는 클로저다. 이 클로저는 인자를 받지 않으며, 호출될 때 내부에 감싸진 표현식의 값을 반환한다. 이 문법적 편의 기능을 통해 명시적인 클로저 대신 일반 표현식을 사용해 함수의 매개변수 주변 중괄호를 생략할 수 있다.

자동 클로저를 받는 함수를 *호출*하는 경우는 많지만, 그런 함수를 *구현*하는 경우는 흔하지 않다. 예를 들어, `assert(condition:message:file:line:)` 함수는 `condition`과 `message` 매개변수로 자동 클로저를 받는다. 이때 `condition` 매개변수는 디버그 빌드에서만 평가되고, `message` 매개변수는 `condition`이 `false`일 때만 평가된다.

자동 클로저는 평가를 지연시킬 수 있다. 클로저 내부의 코드는 클로저가 호출되기 전까지 실행되지 않기 때문이다. 평가 지연은 부수 효과가 있거나 계산 비용이 높은 코드에 유용하다. 이 기능을 통해 코드가 언제 평가될지 제어할 수 있다. 아래 코드는 클로저가 어떻게 평가를 지연시키는지 보여준다.

```swift
var customersInLine = ["Chris", "Alex", "Ewa", "Barry", "Daniella"]
print(customersInLine.count)
// "5" 출력

let customerProvider = { customersInLine.remove(at: 0) }
print(customersInLine.count)
// "5" 출력

print("Now serving \(customerProvider())!")
// "Now serving Chris!" 출력
print(customersInLine.count)
// "4" 출력
```

<!--
  - test: `autoclosures`

  ```swifttest
  -> var customersInLine = ["Chris", "Alex", "Ewa", "Barry", "Daniella"]
  -> print(customersInLine.count)
  <- 5

  -> let customerProvider = { customersInLine.remove(at: 0) }
  -> print(customersInLine.count)
  <- 5

  -> print("Now serving \(customerProvider())!")
  <- Now serving Chris!
  -> print(customersInLine.count)
  <- 4
  ```
-->

`customersInLine` 배열의 첫 번째 요소는 클로저 내부의 코드에 의해 제거되지만, 실제로 클로저가 호출되기 전까지는 배열 요소가 제거되지 않는다. 만약 클로저가 호출되지 않으면, 클로저 내부의 표현식도 평가되지 않으며, 배열 요소도 제거되지 않는다. `customerProvider`의 타입은 `String`이 아니라 `() -> String`이다. 즉, 인자를 받지 않고 문자열을 반환하는 함수다.

클로저를 함수의 인자로 전달할 때도 동일한 평가 지연 동작을 얻을 수 있다.

```swift
// customersInLine은 ["Alex", "Ewa", "Barry", "Daniella"]
func serve(customer customerProvider: () -> String) {
    print("Now serving \(customerProvider())!")
}
serve(customer: { customersInLine.remove(at: 0) } )
// "Now serving Alex!" 출력
```

<!--
  - test: `autoclosures-function`

  ```swifttest
  >> var customersInLine = ["Alex", "Ewa", "Barry", "Daniella"]
  /> customersInLine is \(customersInLine)
  </ customersInLine is ["Alex", "Ewa", "Barry", "Daniella"]
  -> func serve(customer customerProvider: () -> String) {
         print("Now serving \(customerProvider())!")
     }
  -> serve(customer: { customersInLine.remove(at: 0) } )
  <- Now serving Alex!
  ```
-->

위 예제의 `serve(customer:)` 함수는 고객 이름을 반환하는 명시적 클로저를 받는다. 아래 버전의 `serve(customer:)` 함수는 동일한 작업을 수행하지만, 명시적 클로저 대신 `@autoclosure` 속성으로 매개변수 타입을 표시해 자동 클로저를 받는다. 이제 이 함수를 마치 `String` 인자를 받는 것처럼 호출할 수 있다. `customerProvider` 매개변수의 타입이 `@autoclosure` 속성으로 표시되어 있기 때문에, 인자가 자동으로 클로저로 변환된다.

```swift
// customersInLine은 ["Ewa", "Barry", "Daniella"]
func serve(customer customerProvider: @autoclosure () -> String) {
    print("Now serving \(customerProvider())!")
}
serve(customer: customersInLine.remove(at: 0))
// "Now serving Ewa!" 출력
```

<!--
  - test: `autoclosures-function-with-autoclosure`

  ```swifttest
  >> var customersInLine = ["Ewa", "Barry", "Daniella"]
  /> customersInLine is \(customersInLine)
  </ customersInLine is ["Ewa", "Barry", "Daniella"]
  -> func serve(customer customerProvider: @autoclosure () -> String) {
         print("Now serving \(customerProvider())!")
     }
  -> serve(customer: customersInLine.remove(at: 0))
  <- Now serving Ewa!
  ```
-->

> 참고: 자동 클로저를 과도하게 사용하면 코드를 이해하기 어려워질 수 있다. 평가가 지연된다는 사실이 함수 이름과 문맥을 통해 명확히 드러나야 한다.

자동 클로저가 탈출(escape)할 수 있도록 허용하려면, `@autoclosure`와 `@escaping` 속성을 함께 사용한다. `@escaping` 속성은 앞서 <doc:Closures#Escaping-Closures>에서 설명했다.

```swift
// customersInLine은 ["Barry", "Daniella"]
var customerProviders: [() -> String] = []
func collectCustomerProviders(_ customerProvider: @autoclosure @escaping () -> String) {
    customerProviders.append(customerProvider)
}
collectCustomerProviders(customersInLine.remove(at: 0))
collectCustomerProviders(customersInLine.remove(at: 0))

print("Collected \(customerProviders.count) closures.")
// "Collected 2 closures." 출력
for customerProvider in customerProviders {
    print("Now serving \(customerProvider())!")
}
// "Now serving Barry!" 출력
// "Now serving Daniella!" 출력
```

<!--
  - test: `autoclosures-function-with-escape`

  ```swifttest
  >> var customersInLine = ["Barry", "Daniella"]
  /> customersInLine is \(customersInLine)
  </ customersInLine is ["Barry", "Daniella"]
  -> var customerProviders: [() -> String] = []
  -> func collectCustomerProviders(_ customerProvider: @autoclosure @escaping () -> String) {
         customerProviders.append(customerProvider)
     }
  -> collectCustomerProviders(customersInLine.remove(at: 0))
  -> collectCustomerProviders(customersInLine.remove(at: 0))

  -> print("Collected \(customerProviders.count) closures.")
  <- Collected 2 closures.
  -> for customerProvider in customerProviders {
         print("Now serving \(customerProvider())!")
     }
  <- Now serving Barry!
  <- Now serving Daniella!
  ```
-->

위 코드에서 `collectCustomerProviders(_:)` 함수는 `customerProvider` 인자로 전달된 클로저를 호출하지 않고, `customerProviders` 배열에 추가한다. 이 배열은 함수의 범위 밖에서 선언되었으므로, 함수가 반환된 후에도 배열의 클로저를 실행할 수 있다. 따라서 `customerProvider` 인자의 값은 함수의 범위를 벗어날 수 있어야 한다.


