# 제네릭

여러 타입에 대해 동작하는 코드를 작성하고, 해당 타입에 대한 요구사항을 명시할 수 있다.

**제네릭 코드**를 사용하면 정의한 요구사항을 충족하는 모든 타입에 대해 동작하는 유연하고 재사용 가능한 함수와 타입을 작성할 수 있다. 코드 중복을 피하고 의도를 명확하고 추상적으로 표현할 수 있다.

제네릭은 Swift의 가장 강력한 기능 중 하나이며, Swift 표준 라이브러리의 상당 부분이 제네릭 코드로 구성되어 있다. 사실, 여러분은 *Language Guide*를 통해 제네릭을 이미 사용하고 있었다. 예를 들어, Swift의 `Array`와 `Dictionary` 타입은 모두 제네릭 컬렉션이다. `Int` 값을 담는 배열을 만들거나, `String` 값을 담는 배열을 만들거나, Swift에서 생성할 수 있는 다른 어떤 타입의 배열도 만들 수 있다. 마찬가지로, 지정된 타입의 값을 저장하는 딕셔너리를 만들 수 있으며, 해당 타입에 대한 제한은 없다.


## 제네릭이 해결하는 문제

다음은 두 `Int` 값을 교환하는 `swapTwoInts(_:_:)`라는 일반적인 비제네릭 함수의 예시이다:

```swift
func swapTwoInts(_ a: inout Int, _ b: inout Int) {
    let temporaryA = a
    a = b
    b = temporaryA
}
```

<!--
  - test: `whyGenerics`

  ```swifttest
  -> func swapTwoInts(_ a: inout Int, _ b: inout Int) {
        let temporaryA = a
        a = b
        b = temporaryA
     }
  ```
-->

이 함수는 <doc:Functions#In-Out-Parameters>에서 설명한 대로 in-out 매개변수를 사용해 `a`와 `b`의 값을 교환한다.

`swapTwoInts(_:_:)` 함수는 `b`의 원래 값을 `a`에, `a`의 원래 값을 `b`에 할당한다. 이 함수를 호출해 두 `Int` 변수의 값을 교환할 수 있다:

```swift
var someInt = 3
var anotherInt = 107
swapTwoInts(&someInt, &anotherInt)
print("someInt is now \(someInt), and anotherInt is now \(anotherInt)")
// Prints "someInt is now 107, and anotherInt is now 3"
```

<!--
  - test: `whyGenerics`

  ```swifttest
  -> var someInt = 3
  -> var anotherInt = 107
  -> swapTwoInts(&someInt, &anotherInt)
  -> print("someInt is now \(someInt), and anotherInt is now \(anotherInt)")
  <- someInt is now 107, and anotherInt is now 3
  ```
-->

`swapTwoInts(_:_:)` 함수는 유용하지만 `Int` 값에만 사용할 수 있다. 만약 두 `String` 값을 교환하거나 두 `Double` 값을 교환하려면, 다음과 같이 `swapTwoStrings(_:_:)`와 `swapTwoDoubles(_:_:)` 함수를 추가로 작성해야 한다:

```swift
func swapTwoStrings(_ a: inout String, _ b: inout String) {
    let temporaryA = a
    a = b
    b = temporaryA
}

func swapTwoDoubles(_ a: inout Double, _ b: inout Double) {
    let temporaryA = a
    a = b
    b = temporaryA
}
```

<!--
  - test: `whyGenerics`

  ```swifttest
  -> func swapTwoStrings(_ a: inout String, _ b: inout String) {
        let temporaryA = a
        a = b
        b = temporaryA
     }

  -> func swapTwoDoubles(_ a: inout Double, _ b: inout Double) {
        let temporaryA = a
        a = b
        b = temporaryA
     }
  ```
-->

`swapTwoInts(_:_:)`, `swapTwoStrings(_:_:)`, `swapTwoDoubles(_:_:)` 함수의 본문이 동일하다는 것을 눈치챘을 것이다. 유일한 차이는 이 함수들이 받아들이는 값의 타입(`Int`, `String`, `Double`)이다.

*어떤* 타입의 두 값이라도 교환할 수 있는 단일 함수를 작성하는 것이 훨씬 유용하고 유연하다. 제네릭 코드는 이러한 함수를 작성할 수 있게 해준다. (이 함수들의 제네릭 버전은 아래에서 정의한다.)

> 주의: 이 세 함수에서 `a`와 `b`의 타입은 반드시 같아야 한다. `a`와 `b`의 타입이 다르면 값을 교환할 수 없다. Swift는 타입 안전한 언어이므로, 예를 들어 `String` 타입 변수와 `Double` 타입 변수가 서로 값을 교환하는 것을 허용하지 않는다. 이를 시도하면 컴파일 타임 오류가 발생한다.


## 제네릭 함수

**제네릭 함수**는 어떤 타입과도 동작할 수 있다. 앞서 살펴본 `swapTwoInts(_:_:)` 함수의 제네릭 버전인 `swapTwoValues(_:_:)` 함수를 보자:

```swift
func swapTwoValues<T>(_ a: inout T, _ b: inout T) {
    let temporaryA = a
    a = b
    b = temporaryA
}
```

`swapTwoValues(_:_:)` 함수의 본문은 `swapTwoInts(_:_:)` 함수와 동일하다. 그러나 `swapTwoValues(_:_:)` 함수의 첫 번째 줄은 `swapTwoInts(_:_:)`와 약간 다르다. 두 함수의 첫 번째 줄을 비교해 보자:

```swift
func swapTwoInts(_ a: inout Int, _ b: inout Int)
func swapTwoValues<T>(_ a: inout T, _ b: inout T)
```

제네릭 버전의 함수는 **실제 타입 이름**(예: `Int`, `String`, `Double`) 대신 **플레이스홀더** 타입 이름(여기서는 `T`)을 사용한다. 플레이스홀더 타입 이름은 `T`가 무엇이어야 하는지에 대해 명시하지 않지만, `a`와 `b`가 모두 동일한 타입 `T`여야 한다는 점은 분명히 한다. `T` 대신 사용할 실제 타입은 `swapTwoValues(_:_:)` 함수가 호출될 때마다 결정된다.

제네릭 함수와 비제네릭 함수의 또 다른 차이점은 제네릭 함수의 이름(`swapTwoValues(_:_:)`) 뒤에 꺾쇠 괄호(`<T>`) 안에 플레이스홀더 타입 이름(`T`)이 온다는 점이다. 이 괄호는 Swift에게 `T`가 `swapTwoValues(_:_:)` 함수 정의 내에서 플레이스홀더 타입 이름임을 알려준다. `T`가 플레이스홀더이기 때문에 Swift는 `T`라는 실제 타입을 찾지 않는다.

`swapTwoValues(_:_:)` 함수는 `swapTwoInts`와 동일한 방식으로 호출할 수 있지만, **어떤 타입**의 두 값도 전달할 수 있다. 단, 두 값은 서로 같은 타입이어야 한다. `swapTwoValues(_:_:)` 함수가 호출될 때마다, `T`로 사용할 타입은 함수에 전달된 값의 타입에서 추론된다.

아래 두 예제에서 `T`는 각각 `Int`와 `String`으로 추론된다:

```swift
var someInt = 3
var anotherInt = 107
swapTwoValues(&someInt, &anotherInt)
// someInt는 이제 107, anotherInt는 이제 3

var someString = "hello"
var anotherString = "world"
swapTwoValues(&someString, &anotherString)
// someString는 이제 "world", anotherString는 이제 "hello"
```

> 참고: 위에서 정의한 `swapTwoValues(_:_:)` 함수는 Swift 표준 라이브러리의 `swap`이라는 제네릭 함수에서 영감을 받았다. 이 함수는 앱에서 자동으로 사용할 수 있다. 만약 `swapTwoValues(_:_:)` 함수의 동작이 필요하다면, 직접 구현하지 않고 Swift의 기존 `swap(_:_:)` 함수를 사용할 수 있다.


## 타입 매개변수

앞서 살펴본 `swapTwoValues(_:_:)` 예제에서, 
플레이스홀더 타입 `T`는 *타입 매개변수*의 한 예시다. 
타입 매개변수는 플레이스홀더 타입을 지정하고 이름을 붙이며, 
함수 이름 바로 뒤에 꺾쇠 괄호(예: `<T>`)로 감싸서 작성한다.

타입 매개변수를 지정한 후에는 이를 활용해 
함수의 매개변수 타입(예: `swapTwoValues(_:_:)` 함수의 `a`와 `b` 매개변수), 
함수의 반환 타입, 
또는 함수 본문 내부의 타입 어노테이션을 정의할 수 있다. 
각 경우에 타입 매개변수는 함수가 호출될 때마다 *실제* 타입으로 대체된다. 
(앞서 언급한 `swapTwoValues(_:_:)` 예제에서, 
`T`는 함수가 처음 호출될 때 `Int`로, 
두 번째 호출될 때 `String`으로 대체되었다.)

꺾쇠 괄호 안에 여러 타입 매개변수 이름을 쉼표로 구분하여 작성하면, 
하나 이상의 타입 매개변수를 제공할 수 있다.


## 타입 매개변수 이름 지정

대부분의 경우, 타입 매개변수는 `Dictionary<Key, Value>`의 `Key`와 `Value`, 
또는 `Array<Element>`의 `Element`와 같이 설명적인 이름을 가진다. 
이러한 이름은 타입 매개변수와 해당 제네릭 타입 또는 함수 간의 관계를 명확히 보여준다. 
하지만, 둘 사이에 특별한 의미가 없는 경우에는 전통적으로 `T`, `U`, `V`와 같은 단일 문자를 사용해 이름을 짓는다. 
예를 들어, 앞서 살펴본 `swapTwoValues(_:_:)` 함수의 `T`가 그렇다.

타입 매개변수는 *타입*을 위한 자리 표시자이므로, `T`나 `MyTypeParameter`와 같이 대문자 카멜 케이스를 사용해 이름을 짓는다.

> 참고:  
> 타입 매개변수에 이름을 붙일 필요가 없고 제네릭 타입 제약이 간단한 경우,  
> <doc:OpaqueTypes#Opaque-Parameter-Types>에서 설명한 것처럼  
> 더 간단한 문법을 대신 사용할 수 있다.  
<!--
이 문법과 간단한 문법 간의 비교는  
Opaque Types 장에서 다룬다. 여기서는 다루지 않는다.  
아직 제약 조건에 대해 배우지 않았으므로,  
어떤 기능이 지원되는지 나열하는 것은 적절하지 않다.  
-->


## 제네릭 타입

제네릭 함수 외에도 Swift에서는 여러분이 직접 *제네릭 타입*을 정의할 수 있다. 이는 `Array`나 `Dictionary`와 유사하게 *어떤* 타입과도 함께 동작할 수 있는 커스텀 클래스, 구조체, 열거형을 의미한다.

이번 섹션에서는 `Stack`이라는 제네릭 컬렉션 타입을 작성하는 방법을 알아본다. 스택은 배열과 유사하게 순서가 있는 값들의 집합이지만, Swift의 `Array` 타입보다 더 제한된 연산 집합을 제공한다. 배열은 어느 위치에서나 새로운 항목을 삽입하거나 제거할 수 있지만, 스택은 컬렉션의 끝에만 새로운 항목을 추가할 수 있다(이를 *푸시(push)*라고 한다). 마찬가지로, 스택은 컬렉션의 끝에서만 항목을 제거할 수 있다(이를 *팝(pop)*이라고 한다).

> 참고: 스택 개념은 `UINavigationController` 클래스에서 네비게이션 계층 구조의 뷰 컨트롤러를 관리할 때 사용된다. `UINavigationController` 클래스의 `pushViewController(_:animated:)` 메서드를 호출해 뷰 컨트롤러를 네비게이션 스택에 추가하고, `popViewControllerAnimated(_:)` 메서드를 호출해 뷰 컨트롤러를 네비게이션 스택에서 제거한다. 스택은 컬렉션을 관리할 때 엄격한 "후입선출(LIFO)" 방식이 필요할 때 유용한 모델이다.

아래 그림은 스택의 푸시와 팝 동작을 보여준다:

![](stackPushPop)

1. 현재 스택에는 세 개의 값이 있다.
2. 네 번째 값이 스택의 맨 위에 푸시된다.
3. 스택은 이제 네 개의 값을 가지며, 가장 최근에 추가된 값이 맨 위에 있다.
4. 스택의 맨 위 항목이 팝된다.
5. 값을 팝한 후, 스택은 다시 세 개의 값을 가진다.

다음은 `Int` 값에 대한 스택의 비제네릭 버전을 작성한 예시다:

```swift
struct IntStack {
    var items: [Int] = []
    mutating func push(_ item: Int) {
        items.append(item)
    }
    mutating func pop() -> Int {
        return items.removeLast()
    }
}
```

이 구조체는 스택의 값을 저장하기 위해 `items`라는 `Array` 프로퍼티를 사용한다. 스택은 `push`와 `pop` 두 메서드를 제공해 값을 스택에 추가하거나 제거한다. 이 메서드들은 구조체의 `items` 배열을 수정해야 하므로 `mutating`으로 표시된다.

그러나 위의 `IntStack` 타입은 `Int` 값만 사용할 수 있다. *어떤* 타입의 값도 관리할 수 있는 *제네릭* `Stack` 구조체를 정의하는 것이 훨씬 더 유용할 것이다.

다음은 동일한 코드의 제네릭 버전이다:

```swift
struct Stack<Element> {
    var items: [Element] = []
    mutating func push(_ item: Element) {
        items.append(item)
    }
    mutating func pop() -> Element {
        return items.removeLast()
    }
}
```

제네릭 버전의 `Stack`은 기본적으로 비제네릭 버전과 동일하지만, `Int` 대신 `Element`라는 타입 매개변수를 사용한다. 이 타입 매개변수는 구조체 이름 바로 뒤에 꺾쇠 괄호(`<Element>`) 안에 작성된다.

`Element`는 나중에 제공될 타입에 대한 플레이스홀더 이름을 정의한다. 이 미래의 타입은 구조체 정의 내 어디에서나 `Element`로 참조될 수 있다. 이 경우, `Element`는 세 곳에서 플레이스홀더로 사용된다:

- `Element` 타입의 값으로 초기화된 빈 배열인 `items` 프로퍼티를 생성할 때
- `push(_:)` 메서드가 `Element` 타입의 `item`이라는 단일 매개변수를 가져야 함을 지정할 때
- `pop()` 메서드가 반환하는 값이 `Element` 타입이어야 함을 지정할 때

제네릭 타입이기 때문에 `Stack`은 Swift에서 *어떤* 유효한 타입과도 함께 사용될 수 있으며, `Array`와 `Dictionary`와 유사한 방식으로 동작한다.

스택에 저장할 타입을 꺾쇠 괄호 안에 작성해 새로운 `Stack` 인스턴스를 생성한다. 예를 들어, 문자열 스택을 생성하려면 `Stack<String>()`을 작성한다:

```swift
var stackOfStrings = Stack<String>()
stackOfStrings.push("uno")
stackOfStrings.push("dos")
stackOfStrings.push("tres")
stackOfStrings.push("cuatro")
// 스택은 이제 4개의 문자열을 포함한다
```

다음은 네 개의 값을 스택에 푸시한 후의 `stackOfStrings` 모습이다:

![](stackPushedFourStrings)

스택에서 값을 팝하면 맨 위의 값인 `"cuatro"`가 제거되고 반환된다:

```swift
let fromTheTop = stackOfStrings.pop()
// fromTheTop은 "cuatro"이며, 스택은 이제 3개의 문자열을 포함한다
```

다음은 맨 위의 값을 팝한 후의 스택 모습이다:

![](stackPoppedOneString)


## 제네릭 타입 확장하기

제네릭 타입을 확장할 때는 확장 정의 부분에 타입 매개변수 목록을 제공하지 않는다. 대신, *원본* 타입 정의의 타입 매개변수 목록이 확장 본문 내에서 사용 가능하며, 원본 타입 매개변수 이름을 통해 원본 정의의 타입 매개변수를 참조한다.

다음 예제는 제네릭 `Stack` 타입을 확장하여 `topItem`이라는 읽기 전용 계산 프로퍼티를 추가한다. 이 프로퍼티는 스택에서 가장 위에 있는 항목을 반환하지만, 스택에서 제거하지는 않는다.

```swift
extension Stack {
    var topItem: Element? {
        return items.isEmpty ? nil : items[items.count - 1]
    }
}
```

<!--
  - test: `genericStack`

  ```swifttest
  -> extension Stack {
        var topItem: Element? {
           return items.isEmpty ? nil : items[items.count - 1]
        }
     }
  ```
-->

`topItem` 프로퍼티는 `Element` 타입의 옵셔널 값을 반환한다. 스택이 비어 있으면 `topItem`은 `nil`을 반환하고, 스택이 비어 있지 않으면 `items` 배열의 마지막 항목을 반환한다.

이 확장은 타입 매개변수 목록을 정의하지 않는다. 대신, `Stack` 타입의 기존 타입 매개변수 이름인 `Element`를 확장 내에서 사용하여 `topItem` 계산 프로퍼티의 옵셔널 타입을 나타낸다.

이제 `topItem` 계산 프로퍼티는 모든 `Stack` 인스턴스에서 사용할 수 있으며, 스택의 가장 위에 있는 항목을 제거하지 않고 접근하고 조회할 수 있다.

```swift
if let topItem = stackOfStrings.topItem {
    print("The top item on the stack is \(topItem).")
}
// Prints "The top item on the stack is tres."
```

<!--
  - test: `genericStack`

  ```swifttest
  -> if let topItem = stackOfStrings.topItem {
        print("The top item on the stack is \(topItem).")
     }
  <- The top item on the stack is tres.
  ```
-->

제네릭 타입의 확장은 새로운 기능을 얻기 위해 확장된 타입의 인스턴스가 충족해야 하는 요구사항을 포함할 수도 있다. 이에 대한 자세한 내용은 아래 <doc:Generics#Extensions-with-a-Generic-Where-Clause>에서 다룬다.


## 타입 제약

`swapTwoValues(_:_:)` 함수와 `Stack` 타입은 모든 타입과 함께 작동할 수 있다. 하지만 제네릭 함수와 제네릭 타입에 사용할 수 있는 타입에 특정 *타입 제약*을 적용하는 것이 유용할 때가 있다. 타입 제약은 타입 매개변수가 특정 클래스를 상속하거나, 특정 프로토콜 또는 프로토콜 조합을 준수해야 한다는 것을 지정한다.

예를 들어, Swift의 `Dictionary` 타입은 딕셔너리의 키로 사용할 수 있는 타입에 제한을 둔다. <doc:CollectionTypes#Dictionaries>에서 설명한 것처럼, 딕셔너리의 키 타입은 *해시 가능*해야 한다. 즉, 키가 자신을 고유하게 표현할 수 있는 방법을 제공해야 한다. `Dictionary`는 특정 키에 대한 값이 이미 존재하는지 확인하기 위해 키가 해시 가능해야 한다. 이 요구 사항이 없다면, `Dictionary`는 특정 키에 대한 값을 삽입해야 할지, 아니면 교체해야 할지 결정할 수 없으며, 이미 딕셔너리에 있는 키에 대한 값을 찾을 수도 없다.

이 요구 사항은 `Dictionary`의 키 타입에 대한 타입 제약으로 강제된다. 이 제약은 키 타입이 Swift 표준 라이브러리에 정의된 특별한 프로토콜인 `Hashable` 프로토콜을 준수해야 한다는 것을 지정한다. Swift의 기본 타입(예: `String`, `Int`, `Double`, `Bool`)은 모두 기본적으로 해시 가능하다. 커스텀 타입이 `Hashable` 프로토콜을 준수하도록 만드는 방법에 대한 자세한 내용은 [Conforming to the Hashable Protocol](https://developer.apple.com/documentation/swift/hashable#2849490)을 참고한다.

커스텀 제네릭 타입을 생성할 때 자신만의 타입 제약을 정의할 수 있으며, 이러한 제약은 제네릭 프로그래밍의 강력한 기능을 제공한다. `Hashable`과 같은 추상적인 개념은 구체적인 타입이 아니라 개념적 특성에 따라 타입을 특성화한다.


### 타입 제약 문법

타입 제약을 작성할 때는 타입 매개변수 이름 뒤에 콜론을 붙이고, 단일 클래스나 프로토콜 제약을 추가한다. 이는 타입 매개변수 목록의 일부로 작성된다. 제네릭 함수에 대한 타입 제약의 기본 문법은 다음과 같다(제네릭 타입에서도 동일한 문법을 사용한다):

```swift
func someFunction<T: SomeClass, U: SomeProtocol>(someT: T, someU: U) {
    // function body goes here
}
```

<!--
  - test: `typeConstraints`

  ```swifttest
  >> class SomeClass {}
  >> protocol SomeProtocol {}
  -> func someFunction<T: SomeClass, U: SomeProtocol>(someT: T, someU: U) {
        // function body goes here
     }
  ```
-->

위의 가상 함수는 두 개의 타입 매개변수를 가지고 있다. 첫 번째 타입 매개변수 `T`는 `SomeClass`의 하위 클래스여야 한다는 타입 제약을 가지고 있다. 두 번째 타입 매개변수 `U`는 `SomeProtocol`을 준수해야 한다는 타입 제약을 가지고 있다.


### 타입 제약 조건의 활용

`findIndex(ofString:in:)`이라는 비제네릭 함수가 있다. 이 함수는 찾을 `String` 값과 그 값을 찾을 `String` 배열을 인자로 받는다. `findIndex(ofString:in:)` 함수는 옵셔널 `Int` 값을 반환한다. 배열에서 첫 번째로 일치하는 문자열의 인덱스를 반환하거나, 문자열을 찾지 못하면 `nil`을 반환한다.

```swift
func findIndex(ofString valueToFind: String, in array: [String]) -> Int? {
    for (index, value) in array.enumerated() {
        if value == valueToFind {
            return index
        }
    }
    return nil
}
```

<!--
  - test: `typeConstraints`

  ```swifttest
  -> func findIndex(ofString valueToFind: String, in array: [String]) -> Int? {
        for (index, value) in array.enumerated() {
           if value == valueToFind {
              return index
           }
        }
        return nil
     }
  ```
-->

`findIndex(ofString:in:)` 함수는 문자열 배열에서 특정 문자열 값을 찾는 데 사용할 수 있다:

```swift
let strings = ["cat", "dog", "llama", "parakeet", "terrapin"]
if let foundIndex = findIndex(ofString: "llama", in: strings) {
    print("The index of llama is \(foundIndex)")
}
// Prints "The index of llama is 2"
```

<!--
  - test: `typeConstraints`

  ```swifttest
  -> let strings = ["cat", "dog", "llama", "parakeet", "terrapin"]
  -> if let foundIndex = findIndex(ofString: "llama", in: strings) {
        print("The index of llama is \(foundIndex)")
     }
  <- The index of llama is 2
  ```
-->

배열에서 특정 값의 인덱스를 찾는 원리는 문자열에만 국한되지 않는다. 문자열을 특정 타입 `T`의 값으로 대체하면 동일한 기능을 제네릭 함수로 작성할 수 있다.

`findIndex(ofString:in:)`의 제네릭 버전인 `findIndex(of:in:)`을 작성해보자. 이 함수의 반환 타입은 여전히 `Int?`다. 함수는 배열의 값을 반환하는 것이 아니라 옵셔널 인덱스 번호를 반환하기 때문이다. 하지만 이 함수는 컴파일되지 않는다. 그 이유는 예제 뒤에 설명한다.

```swift
func findIndex<T>(of valueToFind: T, in array:[T]) -> Int? {
    for (index, value) in array.enumerated() {
        if value == valueToFind {
            return index
        }
    }
    return nil
}
```

<!--
  - test: `typeConstraints-err`

  ```swifttest
  -> func findIndex<T>(of valueToFind: T, in array:[T]) -> Int? {
        for (index, value) in array.enumerated() {
           if value == valueToFind {
              return index
           }
        }
        return nil
     }
  !$ error: binary operator '==' cannot be applied to two 'T' operands
  !!       if value == valueToFind {
  !!          ~~~~~ ^  ~~~~~~~~~~~
  ```
-->

이 함수는 위와 같이 작성하면 컴파일되지 않는다. 문제는 동등성 비교인 "`if value == valueToFind`"에 있다. Swift의 모든 타입이 동등 연산자(`==`)로 비교할 수 있는 것은 아니다. 예를 들어 복잡한 데이터 모델을 나타내는 클래스나 구조체를 만들면, 해당 클래스나 구조체에 대한 "동등"의 의미를 Swift가 추측할 수 없다. 따라서 이 코드가 *모든* 가능한 타입 `T`에 대해 동작한다고 보장할 수 없으며, 코드를 컴파일하려고 하면 적절한 오류가 발생한다.

하지만 모든 것이 손실된 것은 아니다. Swift 표준 라이브러리는 `Equatable`이라는 프로토콜을 정의한다. 이 프로토콜은 준수하는 모든 타입이 동등 연산자(`==`)와 부등 연산자(`!=`)를 구현하도록 요구한다. Swift의 모든 표준 타입은 자동으로 `Equatable` 프로토콜을 지원한다.

`Equatable`을 준수하는 모든 타입은 `findIndex(of:in:)` 함수와 함께 안전하게 사용할 수 있다. 동등 연산자를 지원한다는 것이 보장되기 때문이다. 이 사실을 표현하기 위해 함수를 정의할 때 타입 매개변수의 정의에 `Equatable` 타입 제약 조건을 추가한다:

```swift
func findIndex<T: Equatable>(of valueToFind: T, in array:[T]) -> Int? {
    for (index, value) in array.enumerated() {
        if value == valueToFind {
            return index
        }
    }
    return nil
}
```

<!--
  - test: `typeConstraintsEquatable`

  ```swifttest
  -> func findIndex<T: Equatable>(of valueToFind: T, in array:[T]) -> Int? {
        for (index, value) in array.enumerated() {
           if value == valueToFind {
              return index
           }
        }
        return nil
     }
  ```
-->

`findIndex(of:in:)`의 단일 타입 매개변수는 `T: Equatable`로 작성된다. 이는 "`Equatable` 프로토콜을 준수하는 모든 타입 `T`"를 의미한다.

이제 `findIndex(of:in:)` 함수는 성공적으로 컴파일되며, `Double`이나 `String`과 같이 `Equatable`을 준수하는 모든 타입과 함께 사용할 수 있다:

```swift
let doubleIndex = findIndex(of: 9.3, in: [3.14159, 0.1, 0.25])
// doubleIndex는 옵셔널 Int이며 값이 없다. 배열에 9.3이 없기 때문이다.
let stringIndex = findIndex(of: "Andrea", in: ["Mike", "Malcolm", "Andrea"])
// stringIndex는 값이 2인 옵셔널 Int다.
```

<!--
  - test: `typeConstraintsEquatable`

  ```swifttest
  -> let doubleIndex = findIndex(of: 9.3, in: [3.14159, 0.1, 0.25])
  /> doubleIndex는 옵셔널 Int이며 값이 없다. 배열에 9.3이 없기 때문이다.
  </ doubleIndex는 옵셔널 Int이며 값이 없다. 배열에 9.3이 없기 때문이다.
  -> let stringIndex = findIndex(of: "Andrea", in: ["Mike", "Malcolm", "Andrea"])
  /> stringIndex는 값이 \(stringIndex!)인 옵셔널 Int다.
  </ stringIndex는 값이 2인 옵셔널 Int다.
  ```
-->


## 연관 타입

프로토콜을 정의할 때, 프로토콜의 일부로 하나 이상의 연관 타입을 선언하는 것이 유용할 때가 있다. *연관 타입*은 프로토콜 내에서 사용될 타입에 대한 플레이스홀더 이름을 제공한다. 이 연관 타입에 사용될 실제 타입은 프로토콜이 채택될 때까지 지정되지 않는다. 연관 타입은 `associatedtype` 키워드를 사용해 지정한다.


### 연관 타입(Associated Types)의 활용

다음은 `Container`라는 프로토콜 예제로, `Item`이라는 연관 타입을 선언한다:

```swift
protocol Container {
    associatedtype Item
    mutating func append(_ item: Item)
    var count: Int { get }
    subscript(i: Int) -> Item { get }
}
```

<!--
  - test: `associatedTypes, associatedTypes-err`

  ```swifttest
  -> protocol Container {
        associatedtype Item
        mutating func append(_ item: Item)
        var count: Int { get }
        subscript(i: Int) -> Item { get }
     }
  ```
-->

`Container` 프로토콜은 모든 컨테이너가 제공해야 하는 세 가지 필수 기능을 정의한다:

- `append(_:)` 메서드를 통해 새로운 아이템을 컨테이너에 추가할 수 있어야 한다.
- `count` 프로퍼티를 통해 컨테이너 내 아이템의 개수를 `Int` 값으로 반환할 수 있어야 한다.
- `Int` 인덱스 값을 사용해 컨테이너 내 각 아이템을 조회할 수 있는 서브스크립트를 제공해야 한다.

이 프로토콜은 컨테이너 내 아이템이 어떻게 저장되어야 하는지, 또는 어떤 타입이 허용되는지 명시하지 않는다. 프로토콜은 단순히 `Container`로 간주되기 위해 제공해야 하는 세 가지 기능만을 정의한다. 이 세 가지 요구사항을 충족하는 한, 해당 타입은 추가적인 기능을 제공할 수 있다.

`Container` 프로토콜을 준수하는 모든 타입은 저장하는 값의 타입을 명시할 수 있어야 한다. 구체적으로, 올바른 타입의 아이템만 컨테이너에 추가되도록 보장해야 하며, 서브스크립트가 반환하는 아이템의 타입이 명확해야 한다.

이러한 요구사항을 정의하기 위해, `Container` 프로토콜은 특정 컨테이너의 타입을 알지 못한 상태에서도 컨테이너가 보유할 요소의 타입을 참조할 수 있는 방법이 필요하다. `Container` 프로토콜은 `append(_:)` 메서드에 전달된 값이 컨테이너의 요소 타입과 동일한 타입이어야 하며, 컨테이너의 서브스크립트가 반환하는 값도 동일한 타입이어야 함을 명시해야 한다.

이를 위해 `Container` 프로토콜은 `associatedtype Item`으로 작성된 `Item`이라는 연관 타입을 선언한다. 프로토콜은 `Item`이 무엇인지 정의하지 않는다. 이 정보는 준수하는 타입이 제공하도록 남겨둔다. 그럼에도 불구하고, `Item` 별칭은 `Container` 내 아이템의 타입을 참조할 수 있는 방법을 제공하며, `append(_:)` 메서드와 서브스크립트에 사용할 타입을 정의해 모든 `Container`의 예상 동작이 강제되도록 한다.

다음은 앞서 <doc:Generics#Generic-Types>에서 다룬 비제네릭 `IntStack` 타입을 `Container` 프로토콜에 맞게 수정한 버전이다:

```swift
struct IntStack: Container {
    // 원래 IntStack 구현
    var items: [Int] = []
    mutating func push(_ item: Int) {
        items.append(item)
    }
    mutating func pop() -> Int {
        return items.removeLast()
    }
    // Container 프로토콜 준수
    typealias Item = Int
    mutating func append(_ item: Int) {
        self.push(item)
    }
    var count: Int {
        return items.count
    }
    subscript(i: Int) -> Int {
        return items[i]
    }
}
```

<!--
  - test: `associatedTypes`

  ```swifttest
  -> struct IntStack: Container {
        // 원래 IntStack 구현
        var items: [Int] = []
        mutating func push(_ item: Int) {
           items.append(item)
        }
        mutating func pop() -> Int {
           return items.removeLast()
        }
        // Container 프로토콜 준수
        typealias Item = Int
        mutating func append(_ item: Int) {
           self.push(item)
        }
        var count: Int {
           return items.count
        }
        subscript(i: Int) -> Int {
           return items[i]
        }
     }
  ```
-->

`IntStack` 타입은 `Container` 프로토콜의 세 가지 요구사항을 모두 구현하며, 각각의 경우에 `IntStack` 타입의 기존 기능을 활용해 이를 충족시킨다.

또한, `IntStack`은 `Container`의 이 구현에서 사용할 적절한 `Item`이 `Int` 타입임을 명시한다. `typealias Item = Int` 정의는 `Item`이라는 추상 타입을 `Container` 프로토콜의 이 구현에서 `Int`라는 구체적인 타입으로 변환한다.

Swift의 타입 추론 덕분에, 실제로 `IntStack`의 정의에서 `Int` 타입의 구체적인 `Item`을 선언할 필요는 없다. `IntStack`이 `Container` 프로토콜의 모든 요구사항을 준수하기 때문에, Swift는 `append(_:)` 메서드의 `item` 매개변수 타입과 서브스크립트의 반환 타입을 살펴보면 적절한 `Item`을 추론할 수 있다. 실제로 위 코드에서 `typealias Item = Int` 줄을 삭제해도 모든 것이 정상적으로 작동한다. 왜냐하면 `Item`에 사용할 타입이 명확하기 때문이다.

제네릭 `Stack` 타입도 `Container` 프로토콜을 준수하도록 만들 수 있다:

```swift
struct Stack<Element>: Container {
    // 원래 Stack<Element> 구현
    var items: [Element] = []
    mutating func push(_ item: Element) {
        items.append(item)
    }
    mutating func pop() -> Element {
        return items.removeLast()
    }
    // Container 프로토콜 준수
    mutating func append(_ item: Element) {
        self.push(item)
    }
    var count: Int {
        return items.count
    }
    subscript(i: Int) -> Element {
        return items[i]
    }
}
```

<!--
  - test: `associatedTypes, associatedTypes-err`

  ```swifttest
  -> struct Stack<Element>: Container {
        // 원래 Stack<Element> 구현
        var items: [Element] = []
        mutating func push(_ item: Element) {
           items.append(item)
        }
        mutating func pop() -> Element {
           return items.removeLast()
        }
        // Container 프로토콜 준수
        mutating func append(_ item: Element) {
           self.push(item)
        }
        var count: Int {
           return items.count
        }
        subscript(i: Int) -> Element {
           return items[i]
        }
     }
  ```
-->

이번에는 타입 매개변수 `Element`가 `append(_:)` 메서드의 `item` 매개변수 타입과 서브스크립트의 반환 타입으로 사용된다. 따라서 Swift는 `Element`가 이 특정 컨테이너의 `Item`으로 사용하기에 적절한 타입임을 추론할 수 있다.


### 기존 타입을 확장하여 연관 타입 지정하기

기존 타입을 확장해 프로토콜을 준수하도록 추가할 수 있다. 이는 연관 타입(associated type)을 포함한 프로토콜에도 적용된다.

Swift의 `Array` 타입은 이미 `append(_:)` 메서드, `count` 프로퍼티, 그리고 `Int` 인덱스를 사용해 요소를 조회하는 서브스크립트를 제공한다. 이 세 가지 기능은 `Container` 프로토콜의 요구 사항과 일치한다. 따라서 `Array`가 `Container` 프로토콜을 준수하도록 간단히 선언하기만 하면 된다. 이는 빈 확장을 통해 수행할 수 있다.

```swift
extension Array: Container {}
```

`Array`의 기존 `append(_:)` 메서드와 서브스크립트는 Swift가 `Item`에 사용할 적절한 타입을 추론할 수 있도록 한다. 이 확장을 정의한 후에는 모든 `Array`를 `Container`로 사용할 수 있다.


### 연관 타입에 제약 조건 추가하기

프로토콜의 연관 타입에 타입 제약을 추가하여, 해당 프로토콜을 준수하는 타입이 특정 조건을 만족하도록 요구할 수 있다. 예를 들어, 다음 코드는 컨테이너 내의 항목이 `Equatable`을 준수해야 하는 `Container` 프로토콜의 버전을 정의한다.

```swift
protocol Container {
    associatedtype Item: Equatable
    mutating func append(_ item: Item)
    var count: Int { get }
    subscript(i: Int) -> Item { get }
}
```

<!--
  - test: `associatedTypes-equatable`

  ```swifttest
  -> protocol Container {
        associatedtype Item: Equatable
        mutating func append(_ item: Item)
        var count: Int { get }
        subscript(i: Int) -> Item { get }
     }
  ```
-->

이 버전의 `Container` 프로토콜을 준수하려면, 컨테이너의 `Item` 타입이 `Equatable` 프로토콜을 준수해야 한다.


### 프로토콜을 연관 타입의 제약 조건으로 사용하기

프로토콜은 자신의 요구 사항의 일부로 나타날 수 있다. 예를 들어, 다음은 `Container` 프로토콜을 확장하여 `suffix(_:)` 메서드를 추가한 프로토콜이다. `suffix(_:)` 메서드는 컨테이너의 끝에서 지정된 수의 요소를 반환하며, 이를 `Suffix` 타입의 인스턴스에 저장한다.

```swift
protocol SuffixableContainer: Container {
    associatedtype Suffix: SuffixableContainer where Suffix.Item == Item
    func suffix(_ size: Int) -> Suffix
}
```

<!--
  - test: `associatedTypes`

  ```swifttest
  -> protocol SuffixableContainer: Container {
         associatedtype Suffix: SuffixableContainer where Suffix.Item == Item
         func suffix(_ size: Int) -> Suffix
     }
  ```
-->

이 프로토콜에서 `Suffix`는 앞서 `Container` 예제의 `Item` 타입과 같은 연관 타입이다. `Suffix`에는 두 가지 제약 조건이 있다: 첫째, `SuffixableContainer` 프로토콜을 준수해야 하며(현재 정의 중인 프로토콜), 둘째, `Item` 타입이 컨테이너의 `Item` 타입과 동일해야 한다. `Item`에 대한 제약 조건은 제네릭 `where` 절로, 이에 대해서는 <doc:Generics#Associated-Types-with-a-Generic-Where-Clause>에서 자세히 다룬다.

다음은 앞서 <doc:Generics#Generic-Types>에서 소개한 `Stack` 타입을 `SuffixableContainer` 프로토콜에 맞게 확장한 예제이다:

```swift
extension Stack: SuffixableContainer {
    func suffix(_ size: Int) -> Stack {
        var result = Stack()
        for index in (count-size)..<count {
            result.append(self[index])
        }
        return result
    }
    // Inferred that Suffix is Stack.
}
var stackOfInts = Stack<Int>()
stackOfInts.append(10)
stackOfInts.append(20)
stackOfInts.append(30)
let suffix = stackOfInts.suffix(2)
// suffix contains 20 and 30
```

<!--
  - test: `associatedTypes`

  ```swifttest
  -> extension Stack: SuffixableContainer {
         func suffix(_ size: Int) -> Stack {
             var result = Stack()
             for index in (count-size)..<count {
                 result.append(self[index])
             }
             return result
         }
         // Inferred that Suffix is Stack.
     }
  -> var stackOfInts = Stack<Int>()
  -> stackOfInts.append(10)
  -> stackOfInts.append(20)
  -> stackOfInts.append(30)
  >> assert(stackOfInts.suffix(0).items == [])
  -> let suffix = stackOfInts.suffix(2)
  // suffix contains 20 and 30
  >> assert(suffix.items == [20, 30])
  ```
-->

위 예제에서 `Stack`의 `Suffix` 연관 타입은 `Stack` 자체이다. 따라서 `Stack`에 대한 `suffix` 연산은 또 다른 `Stack`을 반환한다. 반면, `SuffixableContainer`를 준수하는 타입은 `Suffix` 타입이 자신과 다를 수 있다. 즉, `suffix` 연산이 다른 타입을 반환할 수 있다는 의미이다. 예를 들어, 다음은 제네릭이 아닌 `IntStack` 타입을 `SuffixableContainer`에 맞게 확장한 예제로, `IntStack` 대신 `Stack<Int>`를 `Suffix` 타입으로 사용한다:

```swift
extension IntStack: SuffixableContainer {
    func suffix(_ size: Int) -> Stack<Int> {
        var result = Stack<Int>()
        for index in (count-size)..<count {
            result.append(self[index])
        }
        return result
    }
    // Inferred that Suffix is Stack<Int>.
}
```

<!--
  - test: `associatedTypes`

  ```swifttest
  -> extension IntStack: SuffixableContainer {
         func suffix(_ size: Int) -> Stack<Int> {
             var result = Stack<Int>()
             for index in (count-size)..<count {
                 result.append(self[index])
             }
             return result
         }
         // Inferred that Suffix is Stack<Int>.
     }
  >> var intStack = IntStack()
  >> intStack.append(10)
  >> intStack.append(20)
  >> intStack.append(30)
  >> assert(intStack.suffix(0).items == [])
  >> assert(intStack.suffix(2).items == [20, 30])
  ```
-->


## 일반화된 Where 절

<doc:Generics#Type-Constraints>에서 설명한 타입 제약은 제네릭 함수, 서브스크립트, 타입과 관련된 타입 파라미터에 요구사항을 정의할 수 있게 한다.

이와 유사하게, 연관 타입에 대한 요구사항을 정의하는 것도 유용하다. 이를 위해 *일반화된 where 절*을 사용한다. 일반화된 `where` 절은 연관 타입이 특정 프로토콜을 준수해야 하거나, 특정 타입 파라미터와 연관 타입이 동일해야 한다는 요구사항을 정의할 수 있다. 일반화된 `where` 절은 `where` 키워드로 시작하며, 연관 타입에 대한 제약 조건이나 타입과 연관 타입 간의 동등 관계를 정의한다. 일반화된 `where` 절은 타입 또는 함수의 본문을 여는 중괄호 바로 앞에 작성한다.

아래 예제는 `allItemsMatch`라는 제네릭 함수를 정의하며, 이 함수는 두 `Container` 인스턴스가 동일한 순서로 동일한 아이템을 포함하는지 확인한다. 모든 아이템이 일치하면 `true`를 반환하고, 그렇지 않으면 `false`를 반환한다.

검사할 두 컨테이너는 반드시 동일한 타입일 필요는 없지만(그럴 수도 있음), 동일한 타입의 아이템을 포함해야 한다. 이 요구사항은 타입 제약과 일반화된 `where` 절을 조합하여 표현된다:

```swift
func allItemsMatch<C1: Container, C2: Container>
        (_ someContainer: C1, _ anotherContainer: C2) -> Bool
        where C1.Item == C2.Item, C1.Item: Equatable {

    // 두 컨테이너가 동일한 수의 아이템을 포함하는지 확인한다.
    if someContainer.count != anotherContainer.count {
        return false
    }

    // 각 아이템 쌍이 동일한지 확인한다.
    for i in 0..<someContainer.count {
        if someContainer[i] != anotherContainer[i] {
            return false
        }
    }

    // 모든 아이템이 일치하므로 true를 반환한다.
    return true
}
```

이 함수는 `someContainer`와 `anotherContainer`라는 두 인수를 받는다. `someContainer` 인수는 `C1` 타입이고, `anotherContainer` 인수는 `C2` 타입이다. `C1`과 `C2`는 함수가 호출될 때 결정될 두 컨테이너 타입에 대한 타입 파라미터다.

이 함수의 두 타입 파라미터에 대해 다음과 같은 요구사항이 적용된다:

- `C1`은 `Container` 프로토콜을 준수해야 한다(`C1: Container`로 표기).
- `C2`도 `Container` 프로토콜을 준수해야 한다(`C2: Container`로 표기).
- `C1`의 `Item`은 `C2`의 `Item`과 동일해야 한다(`C1.Item == C2.Item`로 표기).
- `C1`의 `Item`은 `Equatable` 프로토콜을 준수해야 한다(`C1.Item: Equatable`로 표기).

첫 번째와 두 번째 요구사항은 함수의 타입 파라미터 목록에 정의되고, 세 번째와 네 번째 요구사항은 함수의 일반화된 `where` 절에 정의된다.

이러한 요구사항은 다음을 의미한다:

- `someContainer`는 `C1` 타입의 컨테이너다.
- `anotherContainer`는 `C2` 타입의 컨테이너다.
- `someContainer`와 `anotherContainer`는 동일한 타입의 아이템을 포함한다.
- `someContainer`의 아이템은 `!=` 연산자를 사용해 서로 다른지 확인할 수 있다.

세 번째와 네 번째 요구사항은 `anotherContainer`의 아이템도 `!=` 연산자로 확인할 수 있음을 의미한다. 이는 `someContainer`의 아이템과 정확히 동일한 타입이기 때문이다.

이러한 요구사항 덕분에 `allItemsMatch(_:_:)` 함수는 두 컨테이너가 서로 다른 타입이더라도 비교할 수 있다.

`allItemsMatch(_:_:)` 함수는 먼저 두 컨테이너가 동일한 수의 아이템을 포함하는지 확인한다. 아이템 수가 다르면 일치할 수 없으므로 함수는 `false`를 반환한다.

이 확인이 끝나면 함수는 `for`-`in` 루프와 반열린 범위 연산자(`..<`)를 사용해 `someContainer`의 모든 아이템을 순회한다. 각 아이템에 대해 `someContainer`의 아이템이 `anotherContainer`의 해당 아이템과 다른지 확인한다. 두 아이템이 다르면 두 컨테이너는 일치하지 않으므로 함수는 `false`를 반환한다.

루프가 끝날 때까지 불일치가 발견되지 않으면 두 컨테이너는 일치하며, 함수는 `true`를 반환한다.

다음은 `allItemsMatch(_:_:)` 함수가 동작하는 모습이다:

```swift
var stackOfStrings = Stack<String>()
stackOfStrings.push("uno")
stackOfStrings.push("dos")
stackOfStrings.push("tres")

var arrayOfStrings = ["uno", "dos", "tres"]

if allItemsMatch(stackOfStrings, arrayOfStrings) {
    print("All items match.")
} else {
    print("Not all items match.")
}
// "All items match."를 출력한다.
```

위 예제는 `String` 값을 저장하는 `Stack` 인스턴스를 생성하고, 세 개의 문자열을 스택에 푸시한다. 또한, 스택과 동일한 세 개의 문자열을 포함하는 배열 리터럴로 초기화된 `Array` 인스턴스를 생성한다. 스택과 배열은 서로 다른 타입이지만, 둘 다 `Container` 프로토콜을 준수하며 동일한 타입의 값을 포함한다. 따라서 이 두 컨테이너를 인수로 `allItemsMatch(_:_:)` 함수를 호출할 수 있다. 위 예제에서 `allItemsMatch(_:_:)` 함수는 두 컨테이너의 모든 아이템이 일치한다고 올바르게 보고한다.


## 제네릭 Where 절을 사용한 확장

확장에 제네릭 `where` 절을 사용할 수도 있다. 아래 예제는 이전 예제에서 사용한 제네릭 `Stack` 구조체를 확장하여 `isTop(_:)` 메서드를 추가한다.

```swift
extension Stack where Element: Equatable {
    func isTop(_ item: Element) -> Bool {
        guard let topItem = items.last else {
            return false
        }
        return topItem == item
    }
}
```

<!--
  - test: `associatedTypes`

  ```swifttest
  -> extension Stack where Element: Equatable {
         func isTop(_ item: Element) -> Bool {
             guard let topItem = items.last else {
                 return false
             }
             return topItem == item
         }
     }
  ```
-->

이 새로운 `isTop(_:)` 메서드는 스택이 비어 있는지 먼저 확인한 후, 주어진 아이템과 스택의 가장 위에 있는 아이템을 비교한다. 만약 제네릭 `where` 절 없이 이 작업을 시도한다면 문제가 발생한다. `isTop(_:)`의 구현은 `==` 연산자를 사용하지만, `Stack`의 정의는 아이템이 `Equatable`을 준수하도록 요구하지 않기 때문에 `==` 연산자를 사용하면 컴파일 타임 오류가 발생한다. 제네릭 `where` 절을 사용하면 확장에 새로운 요구 사항을 추가할 수 있어, 스택의 아이템이 `Equatable`을 준수할 때만 `isTop(_:)` 메서드를 추가할 수 있다.

`isTop(_:)` 메서드를 실제로 사용하는 모습은 다음과 같다:

```swift
if stackOfStrings.isTop("tres") {
    print("Top element is tres.")
} else {
    print("Top element is something else.")
}
// Prints "Top element is tres."
```

<!--
  - test: `associatedTypes`

  ```swifttest
  -> if stackOfStrings.isTop("tres") {
        print("Top element is tres.")
     } else {
        print("Top element is something else.")
     }
  <- Top element is tres.
  ```
-->

만약 `Equatable`을 준수하지 않는 아이템을 가진 스택에서 `isTop(_:)` 메서드를 호출하려고 하면 컴파일 타임 오류가 발생한다.

```swift
struct NotEquatable { }
var notEquatableStack = Stack<NotEquatable>()
let notEquatableValue = NotEquatable()
notEquatableStack.push(notEquatableValue)
notEquatableStack.isTop(notEquatableValue)  // Error
```

<!--
  - test: `associatedTypes-err`

  ```swifttest
  -> struct NotEquatable { }
  -> var notEquatableStack = Stack<NotEquatable>()
  -> let notEquatableValue = NotEquatable()
  -> notEquatableStack.push(notEquatableValue)
  -> notEquatableStack.isTop(notEquatableValue)  // Error
  !$ error: value of type 'Stack<NotEquatable>' has no member 'isTop'
  !! notEquatableStack.isTop(notEquatableValue)  // Error
  !! ~~~~~~~~~~~~~~~~~ ^~~~~
  ```
-->

프로토콜에 대한 확장에도 제네릭 `where` 절을 사용할 수 있다. 아래 예제는 이전 예제에서 사용한 `Container` 프로토콜을 확장하여 `startsWith(_:)` 메서드를 추가한다.

```swift
extension Container where Item: Equatable {
    func startsWith(_ item: Item) -> Bool {
        return count >= 1 && self[0] == item
    }
}
```

<!--
  - test: `associatedTypes`

  ```swifttest
  -> extension Container where Item: Equatable {
        func startsWith(_ item: Item) -> Bool {
           return count >= 1 && self[0] == item
        }
     }
  ```
-->

`startsWith(_:)` 메서드는 컨테이너에 적어도 하나의 아이템이 있는지 먼저 확인한 후, 컨테이너의 첫 번째 아이템이 주어진 아이템과 일치하는지 확인한다. 이 새로운 `startsWith(_:)` 메서드는 `Container` 프로토콜을 준수하는 모든 타입에 사용할 수 있으며, 위에서 사용한 스택과 배열도 포함된다. 단, 컨테이너의 아이템이 `Equatable`을 준수해야 한다.

```swift
if [9, 9, 9].startsWith(42) {
    print("Starts with 42.")
} else {
    print("Starts with something else.")
}
// Prints "Starts with something else."
```

<!--
  - test: `associatedTypes`

  ```swifttest
  -> if [9, 9, 9].startsWith(42) {
        print("Starts with 42.")
     } else {
        print("Starts with something else.")
     }
  <- Starts with something else.
  ```
-->

위 예제의 제네릭 `where` 절은 `Item`이 프로토콜을 준수하도록 요구하지만, `Item`이 특정 타입이어야 한다는 제네릭 `where` 절을 작성할 수도 있다. 예를 들어:

```swift
extension Container where Item == Double {
    func average() -> Double {
        var sum = 0.0
        for index in 0..<count {
            sum += self[index]
        }
        return sum / Double(count)
    }
}
print([1260.0, 1200.0, 98.6, 37.0].average())
// Prints "648.9"
```

<!--
  - test: `associatedTypes`

  ```swifttest
  -> extension Container where Item == Double {
         func average() -> Double {
             var sum = 0.0
             for index in 0..<count {
                 sum += self[index]
             }
             return sum / Double(count)
         }
     }
  -> print([1260.0, 1200.0, 98.6, 37.0].average())
  <- 648.9
  ```
-->

이 예제는 `Item` 타입이 `Double`인 컨테이너에 `average()` 메서드를 추가한다. 컨테이너의 아이템을 순회하며 합을 구하고, 컨테이너의 아이템 수로 나누어 평균을 계산한다. 부동소수점 나눗셈을 수행하기 위해 `count`를 `Int`에서 `Double`로 명시적으로 변환한다.

확장의 일부로 사용하는 제네릭 `where` 절에 여러 요구 사항을 포함할 수 있다. 각 요구 사항은 쉼표로 구분한다.

<!--
  No example of a compound where clause
  because Container only has one generic part ---
  there isn't anything to write a second constraint for.
-->


## 컨텍스트 기반 Where 절

제네릭 타입이 이미 정의된 컨텍스트에서, 별도의 제네릭 타입 제약이 없는 선언에 제네릭 `where` 절을 작성할 수 있다. 예를 들어, 제네릭 타입의 서브스크립트나 제네릭 타입의 익스텐션에 있는 메서드에 제네릭 `where` 절을 추가할 수 있다. `Container` 구조체는 제네릭 타입이며, 아래 예제의 `where` 절은 이러한 새로운 메서드가 컨테이너에서 사용 가능하도록 하기 위해 충족해야 하는 타입 제약을 명시한다.

```swift
extension Container {
    func average() -> Double where Item == Int {
        var sum = 0.0
        for index in 0..<count {
            sum += Double(self[index])
        }
        return sum / Double(count)
    }
    func endsWith(_ item: Item) -> Bool where Item: Equatable {
        return count >= 1 && self[count-1] == item
    }
}
let numbers = [1260, 1200, 98, 37]
print(numbers.average())
// Prints "648.75"
print(numbers.endsWith(37))
// Prints "true"
```

<!--
  - test: `associatedTypes`

  ```swifttest
  -> extension Container {
         func average() -> Double where Item == Int {
             var sum = 0.0
             for index in 0..<count {
                 sum += Double(self[index])
             }
             return sum / Double(count)
         }
         func endsWith(_ item: Item) -> Bool where Item: Equatable {
             return count >= 1 && self[count-1] == item
         }
     }
  -> let numbers = [1260, 1200, 98, 37]
  -> print(numbers.average())
  <- 648.75
  -> print(numbers.endsWith(37))
  <- true
  ```
-->

이 예제는 `Container`에 `Item`이 정수 타입일 때 사용할 수 있는 `average()` 메서드를 추가하고, `Item`이 동등 비교 가능한 타입일 때 사용할 수 있는 `endsWith(_:)` 메서드를 추가한다. 두 함수 모두 `Container`의 원래 선언에서 가져온 제네릭 `Item` 타입 파라미터에 타입 제약을 추가하는 제네릭 `where` 절을 포함한다.

컨텍스트 기반 `where` 절을 사용하지 않고 이 코드를 작성하려면, 각각의 제네릭 `where` 절에 대해 두 개의 익스텐션을 작성해야 한다. 위의 예제와 아래 예제는 동일한 동작을 한다.

```swift
extension Container where Item == Int {
    func average() -> Double {
        var sum = 0.0
        for index in 0..<count {
            sum += Double(self[index])
        }
        return sum / Double(count)
    }
}
extension Container where Item: Equatable {
    func endsWith(_ item: Item) -> Bool {
        return count >= 1 && self[count-1] == item
    }
}
```

<!--
  - test: `associatedTypes-err`

  ```swifttest
  -> extension Container where Item == Int {
         func average() -> Double {
             var sum = 0.0
             for index in 0..<count {
                 sum += Double(self[index])
             }
             return sum / Double(count)
         }
     }
     extension Container where Item: Equatable {
         func endsWith(_ item: Item) -> Bool {
             return count >= 1 && self[count-1] == item
         }
     }
  ```
-->

컨텍스트 기반 `where` 절을 사용한 이 예제의 버전에서, `average()`와 `endsWith(_:)`의 구현은 모두 동일한 익스텐션 안에 있다. 각 메서드의 제네릭 `where` 절은 해당 메서드를 사용 가능하게 하기 위해 충족해야 하는 요구사항을 명시하기 때문이다. 이러한 요구사항을 익스텐션의 제네릭 `where` 절로 옮기면 메서드가 동일한 상황에서 사용 가능하지만, 각 요구사항마다 하나의 익스텐션이 필요하다.


## 제네릭 `where` 절을 사용한 연관 타입

연관 타입에 제네릭 `where` 절을 추가할 수 있다. 예를 들어, Swift 표준 라이브러리의 `Sequence` 프로토콜에서 사용하는 것과 같은 이터레이터를 포함한 `Container` 버전을 만들고 싶다고 가정해 보자. 이를 구현하는 방법은 다음과 같다:

```swift
protocol Container {
    associatedtype Item
    mutating func append(_ item: Item)
    var count: Int { get }
    subscript(i: Int) -> Item { get }

    associatedtype Iterator: IteratorProtocol where Iterator.Element == Item
    func makeIterator() -> Iterator
}
```

<!--
  - test: `associatedTypes-iterator`

  ```swifttest
  -> protocol Container {
        associatedtype Item
        mutating func append(_ item: Item)
        var count: Int { get }
        subscript(i: Int) -> Item { get }

        associatedtype Iterator: IteratorProtocol where Iterator.Element == Item
        func makeIterator() -> Iterator
     }
  ```
-->

<!--
  makeIterator()를 Container에 추가하면 Sequence 프로토콜을 준수할 수 있지만,
  여기서는 그 부분을 명시적으로 언급하지 않는다.
-->

`Iterator`에 대한 제네릭 `where` 절은 이터레이터가 컨테이너의 아이템과 동일한 타입의 요소를 순회해야 한다는 것을 보장한다. 이터레이터의 타입과 상관없이 이 조건이 적용된다. `makeIterator()` 함수는 컨테이너의 이터레이터에 접근할 수 있는 방법을 제공한다.

<!--
  이 예제는 SE-0157 Recursive protocol constraints를 필요로 한다.
  이는 rdar://20531108에서 추적 중이다.

   서브스크립트에서 인덱스 범위를 받아
   서브 컨테이너를 반환하는 기능을 추가할 수도 있다.
   이는 Swift 표준 라이브러리의 ``Collection``과 유사하게 동작한다.

   .. testcode:: associatedTypes-subcontainer

      -> protocol Container {
            associatedtype Item
            associatedtype SubContainer: Container where SubContainer.Item == Item

            mutating func append(_ item: Item)
            var count: Int { get }
            subscript(i: Int) -> Item { get }
            subscript(range: Range<Int>) -> SubContainer { get }
         }

   ``SubContainer``에 대한 제네릭 ``where`` 절은
   서브 컨테이너가 컨테이너와 동일한 아이템 타입을 가져야 한다는 것을 보장한다.
   서브 컨테이너의 타입과는 무관하다.
   원본 컨테이너와 서브 컨테이너는
   동일한 타입으로 표현될 수도 있고,
   다른 타입으로 표현될 수도 있다.
   범위를 받는 새로운 서브스크립트는
   이 새로운 연관 타입을 반환 값으로 사용한다.
-->

다른 프로토콜을 상속하는 프로토콜의 경우, 프로토콜 선언에 제네릭 `where` 절을 포함해 상속된 연관 타입에 제약을 추가할 수 있다. 예를 들어, 다음 코드는 `Item`이 `Comparable`을 준수하도록 요구하는 `ComparableContainer` 프로토콜을 선언한다:

```swift
protocol ComparableContainer: Container where Item: Comparable { }
```

<!--
  - test: `associatedTypes`

  ```swifttest
  -> protocol ComparableContainer: Container where Item: Comparable { }
  ```
-->

<!--
  Swift commit de66b0c25c70 이후로 이 버전은 경고를 발생시킨다:
  "프로토콜 %1의 연관 타입 %0의 재선언은
  프로토콜에 'where' 절을 추가하는 것이 더 나은 표현이다."

   -> protocol ComparableContainer: Container {
          associatedtype Item: Comparable
      }
-->

<!--
  새로운 컨테이너를 테스트하는 코드를 추가할 수도 있지만,
  이는 실제로 필요하지 않을 수 있으며 복잡성을 증가시킬 수 있다.

  function < (lhs: ComparableContainer, rhs: ComparableContainer) -> Bool {
      // 빈 컨테이너를 비어있지 않은 컨테이너보다 앞에 정렬한다.
      if lhs.count == 0 {
          return true
      } else if rhs.count  == 0 {
          return false
      }

      // 비어있지 않은 컨테이너는 첫 번째 요소로 정렬한다.
      // (실제 코드에서는 첫 번째 요소가 같을 경우
      // 두 번째 요소를 비교하는 식으로 진행해야 할 것이다.)
      return lhs[0] < rhs[0]
  }
-->


## 제네릭 서브스크립트

서브스크립트는 제네릭으로 정의할 수 있으며, 제네릭 `where` 절을 포함할 수도 있다. `subscript` 키워드 뒤에 꺾쇠 괄호 안에 플레이스홀더 타입 이름을 작성하고, 서브스크립트 본문의 여는 중괄호 바로 앞에 제네릭 `where` 절을 추가한다. 예를 들어:

<!--
  위 단락은 이 장 앞부분에서 제네릭과 'where' 절을 소개할 때 사용한 표현을 차용했다.
-->

```swift
extension Container {
    subscript<Indices: Sequence>(indices: Indices) -> [Item]
            where Indices.Iterator.Element == Int {
        var result: [Item] = []
        for index in indices {
            result.append(self[index])
        }
        return result
    }
}
```

<!--
  - test: `genericSubscript`

  ```swifttest
  >> protocol Container {
  >>    associatedtype Item
  >>    mutating func append(_ item: Item)
  >>    var count: Int { get }
  >>    subscript(i: Int) -> Item { get }
  >> }
  -> extension Container {
         subscript<Indices: Sequence>(indices: Indices) -> [Item]
                 where Indices.Iterator.Element == Int {
             var result: [Item] = []
             for index in indices {
                 result.append(self[index])
             }
             return result
         }
     }
  ```
-->

<!--
  - test: `genericSubscript`

  ```swifttest
  >> struct IntStack: Container {
        // original IntStack implementation
        var items: [Int] = []
        mutating func push(_ item: Int) {
           items.append(item)
        }
        mutating func pop() -> Int {
           return items.removeLast()
        }
        // conformance to the Container protocol
        typealias Item = Int
        mutating func append(_ item: Int) {
           self.push(item)
        }
        var count: Int {
           return items.count
        }
        subscript(i: Int) -> Int {
           return items[i]
        }
     }
  >> var s = IntStack()
  >> s.push(10); s.push(20); s.push(30)
  >> let items = s[ [0, 2] ]
  >> assert(items == [10, 30])
  ```
-->

이 `Container` 프로토콜 확장은 인덱스 시퀀스를 받아 각 인덱스에 해당하는 아이템을 배열로 반환하는 서브스크립트를 추가한다. 이 제네릭 서브스크립트는 다음과 같은 제약을 가진다:

- 꺾쇠 괄호 안의 제네릭 파라미터 `Indices`는 Swift 표준 라이브러리의 `Sequence` 프로토콜을 준수하는 타입이어야 한다.
- 서브스크립트는 `Indices` 타입의 인스턴스인 `indices`라는 단일 파라미터를 받는다.
- 제네릭 `where` 절은 시퀀스의 이터레이터가 `Int` 타입의 요소를 순회해야 한다는 조건을 명시한다. 이를 통해 시퀀스의 인덱스가 컨테이너에 사용되는 인덱스와 동일한 타입임을 보장한다.

이러한 제약 조건을 종합해보면, `indices` 파라미터로 전달되는 값은 정수 시퀀스여야 함을 의미한다.

<!--
  TODO: 제네릭 열거형
  --------------------------
-->

<!--
  TODO: Optional<Wrapped>의 동작 방식 설명
-->

<!--
이 소스 파일은 Swift.org 오픈 소스 프로젝트의 일부입니다.

Copyright (c) 2014 - 2022 Apple Inc. 및 Swift 프로젝트 저자들
Apache License v2.0 및 Runtime Library Exception에 따라 라이선스가 부여됩니다.

라이선스 정보는 https://swift.org/LICENSE.txt에서 확인할 수 있습니다.
Swift 프로젝트 저자 목록은 https://swift.org/CONTRIBUTORS.txt에서 확인할 수 있습니다.
-->


