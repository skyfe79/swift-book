# 자동 참조 카운팅

객체의 수명과 관계를 모델링한다.

Swift는 *자동 참조 카운팅*(ARC, Automatic Reference Counting)을 사용해 앱의 메모리 사용을 추적하고 관리한다. 대부분의 경우 Swift에서 메모리 관리는 "그냥 작동"하기 때문에 직접 메모리 관리를 고민할 필요가 없다. ARC는 클래스 인스턴스가 더 이상 필요하지 않을 때 해당 인스턴스가 사용하던 메모리를 자동으로 해제한다.

하지만 몇 가지 경우 ARC는 메모리를 관리하기 위해 코드의 일부 간 관계에 대한 추가 정보를 요구한다. 이 장에서는 이러한 상황을 설명하고 ARC가 앱의 모든 메모리를 관리할 수 있도록 하는 방법을 보여준다. Swift에서 ARC를 사용하는 방식은 Objective-C에서 ARC를 사용하는 방식과 매우 유사하다. 자세한 내용은 [ARC로 전환하기 릴리스 노트](https://developer.apple.com/library/content/releasenotes/ObjectiveC/RN-TransitioningToARC/Introduction/Introduction.html)를 참고한다.

참조 카운팅은 클래스의 인스턴스에만 적용된다. 구조체와 열거형은 값 타입이지 참조 타입이 아니며, 참조로 저장되거나 전달되지 않는다.


## ARC의 동작 원리

클래스의 새 인스턴스를 생성할 때마다 ARC는 해당 인스턴스에 대한 정보를 저장하기 위해 메모리 공간을 할당한다. 이 메모리 공간에는 인스턴스의 타입 정보와 함께, 해당 인스턴스와 연결된 저장 프로퍼티의 값이 포함된다.

또한, 인스턴스가 더 이상 필요하지 않게 되면 ARC는 해당 인스턴스가 사용하던 메모리를 해제하여 다른 용도로 사용할 수 있게 한다. 이를 통해 클래스 인스턴스가 불필요하게 메모리를 차지하는 것을 방지한다.

하지만, ARC가 여전히 사용 중인 인스턴스를 해제해 버리면, 해당 인스턴스의 프로퍼티에 접근하거나 메서드를 호출할 수 없게 된다. 심지어 인스턴스에 접근하려고 시도하면 앱이 크래시될 가능성이 높다.

따라서 ARC는 인스턴스가 필요하지 않을 때까지 사라지지 않도록 보장하기 위해, 현재 각 클래스 인스턴스를 참조하고 있는 프로퍼티, 상수, 변수의 수를 추적한다. ARC는 해당 인스턴스에 대한 활성 참조가 하나라도 남아 있는 한, 인스턴스를 해제하지 않는다.

이를 가능하게 하기 위해, 클래스 인스턴스를 프로퍼티, 상수, 또는 변수에 할당할 때마다, 해당 프로퍼티, 상수, 또는 변수는 인스턴스에 대한 *강한 참조*를 만든다. 이 참조를 "강한" 참조라고 부르는 이유는, 강한 참조가 남아 있는 동안에는 인스턴스를 단단히 붙잡아 두고 해제되지 않도록 하기 때문이다.


## ARC 동작 방식

자동 참조 카운팅(Automatic Reference Counting, ARC)이 어떻게 동작하는지 예제를 통해 살펴본다. 이 예제는 `Person`이라는 간단한 클래스로 시작한다. 이 클래스는 `name`이라는 저장 상수 프로퍼티를 정의한다:

```swift
class Person {
    let name: String
    init(name: String) {
        self.name = name
        print("\(name) is being initialized")
    }
    deinit {
        print("\(name) is being deinitialized")
    }
}
```

<!--
  - test: `howARCWorks`

  ```swifttest
  -> class Person {
        let name: String
        init(name: String) {
           self.name = name
           print("\(name) is being initialized")
        }
        deinit {
           print("\(name) is being deinitialized")
        }
     }
  ```
-->

`Person` 클래스는 인스턴스의 `name` 프로퍼티를 설정하고 초기화가 진행 중임을 알리는 메시지를 출력하는 초기화 메서드를 가지고 있다. 또한 `Person` 클래스는 인스턴스가 메모리에서 해제될 때 메시지를 출력하는 디이니셜라이저를 포함한다.

다음 코드 조각은 `Person?` 타입의 세 변수를 정의한다. 이 변수들은 이후 코드에서 새로운 `Person` 인스턴스에 대한 여러 참조를 설정하는 데 사용된다. 이 변수들은 옵셔널 타입(`Person?`, `Person`이 아님)이기 때문에 자동으로 `nil` 값으로 초기화되며, 현재는 `Person` 인스턴스를 참조하지 않는다.

```swift
var reference1: Person?
var reference2: Person?
var reference3: Person?
```

<!--
  - test: `howARCWorks`

  ```swifttest
  -> var reference1: Person?
  -> var reference2: Person?
  -> var reference3: Person?
  ```
-->

이제 새로운 `Person` 인스턴스를 생성하고 이 세 변수 중 하나에 할당할 수 있다:

```swift
reference1 = Person(name: "John Appleseed")
// Prints "John Appleseed is being initialized"
```

<!--
  - test: `howARCWorks`

  ```swifttest
  -> reference1 = Person(name: "John Appleseed")
  <- John Appleseed is being initialized
  ```
-->

`Person` 클래스의 초기화 메서드를 호출할 때 `"John Appleseed is being initialized"` 메시지가 출력된다. 이는 초기화가 완료되었음을 확인시켜준다.

새로운 `Person` 인스턴스가 `reference1` 변수에 할당되었기 때문에, 이제 `reference1`에서 새로운 `Person` 인스턴스로의 강한 참조가 생성되었다. 최소 하나의 강한 참조가 존재하기 때문에, ARC는 이 `Person` 인스턴스가 메모리에 유지되고 해제되지 않도록 보장한다.

동일한 `Person` 인스턴스를 두 개의 추가 변수에 할당하면, 해당 인스턴스에 대한 두 개의 추가 강한 참조가 생성된다:

```swift
reference2 = reference1
reference3 = reference1
```

<!--
  - test: `howARCWorks`

  ```swifttest
  -> reference2 = reference1
  -> reference3 = reference1
  ```
-->

이제 이 단일 `Person` 인스턴스에 대해 *세 개*의 강한 참조가 존재한다.

두 개의 강한 참조(원래의 참조 포함)를 `nil`로 설정하여 끊으면, 단일 강한 참조만 남게 되고, `Person` 인스턴스는 해제되지 않는다:

```swift
reference1 = nil
reference2 = nil
```

<!--
  - test: `howARCWorks`

  ```swifttest
  -> reference1 = nil
  -> reference2 = nil
  ```
-->

ARC는 세 번째이자 마지막 강한 참조가 끊어질 때까지 `Person` 인스턴스를 해제하지 않는다. 이 시점에서 `Person` 인스턴스가 더 이상 사용되지 않는다는 것이 명확해진다:

```swift
reference3 = nil
// Prints "John Appleseed is being deinitialized"
```

<!--
  - test: `howARCWorks`

  ```swifttest
  -> reference3 = nil
  <- John Appleseed is being deinitialized
  ```
-->


## 클래스 인스턴스 간의 강한 참조 순환

위 예제에서 ARC는 새로운 `Person` 인스턴스에 대한 참조 횟수를 추적하고, 더 이상 필요하지 않을 때 해당 인스턴스를 해제할 수 있다. 하지만 클래스 인스턴스가 **절대로** 강한 참조가 0이 되지 않는 코드를 작성할 수도 있다. 두 클래스 인스턴스가 서로를 강하게 참조하는 경우, 각 인스턴스가 서로를 살려두는 상황이 발생할 수 있다. 이를 **강한 참조 순환**이라고 한다.

강한 참조 순환을 해결하려면 클래스 간의 관계를 강한 참조 대신 약한 참조(weak) 또는 미소유 참조(unowned)로 정의해야 한다. 이 과정은 <doc:AutomaticReferenceCounting#Resolving-Strong-Reference-Cycles-Between-Class-Instances>에서 설명한다. 하지만 강한 참조 순환을 해결하는 방법을 배우기 전에, 이러한 순환이 어떻게 발생하는지 이해하는 것이 유용하다.

다음은 실수로 강한 참조 순환이 발생할 수 있는 예제다. 이 예제는 아파트 단지와 그 거주자를 모델링하는 `Person`과 `Apartment`라는 두 클래스를 정의한다:

```swift
class Person {
    let name: String
    init(name: String) { self.name = name }
    var apartment: Apartment?
    deinit { print("\(name) is being deinitialized") }
}

class Apartment {
    let unit: String
    init(unit: String) { self.unit = unit }
    var tenant: Person?
    deinit { print("Apartment \(unit) is being deinitialized") }
}
```

<!--
  - test: `referenceCycles`

  ```swifttest
  -> class Person {
        let name: String
        init(name: String) { self.name = name }
        var apartment: Apartment?
        deinit { print("\(name) is being deinitialized") }
     }

  -> class Apartment {
        let unit: String
        init(unit: String) { self.unit = unit }
        var tenant: Person?
        deinit { print("Apartment \(unit) is being deinitialized") }
     }
  ```
-->

모든 `Person` 인스턴스는 `String` 타입의 `name` 프로퍼티와 초기값이 `nil`인 옵셔널 `apartment` 프로퍼티를 가진다. `apartment` 프로퍼티는 옵셔널이며, 사람이 항상 아파트를 소유하지 않을 수 있기 때문이다.

마찬가지로, 모든 `Apartment` 인스턴스는 `String` 타입의 `unit` 프로퍼티와 초기값이 `nil`인 옵셔널 `tenant` 프로퍼티를 가진다. `tenant` 프로퍼티는 아파트가 항상 세입자를 보유하지 않을 수 있기 때문에 옵셔널이다.

두 클래스 모두 디이니셜라이저를 정의하며, 해당 클래스의 인스턴스가 해제될 때 이를 출력한다. 이를 통해 `Person`과 `Apartment` 인스턴스가 예상대로 해제되는지 확인할 수 있다.

다음 코드 스니펫은 옵셔널 타입의 `john`과 `unit4A`라는 두 변수를 정의한다. 이 변수들은 아래에서 특정 `Apartment`와 `Person` 인스턴스로 설정될 것이다. 두 변수 모두 옵셔널이기 때문에 초기값은 `nil`이다:

```swift
var john: Person?
var unit4A: Apartment?
```

<!--
  - test: `referenceCycles`

  ```swifttest
  -> var john: Person?
  -> var unit4A: Apartment?
  ```
-->

이제 특정 `Person` 인스턴스와 `Apartment` 인스턴스를 생성하고, 이 새로운 인스턴스를 `john`과 `unit4A` 변수에 할당할 수 있다:

```swift
john = Person(name: "John Appleseed")
unit4A = Apartment(unit: "4A")
```

<!--
  - test: `referenceCycles`

  ```swifttest
  -> john = Person(name: "John Appleseed")
  -> unit4A = Apartment(unit: "4A")
  ```
-->

이 두 인스턴스를 생성하고 할당한 후의 강한 참조 상태는 다음과 같다. `john` 변수는 새로운 `Person` 인스턴스를 강하게 참조하고, `unit4A` 변수는 새로운 `Apartment` 인스턴스를 강하게 참조한다:

![](referenceCycle01)

이제 두 인스턴스를 연결하여 사람이 아파트를 소유하고, 아파트가 세입자를 가지도록 할 수 있다. `john`과 `unit4A` 옵셔널 변수에 저장된 인스턴스에 접근하고 언래핑하기 위해 느낌표(`!`)를 사용하여 해당 인스턴스의 프로퍼티를 설정한다:

```swift
john!.apartment = unit4A
unit4A!.tenant = john
```

<!--
  - test: `referenceCycles`

  ```swifttest
  -> john!.apartment = unit4A
  -> unit4A!.tenant = john
  ```
-->

두 인스턴스를 연결한 후의 강한 참조 상태는 다음과 같다:

![](referenceCycle02)

불행히도, 이 두 인스턴스를 연결하면 강한 참조 순환이 발생한다. `Person` 인스턴스는 `Apartment` 인스턴스를 강하게 참조하고, `Apartment` 인스턴스는 `Person` 인스턴스를 강하게 참조한다. 따라서 `john`과 `unit4A` 변수가 가진 강한 참조를 끊어도 참조 횟수가 0으로 떨어지지 않으며, ARC는 인스턴스를 해제하지 않는다:

```swift
john = nil
unit4A = nil
```

<!--
  - test: `referenceCycles`

  ```swifttest
  -> john = nil
  -> unit4A = nil
  ```
-->

이 두 변수를 `nil`로 설정했을 때 디이니셜라이저가 호출되지 않았음을 주목하라. 강한 참조 순환은 `Person`과 `Apartment` 인스턴스가 해제되지 못하게 하여 앱에서 메모리 누수를 일으킨다.

`john`과 `unit4A` 변수를 `nil`로 설정한 후의 강한 참조 상태는 다음과 같다:

![](referenceCycle03)

`Person` 인스턴스와 `Apartment` 인스턴스 간의 강한 참조는 여전히 남아 있으며, 끊을 수 없다.


## 클래스 인스턴스 간 강한 참조 순환 문제 해결

Swift는 클래스 타입 프로퍼티를 다룰 때 강한 참조 순환 문제를 해결하기 위해 두 가지 방법을 제공한다: 약한 참조(weak reference)와 미소유 참조(unowned reference).

약한 참조와 미소유 참조는 참조 순환에 있는 한 인스턴스가 다른 인스턴스를 강하게 유지하지 않고도 참조할 수 있게 한다. 이렇게 하면 강한 참조 순환을 만들지 않고도 서로를 참조할 수 있다.

다른 인스턴스의 수명이 더 짧을 때, 즉 다른 인스턴스가 먼저 해제될 가능성이 있을 때는 약한 참조를 사용한다. 위의 `Apartment` 예제에서, 아파트가 일생 동안 세입자가 없을 수 있는 상황이므로, 이 경우 약한 참조를 사용해 참조 순환을 끊는 것이 적절하다. 반면, 다른 인스턴스의 수명이 같거나 더 길 때는 미소유 참조를 사용한다.

<!--
  질문: "참조 순환에 있는 두 프로퍼티 중 어떤 것을 약한 참조나 미소유 참조로 표시해야 할까요?"라는 질문에 어떻게 답할 수 있을까요?
-->


### 약한 참조

**약한 참조**는 참조하는 인스턴스를 강하게 유지하지 않아, ARC가 참조된 인스턴스를 해제하는 것을 막지 않는다. 이 동작은 참조가 강한 참조 순환에 포함되는 것을 방지한다. 약한 참조를 나타내려면 프로퍼티나 변수 선언 앞에 `weak` 키워드를 붙인다.

약한 참조는 참조하는 인스턴스를 강하게 유지하지 않기 때문에, 약한 참조가 여전히 해당 인스턴스를 참조하고 있는 동안에도 그 인스턴스가 해제될 수 있다. 따라서 ARC는 참조된 인스턴스가 해제되면 자동으로 약한 참조를 `nil`로 설정한다. 또한, 약한 참조는 런타임에 값이 `nil`로 변경될 수 있어야 하므로, 항상 옵셔널 타입의 변수로 선언된다.

약한 참조의 값이 존재하는지 확인할 수 있으며, 더 이상 존재하지 않는 유효하지 않은 인스턴스를 참조하는 상황은 발생하지 않는다.

> 참고: ARC가 약한 참조를 `nil`로 설정할 때 프로퍼티 옵저버는 호출되지 않는다.

<!--
  - test: `weak-reference-doesnt-trigger-didset`

  ```swifttest
  -> class C {
         weak var w: C? { didSet { print("did set") } }
     }
  -> var c1 = C()
  -> do {
  ->     let c2 = C()
  ->     assert(c1.w == nil)
  ->     c1.w = c2
  << did set
  ->     assert(c1.w != nil)
  -> } // ARC deallocates c2; didSet doesn't fire.
  -> assert(c1.w == nil)
  ```
-->

아래 예제는 앞서 살펴본 `Person`과 `Apartment` 예제와 동일하지만, 한 가지 중요한 차이점이 있다. 이번에는 `Apartment` 타입의 `tenant` 프로퍼티가 약한 참조로 선언되었다:

```swift
class Person {
    let name: String
    init(name: String) { self.name = name }
    var apartment: Apartment?
    deinit { print("\(name) is being deinitialized") }
}

class Apartment {
    let unit: String
    init(unit: String) { self.unit = unit }
    weak var tenant: Person?
    deinit { print("Apartment \(unit) is being deinitialized") }
}
```

<!--
  - test: `weakReferences`

  ```swifttest
  -> class Person {
        let name: String
        init(name: String) { self.name = name }
        var apartment: Apartment?
        deinit { print("\(name) is being deinitialized") }
     }

  -> class Apartment {
        let unit: String
        init(unit: String) { self.unit = unit }
        weak var tenant: Person?
        deinit { print("Apartment \(unit) is being deinitialized") }
     }
  ```
-->

두 변수(`john`과 `unit4A`)의 강한 참조와 두 인스턴스 간의 연결은 이전과 동일하게 생성된다:

```swift
var john: Person?
var unit4A: Apartment?

john = Person(name: "John Appleseed")
unit4A = Apartment(unit: "4A")

john!.apartment = unit4A
unit4A!.tenant = john
```

<!--
  - test: `weakReferences`

  ```swifttest
  -> var john: Person?
  -> var unit4A: Apartment?

  -> john = Person(name: "John Appleseed")
  -> unit4A = Apartment(unit: "4A")

  -> john!.apartment = unit4A
  -> unit4A!.tenant = john
  ```
-->

두 인스턴스를 연결한 후의 참조 상태는 다음과 같다:

![](weakReference01)

`Person` 인스턴스는 여전히 `Apartment` 인스턴스에 대한 강한 참조를 가지고 있지만, `Apartment` 인스턴스는 이제 `Person` 인스턴스에 대한 **약한 참조**를 가지고 있다. 이는 `john` 변수가 `nil`로 설정되어 강한 참조가 끊어지면, `Person` 인스턴스에 대한 강한 참조가 더 이상 없음을 의미한다:

```swift
john = nil
// Prints "John Appleseed is being deinitialized"
```

<!--
  - test: `weakReferences`

  ```swifttest
  -> john = nil
  <- John Appleseed is being deinitialized
  ```
-->

`Person` 인스턴스에 대한 강한 참조가 더 이상 없기 때문에, 해당 인스턴스는 해제되고 `tenant` 프로퍼티는 `nil`로 설정된다:

![](weakReference02)

`Apartment` 인스턴스에 대한 유일한 강한 참조는 `unit4A` 변수에서 온다. 이 강한 참조를 끊으면, `Apartment` 인스턴스에 대한 강한 참조가 더 이상 없게 된다:

```swift
unit4A = nil
// Prints "Apartment 4A is being deinitialized"
```

<!--
  - test: `weakReferences`

  ```swifttest
  -> unit4A = nil
  <- Apartment 4A is being deinitialized
  ```
-->

`Apartment` 인스턴스에 대한 강한 참조가 더 이상 없기 때문에, 이 인스턴스도 해제된다:

![](weakReference03)

> 참고: 가비지 컬렉션을 사용하는 시스템에서는, 강한 참조가 없는 객체는 메모리 압박으로 인해 가비지 컬렉션이 트리거될 때만 해제되기 때문에, 약한 포인터를 간단한 캐싱 메커니즘을 구현하는 데 사용하기도 한다. 그러나 ARC에서는 마지막 강한 참조가 제거되면 즉시 값이 해제되므로, 약한 참조는 이러한 목적에 적합하지 않다.


### 소유하지 않은 참조 (Unowned References)

약한 참조(weak reference)와 마찬가지로, *소유하지 않은 참조(unowned reference)*는 참조하는 인스턴스를 강하게 유지하지 않는다. 그러나 약한 참조와 달리, 소유하지 않은 참조는 다른 인스턴스가 동일한 수명이나 더 긴 수명을 가질 때 사용한다. `unowned` 키워드를 프로퍼티나 변수 선언 앞에 붙여 소유하지 않은 참조를 표시한다.

약한 참조와 달리, 소유하지 않은 참조는 항상 값을 가질 것으로 예상된다. 따라서 값을 `unowned`로 표시하면 옵셔널이 되지 않으며, ARC는 소유하지 않은 참조의 값을 `nil`로 설정하지 않는다.

<!--
  소유하지 않은 참조가 할 수 있는 모든 것을 약한 참조는 더 느리고 더 어색하게 할 수 있다
  (하지만 여전히 올바르게 수행한다).
  소유하지 않은 참조는 더 빠르고 쉽기 때문에(옵셔널이 없음) 흥미롭다 ---
  실제로 데이터에 적합한 경우에만 사용할 때.
-->

> 중요: 참조된 인스턴스가 해제되지 않았다는 것을 확신할 때만 소유하지 않은 참조를 사용하라.
>
> 인스턴스가 해제된 후 소유하지 않은 참조의 값에 접근하려고 하면 런타임 오류가 발생한다.

<!--
  이 요구 사항을 충족하는 한 가지 방법은
  소유하지 않은 프로퍼티를 가진 객체를 소유자를 통해 접근하는 것이다.
  직접 참조를 유지하는 대신, 왜냐하면 그 직접 참조는 소유자보다 더 오래 살 수 있기 때문이다.
  그러나... 이 전략은 소유하지 않은 참조가 객체에서 소유자로의 역참조일 때만 효과적이다.
-->

다음 예제는 은행 고객과 그 고객의 신용카드를 모델링하는 두 클래스, `Customer`와 `CreditCard`를 정의한다. 이 두 클래스는 각각 다른 클래스의 인스턴스를 프로퍼티로 저장한다. 이 관계는 강한 참조 순환을 일으킬 가능성이 있다.

`Customer`와 `CreditCard` 간의 관계는 위의 약한 참조 예제에서 본 `Apartment`와 `Person` 간의 관계와 약간 다르다. 이 데이터 모델에서 고객은 신용카드를 가질 수도 있고 가지지 않을 수도 있지만, 신용카드는 항상 고객과 연결된다. `CreditCard` 인스턴스는 참조하는 `Customer`보다 더 오래 살지 않는다. 이를 나타내기 위해 `Customer` 클래스는 옵셔널 `card` 프로퍼티를 가지지만, `CreditCard` 클래스는 소유하지 않은(그리고 옵셔널이 아닌) `customer` 프로퍼티를 가진다.

또한, 새로운 `CreditCard` 인스턴스는 `number` 값과 `customer` 인스턴스를 커스텀 `CreditCard` 초기화 함수에 전달해야만 생성할 수 있다. 이렇게 하면 `CreditCard` 인스턴스가 생성될 때 항상 연결된 `customer` 인스턴스가 있다는 것을 보장한다.

신용카드는 항상 고객을 가지므로, 강한 참조 순환을 피하기 위해 `customer` 프로퍼티를 소유하지 않은 참조로 정의한다:

```swift
class Customer {
    let name: String
    var card: CreditCard?
    init(name: String) {
        self.name = name
    }
    deinit { print("\(name) is being deinitialized") }
}

class CreditCard {
    let number: UInt64
    unowned let customer: Customer
    init(number: UInt64, customer: Customer) {
        self.number = number
        self.customer = customer
    }
    deinit { print("Card #\(number) is being deinitialized") }
}
```

<!--
  - test: `unownedReferences`

  ```swifttest
  -> class Customer {
        let name: String
        var card: CreditCard?
        init(name: String) {
           self.name = name
        }
        deinit { print("\(name) is being deinitialized") }
     }

  -> class CreditCard {
        let number: UInt64
        unowned let customer: Customer
        init(number: UInt64, customer: Customer) {
           self.number = number
           self.customer = customer
        }
        deinit { print("Card #\(number) is being deinitialized") }
     }
  ```
-->

> 참고: `CreditCard` 클래스의 `number` 프로퍼티는 `Int` 대신 `UInt64` 타입으로 정의되어 있다. 이는 `number` 프로퍼티의 용량이 32비트와 64비트 시스템 모두에서 16자리 카드 번호를 저장할 수 있을 만큼 충분히 크도록 보장하기 위함이다.

다음 코드 조각은 특정 고객에 대한 참조를 저장할 옵셔널 `Customer` 변수 `john`을 정의한다. 이 변수는 옵셔널이기 때문에 초기값이 `nil`이다:

```swift
var john: Customer?
```

<!--
  - test: `unownedReferences`

  ```swifttest
  -> var john: Customer?
  ```
-->

이제 `Customer` 인스턴스를 생성하고, 이를 사용해 새로운 `CreditCard` 인스턴스를 초기화한 후 해당 고객의 `card` 프로퍼티에 할당할 수 있다:

```swift
john = Customer(name: "John Appleseed")
john!.card = CreditCard(number: 1234_5678_9012_3456, customer: john!)
```

<!--
  - test: `unownedReferences`

  ```swifttest
  -> john = Customer(name: "John Appleseed")
  -> john!.card = CreditCard(number: 1234_5678_9012_3456, customer: john!)
  ```
-->

두 인스턴스를 연결한 후의 참조 관계는 다음과 같다:

![](unownedReference01)

이제 `Customer` 인스턴스는 `CreditCard` 인스턴스에 대한 강한 참조를 가지고, `CreditCard` 인스턴스는 `Customer` 인스턴스에 대한 소유하지 않은 참조를 가진다.

소유하지 않은 `customer` 참조 때문에, `john` 변수가 가진 강한 참조를 끊으면 `Customer` 인스턴스에 대한 강한 참조가 더 이상 존재하지 않는다:

![](unownedReference02)

`Customer` 인스턴스에 대한 강한 참조가 더 이상 없으므로, 이 인스턴스는 해제된다. 이 후 `CreditCard` 인스턴스에 대한 강한 참조도 더 이상 없으므로, 이 인스턴스 역시 해제된다:

```swift
john = nil
// Prints "John Appleseed is being deinitialized"
// Prints "Card #1234567890123456 is being deinitialized"
```

<!--
  - test: `unownedReferences`

  ```swifttest
  -> john = nil
  <- John Appleseed is being deinitialized
  <- Card #1234567890123456 is being deinitialized
  ```
-->

위의 최종 코드 조각은 `john` 변수가 `nil`로 설정된 후 `Customer` 인스턴스와 `CreditCard` 인스턴스의 디이니셜라이저가 모두 "해제됨" 메시지를 출력하는 것을 보여준다.

> 참고: 위의 예제는 *안전한* 소유하지 않은 참조를 사용하는 방법을 보여준다. Swift는 또한 런타임 안전 검사를 비활성화해야 하는 경우(예: 성능상의 이유로)를 위해 *안전하지 않은* 소유하지 않은 참조를 제공한다. 모든 안전하지 않은 연산과 마찬가지로, 코드의 안전성을 확인할 책임을 진다.
>
> 안전하지 않은 소유하지 않은 참조는 `unowned(unsafe)`를 사용하여 표시한다. 안전하지 않은 소유하지 않은 참조를 참조된 인스턴스가 해제된 후에 접근하려고 하면, 프로그램은 해당 인스턴스가 있던 메모리 위치에 접근하려고 시도하며, 이는 안전하지 않은 연산이다.

<!--
  <rdar://problem/28805121> TSPL: ARC - Add discussion of "unowned" with different lifetimes
  위의 예제를 확장하여 각 고객이 여러 신용카드를 가질 수 있도록 해 보자.
-->


### 소유하지 않은 옵셔널 참조

클래스에 대한 옵셔널 참조를 소유하지 않은(unowned) 것으로 표시할 수 있다. ARC 소유권 모델에서 소유하지 않은 옵셔널 참조와 약한(weak) 참조는 동일한 상황에서 사용할 수 있다. 차이점은 소유하지 않은 옵셔널 참조를 사용할 때, 항상 유효한 객체를 참조하거나 `nil`로 설정해야 할 책임이 있다는 점이다.

다음은 학교의 특정 학과에서 제공하는 강좌를 추적하는 예제이다:

```swift
class Department {
    var name: String
    var courses: [Course]
    init(name: String) {
        self.name = name
        self.courses = []
    }
}

class Course {
    var name: String
    unowned var department: Department
    unowned var nextCourse: Course?
    init(name: String, in department: Department) {
        self.name = name
        self.department = department
        self.nextCourse = nil
    }
}
```

`Department`는 학과에서 제공하는 각 강좌에 대한 강한 참조를 유지한다. ARC 소유권 모델에서 학과는 강좌를 소유한다. `Course`는 두 개의 소유하지 않은 참조를 가지는데, 하나는 학과를, 다른 하나는 학생이 다음에 들어야 할 강좌를 가리킨다. 강좌는 이 객체들 중 어느 것도 소유하지 않는다. 모든 강좌는 특정 학과에 속하므로 `department` 프로퍼티는 옵셔널이 아니다. 그러나 일부 강좌는 추천 후속 강좌가 없을 수 있으므로 `nextCourse` 프로퍼티는 옵셔널이다.

다음은 이 클래스들을 사용하는 예제이다:

```swift
let department = Department(name: "Horticulture")

let intro = Course(name: "Survey of Plants", in: department)
let intermediate = Course(name: "Growing Common Herbs", in: department)
let advanced = Course(name: "Caring for Tropical Plants", in: department)

intro.nextCourse = intermediate
intermediate.nextCourse = advanced
department.courses = [intro, intermediate, advanced]
```

위 코드는 학과와 세 개의 강좌를 생성한다. 입문 강좌와 중급 강좌는 각각 `nextCourse` 프로퍼티에 추천 후속 강좌를 저장한다. 이 프로퍼티는 학생이 해당 강좌를 마친 후 들어야 할 강좌에 대한 소유하지 않은 옵셔널 참조를 유지한다.

![](unownedOptionalReference)

소유하지 않은 옵셔널 참조는 감싸고 있는 클래스 인스턴스를 강하게 유지하지 않으므로, ARC가 인스턴스를 해제하는 것을 방해하지 않는다. ARC에서 소유하지 않은 참조와 동일하게 동작하지만, 소유하지 않은 옵셔널 참조는 `nil`이 될 수 있다.

옵셔널이 아닌 소유하지 않은 참조와 마찬가지로, `nextCourse`가 항상 해제되지 않은 강좌를 참조하도록 책임져야 한다. 예를 들어, `department.courses`에서 강좌를 삭제할 때, 다른 강좌가 해당 강좌를 참조하지 않도록 해야 한다.

> 참고: 옵셔널 값의 기본 타입은 `Optional`이며, 이는 Swift 표준 라이브러리의 열거형이다. 그러나 옵셔널은 값 타입에 `unowned`를 표시할 수 없다는 규칙의 예외이다.
>
> 클래스를 감싸는 옵셔널은 참조 카운팅을 사용하지 않으므로, 옵셔널에 대한 강한 참조를 유지할 필요가 없다.


### 소유되지 않은 참조와 암시적 언래핑 옵셔널 프로퍼티

앞서 살펴본 약한 참조와 소유되지 않은 참조는 강한 참조 순환을 끊어야 하는 두 가지 일반적인 상황을 다룬다.

`Person`과 `Apartment` 예제는 두 프로퍼티 모두 `nil`이 허용되면서 강한 참조 순환이 발생할 가능성이 있는 상황을 보여준다. 이 경우 약한 참조를 사용하는 것이 가장 적합하다.

`Customer`와 `CreditCard` 예제는 하나의 프로퍼티는 `nil`이 허용되고 다른 프로퍼티는 `nil`이 허용되지 않으면서 강한 참조 순환이 발생할 가능성이 있는 상황을 보여준다. 이 경우 소유되지 않은 참조를 사용하는 것이 가장 적합하다.

하지만 세 번째 시나리오도 있다. 이 시나리오에서는 두 프로퍼티 모두 항상 값을 가져야 하며, 초기화가 완료된 후에는 어느 프로퍼티도 `nil`이 되어서는 안 된다. 이 경우 한 클래스에는 소유되지 않은 프로퍼티를, 다른 클래스에는 암시적 언래핑 옵셔널 프로퍼티를 결합하는 것이 유용하다.

이렇게 하면 초기화가 완료된 후 두 프로퍼티 모두 옵셔널 언래핑 없이 직접 접근할 수 있으면서도 참조 순환을 피할 수 있다. 이 섹션에서는 이러한 관계를 설정하는 방법을 설명한다.

아래 예제는 두 클래스 `Country`와 `City`를 정의한다. 각 클래스는 다른 클래스의 인스턴스를 프로퍼티로 저장한다. 이 데이터 모델에서는 모든 국가는 항상 수도 도시를 가져야 하며, 모든 도시는 항상 국가에 속해야 한다. 이를 표현하기 위해 `Country` 클래스에는 `capitalCity` 프로퍼티가 있고, `City` 클래스에는 `country` 프로퍼티가 있다:

```swift
class Country {
    let name: String
    var capitalCity: City!
    init(name: String, capitalName: String) {
        self.name = name
        self.capitalCity = City(name: capitalName, country: self)
    }
}

class City {
    let name: String
    unowned let country: Country
    init(name: String, country: Country) {
        self.name = name
        self.country = country
    }
}
```

<!--
  - test: `implicitlyUnwrappedOptionals`

  ```swifttest
  -> class Country {
        let name: String
        var capitalCity: City!
        init(name: String, capitalName: String) {
           self.name = name
           self.capitalCity = City(name: capitalName, country: self)
        }
     }

  -> class City {
        let name: String
        unowned let country: Country
        init(name: String, country: Country) {
           self.name = name
           self.country = country
        }
     }
  ```
-->

두 클래스 간의 상호 의존성을 설정하기 위해 `City`의 초기화 메서드는 `Country` 인스턴스를 받아 `country` 프로퍼티에 저장한다.

`City`의 초기화 메서드는 `Country`의 초기화 메서드 내부에서 호출된다. 하지만 <doc:Initialization#Two-Phase-Initialization>에서 설명한 것처럼, 새로운 `Country` 인스턴스가 완전히 초기화되기 전까지는 `Country` 초기화 메서드가 `self`를 `City` 초기화 메서드에 전달할 수 없다.

이 요구 사항을 해결하기 위해 `Country`의 `capitalCity` 프로퍼티를 암시적 언래핑 옵셔널 프로퍼티로 선언한다. 이는 타입 어노테이션 끝에 느낌표(`City!`)를 붙여 표시한다. 이는 `capitalCity` 프로퍼티가 다른 옵셔널과 마찬가지로 기본값이 `nil`이지만, <doc:TheBasics#Implicitly-Unwrapped-Optionals>에서 설명한 것처럼 값을 언래핑하지 않고도 접근할 수 있음을 의미한다.

`capitalCity`가 기본적으로 `nil` 값을 가지기 때문에, `Country` 인스턴스는 초기화 메서드 내에서 `name` 프로퍼티를 설정하는 즉시 완전히 초기화된 것으로 간주된다. 이는 `Country` 초기화 메서드가 `name` 프로퍼티가 설정되자마자 암시적 `self` 프로퍼티를 참조하고 전달할 수 있음을 의미한다. 따라서 `Country` 초기화 메서드는 `capitalCity` 프로퍼티를 설정할 때 `self`를 `City` 초기화 메서드의 매개변수로 전달할 수 있다.

이 모든 것은 강한 참조 순환을 생성하지 않고도 `Country`와 `City` 인스턴스를 단일 문장으로 생성할 수 있으며, `capitalCity` 프로퍼티를 옵셔널 값을 언래핑하기 위해 느낌표를 사용하지 않고도 직접 접근할 수 있음을 의미한다:

```swift
var country = Country(name: "Canada", capitalName: "Ottawa")
print("\(country.name)'s capital city is called \(country.capitalCity.name)")
// Prints "Canada's capital city is called Ottawa"
```

<!--
  - test: `implicitlyUnwrappedOptionals`

  ```swifttest
  -> var country = Country(name: "Canada", capitalName: "Ottawa")
  -> print("\(country.name)'s capital city is called \(country.capitalCity.name)")
  <- Canada's capital city is called Ottawa
  ```
-->

위 예제에서 암시적 언래핑 옵셔널을 사용하면 두 단계 클래스 초기화 요구 사항이 모두 충족된다. 초기화가 완료되면 `capitalCity` 프로퍼티는 옵셔널이 아닌 값처럼 사용하고 접근할 수 있으면서도 강한 참조 순환을 피할 수 있다.


## 클로저에서 발생하는 강한 참조 순환

앞서 두 클래스 인스턴스 프로퍼티가 서로를 강하게 참조할 때 강한 참조 순환이 어떻게 발생하는지 살펴보았다. 또한 이러한 강한 참조 순환을 깨기 위해 약한 참조와 미소유 참조를 사용하는 방법도 배웠다.

강한 참조 순환은 클래스 인스턴스의 프로퍼티에 클로저를 할당하고, 그 클로저의 본문이 해당 인스턴스를 캡처할 때도 발생할 수 있다. 이 캡처는 클로저 본문이 `self.someProperty`와 같이 인스턴스의 프로퍼티에 접근하거나, `self.someMethod()`와 같이 인스턴스의 메서드를 호출할 때 일어난다. 두 경우 모두 이러한 접근은 클로저가 `self`를 캡처하게 만들고, 이로 인해 강한 참조 순환이 발생한다.

이 강한 참조 순환은 클로저가 클래스와 마찬가지로 *참조 타입*이기 때문에 발생한다. 클로저를 프로퍼티에 할당할 때, 실제로는 그 클로저에 대한 *참조*를 할당하는 것이다. 본질적으로 이 문제는 앞서 살펴본 것과 동일하다. 두 강한 참조가 서로를 살려두는 것이다. 다만 이번에는 두 클래스 인스턴스가 아니라, 클래스 인스턴스와 클로저가 서로를 살려두는 것이다.

Swift는 이 문제를 해결하기 위해 *클로저 캡처 리스트*라는 우아한 해결책을 제공한다. 하지만 클로저 캡처 리스트를 사용해 강한 참조 순환을 깨는 방법을 배우기 전에, 이러한 순환이 어떻게 발생하는지 이해하는 것이 유용하다.

아래 예제는 `self`를 참조하는 클로저를 사용할 때 강한 참조 순환을 어떻게 만들 수 있는지 보여준다. 이 예제는 HTML 문서 내의 개별 엘리먼트를 위한 간단한 모델을 제공하는 `HTMLElement`라는 클래스를 정의한다:

```swift
class HTMLElement {

    let name: String
    let text: String?

    lazy var asHTML: () -> String = {
        if let text = self.text {
            return "<\(self.name)>\(text)</\(self.name)>"
        } else {
            return "<\(self.name) />"
        }
    }

    init(name: String, text: String? = nil) {
        self.name = name
        self.text = text
    }

    deinit {
        print("\(name) is being deinitialized")
    }

}
```

`HTMLElement` 클래스는 `name` 프로퍼티를 정의한다. 이 프로퍼티는 엘리먼트의 이름을 나타내며, 예를 들어 제목 엘리먼트는 `"h1"`, 단락 엘리먼트는 `"p"`, 줄바꿈 엘리먼트는 `"br"` 등이 될 수 있다. `HTMLElement`는 또한 선택적 `text` 프로퍼티를 정의한다. 이 프로퍼티는 해당 HTML 엘리먼트 내에 렌더링될 텍스트를 나타내는 문자열로 설정할 수 있다.

이 두 간단한 프로퍼티 외에도, `HTMLElement` 클래스는 `asHTML`이라는 지연 저장 프로퍼티를 정의한다. 이 프로퍼티는 `name`과 `text`를 HTML 문자열 조각으로 결합하는 클로저를 참조한다. `asHTML` 프로퍼티의 타입은 `() -> String`이며, 이는 "매개변수를 받지 않고 `String` 값을 반환하는 함수"를 의미한다.

기본적으로 `asHTML` 프로퍼티는 HTML 태그의 문자열 표현을 반환하는 클로저가 할당된다. 이 태그는 `text` 값이 존재하면 해당 값을 포함하고, `text`가 존재하지 않으면 텍스트 내용을 포함하지 않는다. 예를 들어 단락 엘리먼트의 경우, `text` 프로퍼티가 `"some text"`인지 `nil`인지에 따라 클로저는 `"<p>some text</p>"` 또는 `"<p />"`를 반환한다.

`asHTML` 프로퍼티는 인스턴스 메서드처럼 이름이 지어지고 사용된다. 그러나 `asHTML`은 인스턴스 메서드가 아니라 클로저 프로퍼티이기 때문에, 특정 HTML 엘리먼트의 HTML 렌더링을 변경하려면 `asHTML` 프로퍼티의 기본 값을 커스텀 클로저로 대체할 수 있다.

예를 들어, `asHTML` 프로퍼티를 `text` 프로퍼티가 `nil`일 때 기본 텍스트를 사용하는 클로저로 설정할 수 있다. 이렇게 하면 빈 HTML 태그를 반환하지 않도록 방지할 수 있다:

```swift
let heading = HTMLElement(name: "h1")
let defaultText = "some default text"
heading.asHTML = {
    return "<\(heading.name)>\(heading.text ?? defaultText)</\(heading.name)>"
}
print(heading.asHTML())
// Prints "<h1>some default text</h1>"
```

> 참고: `asHTML` 프로퍼티는 지연 저장 프로퍼티로 선언된다. 이는 엘리먼트가 실제로 HTML 출력 대상으로 문자열 값으로 렌더링되어야 할 때만 필요하기 때문이다. `asHTML`이 지연 저장 프로퍼티라는 사실은 기본 클로저 내에서 `self`를 참조할 수 있음을 의미한다. 왜냐하면 지연 저장 프로퍼티는 초기화가 완료되고 `self`가 존재한다고 알려진 이후에야 접근되기 때문이다.

`HTMLElement` 클래스는 `name` 인자와 (필요한 경우) `text` 인자를 받아 새 엘리먼트를 초기화하는 단일 이니셜라이저를 제공한다. 또한 이 클래스는 `HTMLElement` 인스턴스가 해제될 때 메시지를 출력하는 디이니셜라이저를 정의한다.

다음은 `HTMLElement` 클래스를 사용해 새 인스턴스를 생성하고 출력하는 방법이다:

```swift
var paragraph: HTMLElement? = HTMLElement(name: "p", text: "hello, world")
print(paragraph!.asHTML())
// Prints "<p>hello, world</p>"
```

> 참고: 위의 `paragraph` 변수는 *옵셔널* `HTMLElement`로 정의된다. 이는 아래에서 강한 참조 순환의 존재를 보여주기 위해 `nil`로 설정할 수 있도록 하기 위함이다.

안타깝게도, 위와 같이 작성된 `HTMLElement` 클래스는 `HTMLElement` 인스턴스와 기본 `asHTML` 값을 위한 클로저 사이에 강한 참조 순환을 생성한다. 이 순환은 다음과 같이 나타난다:

![](closureReferenceCycle01)

인스턴스의 `asHTML` 프로퍼티는 클로저에 대한 강한 참조를 보유한다. 그러나 클로저는 본문 내에서 `self`를 참조하기 때문에 (즉, `self.name`과 `self.text`를 참조하기 위해), 클로저는 `self`를 *캡처*한다. 이는 클로저가 `HTMLElement` 인스턴스에 대한 강한 참조를 보유한다는 것을 의미한다. 결과적으로 두 사이에 강한 참조 순환이 생성된다. (클로저에서 값을 캡처하는 방법에 대한 자세한 내용은 <doc:Closures#Capturing-Values>를 참조하라.)

> 참고: 클로저가 `self`를 여러 번 참조하더라도, `HTMLElement` 인스턴스에 대한 강한 참조는 하나만 캡처된다.

`paragraph` 변수를 `nil`로 설정하고 `HTMLElement` 인스턴스에 대한 강한 참조를 끊더라도, 강한 참조 순환으로 인해 `HTMLElement` 인스턴스와 그 클로저 모두 해제되지 않는다:

```swift
paragraph = nil
```

`HTMLElement`의 디이니셜라이저에 있는 메시지가 출력되지 않는다는 점에 주목하라. 이는 `HTMLElement` 인스턴스가 해제되지 않았음을 보여준다.


## 클로저와 강한 참조 순환 문제 해결

클로저와 클래스 인스턴스 간의 강한 참조 순환 문제를 해결하려면 클로저 정의에 **캡처 리스트**를 추가한다. 캡처 리스트는 클로저 본문 내에서 하나 이상의 참조 타입을 캡처할 때 사용할 규칙을 정의한다. 두 클래스 인스턴스 간의 강한 참조 순환 문제와 마찬가지로, 각 캡처된 참조를 강한 참조 대신 약한 참조(weak) 또는 미소유 참조(unowned)로 선언한다. 약한 참조와 미소유 참조 중 어떤 것을 선택할지는 코드의 여러 부분 간의 관계에 따라 결정된다.

> 참고: Swift에서는 클로저 내에서 `self`의 멤버를 참조할 때 `self.someProperty` 또는 `self.someMethod()`와 같이 `self`를 명시적으로 작성해야 한다. 이렇게 하면 실수로 `self`를 캡처할 가능성을 상기시킬 수 있다.


### 캡처 리스트 정의하기

캡처 리스트의 각 항목은 `weak` 또는 `unowned` 키워드와 클래스 인스턴스에 대한 참조(예: `self`) 또는 특정 값으로 초기화된 변수(예: `delegate = self.delegate`)의 쌍으로 이루어진다. 이러한 쌍은 대괄호 안에 쉼표로 구분하여 작성한다.

클로저에 매개변수 목록과 반환 타입이 있는 경우, 캡처 리스트를 매개변수 목록과 반환 타입 앞에 위치시킨다:

```swift
lazy var someClosure = {
        [unowned self, weak delegate = self.delegate]
        (index: Int, stringToProcess: String) -> String in
    // 클로저 본문이 여기에 위치한다
}
```

<!--
  - test: `strongReferenceCyclesForClosures`

  ```swifttest
  >> class SomeClass {
  >> var delegate: AnyObject?
     lazy var someClosure = {
           [unowned self, weak delegate = self.delegate]
           (index: Int, stringToProcess: String) -> String in
        // 클로저 본문이 여기에 위치한다
  >>    return "foo"
     }
  >> }
  ```
-->

클로저가 매개변수 목록과 반환 타입을 지정하지 않고, 이를 컨텍스트에서 추론할 수 있는 경우, 캡처 리스트를 클로저의 가장 앞에 위치시키고 `in` 키워드를 붙인다:

```swift
lazy var someClosure = {
        [unowned self, weak delegate = self.delegate] in
    // 클로저 본문이 여기에 위치한다
}
```

<!--
  - test: `strongReferenceCyclesForClosures`

  ```swifttest
  >> class AnotherClass {
  >> var delegate: AnyObject?
     lazy var someClosure = {
           [unowned self, weak delegate = self.delegate] in
        // 클로저 본문이 여기에 위치한다
  >>    return "foo"
     }
  >> }
  ```
-->


### 약한 참조와 미소유 참조

클로저와 클로저가 캡처한 인스턴스가 항상 서로를 참조하고, 동시에 메모리에서 해제되는 경우에는 클로저 내에서 캡처를 미소유 참조로 정의한다.

반대로, 캡처한 참조가 나중에 `nil`이 될 가능성이 있다면 약한 참조로 정의한다. 약한 참조는 항상 옵셔널 타입이며, 참조한 인스턴스가 해제되면 자동으로 `nil`이 된다. 이를 통해 클로저 본문 내에서 해당 참조의 존재 여부를 확인할 수 있다.

<!--
  <rdar://problem/28812110> Reframe discussion of weak/unowned closure capture in terms of object graph
-->

> 참고: 캡처한 참조가 절대 `nil`이 되지 않는다면, 약한 참조 대신 항상 미소유 참조로 캡처해야 한다.

미소유 참조는 앞서 <doc:AutomaticReferenceCounting#Strong-Reference-Cycles-for-Closures>에서 다룬 `HTMLElement` 예제의 강한 참조 순환 문제를 해결하기에 적합한 캡처 방식이다. 다음은 순환을 방지하기 위해 `HTMLElement` 클래스를 작성하는 방법이다:

```swift
class HTMLElement {

    let name: String
    let text: String?

    lazy var asHTML: () -> String = {
            [unowned self] in
        if let text = self.text {
            return "<\(self.name)>\(text)</\(self.name)>"
        } else {
            return "<\(self.name) />"
        }
    }

    init(name: String, text: String? = nil) {
        self.name = name
        self.text = text
    }

    deinit {
        print("\(name) is being deinitialized")
    }

}
```

<!--
  - test: `unownedReferencesForClosures`

  ```swifttest
  -> class HTMLElement {

        let name: String
        let text: String?

        lazy var asHTML: () -> String = {
              [unowned self] in
           if let text = self.text {
              return "<\(self.name)>\(text)</\(self.name)>"
           } else {
              return "<\(self.name) />"
           }
        }

        init(name: String, text: String? = nil) {
           self.name = name
           self.text = text
        }

        deinit {
           print("\(name) is being deinitialized")
        }

     }
  ```
-->

이 `HTMLElement` 구현은 `asHTML` 클로저 내에 캡처 목록이 추가된 것을 제외하면 이전 구현과 동일하다. 여기서 캡처 목록은 `[unowned self]`로, "self를 강한 참조가 아닌 미소유 참조로 캡처하라"는 의미이다.

이전과 동일하게 `HTMLElement` 인스턴스를 생성하고 출력할 수 있다:

```swift
var paragraph: HTMLElement? = HTMLElement(name: "p", text: "hello, world")
print(paragraph!.asHTML())
// Prints "<p>hello, world</p>"
```

<!--
  - test: `unownedReferencesForClosures`

  ```swifttest
  -> var paragraph: HTMLElement? = HTMLElement(name: "p", text: "hello, world")
  -> print(paragraph!.asHTML())
  <- <p>hello, world</p>
  ```
-->

캡처 목록이 적용된 상태에서의 참조 관계는 다음과 같다:

![](closureReferenceCycle02)

이번에는 클로저가 `self`를 미소유 참조로 캡처하므로, 캡처한 `HTMLElement` 인스턴스를 강하게 유지하지 않는다. `paragraph` 변수의 강한 참조를 `nil`로 설정하면, `HTMLElement` 인스턴스가 해제되며, 아래 예제에서처럼 디이니셜라이저 메시지가 출력된다:

```swift
paragraph = nil
// Prints "p is being deinitialized"
```

<!--
  - test: `unownedReferencesForClosures`

  ```swifttest
  -> paragraph = nil
  <- p is being deinitialized
  ```
-->

캡처 목록에 대한 더 자세한 정보는 <doc:Expressions#Capture-Lists>를 참고한다.

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


