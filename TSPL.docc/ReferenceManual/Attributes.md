# 속성

선언과 타입에 추가 정보를 제공한다.

Swift에는 두 가지 종류의 속성이 있다.  
하나는 선언에 적용되는 속성이고, 다른 하나는 타입에 적용되는 속성이다.  
속성은 선언이나 타입에 대한 추가 정보를 제공한다.  
예를 들어, 함수 선언에 사용하는 `discardableResult` 속성은 함수가 값을 반환하더라도, 반환값이 사용되지 않을 때 컴파일러가 경고를 생성하지 않도록 한다.

속성을 지정할 때는 `@` 기호 뒤에 속성 이름과 해당 속성이 허용하는 인자를 작성한다:

```swift
@<#속성 이름#>
@<#속성 이름#>(<#속성 인자#>)
```

일부 선언 속성은 속성에 대한 추가 정보와 특정 선언에 어떻게 적용되는지 지정하는 인자를 허용한다.  
이러한 *속성 인자*는 괄호로 묶이며, 그 형식은 속성에 따라 정의된다.

부착형 매크로와 프로퍼티 래퍼도 속성 구문을 사용한다.  
매크로가 어떻게 확장되는지에 대한 자세한 내용은 <doc:Expressions#Macro-Expansion-Expression>을 참고한다.  
프로퍼티 래퍼에 대한 자세한 내용은 <doc:Attributes#propertyWrapper>를 확인한다.


## 선언 속성

선언 속성은 오직 선언에만 적용할 수 있다.


### 부착형 매크로

매크로 선언에 `attached` 속성을 적용한다. 이 속성의 인자는 매크로의 역할을 나타낸다. 매크로가 여러 역할을 수행하는 경우, 각 역할에 대해 `attached` 매크로를 한 번씩 적용한다.

<!-- TODO:
안정적인 URL이 있다면, 아래 매크로 프로토콜에 링크를 추가한다.
-->

이 속성의 첫 번째 인자는 매크로의 역할을 나타낸다:

- **Peer 매크로**:  
  이 속성의 첫 번째 인자로 `peer`를 작성한다. 매크로를 구현하는 타입은 `PeerMacro` 프로토콜을 준수한다. 이러한 매크로는 매크로가 부착된 선언과 동일한 스코프에서 새로운 선언을 생성한다. 예를 들어, 구조체의 메서드에 Peer 매크로를 적용하면 해당 구조체에 추가적인 메서드와 프로퍼티를 정의할 수 있다.

- **Member 매크로**:  
  이 속성의 첫 번째 인자로 `member`를 작성한다. 매크로를 구현하는 타입은 `MemberMacro` 프로토콜을 준수한다. 이러한 매크로는 매크로가 부착된 타입 또는 익스텐션의 멤버로 새로운 선언을 생성한다. 예를 들어, 구조체 선언에 Member 매크로를 적용하면 해당 구조체에 추가적인 메서드와 프로퍼티를 정의할 수 있다.

- **Member 속성**:  
  이 속성의 첫 번째 인자로 `memberAttribute`를 작성한다. 매크로를 구현하는 타입은 `MemberAttributeMacro` 프로토콜을 준수한다. 이러한 매크로는 매크로가 부착된 타입 또는 익스텐션의 멤버에 속성을 추가한다.

- **Accessor 매크로**:  
  이 속성의 첫 번째 인자로 `accessor`를 작성한다. 매크로를 구현하는 타입은 `AccessorMacro` 프로토콜을 준수한다. 이러한 매크로는 저장 프로퍼티에 접근자를 추가하여 계산 프로퍼티로 변환한다.

- **Extension 매크로**:  
  이 속성의 첫 번째 인자로 `extension`를 작성한다. 매크로를 구현하는 타입은 `ExtensionMacro` 프로토콜을 준수한다. 이러한 매크로는 프로토콜 준수, `where` 절, 그리고 매크로가 부착된 타입의 멤버로 새로운 선언을 추가할 수 있다. 매크로가 프로토콜 준수를 추가하는 경우, `conformances:` 인자를 포함하고 해당 프로토콜을 지정한다. 준수 목록에는 프로토콜 이름, 준수 목록 항목을 참조하는 타입 별칭, 또는 준수 목록 항목의 프로토콜 합성이 포함된다. 중첩 타입에 대한 Extension 매크로는 해당 파일의 최상위 레벨로 익스텐션을 확장한다. 익스텐션, 타입 별칭, 또는 함수 내부에 중첩된 타입에 Extension 매크로를 작성할 수 없다. 또한 Extension 매크로를 사용해 Peer 매크로가 있는 익스텐션을 추가할 수 없다.

Peer, Member, Accessor 매크로 역할은 `names:` 인자를 필요로 하며, 매크로가 생성하는 심볼의 이름을 나열한다. Extension 매크로 역할도 매크로가 익스텐션 내부에 선언을 추가하는 경우 `names:` 인자를 필요로 한다. 매크로 선언에 `names:` 인자가 포함된 경우, 매크로 구현은 해당 목록과 일치하는 이름의 심볼만 생성해야 한다. 단, 매크로가 나열된 모든 이름에 대해 심볼을 생성할 필요는 없다. 이 인자의 값은 다음 중 하나 이상의 목록이다:

- `named(<#name#>)`  
  여기서 *name*은 미리 알려진 고정된 심볼 이름이다.

- `overloaded`  
  기존 심볼과 동일한 이름이다.

- `prefixed(<#prefix#>)`  
  여기서 *prefix*는 심볼 이름 앞에 추가되며, 고정된 문자열로 시작하는 이름이다.

- `suffixed(<#suffix#>)`  
  여기서 *suffix*는 심볼 이름 뒤에 추가되며, 고정된 문자열로 끝나는 이름이다.

- `arbitrary`  
  매크로 확장이 될 때까지 결정할 수 없는 이름이다.

특별한 경우로, 프로퍼티 래퍼와 유사하게 동작하는 매크로에 대해 `prefixed($)`를 작성할 수 있다.
<!--
TODO TR: 이 경우에 대한 더 자세한 내용이 있는가?
-->


### available

이 속성은 특정 Swift 언어 버전이나 플랫폼 및 운영체제 버전과 관련하여 선언의 생명주기를 나타내기 위해 사용한다.

`available` 속성은 항상 두 개 이상의 쉼표로 구분된 속성 인자와 함께 나타난다. 이 인자들은 다음 플랫폼 또는 언어 이름 중 하나로 시작한다:

- `iOS`
- `iOSApplicationExtension`
- `macOS`
- `macOSApplicationExtension`
- `macCatalyst`
- `macCatalystApplicationExtension`
- `watchOS`
- `watchOSApplicationExtension`
- `tvOS`
- `tvOSApplicationExtension`
- `visionOS`
- `visionOSApplicationExtension`
- `swift`

<!--
  이 목록에 새로운 플랫폼을 추가해야 한다면,
  문법에서도 platform-name을 업데이트해야 할 가능성이 높다.
-->

<!--
  소스 코드의 목록은 include/swift/AST/PlatformKinds.def를 참조하라.
-->

또한 별표(`*`)를 사용하여 위에 나열된 모든 플랫폼에서 선언의 사용 가능성을 나타낼 수 있다. Swift 버전 번호를 사용하여 사용 가능성을 지정하는 `available` 속성은 별표를 사용할 수 없다.

나머지 인자들은 어떤 순서로든 나타날 수 있으며, 선언의 생명주기에 대한 추가 정보를 지정한다. 이는 중요한 마일스톤을 포함한다.

- `unavailable` 인자는 지정된 플랫폼에서 선언이 사용 불가능함을 나타낸다. 이 인자는 Swift 버전 사용 가능성을 지정할 때 사용할 수 없다.
- `introduced` 인자는 지정된 플랫폼이나 언어에서 선언이 처음 도입된 버전을 나타낸다. 형식은 다음과 같다:

  ```swift
  introduced: <#version number#>
  ```
  *버전 번호*는 마침표로 구분된 하나에서 세 개의 양의 정수로 구성된다.
- `deprecated` 인자는 지정된 플랫폼이나 언어에서 선언이 처음으로 사용되지 않게 된 버전을 나타낸다. 형식은 다음과 같다:

  ```swift
  deprecated: <#version number#>
  ```
  선택적 *버전 번호*는 마침표로 구분된 하나에서 세 개의 양의 정수로 구성된다. 버전 번호를 생략하면 선언이 현재 사용되지 않음을 나타내며, 언제 사용이 중단되었는지에 대한 정보는 제공하지 않는다. 버전 번호를 생략하면 콜론(`:`)도 생략해야 한다.
- `obsoleted` 인자는 지정된 플랫폼이나 언어에서 선언이 처음으로 제거된 버전을 나타낸다. 선언이 제거되면 지정된 플랫폼이나 언어에서 더 이상 사용할 수 없다. 형식은 다음과 같다:

  ```swift
  obsoleted: <#version number#>
  ```
  *버전 번호*는 마침표로 구분된 하나에서 세 개의 양의 정수로 구성된다.

- `noasync` 인자는 선언된 심볼이 비동기 컨텍스트에서 직접 사용될 수 없음을 나타낸다.

  Swift의 동시성은 잠재적인 중단 지점 이후에 다른 스레드에서 재개될 수 있기 때문에, 스레드 로컬 스토리지, 락, 뮤텍스, 세마포어와 같은 요소를 중단 지점을 넘어 사용하면 잘못된 결과를 초래할 수 있다.

  이 문제를 피하기 위해 심볼 선언에 `@available(*, noasync)` 속성을 추가한다:

  ```swift
  extension pthread_mutex_t {

    @available(*, noasync)
    mutating func lock() {
        pthread_mutex_lock(&self)
    }

    @available(*, noasync)
    mutating func unlock() {
        pthread_mutex_unlock(&self)
    }
  }
  ```

  이 속성은 비동기 컨텍스트에서 심볼을 사용할 때 컴파일 타임 오류를 발생시킨다. 또한 `message` 인자를 사용하여 심볼에 대한 추가 정보를 제공할 수 있다.

  ```swift
  @available(*, noasync, message: "Migrate locks to Swift concurrency.")
  mutating func lock() {
    pthread_mutex_lock(&self)
  }
  ```

  코드가 잠재적으로 안전하지 않은 심볼을 안전하게 사용한다는 것을 보장할 수 있다면, 동기 함수로 감싸고 비동기 컨텍스트에서 그 함수를 호출할 수 있다.

  ```swift

  // noasync 선언이 있는 메서드 주위에 동기 래퍼를 제공한다.
  extension pthread_mutex_t {
    mutating func withLock(_ operation: () -> ()) {
      self.lock()
      operation()
      self.unlock()
    }
  }

  func downloadAndStore(key: Int,
                      dataStore: MyKeyedStorage,
                      dataLock: inout pthread_mutex_t) async {
    // 비동기 컨텍스트에서 래퍼를 안전하게 호출한다.
    dataLock.withLock {
      dataStore[key] = downloadContent()
    }
  }
  ```

  `noasync` 인자는 대부분의 선언에 사용할 수 있지만, 소멸자를 선언할 때는 사용할 수 없다. Swift는 클래스의 소멸자를 동기 및 비동기 컨텍스트 모두에서 호출할 수 있어야 한다.

- `message` 인자는 `deprecated`, `obsoleted`, 또는 `noasync`로 표시된 선언의 사용에 대해 컴파일러가 경고나 오류를 발생시킬 때 표시할 텍스트 메시지를 제공한다. 형식은 다음과 같다:

  ```swift
  message: <#message#>
  ```
  *메시지*는 문자열 리터럴로 구성된다.
- `renamed` 인자는 이름이 변경된 선언의 새로운 이름을 나타내는 텍스트 메시지를 제공한다. 컴파일러는 이름이 변경된 선언의 사용에 대해 오류를 발생시킬 때 새로운 이름을 표시한다. 형식은 다음과 같다:

  ```swift
  renamed: <#new name#>
  ```
  *새로운 이름*은 문자열 리터럴로 구성된다.

  `available` 속성을 `renamed` 및 `unavailable` 인자와 함께 타입 별칭 선언에 적용하여, 프레임워크나 라이브러리의 릴리스 간에 선언의 이름이 변경되었음을 나타낼 수 있다. 이 조합은 선언의 이름이 변경되었음을 나타내는 컴파일 타임 오류를 발생시킨다.

  ```swift
  // 첫 번째 릴리스
  protocol MyProtocol {
      // 프로토콜 정의
  }
  ```

  ```swift
  // 이후 릴리스에서 MyProtocol의 이름을 변경
  protocol MyRenamedProtocol {
      // 프로토콜 정의
  }

  @available(*, unavailable, renamed: "MyRenamedProtocol")
  typealias MyProtocol = MyRenamedProtocol
  ```

단일 선언에 여러 `available` 속성을 적용하여 다른 플랫폼과 Swift 버전에서의 선언 사용 가능성을 지정할 수 있다. `available` 속성이 적용되는 선언은 현재 대상과 일치하지 않는 플랫폼이나 언어 버전을 지정하는 경우 무시된다. 여러 `available` 속성을 사용할 경우, 효과적인 사용 가능성은 플랫폼과 Swift 사용 가능성의 조합이다.

`available` 속성이 `introduced` 인자와 플랫폼 또는 언어 이름 인자만 지정하는 경우, 다음의 축약형 문법을 사용할 수 있다:

```swift
@available(<#platform name#> <#version number#>, *)
@available(swift <#version number#>)
```

`available` 속성의 축약형 문법은 여러 플랫폼에 대한 사용 가능성을 간결하게 표현한다. 두 형식은 기능적으로 동일하지만, 가능한 경우 축약형을 선호한다.

```swift
@available(iOS 10.0, macOS 10.12, *)
class MyClass {
    // 클래스 정의
}
```

Swift 버전 번호를 사용하여 사용 가능성을 지정하는 `available` 속성은 추가로 선언의 플랫폼 사용 가능성을 지정할 수 없다. 대신, 별도의 `available` 속성을 사용하여 Swift 버전 사용 가능성과 하나 이상의 플랫폼 사용 가능성을 지정한다.

```swift
@available(swift 3.0.2)
@available(macOS 10.12, *)
struct MyStruct {
    // 구조체 정의
}
```


### backDeployed

이 속성은 함수, 메서드, 서브스크립트, 계산된 프로퍼티에 적용한다. 이 속성을 사용하면 해당 심볼을 호출하거나 접근하는 프로그램에 심볼의 구현 복사본을 포함시킨다. 주로 운영체제와 함께 제공되는 API와 같은 플랫폼의 일부로 배포되는 심볼에 이 속성을 사용한다. 이 속성은 접근하는 프로그램에 구현 복사본을 포함함으로써 나중에 사용 가능하게 만들 수 있는 심볼을 표시한다. 구현 복사본을 포함하는 것을 *클라이언트로 내보내기*라고도 한다.

이 속성은 `before:` 인자를 받으며, 해당 심볼을 제공하는 플랫폼의 첫 번째 버전을 지정한다. 이 플랫폼 버전은 `available` 속성에 지정하는 플랫폼 버전과 동일한 의미를 가진다. 단, `available` 속성과 달리 모든 버전을 가리키는 별표(`*`)를 포함할 수 없다. 예를 들어, 다음 코드를 살펴보자:

```swift
@available(iOS 16, *)
@backDeployed(before: iOS 17)
func someFunction() { /* ... */ }
```

위 예제에서 iOS SDK는 `someFunction()`을 iOS 17부터 제공한다. 또한, SDK는 백 데플로이먼트를 통해 `someFunction()`을 iOS 16에서도 사용 가능하게 만든다.

이 함수를 호출하는 코드를 컴파일할 때, Swift는 함수의 구현을 찾는 간접적인 레이어를 삽입한다. 이 함수를 포함하는 SDK 버전에서 코드를 실행하면 SDK의 구현이 사용된다. 그렇지 않으면 호출자에 포함된 복사본이 사용된다. 위 예제에서 `someFunction()`을 호출하면 iOS 17 이상에서 실행할 때 SDK의 구현이 사용되고, iOS 16에서 실행할 때는 호출자에 포함된 `someFunction()`의 복사본이 사용된다.

> 참고:  
> 호출자의 최소 배포 대상이 해당 심볼을 포함하는 SDK의 첫 번째 버전과 같거나 더 높은 경우, 컴파일러는 런타임 검사를 최적화하여 SDK의 구현을 직접 호출할 수 있다. 이 경우, 백 데플로이먼트된 심볼에 직접 접근하면 컴파일러는 클라이언트에서 심볼의 구현 복사본을 생략할 수도 있다.

<!--
클라이언트로 내보낸 복사본을 제거하는 것은 일련의 최적화가 모두 이루어져야 가능하다. 
이 최적화에는 썽크 인라이닝, 가용성 검사의 상수 폴딩, 
사용되지 않는 코드로 간주된 내보낸 복사본 제거 등이 포함된다. 
이러한 세부 사항은 시간이 지남에 따라 변경될 수 있으므로, 
문서에서 항상 이렇게 동작한다고 보장하지는 않는다.
-->

다음 조건을 만족하는 함수, 메서드, 서브스크립트, 계산된 프로퍼티는 백 데플로이먼트될 수 있다:

- 선언이 `public` 또는 `@usableFromInline`이다.
- 클래스 인스턴스 메서드와 클래스 타입 메서드의 경우, 메서드가 `final`로 표시되고 `@objc`로 표시되지 않는다.
- 구현이 <doc:Attributes#inlinable>에 설명된 인라이너블 함수의 요구 사항을 충족한다.


### discardableResult

이 속성을 함수나 메서드 선언에 적용하면, 반환값이 있는 함수나 메서드를 호출할 때 그 결과를 사용하지 않아도 컴파일러 경고를 무시할 수 있다.


### dynamicCallable

이 속성을 클래스, 구조체, 열거형 또는 프로토콜에 적용하면 해당 타입의 인스턴스를 호출 가능한 함수처럼 사용할 수 있다. 타입은 `dynamicallyCall(withArguments:)` 메서드나 `dynamicallyCall(withKeywordArguments:)` 메서드 중 하나 또는 둘 다를 구현해야 한다.

동적으로 호출 가능한 타입의 인스턴스를 함수처럼 호출할 수 있으며, 이때 임의의 개수의 인자를 전달할 수 있다.

```swift
@dynamicCallable
struct TelephoneExchange {
    func dynamicallyCall(withArguments phoneNumber: [Int]) {
        if phoneNumber == [4, 1, 1] {
            print("Get Swift help on forums.swift.org")
        } else {
            print("Unrecognized number")
        }
    }
}

let dial = TelephoneExchange()

// 동적 메서드 호출 사용
dial(4, 1, 1)
// "Get Swift help on forums.swift.org" 출력

dial(8, 6, 7, 5, 3, 0, 9)
// "Unrecognized number" 출력

// 기본 메서드 직접 호출
dial.dynamicallyCall(withArguments: [4, 1, 1])
```

<!--
  - test: `dynamicCallable`

  ```swifttest
  -> @dynamicCallable
  -> struct TelephoneExchange {
         func dynamicallyCall(withArguments phoneNumber: [Int]) {
             if phoneNumber == [4, 1, 1] {
                 print("Get Swift help on forums.swift.org")
             } else {
                 print("Unrecognized number")
             }
         }
     }

  -> let dial = TelephoneExchange()

  -> // Use a dynamic method call.
  -> dial(4, 1, 1)
  <- Get Swift help on forums.swift.org

  -> dial(8, 6, 7, 5, 3, 0, 9)
  <- Unrecognized number

  -> // Call the underlying method directly.
  -> dial.dynamicallyCall(withArguments: [4, 1, 1])
  << Get Swift help on forums.swift.org
  ```
-->

`dynamicallyCall(withArguments:)` 메서드의 선언은 [`ExpressibleByArrayLiteral`](https://developer.apple.com/documentation/swift/expressiblebyarrayliteral) 프로토콜을 준수하는 단일 매개변수를 가져야 한다. 위 예제에서처럼 `[Int]` 타입을 사용할 수 있다. 반환 타입은 어떤 타입이든 가능하다.

동적 메서드 호출에 라벨을 포함하려면 `dynamicallyCall(withKeywordArguments:)` 메서드를 구현해야 한다.

```swift
@dynamicCallable
struct Repeater {
    func dynamicallyCall(withKeywordArguments pairs: KeyValuePairs<String, Int>) -> String {
        return pairs
            .map { label, count in
                repeatElement(label, count: count).joined(separator: " ")
            }
            .joined(separator: "\n")
    }
}

let repeatLabels = Repeater()
print(repeatLabels(a: 1, b: 2, c: 3, b: 2, a: 1))
// a
// b b
// c c c
// b b
// a
```

<!--
  - test: `dynamicCallable`

  ```swifttest
  -> @dynamicCallable
     struct Repeater {
         func dynamicallyCall(withKeywordArguments pairs: KeyValuePairs<String, Int>) -> String {
             return pairs
                 .map { label, count in
                     repeatElement(label, count: count).joined(separator: " ")
                 }
                 .joined(separator: "\n")
         }
     }

  -> let repeatLabels = Repeater()
  -> print(repeatLabels(a: 1, b: 2, c: 3, b: 2, a: 1))
  </ a
  </ b b
  </ c c c
  </ b b
  </ a
  ```
-->

`dynamicallyCall(withKeywordArguments:)` 메서드의 선언은 [`ExpressibleByDictionaryLiteral`](https://developer.apple.com/documentation/swift/expressiblebydictionaryliteral) 프로토콜을 준수하는 단일 매개변수를 가져야 하며, 반환 타입은 어떤 타입이든 가능하다. 매개변수의 [`Key`](https://developer.apple.com/documentation/swift/expressiblebydictionaryliteral/2294108-key)는 [`ExpressibleByStringLiteral`](https://developer.apple.com/documentation/swift/expressiblebystringliteral)을 준수해야 한다. 위 예제에서는 호출자가 중복된 라벨을 포함할 수 있도록 매개변수 타입으로 [`KeyValuePairs`](https://developer.apple.com/documentation/swift/keyvaluepairs)를 사용했다. `repeat` 호출에서 `a`와 `b`가 여러 번 나타난다.

두 `dynamicallyCall` 메서드를 모두 구현한 경우, 메서드 호출에 키워드 인자가 포함되면 `dynamicallyCall(withKeywordArguments:)`가 호출된다. 그 외의 경우에는 `dynamicallyCall(withArguments:)`가 호출된다.

동적으로 호출 가능한 인스턴스는 `dynamicallyCall` 메서드 구현에서 지정한 타입과 일치하는 인자와 반환 값으로만 호출할 수 있다. 다음 예제의 호출은 `KeyValuePairs<String, String>`을 받는 `dynamicallyCall(withArguments:)` 구현이 없기 때문에 컴파일되지 않는다.

```swift
repeatLabels(a: "four") // 오류
```

<!--
  - test: `dynamicCallable-err`

  ```swifttest
  >> @dynamicCallable
  >> struct Repeater {
  >>     func dynamicallyCall(withKeywordArguments pairs: KeyValuePairs<String, Int>) -> String {
  >>         return pairs
  >>             .map { label, count in
  >>                 repeatElement(label, count: count).joined(separator: " ")
  >>             }
  >>             .joined(separator: "\n")
  >>     }
  >> }
  >> let repeatLabels = Repeater()
  -> repeatLabels(a: "four") // 오류
  !$ error: cannot convert value of type 'String' to expected argument type 'Int'
  !! repeatLabels(a: "four") // 오류
  !! ^
  ```
-->


### dynamicMemberLookup

이 속성을 클래스, 구조체, 열거형 또는 프로토콜에 적용하면 런타임에 이름을 통해 멤버를 조회할 수 있다. 이 타입은 `subscript(dynamicMember:)` 서브스크립트를 구현해야 한다.

명시적 멤버 표현식에서 해당 이름의 멤버 선언이 없을 경우, 해당 표현식은 타입의 `subscript(dynamicMember:)` 서브스크립트를 호출하는 것으로 이해된다. 이때 멤버에 대한 정보가 인자로 전달된다. 서브스크립트는 키 경로(key path) 또는 멤버 이름을 파라미터로 받을 수 있다. 두 가지 서브스크립트를 모두 구현한 경우, 키 경로를 인자로 받는 서브스크립트가 사용된다.

`subscript(dynamicMember:)` 구현은 [`KeyPath`](https://developer.apple.com/documentation/swift/keypath), [`WritableKeyPath`](https://developer.apple.com/documentation/swift/writablekeypath), 또는 [`ReferenceWritableKeyPath`](https://developer.apple.com/documentation/swift/referencewritablekeypath) 타입의 인자를 통해 키 경로를 받을 수 있다. 또한 [`ExpressibleByStringLiteral`](https://developer.apple.com/documentation/swift/expressiblebystringliteral) 프로토콜을 준수하는 타입(대부분 `String`)의 인자를 통해 멤버 이름을 받을 수 있다. 서브스크립트의 반환 타입은 어떤 타입이든 가능하다.

멤버 이름을 통한 동적 멤버 조회는 컴파일 타임에 타입 검사를 할 수 없는 데이터를 감싸는 래퍼 타입을 생성할 때 사용할 수 있다. 예를 들어, 다른 언어에서 Swift로 데이터를 연결할 때 유용하다.

```swift
@dynamicMemberLookup
struct DynamicStruct {
    let dictionary = ["someDynamicMember": 325,
                      "someOtherMember": 787]
    subscript(dynamicMember member: String) -> Int {
        return dictionary[member] ?? 1054
    }
}
let s = DynamicStruct()

// 동적 멤버 조회 사용
let dynamic = s.someDynamicMember
print(dynamic)
// "325" 출력

// 직접 서브스크립트 호출
let equivalent = s[dynamicMember: "someDynamicMember"]
print(dynamic == equivalent)
// "true" 출력
```

<!--
  - test: `dynamicMemberLookup`

  ```swifttest
  -> @dynamicMemberLookup
  -> struct DynamicStruct {
         let dictionary = ["someDynamicMember": 325,
                           "someOtherMember": 787]
         subscript(dynamicMember member: String) -> Int {
             return dictionary[member] ?? 1054
         }
     }
  -> let s = DynamicStruct()

  // Use dynamic member lookup.
  -> let dynamic = s.someDynamicMember
  -> print(dynamic)
  <- 325

  // Call the underlying subscript directly.
  -> let equivalent = s[dynamicMember: "someDynamicMember"]
  -> print(dynamic == equivalent)
  <- true
  ```
-->

키 경로를 통한 동적 멤버 조회는 컴파일 타임 타입 검사를 지원하는 방식으로 래퍼 타입을 구현할 때 사용할 수 있다.

```swift
struct Point { var x, y: Int }

@dynamicMemberLookup
struct PassthroughWrapper<Value> {
    var value: Value
    subscript<T>(dynamicMember member: KeyPath<Value, T>) -> T {
        get { return value[keyPath: member] }
    }
}

let point = Point(x: 381, y: 431)
let wrapper = PassthroughWrapper(value: point)
print(wrapper.x)
```

<!--
  - test: `dynamicMemberLookup`

  ```swifttest
  -> struct Point { var x, y: Int }

  -> @dynamicMemberLookup
     struct PassthroughWrapper<Value> {
         var value: Value
         subscript<T>(dynamicMember member: KeyPath<Value, T>) -> T {
             get { return value[keyPath: member] }
         }
     }

  -> let point = Point(x: 381, y: 431)
  -> let wrapper = PassthroughWrapper(value: point)
  -> print(wrapper.x)
  << 381
  ```
-->


### 독립형 매크로

독립형 매크로를 선언할 때 `freestanding` 속성을 적용한다.

<!--

추후 다른 역할이 지원될 때를 위해:

이 속성의 인자는 매크로의 역할을 나타낸다:

- `expression`
  표현식을 생성하는 매크로

- `declaration`
  선언을 생성하는 매크로

혹시 이 기능들이 현재 지원되고 있는가?
stdlib에서 #error와 #warning이 @freestanding(declaration)으로
이미 사용되고 있는 것을 확인할 수 있다:

https://github.com/swiftlang/swift/blob/main/stdlib/public/core/Macros.swift#L102
-->


### frozen

이 속성을 구조체나 열거형 선언에 적용하면 타입을 변경할 수 있는 범위를 제한한다. 이 속성은 라이브러리 진화 모드에서만 사용할 수 있다. 라이브러리의 향후 버전에서 열거형의 케이스를 추가, 삭제, 재정렬하거나 구조체의 저장된 인스턴스 프로퍼티를 변경할 수 없다. 이러한 변경은 nonfrozen 타입에서는 허용되지만, frozen 타입에서는 ABI 호환성을 깨뜨린다.

> 참고: 컴파일러가 라이브러리 진화 모드가 아닐 때는 모든 구조체와 열거형이 암묵적으로 frozen 상태가 되며, 이 속성은 무시된다.

라이브러리 진화 모드에서 nonfrozen 구조체와 열거형의 멤버와 상호작용하는 코드는 재컴파일 없이도 계속 동작하도록 컴파일된다. 라이브러리의 향후 버전에서 해당 타입의 멤버를 추가, 삭제, 재정렬하더라도 말이다. 컴파일러는 런타임에 정보를 조회하거나 간접적인 레이어를 추가하는 등의 기법을 사용해 이를 가능하게 한다. 구조체나 열거형을 frozen으로 표시하면 이 유연성을 포기하는 대신 성능을 얻을 수 있다. 라이브러리의 향후 버전에서는 타입에 제한된 변경만 가능하지만, 컴파일러는 해당 타입의 멤버와 상호작용하는 코드에서 추가적인 최적화를 수행할 수 있다.

frozen 타입, frozen 구조체의 저장된 프로퍼티 타입, 그리고 frozen 열거형 케이스의 연관 값은 반드시 public이거나 `usableFromInline` 속성으로 표시되어야 한다. frozen 구조체의 프로퍼티는 프로퍼티 관찰자를 가질 수 없으며, 저장된 인스턴스 프로퍼티의 초기값을 제공하는 표현식은 <doc:Attributes#inlinable>에서 설명한 것처럼 인라인 가능한 함수와 동일한 제한을 따라야 한다.

라이브러리 진화 모드를 커맨드라인에서 활성화하려면 Swift 컴파일러에 `-enable-library-evolution` 옵션을 전달한다. Xcode에서 활성화하려면 "Build Libraries for Distribution" 빌드 설정(`BUILD_LIBRARY_FOR_DISTRIBUTION`)을 Yes로 설정한다. 자세한 내용은 [Xcode Help](https://help.apple.com/xcode/mac/current/#/dev04b3a04ba)를 참고한다.

frozen 열거형에 대한 switch 문은 `default` 케이스를 요구하지 않는다. <doc:Statements#Switching-Over-Future-Enumeration-Cases>에서 설명한 것처럼, frozen 열거형에 대해 `default`나 `@unknown default` 케이스를 포함하면 해당 코드가 실행되지 않기 때문에 경고가 발생한다.


### GKInspectable

이 속성은 커스텀 GameplayKit 컴포넌트 프로퍼티를 SpriteKit 에디터 UI에 노출시키기 위해 사용한다. 이 속성을 적용하면 `objc` 속성도 함께 적용된다.

<!--
  <rdar://problem/27287369> @GKInspectable 속성 문서화 관련 링크 추가 예정
-->


### 인라인 가능(inlinable)

이 속성을 함수, 메서드, 계산된 프로퍼티, 서브스크립트, 편의 이니셜라이저, 디이니셜라이저 선언에 적용하면 해당 선언의 구현을 모듈의 공개 인터페이스의 일부로 노출할 수 있다. 컴파일러는 인라인 가능한 심볼에 대한 호출을 호출 위치에서 심볼의 구현 복사본으로 대체할 수 있다.

인라인 가능한 코드는 모든 모듈에서 선언된 `open` 및 `public` 심볼과 상호작용할 수 있으며, 동일한 모듈에서 선언되고 `usableFromInline` 속성이 표시된 `internal` 심볼과도 상호작용할 수 있다. 인라인 가능한 코드는 `private` 또는 `fileprivate` 심볼과 상호작용할 수 없다.

이 속성은 함수 내부에 중첩된 선언이나 `fileprivate` 또는 `private` 선언에는 적용할 수 없다. 인라인 가능한 함수 내부에 정의된 함수와 클로저는 이 속성으로 표시할 수 없더라도 암묵적으로 인라인 가능하다.

<!--
  - test: `cant-inline-private`

  ```swifttest
  >> @inlinable private func f() { }
  !$ error: '@inlinable' 속성은 공개 선언에만 적용할 수 있지만, 'f'는 private입니다
  !! @inlinable private func f() { }
  !! ^~~~~~~~~~~
  ```
-->

<!--
  - test: `cant-inline-nested`

  ```swifttest
  >> public func outer() {
  >>    @inlinable func f() { }
  >> }
  !$ error: '@inlinable' 속성은 공개 선언에만 적용할 수 있지만, 'f'는 private입니다
  !! @inlinable func f() { }
  !! ^~~~~~~~~~~
  !!-
  ```
-->

<!--
  TODO: When we get resilience, this will actually be a problem.
  Until then, per discussion with [Contributor 6004], there's no (supported) way
  for folks to get into the state where this behavior would be triggered.

  If a project uses a module that includes inlinable functions,
  the inlined copies aren't necessarily updated
  when the module's implementation of the function changes.
  For this reason,
  an inlinable function must be compatible with
  every past version of that function.
  In most cases, this means
  externally visible aspects of their implementation can't be changed.
  For example,
  an inlinable hash function can't change what algorithm is used ---
  inlined copies outside the module would use the old algorithm
  and the noninlined copy would use the new algorithm,
  yielding inconsistent results.
-->


### main

이 속성을 구조체, 클래스, 열거형 선언에 적용해 프로그램 흐름의 최상위 진입점을 나타낸다. 해당 타입은 인자를 받지 않고 `Void`를 반환하는 `main` 타입 함수를 제공해야 한다. 예를 들어:

```swift
@main
struct MyTopLevel {
    static func main() {
        // 최상위 코드를 여기에 작성한다
    }
}
```

<!--
  - test: `atMain`

  ```swifttest
  -> @main
  -> struct MyTopLevel {
  ->     static func main() {
  ->         // 최상위 코드를 여기에 작성한다
  >>         print("Hello")
  ->     }
  -> }
  << Hello
  ```
-->

`main` 속성의 요구사항을 설명하는 또 다른 방법은, 이 속성을 작성한 타입이 다음과 같은 가상 프로토콜을 준수하는 타입과 동일한 요구사항을 충족해야 한다는 것이다:

```swift
protocol ProvidesMain {
    static func main() throws
}
```

<!--
  - test: `atMain_ProvidesMain`

  ```swifttest
  -> protocol ProvidesMain {
         static func main() throws
     }
  ```
-->

실행 파일을 만들기 위해 컴파일하는 Swift 코드는 최대 하나의 최상위 진입점만 포함할 수 있다. 이는 <doc:Declarations#Top-Level-Code>에서 논의한 바와 같다.

<!--
  - test: `no-at-main-in-top-level-code`

  ```swifttest
  // 이 예제는 atMain과 동일하지만 :compile: true 없이 작성되었다.
  >> @main
  >> struct MyTopLevel {
  >>     static func main() {
  >>         print("Hello")
  >>     }
  >> }
  !$ error: 'main' 속성은 최상위 코드를 포함하는 모듈에서 사용할 수 없다
  !! @main
  !! ^
  !$ note: 이 소스 파일에 정의된 최상위 코드
  !! @main
  !! ^
  ```
-->

<!--
  - test: `atMain_library`

  ```swifttest
  -> // 파일 "library.swift"에서
  -> open class C {
         public static func main() { print("Hello") }
     }
  ```
-->

<!--
  - test: `atMain_client`

  ```swifttest
  -> import atMain_library
  -> @main class CC: C { }
  ```
-->


`nonobjc` 속성을 메서드, 프로퍼티, 서브스크립트, 또는 초기화 선언에 적용하면 암시적인 `objc` 속성을 억제할 수 있다. `nonobjc` 속성은 해당 선언이 Objective-C 코드에서 사용 불가능하도록 컴파일러에 지시한다. 비록 Objective-C로 표현할 수 있는 경우에도 이 속성이 적용되면 사용할 수 없다.

이 속성을 익스텐션에 적용하면, `objc` 속성이 명시적으로 표시되지 않은 모든 멤버에 동일한 효과가 적용된다.

`nonobjc` 속성은 `objc` 속성이 적용된 클래스에서 브리징 메서드의 순환 참조 문제를 해결하거나, `objc` 속성이 적용된 클래스에서 메서드와 초기화 메서드의 오버로딩을 허용하기 위해 사용한다.

`nonobjc` 속성이 적용된 메서드는 `objc` 속성이 적용된 메서드를 오버라이드할 수 없다. 반대로 `objc` 속성이 적용된 메서드는 `nonobjc` 속성이 적용된 메서드를 오버라이드할 수 있다. 마찬가지로, `nonobjc` 속성이 적용된 메서드는 `objc` 속성이 적용된 메서드의 프로토콜 요구 사항을 충족할 수 없다.


### NSApplicationMain

> Deprecated:
> 이 속성은 더 이상 사용되지 않는다.
> 대신 <doc:Attributes#main> 속성을 사용한다.
> Swift 6에서는 이 속성을 사용하면 오류가 발생한다.

이 속성을 클래스에 적용하면 해당 클래스가 앱 델리게이트임을 나타낸다.
이 속성을 사용하는 것은 `NSApplicationMain(_:_:)` 함수를 호출하는 것과 동일하다.

이 속성을 사용하지 않는다면,
최상위 수준에서 `NSApplicationMain(_:_:)` 함수를 호출하는 코드를 포함한 `main.swift` 파일을 제공해야 한다.
예를 들면 다음과 같다:

```swift
import AppKit
NSApplicationMain(CommandLine.argc, CommandLine.unsafeArgv)
```

<!--
  위 코드는 REPL에서 무한정 멈추기 때문에 테스트하지 않았다.
  이와 같은 반환하지 않는 함수를 호출할 때의 올바른 동작이다.
-->

실행 파일을 만들기 위해 컴파일하는 Swift 코드는
최대 하나의 최상위 진입점만 포함할 수 있다.
이는 <doc:Declarations#Top-Level-Code>에서 설명한 바와 같다.


### NSCopying

이 속성을 클래스의 저장 프로퍼티에 적용한다. 이 속성은 프로퍼티의 setter가 프로퍼티 자체의 값 대신 `copyWithZone(_:)` 메서드에서 반환된 값의 *복사본*을 사용하도록 만든다. 프로퍼티의 타입은 `NSCopying` 프로토콜을 준수해야 한다.

`NSCopying` 속성은 Objective-C의 `copy` 프로퍼티 속성과 유사하게 동작한다.

<!--
  TODO: Dave가 가이드에서 이 부분을 다루는 섹션을 추가한다면, 해당 섹션으로 연결할 링크를 제공한다.
-->


### NSManaged

이 속성은 `NSManagedObject`를 상속받는 클래스의 인스턴스 메서드나 저장 프로퍼티에 적용한다. Core Data가 런타임에 해당 엔티티 설명에 기반해 구현을 동적으로 제공한다는 것을 나타낸다. `NSManaged` 속성이 표시된 프로퍼티의 경우, Core Data는 런타임에 스토리지도 함께 제공한다. 이 속성을 적용하면 암묵적으로 `objc` 속성도 함께 적용된다.


### Objective-C 호환성

`objc` 속성은 Objective-C 코드에서 사용할 수 있는 선언에 적용한다. 예를 들어, 중첩되지 않은 클래스, 프로토콜, 정수형 원시 값을 사용하는 제네릭이 아닌 열거형, 클래스의 프로퍼티와 메서드(게터와 세터 포함), 프로토콜 및 프로토콜의 옵셔널 멤버, 초기화 메서드, 서브스크립트 등이 이에 해당한다. `objc` 속성은 컴파일러에게 해당 선언이 Objective-C 코드에서 사용 가능함을 알린다.

이 속성을 익스텐션에 적용하면, `nonobjc` 속성으로 명시적으로 표시되지 않은 모든 멤버에 동일한 효과가 적용된다.

컴파일러는 Objective-C로 정의된 클래스의 서브클래스에 `objc` 속성을 암시적으로 추가한다. 단, 서브클래스는 제네릭이 아니어야 하며, 제네릭 클래스를 상속받지 않아야 한다. 이러한 조건을 충족하는 서브클래스에 `objc` 속성을 명시적으로 추가해 Objective-C 이름을 지정할 수 있다. `objc` 속성이 적용된 프로토콜은 이 속성이 없는 프로토콜을 상속받을 수 없다.

`objc` 속성은 다음과 같은 경우에도 암시적으로 추가된다:

- 선언이 서브클래스에서 오버라이드되고, 부모 클래스의 선언에 `objc` 속성이 있는 경우
- 선언이 `objc` 속성이 있는 프로토콜의 요구 사항을 충족하는 경우
- 선언에 `IBAction`, `IBSegueAction`, `IBOutlet`, `IBDesignable`, `IBInspectable`, `NSManaged`, `GKInspectable` 속성이 있는 경우

열거형에 `objc` 속성을 적용하면, 각 열거형 케이스는 열거형 이름과 케이스 이름을 연결한 형태로 Objective-C 코드에 노출된다. 케이스 이름의 첫 글자는 대문자로 표시된다. 예를 들어, Swift의 `Planet` 열거형에 `venus`라는 케이스가 있으면, Objective-C 코드에서는 `PlanetVenus`라는 케이스로 노출된다.

`objc` 속성은 선택적으로 단일 인자를 받을 수 있으며, 이 인자는 식별자로 구성된다. 이 식별자는 `objc` 속성이 적용된 엔티티가 Objective-C에 노출될 때 사용할 이름을 지정한다. 이 인자를 사용해 클래스, 열거형, 열거형 케이스, 프로토콜, 메서드, 게터, 세터, 초기화 메서드의 이름을 지정할 수 있다. 클래스, 프로토콜, 또는 열거형의 Objective-C 이름을 지정할 때는 [Objective-C 프로그래밍](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011210)의 [규칙](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Conventions/Conventions.html#//apple_ref/doc/uid/TP40011210-CH10-SW1)에 따라 세 글자 접두사를 포함해야 한다. 아래 예제는 `ExampleClass`의 `enabled` 프로퍼티의 게터를 Objective-C 코드에서 `isEnabled`로 노출한다.

```swift
class ExampleClass: NSObject {
    @objc var enabled: Bool {
        @objc(isEnabled) get {
            // 적절한 값을 반환
        }
    }
}
```

<!--
  - test: `objc-attribute`

  ```swifttest
  >> import Foundation
  -> class ExampleClass: NSObject {
  ->    @objc var enabled: Bool {
  ->       @objc(isEnabled) get {
  ->          // 적절한 값을 반환
  >>          return true
  ->       }
  ->    }
  -> }
  ```
-->

더 많은 정보는 [Swift를 Objective-C로 임포트하기](https://developer.apple.com/documentation/swift/imported_c_and_objective-c_apis/importing_swift_into_objective-c)를 참고한다.

> 참고: `objc` 속성의 인자는 해당 선언의 런타임 이름도 변경할 수 있다. 런타임 이름은 Objective-C 런타임과 상호작용하는 함수를 호출할 때(예: [`NSClassFromString(_:)`](https://developer.apple.com/documentation/foundation/1395135-nsclassfromstring))나 앱의 Info.plist 파일에서 클래스 이름을 지정할 때 사용한다. 인자를 전달해 이름을 지정하면, 그 이름이 Objective-C 코드와 런타임 이름으로 사용된다. 인자를 생략하면, Objective-C 코드에서 사용하는 이름은 Swift 코드의 이름과 일치하며, 런타임 이름은 Swift 컴파일러의 일반적인 이름 맹글링 규칙을 따른다.


### objcMembers

이 속성을 클래스 선언에 적용하면, 해당 클래스와 그 확장(extensions), 하위 클래스(subclasses), 그리고 하위 클래스의 모든 확장에서 Objective-C와 호환되는 모든 멤버에 `objc` 속성이 자동으로 적용된다.

대부분의 코드는 필요한 선언만 노출하기 위해 `objc` 속성을 사용해야 한다. 많은 선언을 노출해야 할 경우, `objc` 속성이 적용된 확장(extension)으로 그룹화할 수 있다. `objcMembers` 속성은 Objective-C 런타임의 내부 검사(introspection) 기능을 많이 사용하는 라이브러리를 위해 편의를 제공한다. 필요하지 않은 곳에 `objc` 속성을 적용하면 바이너리 크기가 증가하고 성능에 부정적인 영향을 미칠 수 있다.

<!--
  바이너리 크기가 증가하는 이유는 호출 규약(calling conventions) 간 변환을 위한 추가적인 썽크(thunk) 때문이다.
  더 큰 심볼 테이블로 인해 dyld가 느려져 링크와 런치 성능이 저하된다.
-->


### preconcurrency

이 속성을 선언에 적용하면 엄격한 동시성 검사를 억제할 수 있다. 다음과 같은 종류의 선언에 이 속성을 적용할 수 있다:

- 임포트
- 구조체, 클래스, 액터
- 열거형 및 열거형 케이스
- 프로토콜
- 변수와 상수
- 서브스크립트
- 이니셜라이저
- 함수

임포트 선언에 이 속성을 적용하면, 임포트된 모듈에서 가져온 타입을 사용하는 코드에 대해 동시성 검사의 엄격성을 줄인다. 구체적으로, 임포트된 모듈에서 명시적으로 `nonsendable`로 표시되지 않은 타입은 `Sendable` 타입이 필요한 컨텍스트에서 사용할 수 있다.

다른 선언에 이 속성을 적용하면, 해당 선언을 사용하는 코드에 대해 동시성 검사의 엄격성을 줄인다. 최소한의 동시성 검사가 적용된 범위에서 이 심볼을 사용할 때, `Sendable` 요구사항이나 글로벌 액터와 같은 동시성 관련 제약 조건은 검사되지 않는다.

이 속성은 엄격한 동시성 검사로 코드를 마이그레이션하는 데 도움을 주기 위해 다음과 같이 사용할 수 있다:

1. 엄격한 검사를 활성화한다.
1. 엄격한 검사를 활성화하지 않은 모듈에 대해 `preconcurrency` 속성을 임포트에 추가한다.
1. 모듈을 엄격한 검사로 마이그레이션한 후, `preconcurrency` 속성을 제거한다. 컴파일러는 더 이상 효과가 없어 제거해야 하는 `preconcurrency` 속성이 있는 위치에 대해 경고를 표시한다.

다른 선언의 경우, 동시성 관련 제약 조건을 선언에 추가할 때 `preconcurrency` 속성을 추가할 수 있다. 아직 엄격한 검사로 마이그레이션하지 않은 클라이언트가 있는 경우에 해당한다. 모든 클라이언트가 마이그레이션한 후에는 `preconcurrency` 속성을 제거한다.

Objective-C에서 가져온 선언은 항상 `preconcurrency` 속성이 적용된 것처럼 처리된다.


### propertyWrapper

이 속성을 클래스, 구조체, 혹은 열거형 선언에 적용하면 해당 타입을 프로퍼티 래퍼로 사용할 수 있다. 이 속성을 타입에 적용하면, 타입과 동일한 이름을 가진 커스텀 속성을 생성한다. 이 새로운 속성을 클래스, 구조체, 혹은 열거형의 프로퍼티에 적용하면, 해당 프로퍼티에 대한 접근을 래퍼 타입의 인스턴스를 통해 래핑할 수 있다. 또한, 이 속성을 로컬 저장 변수 선언에 적용하면, 변수에 대한 접근도 동일한 방식으로 래핑할 수 있다. 계산된 변수, 전역 변수, 그리고 상수는 프로퍼티 래퍼를 사용할 수 없다.

<!--
  - test: `property-wrappers-can-go-on-stored-variable`

  ```swifttest
  >> @propertyWrapper struct UselessWrapper { var wrappedValue: Int }
  >> func f() {
  >>     @UselessWrapper var d: Int = 20
  >>     print(d)
  >> }
  >> f()
  << 20
  ```
-->

<!--
  - test: `property-wrappers-cant-go-on-constants`

  ```swifttest
  >> @propertyWrapper struct UselessWrapper { var wrappedValue: Int }
  >> func f() {
  >>     @UselessWrapper let d: Int = 20
  >>     print(d)
  >> }
  !$ error: property wrapper can only be applied to a 'var'
  !! @UselessWrapper let d: Int = 20
  !! ^
  ```
-->

<!--
  - test: `property-wrappers-cant-go-on-computed-variable`

  ```swifttest
  >> @propertyWrapper struct UselessWrapper { var wrappedValue: Int }
  >> func f() {
  >>     @UselessWrapper var d: Int { return 20 }
  >>     print(d)
  >> }
  >> f()
  !$ error: property wrapper cannot be applied to a computed property
  !! @UselessWrapper var d: Int { return 20 }
  !! ^
  ```
-->

래퍼는 반드시 `wrappedValue` 인스턴스 프로퍼티를 정의해야 한다. 프로퍼티의 *래핑된 값*은 이 프로퍼티의 getter와 setter가 노출하는 값이다. 대부분의 경우, `wrappedValue`는 계산된 값이지만, 저장된 값일 수도 있다. 래퍼는 래핑된 값에 필요한 모든 기본 저장소를 정의하고 관리한다. 컴파일러는 래퍼 타입의 인스턴스에 대한 저장소를 생성하며, 래핑된 프로퍼티 이름 앞에 밑줄(`_`)을 붙인다. 예를 들어, `someProperty`의 래퍼는 `_someProperty`로 저장된다. 래퍼에 대한 생성된 저장소는 `private` 접근 제어 수준을 가진다.

프로퍼티 래퍼를 가진 프로퍼티는 `willSet`과 `didSet` 블록을 포함할 수 있지만, 컴파일러가 생성한 `get` 또는 `set` 블록을 재정의할 수는 없다.

Swift는 프로퍼티 래퍼 초기화를 위해 두 가지 형태의 문법적 편의를 제공한다. 래핑된 값의 정의에서 할당 문법을 사용할 수 있으며, 이때 할당의 오른쪽에 있는 표현식은 프로퍼티 래퍼의 초기화 함수의 `wrappedValue` 매개변수로 전달된다. 또한, 프로퍼티에 속성을 적용할 때 인자를 제공할 수 있으며, 이 인자들은 프로퍼티 래퍼의 초기화 함수로 전달된다. 예를 들어, 아래 코드에서 `SomeStruct`는 `SomeWrapper`가 정의한 각 초기화 함수를 호출한다.

```swift
@propertyWrapper
struct SomeWrapper {
    var wrappedValue: Int
    var someValue: Double
    init() {
        self.wrappedValue = 100
        self.someValue = 12.3
    }
    init(wrappedValue: Int) {
        self.wrappedValue = wrappedValue
        self.someValue = 45.6
    }
    init(wrappedValue value: Int, custom: Double) {
        self.wrappedValue = value
        self.someValue = custom
    }
}

struct SomeStruct {
    // Uses init()
    @SomeWrapper var a: Int

    // Uses init(wrappedValue:)
    @SomeWrapper var b = 10

    // Both use init(wrappedValue:custom:)
    @SomeWrapper(custom: 98.7) var c = 30
    @SomeWrapper(wrappedValue: 30, custom: 98.7) var d
}
```

<!--
  - test: `propertyWrapper`

  ```swifttest
  -> @propertyWrapper
  -> struct SomeWrapper {
         var wrappedValue: Int
         var someValue: Double
         init() {
             self.wrappedValue = 100
             self.someValue = 12.3
         }
         init(wrappedValue: Int) {
             self.wrappedValue = wrappedValue
             self.someValue = 45.6
         }
         init(wrappedValue value: Int, custom: Double) {
             self.wrappedValue = value
             self.someValue = custom
         }
     }

  -> struct SomeStruct {
  ->     // Uses init()
  ->     @SomeWrapper var a: Int

  ->     // Uses init(wrappedValue:)
  ->     @SomeWrapper var b = 10

  ->     // Both use init(wrappedValue:custom:)
  ->     @SomeWrapper(custom: 98.7) var c = 30
  ->     @SomeWrapper(wrappedValue: 30, custom: 98.7) var d
  -> }
  ```
-->

<!--
  Comments in the SomeStruct part of the example above
  are on the line before instead of at the end of the line
  because the last example gets too long to fit on one line.
-->

<!--
  Initialization of a wrapped property using ``init(wrappedValue:)``
  can be split across multiple statements.
  However, you can only see that behavior using local variables
  which currently can't have a property wrapper.
  It would look like this:

  -> @SomeWrapper var e
  -> e = 20  // Uses init(wrappedValue:)
  -> e = 30  // Uses the property setter
-->

래핑된 프로퍼티의 *투영된 값*은 프로퍼티 래퍼가 추가 기능을 노출하기 위해 사용할 수 있는 두 번째 값이다. 프로퍼티 래퍼 타입의 작성자는 투영된 값의 의미를 결정하고, 투영된 값이 노출하는 인터페이스를 정의할 책임이 있다. 프로퍼티 래퍼에서 값을 투영하려면, 래퍼 타입에 `projectedValue` 인스턴스 프로퍼티를 정의해야 한다. 컴파일러는 투영된 값에 대한 식별자를 생성하며, 이때 래핑된 프로퍼티 이름 앞에 달러 기호(`$`)를 붙인다. 예를 들어, `someProperty`의 투영된 값은 `$someProperty`이다. 투영된 값은 원래 래핑된 프로퍼티와 동일한 접근 제어 수준을 가진다.

```swift
@propertyWrapper
struct WrapperWithProjection {
    var wrappedValue: Int
    var projectedValue: SomeProjection {
        return SomeProjection(wrapper: self)
    }
}
struct SomeProjection {
    var wrapper: WrapperWithProjection
}

struct SomeStruct {
    @WrapperWithProjection var x = 123
}
let s = SomeStruct()
s.x           // Int value
s.$x          // SomeProjection value
s.$x.wrapper  // WrapperWithProjection value
```

<!--
  - test: `propertyWrapper-projection`

  ```swifttest
  -> @propertyWrapper
  -> struct WrapperWithProjection {
         var wrappedValue: Int
         var projectedValue: SomeProjection {
             return SomeProjection(wrapper: self)
         }
  }
  -> struct SomeProjection {
         var wrapper: WrapperWithProjection
  }

  -> struct SomeStruct {
  ->     @WrapperWithProjection var x = 123
  -> }
  -> let s = SomeStruct()
  >> _ =
  -> s.x           // Int value
  >> _ =
  -> s.$x          // SomeProjection value
  >> _ =
  -> s.$x.wrapper  // WrapperWithProjection value
  ```
-->


### resultBuilder

이 속성을 클래스, 구조체, 혹은 열거형에 적용하면 해당 타입을 결과 빌더로 사용할 수 있다. **결과 빌더**는 단계별로 중첩된 데이터 구조를 만드는 타입이다. 결과 빌더를 사용하면 자연스럽고 선언적인 방식으로 중첩된 데이터 구조를 생성하는 도메인 특화 언어(DSL)를 구현할 수 있다. `resultBuilder` 속성을 어떻게 사용하는지 예제를 보려면 <doc:AdvancedOperators#Result-Builders>를 참고한다.


#### 결과 빌더 메서드

결과 빌더는 아래 설명된 정적 메서드를 구현한다. 결과 빌더의 모든 기능이 정적 메서드를 통해 제공되기 때문에, 해당 타입의 인스턴스를 초기화할 필요가 없다. 결과 빌더는 `buildBlock(_:)` 메서드 또는 `buildPartialBlock(first:)`와 `buildPartialBlock(accumulated:next:)` 메서드를 모두 구현해야 한다. DSL에서 추가 기능을 가능하게 하는 다른 메서드들은 선택 사항이다. 결과 빌더 타입의 선언은 실제로 프로토콜 준수를 포함할 필요가 없다.

정적 메서드 설명에는 세 가지 타입이 자리 표시자로 사용된다. `Expression` 타입은 결과 빌더의 입력 타입을 나타내는 자리 표시자이고, `Component`는 부분 결과의 타입을 나타내는 자리 표시자이며, `FinalResult`는 결과 빌더가 생성하는 최종 결과의 타입을 나타내는 자리 표시자이다. 이 타입들은 결과 빌더가 실제로 사용하는 타입으로 대체한다. 결과 빌더 메서드가 `Expression` 또는 `FinalResult`에 대한 타입을 지정하지 않으면, 기본적으로 `Component`와 동일한 타입으로 간주한다.

블록 빌딩 메서드는 다음과 같다:

- term `static func buildBlock(_ components: Component...) -> Component`:
  여러 부분 결과를 하나의 부분 결과로 결합한다.

- term `static func buildPartialBlock(first: Component) -> Component`:
  첫 번째 컴포넌트로부터 부분 결과를 생성한다. 이 메서드와 `buildPartialBlock(accumulated:next:)`를 모두 구현하여 한 번에 하나의 컴포넌트씩 블록을 빌드할 수 있다. `buildBlock(_:)`에 비해 이 방법은 다양한 수의 인자를 처리하기 위한 제네릭 오버로드의 필요성을 줄인다.

- term `static func buildPartialBlock(accumulated: Component, next: Component) -> Component`:
  누적된 컴포넌트와 새로운 컴포넌트를 결합하여 부분 결과를 생성한다. 이 메서드와 `buildPartialBlock(first:)`를 모두 구현하여 한 번에 하나의 컴포넌트씩 블록을 빌드할 수 있다. `buildBlock(_:)`에 비해 이 방법은 다양한 수의 인자를 처리하기 위한 제네릭 오버로드의 필요성을 줄인다.

결과 빌더는 위에 나열된 세 가지 블록 빌딩 메서드를 모두 구현할 수 있다. 이 경우, 사용 가능성에 따라 어떤 메서드가 호출될지 결정된다. 기본적으로 Swift는 `buildPartialBlock(first:)`와 `buildPartialBlock(accumulated:next:)` 메서드를 호출한다. Swift가 `buildBlock(_:)`을 호출하도록 하려면, `buildPartialBlock(first:)`와 `buildPartialBlock(accumulated:next:)`에 작성한 사용 가능성 이전에 해당 선언을 사용 가능으로 표시해야 한다.

추가 결과 빌딩 메서드는 다음과 같다:

- term `static func buildOptional(_ component: Component?) -> Component`:
  `nil`일 수 있는 부분 결과로부터 부분 결과를 생성한다. `else` 절이 없는 `if` 문을 지원하려면 이 메서드를 구현한다.

- term `static func buildEither(first: Component) -> Component`:
  특정 조건에 따라 값이 달라지는 부분 결과를 생성한다. `switch` 문과 `else` 절이 포함된 `if` 문을 지원하려면 이 메서드와 `buildEither(second:)`를 모두 구현한다.

- term `static func buildEither(second: Component) -> Component`:
  특정 조건에 따라 값이 달라지는 부분 결과를 생성한다. `switch` 문과 `else` 절이 포함된 `if` 문을 지원하려면 이 메서드와 `buildEither(first:)`를 모두 구현한다.

- term `static func buildArray(_ components: [Component]) -> Component`:
  부분 결과 배열로부터 부분 결과를 생성한다. `for` 루프를 지원하려면 이 메서드를 구현한다.

- term `static func buildExpression(_ expression: Expression) -> Component`:
  표현식으로부터 부분 결과를 생성한다. 이 메서드를 구현하여 전처리를 수행하거나(예: 표현식을 내부 타입으로 변환) 사용 지점에서 타입 추론을 위한 추가 정보를 제공할 수 있다.

- term `static func buildFinalResult(_ component: Component) -> FinalResult`:
  부분 결과로부터 최종 결과를 생성한다. 부분 결과와 최종 결과에 대해 다른 타입을 사용하는 결과 빌더의 일부로 이 메서드를 구현하거나, 결과를 반환하기 전에 다른 후처리를 수행할 수 있다.

- term `static func buildLimitedAvailability(_ component: Component) -> Component`:
  타입 정보를 지우는 부분 결과를 생성한다. 이 메서드를 구현하여 컴파일러 제어문 외부로 타입 정보가 전파되는 것을 방지할 수 있다.

예를 들어, 아래 코드는 정수 배열을 생성하는 간단한 결과 빌더를 정의한다. 이 코드는 `Component`와 `Expression`을 타입 별칭으로 정의하여 위의 메서드 목록과 예제를 쉽게 매칭할 수 있게 한다.

```swift
@resultBuilder
struct ArrayBuilder {
    typealias Component = [Int]
    typealias Expression = Int
    static func buildExpression(_ element: Expression) -> Component {
        return [element]
    }
    static func buildOptional(_ component: Component?) -> Component {
        guard let component = component else { return [] }
        return component
    }
    static func buildEither(first component: Component) -> Component {
        return component
    }
    static func buildEither(second component: Component) -> Component {
        return component
    }
    static func buildArray(_ components: [Component]) -> Component {
        return Array(components.joined())
    }
    static func buildBlock(_ components: Component...) -> Component {
        return Array(components.joined())
    }
}
```

<!--
  - test: `array-result-builder`

  ```swifttest
  -> @resultBuilder
  -> struct ArrayBuilder {
         typealias Component = [Int]
         typealias Expression = Int
         static func buildExpression(_ element: Expression) -> Component {
             return [element]
         }
         static func buildOptional(_ component: Component?) -> Component {
  >>         print("Building optional...", component as Any)
             guard let component = component else { return [] }
             return component
         }
         static func buildEither(first component: Component) -> Component {
  >>         print("Building first...", component)
             return component
         }
         static func buildEither(second component: Component) -> Component {
  >>         print("Building second...", component)
             return component
         }
         static func buildArray(_ components: [Component]) -> Component {
             return Array(components.joined())
         }
         static func buildBlock(_ components: Component...) -> Component {
             return Array(components.joined())
         }
     }
  ```
-->


#### 결과 변환

다음 구문 변환은 결과 빌더 구문을 사용하는 코드를 결과 빌더 타입의 정적 메서드를 호출하는 코드로 재귀적으로 변환한다:

- 결과 빌더에 `buildExpression(_:)` 메서드가 있다면, 각 표현식은 해당 메서드 호출로 변환된다. 이 변환은 항상 첫 번째로 적용된다. 예를 들어, 다음 두 선언은 동일하다:

  ```swift
  @ArrayBuilder var builderNumber: [Int] { 10 }
  var manualNumber = ArrayBuilder.buildExpression(10)
  ```

  <!--
    - test: `array-result-builder`

    ```swifttest
    -> @ArrayBuilder var builderNumber: [Int] { 10 }
    -> var manualNumber = ArrayBuilder.buildExpression(10)
    >> assert(builderNumber == manualNumber)
    ```
  -->

- 할당문은 표현식처럼 변환되지만, `()`를 반환한다고 간주한다. `buildExpression(_:)` 메서드를 오버로드하여 `()` 타입의 인자를 받는 버전을 정의하면 할당문을 특별히 처리할 수 있다.

- 가용성 조건을 확인하는 분기문은 `buildLimitedAvailability(_:)` 메서드가 구현된 경우 해당 메서드 호출로 변환된다. `buildLimitedAvailability(_:)`를 구현하지 않으면, 가용성을 확인하는 분기문은 다른 분기문과 동일한 변환을 거친다. 이 변환은 `buildEither(first:)`, `buildEither(second:)`, 또는 `buildOptional(_:)` 호출로 변환되기 전에 수행된다.

  `buildLimitedAvailability(_:)` 메서드는 선택된 분기에 따라 달라지는 타입 정보를 지우는 데 사용된다. 예를 들어, 아래의 `buildEither(first:)`와 `buildEither(second:)` 메서드는 두 분기에 대한 타입 정보를 캡처하는 제네릭 타입을 사용한다.

  ```swift
  protocol Drawable {
      func draw() -> String
  }
  struct Text: Drawable {
      var content: String
      init(_ content: String) { self.content = content }
      func draw() -> String { return content }
  }
  struct Line<D: Drawable>: Drawable {
      var elements: [D]
      func draw() -> String {
          return elements.map { $0.draw() }.joined(separator: "")
      }
  }
  struct DrawEither<First: Drawable, Second: Drawable>: Drawable {
      var content: Drawable
      func draw() -> String { return content.draw() }
  }

  @resultBuilder
  struct DrawingBuilder {
      static func buildBlock<D: Drawable>(_ components: D...) -> Line<D> {
          return Line(elements: components)
      }
      static func buildEither<First, Second>(first: First)
              -> DrawEither<First, Second> {
          return DrawEither(content: first)
      }
      static func buildEither<First, Second>(second: Second)
              -> DrawEither<First, Second> {
          return DrawEither(content: second)
      }
  }
  ```

  그러나 이 접근 방식은 가용성 검사가 있는 코드에서 문제를 일으킬 수 있다:

  ```swift
  @available(macOS 99, *)
  struct FutureText: Drawable {
      var content: String
      init(_ content: String) { self.content = content }
      func draw() -> String { return content }
  }
  @DrawingBuilder var brokenDrawing: Drawable {
      if #available(macOS 99, *) {
          FutureText("Inside.future")  // 문제 발생
      } else {
          Text("Inside.present")
      }
  }
  // brokenDrawing의 타입은 Line<DrawEither<Line<FutureText>, Line<Text>>>
  ```

  위 코드에서 `FutureText`는 `DrawEither` 제네릭 타입의 일부로 `brokenDrawing`의 타입에 나타난다. 이는 런타임에 `FutureText`가 사용되지 않는 경우에도 프로그램이 충돌할 수 있다.

  이 문제를 해결하기 위해 `buildLimitedAvailability(_:)` 메서드를 구현하여 항상 사용 가능한 타입을 반환함으로써 타입 정보를 지울 수 있다. 예를 들어, 아래 코드는 가용성 검사에서 `AnyDrawable` 값을 생성한다.

  ```swift
  struct AnyDrawable: Drawable {
      var content: Drawable
      func draw() -> String { return content.draw() }
  }
  extension DrawingBuilder {
      static func buildLimitedAvailability(_ content: some Drawable) -> AnyDrawable {
          return AnyDrawable(content: content)
      }
  }

  @DrawingBuilder var typeErasedDrawing: Drawable {
      if #available(macOS 99, *) {
          FutureText("Inside.future")
      } else {
          Text("Inside.present")
      }
  }
  // typeErasedDrawing의 타입은 Line<DrawEither<AnyDrawable, Line<Text>>>
  ```

- 분기문은 `buildEither(first:)`와 `buildEither(second:)` 메서드에 대한 일련의 중첩 호출로 변환된다. 문장의 조건과 케이스는 이진 트리의 리프 노드에 매핑되며, 문장은 루트 노드에서 해당 리프 노드로의 경로를 따라 `buildEither` 메서드의 중첩 호출이 된다.

  예를 들어, 세 가지 케이스가 있는 `switch` 문을 작성하면 컴파일러는 세 개의 리프 노드가 있는 이진 트리를 사용한다. 마찬가지로, 루트 노드에서 두 번째 케이스로의 경로가 "두 번째 자식" 다음에 "첫 번째 자식"이라면, 해당 케이스는 `buildEither(first: buildEither(second: ... ))`와 같은 중첩 호출이 된다. 다음 두 선언은 동일하다:

  ```swift
  let someNumber = 19
  @ArrayBuilder var builderConditional: [Int] {
      if someNumber < 12 {
          31
      } else if someNumber == 19 {
          32
      } else {
          33
      }
  }

  var manualConditional: [Int]
  if someNumber < 12 {
      let partialResult = ArrayBuilder.buildExpression(31)
      let outerPartialResult = ArrayBuilder.buildEither(first: partialResult)
      manualConditional = ArrayBuilder.buildEither(first: outerPartialResult)
  } else if someNumber == 19 {
      let partialResult = ArrayBuilder.buildExpression(32)
      let outerPartialResult = ArrayBuilder.buildEither(second: partialResult)
      manualConditional = ArrayBuilder.buildEither(first: outerPartialResult)
  } else {
      let partialResult = ArrayBuilder.buildExpression(33)
      manualConditional = ArrayBuilder.buildEither(second: partialResult)
  }
  ```

- 값을 생성하지 않을 수 있는 분기문(예: `else` 절이 없는 `if` 문)은 `buildOptional(_:)` 호출로 변환된다. `if` 문의 조건이 충족되면 해당 코드 블록이 변환되어 인자로 전달되고, 그렇지 않으면 `buildOptional(_:)`이 `nil`을 인자로 호출된다. 예를 들어, 다음 두 선언은 동일하다:

  ```swift
  @ArrayBuilder var builderOptional: [Int] {
      if (someNumber % 2) == 1 { 20 }
  }

  var partialResult: [Int]? = nil
  if (someNumber % 2) == 1 {
      partialResult = ArrayBuilder.buildExpression(20)
  }
  var manualOptional = ArrayBuilder.buildOptional(partialResult)
  ```

- 결과 빌더가 `buildPartialBlock(first:)`와 `buildPartialBlock(accumulated:next:)` 메서드를 구현한다면, 코드 블록 또는 `do` 문은 해당 메서드 호출로 변환된다. 블록 내의 첫 번째 문장은 `buildPartialBlock(first:)` 메서드의 인자로 변환되고, 나머지 문장은 `buildPartialBlock(accumulated:next:)` 메서드의 중첩 호출이 된다. 예를 들어, 다음 두 선언은 동일하다:

  ```swift
  struct DrawBoth<First: Drawable, Second: Drawable>: Drawable {
      var first: First
      var second: Second
      func draw() -> String { return first.draw() + second.draw() }
  }

  @resultBuilder
  struct DrawingPartialBlockBuilder {
      static func buildPartialBlock<D: Drawable>(first: D) -> D {
          return first
      }
      static func buildPartialBlock<Accumulated: Drawable, Next: Drawable>(
          accumulated: Accumulated, next: Next
      ) -> DrawBoth<Accumulated, Next> {
          return DrawBoth(first: accumulated, second: next)
      }
  }

  @DrawingPartialBlockBuilder var builderBlock: some Drawable {
      Text("First")
      Line(elements: [Text("Second"), Text("Third")])
      Text("Last")
  }

  let partialResult1 = DrawingPartialBlockBuilder.buildPartialBlock(first: Text("first"))
  let partialResult2 = DrawingPartialBlockBuilder.buildPartialBlock(
      accumulated: partialResult1,
      next: Line(elements: [Text("Second"), Text("Third")])
  )
  let manualResult = DrawingPartialBlockBuilder.buildPartialBlock(
      accumulated: partialResult2,
      next: Text("Last")
  )
  ```

- 그렇지 않으면, 코드 블록 또는 `do` 문은 `buildBlock(_:)` 메서드 호출로 변환된다. 블록 내의 각 문장은 하나씩 변환되어 `buildBlock(_:)` 메서드의 인자가 된다. 예를 들어, 다음 두 선언은 동일하다:

  ```swift
  @ArrayBuilder var builderBlock: [Int] {
      100
      200
      300
  }

  var manualBlock = ArrayBuilder.buildBlock(
      ArrayBuilder.buildExpression(100),
      ArrayBuilder.buildExpression(200),
      ArrayBuilder.buildExpression(300)
  )
  ```

- `for` 루프는 임시 변수, `for` 루프, 그리고 `buildArray(_:)` 메서드 호출로 변환된다. 새로운 `for` 루프는 시퀀스를 순회하며 각 부분 결과를 배열에 추가한다. 임시 배열은 `buildArray(_:)` 호출의 인자로 전달된다. 예를 들어, 다음 두 선언은 동일하다:

  ```swift
  @ArrayBuilder var builderArray: [Int] {
      for i in 5...7 {
          100 + i
      }
  }

  var temporary: [[Int]] = []
  for i in 5...7 {
      let partialResult = ArrayBuilder.buildExpression(100 + i)
      temporary.append(partialResult)
  }
  let manualArray = ArrayBuilder.buildArray(temporary)
  ```

- 결과 빌더에 `buildFinalResult(_:)` 메서드가 있다면, 최종 결과는 해당 메서드 호출로 변환된다. 이 변환은 항상 마지막에 적용된다.

변환 동작은 임시 변수를 기준으로 설명되지만, 결과 빌더를 사용해도 실제로는 코드의 나머지 부분에서 볼 수 있는 새로운 선언이 생성되지 않는다.

결과 빌더가 변환하는 코드에서는 `break`, `continue`, `defer`, `guard`, `return` 문, `while` 문, 또는 `do`-`catch` 문을 사용할 수 없다.

변환 프로세스는 코드 내의 선언을 변경하지 않으므로, 표현식을 조금씩 구축하기 위해 임시 상수와 변수를 사용할 수 있다. 또한 `throw` 문, 컴파일 타임 진단 문, 또는 `return` 문이 포함된 클로저도 변경되지 않는다.

가능한 경우, 변환은 통합된다. 예를 들어, 표현식 `4 + 5 * 6`은 해당 함수에 대한 여러 호출 대신 `buildExpression(4 + 5 * 6)`이 된다. 마찬가지로, 중첩된 분기문은 `buildEither` 메서드 호출의 단일 이진 트리가 된다.


#### 커스텀 결과 빌더 어트리뷰트

결과 빌더 타입을 생성하면 동일한 이름의 커스텀 어트리뷰트가 만들어진다. 이 어트리뷰트는 다음과 같은 위치에 적용할 수 있다:

- 함수 선언에 적용하면, 결과 빌더가 함수의 본문을 구성한다.
- getter를 포함하는 변수나 서브스크립트 선언에 적용하면, 결과 빌더가 getter의 본문을 구성한다.
- 함수 선언의 매개변수에 적용하면, 결과 빌더가 해당 인자로 전달되는 클로저의 본문을 구성한다.

결과 빌더 어트리뷰트를 적용해도 ABI 호환성에는 영향을 미치지 않는다. 하지만 매개변수에 결과 빌더 어트리뷰트를 적용하면, 이 어트리뷰트가 함수의 인터페이스의 일부가 되어 소스 호환성에 영향을 줄 수 있다.


### requires_stored_property_inits

이 속성은 클래스 선언에 적용하여 클래스 내 모든 저장 프로퍼티가 정의 시 기본값을 제공하도록 요구한다. 이 속성은 `NSManagedObject`를 상속받는 모든 클래스에서 암시적으로 적용된다.

<!--
  - test: `requires_stored_property_inits-requires-default-values`

  ```swifttest
  >> @requires_stored_property_inits class DefaultValueProvided {
         var value: Int = -1
         init() { self.value = 0 }
     }
  -> @requires_stored_property_inits class NoDefaultValue {
         var value: Int
         init() { self.value = 0 }
     }
  !$ error: stored property 'value' requires an initial value
  !! var value: Int
  !! ^
  !$ note: class 'NoDefaultValue' requires all stored properties to have initial values
  !! @requires_stored_property_inits class NoDefaultValue {
  !! ^
  ```
-->


### testable

이 속성을 `import` 선언에 적용하면
모듈의 접근 제어를 변경하여 테스트를 간소화할 수 있다.
임포트된 모듈 내부에서
`internal` 접근 레벨으로 표시된 엔티티들은
`public` 접근 레벨으로 선언된 것처럼 임포트된다.
`internal` 또는 `public` 접근 레벨으로 표시된
클래스와 클래스 멤버들은
`open` 접근 레벨으로 선언된 것처럼 임포트된다.
임포트된 모듈은 테스트가 활성화된 상태로 컴파일되어야 한다.


### UIApplicationMain

> **사용 중단:**
> 이 속성은 더 이상 사용되지 않는다.
> 대신 <doc:Attributes#main> 속성을 사용한다.
> Swift 6부터는 이 속성을 사용하면 오류가 발생한다.

이 속성을 클래스에 적용하여
앱 델리게이트임을 나타낸다.
이 속성을 사용하는 것은
`UIApplicationMain` 함수를 호출하고
델리게이트 클래스의 이름으로 이 클래스의 이름을 전달하는 것과 같다.

이 속성을 사용하지 않는다면,
`main.swift` 파일을 제공하고
최상위 수준에서 [`UIApplicationMain(_:_:_:_:)`](https://developer.apple.com/documentation/uikit/1622933-uiapplicationmain) 함수를 호출하는 코드를 작성한다.
예를 들어,
앱이 주 클래스로 `UIApplication`의 커스텀 서브클래스를 사용한다면,
이 속성을 사용하는 대신
`UIApplicationMain(_:_:_:_:)` 함수를 호출한다.

실행 파일을 만들기 위해 컴파일하는 Swift 코드는
최대 하나의 최상위 진입점만 포함할 수 있다.
이는 <doc:Declarations#Top-Level-Code>에서 설명한 바와 같다.


### unchecked

이 속성을 프로토콜 타입에 적용해 선언된 타입의 채택 프로토콜 목록에 포함시키면, 해당 프로토콜의 요구사항을 강제하지 않는다.

현재 지원되는 유일한 프로토콜은 [`Sendable`](https://developer.apple.com/documentation/swift/sendable)이다.


### usableFromInline

이 속성을 함수, 메서드, 계산된 프로퍼티, 서브스크립트, 이니셜라이저, 혹은 디이니셜라이저 선언에 적용하면, 동일 모듈 내에서 정의된 인라인 가능한 코드에서 해당 심볼을 사용할 수 있다. 이때, 선언은 반드시 `internal` 접근 레벨을 가져야 한다. `usableFromInline`으로 표시된 구조체나 클래스는 프로퍼티에 대해 `public`이거나 `usableFromInline`인 타입만 사용할 수 있다. `usableFromInline`으로 표시된 열거형은 케이스의 원시 값과 연관 값에 대해 `public`이거나 `usableFromInline`인 타입만 사용할 수 있다.

`public` 접근 레벨과 마찬가지로, 이 속성은 선언을 모듈의 공개 인터페이스의 일부로 노출한다. 그러나 `public`과 달리, 컴파일러는 `usableFromInline`으로 표시된 선언을 모듈 외부의 코드에서 이름으로 참조하는 것을 허용하지 않는다. 심볼이 내보내지더라도 말이다. 하지만 모듈 외부의 코드는 여전히 런타임 동작을 통해 해당 심볼과 상호작용할 수 있다.

`inlinable` 속성으로 표시된 선언은 암묵적으로 인라인 가능한 코드에서 사용할 수 있다. `inlinable`이나 `usableFromInline` 중 하나는 `internal` 선언에 적용할 수 있지만, 두 속성을 동시에 적용하면 오류가 발생한다.

<!--
  - test: `usableFromInline-and-inlinable-is-redundant`

  ```swifttest
  >> @usableFromInline @inlinable internal func f() { }
  !$ warning: '@usableFromInline' attribute has no effect on '@inlinable' global function 'f()'
  !! @usableFromInline @inlinable internal func f() { }
  !! ^~~~~~~~~~~~~~~~~~
  ```
-->


### warn_unqualified_access

이 속성은 최상위 함수, 인스턴스 메서드, 클래스 또는 정적 메서드에 적용한다. 해당 함수나 메서드가 모듈 이름, 타입 이름, 인스턴스 변수 또는 상수와 같은 한정자 없이 사용될 때 경고를 트리거한다. 이 속성을 사용하면 동일한 스코프에서 접근 가능한 동일한 이름의 함수 간 모호성을 줄이는 데 도움이 된다.

예를 들어, Swift 표준 라이브러리에는 최상위 [`min(_:_:)`](https://developer.apple.com/documentation/swift/1538339-min/) 함수와 비교 가능한 요소를 가진 시퀀스를 위한 [`min()`](https://developer.apple.com/documentation/swift/sequence/1641174-min) 메서드가 모두 포함되어 있다. 시퀀스 메서드는 `warn_unqualified_access` 속성과 함께 선언되어, `Sequence` 확장 내에서 둘 중 하나를 사용하려고 할 때 혼동을 줄이는 데 도움을 준다.


### 인터페이스 빌더에서 사용하는 선언 속성

인터페이스 빌더 속성은 Xcode와 동기화하기 위해 인터페이스 빌더에서 사용하는 선언 속성이다. Swift는 다음과 같은 인터페이스 빌더 속성을 제공한다: `IBAction`, `IBSegueAction`, `IBOutlet`, `IBDesignable`, `IBInspectable`. 이 속성들은 개념적으로 Objective-C의 동일한 속성들과 같다.

<!--
  TODO: Need to link to the relevant discussion of these attributes in Objc.
-->

`IBOutlet`과 `IBInspectable` 속성은 클래스의 프로퍼티 선언에 적용한다. `IBAction`과 `IBSegueAction` 속성은 클래스의 메서드 선언에, `IBDesignable` 속성은 클래스 선언에 적용한다.

`IBAction`, `IBSegueAction`, `IBOutlet`, `IBDesignable`, `IBInspectable` 속성을 적용하면 `objc` 속성도 암시적으로 적용된다.


## 타입 속성

타입 속성은 타입에만 적용할 수 있다.


### autoclosure

이 속성은 표현식의 평가를 지연하기 위해 사용한다. 인자가 없는 클로저로 표현식을 자동으로 감싸는 방식으로 동작한다. 함수나 메서드 선언에서 파라미터의 타입에 적용할 수 있으며, 이때 파라미터의 타입은 인자가 없고 표현식의 타입을 반환하는 함수 타입이어야 한다. `autoclosure` 속성을 사용하는 방법은 <doc:Closures#Autoclosures>와 <doc:Types#Function-Type>에서 확인할 수 있다.


### 호출 규약

함수 타입에 이 속성을 적용하면 해당 함수의 호출 규약을 지정할 수 있다.

`convention` 속성은 항상 다음 인자 중 하나와 함께 사용된다:

- `swift` 인자는 Swift 함수 참조를 나타낸다. 이는 Swift에서 함수 값의 표준 호출 규약이다.
- `block` 인자는 Objective-C와 호환되는 블록 참조를 나타낸다. 함수 값은 블록 객체에 대한 참조로 표현되며, 이 객체는 `id`와 호환되는 Objective-C 객체로, 객체 내부에 호출 함수를 포함한다. 호출 함수는 C 호출 규약을 사용한다.
- `c` 인자는 C 함수 참조를 나타낸다. 함수 값은 컨텍스트를 가지지 않으며 C 호출 규약을 사용한다.

<!--
  참고: @convention(thin)은 비공개이며, 밑줄이 없더라도 비공개로 간주된다.
  https://forums.swift.org/t/12087/6
-->

몇 가지 예외를 제외하면, 어떤 호출 규약을 가진 함수도 다른 호출 규약이 필요한 경우에 사용할 수 있다. 제네릭이 아닌 전역 함수, 지역 변수를 캡처하지 않는 지역 함수, 또는 지역 변수를 캡처하지 않는 클로저는 C 호출 규약으로 변환할 수 있다. 다른 Swift 함수는 C 호출 규약으로 변환할 수 없다. Objective-C 블록 호출 규약을 가진 함수는 C 호출 규약으로 변환할 수 없다.


### escaping

이 속성은 함수나 메서드 선언에서 매개변수의 타입에 적용한다. 이를 통해 매개변수의 값을 나중에 실행할 수 있도록 저장할 수 있음을 나타낸다. 즉, 이 값은 호출의 생명주기를 넘어서도 존재할 수 있다. `escaping` 타입 속성이 적용된 함수 타입 매개변수는 프로퍼티나 메서드를 사용할 때 명시적으로 `self.`를 사용해야 한다. `escaping` 속성을 어떻게 사용하는지에 대한 예제는 <doc:Closures#Escaping-Closures>를 참고한다.


### Sendable

이 속성은 함수 타입에 적용하여, 해당 함수나 클로저가 `Sendable`임을 나타낸다. 이 속성을 함수 타입에 적용하는 것은 비함수 타입이 [`Sendable`](https://developer.apple.com/documentation/swift/sendable) 프로토콜을 준수하는 것과 동일한 의미를 가진다.

이 속성은 함수나 클로저가 `Sendable` 값이 필요한 문맥에서 사용되고, 해당 함수나 클로저가 `Sendable` 요구 사항을 충족할 경우 자동으로 추론된다.

`Sendable` 함수 타입은 해당하는 비 `Sendable` 함수 타입의 하위 타입이다.


## Switch Case 속성의 적용 범위

Switch case 속성은 오직 switch case에만 적용할 수 있다.


`unknown` 속성은 스위치 케이스에 적용하여, 코드가 컴파일될 때 알려진 열거형의 어떤 케이스와도 일치하지 않을 것으로 예상되는 경우를 나타낸다. 이 속성을 사용하는 방법에 대한 예제는 <doc:Statements#Switching-Over-Future-Enumeration-Cases>를 참고한다.

> 속성의 문법:
>
> *attribute* → **`@`** *attribute-name* *attribute-argument-clause*_?_ \
> *attribute-name* → *identifier* \
> *attribute-argument-clause* → **`(`** *balanced-tokens*_?_ **`)`** \
> *attributes* → *attribute* *attributes*_?_
>
> *balanced-tokens* → *balanced-token* *balanced-tokens*_?_ \
> *balanced-token* → **`(`** *balanced-tokens*_?_ **`)`** \
> *balanced-token* → **`[`** *balanced-tokens*_?_ **`]`** \
> *balanced-token* → **`{`** *balanced-tokens*_?_ **`}`** \
> *balanced-token* → Any identifier, keyword, literal, or operator \
> *balanced-token* → Any punctuation except  **`(`**,  **`)`**,  **`[`**,  **`]`**,  **`{`**, or  **`}`**

<!--
이 소스 파일은 Swift.org 오픈 소스 프로젝트의 일부다.

Copyright (c) 2014 - 2022 Apple Inc. and the Swift 프로젝트 저자들
Apache License v2.0 및 Runtime Library Exception에 따라 라이선스가 부여됨

라이선스 정보는 https://swift.org/LICENSE.txt에서 확인할 수 있다.
Swift 프로젝트 저자 목록은 https://swift.org/CONTRIBUTORS.txt에서 확인할 수 있다.
-->


