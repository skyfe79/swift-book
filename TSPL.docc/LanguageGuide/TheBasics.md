# 기본 개념

Swift는 일반적인 데이터 타입을 다루고 기본 문법을 작성하는 방법을 제공한다. Swift는 정수를 표현하는 `Int`, 부동소수점 값을 표현하는 `Double`, 불리언 값을 표현하는 `Bool`, 그리고 텍스트를 표현하는 `String`과 같은 기본 데이터 타입을 제공한다. 또한 Swift는 `Array`, `Set`, `Dictionary`라는 세 가지 주요 컬렉션 타입의 강력한 버전도 제공하며, 이에 대한 자세한 내용은 <doc:CollectionTypes>에서 확인할 수 있다.

Swift는 값을 저장하고 참조하기 위해 변수를 사용한다. 또한 Swift는 값이 변경되지 않는 변수를 광범위하게 활용한다. 이러한 변수를 상수라고 하며, 값이 변경될 필요가 없는 상황에서 코드를 더 안전하고 명확하게 만들기 위해 Swift 전반에 걸쳐 사용된다.

익숙한 타입 외에도 Swift는 튜플과 같은 고급 타입을 도입한다. 튜플을 사용하면 여러 값을 그룹화하여 생성하고 전달할 수 있다. 튜플을 활용하면 함수에서 여러 값을 하나의 복합 값으로 반환할 수 있다.

Swift는 또한 값이 없을 경우를 처리하기 위해 옵셔널 타입을 도입한다. 옵셔널은 "값이 *있고*, 그 값이 *x*다" 또는 "값이 *전혀 없다*"라는 두 가지 가능성을 표현한다.

Swift는 *타입 안전* 언어이다. 이는 언어가 코드가 다룰 수 있는 값의 타입을 명확히 하도록 도와준다는 의미이다. 코드의 일부가 `String`을 요구할 때, 타입 안전성은 실수로 `Int`를 전달하는 것을 방지한다. 마찬가지로, 타입 안전성은 옵셔널 `String`을 옵셔널이 아닌 `String`을 요구하는 코드에 실수로 전달하는 것을 막는다. 타입 안전성은 개발 과정에서 가능한 한 빨리 오류를 발견하고 수정할 수 있도록 도와준다.


## 상수와 변수

상수와 변수는 특정 타입의 값을 이름과 연결한다. 예를 들어 `maximumNumberOfLoginAttempts`나 `welcomeMessage` 같은 이름을 사용해 숫자 `10`이나 문자열 `"Hello"` 같은 값을 저장할 수 있다. **상수**는 한 번 설정한 값을 변경할 수 없지만, **변수**는 나중에 다른 값으로 변경할 수 있다.


### 상수와 변수 선언

상수와 변수는 사용하기 전에 반드시 선언해야 한다. 상수는 `let` 키워드로 선언하고, 변수는 `var` 키워드로 선언한다. 다음 예제는 사용자의 로그인 시도 횟수를 추적하기 위해 상수와 변수를 어떻게 사용하는지 보여준다.

```swift
let maximumNumberOfLoginAttempts = 10
var currentLoginAttempt = 0
```

<!--
  - test: `constantsAndVariables`

  ```swifttest
  -> let maximumNumberOfLoginAttempts = 10
  -> var currentLoginAttempt = 0
  ```
-->

이 코드는 다음과 같이 읽을 수 있다:

"`maximumNumberOfLoginAttempts`라는 새로운 상수를 선언하고, 값을 10으로 설정한다. 그리고 `currentLoginAttempt`라는 새로운 변수를 선언하고, 초기값을 0으로 설정한다."

이 예제에서 허용되는 최대 로그인 시도 횟수는 상수로 선언했다. 최대값은 절대 변하지 않기 때문이다. 반면 현재 로그인 시도 횟수는 변수로 선언했다. 로그인 시도가 실패할 때마다 이 값을 증가시켜야 하기 때문이다.

코드에서 저장된 값이 변하지 않는다면 항상 `let` 키워드를 사용해 상수로 선언한다. 변하는 값을 저장할 때만 변수를 사용한다.

상수나 변수를 선언할 때, 위의 예제처럼 선언과 동시에 값을 할당할 수 있다. 또는 프로그램에서 나중에 초기값을 할당할 수도 있다. 단, 값을 처음 읽기 전에 반드시 값이 할당되어 있어야 한다.

```swift
var environment = "development"
let maximumNumberOfLoginAttempts: Int
// maximumNumberOfLoginAttempts는 아직 값이 없다.

if environment == "development" {
    maximumNumberOfLoginAttempts = 100
} else {
    maximumNumberOfLoginAttempts = 10
}
// 이제 maximumNumberOfLoginAttempts는 값을 가지며, 읽을 수 있다.
```

<!--
  - test: `constantsWithDeferredInitialization`

  ```swifttest
  -> var environment = "development"
  -> let maximumNumberOfLoginAttempts: Int
  -> if environment == "development" {
         maximumNumberOfLoginAttempts = 100
     } else {
         maximumNumberOfLoginAttempts = 10
     }
  >> print(maxNumberOfLoginAttempts)
  << 100
  ```
-->

이 예제에서 최대 로그인 시도 횟수는 상수이며, 그 값은 환경에 따라 달라진다. 개발 환경에서는 값이 100이고, 다른 환경에서는 값이 10이다. `if` 문의 두 가지 경우 모두 `maximumNumberOfLoginAttempts`에 어떤 값을 할당하므로, 이 상수는 항상 값을 가지게 된다. 이런 방식으로 초기값을 설정할 때 Swift가 코드를 어떻게 검사하는지에 대한 자세한 내용은 <doc:Declarations#Constant-Declaration>을 참고한다.

한 줄에 여러 상수나 변수를 선언할 수도 있다. 각각을 쉼표로 구분하면 된다.

```swift
var x = 0.0, y = 0.0, z = 0.0
```

<!--
  - test: `multipleDeclarations`

  ```swifttest
  -> var x = 0.0, y = 0.0, z = 0.0
  >> print(x, y, z)
  << 0.0 0.0 0.0
  ```
-->


### 타입 어노테이션

상수나 변수를 선언할 때 *타입 어노테이션*을 제공해 해당 상수나 변수가 어떤 종류의 값을 저장할 수 있는지 명확히 할 수 있다. 타입 어노테이션은 상수나 변수 이름 뒤에 콜론을 붙이고, 공백을 둔 다음 사용할 타입 이름을 적어 작성한다.

이 예제는 `welcomeMessage`라는 변수에 타입 어노테이션을 제공해, 이 변수가 `String` 값을 저장할 수 있음을 나타낸다:

```swift
var welcomeMessage: String
```

<!--
  - test: `typeAnnotations`

  ```swifttest
  -> var welcomeMessage: String
  ```
-->

선언에서 콜론은 "...의 타입..."을 의미한다. 따라서 위 코드는 다음과 같이 읽을 수 있다:

"`welcomeMessage`라는 변수를 선언한다. 이 변수의 타입은 `String`이다."

"타입 `String`"이라는 구문은 "어떤 `String` 값이든 저장할 수 있다"는 뜻이다. 이를 "저장할 수 있는 것의 종류"로 생각하면 이해하기 쉽다.

이제 `welcomeMessage` 변수는 어떤 문자열 값이든 오류 없이 설정할 수 있다:

```swift
welcomeMessage = "Hello"
```

<!--
  - test: `typeAnnotations`

  ```swifttest
  -> welcomeMessage = "Hello"
  >> print(welcomeMessage)
  << Hello
  ```
-->

관련된 여러 변수를 한 줄에 정의할 때, 쉼표로 구분하고 마지막 변수 이름 뒤에 단일 타입 어노테이션을 작성할 수 있다:

```swift
var red, green, blue: Double
```

<!--
  - test: `typeAnnotations`

  ```swifttest
  -> var red, green, blue: Double
  ```
-->

> 참고: 실제로 타입 어노테이션을 작성할 일은 드물다. 상수나 변수를 정의할 때 초기값을 제공하면, Swift는 거의 항상 해당 상수나 변수의 타입을 추론할 수 있다. 이 내용은 <doc:TheBasics#Type-Safety-and-Type-Inference>에서 설명한다. 위의 `welcomeMessage` 예제에서는 초기값이 제공되지 않았기 때문에, `welcomeMessage` 변수의 타입은 초기값으로부터 추론되지 않고 타입 어노테이션으로 지정되었다.


### 상수와 변수 이름 짓기

상수와 변수 이름에는 유니코드 문자를 포함한 거의 모든 문자를 사용할 수 있다:

```swift
let π = 3.14159
let 你好 = "你好世界"
let 🐶🐮 = "dogcow"
```

<!--
  - test: `constantsAndVariables`

  ```swifttest
  -> let π = 3.14159
  -> let 你好 = "你好世界"
  -> let 🐶🐮 = "dogcow"
  ```
-->

하지만 상수와 변수 이름에는 공백 문자, 수학 기호, 화살표, 전용 유니코드 스칼라 값, 선 및 상자 그리기 문자를 포함할 수 없다. 또한 숫자로 시작할 수 없지만, 이름 중간에는 숫자를 포함할 수 있다.

한 번 특정 타입으로 선언한 상수나 변수는 같은 이름으로 다시 선언하거나 다른 타입의 값을 저장하도록 변경할 수 없다. 또한 상수를 변수로, 또는 변수를 상수로 바꿀 수도 없다.

> 주의: 상수나 변수 이름으로 Swift 예약어를 사용해야 한다면, 이름으로 사용할 때 백틱(`` ` ``)으로 예약어를 감싸야 한다. 하지만 가능하면 예약어를 이름으로 사용하지 않는 것이 좋다.

기존 변수의 값을 호환되는 타입의 다른 값으로 변경할 수 있다. 아래 예제에서 `friendlyWelcome`의 값은 `"Hello!"`에서 `"Bonjour!"`로 변경된다:

```swift
var friendlyWelcome = "Hello!"
friendlyWelcome = "Bonjour!"
// friendlyWelcome is now "Bonjour!"
```

<!--
  - test: `constantsAndVariables`

  ```swifttest
  -> var friendlyWelcome = "Hello!"
  -> friendlyWelcome = "Bonjour!"
  /> friendlyWelcome is now \"\(friendlyWelcome)\"
  </ friendlyWelcome is now "Bonjour!"
  ```
-->

변수와 달리 상수는 한 번 설정된 값을 변경할 수 없다. 이를 시도하면 코드를 컴파일할 때 오류가 발생한다:

```swift
let languageName = "Swift"
languageName = "Swift++"
// This is a compile-time error: languageName cannot be changed.
```

<!--
  - test: `constantsAndVariables_err`

  ```swifttest
  -> let languageName = "Swift"
  -> languageName = "Swift++"
  // This is a compile-time error: languageName cannot be changed.
  !$ error: cannot assign to value: 'languageName' is a 'let' constant
  !! languageName = "Swift++"
  !! ^~~~~~~~~~~~
  !! /tmp/swifttest.swift:1:1: note: change 'let' to 'var' to make it mutable
  !! let languageName = "Swift"
  !! ^~~
  !! var
  ```
-->


### 상수와 변수 출력하기

`print(_:separator:terminator:)` 함수를 사용하면 상수나 변수의 현재 값을 출력할 수 있다:

```swift
print(friendlyWelcome)
// Prints "Bonjour!"
```

<!--
  - test: `constantsAndVariables`

  ```swifttest
  -> print(friendlyWelcome)
  <- Bonjour!
  ```
-->

`print(_:separator:terminator:)` 함수는 하나 이상의 값을 적절한 출력 장치로 출력하는 전역 함수다. 예를 들어, Xcode에서는 이 함수가 출력 결과를 Xcode의 "콘솔" 창에 표시한다. `separator`와 `terminator` 매개변수는 기본값을 가지고 있으므로, 이 함수를 호출할 때 생략할 수 있다. 기본적으로 이 함수는 출력한 후 줄바꿈을 추가한다. 줄바꿈 없이 값을 출력하려면 `terminator`에 빈 문자열을 전달하면 된다. 예를 들어, `print(someValue, terminator: "")`와 같이 사용할 수 있다. 기본값이 있는 매개변수에 대한 자세한 내용은 <doc:Functions#Default-Parameter-Values>를 참고한다.

<!--
  - test: `printingWithoutNewline`

  ```swifttest
  >> let someValue = 10
  -> print(someValue, terminator: "")
  -> print(someValue)
  << 1010
  ```
-->

<!--
  QUESTION: have I referred to Xcode's console correctly here?
  Should I mention other output streams, such as the REPL / playgrounds?
-->

<!--
  NOTE: this is a deliberately simplistic description of what you can do with print().
  It will be expanded later on.
-->

Swift는 *문자열 보간법*을 사용해 상수나 변수의 이름을 더 긴 문자열 안에 플레이스홀더로 포함시키고, 이를 해당 상수나 변수의 현재 값으로 대체한다. 이름을 괄호로 감싸고, 여는 괄호 앞에 백슬래시를 붙이면 된다:

```swift
print("The current value of friendlyWelcome is \(friendlyWelcome)")
// Prints "The current value of friendlyWelcome is Bonjour!"
```

<!--
  - test: `constantsAndVariables`

  ```swifttest
  -> print("The current value of friendlyWelcome is \(friendlyWelcome)")
  <- The current value of friendlyWelcome is Bonjour!
  ```
-->

> 참고: 문자열 보간법과 함께 사용할 수 있는 모든 옵션은 <doc:StringsAndCharacters#String-Interpolation>에서 확인할 수 있다.


## 주석

주석은 코드에 실행되지 않는 텍스트를 포함하는 데 사용한다. 주로 메모나 나중에 참고할 내용을 적어둔다. Swift 컴파일러는 코드를 컴파일할 때 주석을 무시한다.

Swift의 주석은 C언어의 주석과 매우 유사하다. 한 줄 주석은 두 개의 슬래시(`//`)로 시작한다:

```swift
// 이것은 주석이다.
```

<!--
  - test: `comments`

  ```swifttest
  -> // This is a comment.
  ```
-->

여러 줄 주석은 슬래시와 별표(`/*`)로 시작하고, 별표와 슬래시(`*/`)로 끝난다:

```swift
/* 이것도 주석이지만
여러 줄에 걸쳐 작성되었다. */
```

<!--
  - test: `comments`

  ```swifttest
  -> /* This is also a comment
     but is written over multiple lines. */
  ```
-->

C언어의 여러 줄 주석과 달리, Swift에서는 여러 줄 주석 안에 다른 여러 줄 주석을 중첩할 수 있다. 중첩 주석을 작성하려면 첫 번째 여러 줄 주석 블록을 시작한 후, 그 안에 두 번째 여러 줄 주석을 시작한다. 두 번째 블록을 먼저 닫고, 그 다음 첫 번째 블록을 닫는다:

```swift
/* 이것은 첫 번째 여러 줄 주석의 시작이다.
    /* 이것은 중첩된 두 번째 여러 줄 주석이다. */
이것은 첫 번째 여러 줄 주석의 끝이다. */
```

<!--
  - test: `comments`

  ```swifttest
  -> /* This is the start of the first multiline comment.
        /* This is the second, nested multiline comment. */
     This is the end of the first multiline comment. */
  ```
-->

중첩된 여러 줄 주석을 사용하면, 이미 여러 줄 주석이 포함된 코드 블록도 쉽고 빠르게 주석 처리할 수 있다.


## 세미콜론

다른 많은 프로그래밍 언어와 달리, Swift에서는 각 문장 끝에 세미콜론(`;`)을 반드시 붙일 필요가 없다. 물론 원한다면 사용할 수는 있다. 하지만 한 줄에 여러 개의 독립된 문장을 작성할 때는 세미콜론이 *필수적*이다:

```swift
let cat = "🐱"; print(cat)
// "🐱"를 출력
```

<!--
  - test: `semiColons`

  ```swifttest
  -> let cat = "🐱"; print(cat)
  <- 🐱
  ```
-->


## 정수

*정수*는 소수 부분이 없는 전체 숫자다. 예를 들어 `42`와 `-23`이 여기에 해당한다. 정수는 *부호 있는* (양수, 0, 음수) 또는 *부호 없는* (양수, 0) 두 가지 형태로 나뉜다.

Swift는 8비트, 16비트, 32비트, 64비트 형태의 부호 있는 정수와 부호 없는 정수를 제공한다. 이러한 정수는 C 언어와 유사한 네이밍 규칙을 따른다. 예를 들어 8비트 부호 없는 정수는 `UInt8` 타입이고, 32비트 부호 있는 정수는 `Int32` 타입이다. Swift의 모든 타입과 마찬가지로, 이러한 정수 타입도 대문자로 시작하는 이름을 가진다.


### 정수 타입의 범위

각 정수 타입의 최솟값과 최댓값은 `min`과 `max` 프로퍼티를 통해 확인할 수 있다:

```swift
let minValue = UInt8.min  // minValue는 0이고, 타입은 UInt8이다
let maxValue = UInt8.max  // maxValue는 255이고, 타입은 UInt8이다
```

<!--
  - test: `integerBounds`

  ```swifttest
  -> let minValue = UInt8.min  // minValue is equal to 0, and is of type UInt8
  -> let maxValue = UInt8.max  // maxValue is equal to 255, and is of type UInt8
  >> print(minValue, maxValue)
  << 0 255
  ```
-->

이 프로퍼티의 값은 해당 크기의 숫자 타입(예: 위 예제의 `UInt8`)으로 반환되므로, 같은 타입의 다른 값과 함께 표현식에서 사용할 수 있다.


대부분의 경우, 코드에서 사용할 정수의 크기를 특별히 지정할 필요가 없다.  
Swift는 추가적인 정수 타입인 `Int`를 제공하며, 이는 현재 플랫폼의 기본 워드 크기와 동일한 크기를 가진다:

- 32비트 플랫폼에서는 `Int`가 `Int32`와 같은 크기다.  
- 64비트 플랫폼에서는 `Int`가 `Int64`와 같은 크기다.  

특정 크기의 정수를 다뤄야 할 필요가 없다면, 코드에서 정수 값을 다룰 때 항상 `Int`를 사용한다.  
이렇게 하면 코드의 일관성과 상호 운용성을 높일 수 있다.  
32비트 플랫폼에서도 `Int`는 `-2,147,483,648`부터 `2,147,483,647`까지의 값을 저장할 수 있으며, 많은 정수 범위를 충분히 커버한다.


### UInt 타입

Swift는 현재 플랫폼의 기본 워드 크기와 동일한 크기를 가진 부호 없는 정수 타입인 `UInt`를 제공한다:

- 32비트 플랫폼에서 `UInt`는 `UInt32`와 동일한 크기를 가진다.
- 64비트 플랫폼에서 `UInt`는 `UInt64`와 동일한 크기를 가진다.

> 참고: `UInt`는 플랫폼의 기본 워드 크기와 동일한 크기의 부호 없는 정수 타입이 필요한 경우에만 사용한다. 그렇지 않은 경우, 저장할 값이 음수가 아니라는 것이 확실하더라도 `Int`를 사용하는 것이 좋다. 정수 값에 대해 일관되게 `Int`를 사용하면 코드의 상호 운용성을 높이고, 다른 숫자 타입 간의 변환을 피할 수 있으며, <doc:TheBasics#Type-Safety-and-Type-Inference>에서 설명한 것처럼 정수 타입 추론과도 일치한다.


## 부동소수점 숫자

*부동소수점 숫자*는 소수 부분을 포함하는 숫자를 말한다. 예를 들어 `3.14159`, `0.1`, `-273.15` 등이 이에 해당한다.

부동소수점 타입은 정수 타입보다 훨씬 넓은 범위의 값을 표현할 수 있으며, `Int`에 저장할 수 있는 숫자보다 훨씬 크거나 작은 값을 저장할 수 있다. Swift는 두 가지 부동소수점 숫자 타입을 제공한다:

- `Double`은 64비트 부동소수점 숫자를 나타낸다.
- `Float`은 32비트 부동소수점 숫자를 나타낸다.

> 참고: `Double`은 최소 15자리의 소수점 정밀도를 가지지만, `Float`은 최소 6자리의 정밀도를 가질 수 있다. 코드에서 다뤄야 할 값의 특성과 범위에 따라 적절한 부동소수점 타입을 선택해야 한다. 두 타입 모두 적합한 상황에서는 `Double`을 사용하는 것이 일반적이다.

<!--
  TODO: Float이 적합한 상황을 명시적으로 언급할 필요가 있음,
  예를 들어 컬렉션의 저장 공간을 최적화해야 할 때 등
-->

<!--
  TODO: 무한대, 음의 무한대 등에 대해 언급할 필요가 있음
-->


## 타입 안전성과 타입 추론

Swift는 *타입 안전성*을 갖춘 언어이다. 타입 안전한 언어는 코드가 다룰 수 있는 값의 타입을 명확히 하는 것을 권장한다. 예를 들어, 코드의 일부에서 `String` 타입이 필요한 경우, 실수로 `Int` 타입을 전달할 수 없다.

Swift는 타입 안전성을 갖추고 있기 때문에, 코드를 컴파일할 때 *타입 검사*를 수행하고 일치하지 않는 타입을 오류로 표시한다. 이를 통해 개발 과정에서 가능한 한 빨리 오류를 발견하고 수정할 수 있다.

타입 검사는 서로 다른 타입의 값을 다룰 때 오류를 방지하는 데 도움을 준다. 그러나 모든 상수와 변수의 타입을 일일이 지정할 필요는 없다. 만약 필요한 값의 타입을 지정하지 않으면, Swift는 *타입 추론*을 통해 적절한 타입을 알아낸다. 타입 추론은 컴파일러가 코드를 컴파일할 때 제공된 값을 단순히 검토하여 특정 표현식의 타입을 자동으로 추론할 수 있게 한다.

타입 추론 덕분에 Swift는 C나 Objective-C 같은 언어보다 훨씬 적은 타입 선언을 요구한다. 상수와 변수는 여전히 명시적으로 타입이 지정되지만, 타입을 지정하는 대부분의 작업은 Swift가 대신 처리한다.

타입 추론은 초기값을 가진 상수나 변수를 선언할 때 특히 유용하다. 이는 종종 상수나 변수를 선언할 때 *리터럴 값*을 할당함으로써 이루어진다. (리터럴 값은 소스 코드에 직접 나타나는 값으로, 아래 예제의 `42`와 `3.14159`와 같은 값이다.)

예를 들어, 새로운 상수에 `42`라는 리터럴 값을 할당하면서 타입을 지정하지 않으면, Swift는 해당 상수가 `Int` 타입이 되길 원한다고 추론한다. 이는 정수처럼 보이는 숫자로 초기화했기 때문이다:

```swift
let meaningOfLife = 42
// meaningOfLife는 Int 타입으로 추론된다
```

<!--
  - test: `typeInference`

  ```swifttest
  -> let meaningOfLife = 42
  // meaningOfLife는 Int 타입으로 추론된다
  >> print(type(of: meaningOfLife))
  << Int
  ```
-->

마찬가지로, 부동소수점 리터럴의 타입을 지정하지 않으면, Swift는 `Double` 타입을 생성하려 한다고 추론한다:

```swift
let pi = 3.14159
// pi는 Double 타입으로 추론된다
```

<!--
  - test: `typeInference`

  ```swifttest
  -> let pi = 3.14159
  // pi는 Double 타입으로 추론된다
  >> print(type(of: pi))
  << Double
  ```
-->

Swift는 부동소수점 숫자의 타입을 추론할 때 항상 `Double`을 선택한다 (`Float`가 아니다).

정수와 부동소수점 리터럴을 표현식에서 결합하면, `Double` 타입이 문맥으로부터 추론된다:

```swift
let anotherPi = 3 + 0.14159
// anotherPi 역시 Double 타입으로 추론된다
```

<!--
  - test: `typeInference`

  ```swifttest
  -> let anotherPi = 3 + 0.14159
  // anotherPi 역시 Double 타입으로 추론된다
  >> print(type(of: anotherPi))
  << Double
  ```
-->

`3`이라는 리터럴 값은 그 자체로 명시적인 타입이 없으며, 따라서 덧셈의 일부로 부동소수점 리터럴이 존재함에 따라 적절한 출력 타입인 `Double`이 추론된다.


## 숫자 리터럴

정수 리터럴은 다음과 같은 방식으로 작성할 수 있다:

- 접두사 없이 *10진수*로 표현
- `0b` 접두사를 사용한 *2진수*로 표현
- `0o` 접두사를 사용한 *8진수*로 표현
- `0x` 접두사를 사용한 *16진수*로 표현

다음 정수 리터럴은 모두 10진수 값 `17`을 나타낸다:

```swift
let decimalInteger = 17
let binaryInteger = 0b10001       // 2진수 표기법으로 17
let octalInteger = 0o21           // 8진수 표기법으로 17
let hexadecimalInteger = 0x11     // 16진수 표기법으로 17
```

<!--
  - test: `numberLiterals`

  ```swifttest
  -> let decimalInteger = 17
  -> let binaryInteger = 0b10001       // 17 in binary notation
  -> let octalInteger = 0o21           // 17 in octal notation
  -> let hexadecimalInteger = 0x11     // 17 in hexadecimal notation
  >> print(binaryInteger, octalInteger, hexadecimalInteger)
  << 17 17 17
  ```
-->

부동소수점 리터럴은 접두사 없이 10진수로 표현하거나, `0x` 접두사를 사용해 16진수로 표현할 수 있다. 부동소수점 리터럴은 소수점 양쪽에 반드시 숫자(또는 16진수)가 있어야 한다. 10진수 부동소수점은 선택적으로 *지수*를 포함할 수 있으며, 이는 대문자 또는 소문자 `e`로 표시한다. 16진수 부동소수점은 반드시 지수를 포함해야 하며, 이는 대문자 또는 소문자 `p`로 표시한다.

<!--
  - test: `float-required-vs-optional-exponent-err`

  ```swifttest
  -> let hexWithout = 0x1.5
  !$ error: hexadecimal floating point literal must end with an exponent
  !! let hexWithout = 0x1.5
  !!                       ^
  ```
-->

<!--
  - test: `float-required-vs-optional-exponent`

  ```swifttest
  -> let hexWith = 0x1.5p7
  -> let decimalWithout = 0.5
  -> let decimalWith = 0.5e7
  ```
-->

10진수에서 지수가 `x`인 경우, 기본 숫자에 10ˣ을 곱한다:

- `1.25e2`는 1.25 x 10², 즉 `125.0`을 의미한다.
- `1.25e-2`는 1.25 x 10⁻², 즉 `0.0125`를 의미한다.

16진수에서 지수가 `x`인 경우, 기본 숫자에 2ˣ을 곱한다:

- `0xFp2`는 15 x 2², 즉 `60.0`을 의미한다.
- `0xFp-2`는 15 x 2⁻², 즉 `3.75`를 의미한다.

다음 부동소수점 리터럴은 모두 10진수 값 `12.1875`를 나타낸다:

```swift
let decimalDouble = 12.1875
let exponentDouble = 1.21875e1
let hexadecimalDouble = 0xC.3p0
```

<!--
  - test: `numberLiterals`

  ```swifttest
  -> let decimalDouble = 12.1875
  -> let exponentDouble = 1.21875e1
  -> let hexadecimalDouble = 0xC.3p0
  ```
-->

숫자 리터럴은 가독성을 높이기 위해 추가적인 서식을 포함할 수 있다. 정수와 부동소수점 모두 추가적인 0으로 채우거나, 가독성을 높이기 위해 언더스코어(`_`)를 포함할 수 있다. 이러한 서식은 리터럴의 실제 값에 영향을 미치지 않는다:

```swift
let paddedDouble = 000123.456
let oneMillion = 1_000_000
let justOverOneMillion = 1_000_000.000_000_1
```

<!--
  - test: `numberLiterals`

  ```swifttest
  -> let paddedDouble = 000123.456
  -> let oneMillion = 1_000_000
  -> let justOverOneMillion = 1_000_000.000_000_1
  ```
-->


## 숫자 타입 변환

코드에서 일반적인 정수 상수와 변수에는 `Int` 타입을 사용한다. 값이 음수가 아니라는 것을 알고 있더라도 이 원칙을 지킨다. 일상적인 상황에서 기본 정수 타입을 사용하면, 정수 상수와 변수가 코드 내에서 즉시 호환되며 정수 리터럴 값의 추론된 타입과 일치한다.

다른 정수 타입은 특정 작업에 명시적으로 필요한 경우에만 사용한다. 외부 소스에서 명시적으로 크기가 지정된 데이터를 다루거나, 성능, 메모리 사용량, 기타 필요한 최적화를 위해 사용한다. 이러한 상황에서 명시적으로 크기가 지정된 타입을 사용하면, 의도치 않은 값 오버플로를 방지하고 사용 중인 데이터의 특성을 암묵적으로 문서화하는 데 도움이 된다.


### 정수 타입 변환

각 정수 타입은 저장할 수 있는 숫자의 범위가 다르다. `Int8` 타입의 상수나 변수는 `-128`부터 `127`까지의 숫자를 저장할 수 있고, `UInt8` 타입은 `0`부터 `255`까지의 숫자를 저장할 수 있다. 만약 특정 정수 타입의 범위를 벗어나는 숫자를 저장하려고 하면, 코드를 컴파일할 때 오류가 발생한다:

```swift
let cannotBeNegative: UInt8 = -1
// UInt8은 음수를 저장할 수 없으므로 오류가 발생한다
let tooBig: Int8 = Int8.max + 1
// Int8은 최댓값보다 큰 숫자를 저장할 수 없으므로 이 역시 오류가 발생한다
```

<!--
  - test: `constantsAndVariablesOverflowError`

  ```swifttest
  -> let cannotBeNegative: UInt8 = -1
  // UInt8 can't store negative numbers, and so this will report an error
  -> let tooBig: Int8 = Int8.max + 1
  // Int8 can't store a number larger than its maximum value,
  // and so this will also report an error
  !! /tmp/swifttest.swift:2:29: error: arithmetic operation '127 + 1' (on type 'Int8') results in an overflow
  !! let tooBig: Int8 = Int8.max + 1
  !!                    ~~~~~~~~ ^ ~
  !! /tmp/swifttest.swift:1:31: error: negative integer '-1' overflows when stored into unsigned type 'UInt8'
  !! let cannotBeNegative: UInt8 = -1
  !!                                ^
  ```
-->

각 숫자 타입이 저장할 수 있는 값의 범위가 다르기 때문에, 숫자 타입 변환은 필요할 때마다 명시적으로 선택해야 한다. 이렇게 선택적으로 변환하는 방식은 숨겨진 변환 오류를 방지하고, 코드에서 타입 변환 의도를 명확하게 표현하는 데 도움이 된다.

특정 숫자 타입을 다른 타입으로 변환하려면, 기존 값을 사용해 원하는 타입의 새로운 숫자를 초기화하면 된다. 아래 예제에서 상수 `twoThousand`는 `UInt16` 타입이고, 상수 `one`은 `UInt8` 타입이다. 두 값은 타입이 다르기 때문에 직접 더할 수 없다. 대신, 이 예제에서는 `UInt16(one)`을 호출해 `one`의 값으로 초기화된 새로운 `UInt16`을 생성하고, 이 값을 원래 값 대신 사용한다:

```swift
let twoThousand: UInt16 = 2_000
let one: UInt8 = 1
let twoThousandAndOne = twoThousand + UInt16(one)
```

<!--
  - test: `typeConversion`

  ```swifttest
  -> let twoThousand: UInt16 = 2_000
  -> let one: UInt8 = 1
  -> let twoThousandAndOne = twoThousand + UInt16(one)
  >> print(twoThousandAndOne)
  << 2001
  ```
-->

이제 더하기 연산의 양쪽 모두 `UInt16` 타입이 되었기 때문에, 연산이 허용된다. 결과 상수 `twoThousandAndOne`은 두 `UInt16` 값의 합이므로 `UInt16` 타입으로 추론된다.

`SomeType(ofInitialValue)`는 Swift 타입의 초기화 메서드를 호출하고 초기값을 전달하는 기본적인 방법이다. 내부적으로 `UInt16`은 `UInt8` 값을 받아들이는 초기화 메서드를 가지고 있기 때문에, 이 메서드를 사용해 기존 `UInt8` 값으로부터 새로운 `UInt16`을 만들 수 있다. 하지만 여기서 *어떤* 타입이든 전달할 수 있는 것은 아니다. `UInt16`이 초기화 메서드를 제공하는 타입만 가능하다. 기존 타입을 확장해 새로운 타입(자신이 정의한 타입 포함)을 받아들이는 초기화 메서드를 제공하는 방법은 <doc:Extensions>에서 다룬다.


### 정수와 부동소수점 변환

정수와 부동소수점 숫자 타입 간의 변환은 명시적으로 이루어져야 한다:

```swift
let three = 3
let pointOneFourOneFiveNine = 0.14159
let pi = Double(three) + pointOneFourOneFiveNine
// pi는 3.14159이며, Double 타입으로 추론된다
```

<!--
  - test: `typeConversion`

  ```swifttest
  -> let three = 3
  -> let pointOneFourOneFiveNine = 0.14159
  -> let pi = Double(three) + pointOneFourOneFiveNine
  /> pi equals \(pi), and is inferred to be of type Double
  </ pi equals 3.14159, and is inferred to be of type Double
  ```
-->

여기서 상수 `three`의 값을 사용해 `Double` 타입의 새로운 값을 생성한다. 이렇게 하면 덧셈의 양쪽이 동일한 타입을 갖게 된다. 이 변환이 없다면 덧셈이 허용되지 않는다.

부동소수점에서 정수로의 변환도 명시적으로 이루어져야 한다. 정수 타입은 `Double`이나 `Float` 값으로 초기화할 수 있다:

```swift
let integerPi = Int(pi)
// integerPi는 3이며, Int 타입으로 추론된다
```

<!--
  - test: `typeConversion`

  ```swifttest
  -> let integerPi = Int(pi)
  /> integerPi equals \(integerPi), and is inferred to be of type Int
  </ integerPi equals 3, and is inferred to be of type Int
  ```
-->

이 방식으로 새로운 정수 값을 초기화할 때 부동소수점 값은 항상 잘린다. 즉, `4.75`는 `4`가 되고, `-3.9`는 `-3`이 된다.

> 참고: 숫자 상수와 변수를 결합하는 규칙은 숫자 리터럴의 규칙과 다르다. 리터럴 값 `3`은 리터럴 값 `0.14159`에 직접 더할 수 있다. 숫자 리터럴은 그 자체로 명시적인 타입을 갖지 않기 때문이다. 리터럴의 타입은 컴파일러가 평가하는 시점에만 추론된다.

<!--
  NOTE: this section on explicit conversions could be included in the Operators section.
  I think it's more appropriate here, however,
  and helps to reinforce the “just use Int” message.
-->


## 타입 별칭

*타입 별칭*은 기존 타입에 대한 대체 이름을 정의한다. `typealias` 키워드를 사용해 타입 별칭을 정의할 수 있다.

타입 별칭은 특정 문맥에서 더 적절한 이름으로 기존 타입을 참조하고 싶을 때 유용하다. 예를 들어 외부 소스에서 특정 크기의 데이터를 다룰 때 다음과 같이 사용할 수 있다:

```swift
typealias AudioSample = UInt16
```

<!--
  - test: `typeAliases`

  ```swifttest
  -> typealias AudioSample = UInt16
  ```
-->

타입 별칭을 정의하면 원래 타입 이름을 사용할 수 있는 모든 곳에서 별칭을 사용할 수 있다:

```swift
var maxAmplitudeFound = AudioSample.min
// maxAmplitudeFound는 이제 0이다
```

<!--
  - test: `typeAliases`

  ```swifttest
  -> var maxAmplitudeFound = AudioSample.min
  /> maxAmplitudeFound is now \(maxAmplitudeFound)
  </ maxAmplitudeFound is now 0
  ```
-->

여기서 `AudioSample`은 `UInt16`의 별칭으로 정의된다. 별칭이기 때문에 `AudioSample.min`을 호출하면 실제로는 `UInt16.min`이 호출되며, 이는 `maxAmplitudeFound` 변수에 초기값 `0`을 제공한다.


## 불리언

Swift는 기본적인 *불리언* 타입인 `Bool`을 제공한다. 불리언 값은 *논리적* 값으로 간주되며, 오직 참(true) 또는 거짓(false)만 가질 수 있다. Swift는 두 가지 불리언 상수 값인 `true`와 `false`를 제공한다:

```swift
let orangesAreOrange = true
let turnipsAreDelicious = false
```

<!--
  - test: `booleans`

  ```swifttest
  -> let orangesAreOrange = true
  -> let turnipsAreDelicious = false
  ```
-->

`orangesAreOrange`와 `turnipsAreDelicious`의 타입은 불리언 리터럴 값으로 초기화되었기 때문에 `Bool`로 추론된다. 앞서 살펴본 `Int`와 `Double`과 마찬가지로, 상수나 변수를 생성할 때 `true`나 `false`로 설정하면 `Bool` 타입을 명시적으로 선언할 필요가 없다. 타입 추론은 이미 타입이 알려진 값으로 상수나 변수를 초기화할 때 Swift 코드를 더 간결하고 가독성 있게 만드는 데 도움을 준다.

불리언 값은 특히 `if` 문과 같은 조건문을 다룰 때 유용하다:

```swift
if turnipsAreDelicious {
    print("Mmm, tasty turnips!")
} else {
    print("Eww, turnips are horrible.")
}
// Prints "Eww, turnips are horrible."
```

<!--
  - test: `booleans`

  ```swifttest
  -> if turnipsAreDelicious {
        print("Mmm, tasty turnips!")
     } else {
        print("Eww, turnips are horrible.")
     }
  <- Eww, turnips are horrible.
  ```
-->

`if` 문과 같은 조건문은 <doc:ControlFlow>에서 더 자세히 다룬다.

Swift의 타입 안전성은 불리언이 아닌 값이 `Bool` 대신 사용되는 것을 방지한다. 다음 예제는 컴파일 타임 오류를 발생시킨다:

```swift
let i = 1
if i {
    // 이 예제는 컴파일되지 않으며 오류를 보고한다
}
```

<!--
  - test: `booleansNotBoolean`

  ```swifttest
  -> let i = 1
  -> if i {
        // 이 예제는 컴파일되지 않으며 오류를 보고한다
     }
  !$ error: type 'Int' cannot be used as a boolean; test for '!= 0' instead
  !! if i {
  !!   ^
  !! ( != 0)
  ```
-->

하지만 아래의 대체 예제는 유효하다:

```swift
let i = 1
if i == 1 {
    // 이 예제는 성공적으로 컴파일된다
}
```

<!--
  - test: `booleansIsBoolean`

  ```swifttest
  -> let i = 1
  -> if i == 1 {
        // 이 예제는 성공적으로 컴파일된다
     }
  ```
-->

`i == 1` 비교의 결과는 `Bool` 타입이므로, 이 두 번째 예제는 타입 검사를 통과한다. `i == 1`과 같은 비교 연산자는 <doc:BasicOperators>에서 다룬다.

Swift의 타입 안전성에 대한 다른 예제와 마찬가지로, 이 접근 방식은 실수로 인한 오류를 방지하고 특정 코드 섹션의 의도를 항상 명확하게 만드는 데 도움을 준다.


## 튜플

*튜플*은 여러 값을 하나의 복합 값으로 묶는다. 튜플 내의 값은 어떤 타입이든 가능하며, 서로 다른 타입을 포함할 수 있다.

이 예제에서 `(404, "Not Found")`는 *HTTP 상태 코드*를 설명하는 튜플이다. HTTP 상태 코드는 웹 페이지를 요청할 때 웹 서버가 반환하는 특별한 값이다. 존재하지 않는 웹 페이지를 요청하면 `404 Not Found` 상태 코드가 반환된다.

```swift
let http404Error = (404, "Not Found")
// http404Error는 (Int, String) 타입이며, 값은 (404, "Not Found")이다.
```

`(404, "Not Found")` 튜플은 `Int`와 `String`을 묶어 HTTP 상태 코드를 숫자와 사람이 읽을 수 있는 설명으로 표현한다. 이를 "`(Int, String)` 타입의 튜플"이라고 설명할 수 있다.

어떤 타입 조합으로든 튜플을 생성할 수 있으며, 원하는 만큼 다양한 타입을 포함할 수 있다. 예를 들어 `(Int, Int, Int)`나 `(String, Bool)`과 같은 튜플을 만들 수 있다.

튜플의 내용을 분해하여 별도의 상수나 변수로 할당할 수 있다. 이후에는 일반적으로 접근하는 것처럼 사용할 수 있다.

```swift
let (statusCode, statusMessage) = http404Error
print("The status code is \(statusCode)")
// "The status code is 404" 출력
print("The status message is \(statusMessage)")
// "The status message is Not Found" 출력
```

튜플의 일부 값만 필요하다면, 튜플을 분해할 때 언더스코어(`_`)를 사용해 무시할 수 있다.

```swift
let (justTheStatusCode, _) = http404Error
print("The status code is \(justTheStatusCode)")
// "The status code is 404" 출력
```

또는, 튜플의 각 요소에 인덱스 번호를 사용해 접근할 수 있다. 인덱스는 0부터 시작한다.

```swift
print("The status code is \(http404Error.0)")
// "The status code is 404" 출력
print("The status message is \(http404Error.1)")
// "The status message is Not Found" 출력
```

튜플을 정의할 때 각 요소에 이름을 붙일 수 있다.

```swift
let http200Status = (statusCode: 200, description: "OK")
```

튜플의 요소에 이름을 붙였다면, 그 이름을 사용해 요소의 값에 접근할 수 있다.

```swift
print("The status code is \(http200Status.statusCode)")
// "The status code is 200" 출력
print("The status message is \(http200Status.description)")
// "The status message is OK" 출력
```

튜플은 함수의 반환 값으로 특히 유용하다. 웹 페이지를 가져오려는 함수는 페이지 가져오기의 성공 여부를 설명하기 위해 `(Int, String)` 튜플 타입을 반환할 수 있다. 두 개의 서로 다른 값을 반환함으로써, 단일 타입의 단일 값만 반환하는 것보다 더 유용한 정보를 제공한다. 자세한 내용은 <doc:Functions#Functions-with-Multiple-Return-Values>를 참고한다.

> 참고: 튜플은 간단한 관련 값 그룹에 유용하다. 복잡한 데이터 구조를 생성하는 데는 적합하지 않다. 데이터 구조가 복잡해질 가능성이 있다면, 튜플 대신 클래스나 구조체로 모델링하는 것이 좋다. 자세한 내용은 <doc:ClassesAndStructures>를 참고한다.


## 옵셔널

값이 존재하지 않을 수 있는 상황에서 **옵셔널**을 사용한다. 옵셔널은 두 가지 가능성을 나타낸다: 특정 타입의 값이 존재할 수도 있고, 옵셔널을 언래핑해 그 값에 접근할 수 있다. 또는 값이 전혀 없을 수도 있다.

값이 없을 수 있는 예로, Swift의 `Int` 타입은 `String` 값을 `Int` 값으로 변환하려고 시도하는 초기화 메서드를 제공한다. 하지만 모든 문자열이 정수로 변환될 수는 없다. 문자열 `"123"`은 숫자 값 `123`으로 변환할 수 있지만, `"hello, world"` 같은 문자열은 대응하는 숫자 값이 없다. 아래 예제는 초기화 메서드를 사용해 `String`을 `Int`로 변환하려고 시도한다:

```swift
let possibleNumber = "123"
let convertedNumber = Int(possibleNumber)
// convertedNumber의 타입은 "옵셔널 Int"이다
```

<!--
  - test: `optionals`

  ```swifttest
  -> let possibleNumber = "123"
  -> let convertedNumber = Int(possibleNumber)
  // convertedNumber는 "Int?" 또는 "옵셔널 Int" 타입으로 추론된다
  >> print(type(of: convertedNumber))
  << Optional<Int>
  ```
-->

위 코드의 초기화 메서드는 실패할 가능성이 있기 때문에, `Int` 대신 **옵셔널** `Int`를 반환한다.

옵셔널 타입을 작성하려면, 옵셔널이 포함할 타입 이름 뒤에 물음표(`?`)를 붙인다. 예를 들어, 옵셔널 `Int`의 타입은 `Int?`이다. 옵셔널 `Int`는 항상 어떤 `Int` 값이거나 값이 없다. `Bool`이나 `String` 같은 다른 타입의 값을 포함할 수 없다.


### nil

옵셔널 변수에 특별한 값 `nil`을 할당하면 값이 없는 상태로 설정할 수 있다:

```swift
var serverResponseCode: Int? = 404
// serverResponseCode는 실제 Int 값 404를 포함함
serverResponseCode = nil
// 이제 serverResponseCode는 값을 포함하지 않음
```

<!--
  - test: `optionals`

  ```swifttest
  -> var serverResponseCode: Int? = 404
  /> serverResponseCode contains an actual Int value of \(serverResponseCode!)
  </ serverResponseCode contains an actual Int value of 404
  -> serverResponseCode = nil
  // serverResponseCode now contains no value
  ```
-->

옵셔널 변수를 정의할 때 기본값을 제공하지 않으면, 변수는 자동으로 `nil`로 설정된다:

```swift
var surveyAnswer: String?
// surveyAnswer는 자동으로 nil로 설정됨
```

<!--
  - test: `optionals`

  ```swifttest
  -> var surveyAnswer: String?
  // surveyAnswer is automatically set to nil
  ```
-->

`if` 문을 사용해 옵셔널이 값을 포함하는지 확인할 수 있다. 이때 옵셔널을 `nil`과 비교한다. 비교는 "같음" 연산자(`==`)나 "같지 않음" 연산자(`!=`)를 사용해 수행한다.

옵셔널이 값을 가지고 있다면, `nil`과 "같지 않음"으로 간주된다:

```swift
let possibleNumber = "123"
let convertedNumber = Int(possibleNumber)

if convertedNumber != nil {
    print("convertedNumber contains some integer value.")
}
// "convertedNumber contains some integer value." 출력
```

<!--
  - test: `optionals`

  ```swifttest
  -> if convertedNumber != nil {
        print("convertedNumber contains some integer value.")
     }
  <- convertedNumber contains some integer value.
  ```
-->

`nil`은 옵셔널이 아닌 상수나 변수와 함께 사용할 수 없다. 코드에서 특정 조건에서 값이 없을 가능성이 있는 상수나 변수를 다루려면, 적절한 타입의 옵셔널 값으로 선언해야 한다. 옵셔널이 아닌 값으로 선언된 상수나 변수는 절대 `nil` 값을 포함하지 않는다. `nil`을 옵셔널이 아닌 값에 할당하려고 하면 컴파일 시 오류가 발생한다.

옵셔널과 옵셔널이 아닌 값을 구분함으로써, 어떤 정보가 누락될 수 있는지 명시적으로 표시할 수 있고, 누락된 값을 처리하는 코드를 더 쉽게 작성할 수 있다. 옵셔널을 옵셔널이 아닌 것처럼 실수로 처리할 수 없는데, 이는 컴파일 시 오류를 발생시키기 때문이다. 값을 언래핑한 후에는 해당 값을 다루는 다른 코드에서 `nil`을 확인할 필요가 없으므로, 코드의 여러 부분에서 동일한 값을 반복적으로 확인할 필요가 없다.

옵셔널 값에 접근할 때, 코드는 항상 `nil`인 경우와 아닌 경우를 모두 처리해야 한다. 값이 누락된 경우 다음과 같은 여러 가지 방법으로 처리할 수 있으며, 이는 다음 섹션에서 설명한다:

- 값이 `nil`일 때 해당 값을 다루는 코드를 건너뛴다.

- `nil` 값을 전파한다. 이때 `nil`을 반환하거나 <doc:OptionalChaining>에서 설명한 `?.` 연산자를 사용한다.

- `??` 연산자를 사용해 대체 값을 제공한다.

- `!` 연산자를 사용해 프로그램 실행을 중단한다.

> 참고:
> Objective-C에서 `nil`은 존재하지 않는 객체를 가리키는 포인터다. Swift에서 `nil`은 포인터가 아니라 특정 타입의 값이 없는 상태를 나타낸다. *어떤* 타입의 옵셔널이라도 `nil`로 설정할 수 있으며, 객체 타입만이 아니다.


### 옵셔널 바인딩

옵셔널 바인딩은 옵셔널이 값을 가지고 있는지 확인하고, 값이 있다면 그 값을 임시 상수나 변수로 사용할 수 있게 해준다. 옵셔널 바인딩은 `if`, `guard`, `while` 문과 함께 사용해 옵셔널 내부의 값을 확인하고, 그 값을 상수나 변수로 추출할 수 있다. 이 과정은 하나의 동작으로 이루어진다. `if`, `guard`, `while` 문에 대한 더 자세한 내용은 <doc:ControlFlow>를 참고하라.

`if` 문에서 옵셔널 바인딩을 사용하는 방법은 다음과 같다:

```swift
if let <#constantName#> = <#someOptional#> {
   <#statements#>
}
```

`possibleNumber` 예제를 강제 언래핑 대신 옵셔널 바인딩을 사용하도록 다시 작성할 수 있다:

```swift
if let actualNumber = Int(possibleNumber) {
    print("The string \"\(possibleNumber)\" has an integer value of \(actualNumber)")
} else {
    print("The string \"\(possibleNumber)\" couldn't be converted to an integer")
}
// Prints "The string "123" has an integer value of 123"
```

<!--
  - test: `optionals`

  ```swifttest
  -> if let actualNumber = Int(possibleNumber) {
        print("The string \"\(possibleNumber)\" has an integer value of \(actualNumber)")
     } else {
        print("The string \"\(possibleNumber)\" couldn't be converted to an integer")
     }
  <- The string "123" has an integer value of 123
  ```
-->

이 코드는 다음과 같이 읽을 수 있다:

“`Int(possibleNumber)`가 반환한 옵셔널 `Int`가 값을 가지고 있다면, `actualNumber`라는 새로운 상수를 옵셔널에 포함된 값으로 설정한다.”

변환이 성공하면, `actualNumber` 상수는 `if` 문의 첫 번째 분기 내에서 사용할 수 있게 된다. 이 상수는 이미 옵셔널 내부의 값으로 초기화되었으며, 해당하는 논옵셔널 타입을 가진다. 이 경우 `possibleNumber`의 타입은 `Int?`이므로, `actualNumber`의 타입은 `Int`가 된다.

값을 추출한 후 원래의 옵셔널 상수나 변수를 더 이상 참조할 필요가 없다면, 새로운 상수나 변수에 동일한 이름을 사용할 수 있다:

```swift
let myNumber = Int(possibleNumber)
// 여기서 myNumber는 옵셔널 정수다
if let myNumber = myNumber {
    // 여기서 myNumber는 논옵셔널 정수다
    print("My number is \(myNumber)")
}
// Prints "My number is 123"
```

<!--
  - test: `optionals`

  ```swifttest
  -> let myNumber = Int(possibleNumber)
  // 여기서 myNumber는 옵셔널 정수다
  -> if let myNumber = myNumber {
         // 여기서 myNumber는 논옵셔널 정수다
         print("My number is \(myNumber)")
     }
  <- My number is 123
  ```
-->

이 코드는 이전 예제와 마찬가지로 `myNumber`가 값을 가지고 있는지 먼저 확인한다. `myNumber`가 값을 가지고 있다면, `myNumber`라는 새로운 상수를 그 값으로 설정한다. `if` 문의 본문 내에서 `myNumber`를 참조하면 이 새로운 논옵셔널 상수를 가리킨다. `if` 문 전후에서 `myNumber`를 참조하면 원래의 옵셔널 정수 상수를 가리킨다.

이러한 코드는 매우 흔하기 때문에, 옵셔널 값을 언래핑하는 더 짧은 표기법을 사용할 수 있다: 언래핑할 상수나 변수의 이름만 적으면 된다. 새로운 언래핑된 상수나 변수는 암시적으로 옵셔널 값과 동일한 이름을 사용한다.

```swift
if let myNumber {
    print("My number is \(myNumber)")
}
// Prints "My number is 123"
```

<!--
  - test: `optionals`

  ```swifttest
  -> if let myNumber {
         print("My number is \(myNumber)")
     }
  <- My number is 123
  ```
-->

옵셔널 바인딩은 상수와 변수 모두에 사용할 수 있다. `if` 문의 첫 번째 분기 내에서 `myNumber`의 값을 조작하려면 `if var myNumber`로 작성하면 된다. 이렇게 하면 옵셔널 내부의 값이 상수가 아닌 변수로 사용 가능해진다. `if` 문 본문 내에서 `myNumber`에 가한 변경은 해당 지역 변수에만 적용되며, 언래핑한 원래의 옵셔널 상수나 변수에는 영향을 미치지 않는다.

하나의 `if` 문에 필요한 만큼 여러 옵셔널 바인딩과 불리언 조건을 포함할 수 있으며, 이를 쉼표로 구분한다. 옵셔널 바인딩 중 하나라도 `nil`이거나 불리언 조건이 `false`로 평가되면, 전체 `if` 문의 조건은 `false`로 간주된다. 다음 두 `if` 문은 동일하다:

```swift
if let firstNumber = Int("4"), let secondNumber = Int("42"), firstNumber < secondNumber && secondNumber < 100 {
    print("\(firstNumber) < \(secondNumber) < 100")
}
// Prints "4 < 42 < 100"

if let firstNumber = Int("4") {
    if let secondNumber = Int("42") {
        if firstNumber < secondNumber && secondNumber < 100 {
            print("\(firstNumber) < \(secondNumber) < 100")
        }
    }
}
// Prints "4 < 42 < 100"
```

<!--
  - test: `multipleOptionalBindings`

  ```swifttest
  -> if let firstNumber = Int("4"), let secondNumber = Int("42"), firstNumber < secondNumber && secondNumber < 100 {
        print("\(firstNumber) < \(secondNumber) < 100")
     }
  <- 4 < 42 < 100

  -> if let firstNumber = Int("4") {
         if let secondNumber = Int("42") {
             if firstNumber < secondNumber && secondNumber < 100 {
                 print("\(firstNumber) < \(secondNumber) < 100")
             }
         }
     }
  <- 4 < 42 < 100
  ```
-->

`if` 문에서 옵셔널 바인딩으로 생성된 상수와 변수는 `if` 문의 본문 내에서만 사용할 수 있다. 반면, `guard` 문으로 생성된 상수와 변수는 `guard` 문 이후의 코드에서도 사용할 수 있다. 이에 대한 자세한 내용은 <doc:ControlFlow#Early-Exit>에서 확인할 수 있다.


### 기본값 제공하기

값이 없는 경우를 처리하는 또 다른 방법은 nil 병합 연산자(`??`)를 사용해 기본값을 제공하는 것이다. `??` 왼쪽에 있는 옵셔널 값이 `nil`이 아니면 해당 값을 언래핑해 사용한다. 반면 `nil`인 경우 `??` 오른쪽에 있는 값을 사용한다. 예를 들어, 아래 코드는 이름이 지정된 경우 해당 이름으로 인사하고, 이름이 `nil`인 경우 일반적인 인사말을 사용한다.

```swift
let name: String? = nil
let greeting = "Hello, " + (name ?? "friend") + "!"
print(greeting)
// Prints "Hello, friend!"
```

<!--
.. testcode:: optionalFallback

   ```swifttest
   -> let name: String? = nil
   -> let greeting = "Hello, " + (name ?? "friend") + "!"
   -> print(greeting)
   <- Hello, friend!
   ```
-->

`??`를 사용해 기본값을 제공하는 방법에 대한 더 자세한 정보는 <doc:BasicOperators#Nil-Coalescing-Operator>를 참고한다.


### 강제 언래핑(Force Unwrapping)

`nil`이 프로그래머 실수나 손상된 상태처럼 복구할 수 없는 오류를 나타낼 때, 옵셔널 값 뒤에 느낌표(`!`)를 추가해 내부 값을 직접 접근할 수 있다. 이를 *강제 언래핑*이라고 한다. 강제 언래핑을 통해 `nil`이 아닌 값에 접근하면 언래핑된 값을 얻을 수 있다. 하지만 `nil`에 강제 언래핑을 시도하면 런타임 오류가 발생한다.

`!`는 사실상 [`fatalError(_:file:line:)`][]의 짧은 표현이다. 예를 들어, 아래 코드는 두 가지 동일한 접근 방식을 보여준다:

[`fatalError(_:file:line:)`]: https://developer.apple.com/documentation/swift/fatalerror(_:file:line:)

```swift
let possibleNumber = "123"
let convertedNumber = Int(possibleNumber)

let number = convertedNumber!

guard let number = convertedNumber else {
    fatalError("The number was invalid")
}
```

위 코드의 두 버전 모두 `convertedNumber`가 항상 값을 포함한다고 가정한다. 이 요구사항을 코드에 명시적으로 작성하면, 런타임에 해당 조건이 충족되는지 확인할 수 있다.

데이터 요구사항을 강제하고 런타임에 가정을 검증하는 방법에 대한 자세한 내용은 <doc:TheBasics#Assertions-and-Preconditions>를 참고한다.


### 암시적 옵셔널 언래핑

앞서 설명한 것처럼, 옵셔널은 상수나 변수가 "값이 없을 수 있음"을 나타낸다. `if` 문을 사용해 옵셔널에 값이 있는지 확인할 수 있으며, 옵셔널 바인딩을 통해 조건부로 값을 언래핑하여 접근할 수도 있다.

프로그램의 구조상 특정 옵셔널이 처음 값이 설정된 후에는 *항상* 값을 가질 것임이 명확한 경우가 있다. 이런 경우에는 매번 옵셔널 값을 확인하고 언래핑할 필요를 없앨 수 있다. 항상 값이 있다고 안전하게 가정할 수 있기 때문이다.

이런 종류의 옵셔널을 *암시적 옵셔널 언래핑*이라고 한다. 암시적 옵셔널 언래핑을 사용하려면 옵셔널로 만들 타입 뒤에 물음표(`String?`) 대신 느낌표(`String!`)를 붙인다. 옵셔널을 사용할 때 이름 뒤에 느낌표를 붙이는 대신, 선언 시 타입 뒤에 느낌표를 붙인다.

암시적 옵셔널 언래핑은 옵셔널이 처음 정의된 직후에 값이 존재하는 것이 확인되고, 이후에도 항상 값이 존재한다고 확신할 수 있는 경우에 유용하다. Swift에서 암시적 옵셔널 언래핑의 주요 사용처는 클래스 초기화 과정이다. 이는 <doc:AutomaticReferenceCounting#Unowned-References-and-Implicitly-Unwrapped-Optional-Properties>에서 자세히 설명한다.

나중에 변수가 `nil`이 될 가능성이 있다면 암시적 옵셔널 언래핑을 사용하지 않는다. 변수의 수명 동안 `nil` 값을 확인해야 한다면 항상 일반 옵셔널 타입을 사용한다.

암시적 옵셔널 언래핑은 내부적으로는 일반 옵셔널과 같지만, 매번 옵셔널 값을 언래핑할 필요 없이 비옵셔널 값처럼 사용할 수 있다. 다음 예제는 옵셔널 문자열과 암시적 옵셔널 언래핑 문자열의 차이를 보여준다:

```swift
let possibleString: String? = "An optional string."
let forcedString: String = possibleString! // 명시적 언래핑 필요

let assumedString: String! = "An implicitly unwrapped optional string."
let implicitString: String = assumedString // 자동으로 언래핑됨
```

<!--
  - test: `implicitlyUnwrappedOptionals`

  ```swifttest
  -> let possibleString: String? = "An optional string."
  -> let forcedString: String = possibleString! // 느낌표 필요

  -> let assumedString: String! = "An implicitly unwrapped optional string."
  -> let implicitString: String = assumedString // 느낌표 필요 없음
  ```
-->

암시적 옵셔널 언래핑은 필요할 때 옵셔널을 강제로 언래핑할 수 있는 권한을 부여한다고 생각할 수 있다. 암시적 옵셔널 언래핑 값을 사용할 때, Swift는 먼저 일반 옵셔널 값으로 사용하려고 시도한다. 옵셔널로 사용할 수 없으면 Swift가 값을 강제로 언래핑한다. 위 코드에서 `assumedString` 옵셔널 값은 `implicitString`에 할당되기 전에 강제로 언래핑된다. `implicitString`이 명시적 비옵셔널 타입 `String`을 가지고 있기 때문이다. 아래 코드에서 `optionalString`은 명시적 타입이 없으므로 일반 옵셔널이다.

```swift
let optionalString = assumedString
// optionalString의 타입은 "String?"이고 assumedString은 강제로 언래핑되지 않는다.
```

<!--
  - test: `implicitlyUnwrappedOptionals`

  ```swifttest
  -> let optionalString = assumedString
  // optionalString의 타입은 "String?"이고 assumedString은 강제로 언래핑되지 않는다.
  >> print(type(of: optionalString))
  << Optional<String>
  ```
-->

암시적 옵셔널 언래핑이 `nil`인 상태에서 그 안의 값에 접근하려고 하면 런타임 오류가 발생한다. 이 결과는 일반 옵셔널을 강제로 언래핑하려고 할 때와 정확히 같다.

암시적 옵셔널 언래핑이 `nil`인지 확인하는 방법은 일반 옵셔널을 확인하는 방법과 동일하다:

```swift
if assumedString != nil {
    print(assumedString!)
}
// "An implicitly unwrapped optional string." 출력
```

<!--
  - test: `implicitlyUnwrappedOptionals`

  ```swifttest
  -> if assumedString != nil {
        print(assumedString!)
     }
  <- An implicitly unwrapped optional string.
  ```
-->

옵셔널 바인딩을 사용해 암시적 옵셔널 언래핑의 값을 확인하고 언래핑할 수도 있다:

```swift
if let definiteString = assumedString {
    print(definiteString)
}
// "An implicitly unwrapped optional string." 출력
```

<!--
  - test: `implicitlyUnwrappedOptionals`

  ```swifttest
  -> if let definiteString = assumedString {
        print(definiteString)
     }
  <- An implicitly unwrapped optional string.
  ```
-->


## 에러 처리

프로그램 실행 중 발생할 수 있는 오류 상황에 대응하기 위해 **에러 처리**를 사용한다.

옵셔널은 값의 존재 여부로 함수의 성공 또는 실패를 전달할 수 있지만,  
에러 처리를 사용하면 실패의 근본적인 원인을 파악하고, 필요할 경우 에러를 프로그램의 다른 부분으로 전파할 수 있다.

함수가 오류 상황을 만나면 에러를 **던지고**(throw),  
해당 함수를 호출한 쪽에서 에러를 **잡아서**(catch) 적절히 대응한다.

```swift
func canThrowAnError() throws {
    // 이 함수는 에러를 던질 수도 있고, 던지지 않을 수도 있다
}
```

함수가 에러를 던질 수 있음을 나타내려면 선언부에 `throws` 키워드를 추가한다.  
에러를 던질 수 있는 함수를 호출할 때는 표현식 앞에 `try` 키워드를 붙인다.

Swift는 에러가 `catch` 절에 처리될 때까지 현재 스코프 밖으로 자동으로 전파한다.

```swift
do {
    try canThrowAnError()
    // 에러가 던져지지 않음
} catch {
    // 에러가 던져짐
}
```

`do` 문은 새로운 포함 스코프를 생성하며,  
이를 통해 에러를 하나 이상의 `catch` 절로 전파할 수 있다.

다음은 다양한 오류 상황에 대응하기 위해 에러 처리를 사용하는 예제다:

```swift
func makeASandwich() throws {
    // ...
}

do {
    try makeASandwich()
    eatASandwich()
} catch SandwichError.outOfCleanDishes {
    washDishes()
} catch SandwichError.missingIngredients(let ingredients) {
    buyGroceries(ingredients)
}
```

이 예제에서 `makeASandwich()` 함수는  
깨끗한 접시가 없거나 재료가 부족할 때 에러를 던진다.  
`makeASandwich()`가 에러를 던질 수 있으므로,  
함수 호출은 `try` 표현식으로 감싼다.  
`do` 문으로 함수 호출을 감싸면,  
던져진 모든 에러는 제공된 `catch` 절로 전파된다.

에러가 던져지지 않으면 `eatASandwich()` 함수가 호출된다.  
에러가 던져지고 `SandwichError.outOfCleanDishes` 케이스와 일치하면  
`washDishes()` 함수가 호출된다.  
에러가 던져지고 `SandwichError.missingIngredients` 케이스와 일치하면  
`catch` 패턴에 의해 캡처된 연관 값 `[String]`을 사용해  
`buyGroceries(_:)` 함수가 호출된다.

에러를 던지고, 잡고, 전파하는 방법에 대한 자세한 내용은  
<doc:ErrorHandling>에서 확인할 수 있다.


## 어설션과 전제 조건

*어설션(Assertion)*과 *전제 조건(Precondition)*은 런타임에 실행되는 검사 기능이다. 이들은 코드를 더 진행하기 전에 필수적인 조건이 충족되었는지 확인하는 데 사용된다. 어설션 또는 전제 조건의 불리언 조건이 `true`로 평가되면 코드 실행이 정상적으로 계속된다. 하지만 조건이 `false`로 평가되면 프로그램의 현재 상태가 유효하지 않다는 의미이며, 코드 실행이 중단되고 앱이 종료된다.

어설션과 전제 조건은 코드를 작성할 때 가정한 내용과 기대 사항을 표현하는 데 사용된다. 따라서 이들은 코드의 일부로 포함될 수 있다. 어설션은 개발 과정에서 발생할 수 있는 실수나 잘못된 가정을 찾는 데 도움을 주며, 전제 조건은 프로덕션 환경에서 발생할 수 있는 문제를 감지하는 데 유용하다.

런타임에 기대 사항을 검증하는 것 외에도, 어설션과 전제 조건은 코드 내에서 유용한 문서 역할도 한다. 앞서 <doc:TheBasics#Error-Handling>에서 다룬 오류 조건과 달리, 어설션과 전제 조건은 복구 가능하거나 예상된 오류를 처리하는 데 사용되지 않는다. 어설션 또는 전제 조건이 실패하면 프로그램의 상태가 유효하지 않음을 의미하며, 실패한 어설션을 잡아내는 방법은 없다. 유효하지 않은 상태에서 복구하는 것은 불가능하다. 어설션이 실패하면 프로그램의 데이터 중 최소한 하나가 유효하지 않다는 뜻이지만, 왜 유효하지 않은지 또는 추가적인 상태도 유효하지 않은지는 알 수 없다.

어설션과 전제 조건을 사용하는 것은 유효하지 않은 조건이 발생하지 않도록 코드를 설계하는 대체 수단이 아니다. 그러나 유효한 데이터와 상태를 강제하기 위해 이들을 사용하면, 유효하지 않은 상태가 발생했을 때 앱이 더 예측 가능한 방식으로 종료되며 문제를 디버깅하기 쉬워진다. 가정을 검사하지 않으면, 사용자 데이터가 조용히 손상된 후 다른 코드에서 명확한 오류가 발생할 때까지 이와 같은 문제를 알아차리지 못할 수 있다. 유효하지 않은 상태가 감지되면 즉시 실행을 중단하는 것은 해당 상태로 인한 피해를 제한하는 데도 도움이 된다.

어설션과 전제 조건의 차이는 검사 시점에 있다. 어설션은 디버그 빌드에서만 검사되지만, 전제 조건은 디버그와 프로덕션 빌드 모두에서 검사된다. 프로덕션 빌드에서는 어설션 내부의 조건이 평가되지 않는다. 이는 개발 과정에서 원하는 만큼 어설션을 사용하더라도 프로덕션 환경의 성능에 영향을 미치지 않음을 의미한다.


### 어설션을 활용한 디버깅

<!--
  디버그 환경에서 코드가 어설션을 트리거하면,
  예를 들어 Xcode에서 앱을 빌드하고 실행할 때,
  잘못된 상태가 발생한 정확한 위치를 확인할 수 있고
  어설션이 트리거된 시점의 앱 상태를 조회할 수 있다.
  또한 어설션을 통해 디버그 메시지를 제공할 수 있다.
-->

Swift 표준 라이브러리의 [`assert(_:_:file:line:)`](https://developer.apple.com/documentation/swift/1541112-assert) 함수를 호출해 어설션을 작성한다. 이 함수에 `true` 또는 `false`로 평가되는 표현식과 조건이 `false`일 때 표시할 메시지를 전달한다. 예를 들어:

```swift
let age = -3
assert(age >= 0, "사람의 나이는 0보다 작을 수 없습니다.")
// -3은 >= 0이 아니므로 이 어설션은 실패한다.
```

<!--
  - test: `assertions-1`

  ```swifttest
  -> let age = -3
  -> assert(age >= 0, "A person's age can't be less than zero.")
  xx assert
  // This assertion fails because -3 isn't >= 0.
  ```
-->

이 예제에서 `age >= 0`이 `true`로 평가되면 코드 실행이 계속된다. 즉, `age` 값이 음수가 아닌 경우다. 위 코드처럼 `age` 값이 음수라면 `age >= 0`은 `false`로 평가되고, 어설션이 실패하며 애플리케이션이 종료된다.

어설션 메시지는 생략할 수 있다. 예를 들어, 조건을 그대로 반복하는 경우다.

```swift
assert(age >= 0)
```

<!--
  - test: `assertions-2`

  ```swifttest
  >> let age = -3
  -> assert(age >= 0)
  xx assert
  ```
-->

<!--
  - test: `assertionsCanUseStringInterpolation`

  ```swifttest
  -> let age = -3
  -> assert(age >= 0, "A person's age can't be less than zero, but value is \(age).")
  xx assert
  ```
-->

이미 조건을 확인한 경우, [`assertionFailure(_:file:line:)`](https://developer.apple.com/documentation/swift/1539616-assertionfailure) 함수를 사용해 어설션이 실패했음을 나타낼 수 있다. 예를 들어:

```swift
if age > 10 {
    print("롤러코스터나 페리스휠을 탈 수 있습니다.")
} else if age >= 0 {
    print("페리스휠을 탈 수 있습니다.")
} else {
    assertionFailure("사람의 나이는 0보다 작을 수 없습니다.")
}
```

<!--
  - test: `assertions-3`

  ```swifttest
  >> let age = -3
  -> if age > 10 {
         print("You can ride the roller-coaster or the ferris wheel.")
     } else if age >= 0 {
         print("You can ride the ferris wheel.")
     } else {
         assertionFailure("A person's age can't be less than zero.")
     }
  xx assert
  ```
-->


### 전제 조건 강제 적용

코드가 계속 실행되려면 반드시 참이어야 하는 조건이 거짓일 가능성이 있을 때 전제 조건을 사용한다. 예를 들어, 배열의 인덱스가 범위를 벗어나지 않았는지 확인하거나, 함수에 유효한 값이 전달되었는지 검사할 때 전제 조건을 활용한다.

전제 조건은 [`precondition(_:_:file:line:)`](https://developer.apple.com/documentation/swift/1540960-precondition) 함수를 호출해 작성한다. 이 함수에는 참 또는 거짓으로 평가되는 표현식과 조건이 거짓일 때 표시할 메시지를 전달한다. 예를 들어:

```swift
// 서브스크립트 구현에서...
precondition(index > 0, "인덱스는 0보다 커야 합니다.")
```

<!--
  - test: `preconditions`

  ```swifttest
  >> let index = -1
  // 서브스크립트 구현에서...
  -> precondition(index > 0, "인덱스는 0보다 커야 합니다.")
  xx assert
  ```
-->

또한 [`preconditionFailure(_:file:line:)`](https://developer.apple.com/documentation/swift/1539374-preconditionfailure) 함수를 호출해 실패가 발생했음을 나타낼 수도 있다. 예를 들어, 스위치 문의 기본 케이스가 실행되었지만, 모든 유효한 입력 데이터는 스위치의 다른 케이스에서 처리되어야 하는 경우에 사용할 수 있다.

> 참고: 확인되지 않은 모드(`-Ounchecked`)로 컴파일하면 전제 조건이 검사되지 않는다. 컴파일러는 전제 조건이 항상 참이라고 가정하고, 이에 따라 코드를 최적화한다. 그러나 `fatalError(_:file:line:)` 함수는 최적화 설정에 관계없이 항상 실행을 중단한다.
>
> 프로토타이핑이나 초기 개발 단계에서 아직 구현되지 않은 기능의 스텁을 만들 때 `fatalError(_:file:line:)` 함수를 사용할 수 있다. `fatalError("구현되지 않음")`을 스텁 구현으로 작성하면 된다. 치명적 오류는 단언문이나 전제 조건과 달리 최적화되지 않으므로, 스텁 구현을 만나면 항상 실행이 중단됨을 보장할 수 있다.

<!--
  "\ " in the first cell below lets it be empty.
  Otherwise RST treats the row as a continuation.

  ============ =====  ==========  ===============================
  \            Debug  Production  Production with ``-Ounchecked``
  ============ =====  ==========  ===============================
  Assertion    Yes    No          No
  ------------ -----  ----------  -------------------------------
  Precondition Yes    Yes         No
  ------------ -----  ----------  -------------------------------
  Fatal Error  Yes    Yes         Yes
  ============ =====  ==========  ===============================
-->

<!--
  TODO: In Xcode, can you set a breakpoint on assertion/precondition failure?
  If so, mention that fact and give a link to a guide that shows you how.
  In LLDB, 'breakpoint set -E swift' catches when errors are thrown,
  but doesn't stop at assertions.
-->

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


