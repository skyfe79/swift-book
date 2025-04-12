# 확장 기능

기존 타입에 새로운 기능을 추가한다.

*확장 기능*은 기존 클래스, 구조체, 열거형, 프로토콜 타입에 새로운 기능을 추가할 수 있다. 여기에는 원본 소스 코드에 접근할 수 없는 타입을 확장하는 것도 포함된다(*레트로액티브 모델링*이라고 함). 확장 기능은 Objective-C의 카테고리와 유사하다. (Objective-C 카테고리와 달리 Swift의 확장 기능은 이름을 가지지 않는다.)

Swift에서 확장 기능은 다음과 같은 작업을 수행할 수 있다:

- 계산된 인스턴스 속성과 계산된 타입 속성을 추가
- 인스턴스 메서드와 타입 메서드를 정의
- 새로운 초기화 메서드 제공
- 서브스크립트 정의
- 새로운 중첩 타입 정의 및 사용
- 기존 타입이 프로토콜을 준수하도록 만듦

Swift에서는 프로토콜을 확장하여 해당 요구 사항을 구현하거나, 프로토콜을 준수하는 타입이 활용할 수 있는 추가 기능을 제공할 수도 있다. 자세한 내용은 <doc:Protocols#Protocol-Extensions>를 참고한다.

> 참고: 확장 기능은 타입에 새로운 기능을 추가할 수 있지만, 기존 기능을 재정의할 수는 없다.

<!--
  - test: `extensionsCannotOverrideExistingBehavior`

  ```swifttest
  -> class C {
        var x = 0
        func foo() {}
     }
  -> extension C {
        override var x: Int {
           didSet {
              print("new x is \(x)")
           }
        }
        override func foo() {
           print("called overridden foo")
        }
     }
  !$ error: property does not override any property from its superclass
  !! override var x: Int {
  !! ~~~~~~~~     ^
  !$ error: ambiguous use of 'x'
  !! print("new x is \(x)")
  !!            ^
  !$ note: found this candidate
  !! var x = 0
  !!     ^
  !$ note: found this candidate
  !! override var x: Int {
  !!              ^
  !$ error: invalid redeclaration of 'x'
  !! override var x: Int {
  !!              ^
  !$ note: 'x' previously declared here
  !! var x = 0
  !!     ^
  !$ error: method does not override any method from its superclass
  !! override func foo() {
  !! ~~~~~~~~      ^
  !$ error: invalid redeclaration of 'foo()'
  !! override func foo() {
  !!               ^
  !$ note: 'foo()' previously declared here
  !! func foo() {}
  !!      ^
  ```
-->


## 확장 구문

`extension` 키워드를 사용해 확장을 선언한다:

```swift
extension SomeType {
    // SomeType에 추가할 새로운 기능을 여기에 작성한다
}
```

<!--
  - test: `extensionSyntax`

  ```swifttest
  >> struct SomeType {}
  -> extension SomeType {
        // new functionality to add to SomeType goes here
     }
  ```
-->

확장은 기존 타입이 하나 이상의 프로토콜을 준수하도록 확장할 수 있다. 프로토콜 준수를 추가하려면, 클래스나 구조체에서와 동일한 방식으로 프로토콜 이름을 작성한다:

```swift
extension SomeType: SomeProtocol, AnotherProtocol {
    // 프로토콜 요구사항 구현을 여기에 작성한다
}
```

<!--
  - test: `extensionSyntax`

  ```swifttest
  >> protocol SomeProtocol {}
  >> protocol AnotherProtocol {}
  -> extension SomeType: SomeProtocol, AnotherProtocol {
        // implementation of protocol requirements goes here
     }
  ```
-->

이 방식으로 프로토콜 준수를 추가하는 방법은 <doc:Protocols#Adding-Protocol-Conformance-with-an-Extension>에서 자세히 설명한다.

확장은 기존 제네릭 타입을 확장하는 데 사용할 수 있으며, 이는 <doc:Generics#Extending-a-Generic-Type>에서 설명한다. 또한 제네릭 타입을 확장해 조건부로 기능을 추가할 수도 있다. 이는 <doc:Generics#Extensions-with-a-Generic-Where-Clause>에서 다룬다.

> 참고: 기존 타입에 새로운 기능을 추가하기 위해 확장을 정의하면, 해당 타입의 모든 기존 인스턴스에서 새로운 기능을 사용할 수 있다. 확장이 정의되기 전에 생성된 인스턴스도 포함된다.


## 계산된 프로퍼티

익스텐션은 기존 타입에 계산된 인스턴스 프로퍼티와 계산된 타입 프로퍼티를 추가할 수 있다. 이 예제는 Swift의 기본 `Double` 타입에 다섯 개의 계산된 인스턴스 프로퍼티를 추가해 거리 단위를 다루는 기본 기능을 제공한다:

```swift
extension Double {
    var km: Double { return self * 1_000.0 }
    var m: Double { return self }
    var cm: Double { return self / 100.0 }
    var mm: Double { return self / 1_000.0 }
    var ft: Double { return self / 3.28084 }
}
let oneInch = 25.4.mm
print("One inch is \(oneInch) meters")
// Prints "One inch is 0.0254 meters"
let threeFeet = 3.ft
print("Three feet is \(threeFeet) meters")
// Prints "Three feet is 0.914399970739201 meters"
```

<!--
  - test: `extensionsComputedProperties`

  ```swifttest
  -> extension Double {
        var km: Double { return self * 1_000.0 }
        var m: Double { return self }
        var cm: Double { return self / 100.0 }
        var mm: Double { return self / 1_000.0 }
        var ft: Double { return self / 3.28084 }
     }
  -> let oneInch = 25.4.mm
  -> print("One inch is \(oneInch) meters")
  <- One inch is 0.0254 meters
  -> let threeFeet = 3.ft
  -> print("Three feet is \(threeFeet) meters")
  <- Three feet is 0.914399970739201 meters
  ```
-->

이 계산된 프로퍼티들은 `Double` 값이 특정 길이 단위로 간주되어야 함을 나타낸다. 이 프로퍼티들이 계산된 프로퍼티로 구현되었지만, 점 문법을 통해 부동소수점 리터럴 값에 이 프로퍼티 이름을 추가해 거리 변환을 수행할 수 있다.

이 예제에서 `Double` 값 `1.0`은 "1미터"를 나타낸다. 그래서 `m` 계산된 프로퍼티는 `self`를 반환한다. 즉, 표현식 `1.m`은 `Double` 값 `1.0`을 계산하는 것으로 간주된다.

다른 단위들은 미터 단위로 표현하기 위해 일부 변환이 필요하다. 1킬로미터는 1,000미터와 같으므로, `km` 계산된 프로퍼티는 값을 `1_000.00`으로 곱해 미터 단위로 변환한다. 마찬가지로, 1미터는 3.28084피트이므로, `ft` 계산된 프로퍼티는 기본 `Double` 값을 `3.28084`로 나눠 피트에서 미터로 변환한다.

이 프로퍼티들은 읽기 전용 계산된 프로퍼티이므로, 간결함을 위해 `get` 키워드 없이 표현된다. 반환 값은 `Double` 타입이며, `Double`이 허용되는 모든 수학적 계산에서 사용할 수 있다:

```swift
let aMarathon = 42.km + 195.m
print("A marathon is \(aMarathon) meters long")
// Prints "A marathon is 42195.0 meters long"
```

<!--
  - test: `extensionsComputedProperties`

  ```swifttest
  -> let aMarathon = 42.km + 195.m
  -> print("A marathon is \(aMarathon) meters long")
  <- A marathon is 42195.0 meters long
  ```
-->

> 참고: 익스텐션은 새로운 계산된 프로퍼티를 추가할 수 있지만, 저장된 프로퍼티를 추가하거나 기존 프로퍼티에 프로퍼티 옵저버를 추가할 수는 없다.

<!--
  - test: `extensionsCannotAddStoredProperties`

  ```swifttest
  -> class C {}
  -> extension C { var x = 0 }
  !$ error: extensions must not contain stored properties
  !! extension C { var x = 0 }
  !!                   ^
  ```
-->

<!--
  TODO: change this example to something more advisable / less contentious.
-->


## 초기화 메서드

익스텐션을 통해 기존 타입에 새로운 초기화 메서드를 추가할 수 있다. 이를 통해 다른 타입이 여러분이 정의한 커스텀 타입을 초기화 매개변수로 받아들이도록 확장하거나, 원래 타입 구현에 포함되지 않았던 추가적인 초기화 옵션을 제공할 수 있다.

익스텐션은 클래스에 새로운 편의 초기화 메서드를 추가할 수 있지만, 지정 초기화 메서드나 소멸자는 추가할 수 없다. 지정 초기화 메서드와 소멸자는 반드시 원래 클래스 구현에서 제공해야 한다.

모든 저장 프로퍼티에 기본값을 제공하고 커스텀 초기화 메서드를 정의하지 않은 값 타입에 익스텐션으로 초기화 메서드를 추가하는 경우, 해당 익스텐션의 초기화 메서드 내에서 기본 초기화 메서드와 멤버별 초기화 메서드를 호출할 수 있다. 이는 값 타입의 원래 구현에 초기화 메서드를 작성한 경우와는 다른데, 이에 대한 자세한 내용은 <doc:Initialization#값-타입의-초기화-메서드-위임>에서 확인할 수 있다.

다른 모듈에서 선언된 구조체에 익스텐션으로 초기화 메서드를 추가하는 경우, 새로운 초기화 메서드는 정의 모듈의 초기화 메서드를 호출하기 전까지 `self`에 접근할 수 없다.

아래 예제는 기하학적 사각형을 나타내는 커스텀 `Rect` 구조체를 정의한다. 또한 `Size`와 `Point`라는 두 개의 지원 구조체를 정의하며, 두 구조체는 모든 프로퍼티에 `0.0`이라는 기본값을 제공한다:

```swift
struct Size {
    var width = 0.0, height = 0.0
}
struct Point {
    var x = 0.0, y = 0.0
}
struct Rect {
    var origin = Point()
    var size = Size()
}
```

<!--
  - test: `extensionsInitializers`

  ```swifttest
  -> struct Size {
        var width = 0.0, height = 0.0
     }
  -> struct Point {
        var x = 0.0, y = 0.0
     }
  -> struct Rect {
        var origin = Point()
        var size = Size()
     }
  ```
-->

`Rect` 구조체는 모든 프로퍼티에 기본값을 제공하기 때문에, <doc:Initialization#기본-초기화-메서드>에서 설명한 대로 기본 초기화 메서드와 멤버별 초기화 메서드를 자동으로 받는다. 이러한 초기화 메서드를 사용해 새로운 `Rect` 인스턴스를 생성할 수 있다:

```swift
let defaultRect = Rect()
let memberwiseRect = Rect(origin: Point(x: 2.0, y: 2.0),
    size: Size(width: 5.0, height: 5.0))
```

<!--
  - test: `extensionsInitializers`

  ```swifttest
  -> let defaultRect = Rect()
  -> let memberwiseRect = Rect(origin: Point(x: 2.0, y: 2.0),
        size: Size(width: 5.0, height: 5.0))
  ```
-->

`Rect` 구조체를 확장해 특정 중심점과 크기를 받는 추가 초기화 메서드를 제공할 수 있다:

```swift
extension Rect {
    init(center: Point, size: Size) {
        let originX = center.x - (size.width / 2)
        let originY = center.y - (size.height / 2)
        self.init(origin: Point(x: originX, y: originY), size: size)
    }
}
```

<!--
  - test: `extensionsInitializers`

  ```swifttest
  -> extension Rect {
        init(center: Point, size: Size) {
           let originX = center.x - (size.width / 2)
           let originY = center.y - (size.height / 2)
           self.init(origin: Point(x: originX, y: originY), size: size)
        }
     }
  ```
-->

이 새로운 초기화 메서드는 제공된 `center` 점과 `size` 값을 기반으로 적절한 원점을 계산하는 것으로 시작한다. 그런 다음 구조체의 자동 멤버별 초기화 메서드 `init(origin:size:)`를 호출해 새로운 원점과 크기 값을 적절한 프로퍼티에 저장한다:

```swift
let centerRect = Rect(center: Point(x: 4.0, y: 4.0),
    size: Size(width: 3.0, height: 3.0))
// centerRect의 원점은 (2.5, 2.5)이고 크기는 (3.0, 3.0)이다.
```

<!--
  - test: `extensionsInitializers`

  ```swifttest
  -> let centerRect = Rect(center: Point(x: 4.0, y: 4.0),
        size: Size(width: 3.0, height: 3.0))
  /> centerRect의 원점은 (\(centerRect.origin.x), \(centerRect.origin.y))이고 크기는 (\(centerRect.size.width), \(centerRect.size.height))이다.
  </ centerRect의 원점은 (2.5, 2.5)이고 크기는 (3.0, 3.0)이다.
  ```
-->

> 참고: 익스텐션으로 새로운 초기화 메서드를 제공하는 경우, 초기화 메서드가 완료된 시점에 각 인스턴스가 완전히 초기화되도록 해야 한다.


## 메서드

익스텐션을 사용하면 기존 타입에 새로운 인스턴스 메서드와 타입 메서드를 추가할 수 있다. 다음 예제는 `Int` 타입에 `repetitions`라는 새로운 인스턴스 메서드를 추가한다:

```swift
extension Int {
    func repetitions(task: () -> Void) {
        for _ in 0..<self {
            task()
        }
    }
}
```

<!--
  - test: `extensionsInstanceMethods`

  ```swifttest
  -> extension Int {
        func repetitions(task: () -> Void) {
           for _ in 0..<self {
              task()
           }
        }
     }
  ```
-->

`repetitions(task:)` 메서드는 `() -> Void` 타입의 단일 인자를 받는다. 이는 매개변수가 없고 반환 값도 없는 함수를 나타낸다.

이 익스텐션을 정의한 후에는 임의의 정수에서 `repetitions(task:)` 메서드를 호출하여 작업을 여러 번 수행할 수 있다:

```swift
3.repetitions {
    print("Hello!")
}
// Hello!
// Hello!
// Hello!
```

<!--
  - test: `extensionsInstanceMethods`

  ```swifttest
  -> 3.repetitions {
        print("Hello!")
     }
  </ Hello!
  </ Hello!
  </ Hello!
  ```
-->


### 인스턴스 메서드의 뮤테이션

익스텐션을 통해 추가된 인스턴스 메서드는 인스턴스 자체를 수정(또는 *뮤테이트*)할 수도 있다. `self` 또는 그 속성을 수정하는 구조체와 열거형 메서드는 원래 구현에서의 뮤테이팅 메서드와 마찬가지로 인스턴스 메서드를 `mutating`으로 표시해야 한다.

아래 예제는 Swift의 `Int` 타입에 새로운 뮤테이팅 메서드 `square`를 추가한다. 이 메서드는 원래 값을 제곱한다:

```swift
extension Int {
    mutating func square() {
        self = self * self
    }
}
var someInt = 3
someInt.square()
// someInt is now 9
```

<!--
  - test: `extensionsInstanceMethods`

  ```swifttest
  -> extension Int {
        mutating func square() {
           self = self * self
        }
     }
  -> var someInt = 3
  -> someInt.square()
  /> someInt is now \(someInt)
  </ someInt is now 9
  ```
-->


## 서브스크립트

익스텐션을 사용하면 기존 타입에 새로운 서브스크립트를 추가할 수 있다. 이 예제는 Swift의 기본 `Int` 타입에 정수 서브스크립트를 추가한다. 이 서브스크립트 `[n]`은 숫자의 오른쪽에서 `n`번째 자리의 십진수 값을 반환한다:

- `123456789[0]`은 `9`를 반환
- `123456789[1]`은 `8`을 반환

...이런 식으로 동작한다:

```swift
extension Int {
    subscript(digitIndex: Int) -> Int {
        var decimalBase = 1
        for _ in 0..<digitIndex {
            decimalBase *= 10
        }
        return (self / decimalBase) % 10
    }
}
746381295[0]
// 5를 반환
746381295[1]
// 9를 반환
746381295[2]
// 2를 반환
746381295[8]
// 7를 반환
```

<!--
  - test: `extensionsSubscripts`

  ```swifttest
  -> extension Int {
        subscript(digitIndex: Int) -> Int {
           var decimalBase = 1
           for _ in 0..<digitIndex {
              decimalBase *= 10
           }
           return (self / decimalBase) % 10
        }
     }
  >> let r0 =
  -> 746381295[0]
  /> returns \(r0)
  </ returns 5
  >> let r1 =
  -> 746381295[1]
  /> returns \(r1)
  </ returns 9
  >> let r2 =
  -> 746381295[2]
  /> returns \(r2)
  </ returns 2
  >> let r3 =
  -> 746381295[8]
  /> returns \(r3)
  </ returns 7
  ```
-->

<!--
  Rewrite the above to avoid bare expressions.
  Tracking bug is <rdar://problem/35301593>
-->

<!--
  TODO: Replace the for loop above with an exponent,
  if/when integer exponents land in the stdlib.
  Darwin's pow() function is only for floating point.
-->

만약 `Int` 값이 요청한 인덱스에 충분한 자릿수를 가지고 있지 않다면, 서브스크립트 구현은 `0`을 반환한다. 마치 숫자의 왼쪽에 0이 채워진 것처럼 동작한다:

```swift
746381295[9]
// 0을 반환, 마치 다음을 요청한 것처럼:
0746381295[9]
```

<!--
  - test: `extensionsSubscripts`

  ```swifttest
  >> let r4 =
  -> 746381295[9]
  /> returns \(r4), as if you had requested:
  </ returns 0, as if you had requested:
  >> let r5 =
  -> 0746381295[9]
  ```
-->

<!--
  TODO: provide an explanation of this example
-->

<!--
  Rewrite the above to avoid bare expressions.
  Tracking bug is <rdar://problem/35301593>
-->


## 중첩 타입

익스텐션은 기존 클래스, 구조체, 열거형에 새로운 중첩 타입을 추가할 수 있다:

```swift
extension Int {
    enum Kind {
        case negative, zero, positive
    }
    var kind: Kind {
        switch self {
        case 0:
            return .zero
        case let x where x > 0:
            return .positive
        default:
            return .negative
        }
    }
}
```

<!--
  - test: `extensionsNestedTypes`

  ```swifttest
  -> extension Int {
        enum Kind {
           case negative, zero, positive
        }
        var kind: Kind {
           switch self {
              case 0:
                 return .zero
              case let x where x > 0:
                 return .positive
              default:
                 return .negative
           }
        }
     }
  ```
-->

이 예제는 `Int` 타입에 새로운 중첩 열거형을 추가한다. 이 열거형은 `Kind`라고 불리며, 특정 정수가 어떤 종류의 숫자를 나타내는지 표현한다. 구체적으로, 숫자가 음수인지, 0인지, 양수인지를 나타낸다.

이 예제는 또한 `Int` 타입에 `kind`라는 새로운 계산 프로퍼티를 추가한다. 이 프로퍼티는 해당 정수에 맞는 `Kind` 열거형 케이스를 반환한다.

이 중첩 열거형은 이제 모든 `Int` 값과 함께 사용할 수 있다:

```swift
func printIntegerKinds(_ numbers: [Int]) {
    for number in numbers {
        switch number.kind {
        case .negative:
            print("- ", terminator: "")
        case .zero:
            print("0 ", terminator: "")
        case .positive:
            print("+ ", terminator: "")
        }
    }
    print("")
}
printIntegerKinds([3, 19, -27, 0, -6, 0, 7])
// Prints "+ + - 0 - 0 + "
```

<!--
  - test: `extensionsNestedTypes`

  ```swifttest
  -> func printIntegerKinds(_ numbers: [Int]) {
        for number in numbers {
           switch number.kind {
              case .negative:
                 print("- ", terminator: "")
              case .zero:
                 print("0 ", terminator: "")
              case .positive:
                 print("+ ", terminator: "")
           }
        }
        print("")
     }
  -> printIntegerKinds([3, 19, -27, 0, -6, 0, 7])
  << + + - 0 - 0 +
  // Prints "+ + - 0 - 0 + "
  ```
-->

<!--
  Workaround for rdar://26016325
-->

이 함수인 `printIntegerKinds(_:)`는 `Int` 값의 배열을 입력받아 각 값을 순회한다. 배열의 각 정수에 대해, 함수는 해당 정수의 `kind` 계산 프로퍼티를 확인하고 적절한 설명을 출력한다.

> 참고: `number.kind`는 이미 `Int.Kind` 타입으로 알려져 있다. 따라서 `switch` 문 내에서 모든 `Int.Kind` 케이스 값을 축약형으로 작성할 수 있다. 예를 들어, `Int.Kind.negative` 대신 `.negative`로 작성할 수 있다.

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


