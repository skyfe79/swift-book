# 패턴

값을 매칭하고 구조를 분해한다.

*패턴*은 단일 값 또는 복합 값의 구조를 나타낸다. 예를 들어, 튜플 `(1, 2)`의 구조는 두 개의 요소로 이루어진 쉼표로 구분된 리스트다. 패턴은 특정 값이 아닌 값의 구조를 나타내므로 다양한 값과 매칭할 수 있다. 예를 들어, 패턴 `(x, y)`는 튜플 `(1, 2)`뿐만 아니라 다른 두 요소 튜플과도 매칭된다. 패턴을 값과 매칭하는 것 외에도, 복합 값의 일부 또는 전체를 추출하고 각 부분을 상수나 변수 이름에 바인딩할 수 있다.

Swift에는 두 가지 기본적인 종류의 패턴이 있다: 모든 종류의 값과 성공적으로 매칭되는 패턴과 런타임에 지정된 값과 매칭되지 않을 수 있는 패턴.

첫 번째 종류의 패턴은 단순 변수, 상수, 옵셔널 바인딩에서 값을 분해할 때 사용된다. 이 패턴에는 와일드카드 패턴, 식별자 패턴, 그리고 이를 포함하는 값 바인딩 또는 튜플 패턴이 포함된다. 이러한 패턴에 타입 어노테이션을 지정해 특정 타입의 값만 매칭되도록 제한할 수 있다.

두 번째 종류의 패턴은 완전한 패턴 매칭에 사용되며, 런타임에 매칭하려는 값이 없을 수 있다. 이 패턴에는 열거형 케이스 패턴, 옵셔널 패턴, 표현식 패턴, 타입 캐스팅 패턴이 포함된다. 이러한 패턴은 `switch` 문의 케이스 라벨, `do` 문의 `catch` 절, 또는 `if`, `while`, `guard`, `for`-`in` 문의 케이스 조건에서 사용된다.

> 패턴 문법:
>
> *pattern* → *wildcard-pattern* *type-annotation*_?_ \
> *pattern* → *identifier-pattern* *type-annotation*_?_ \
> *pattern* → *value-binding-pattern* \
> *pattern* → *tuple-pattern* *type-annotation*_?_ \
> *pattern* → *enum-case-pattern* \
> *pattern* → *optional-pattern* \
> *pattern* → *type-casting-pattern* \
> *pattern* → *expression-pattern*


## 와일드카드 패턴

*와일드카드 패턴*은 모든 값을 매칭하고 무시하며, 언더스코어(`_`)로 구성된다. 매칭 대상의 값이 중요하지 않을 때 와일드카드 패턴을 사용한다. 예를 들어, 다음 코드는 `1...3` 범위를 순회하면서 각 반복에서 범위의 현재 값을 무시한다:

```swift
for _ in 1...3 {
    // 어떤 작업을 세 번 수행한다.
}
```

<!--
  - test: `wildcard-pattern`

  ```swifttest
  -> for _ in 1...3 {
        // 어떤 작업을 세 번 수행한다.
     }
  ```
-->

> 와일드카드 패턴 문법:
>
> *와일드카드 패턴* → **`_`**


## 식별자 패턴

*식별자 패턴*은 모든 값을 매칭하고, 매칭된 값을 변수나 상수 이름에 바인딩한다. 예를 들어, 다음 상수 선언에서 `someValue`는 `Int` 타입의 값 `42`와 매칭되는 식별자 패턴이다:

```swift
let someValue = 42
```

<!--
  - test: `identifier-pattern`

  ```swifttest
  -> let someValue = 42
  ```
-->

매칭이 성공하면, 값 `42`는 상수 이름 `someValue`에 바인딩(할당)된다.

변수나 상수 선언의 왼쪽에 있는 패턴이 식별자 패턴일 때, 식별자 패턴은 암시적으로 값 바인딩 패턴의 하위 패턴이 된다.

> 식별자 패턴의 문법:
>
> *identifier-pattern* → *identifier*


## 값 바인딩 패턴

*값 바인딩 패턴*은 매칭된 값을 변수나 상수 이름에 바인딩한다. 매칭된 값을 상수 이름에 바인딩하는 값 바인딩 패턴은 `let` 키워드로 시작하고, 변수 이름에 바인딩하는 패턴은 `var` 키워드로 시작한다.

값 바인딩 패턴 내의 식별자 패턴은 매칭된 값에 새로운 변수나 상수를 바인딩한다. 예를 들어, 튜플의 요소를 분해하고 각 요소의 값을 해당 식별자 패턴에 바인딩할 수 있다.

```swift
let point = (3, 2)
switch point {
// point의 요소를 x와 y에 바인딩.
case let (x, y):
    print("The point is at (\(x), \(y)).")
}
// 출력: "The point is at (3, 2)."
```

<!--
  - test: `value-binding-pattern`

  ```swifttest
  -> let point = (3, 2)
  -> switch point {
        // point의 요소를 x와 y에 바인딩.
        case let (x, y):
           print("The point is at (\(x), \(y)).")
     }
  <- The point is at (3, 2).
  ```
-->

위 예제에서 `let`은 튜플 패턴 `(x, y)`의 각 식별자 패턴에 적용된다. 이 동작 때문에 `switch` 케이스 `case let (x, y):`와 `case (let x, let y):`는 동일한 값에 매칭된다.

> 값 바인딩 패턴 문법:
>
> *value-binding-pattern* → **`var`** *pattern* | **`let`** *pattern*

<!--
  NOTE: 이 패턴을 "variable pattern" 대신 "value-binding pattern"이라고 부르기로 결정했다.
  이는 이 패턴이 값에 변수나 상수를 바인딩하는 패턴이기 때문이며,
  패턴 자체가 변하는 패턴이 아니기 때문이다.
  "Variable pattern"은 이 두 가지 의미 사이에서 모호하다.
-->


## 튜플 패턴

*튜플 패턴*은 쉼표로 구분된 0개 이상의 패턴을 괄호로 감싼 형태이다. 튜플 패턴은 해당 튜플 타입의 값과 매칭된다.

타입 어노테이션을 사용하면 튜플 패턴이 특정 튜플 타입과만 매칭되도록 제한할 수 있다. 예를 들어, 상수 선언 `let (x, y): (Int, Int) = (1, 2)`에서 튜플 패턴 `(x, y): (Int, Int)`는 두 요소가 모두 `Int` 타입인 튜플 타입과만 매칭된다.

튜플 패턴이 `for`-`in` 문이나 변수/상수 선언에서 패턴으로 사용될 때, 와일드카드 패턴, 식별자 패턴, 옵셔널 패턴, 또는 이러한 패턴을 포함한 다른 튜플 패턴만 포함할 수 있다. 예를 들어, 다음 코드는 튜플 패턴 `(x, 0)`의 요소 `0`이 표현식 패턴이기 때문에 유효하지 않다:

```swift
let points = [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1)]
// 이 코드는 유효하지 않다.
for (x, 0) in points {
    /* ... */
}
```

<!--
  - test: `tuple-pattern`

  ```swifttest
  -> let points = [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1)]
  -> // This code isn't valid.
  -> for (x, 0) in points {
  >>    _ = x
        /* ... */
     }
  !$ error: expected pattern
  !! for (x, 0) in points {
  !!         ^
  ```
-->

단일 요소를 포함하는 튜플 패턴의 괄호는 아무런 효과가 없다. 이 패턴은 단일 요소의 타입과 매칭된다. 예를 들어, 다음 코드는 모두 동일하다:

<!--
  This test needs to be compiled.
  The error message in the REPL is unpredictable as of
  Swift version 1.1 (swift-600.0.54.20)
-->

```swift
let a = 2        // a: Int = 2
let (a) = 2      // a: Int = 2
let (a): Int = 2 // a: Int = 2
```

<!--
  - test: `single-element-tuple-pattern`

  ```swifttest
  -> let a = 2        // a: Int = 2
  -> let (a) = 2      // a: Int = 2
  -> let (a): Int = 2 // a: Int = 2
  !$ error: invalid redeclaration of 'a'
  !! let (a) = 2      // a: Int = 2
  !! ^
  !$ note: 'a' previously declared here
  !! let a = 2        // a: Int = 2
  !! ^
  !$ error: invalid redeclaration of 'a'
  !! let (a): Int = 2 // a: Int = 2
  !! ^
  !$ note: 'a' previously declared here
  !! let a = 2        // a: Int = 2
  !! ^
  ```
-->

> 튜플 패턴 문법:
>
> *tuple-pattern* → **`(`** *tuple-pattern-element-list*_?_ **`)`** \
> *tuple-pattern-element-list* → *tuple-pattern-element* | *tuple-pattern-element* **`,`** *tuple-pattern-element-list* \
> *tuple-pattern-element* → *pattern* | *identifier* **`:`** *pattern*


## 열거형 케이스 패턴

*열거형 케이스 패턴*은 기존 열거형 타입의 특정 케이스와 매칭된다. 이 패턴은 `switch` 문의 케이스 레이블과 `if`, `while`, `guard`, `for`-`in` 문의 조건에서 사용된다.

매칭하려는 열거형 케이스에 연관 값이 있다면, 해당 열거형 케이스 패턴은 각 연관 값에 대한 요소를 포함하는 튜플 패턴을 명시해야 한다. 연관 값을 포함한 열거형 케이스를 매칭하는 `switch` 문의 예제는 <doc:Enumerations#Associated-Values>를 참고한다.

열거형 케이스 패턴은 옵셔널로 감싸진 해당 케이스의 값과도 매칭된다. 이 간결한 문법을 사용하면 옵셔널 패턴을 생략할 수 있다. `Optional`이 열거형으로 구현되어 있기 때문에, `.none`과 `.some`은 동일한 `switch` 문에서 열거형 타입의 케이스와 함께 사용할 수 있다.

```swift
enum SomeEnum { case left, right }
let x: SomeEnum? = .left
switch x {
case .left:
    print("Turn left")
case .right:
    print("Turn right")
case nil:
    print("Keep going straight")
}
// Prints "Turn left"
```

<!--
  - test: `enum-pattern-matching-optional`

  ```swifttest
  -> enum SomeEnum { case left, right }
  -> let x: SomeEnum? = .left
  -> switch x {
     case .left:
         print("Turn left")
     case .right:
         print("Turn right")
     case nil:
         print("Keep going straight")
     }
  <- Turn left
  ```
-->

> 열거형 케이스 패턴의 문법:
>
> *enum-case-pattern* → *type-identifier*_?_ **`.`** *enum-case-name* *tuple-pattern*_?_


## 옵셔널 패턴

옵셔널 패턴은 `Optional<Wrapped>` 열거형의 `some(Wrapped)` 케이스로 래핑된 값을 매칭한다. 옵셔널 패턴은 식별자 패턴 뒤에 물음표를 붙여 사용하며, 열거형 케이스 패턴이 사용되는 곳에서 동일하게 활용할 수 있다.

옵셔널 패턴은 `Optional` 열거형 케이스 패턴을 간편하게 사용할 수 있도록 하는 문법적 설탕이다. 따라서 다음 두 코드는 동일한 결과를 보인다:

```swift
let someOptional: Int? = 42
// 열거형 케이스 패턴을 사용해 매칭
if case .some(let x) = someOptional {
    print(x)
}

// 옵셔널 패턴을 사용해 매칭
if case let x? = someOptional {
    print(x)
}
```

<!--
  - test: `optional-pattern`

  ```swifttest
  -> let someOptional: Int? = 42
  -> // Match using an enumeration case pattern.
  -> if case .some(let x) = someOptional {
        print(x)
     }
  << 42

  -> // Match using an optional pattern.
  -> if case let x? = someOptional {
        print(x)
     }
  << 42
  ```
-->

옵셔널 패턴은 `for`-`in` 구문에서 옵셔널 값 배열을 순회할 때 유용하다. 이 패턴을 사용하면 `nil`이 아닌 요소에 대해서만 반복문의 본문을 실행할 수 있다.

```swift
let arrayOfOptionalInts: [Int?] = [nil, 2, 3, nil, 5]
// nil이 아닌 값만 매칭
for case let number? in arrayOfOptionalInts {
    print("Found a \(number)")
}
// Found a 2
// Found a 3
// Found a 5
```

<!--
  - test: `optional-pattern-for-in`

  ```swifttest
  -> let arrayOfOptionalInts: [Int?] = [nil, 2, 3, nil, 5]
  -> // Match only non-nil values.
  -> for case let number? in arrayOfOptionalInts {
        print("Found a \(number)")
     }
  </ Found a 2
  </ Found a 3
  </ Found a 5
  ```
-->

> 옵셔널 패턴 문법:
>
> *optional-pattern* → *identifier-pattern* **`?`**


## 타입 캐스팅 패턴

타입 캐스팅 패턴에는 `is` 패턴과 `as` 패턴 두 가지가 있다. `is` 패턴은 `switch` 문의 case 레이블에서만 사용된다. `is`와 `as` 패턴은 다음과 같은 형태를 가진다:

```swift
is <#type#>
<#pattern#> as <#type#>
```

`is` 패턴은 런타임에 값의 타입이 `is` 패턴의 오른쪽에 지정된 타입과 동일하거나 그 타입의 하위 클래스인 경우에 매칭된다. `is` 패턴은 `is` 연산자와 유사하게 동작하며, 둘 다 타입 캐스팅을 수행하지만 반환된 타입을 버린다.

`as` 패턴은 런타임에 값의 타입이 `as` 패턴의 오른쪽에 지정된 타입과 동일하거나 그 타입의 하위 클래스인 경우에 매칭된다. 매칭이 성공하면, 매칭된 값의 타입은 `as` 패턴의 오른쪽에 지정된 *패턴*으로 캐스팅된다.

`switch` 문을 사용해 `is`와 `as` 패턴으로 값을 매칭하는 예제는 <doc:TypeCasting#Type-Casting-for-Any-and-AnyObject>를 참고한다.

> 타입 캐스팅 패턴 문법:
>
> *type-casting-pattern* → *is-pattern* | *as-pattern* \
> *is-pattern* → **`is`** *type* \
> *as-pattern* → *pattern* **`as`** *type*


## 표현식 패턴

*표현식 패턴*은 표현식의 값을 나타낸다. 표현식 패턴은 `switch` 문의 case 라벨에서만 사용된다.

표현식 패턴으로 표현된 값은 Swift 표준 라이브러리의 패턴 매칭 연산자(`~=`)를 사용해 입력된 표현식의 값과 비교된다. `~=` 연산자가 `true`를 반환하면 매칭이 성공한다. 기본적으로 `~=` 연산자는 동일한 타입의 두 값을 `==` 연산자를 사용해 비교한다. 또한 특정 범위 내에 값이 포함되는지 확인하는 방식으로 범위와의 매칭도 가능하다. 다음 예제에서 이를 확인할 수 있다.

```swift
let point = (1, 2)
switch point {
case (0, 0):
    print("(0, 0) is at the origin.")
case (-2...2, -2...2):
    print("(\(point.0), \(point.1)) is near the origin.")
default:
    print("The point is at (\(point.0), \(point.1)).")
}
// Prints "(1, 2) is near the origin."
```

<!--
  - test: `expression-pattern`

  ```swifttest
  -> let point = (1, 2)
  -> switch point {
        case (0, 0):
           print("(0, 0) is at the origin.")
        case (-2...2, -2...2):
           print("(\(point.0), \(point.1)) is near the origin.")
        default:
           print("The point is at (\(point.0), \(point.1)).")
     }
  <- (1, 2) is near the origin.
  ```
-->

`~=` 연산자를 오버로드해 커스텀 매칭 동작을 정의할 수 있다. 예를 들어, 위 예제를 수정해 `point` 표현식을 문자열 형태의 점과 비교하도록 만들 수 있다.

```swift
// 문자열과 정수를 매칭하기 위해 ~= 연산자를 오버로드한다.
func ~= (pattern: String, value: Int) -> Bool {
    return pattern == "\(value)"
}
switch point {
case ("0", "0"):
    print("(0, 0) is at the origin.")
default:
    print("The point is at (\(point.0), \(point.1)).")
}
// Prints "The point is at (1, 2)."
```

<!--
  - test: `expression-pattern`

  ```swifttest
  -> // Overload the ~= operator to match a string with an integer.
  -> func ~= (pattern: String, value: Int) -> Bool {
        return pattern == "\(value)"
     }
  -> switch point {
        case ("0", "0"):
           print("(0, 0) is at the origin.")
        default:
           print("The point is at (\(point.0), \(point.1)).")
     }
  <- The point is at (1, 2).
  ```
-->

> 표현식 패턴 문법:
>
> *expression-pattern* → *expression*

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


