# 메서드

특정 인스턴스나 타입에 속한 함수를 정의하고 호출하는 방법을 알아본다.

*메서드*는 특정 타입과 연관된 함수를 의미한다. 클래스, 구조체, 열거형 모두 인스턴스 메서드를 정의할 수 있다. 인스턴스 메서드는 해당 타입의 인스턴스와 관련된 특정 작업과 기능을 캡슐화한다. 또한 클래스, 구조체, 열거형은 타입 메서드도 정의할 수 있다. 타입 메서드는 타입 자체와 연관되며, Objective-C의 클래스 메서드와 유사하다.

Swift에서 구조체와 열거형이 메서드를 정의할 수 있다는 점은 C와 Objective-C와의 큰 차이점이다. Objective-C에서는 클래스만 메서드를 정의할 수 있다. 반면 Swift에서는 클래스, 구조체, 열거형 중 어떤 타입을 정의할지 선택할 수 있고, 여전히 해당 타입에 메서드를 정의할 수 있는 유연성을 제공한다.


## 인스턴스 메서드

*인스턴스 메서드*는 특정 클래스, 구조체, 또는 열거형의 인스턴스에 속하는 함수다. 이 메서드는 인스턴스 프로퍼티에 접근하고 수정하는 방법을 제공하거나, 인스턴스의 목적과 관련된 기능을 제공함으로써 해당 인스턴스의 기능을 지원한다. 인스턴스 메서드는 <doc:Functions>에서 설명한 함수와 동일한 문법을 사용한다.

인스턴스 메서드는 해당 타입의 시작과 끝 중괄호 안에 작성한다. 인스턴스 메서드는 해당 타입의 다른 모든 인스턴스 메서드와 프로퍼티에 암시적으로 접근할 수 있다. 인스턴스 메서드는 해당 타입의 특정 인스턴스에서만 호출할 수 있다. 기존 인스턴스 없이 단독으로 호출할 수 없다.

다음은 특정 동작이 발생한 횟수를 세는 데 사용할 수 있는 간단한 `Counter` 클래스를 정의한 예제다:

```swift
class Counter {
    var count = 0
    func increment() {
        count += 1
    }
    func increment(by amount: Int) {
        count += amount
    }
    func reset() {
        count = 0
    }
}
```

<!--
  - test: `instanceMethods`

  ```swifttest
  -> class Counter {
        var count = 0
        func increment() {
           count += 1
        }
        func increment(by amount: Int) {
           count += amount
        }
        func reset() {
           count = 0
        }
     }
  ```
-->

`Counter` 클래스는 세 가지 인스턴스 메서드를 정의한다:

- `increment()`는 카운터를 `1`만큼 증가시킨다.
- `increment(by: Int)`는 카운터를 지정된 정수만큼 증가시킨다.
- `reset()`는 카운터를 `0`으로 초기화한다.

`Counter` 클래스는 현재 카운터 값을 추적하기 위해 `count`라는 변수 프로퍼티도 선언한다.

인스턴스 메서드는 프로퍼티와 동일한 점 문법으로 호출한다:

```swift
let counter = Counter()
// 초기 카운터 값은 0
counter.increment()
// 카운터 값은 이제 1
counter.increment(by: 5)
// 카운터 값은 이제 6
counter.reset()
// 카운터 값은 이제 0
```

<!--
  - test: `instanceMethods`

  ```swifttest
  -> let counter = Counter()
  /> the initial counter value is \(counter.count)
  </ the initial counter value is 0
  -> counter.increment()
  /> the counter's value is now \(counter.count)
  </ the counter's value is now 1
  -> counter.increment(by: 5)
  /> the counter's value is now \(counter.count)
  </ the counter's value is now 6
  -> counter.reset()
  /> the counter's value is now \(counter.count)
  </ the counter's value is now 0
  ```
-->

함수 매개변수는 함수 본문 내에서 사용할 이름과 함수를 호출할 때 사용할 인자 레이블을 모두 가질 수 있다. 이는 <doc:Functions#Function-Argument-Labels-and-Parameter-Names>에서 설명한 바와 같다. 메서드 매개변수도 마찬가지다. 메서드는 단순히 타입과 연관된 함수이기 때문이다.


### self 프로퍼티

모든 타입의 인스턴스는 `self`라는 암시적 프로퍼티를 가지고 있다. 이 `self` 프로퍼티는 인스턴스 자체와 정확히 동일하다. 인스턴스 메서드 내에서 현재 인스턴스를 참조할 때 `self` 프로퍼티를 사용한다.

앞서 예제의 `increment()` 메서드는 다음과 같이 작성할 수도 있다:

```swift
func increment() {
    self.count += 1
}
```

<!--
  - test: `instanceMethodsIncrement`

  ```swifttest
  >> class Counter {
  >> var count: Int = 0
     func increment() {
        self.count += 1
     }
  >> }
  ```
-->

<!--
  NOTE: I'm slightly cheating with my testing of this excerpt, but it works!
-->

실제로는 코드에 `self`를 자주 작성할 필요가 없다. `self`를 명시적으로 작성하지 않으면, Swift는 메서드 내에서 알려진 프로퍼티나 메서드 이름을 사용할 때 현재 인스턴스의 프로퍼티나 메서드를 참조한다고 가정한다. 이 가정은 `Counter`의 세 인스턴스 메서드 내에서 `self.count` 대신 `count`를 사용한 것에서 확인할 수 있다.

이 규칙의 주요 예외는 인스턴스 메서드의 매개변수 이름이 해당 인스턴스의 프로퍼티 이름과 동일한 경우다. 이 경우 매개변수 이름이 우선순위를 가지며, 프로퍼티를 더 명확하게 참조해야 한다. 이때 `self` 프로퍼티를 사용해 매개변수 이름과 프로퍼티 이름을 구분한다.

여기서 `self`는 `x`라는 메서드 매개변수와 `x`라는 인스턴스 프로퍼티를 명확히 구분한다:

```swift
struct Point {
    var x = 0.0, y = 0.0
    func isToTheRightOf(x: Double) -> Bool {
        return self.x > x
    }
}
let somePoint = Point(x: 4.0, y: 5.0)
if somePoint.isToTheRightOf(x: 1.0) {
    print("This point is to the right of the line where x == 1.0")
}
// Prints "This point is to the right of the line where x == 1.0"
```

<!--
  - test: `self`

  ```swifttest
  -> struct Point {
        var x = 0.0, y = 0.0
        func isToTheRightOf(x: Double) -> Bool {
           return self.x > x
        }
     }
  -> let somePoint = Point(x: 4.0, y: 5.0)
  -> if somePoint.isToTheRightOf(x: 1.0) {
        print("This point is to the right of the line where x == 1.0")
     }
  <- This point is to the right of the line where x == 1.0
  ```
-->

`self` 접두사가 없으면 Swift는 `x`의 두 사용 모두 메서드 매개변수 `x`를 참조한다고 가정한다.


### 인스턴스 메서드 내부에서 값 타입 수정하기

구조체와 열거형은 *값 타입*이다. 기본적으로 값 타입의 프로퍼티는 인스턴스 메서드 내부에서 수정할 수 없다.

그러나 특정 메서드 내부에서 구조체나 열거형의 프로퍼티를 수정해야 한다면, 해당 메서드에 *mutating* 동작을 허용할 수 있다. 이렇게 하면 메서드 내부에서 프로퍼티를 변경할 수 있으며, 메서드가 종료될 때 변경 사항이 원래 구조체에 반영된다. 또한 메서드는 암시적인 `self` 프로퍼티에 완전히 새로운 인스턴스를 할당할 수도 있으며, 이 새로운 인스턴스는 메서드가 종료될 때 기존 인스턴스를 대체한다.

이 동작을 허용하려면 해당 메서드의 `func` 키워드 앞에 `mutating` 키워드를 추가하면 된다:

```swift
struct Point {
    var x = 0.0, y = 0.0
    mutating func moveBy(x deltaX: Double, y deltaY: Double) {
        x += deltaX
        y += deltaY
    }
}
var somePoint = Point(x: 1.0, y: 1.0)
somePoint.moveBy(x: 2.0, y: 3.0)
print("The point is now at (\(somePoint.x), \(somePoint.y))")
// Prints "The point is now at (3.0, 4.0)"
```

위의 `Point` 구조체는 `moveBy(x:y:)`라는 mutating 메서드를 정의한다. 이 메서드는 `Point` 인스턴스를 특정 양만큼 이동시킨다. 이 메서드는 새로운 점을 반환하는 대신, 호출된 점을 직접 수정한다. 프로퍼티를 수정할 수 있도록 메서드 정의에 `mutating` 키워드를 추가했다.

구조체 타입의 상수에서는 mutating 메서드를 호출할 수 없다는 점에 주의해야 한다. 이는 프로퍼티가 변수로 선언되었더라도 상수로 선언된 인스턴스의 프로퍼티는 변경할 수 없기 때문이다. 이 내용은 <doc:Properties#Stored-Properties-of-Constant-Structure-Instances>에서 자세히 설명한다:

```swift
let fixedPoint = Point(x: 3.0, y: 3.0)
fixedPoint.moveBy(x: 2.0, y: 3.0)
// this will report an error
```


### 뮤테이션 메서드 내에서 self에 할당하기

뮤테이션 메서드는 암시적 `self` 프로퍼티에 완전히 새로운 인스턴스를 할당할 수 있다. 위에서 보여준 `Point` 예제를 다음과 같은 방식으로 작성할 수도 있다:

```swift
struct Point {
    var x = 0.0, y = 0.0
    mutating func moveBy(x deltaX: Double, y deltaY: Double) {
        self = Point(x: x + deltaX, y: y + deltaY)
    }
}
```

<!--
  - test: `selfStructuresAssign`

  ```swifttest
  -> struct Point {
        var x = 0.0, y = 0.0
        mutating func moveBy(x deltaX: Double, y deltaY: Double) {
           self = Point(x: x + deltaX, y: y + deltaY)
        }
     }
  >> var somePoint = Point(x: 1.0, y: 1.0)
  >> somePoint.moveBy(x: 2.0, y: 3.0)
  >> print("The point is now at (\(somePoint.x), \(somePoint.y))")
  << The point is now at (3.0, 4.0)
  ```
-->

이 버전의 뮤테이션 `moveBy(x:y:)` 메서드는 `x`와 `y` 값이 목표 위치로 설정된 새로운 구조체를 생성한다. 이 메서드를 호출한 결과는 이전 버전을 호출한 것과 정확히 동일하다.

열거형의 뮤테이션 메서드는 암시적 `self` 매개변수를 동일한 열거형의 다른 케이스로 설정할 수 있다:

```swift
enum TriStateSwitch {
    case off, low, high
    mutating func next() {
        switch self {
        case .off:
            self = .low
        case .low:
            self = .high
        case .high:
            self = .off
        }
    }
}
var ovenLight = TriStateSwitch.low
ovenLight.next()
// ovenLight은 이제 .high와 같다
ovenLight.next()
// ovenLight은 이제 .off와 같다
```

<!--
  - test: `selfEnumerations`

  ```swifttest
  -> enum TriStateSwitch {
        case off, low, high
        mutating func next() {
           switch self {
              case .off:
                 self = .low
              case .low:
                 self = .high
              case .high:
                 self = .off
           }
        }
     }
  -> var ovenLight = TriStateSwitch.low
  -> ovenLight.next()
  // ovenLight is now equal to .high
  -> ovenLight.next()
  // ovenLight is now equal to .off
  ```
-->

이 예제는 세 가지 상태를 가진 스위치를 위한 열거형을 정의한다. 스위치는 `next()` 메서드가 호출될 때마다 세 가지 전원 상태(`off`, `low`, `high`) 사이를 순환한다.


## 타입 메서드

앞서 설명한 인스턴스 메서드는 특정 타입의 인스턴스에서 호출하는 메서드이다. 반면, 타입 자체에서 호출하는 메서드도 정의할 수 있다. 이러한 메서드를 *타입 메서드*라고 한다. 타입 메서드는 메서드의 `func` 키워드 앞에 `static` 키워드를 붙여 표시한다. 클래스의 경우 `class` 키워드를 사용할 수 있으며, 이 경우 서브클래스가 슈퍼클래스의 메서드 구현을 재정의할 수 있다.

> 참고: Objective-C에서는 Objective-C 클래스에만 타입 레벨 메서드를 정의할 수 있다. 하지만 Swift에서는 모든 클래스, 구조체, 열거형에 타입 메서드를 정의할 수 있다. 각 타입 메서드는 해당 타입에 명시적으로 범위가 한정된다.

타입 메서드는 인스턴스 메서드와 마찬가지로 점 문법을 사용해 호출한다. 하지만 타입 메서드는 타입 자체에서 호출하며, 타입의 인스턴스에서 호출하지 않는다. 다음은 `SomeClass`라는 클래스의 타입 메서드를 호출하는 예시이다:

```swift
class SomeClass {
    class func someTypeMethod() {
        // 타입 메서드 구현
    }
}
SomeClass.someTypeMethod()
```

<!--
  - test: `typeMethods`

  ```swifttest
  -> class SomeClass {
        class func someTypeMethod() {
           // 타입 메서드 구현
        }
     }
  -> SomeClass.someTypeMethod()
  ```
-->

타입 메서드 내부에서 암시적 `self` 프로퍼티는 타입 자체를 참조하며, 타입의 인스턴스를 참조하지 않는다. 이는 타입 프로퍼티와 타입 메서드 매개변수 간의 모호함을 해결하기 위해 `self`를 사용할 수 있음을 의미한다. 이는 인스턴스 프로퍼티와 인스턴스 메서드 매개변수에서와 동일한 방식이다.

일반적으로 타입 메서드 내부에서 사용하는 모든 한정되지 않은 메서드와 프로퍼티 이름은 다른 타입 레벨 메서드와 프로퍼티를 참조한다. 타입 메서드는 다른 타입 메서드를 타입 이름 없이 메서드 이름만으로 호출할 수 있다. 마찬가지로 구조체와 열거형의 타입 메서드는 타입 프로퍼티를 타입 이름 없이 프로퍼티 이름만으로 접근할 수 있다.

다음 예제는 `LevelTracker`라는 구조체를 정의한다. 이 구조체는 게임의 다양한 레벨 또는 단계를 통해 플레이어의 진행 상황을 추적한다. 이 게임은 싱글 플레이어 게임이지만, 단일 기기에서 여러 플레이어의 정보를 저장할 수 있다.

게임을 처음 시작할 때는 첫 번째 레벨을 제외한 모든 레벨이 잠겨 있다. 플레이어가 레벨을 완료할 때마다 해당 레벨은 기기의 모든 플레이어에 대해 잠금 해제된다. `LevelTracker` 구조체는 타입 프로퍼티와 메서드를 사용해 게임에서 잠금 해제된 레벨을 추적한다. 또한 개별 플레이어의 현재 레벨도 추적한다.

```swift
struct LevelTracker {
    static var highestUnlockedLevel = 1
    var currentLevel = 1

    static func unlock(_ level: Int) {
        if level > highestUnlockedLevel { highestUnlockedLevel = level }
    }

    static func isUnlocked(_ level: Int) -> Bool {
        return level <= highestUnlockedLevel
    }

    @discardableResult
    mutating func advance(to level: Int) -> Bool {
        if LevelTracker.isUnlocked(level) {
            currentLevel = level
            return true
        } else {
            return false
        }
    }
}
```

<!--
  - test: `typeMethods`

  ```swifttest
  -> struct LevelTracker {
        static var highestUnlockedLevel = 1
        var currentLevel = 1

  ->    static func unlock(_ level: Int) {
           if level > highestUnlockedLevel { highestUnlockedLevel = level }
        }

  ->    static func isUnlocked(_ level: Int) -> Bool {
           return level <= highestUnlockedLevel
        }

  ->    @discardableResult
        mutating func advance(to level: Int) -> Bool {
           if LevelTracker.isUnlocked(level) {
              currentLevel = level
              return true
           } else {
              return false
           }
        }
     }
  ```
-->

`LevelTracker` 구조체는 어떤 플레이어가 잠금 해제한 가장 높은 레벨을 추적한다. 이 값은 `highestUnlockedLevel`이라는 타입 프로퍼티에 저장된다.

`LevelTracker`는 `highestUnlockedLevel` 프로퍼티를 다루기 위해 두 개의 타입 메서드를 정의한다. 첫 번째는 `unlock(_:)`이라는 타입 메서드로, 새로운 레벨이 잠금 해제될 때마다 `highestUnlockedLevel` 값을 업데이트한다. 두 번째는 `isUnlocked(_:)`라는 편의 타입 메서드로, 특정 레벨 번호가 이미 잠금 해제되었는지 여부를 `true` 또는 `false`로 반환한다. (이 타입 메서드들은 `LevelTracker.highestUnlockedLevel`과 같이 타입 이름을 붙이지 않고도 `highestUnlockedLevel` 타입 프로퍼티에 접근할 수 있다.)

타입 프로퍼티와 타입 메서드 외에도, `LevelTracker`는 개별 플레이어의 게임 진행 상황을 추적한다. `currentLevel`이라는 인스턴스 프로퍼티를 사용해 플레이어가 현재 진행 중인 레벨을 추적한다.

`currentLevel` 프로퍼티를 관리하기 위해 `LevelTracker`는 `advance(to:)`라는 인스턴스 메서드를 정의한다. 이 메서드는 `currentLevel`을 업데이트하기 전에 요청한 새 레벨이 이미 잠금 해제되었는지 확인한다. `advance(to:)` 메서드는 `currentLevel`을 실제로 설정할 수 있었는지 여부를 나타내는 불리언 값을 반환한다. `advance(to:)` 메서드를 호출하는 코드가 반환 값을 무시해도 문제가 되지 않기 때문에, 이 함수는 `@discardableResult` 속성으로 표시된다. 이 속성에 대한 자세한 내용은 <doc:Attributes>를 참고한다.

`LevelTracker` 구조체는 아래에 표시된 `Player` 클래스와 함께 사용되어 개별 플레이어의 진행 상황을 추적하고 업데이트한다:

```swift
class Player {
    var tracker = LevelTracker()
    let playerName: String
    func complete(level: Int) {
        LevelTracker.unlock(level + 1)
        tracker.advance(to: level + 1)
    }
    init(name: String) {
        playerName = name
    }
}
```

<!--
  - test: `typeMethods`

  ```swifttest
  -> class Player {
        var tracker = LevelTracker()
        let playerName: String
        func complete(level: Int) {
           LevelTracker.unlock(level + 1)
           tracker.advance(to: level + 1)
        }
        init(name: String) {
           playerName = name
        }
     }
  ```
-->

`Player` 클래스는 플레이어의 진행 상황을 추적하기 위해 `LevelTracker`의 새 인스턴스를 생성한다. 또한 `complete(level:)`이라는 메서드를 제공하며, 이 메서드는 플레이어가 특정 레벨을 완료할 때마다 호출된다. 이 메서드는 모든 플레이어를 위해 다음 레벨을 잠금 해제하고 플레이어의 진행 상황을 업데이트해 다음 레벨로 이동시킨다. (`advance(to:)`의 불리언 반환 값은 무시된다. 이전 줄에서 `LevelTracker.unlock(_:)` 호출로 레벨이 잠금 해제되었음을 알 수 있기 때문이다.)

새 플레이어를 위해 `Player` 클래스의 인스턴스를 생성하고, 플레이어가 레벨 1을 완료할 때 어떤 일이 발생하는지 확인할 수 있다:

```swift
var player = Player(name: "Argyrios")
player.complete(level: 1)
print("highest unlocked level is now \(LevelTracker.highestUnlockedLevel)")
// "highest unlocked level is now 2" 출력
```

<!--
  - test: `typeMethods`

  ```swifttest
  -> var player = Player(name: "Argyrios")
  -> player.complete(level: 1)
  -> print("highest unlocked level is now \(LevelTracker.highestUnlockedLevel)")
  <- highest unlocked level is now 2
  ```
-->

두 번째 플레이어를 생성하고, 아직 게임 내 어떤 플레이어도 잠금 해제하지 않은 레벨로 이동하려고 하면, 플레이어의 현재 레벨 설정 시도가 실패한다:

```swift
player = Player(name: "Beto")
if player.tracker.advance(to: 6) {
    print("player is now on level 6")
} else {
    print("level 6 hasn't yet been unlocked")
}
// "level 6 hasn't yet been unlocked" 출력
```

<!--
  - test: `typeMethods`

  ```swifttest
  -> player = Player(name: "Beto")
  -> if player.tracker.advance(to: 6) {
        print("player is now on level 6")
     } else {
        print("level 6 hasn't yet been unlocked")
     }
  <- level 6 hasn't yet been unlocked
  ```
-->

<!--
  TODO: Method Binding
  --------------------

  TODO: you can get a function that refers to a method, either with or without the 'self' argument already being bound:
  class C {
     func foo(x: Int) -> Float { ... }
  }
  var c = C()
  var boundFunc = c.foo   // a function with type (Int) -> Float
  var unboundFunc = C.foo // a function with type (C) -> (Int) -> Float

  TODO: selector-style methods can be referenced as foo.bar:bas:
  (see Doug's comments from the 2014-03-12 release notes)
-->

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


