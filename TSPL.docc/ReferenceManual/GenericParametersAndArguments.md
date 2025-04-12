# 제네릭 타입과 인자

구체적인 타입을 추상화하기 위해 선언을 일반화한다.

이 장에서는 제네릭 타입, 함수, 이니셜라이저에 사용되는 파라미터와 인자에 대해 설명한다. 제네릭 타입, 함수, 서브스크립트, 이니셜라이저를 선언할 때, 해당 제네릭이 처리할 수 있는 타입 파라미터를 지정한다. 이 타입 파라미터는 플레이스홀더 역할을 하며, 제네릭 타입의 인스턴스가 생성되거나 제네릭 함수나 이니셜라이저가 호출될 때 실제 구체적인 타입 인자로 대체된다.

Swift에서 제네릭에 대한 개요는 <doc:Generics>를 참고한다.

<!--
  NOTE: 제네릭 타입은 때때로 :newTerm:`파라미터화된 타입`이라고도 불린다.
  하나 이상의 타입 파라미터로 선언되기 때문이다.
-->


## 제네릭 매개변수 절

**제네릭 매개변수 절**은 제네릭 타입이나 함수의 타입 매개변수를 정의한다. 이때 각 매개변수에 대한 제약 조건과 요구 사항을 함께 명시한다. 제네릭 매개변수 절은 꺾쇠 괄호(<>)로 둘러싸여 있으며, 다음과 같은 형태를 가진다.

```swift
<<#generic parameter list#>>
```

**제네릭 매개변수 목록**은 쉼표로 구분된 제네릭 매개변수들의 목록이다. 각 매개변수는 다음과 같은 형태를 가진다.

```swift
<#type parameter#>: <#constraint#>
```

제네릭 매개변수는 **타입 매개변수**와 선택적인 **제약 조건**으로 구성된다. **타입 매개변수**는 단순히 플레이스홀더 타입의 이름이다. 예를 들어 `T`, `U`, `V`, `Key`, `Value` 등이 있다. 타입 매개변수(그리고 관련된 타입들)는 해당 타입, 함수, 또는 초기화 선언의 나머지 부분에서 사용할 수 있다. 여기에는 함수나 초기화의 시그니처도 포함된다.

**제약 조건**은 타입 매개변수가 특정 클래스를 상속하거나 프로토콜 또는 프로토콜 조합을 준수해야 함을 명시한다. 예를 들어, 아래 제네릭 함수에서 `T: Comparable`은 타입 매개변수 `T`에 대체되는 모든 타입이 `Comparable` 프로토콜을 준수해야 함을 나타낸다.

```swift
func simpleMax<T: Comparable>(_ x: T, _ y: T) -> T {
    if x < y {
        return y
    }
    return x
}
```

<!--
  - test: `generic-params`

  ```swifttest
  -> func simpleMax<T: Comparable>(_ x: T, _ y: T) -> T {
        if x < y {
           return y
        }
        return x
     }
  ```
-->

예를 들어 `Int`와 `Double`은 모두 `Comparable` 프로토콜을 준수하므로, 이 함수는 두 타입의 인자를 모두 받을 수 있다. 제네릭 타입과 달리, 제네릭 함수나 초기화를 사용할 때는 제네릭 인자 절을 명시하지 않는다. 대신 함수나 초기화에 전달된 인자의 타입으로부터 타입 인자를 추론한다.

```swift
simpleMax(17, 42) // T는 Int로 추론됨
simpleMax(3.14159, 2.71828) // T는 Double로 추론됨
```

<!--
  - test: `generic-params`

  ```swifttest
  >> let r0 =
  -> simpleMax(17, 42) // T is inferred to be Int
  >> assert(r0 == 42)
  >> let r1 =
  -> simpleMax(3.14159, 2.71828) // T is inferred to be Double
  >> assert(r1 == 3.14159)
  ```
-->

<!--
  Rewrite the above to avoid bare expressions.
  Tracking bug is <rdar://problem/35301593>
-->


### 제네릭 Where 절

타입 매개변수와 관련 타입에 추가 요구사항을 지정하려면, 타입이나 함수의 본문을 여는 중괄호 바로 앞에 제네릭 `where` 절을 추가한다. 제네릭 `where` 절은 `where` 키워드 뒤에 쉼표로 구분된 하나 이상의 *요구사항* 목록으로 구성된다.

```swift
where <#requirements#>
```

제네릭 `where` 절의 *요구사항*은 타입 매개변수가 특정 클래스를 상속하거나 프로토콜 또는 프로토콜 조합을 준수하도록 지정한다. 제네릭 `where` 절은 타입 매개변수에 대한 간단한 제약 조건을 표현하는 데 사용할 수 있지만, 더 복잡한 제약 조건을 지정할 수도 있다. 예를 들어, 타입 매개변수의 관련 타입이 특정 프로토콜을 준수하도록 제약을 걸 수 있다. `<S: Sequence> where S.Iterator.Element: Equatable`는 `S`가 `Sequence` 프로토콜을 준수하고, `S.Iterator.Element`가 `Equatable` 프로토콜을 준수하도록 지정한다. 이 제약 조건은 시퀀스의 각 요소가 비교 가능하도록 보장한다.

또한 `==` 연산자를 사용해 두 타입이 동일해야 한다는 요구사항을 지정할 수 있다. 예를 들어, `<S1: Sequence, S2: Sequence> where S1.Iterator.Element == S2.Iterator.Element`는 `S1`과 `S2`가 `Sequence` 프로토콜을 준수하고, 두 시퀀스의 요소가 동일한 타입이어야 한다는 제약 조건을 표현한다.

타입 매개변수에 대체되는 모든 타입 인자는 해당 타입 매개변수에 부과된 모든 제약 조건과 요구사항을 충족해야 한다.

제네릭 `where` 절은 타입 매개변수를 포함하는 선언의 일부로 나타날 수 있으며, 타입 매개변수를 포함하는 선언 내부에 중첩된 선언의 일부로도 나타날 수 있다. 중첩된 선언의 제네릭 `where` 절은 여전히 외부 선언의 타입 매개변수를 참조할 수 있다. 그러나 해당 `where` 절의 요구사항은 해당 절이 작성된 선언에만 적용된다.

외부 선언에도 `where` 절이 있는 경우, 두 절의 요구사항이 결합된다. 아래 예제에서 `startsWithZero()`는 `Element`가 `SomeProtocol`과 `Numeric`을 모두 준수할 때만 사용할 수 있다.

```swift
extension Collection where Element: SomeProtocol {
    func startsWithZero() -> Bool where Element: Numeric {
        return first == .zero
    }
}
```

<!--
  - test: `contextual-where-clauses-combine`

  ```swifttest
  >> protocol SomeProtocol { }
  >> extension Int: SomeProtocol { }
  -> extension Collection where Element: SomeProtocol {
         func startsWithZero() -> Bool where Element: Numeric {
             return first == .zero
         }
     }
  >> print( [1, 2, 3].startsWithZero() )
  << false
  ```
-->

<!--
  - test: `contextual-where-clause-combine-err`

  ```swifttest
  >> protocol SomeProtocol { }
  >> extension Bool: SomeProtocol { }

  >> extension Collection where Element: SomeProtocol {
  >>     func returnTrue() -> Bool where Element == Bool {
  >>         return true
  >>     }
  >>     func returnTrue() -> Bool where Element == Int {
  >>         return true
  >>     }
  >> }
  !$ error: no type for 'Self.Element' can satisfy both 'Self.Element == Int' and 'Self.Element : SomeProtocol'
  !! func returnTrue() -> Bool where Element == Int {
  !!                                            ^
  ```
-->

제네릭 함수나 이니셜라이저를 오버로드하려면 타입 매개변수에 다른 제약 조건이나 요구사항을 제공할 수 있다. 오버로드된 제네릭 함수나 이니셜라이저를 호출할 때, 컴파일러는 이러한 제약 조건을 사용해 어떤 오버로드된 함수나 이니셜라이저를 호출할지 결정한다.

제네릭 `where` 절에 대한 더 자세한 정보와 제네릭 함수 선언에서의 예제는 <doc:Generics#Generic-Where-Clauses>를 참고한다.

> 제네릭 매개변수 절 문법:
>
> *generic-parameter-clause* → **`<`** *generic-parameter-list* **`>`** \
> *generic-parameter-list* → *generic-parameter* | *generic-parameter* **`,`** *generic-parameter-list* \
> *generic-parameter* → *type-name* \
> *generic-parameter* → *type-name* **`:`** *type-identifier* \
> *generic-parameter* → *type-name* **`:`** *protocol-composition-type*
>
> *generic-where-clause* → **`where`** *requirement-list* \
> *requirement-list* → *requirement* | *requirement* **`,`** *requirement-list* \
> *requirement* → *conformance-requirement* | *same-type-requirement*
>
> *conformance-requirement* → *type-identifier* **`:`** *type-identifier* \
> *conformance-requirement* → *type-identifier* **`:`** *protocol-composition-type* \
> *same-type-requirement* → *type-identifier* **`==`** *type*

<!--
  NOTE: A conformance requirement can only have one type after the colon,
  otherwise, you'd have a syntactic ambiguity
  (a comma-separated list types inside of a comma-separated list of requirements).
-->


## 제네릭 인자 절

*제네릭 인자 절*은 제네릭 타입의 타입 인자를 지정한다. 제네릭 인자 절은 꺾쇠 괄호(<>)로 둘러싸여 있으며, 다음과 같은 형태를 가진다:

```swift
<<#generic argument list#>>
```

*제네릭 인자 목록*은 쉼표로 구분된 타입 인자들의 목록이다. *타입 인자*는 제네릭 타입의 제네릭 매개변수 절에서 해당 타입 매개변수를 대체하는 실제 구체 타입의 이름이다. 이를 통해 해당 제네릭 타입의 특수화된 버전을 만들 수 있다. 아래 예제는 Swift 표준 라이브러리의 제네릭 Dictionary 타입을 간략화한 버전을 보여준다.

```swift
struct Dictionary<Key: Hashable, Value>: Collection, ExpressibleByDictionaryLiteral {
    /* ... */
}
```

<!--
  TODO: How are we supposed to wrap code lines like the above?
-->

제네릭 `Dictionary` 타입의 특수화된 버전인 `Dictionary<String, Int>`는 제네릭 매개변수 `Key: Hashable`과 `Value`를 구체 타입 인자인 `String`과 `Int`로 대체하여 만들어진다. 각 타입 인자는 대체하는 제네릭 매개변수의 모든 제약 조건을 충족해야 하며, 제네릭 `where` 절에서 지정된 추가 요구사항도 만족해야 한다. 위 예제에서 `Key` 타입 매개변수는 `Hashable` 프로토콜을 준수해야 하므로, `String`도 `Hashable` 프로토콜을 준수해야 한다.

타입 매개변수를 제네릭 타입의 특수화된 버전인 타입 인자로 대체할 수도 있다(해당 제약 조건과 요구사항을 충족한다면). 예를 들어, `Array<Element>`의 타입 매개변수 `Element`를 정수 배열의 특수화된 버전인 `Array<Int>`로 대체하여, 요소가 정수 배열인 배열을 만들 수 있다.

```swift
let arrayOfArrays: Array<Array<Int>> = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

<!--
  - test: `array-of-arrays`

  ```swifttest
  -> let arrayOfArrays: Array<Array<Int>> = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  ```
-->

<doc:GenericParametersAndArguments#Generic-Parameter-Clause>에서 언급했듯이, 제네릭 함수나 이니셜라이저의 타입 인자를 지정할 때는 제네릭 인자 절을 사용하지 않는다.

> 제네릭 인자 절 문법:
>
> *generic-argument-clause* → **`<`** *generic-argument-list* **`>`** \
> *generic-argument-list* → *generic-argument* | *generic-argument* **`,`** *generic-argument-list* \
> *generic-argument* → *type*

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


