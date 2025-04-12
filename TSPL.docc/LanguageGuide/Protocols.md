# 프로토콜

특정 타입이 반드시 구현해야 하는 요구사항을 정의한다.

*프로토콜*은 특정 작업이나 기능을 수행하기 위해 필요한 메서드, 프로퍼티, 그리고 기타 요구사항에 대한 청사진을 정의한다. 클래스, 구조체, 열거형은 이 프로토콜을 *채택*하여 해당 요구사항을 실제로 구현할 수 있다. 프로토콜의 요구사항을 충족하는 모든 타입은 해당 프로토콜을 *준수*한다고 말한다.

프로토콜은 준수 타입이 반드시 구현해야 하는 요구사항을 지정할 뿐만 아니라, 이를 확장하여 일부 요구사항을 구현하거나 준수 타입이 활용할 수 있는 추가 기능을 제공할 수도 있다.

<!--
  FIXME: 프로토콜은 초기화 구문도 지원할 수 있어야 하며, 현재 이를 작성할 수는 있지만
  <rdar://problem/13695680> 프로토콜의 생성자 요구사항(NSCoding에 필요) 문제로 인해 작동하지 않는다.
  이 문제가 해결되면 이에 대해 작성해야 할 것이다.
  UPDATE: 사실, 현재 이 기능을 사용할 수는 있지만 제네릭 함수 내에서만 가능하며,
  프로토콜 타입과 함께 일반적으로 사용할 수는 없다.
  이 기능이 더 일반적으로 작동할 때까지 이 장에서 언급할지 여부는 확실하지 않다.
-->


## 프로토콜 문법

프로토콜은 클래스, 구조체, 열거형과 매우 유사한 방식으로 정의한다:

```swift
protocol SomeProtocol {
    // 프로토콜 정의가 여기에 위치한다
}
```

<!--
  - test: `protocolSyntax`

  ```swifttest
  -> protocol SomeProtocol {
        // 프로토콜 정의가 여기에 위치한다
     }
  ```
-->

커스텀 타입은 특정 프로토콜을 채택한다고 선언할 때, 타입 이름 뒤에 콜론을 붙이고 프로토콜 이름을 적는다. 여러 프로토콜을 채택할 경우 쉼표로 구분한다:

```swift
struct SomeStructure: FirstProtocol, AnotherProtocol {
    // 구조체 정의가 여기에 위치한다
}
```

<!--
  - test: `protocolSyntax`

  ```swifttest
  >> protocol FirstProtocol {}
  >> protocol AnotherProtocol {}
  -> struct SomeStructure: FirstProtocol, AnotherProtocol {
        // 구조체 정의가 여기에 위치한다
     }
  ```
-->

클래스가 슈퍼클래스를 가지고 있다면, 슈퍼클래스 이름을 프로토콜 목록 앞에 적고 쉼표로 구분한다:

```swift
class SomeClass: SomeSuperclass, FirstProtocol, AnotherProtocol {
    // 클래스 정의가 여기에 위치한다
}
```

<!--
  - test: `protocolSyntax`

  ```swifttest
  >> class SomeSuperclass {}
  -> class SomeClass: SomeSuperclass, FirstProtocol, AnotherProtocol {
        // 클래스 정의가 여기에 위치한다
     }
  ```
-->

> 참고: 프로토콜도 타입이기 때문에, 이름은 대문자로 시작한다(예: `FullyNamed`, `RandomNumberGenerator`). 이는 Swift의 다른 타입 이름(예: `Int`, `String`, `Double`)과 일관성을 유지하기 위함이다.


## 프로퍼티 요구사항

프로토콜은 특정 이름과 타입을 가진 인스턴스 프로퍼티나 타입 프로퍼티를 제공하도록 요구할 수 있다. 프로토콜은 프로퍼티가 저장 프로퍼티인지 계산 프로퍼티인지 명시하지 않는다. 단지 프로퍼티 이름과 타입만 지정한다. 또한 프로토콜은 각 프로퍼티가 읽기 전용인지, 읽기와 쓰기가 모두 가능한지를 명시한다.

프로토콜이 프로퍼티를 읽기와 쓰기가 모두 가능하도록 요구한다면, 해당 요구사항은 상수 저장 프로퍼티나 읽기 전용 계산 프로퍼티로는 충족할 수 없다. 프로토콜이 프로퍼티를 읽기 전용으로만 요구한다면, 어떤 종류의 프로퍼티로도 요구사항을 충족할 수 있으며, 코드에 유용하다면 프로퍼티가 쓰기 가능하도록 구현해도 문제없다.

프로퍼티 요구사항은 항상 `var` 키워드로 선언하며, 읽기와 쓰기가 모두 가능한 프로퍼티는 타입 선언 뒤에 `{ get set }`을, 읽기 전용 프로퍼티는 `{ get }`을 추가해 표시한다.

```swift
protocol SomeProtocol {
    var mustBeSettable: Int { get set }
    var doesNotNeedToBeSettable: Int { get }
}
```

<!--
  - test: `instanceProperties`

  ```swifttest
  -> protocol SomeProtocol {
        var mustBeSettable: Int { get set }
        var doesNotNeedToBeSettable: Int { get }
     }
  ```
-->

프로토콜에서 타입 프로퍼티 요구사항을 정의할 때는 항상 `static` 키워드를 붙인다. 이 규칙은 클래스에서 타입 프로퍼티 요구사항을 구현할 때 `class`나 `static` 키워드를 사용할 수 있더라도 동일하게 적용된다.

```swift
protocol AnotherProtocol {
    static var someTypeProperty: Int { get set }
}
```

<!--
  - test: `instanceProperties`

  ```swifttest
  -> protocol AnotherProtocol {
        static var someTypeProperty: Int { get set }
     }
  ```
-->

다음은 단일 인스턴스 프로퍼티 요구사항을 가진 프로토콜의 예시다.

```swift
protocol FullyNamed {
    var fullName: String { get }
}
```

<!--
  - test: `instanceProperties`

  ```swifttest
  -> protocol FullyNamed {
        var fullName: String { get }
     }
  ```
-->

`FullyNamed` 프로토콜은 해당 타입이 완전한 이름을 제공하도록 요구한다. 프로토콜은 타입의 다른 특성에 대해 아무것도 명시하지 않는다. 단지 타입이 자신의 전체 이름을 제공할 수 있어야 한다는 점만 요구한다. 이 프로토콜은 `FullyNamed` 타입이 `String` 타입의 `fullName`이라는 읽기 전용 인스턴스 프로퍼티를 가져야 한다고 명시한다.

다음은 `FullyNamed` 프로토콜을 채택하고 준수하는 간단한 구조체의 예시다.

```swift
struct Person: FullyNamed {
    var fullName: String
}
let john = Person(fullName: "John Appleseed")
// john.fullName은 "John Appleseed"이다.
```

<!--
  - test: `instanceProperties`

  ```swifttest
  -> struct Person: FullyNamed {
        var fullName: String
     }
  -> let john = Person(fullName: "John Appleseed")
  /> john.fullName is \"\(john.fullName)\"
  </ john.fullName is "John Appleseed"
  ```
-->

이 예시는 `Person`이라는 구조체를 정의하며, 특정 이름을 가진 사람을 나타낸다. 구조체 정의의 첫 줄에서 `FullyNamed` 프로토콜을 채택한다고 명시한다.

`Person`의 각 인스턴스는 `String` 타입의 `fullName`이라는 단일 저장 프로퍼티를 가진다. 이는 `FullyNamed` 프로토콜의 단일 요구사항과 일치하며, `Person`이 프로토콜을 올바르게 준수한다는 의미이다. (Swift는 프로토콜 요구사항이 충족되지 않으면 컴파일 시점에 오류를 발생시킨다.)

다음은 `FullyNamed` 프로토콜을 채택하고 준수하는 더 복잡한 클래스의 예시다.

```swift
class Starship: FullyNamed {
    var prefix: String?
    var name: String
    init(name: String, prefix: String? = nil) {
        self.name = name
        self.prefix = prefix
    }
    var fullName: String {
        return (prefix != nil ? prefix! + " " : "") + name
    }
}
var ncc1701 = Starship(name: "Enterprise", prefix: "USS")
// ncc1701.fullName은 "USS Enterprise"이다.
```

<!--
  - test: `instanceProperties`

  ```swifttest
  -> class Starship: FullyNamed {
        var prefix: String?
        var name: String
        init(name: String, prefix: String? = nil) {
           self.name = name
           self.prefix = prefix
        }
        var fullName: String {
           return (prefix != nil ? prefix! + " " : "") + name
        }
     }
  -> var ncc1701 = Starship(name: "Enterprise", prefix: "USS")
  /> ncc1701.fullName is \"\(ncc1701.fullName)\"
  </ ncc1701.fullName is "USS Enterprise"
  ```
-->

이 클래스는 `fullName` 프로퍼티 요구사항을 우주선의 계산된 읽기 전용 프로퍼티로 구현한다. 각 `Starship` 클래스 인스턴스는 필수 `name`과 선택적 `prefix`를 저장한다. `fullName` 프로퍼티는 `prefix` 값이 존재하면 이를 사용하고, `name` 앞에 추가해 우주선의 전체 이름을 생성한다.

<!--
  TODO: add some advice on how protocols should be named
-->


## 메서드 요구사항

프로토콜은 특정 인스턴스 메서드와 타입 메서드를 구현하도록 요구할 수 있다. 이러한 메서드는 일반 인스턴스 메서드와 타입 메서드와 동일한 방식으로 프로토콜 정의의 일부로 작성되지만, 중괄호나 메서드 본문은 포함하지 않는다. 일반 메서드와 마찬가지로 가변 인자를 허용하지만, 프로토콜 정의 내에서는 메서드 매개변수에 기본값을 지정할 수 없다.

타입 프로퍼티 요구사항과 마찬가지로, 프로토콜에 정의된 타입 메서드 요구사항에는 항상 `static` 키워드를 붙인다. 이는 클래스에서 구현할 때 `class` 또는 `static` 키워드를 사용하더라도 마찬가지로 적용된다:

```swift
protocol SomeProtocol {
    static func someTypeMethod()
}
```

<!--
  - test: `typeMethods`

  ```swifttest
  -> protocol SomeProtocol {
        static func someTypeMethod()
     }
  ```
-->

다음 예제는 단일 인스턴스 메서드 요구사항을 가진 프로토콜을 정의한다:

```swift
protocol RandomNumberGenerator {
    func random() -> Double
}
```

<!--
  - test: `protocols`

  ```swifttest
  -> protocol RandomNumberGenerator {
        func random() -> Double
     }
  ```
-->

이 프로토콜인 `RandomNumberGenerator`는 해당 프로토콜을 준수하는 모든 타입이 `random`이라는 인스턴스 메서드를 구현하도록 요구한다. 이 메서드는 호출될 때마다 `Double` 값을 반환한다. 프로토콜에 명시되지는 않았지만, 이 값은 `0.0` 이상 `1.0` 미만의 숫자일 것으로 가정한다.

`RandomNumberGenerator` 프로토콜은 각 난수가 어떻게 생성되는지에 대해 어떤 가정도 하지 않는다. 단지 새로운 난수를 생성하기 위한 표준 방법을 제공할 것을 요구할 뿐이다.

다음은 `RandomNumberGenerator` 프로토콜을 채택하고 준수하는 클래스의 구현 예제다. 이 클래스는 *선형 합동 생성기*라고 알려진 의사 난수 생성 알고리즘을 구현한다:

```swift
class LinearCongruentialGenerator: RandomNumberGenerator {
    var lastRandom = 42.0
    let m = 139968.0
    let a = 3877.0
    let c = 29573.0
    func random() -> Double {
        lastRandom = ((lastRandom * a + c)
            .truncatingRemainder(dividingBy:m))
        return lastRandom / m
    }
}
let generator = LinearCongruentialGenerator()
print("Here's a random number: \(generator.random())")
// Prints "Here's a random number: 0.3746499199817101"
print("And another one: \(generator.random())")
// Prints "And another one: 0.729023776863283"
```

<!--
  - test: `protocols`

  ```swifttest
  -> class LinearCongruentialGenerator: RandomNumberGenerator {
        var lastRandom = 42.0
        let m = 139968.0
        let a = 3877.0
        let c = 29573.0
        func random() -> Double {
           lastRandom = ((lastRandom * a + c)
               .truncatingRemainder(dividingBy:m))
           return lastRandom / m
        }
     }
  -> let generator = LinearCongruentialGenerator()
  -> print("Here's a random number: \(generator.random())")
  <- Here's a random number: 0.3746499199817101
  -> print("And another one: \(generator.random())")
  <- And another one: 0.729023776863283
  ```
-->


## 뮤테이션 메서드 요구사항

때로는 메서드가 자신이 속한 인스턴스를 수정(또는 *뮤테이트*)해야 할 필요가 있다. 값 타입(구조체와 열거형)의 인스턴스 메서드의 경우, `mutating` 키워드를 `func` 키워드 앞에 붙여 해당 메서드가 인스턴스와 그 속성을 수정할 수 있음을 나타낸다. 이 과정은 <doc:Methods#Modifying-Value-Types-from-Within-Instance-Methods>에서 자세히 설명한다.

프로토콜의 인스턴스 메서드 요구사항을 정의할 때, 해당 프로토콜을 채택한 모든 타입의 인스턴스를 뮤테이트할 의도가 있다면, 메서드를 `mutating` 키워드로 표시해야 한다. 이렇게 하면 구조체와 열거형이 프로토콜을 채택하고 해당 메서드 요구사항을 충족할 수 있다.

> 참고: 프로토콜 인스턴스 메서드 요구사항을 `mutating`으로 표시했다면, 클래스에서 해당 메서드를 구현할 때 `mutating` 키워드를 작성할 필요가 없다. `mutating` 키워드는 구조체와 열거형에서만 사용한다.

아래 예제는 `Togglable`이라는 프로토콜을 정의한다. 이 프로토콜은 `toggle`이라는 단일 인스턴스 메서드 요구사항을 정의한다. 이름에서 알 수 있듯이, `toggle()` 메서드는 일반적으로 해당 타입의 속성을 수정하여 상태를 토글하거나 반전시키는 역할을 한다.

`toggle()` 메서드는 `Togglable` 프로토콜 정의의 일부로 `mutating` 키워드로 표시된다. 이는 메서드가 호출될 때 프로토콜을 준수하는 인스턴스의 상태를 뮤테이트할 것으로 예상됨을 나타낸다:

```swift
protocol Togglable {
    mutating func toggle()
}
```

<!--
  - test: `mutatingRequirements`

  ```swifttest
  -> protocol Togglable {
        mutating func toggle()
     }
  ```
-->

구조체나 열거형에서 `Togglable` 프로토콜을 구현할 때, `toggle()` 메서드를 `mutating`으로 표시하여 프로토콜을 준수할 수 있다.

아래 예제는 `OnOffSwitch`라는 열거형을 정의한다. 이 열거형은 `on`과 `off`라는 두 가지 상태 사이를 토글한다. 열거형의 `toggle` 구현은 `Togglable` 프로토콜의 요구사항과 일치하도록 `mutating`으로 표시된다:

```swift
enum OnOffSwitch: Togglable {
    case off, on
    mutating func toggle() {
        switch self {
        case .off:
            self = .on
        case .on:
            self = .off
        }
    }
}
var lightSwitch = OnOffSwitch.off
lightSwitch.toggle()
// lightSwitch is now equal to .on
```

<!--
  - test: `mutatingRequirements`

  ```swifttest
  -> enum OnOffSwitch: Togglable {
        case off, on
        mutating func toggle() {
           switch self {
              case .off:
                 self = .on
              case .on:
                 self = .off
           }
        }
     }
  -> var lightSwitch = OnOffSwitch.off
  -> lightSwitch.toggle()
  // lightSwitch is now equal to .on
  ```
-->


## 초기화 요구사항

프로토콜은 특정 초기화 메서드를 구현하도록 요구할 수 있다. 이 초기화 메서드는 일반 초기화 메서드를 정의하는 방식과 동일하게 프로토콜 정의의 일부로 작성한다. 단, 중괄호나 초기화 본문은 작성하지 않는다:

```swift
protocol SomeProtocol {
    init(someParameter: Int)
}
```

<!--
  - test: `initializers`

  ```swifttest
  -> protocol SomeProtocol {
        init(someParameter: Int)
     }
  ```
-->


### 프로토콜 초기화 요구사항의 클래스 구현

프로토콜의 초기화 요구사항을 준수하는 클래스에서는 이를 지정 초기화자(designated initializer)나 편의 초기화자(convenience initializer)로 구현할 수 있다. 두 경우 모두 `required` 수식어를 사용해 초기화자를 표시해야 한다:

```swift
class SomeClass: SomeProtocol {
    required init(someParameter: Int) {
        // 초기화자 구현
    }
}
```

`required` 수식어를 사용하면 해당 클래스를 상속하는 모든 서브클래스에서 초기화 요구사항을 명시적으로 구현하거나 상속받도록 보장한다. 이를 통해 서브클래스도 프로토콜을 준수할 수 있다.

초기화자에 대한 더 자세한 내용은 <doc:Initialization#Required-Initializers>를 참고한다.

> 참고: `final` 수식어가 붙은 클래스에서는 `required` 수식어를 사용할 필요가 없다. `final` 클래스는 상속할 수 없기 때문이다. `final` 수식어에 대한 더 자세한 내용은 <doc:Inheritance#Preventing-Overrides>를 참고한다.

서브클래스가 슈퍼클래스의 지정 초기화자를 재정의하면서 동시에 프로토콜의 초기화 요구사항을 구현해야 하는 경우, `required`와 `override` 수식어를 모두 사용해야 한다:

```swift
protocol SomeProtocol {
    init()
}

class SomeSuperClass {
    init() {
        // 초기화자 구현
    }
}

class SomeSubClass: SomeSuperClass, SomeProtocol {
    // SomeProtocol 준수를 위한 "required"; SomeSuperClass 재정의를 위한 "override"
    required override init() {
        // 초기화자 구현
    }
}
```


### 실패 가능한 초기화 요구사항

프로토콜은 준수 타입에 대해 실패 가능한 초기화 요구사항을 정의할 수 있다. 이는 <doc:Initialization#Failable-Initializers>에서 설명한 바와 같다.

실패 가능한 초기화 요구사항은 준수 타입의 실패 가능한 초기화 메서드 또는 실패하지 않는 초기화 메서드로 충족할 수 있다. 반면, 실패하지 않는 초기화 요구사항은 실패하지 않는 초기화 메서드 또는 암시적으로 언래핑된 실패 가능한 초기화 메서드로 충족할 수 있다.

<!--
  - test: `failableRequirementCanBeSatisfiedByFailableInitializer`

  ```swifttest
  -> protocol P { init?(i: Int) }
  -> class C: P { required init?(i: Int) {} }
  -> struct S: P { init?(i: Int) {} }
  ```
-->

<!--
  - test: `failableRequirementCanBeSatisfiedByIUOInitializer`

  ```swifttest
  -> protocol P { init?(i: Int) }
  -> class C: P { required init!(i: Int) {} }
  -> struct S: P { init!(i: Int) {} }
  ```
-->

<!--
  - test: `iuoRequirementCanBeSatisfiedByFailableInitializer`

  ```swifttest
  -> protocol P { init!(i: Int) }
  -> class C: P { required init?(i: Int) {} }
  -> struct S: P { init?(i: Int) {} }
  ```
-->

<!--
  - test: `iuoRequirementCanBeSatisfiedByIUOInitializer`

  ```swifttest
  -> protocol P { init!(i: Int) }
  -> class C: P { required init!(i: Int) {} }
  -> struct S: P { init!(i: Int) {} }
  ```
-->

<!--
  - test: `failableRequirementCanBeSatisfiedByNonFailableInitializer`

  ```swifttest
  -> protocol P { init?(i: Int) }
  -> class C: P { required init(i: Int) {} }
  -> struct S: P { init(i: Int) {} }
  ```
-->

<!--
  - test: `iuoRequirementCanBeSatisfiedByNonFailableInitializer`

  ```swifttest
  -> protocol P { init!(i: Int) }
  -> class C: P { required init(i: Int) {} }
  -> struct S: P { init(i: Int) {} }
  ```
-->

<!--
  - test: `nonFailableRequirementCanBeSatisfiedByNonFailableInitializer`

  ```swifttest
  -> protocol P { init(i: Int) }
  -> class C: P { required init(i: Int) {} }
  -> struct S: P { init(i: Int) {} }
  ```
-->

<!--
  - test: `nonFailableRequirementCanBeSatisfiedByIUOInitializer`

  ```swifttest
  -> protocol P { init(i: Int) }
  -> class C: P { required init!(i: Int) {} }
  -> struct S: P { init!(i: Int) {} }
  ```
-->


## 프로토콜을 타입으로 사용하기

프로토콜 자체는 실제 기능을 구현하지 않는다. 하지만 프로토콜을 코드에서 타입으로 사용할 수 있다.

프로토콜을 타입으로 사용하는 가장 일반적인 방법은 프로토콜을 제네릭 제약 조건으로 활용하는 것이다. 제네릭 제약 조건이 있는 코드는 해당 프로토콜을 준수하는 모든 타입과 함께 작동하며, 구체적인 타입은 API를 사용하는 코드에서 선택한다. 예를 들어, 인자를 받는 함수를 호출할 때 그 인자의 타입이 제네릭이라면, 호출자가 타입을 결정한다.

불투명 타입(opaque type)을 사용하는 코드는 프로토콜을 준수하는 어떤 타입과도 작동한다. 내부 타입은 컴파일 시점에 알려지며, API 구현이 그 타입을 선택한다. 하지만 이 타입의 정체는 API 클라이언트에게 숨겨진다. 불투명 타입을 사용하면 API의 구현 세부사항이 추상화 계층을 통해 유출되는 것을 방지할 수 있다. 예를 들어, 함수의 구체적인 반환 타입을 숨기고 값이 주어진 프로토콜을 준수한다는 점만 보장할 수 있다.

박스형 프로토콜 타입(boxed protocol type)을 사용하는 코드는 런타임에 선택된 프로토콜을 준수하는 모든 타입과 작동한다. 이 런타임 유연성을 지원하기 위해, Swift는 필요한 경우 간접 참조 계층을 추가한다. 이를 *박스*라고 하며, 이는 성능 비용을 수반한다. 이러한 유연성 때문에 Swift는 컴파일 시점에 내부 타입을 알 수 없으며, 이는 프로토콜에서 요구하는 멤버만 접근할 수 있음을 의미한다. 내부 타입의 다른 API에 접근하려면 런타임에 타입 캐스팅이 필요하다.

프로토콜을 제네릭 제약 조건으로 사용하는 방법에 대한 자세한 내용은 <doc:Generics>를 참고한다. 불투명 타입과 박스형 프로토콜 타입에 대한 정보는 <doc:OpaqueTypes>를 확인한다.

<!--
SE-0335의 성능 영향:

실존 타입(existential type)은 구체적인 타입을 사용하는 것보다 훨씬 더 비용이 많이 든다. 프로토콜을 준수하는 모든 타입의 값을 저장할 수 있고, 저장된 값의 타입이 동적으로 변경될 수 있기 때문에, 실존 타입은 값이 인라인 3워드 버퍼에 맞을 정도로 작지 않은 한 동적 메모리가 필요하다. 힙 할당과 참조 카운팅 외에도, 실존 타입을 사용하는 코드는 포인터 간접 참조와 최적화할 수 없는 동적 메서드 디스패치를 수반한다.
-->


## 위임(Delegation)

*위임*은 클래스나 구조체가 특정 책임을 다른 타입의 인스턴스에 넘기는 디자인 패턴이다. 이 패턴은 위임할 책임을 캡슐화한 프로토콜을 정의함으로써 구현된다. 프로토콜을 준수하는 타입(위임자라고 함)은 위임된 기능을 제공할 것을 보장한다. 위임은 특정 작업에 응답하거나, 외부 소스로부터 데이터를 가져오는 데 사용할 수 있다. 이때 외부 소스의 내부 타입을 알 필요가 없다.

아래 예제는 주사위 게임과 게임 진행을 추적하는 위임자를 위한 중첩 프로토콜을 정의한다:

```swift
class DiceGame {
    let sides: Int
    let generator = LinearCongruentialGenerator()
    weak var delegate: Delegate?

    init(sides: Int) {
        self.sides = sides
    }

    func roll() -> Int {
        return Int(generator.random() * Double(sides)) + 1
    }

    func play(rounds: Int) {
        delegate?.gameDidStart(self)
        for round in 1...rounds {
            let player1 = roll()
            let player2 = roll()
            if player1 == player2 {
                delegate?.game(self, didEndRound: round, winner: nil)
            } else if player1 > player2 {
                delegate?.game(self, didEndRound: round, winner: 1)
            } else {
                delegate?.game(self, didEndRound: round, winner: 2)
            }
        }
        delegate?.gameDidEnd(self)
    }

    protocol Delegate: AnyObject {
        func gameDidStart(_ game: DiceGame)
        func game(_ game: DiceGame, didEndRound round: Int, winner: Int?)
        func gameDidEnd(_ game: DiceGame)
    }
}
```

`DiceGame` 클래스는 각 플레이어가 주사위를 굴리고, 더 높은 숫자를 굴린 플레이어가 라운드에서 승리하는 게임을 구현한다. 이 클래스는 주사위 굴림을 위한 난수를 생성하기 위해 이전 장에서 다룬 선형 합동 생성기를 사용한다.

`DiceGame.Delegate` 프로토콜은 주사위 게임의 진행 상황을 추적하기 위해 채택할 수 있다. 이 프로토콜은 항상 주사위 게임의 맥락에서 사용되므로 `DiceGame` 클래스 내부에 중첩되어 있다. 프로토콜은 외부 선언이 제네릭이 아닌 한, 구조체나 클래스와 같은 타입 선언 내부에 중첩될 수 있다. 중첩 타입에 대한 자세한 내용은 <doc:NestedTypes>를 참조한다.

강한 참조 순환을 방지하기 위해 위임자는 약한 참조로 선언된다. 약한 참조에 대한 자세한 내용은 <doc:AutomaticReferenceCounting#Strong-Reference-Cycles-Between-Class-Instances>를 참조한다. 프로토콜을 클래스 전용으로 표시하면 `DiceGame` 클래스가 위임자를 약한 참조로 선언할 수 있다. 클래스 전용 프로토콜은 `AnyObject`를 상속함으로써 표시되며, 이에 대한 자세한 내용은 <doc:Protocols#Class-Only-Protocols>에서 다룬다.

`DiceGame.Delegate`는 게임 진행 상황을 추적하기 위한 세 가지 메서드를 제공한다. 이 세 메서드는 위의 `play(rounds:)` 메서드에 통합되어 있다. `DiceGame` 클래스는 새로운 게임이 시작되거나, 새로운 턴이 시작되거나, 게임이 종료될 때 위임자 메서드를 호출한다.

`delegate` 프로퍼티는 *옵셔널* `DiceGame.Delegate` 타입이므로, `play(rounds:)` 메서드는 위임자 메서드를 호출할 때마다 옵셔널 체이닝을 사용한다. 이는 <doc:OptionalChaining>에서 다룬다. `delegate` 프로퍼티가 nil이면 위임자 호출은 무시된다. `delegate` 프로퍼티가 nil이 아니면 위임자 메서드가 호출되고, `DiceGame` 인스턴스가 매개변수로 전달된다.

다음 예제는 `DiceGame.Delegate` 프로토콜을 채택한 `DiceGameTracker` 클래스를 보여준다:

```swift
class DiceGameTracker: DiceGame.Delegate {
    var playerScore1 = 0
    var playerScore2 = 0
    func gameDidStart(_ game: DiceGame) {
        print("Started a new game")
        playerScore1 = 0
        playerScore2 = 0
    }
    func game(_ game: DiceGame, didEndRound round: Int, winner: Int?) {
        switch winner {
            case 1:
                playerScore1 += 1
                print("Player 1 won round \(round)")
            case 2: playerScore2 += 1
                print("Player 2 won round \(round)")
            default:
                print("The round was a draw")
        }
    }
    func gameDidEnd(_ game: DiceGame) {
        if playerScore1 == playerScore2 {
            print("The game ended in a draw.")
        } else if playerScore1 > playerScore2 {
            print("Player 1 won!")
        } else {
            print("Player 2 won!")
        }
    }
}
```

`DiceGameTracker` 클래스는 `DiceGame.Delegate` 프로토콜이 요구하는 세 가지 메서드를 모두 구현한다. 이 클래스는 새 게임이 시작될 때 두 플레이어의 점수를 초기화하고, 각 라운드가 끝날 때 점수를 업데이트하며, 게임이 끝날 때 승자를 발표한다.

다음은 `DiceGame`과 `DiceGameTracker`가 동작하는 모습이다:

```swift
let tracker = DiceGameTracker()
let game = DiceGame(sides: 6)
game.delegate = tracker
game.play(rounds: 3)
// Started a new game
// Player 2 won round 1
// Player 2 won round 2
// Player 1 won round 3
// Player 2 won!
```


## 확장을 통해 프로토콜 준수성 추가하기

기존 타입의 소스 코드에 접근할 수 없더라도, 확장(extension)을 사용해 새로운 프로토콜을 채택하고 준수하도록 만들 수 있다. 확장은 기존 타입에 새로운 프로퍼티, 메서드, 서브스크립트를 추가할 수 있으므로, 프로토콜이 요구하는 모든 조건을 충족시킬 수 있다. 확장에 대한 더 자세한 내용은 <doc:Extensions>를 참고한다.

> 참고: 타입의 기존 인스턴스는 확장에서 해당 타입에 프로토콜 준수성을 추가하면 자동으로 프로토콜을 채택하고 준수하게 된다.

예를 들어, `TextRepresentable`이라는 프로토콜은 텍스트로 표현할 수 있는 모든 타입이 구현할 수 있다. 이는 타입 자체에 대한 설명이거나, 현재 상태의 텍스트 버전일 수 있다:

```swift
protocol TextRepresentable {
    var textualDescription: String { get }
}
```

<!--
  - test: `protocols`

  ```swifttest
  -> protocol TextRepresentable {
        var textualDescription: String { get }
     }
  ```
-->

이전에 정의한 `Dice` 클래스를 확장해 `TextRepresentable` 프로토콜을 채택하고 준수하도록 만들 수 있다:

```swift
extension Dice: TextRepresentable {
    var textualDescription: String {
        return "A \(sides)-sided dice"
    }
}
```

<!--
  - test: `protocols`

  ```swifttest
  -> extension Dice: TextRepresentable {
        var textualDescription: String {
           return "A \(sides)-sided dice"
        }
     }
  ```
-->

이 확장은 `Dice`가 원래 구현에서 프로토콜을 제공한 것과 동일한 방식으로 새로운 프로토콜을 채택한다. 프로토콜 이름은 타입 이름 뒤에 콜론으로 구분해 추가하며, 프로토콜의 모든 요구 사항을 확장의 중괄호 안에 구현한다.

이제 모든 `Dice` 인스턴스를 `TextRepresentable`로 취급할 수 있다:

```swift
let d12 = Dice(sides: 12, generator: LinearCongruentialGenerator())
print(d12.textualDescription)
// Prints "A 12-sided dice"
```

<!--
  - test: `protocols`

  ```swifttest
  -> let d12 = Dice(sides: 12, generator: LinearCongruentialGenerator())
  -> print(d12.textualDescription)
  <- A 12-sided dice
  ```
-->

마찬가지로, `SnakesAndLadders` 게임 클래스도 확장을 통해 `TextRepresentable` 프로토콜을 채택하고 준수하도록 만들 수 있다:

```swift
extension SnakesAndLadders: TextRepresentable {
    var textualDescription: String {
        return "A game of Snakes and Ladders with \(finalSquare) squares"
    }
}
print(game.textualDescription)
// Prints "A game of Snakes and Ladders with 25 squares"
```

<!--
  - test: `protocols`

  ```swifttest
  -> extension SnakesAndLadders: TextRepresentable {
        var textualDescription: String {
           return "A game of Snakes and Ladders with \(finalSquare) squares"
        }
     }
  -> print(game.textualDescription)
  <- A game of Snakes and Ladders with 25 squares
  ```
-->


### 조건부 프로토콜 준수

제네릭 타입은 특정 조건 하에서만 프로토콜의 요구 사항을 충족할 수 있다. 예를 들어, 타입의 제네릭 파라미터가 프로토콜을 준수할 때가 그렇다. 제네릭 타입이 조건부로 프로토콜을 준수하도록 만들려면, 타입을 확장할 때 제약 조건을 나열하면 된다. 이러한 제약 조건은 프로토콜 이름 뒤에 제네릭 `where` 절을 작성하여 추가한다. 제네릭 `where` 절에 대한 자세한 내용은 <doc:Generics#Generic-Where-Clauses>를 참고한다.

다음 확장은 `Array` 인스턴스가 `TextRepresentable` 프로토콜을 준수하는 타입의 요소를 저장할 때, `Array`가 `TextRepresentable` 프로토콜을 준수하도록 만든다.

```swift
extension Array: TextRepresentable where Element: TextRepresentable {
    var textualDescription: String {
        let itemsAsText = self.map { $0.textualDescription }
        return "[" + itemsAsText.joined(separator: ", ") + "]"
    }
}
let myDice = [d6, d12]
print(myDice.textualDescription)
// Prints "[A 6-sided dice, A 12-sided dice]"
```

<!--
  - test: `protocols`

  ```swifttest
  -> extension Array: TextRepresentable where Element: TextRepresentable {
        var textualDescription: String {
           let itemsAsText = self.map { $0.textualDescription }
           return "[" + itemsAsText.joined(separator: ", ") + "]"
        }
     }
     let myDice = [d6, d12]
  -> print(myDice.textualDescription)
  <- [A 6-sided dice, A 12-sided dice]
  ```
-->


### 익스텐션을 통해 프로토콜 채택 선언하기

타입이 이미 프로토콜의 모든 요구 사항을 충족하지만, 아직 해당 프로토콜을 채택한다고 명시하지 않은 경우, 빈 익스텐션을 사용해 프로토콜을 채택하도록 할 수 있다:

```swift
struct Hamster {
    var name: String
    var textualDescription: String {
        return "A hamster named \(name)"
    }
}
extension Hamster: TextRepresentable {}
```

<!--
  - test: `protocols`

  ```swifttest
  -> struct Hamster {
        var name: String
        var textualDescription: String {
           return "A hamster named \(name)"
        }
     }
  -> extension Hamster: TextRepresentable {}
  ```
-->

이제 `Hamster`의 인스턴스는 `TextRepresentable` 타입이 요구되는 모든 곳에서 사용할 수 있다:

```swift
let simonTheHamster = Hamster(name: "Simon")
let somethingTextRepresentable: TextRepresentable = simonTheHamster
print(somethingTextRepresentable.textualDescription)
// Prints "A hamster named Simon"
```

<!--
  - test: `protocols`

  ```swifttest
  -> let simonTheHamster = Hamster(name: "Simon")
  -> let somethingTextRepresentable: TextRepresentable = simonTheHamster
  -> print(somethingTextRepresentable.textualDescription)
  <- A hamster named Simon
  ```
-->

> 참고: 타입이 프로토콜의 요구 사항을 충족한다고 해서 자동으로 프로토콜을 채택하지는 않는다. 항상 명시적으로 프로토콜 채택을 선언해야 한다.


## 합성 구현을 통한 프로토콜 채택

Swift는 `Equatable`, `Hashable`, `Comparable` 프로토콜에 대해 많은 간단한 경우에 자동으로 프로토콜 준수를 제공한다. 이 합성 구현을 사용하면 프로토콜 요구사항을 직접 구현하기 위해 반복적인 보일러플레이트 코드를 작성할 필요가 없다.

<!--
  아래 URL과 같은 섹션에 직접 연결하는 것은 안정적일 것으로 예상된다.
  해당 섹션이 존재하는 한, 그 토픽 ID도 계속 유지될 것이다.

  Equatable 프로토콜 준수
  https://developer.apple.com/documentation/swift/equatable#2847780

  Hashable 프로토콜 준수
  https://developer.apple.com/documentation/swift/hashable#2849490

  Comparable 프로토콜 준수
  https://developer.apple.com/documentation/swift/comparable#2845320

  ^-- Comparable에 대한 참조 문서에 합성 구현에 대한 논의를 추가해야 한다.
  이는 새로운 내용이기 때문이다.

  위 타입 참조의 일부 정보는 "Adopting Common Protocols" 문서의
  "Conform Automatically to Equatable and Hashable" 섹션에서도 반복된다.
  https://developer.apple.com/documentation/swift/adopting_common_protocols#2991123
-->

Swift는 다음과 같은 커스텀 타입에 대해 `Equatable`의 합성 구현을 제공한다:

- `Equatable` 프로토콜을 준수하는 저장 프로퍼티만 있는 구조체
- `Equatable` 프로토콜을 준수하는 연관 타입만 있는 열거형
- 연관 타입이 없는 열거형

`==` 연산자의 합성 구현을 받으려면, 원래 선언이 포함된 파일에서 `Equatable` 프로토콜을 준수한다고 선언하고, `==` 연산자를 직접 구현하지 않아도 된다. `Equatable` 프로토콜은 `!=` 연산자의 기본 구현을 제공한다.

아래 예제는 `Vector2D` 구조체와 유사한 3차원 위치 벡터 `(x, y, z)`를 위한 `Vector3D` 구조체를 정의한다. `x`, `y`, `z` 프로퍼티가 모두 `Equatable` 타입이기 때문에, `Vector3D`는 동등 연산자의 합성 구현을 받는다.

```swift
struct Vector3D: Equatable {
    var x = 0.0, y = 0.0, z = 0.0
}

let twoThreeFour = Vector3D(x: 2.0, y: 3.0, z: 4.0)
let anotherTwoThreeFour = Vector3D(x: 2.0, y: 3.0, z: 4.0)
if twoThreeFour == anotherTwoThreeFour {
    print("These two vectors are also equivalent.")
}
// Prints "These two vectors are also equivalent."
```

<!--
  - test: `equatable_synthesis`

  ```swifttest
  -> struct Vector3D: Equatable {
        var x = 0.0, y = 0.0, z = 0.0
     }

  -> let twoThreeFour = Vector3D(x: 2.0, y: 3.0, z: 4.0)
  -> let anotherTwoThreeFour = Vector3D(x: 2.0, y: 3.0, z: 4.0)
  -> if twoThreeFour == anotherTwoThreeFour {
         print("These two vectors are also equivalent.")
     }
  <- These two vectors are also equivalent.
  ```
-->

<!--
  "Adopting Common Protocols" 문서에서 여기로 교차 참조를 추가해야 한다.
  https://developer.apple.com/documentation/swift/adopting_common_protocols

  문서의 논의에서는 연관 값이 없는 열거형은 프로토콜 준수를 선언하지 않아도
  Equatable 및 Hashable을 준수한다고 언급한다.
-->

Swift는 다음과 같은 커스텀 타입에 대해 `Hashable`의 합성 구현을 제공한다:

- `Hashable` 프로토콜을 준수하는 저장 프로퍼티만 있는 구조체
- `Hashable` 프로토콜을 준수하는 연관 타입만 있는 열거형
- 연관 타입이 없는 열거형

`hash(into:)` 메서드의 합성 구현을 받으려면, 원래 선언이 포함된 파일에서 `Hashable` 프로토콜을 준수한다고 선언하고, `hash(into:)` 메서드를 직접 구현하지 않아도 된다.

Swift는 원시 값이 없는 열거형에 대해 `Comparable`의 합성 구현을 제공한다. 열거형에 연관 타입이 있는 경우, 모든 연관 타입이 `Comparable` 프로토콜을 준수해야 한다. `<` 연산자의 합성 구현을 받으려면, 원래 열거형 선언이 포함된 파일에서 `Comparable` 프로토콜을 준수한다고 선언하고, `<` 연산자를 직접 구현하지 않아도 된다. `Comparable` 프로토콜의 기본 구현은 `<=`, `>`, `>=` 연산자를 제공한다.

아래 예제는 초보자, 중급자, 전문가를 위한 `SkillLevel` 열거형을 정의한다. 전문가는 추가로 별의 개수에 따라 순위가 매겨진다.

```swift
enum SkillLevel: Comparable {
    case beginner
    case intermediate
    case expert(stars: Int)
}
var levels = [SkillLevel.intermediate, SkillLevel.beginner,
              SkillLevel.expert(stars: 5), SkillLevel.expert(stars: 3)]
for level in levels.sorted() {
    print(level)
}
// Prints "beginner"
// Prints "intermediate"
// Prints "expert(stars: 3)"
// Prints "expert(stars: 5)"
```

<!--
  - test: `comparable-enum-synthesis`

  ```swifttest
  -> enum SkillLevel: Comparable {
         case beginner
         case intermediate
         case expert(stars: Int)
     }
  -> var levels = [SkillLevel.intermediate, SkillLevel.beginner,
                   SkillLevel.expert(stars: 5), SkillLevel.expert(stars: 3)]
  -> for level in levels.sorted() {
         print(level)
     }
  <- beginner
  <- intermediate
  <- expert(stars: 3)
  <- expert(stars: 5)
  ```
-->

<!--
  위 예제는 전체 배열을 출력하는 대신 반복하여 출력한다.
  배열을 출력하면 각 요소의 디버그 설명이 출력되기 때문이다.
  이는 temp123908.SkillLevel.expert(5)와 같이 보여 읽기 불편하다.
-->

<!--
  - test: `no-synthesized-comparable-for-raw-value-enum`

  ```swifttest
  >> enum E: Int, Comparable {
  >>     case ten = 10
  >>     case twelve = 12
  >> }
  !$ error: type 'E' does not conform to protocol 'Comparable'
  !! enum E: Int, Comparable {
  !!      ^
  !$ note: enum declares raw type 'Int', preventing synthesized conformance of 'E' to 'Comparable'
  !! enum E: Int, Comparable {
  !!         ^
  !$ note: candidate would match if 'E' conformed to 'FloatingPoint'
  !! public static func < (lhs: Self, rhs: Self) -> Bool
  !!                        ^
  !$ note: candidate has non-matching type '<Self, Other> (Self, Other) -> Bool'
  !! public static func < <Other>(lhs: Self, rhs: Other) -> Bool where Other : BinaryInteger
  !!                        ^
  !$ note: candidate would match if 'E' conformed to '_Pointer'
  !! public static func < (lhs: Self, rhs: Self) -> Bool
  !!                        ^
  !$ note: candidate would match if 'E' conformed to '_Pointer'
  !! @inlinable public static func < <Other>(lhs: Self, rhs: Other) -> Bool where Other : _Pointer
  !!                                   ^
  !$ note: candidate has non-matching type '<Self> (Self, Self) -> Bool'
  !! @inlinable public static func < (x: Self, y: Self) -> Bool
  !!                                   ^
  !$ note: candidate would match if 'E' conformed to 'StringProtocol'
  !! @inlinable public static func < <RHS>(lhs: Self, rhs: RHS) -> Bool where RHS : StringProtocol
  !!                                   ^
  !$ note: protocol requires function '<' with type '(E, E) -> Bool'
  !! static func < (lhs: Self, rhs: Self) -> Bool
  !!                 ^
  ```
-->


## 프로토콜 타입 컬렉션

프로토콜은 배열이나 딕셔너리와 같은 컬렉션에 저장할 타입으로 사용할 수 있다. 이는 <doc:Protocols#Protocols-as-Types>에서 언급한 내용과 같다. 다음 예제는 `TextRepresentable` 타입의 배열을 생성한다:

```swift
let things: [TextRepresentable] = [game, d12, simonTheHamster]
```

<!--
  - test: `protocols`

  ```swifttest
  -> let things: [TextRepresentable] = [game, d12, simonTheHamster]
  ```
-->

이제 배열의 각 항목을 순회하며 텍스트 설명을 출력할 수 있다:

```swift
for thing in things {
    print(thing.textualDescription)
}
// A game of Snakes and Ladders with 25 squares
// A 12-sided dice
// A hamster named Simon
```

<!--
  - test: `protocols`

  ```swifttest
  -> for thing in things {
        print(thing.textualDescription)
     }
  </ A game of Snakes and Ladders with 25 squares
  </ A 12-sided dice
  </ A hamster named Simon
  ```
-->

여기서 `thing` 상수는 `TextRepresentable` 타입이다. 실제 인스턴스가 `Dice`, `DiceGame`, 또는 `Hamster` 타입일지라도 `thing`은 이 타입들 중 하나가 아니다. 그럼에도 불구하고 `thing`이 `TextRepresentable` 타입이므로, `textualDescription` 프로퍼티에 접근하는 것이 안전하다. `TextRepresentable`을 준수하는 모든 타입은 `textualDescription` 프로퍼티를 가지고 있기 때문이다.


## 프로토콜 상속

프로토콜은 하나 이상의 다른 프로토콜을 *상속*할 수 있으며, 상속받은 요구사항 위에 추가 요구사항을 정의할 수 있다. 프로토콜 상속 구문은 클래스 상속 구문과 유사하지만, 여러 프로토콜을 쉼표로 구분하여 나열할 수 있다는 점이 다르다:

```swift
protocol InheritingProtocol: SomeProtocol, AnotherProtocol {
    // 프로토콜 정의
}
```

<!--
  - test: `protocols`

  ```swifttest
  >> protocol SomeProtocol {}
  >> protocol AnotherProtocol {}
  -> protocol InheritingProtocol: SomeProtocol, AnotherProtocol {
        // 프로토콜 정의
     }
  ```
-->

다음은 위에서 정의한 `TextRepresentable` 프로토콜을 상속하는 프로토콜의 예시다:

```swift
protocol PrettyTextRepresentable: TextRepresentable {
    var prettyTextualDescription: String { get }
}
```

<!--
  - test: `protocols`

  ```swifttest
  -> protocol PrettyTextRepresentable: TextRepresentable {
        var prettyTextualDescription: String { get }
     }
  ```
-->

이 예시에서는 `TextRepresentable` 프로토콜을 상속하는 `PrettyTextRepresentable`이라는 새로운 프로토콜을 정의한다. `PrettyTextRepresentable`을 채택하는 모든 타입은 `TextRepresentable`의 요구사항을 모두 충족해야 하며, 추가로 `PrettyTextRepresentable`의 요구사항도 충족해야 한다. 이 예시에서 `PrettyTextRepresentable`은 `String` 타입의 `prettyTextualDescription`이라는 읽기 전용 프로퍼티를 제공해야 한다는 단일 요구사항을 추가한다.

`SnakesAndLadders` 클래스를 확장하여 `PrettyTextRepresentable`을 채택하고 준수하도록 할 수 있다:

```swift
extension SnakesAndLadders: PrettyTextRepresentable {
    var prettyTextualDescription: String {
        var output = textualDescription + ":\n"
        for index in 1...finalSquare {
            switch board[index] {
            case let ladder where ladder > 0:
                output += "▲ "
            case let snake where snake < 0:
                output += "▼ "
            default:
                output += "○ "
            }
        }
        return output
    }
}
```

<!--
  - test: `protocols`

  ```swifttest
  -> extension SnakesAndLadders: PrettyTextRepresentable {
        var prettyTextualDescription: String {
           var output = textualDescription + ":\n"
           for index in 1...finalSquare {
              switch board[index] {
                 case let ladder where ladder > 0:
                    output += "▲ "
                 case let snake where snake < 0:
                    output += "▼ "
                 default:
                    output += "○ "
              }
           }
           return output
        }
     }
  ```
-->

이 확장은 `PrettyTextRepresentable` 프로토콜을 채택하고, `SnakesAndLadders` 타입에 대해 `prettyTextualDescription` 프로퍼티의 구현을 제공한다. `PrettyTextRepresentable`은 `TextRepresentable`이기도 해야 하므로, `prettyTextualDescription`의 구현은 `TextRepresentable` 프로토콜의 `textualDescription` 프로퍼티에 접근하여 출력 문자열을 시작한다. 그런 다음 콜론과 줄 바꿈을 추가하고, 이를 예쁜 텍스트 표현의 시작점으로 사용한다. 이후 보드 사각형 배열을 순회하며, 각 사각형의 내용을 나타내는 기하학적 모양을 추가한다:

- 사각형의 값이 `0`보다 크면 사다리의 시작점을 나타내며, `▲`로 표현된다.
- 사각형의 값이 `0`보다 작으면 뱀의 머리를 나타내며, `▼`로 표현된다.
- 그 외의 경우, 사각형의 값은 `0`이며, "자유" 사각형을 나타내고 `○`로 표현된다.

이제 `prettyTextualDescription` 프로퍼티를 사용해 `SnakesAndLadders` 인스턴스의 예쁜 텍스트 설명을 출력할 수 있다:

```swift
print(game.prettyTextualDescription)
// A game of Snakes and Ladders with 25 squares:
// ○ ○ ▲ ○ ○ ▲ ○ ○ ▲ ▲ ○ ○ ○ ▼ ○ ○ ○ ○ ▼ ○ ○ ▼ ○ ▼ ○
```

<!--
  - test: `protocols`

  ```swifttest
  -> print(game.prettyTextualDescription)
  </ A game of Snakes and Ladders with 25 squares:
  </ ○ ○ ▲ ○ ○ ▲ ○ ○ ▲ ▲ ○ ○ ○ ▼ ○ ○ ○ ○ ▼ ○ ○ ▼ ○ ▼ ○
  ```
-->


## 클래스 전용 프로토콜

프로토콜의 상속 목록에 `AnyObject` 프로토콜을 추가하면, 해당 프로토콜을 클래스 타입으로만 채택할 수 있도록 제한할 수 있다. 구조체나 열거형에서는 이 프로토콜을 채택할 수 없다.

```swift
protocol SomeClassOnlyProtocol: AnyObject, SomeInheritedProtocol {
    // 클래스 전용 프로토콜 정의
}
```

<!--
  - test: `classOnlyProtocols`

  ```swifttest
  >> protocol SomeInheritedProtocol {}
  -> protocol SomeClassOnlyProtocol: AnyObject, SomeInheritedProtocol {
        // 클래스 전용 프로토콜 정의
     }
  ```
-->

위 예제에서 `SomeClassOnlyProtocol`은 클래스 타입에만 채택할 수 있다. 구조체나 열거형 정의에서 `SomeClassOnlyProtocol`을 채택하려고 하면 컴파일 타임 오류가 발생한다.

> 참고: 프로토콜의 요구사항이 참조 의미론(reference semantics)을 가진 타입을 필요로 할 때 클래스 전용 프로토콜을 사용한다. 값 의미론(value semantics)과 참조 의미론에 대한 자세한 내용은 <doc:ClassesAndStructures#Structures-and-Enumerations-Are-Value-Types>와 <doc:ClassesAndStructures#Classes-Are-Reference-Types>를 참고한다.

<!--
  - test: `anyobject-doesn't-have-to-be-first`

  ```swifttest
  >> protocol SomeInheritedProtocol {}
  -> protocol SomeClassOnlyProtocol: SomeInheritedProtocol, AnyObject {
        // 클래스 전용 프로토콜 정의
     }
  ```
-->

<!--
  TODO: 여기에 Cacheable 프로토콜 예제를 추가하는 것이 좋을지 고민해보자.
-->


## 프로토콜 합성

특정 타입이 여러 프로토콜을 동시에 준수하도록 요구하는 것이 유용할 때가 있다. 이때 *프로토콜 합성*을 사용해 여러 프로토콜을 하나의 요구사항으로 결합할 수 있다. 프로토콜 합성은 마치 합성된 모든 프로토콜의 요구사항을 가진 임시 로컬 프로토콜을 정의한 것처럼 동작한다. 단, 프로토콜 합성은 새로운 프로토콜 타입을 정의하지는 않는다.

프로토콜 합성은 `SomeProtocol & AnotherProtocol` 형태로 작성한다. 필요한 만큼의 프로토콜을 앰퍼샌드(`&`)로 구분해 나열할 수 있다. 프로토콜 목록 외에도, 프로토콜 합성은 하나의 클래스 타입을 포함할 수 있으며, 이를 통해 특정 슈퍼클래스를 요구할 수 있다.

다음 예제는 `Named`와 `Aged`라는 두 프로토콜을 합성해 함수 파라미터에 대한 단일 프로토콜 합성 요구사항을 정의한다:

```swift
protocol Named {
    var name: String { get }
}
protocol Aged {
    var age: Int { get }
}
struct Person: Named, Aged {
    var name: String
    var age: Int
}
func wishHappyBirthday(to celebrator: Named & Aged) {
    print("Happy birthday, \(celebrator.name), you're \(celebrator.age)!")
}
let birthdayPerson = Person(name: "Malcolm", age: 21)
wishHappyBirthday(to: birthdayPerson)
// Prints "Happy birthday, Malcolm, you're 21!"
```

<!--
  - test: `protocolComposition`

  ```swifttest
  -> protocol Named {
        var name: String { get }
     }
  -> protocol Aged {
        var age: Int { get }
     }
  -> struct Person: Named, Aged {
        var name: String
        var age: Int
     }
  -> func wishHappyBirthday(to celebrator: Named & Aged) {
        print("Happy birthday, \(celebrator.name), you're \(celebrator.age)!")
     }
  -> let birthdayPerson = Person(name: "Malcolm", age: 21)
  -> wishHappyBirthday(to: birthdayPerson)
  <- Happy birthday, Malcolm, you're 21!
  ```
-->

이 예제에서 `Named` 프로토콜은 `name`이라는 `String` 타입의 읽기 전용 프로퍼티를 요구한다. `Aged` 프로토콜은 `age`라는 `Int` 타입의 읽기 전용 프로퍼티를 요구한다. 두 프로토콜 모두 `Person`이라는 구조체에서 채택된다.

이 예제는 또한 `wishHappyBirthday(to:)` 함수를 정의한다. `celebrator` 파라미터의 타입은 `Named & Aged`로, 이는 "`Named`와 `Aged` 프로토콜을 모두 준수하는 어떤 타입"을 의미한다. 함수에 전달되는 특정 타입이 무엇인지는 중요하지 않으며, 단지 두 프로토콜을 모두 준수하기만 하면 된다.

예제는 `birthdayPerson`이라는 새로운 `Person` 인스턴스를 생성하고, 이 인스턴스를 `wishHappyBirthday(to:)` 함수에 전달한다. `Person`이 두 프로토콜을 모두 준수하기 때문에 이 호출은 유효하며, `wishHappyBirthday(to:)` 함수는 생일 축하 메시지를 출력할 수 있다.

다음은 이전 예제의 `Named` 프로토콜을 `Location` 클래스와 결합한 예제이다:

```swift
class Location {
    var latitude: Double
    var longitude: Double
    init(latitude: Double, longitude: Double) {
        self.latitude = latitude
        self.longitude = longitude
    }
}
class City: Location, Named {
    var name: String
    init(name: String, latitude: Double, longitude: Double) {
        self.name = name
        super.init(latitude: latitude, longitude: longitude)
    }
}
func beginConcert(in location: Location & Named) {
    print("Hello, \(location.name)!")
}

let seattle = City(name: "Seattle", latitude: 47.6, longitude: -122.3)
beginConcert(in: seattle)
// Prints "Hello, Seattle!"
```

<!--
  - test: `protocolComposition`

  ```swifttest
  -> class Location {
         var latitude: Double
         var longitude: Double
         init(latitude: Double, longitude: Double) {
             self.latitude = latitude
             self.longitude = longitude
         }
     }
  -> class City: Location, Named {
         var name: String
         init(name: String, latitude: Double, longitude: Double) {
             self.name = name
             super.init(latitude: latitude, longitude: longitude)
         }
     }
  -> func beginConcert(in location: Location & Named) {
         print("Hello, \(location.name)!")
     }

  -> let seattle = City(name: "Seattle", latitude: 47.6, longitude: -122.3)
  -> beginConcert(in: seattle)
  <- Hello, Seattle!
  ```
-->

`beginConcert(in:)` 함수는 `Location & Named` 타입의 파라미터를 받는다. 이는 "`Location`의 서브클래스이면서 `Named` 프로토콜을 준수하는 어떤 타입"을 의미한다. 이 경우, `City`가 두 요구사항을 모두 충족한다.

`birthdayPerson`을 `beginConcert(in:)` 함수에 전달하는 것은 유효하지 않다. 왜냐하면 `Person`은 `Location`의 서브클래스가 아니기 때문이다. 마찬가지로, `Named` 프로토콜을 준수하지 않는 `Location`의 서브클래스를 만들었다면, 그 타입의 인스턴스로 `beginConcert(in:)`을 호출하는 것도 유효하지 않다.


## 프로토콜 준수 확인

`is`와 `as` 연산자를 사용해 프로토콜 준수 여부를 확인하고 특정 프로토콜로 타입 캐스팅을 할 수 있다. 프로토콜에 대한 확인과 캐스팅은 타입에 대한 확인과 캐스팅과 동일한 문법을 따른다:

- `is` 연산자는 인스턴스가 프로토콜을 준수하면 `true`를 반환하고, 그렇지 않으면 `false`를 반환한다.
- 다운캐스트 연산자 `as?`는 프로토콜 타입의 옵셔널 값을 반환하며, 인스턴스가 해당 프로토콜을 준수하지 않으면 `nil`이 된다.
- 다운캐스트 연산자 `as!`는 프로토콜 타입으로 강제 다운캐스트를 시도하며, 다운캐스트가 실패하면 런타임 에러가 발생한다.

다음 예제는 `HasArea`라는 프로토콜을 정의하며, `area`라는 읽기 전용 `Double` 타입의 프로퍼티 요구사항을 포함한다:

```swift
protocol HasArea {
    var area: Double { get }
}
```

<!--
  - test: `protocolConformance`

  ```swifttest
  -> protocol HasArea {
        var area: Double { get }
     }
  ```
-->

다음은 `HasArea` 프로토콜을 준수하는 `Circle`과 `Country` 두 클래스이다:

```swift
class Circle: HasArea {
    let pi = 3.1415927
    var radius: Double
    var area: Double { return pi * radius * radius }
    init(radius: Double) { self.radius = radius }
}
class Country: HasArea {
    var area: Double
    init(area: Double) { self.area = area }
}
```

<!--
  - test: `protocolConformance`

  ```swifttest
  -> class Circle: HasArea {
        let pi = 3.1415927
        var radius: Double
        var area: Double { return pi * radius * radius }
        init(radius: Double) { self.radius = radius }
     }
  -> class Country: HasArea {
        var area: Double
        init(area: Double) { self.area = area }
     }
  ```
-->

`Circle` 클래스는 저장 프로퍼티 `radius`를 기반으로 계산된 프로퍼티로 `area` 요구사항을 구현한다. `Country` 클래스는 `area` 요구사항을 직접 저장 프로퍼티로 구현한다. 두 클래스 모두 `HasArea` 프로토콜을 올바르게 준수한다.

다음은 `HasArea` 프로토콜을 준수하지 않는 `Animal` 클래스이다:

```swift
class Animal {
    var legs: Int
    init(legs: Int) { self.legs = legs }
}
```

<!--
  - test: `protocolConformance`

  ```swifttest
  -> class Animal {
        var legs: Int
        init(legs: Int) { self.legs = legs }
     }
  ```
-->

`Circle`, `Country`, `Animal` 클래스는 공통된 기본 클래스를 가지고 있지 않다. 그러나 모두 클래스이므로, 세 타입의 인스턴스를 `AnyObject` 타입의 배열로 초기화할 수 있다:

```swift
let objects: [AnyObject] = [
    Circle(radius: 2.0),
    Country(area: 243_610),
    Animal(legs: 4)
]
```

<!--
  - test: `protocolConformance`

  ```swifttest
  -> let objects: [AnyObject] = [
        Circle(radius: 2.0),
        Country(area: 243_610),
        Animal(legs: 4)
     ]
  ```
-->

`objects` 배열은 반지름이 2 단위인 `Circle` 인스턴스, 영국의 면적(제곱킬로미터)으로 초기화된 `Country` 인스턴스, 그리고 다리가 4개인 `Animal` 인스턴스를 포함하는 배열 리터럴로 초기화된다.

이제 `objects` 배열을 순회하며 각 객체가 `HasArea` 프로토콜을 준수하는지 확인할 수 있다:

```swift
for object in objects {
    if let objectWithArea = object as? HasArea {
        print("Area is \(objectWithArea.area)")
    } else {
        print("Something that doesn't have an area")
    }
}
// Area is 12.5663708
// Area is 243610.0
// Something that doesn't have an area
```

<!--
  - test: `protocolConformance`

  ```swifttest
  -> for object in objects {
        if let objectWithArea = object as? HasArea {
           print("Area is \(objectWithArea.area)")
        } else {
           print("Something that doesn't have an area")
        }
     }
  </ Area is 12.5663708
  </ Area is 243610.0
  </ Something that doesn't have an area
  ```
-->

배열의 객체가 `HasArea` 프로토콜을 준수할 때마다, `as?` 연산자가 반환한 옵셔널 값을 `objectWithArea`라는 상수로 언래핑한다. `objectWithArea` 상수는 `HasArea` 타입으로 알려져 있으므로, `area` 프로퍼티에 안전하게 접근하고 출력할 수 있다.

캐스팅 과정에서 기본 객체는 변경되지 않는다. 여전히 `Circle`, `Country`, `Animal` 타입이다. 그러나 `objectWithArea` 상수에 저장된 시점에는 `HasArea` 타입으로만 알려져 있으므로, `area` 프로퍼티만 접근할 수 있다.

<!--
  TODO: 이 예제는 매우 인위적으로 구성되었다.
  또한, 이 두 객체의 면적을 얻는 것은 특별히 유용하지 않다. 공통된 단위 체계가 없기 때문이다.
  그리고 원은 클래스가 아닌 구조체로 정의하는 것이 더 적절할 것이다.
  게다가, 많은 보일러플레이트 초기화 코드를 작성해야 해서 예제가 원하는 만큼 간결하지 않다.
  문제는 @objc 프로토콜 내에서 문자열을 사용하려면 Foundation을 임포트해야 하므로, 숫자만 사용할 수 있다는 점이다.
-->

<!--
  TODO: 이전 TODO에서 언급된 @objc 제한이 해제되었으므로, 이전 예제를 다시 검토해야 할까?
-->


## 선택적 프로토콜 요구사항

프로토콜에 *선택적 요구사항*을 정의할 수 있다. 이 요구사항은 프로토콜을 준수하는 타입에서 반드시 구현할 필요가 없다. 선택적 요구사항은 프로토콜 정의 내에서 `optional` 수식어를 붙여 표시한다. 선택적 요구사항은 Objective-C와의 호환성을 위해 사용된다. 프로토콜과 선택적 요구사항 모두 `@objc` 속성으로 표시해야 한다. `@objc` 프로토콜은 클래스에서만 채택할 수 있으며, 구조체나 열거형에서는 사용할 수 없다.

선택적 요구사항에서 메서드나 프로퍼티를 사용할 때, 그 타입은 자동으로 옵셔널이 된다. 예를 들어, `(Int) -> String` 타입의 메서드는 `((Int) -> String)?`이 된다. 이때 함수 타입 전체가 옵셔널로 감싸지며, 메서드의 반환 값만 옵셔널이 되는 것은 아니다.

선택적 프로토콜 요구사항은 옵셔널 체이닝을 통해 호출할 수 있다. 이는 프로토콜을 준수하는 타입이 해당 요구사항을 구현하지 않았을 가능성을 고려한 것이다. 선택적 메서드의 구현 여부를 확인하려면 메서드 이름 뒤에 물음표를 붙여 호출한다. 예를 들어 `someOptionalMethod?(someArgument)`와 같이 사용한다. 옵셔널 체이닝에 대한 자세한 내용은 <doc:OptionalChaining>을 참고한다.

다음 예제는 `Counter`라는 정수 카운팅 클래스를 정의한다. 이 클래스는 외부 데이터 소스를 사용해 증가량을 제공한다. 이 데이터 소스는 `CounterDataSource` 프로토콜로 정의되며, 두 가지 선택적 요구사항을 포함한다:

```swift
@objc protocol CounterDataSource {
    @objc optional func increment(forCount count: Int) -> Int
    @objc optional var fixedIncrement: Int { get }
}
```

`CounterDataSource` 프로토콜은 `increment(forCount:)`라는 선택적 메서드 요구사항과 `fixedIncrement`라는 선택적 프로퍼티 요구사항을 정의한다. 이 요구사항들은 데이터 소스가 `Counter` 인스턴스에 적절한 증가량을 제공하는 두 가지 방법을 정의한다.

> 참고: 엄밀히 말하면, `CounterDataSource` 프로토콜을 준수하는 커스텀 클래스를 작성할 때, 두 요구사항 모두 구현하지 않아도 된다. 둘 다 선택적이기 때문이다. 기술적으로는 허용되지만, 이는 좋은 데이터 소스라고 할 수 없다.

아래에 정의된 `Counter` 클래스는 `CounterDataSource?` 타입의 선택적 `dataSource` 프로퍼티를 가지고 있다:

```swift
class Counter {
    var count = 0
    var dataSource: CounterDataSource?
    func increment() {
        if let amount = dataSource?.increment?(forCount: count) {
            count += amount
        } else if let amount = dataSource?.fixedIncrement {
            count += amount
        }
    }
}
```

`Counter` 클래스는 현재 값을 `count`라는 변수 프로퍼티에 저장한다. 또한 `increment`라는 메서드를 정의하며, 이 메서드는 호출될 때마다 `count` 프로퍼티를 증가시킨다.

`increment()` 메서드는 먼저 데이터 소스에서 `increment(forCount:)` 메서드의 구현을 찾아 증가량을 가져오려고 시도한다. `increment()` 메서드는 옵셔널 체이닝을 사용해 `increment(forCount:)`를 호출하며, 현재 `count` 값을 메서드의 인자로 전달한다.

여기서 *두 가지* 수준의 옵셔널 체이닝이 사용된다. 첫째, `dataSource`가 `nil`일 가능성이 있으므로, `dataSource` 이름 뒤에 물음표를 붙여 `dataSource`가 `nil`이 아닐 때만 `increment(forCount:)`를 호출한다. 둘째, `dataSource`가 존재하더라도 `increment(forCount:)`를 구현하지 않았을 가능성이 있다. 이 경우에도 옵셔널 체이닝을 통해 처리된다. `increment(forCount:)`가 존재할 때만 호출되며, 이는 `increment(forCount:)` 이름 뒤에 물음표를 붙여 표시한다.

`increment(forCount:)` 호출은 두 가지 이유로 실패할 수 있으므로, 호출 결과는 옵셔널 `Int` 값을 반환한다. 이는 `CounterDataSource` 정의에서 `increment(forCount:)`가 비옵셔널 `Int`를 반환하도록 정의되어 있더라도 마찬가지다. 두 가지 옵셔널 체이닝 연산이 연속적으로 사용되었지만, 결과는 여전히 단일 옵셔널로 감싸진다. 여러 수준의 옵셔널 체이닝을 사용하는 방법에 대한 자세한 내용은 <doc:OptionalChaining#Linking-Multiple-Levels-of-Chaining>을 참고한다.

`increment(forCount:)`를 호출한 후, 반환된 옵셔널 `Int`는 옵셔널 바인딩을 사용해 `amount`라는 상수로 언래핑된다. 옵셔널 `Int`에 값이 포함되어 있다면(즉, 델리게이트와 메서드가 모두 존재하고 메서드가 값을 반환했다면), 언래핑된 `amount`가 저장된 `count` 프로퍼티에 더해지고 증가가 완료된다.

`increment(forCount:)` 메서드로부터 값을 가져올 수 없는 경우(즉, `dataSource`가 `nil`이거나 데이터 소스가 `increment(forCount:)`를 구현하지 않은 경우), `increment()` 메서드는 대신 데이터 소스의 `fixedIncrement` 프로퍼티에서 값을 가져오려고 시도한다. `fixedIncrement` 프로퍼티도 선택적 요구사항이므로, 그 값은 옵셔널 `Int` 값이다. `CounterDataSource` 프로토콜 정의에서 `fixedIncrement`는 비옵셔널 `Int` 프로퍼티로 정의되어 있지만, 여전히 옵셔널로 간주된다.

다음은 데이터 소스가 매번 `3`이라는 고정 값을 반환하는 간단한 `CounterDataSource` 구현이다. 이는 선택적 `fixedIncrement` 프로퍼티 요구사항을 구현함으로써 이루어진다:

```swift
class ThreeSource: NSObject, CounterDataSource {
    let fixedIncrement = 3
}
```

`ThreeSource` 인스턴스를 새로운 `Counter` 인스턴스의 데이터 소스로 사용할 수 있다:

```swift
var counter = Counter()
counter.dataSource = ThreeSource()
for _ in 1...4 {
    counter.increment()
    print(counter.count)
}
// 3
// 6
// 9
// 12
```

위 코드는 새로운 `Counter` 인스턴스를 생성하고, 데이터 소스를 `ThreeSource` 인스턴스로 설정한 후, 카운터의 `increment()` 메서드를 네 번 호출한다. 예상대로, `increment()`가 호출될 때마다 카운터의 `count` 프로퍼티는 3씩 증가한다.

다음은 `TowardsZeroSource`라는 더 복잡한 데이터 소스로, `Counter` 인스턴스가 현재 `count` 값에서 0을 향해 증가하거나 감소하도록 만든다:

```swift
class TowardsZeroSource: NSObject, CounterDataSource {
    func increment(forCount count: Int) -> Int {
        if count == 0 {
            return 0
        } else if count < 0 {
            return 1
        } else {
            return -1
        }
    }
}
```

`TowardsZeroSource` 클래스는 `CounterDataSource` 프로토콜의 선택적 `increment(forCount:)` 메서드를 구현하며, `count` 인자 값을 사용해 어느 방향으로 카운트할지 결정한다. `count`가 이미 0이라면, 메서드는 `0`을 반환해 더 이상 카운트하지 않도록 한다.

기존 `Counter` 인스턴스와 `TowardsZeroSource` 인스턴스를 함께 사용해 `-4`에서 0까지 카운트할 수 있다. 카운터가 0에 도달하면 더 이상 카운트하지 않는다:

```swift
counter.count = -4
counter.dataSource = TowardsZeroSource()
for _ in 1...5 {
    counter.increment()
    print(counter.count)
}
// -3
// -2
// -1
// 0
// 0
```


## 프로토콜 확장

프로토콜은 메서드, 초기화 구문, 서브스크립트, 그리고 계산 프로퍼티 구현을 제공하기 위해 확장할 수 있다. 이를 통해 각 타입의 개별 준수 사항이나 전역 함수가 아닌 프로토콜 자체에 동작을 정의할 수 있다.

예를 들어, `RandomNumberGenerator` 프로토콜을 확장하여 `randomBool()` 메서드를 제공할 수 있다. 이 메서드는 필수 `random()` 메서드의 결과를 사용해 무작위 `Bool` 값을 반환한다:

```swift
extension RandomNumberGenerator {
    func randomBool() -> Bool {
        return random() > 0.5
    }
}
```

<!--
  - test: `protocols`

  ```swifttest
  -> extension RandomNumberGenerator {
        func randomBool() -> Bool {
           return random() > 0.5
        }
     }
  ```
-->

프로토콜에 확장을 생성하면, 모든 준수 타입은 추가 수정 없이 이 메서드 구현을 자동으로 얻게 된다.

```swift
let generator = LinearCongruentialGenerator()
print("Here's a random number: \(generator.random())")
// Prints "Here's a random number: 0.3746499199817101"
print("And here's a random Boolean: \(generator.randomBool())")
// Prints "And here's a random Boolean: true"
```

<!--
  - test: `protocols`

  ```swifttest
  >> do {
  -> let generator = LinearCongruentialGenerator()
  -> print("Here's a random number: \(generator.random())")
  <- Here's a random number: 0.3746499199817101
  -> print("And here's a random Boolean: \(generator.randomBool())")
  <- And here's a random Boolean: true
  >> }
  ```
-->

<!--
  The extra scope in the above test code allows this 'generator' variable to shadow
  the variable that already exists from a previous testcode block.
-->

프로토콜 확장은 준수 타입에 구현을 추가할 수 있지만, 프로토콜이 다른 프로토콜을 확장하거나 상속하도록 만들 수는 없다. 프로토콜 상속은 항상 프로토콜 선언 자체에서 지정된다.


### 기본 구현 제공하기

프로토콜 확장을 사용하면 프로토콜의 메서드나 계산된 프로퍼티 요구사항에 대한 기본 구현을 제공할 수 있다. 프로토콜을 준수하는 타입이 해당 메서드나 프로퍼티에 대해 자체 구현을 제공하면, 확장에서 제공한 구현 대신 자체 구현이 사용된다.

> 주의: 확장을 통해 기본 구현이 제공된 프로토콜 요구사항은 옵셔널 프로토콜 요구사항과 다르다. 준수 타입이 자체 구현을 제공하지 않아도 되지만, 기본 구현이 있는 요구사항은 옵셔널 체이닝 없이 호출할 수 있다.

예를 들어, `TextRepresentable` 프로토콜을 상속받는 `PrettyTextRepresentable` 프로토콜은 `prettyTextualDescription` 프로퍼티에 대한 기본 구현을 제공할 수 있다. 이 구현은 단순히 `textualDescription` 프로퍼티의 결과를 반환한다:

```swift
extension PrettyTextRepresentable  {
    var prettyTextualDescription: String {
        return textualDescription
    }
}
```

<!--
  - test: `protocols`

  ```swifttest
  -> extension PrettyTextRepresentable  {
        var prettyTextualDescription: String {
           return textualDescription
        }
     }
  ```
-->

<!--
  TODO <rdar://problem/32211512> TSPL: Explain when you can/can't override a protocol default implementation
-->

<!--
  프로토콜 요구사항인 경우,
  프로토콜을 준수하는 타입이 기본 구현을 재정의할 수 있다.
-->

<!--
  요구사항이 아닌 경우,
  기본 구현을 재정의하려고 하면 이상한 동작이 발생할 수 있다.
-->

<!--
  정적 타입이 준수 타입인 경우,
  재정의한 구현이 사용된다.
-->

<!--
  정적 타입이 프로토콜 타입인 경우,
  기본 구현이 사용된다.
-->

<!--
  기본 구현에 ``final``을 붙여서
  준수 타입에서 재정의하는 것을 막을 수 없다.
-->


### 프로토콜 확장에 제약 조건 추가하기

프로토콜 확장을 정의할 때, 특정 메서드나 프로퍼티를 사용하기 위해 해당 타입이 충족해야 하는 조건을 지정할 수 있다. 이러한 조건은 확장하려는 프로토콜 이름 뒤에 제네릭 `where` 절을 작성하여 정의한다. 제네릭 `where` 절에 대한 자세한 내용은 <doc:Generics#Generic-Where-Clauses>를 참고한다.

예를 들어, `Collection` 프로토콜을 확장하여 해당 컬렉션의 요소가 `Equatable` 프로토콜을 준수하는 경우에만 적용되는 메서드를 정의할 수 있다. Swift 표준 라이브러리의 일부인 `Equatable` 프로토콜을 통해 컬렉션의 요소를 제한하면, `==`와 `!=` 연산자를 사용해 두 요소가 같은지 다른지 비교할 수 있다.

```swift
extension Collection where Element: Equatable {
    func allEqual() -> Bool {
        for element in self {
            if element != self.first {
                return false
            }
        }
        return true
    }
}
```

<!--
  - test: `protocols`

  ```swifttest
  -> extension Collection where Element: Equatable {
         func allEqual() -> Bool {
             for element in self {
                 if element != self.first {
                     return false
                 }
             }
             return true
         }
     }
  ```
-->

`allEqual()` 메서드는 컬렉션의 모든 요소가 동일한 경우에만 `true`를 반환한다.

두 개의 정수 배열을 예로 들어보자. 하나는 모든 요소가 동일하고, 다른 하나는 그렇지 않다:

```swift
let equalNumbers = [100, 100, 100, 100, 100]
let differentNumbers = [100, 100, 200, 100, 200]
```

<!--
  - test: `protocols`

  ```swifttest
  -> let equalNumbers = [100, 100, 100, 100, 100]
  -> let differentNumbers = [100, 100, 200, 100, 200]
  ```
-->

배열은 `Collection` 프로토콜을 준수하고, 정수는 `Equatable` 프로토콜을 준수하므로, `equalNumbers`와 `differentNumbers` 모두 `allEqual()` 메서드를 사용할 수 있다:

```swift
print(equalNumbers.allEqual())
// Prints "true"
print(differentNumbers.allEqual())
// Prints "false"
```

<!--
  - test: `protocols`

  ```swifttest
  -> print(equalNumbers.allEqual())
  <- true
  -> print(differentNumbers.allEqual())
  <- false
  ```
-->

> 참고: 만약 특정 타입이 동일한 메서드나 프로퍼티를 제공하는 여러 제약 조건을 가진 확장의 요구 사항을 모두 충족한다면, Swift는 가장 구체적인 제약 조건에 해당하는 구현을 사용한다.

<!--
  TODO: It would be great to pull this out of a note,
  but we should wait until we have a better narrative that shows how this
  works with some examples.
-->

<!--
  TODO: Other things to be included
  ---------------------------------
  Class-only protocols
  Protocols marked @objc
  Standard-library protocols such as Sequence, Equatable etc.?
  Show how to make a custom type conform to Boolean or some other protocol
  Show a protocol being used by an enumeration
  accessing protocol methods, properties etc.  through a constant or variable that's *just* of protocol type
  Protocols can't be nested, but nested types can implement protocols
  Protocol requirements can be marked as @unavailable, but this currently only works if they're also marked as @objc.
  Checking for (and calling) optional implementations via optional binding and closures
-->

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


