# 접근 제어

코드의 가시성을 선언, 파일, 모듈 단위로 관리한다.

*접근 제어*는 다른 소스 파일과 모듈에서 특정 코드 부분에 접근하는 것을 제한한다. 이 기능은 코드의 구현 세부 사항을 숨기고, 코드에 접근하고 사용할 수 있는 선호 인터페이스를 지정할 수 있게 한다.

개별 타입(클래스, 구조체, 열거형)뿐만 아니라 해당 타입에 속한 프로퍼티, 메서드, 이니셜라이저, 서브스크립트에도 특정 접근 레벨을 할당할 수 있다. 프로토콜은 특정 컨텍스트로 제한할 수 있으며, 전역 상수, 변수, 함수도 마찬가지다.

다양한 수준의 접근 제어를 제공하는 것 외에도, Swift는 일반적인 시나리오에 대한 기본 접근 레벨을 제공하여 명시적 접근 제어 수준을 지정할 필요를 줄인다. 실제로 단일 타겟 앱을 작성하는 경우, 명시적 접근 제어 수준을 전혀 지정하지 않아도 될 수 있다.

> 참고: 접근 제어가 적용될 수 있는 코드의 다양한 측면(프로퍼티, 타입, 함수 등)은 아래 섹션에서 간결하게 "엔티티"라고 부른다.


## 모듈, 소스 파일, 그리고 패키지

Swift의 접근 제어 모델은 모듈, 소스 파일, 그리고 패키지라는 개념을 기반으로 한다.

*모듈*은 코드 배포의 단일 단위로, 프레임워크나 애플리케이션처럼 단일 단위로 빌드되고 배포되며, Swift의 `import` 키워드를 통해 다른 모듈에서 임포트할 수 있다. Xcode에서 각 빌드 타겟(예: 앱 번들 또는 프레임워크)은 Swift에서 별도의 모듈로 취급된다. 만약 앱의 코드 일부를 독립적인 프레임워크로 묶어 여러 애플리케이션에서 재사용하려는 경우, 해당 프레임워크 내에서 정의한 모든 내용은 앱이나 다른 프레임워크에서 임포트되거나 사용될 때 별도의 모듈로 간주된다.

*소스 파일*은 모듈 내의 단일 Swift 소스 코드 파일을 의미한다(즉, 앱이나 프레임워크 내의 단일 파일). 일반적으로 각 타입을 별도의 소스 파일에 정의하지만, 하나의 소스 파일에 여러 타입, 함수 등을 정의할 수도 있다.

*패키지*는 단위로 개발하는 모듈 그룹을 말한다. 패키지를 구성하는 모듈은 Swift 소스 코드가 아닌, 사용 중인 빌드 시스템의 설정 과정에서 정의된다. 예를 들어, Swift Package Manager를 사용하여 코드를 빌드하는 경우, `Package.swift` 파일에서 [PackageDescription][] 모듈의 API를 사용해 패키지를 정의한다. Xcode를 사용하는 경우, 패키지 이름은 Package Access Identifier 빌드 설정에서 지정한다.

[PackageDescription]: https://developer.apple.com/documentation/packagedescription


## 접근 레벨

Swift는 코드 내의 엔티티에 대해 여섯 가지 *접근 레벨*을 제공한다. 이 접근 레벨은 엔티티가 정의된 소스 파일, 해당 소스 파일이 속한 모듈, 그리고 모듈이 속한 패키지와 관련이 있다.

- *Open 접근*과 *Public 접근*은 엔티티가 정의된 모듈 내의 모든 소스 파일에서 사용할 수 있게 한다. 또한 정의된 모듈을 임포트한 다른 모듈의 소스 파일에서도 사용할 수 있다. 일반적으로 프레임워크의 공개 인터페이스를 지정할 때 Open 또는 Public 접근을 사용한다. Open과 Public 접근의 차이점은 아래에서 설명한다.
  
- *Package 접근*은 엔티티가 정의된 패키지 내의 모든 소스 파일에서 사용할 수 있게 한다. 하지만 해당 패키지 외부의 소스 파일에서는 사용할 수 없다. 일반적으로 여러 모듈로 구성된 앱이나 프레임워크 내에서 Package 접근을 사용한다.

- *Internal 접근*은 엔티티가 정의된 모듈 내의 모든 소스 파일에서 사용할 수 있게 한다. 하지만 해당 모듈 외부의 소스 파일에서는 사용할 수 없다. 일반적으로 앱이나 프레임워크의 내부 구조를 정의할 때 Internal 접근을 사용한다.

- *File-private 접근*은 엔티티를 정의한 소스 파일 내에서만 사용할 수 있게 제한한다. 특정 기능의 구현 세부 사항을 전체 파일 내에서 사용할 때 File-private 접근을 사용해 이를 숨길 수 있다.

- *Private 접근*은 엔티티를 선언된 범위 내에서만 사용할 수 있게 제한하며, 동일한 파일 내의 확장에서도 사용할 수 있다. 특정 기능의 구현 세부 사항을 단일 선언 내에서만 사용할 때 Private 접근을 사용해 이를 숨길 수 있다.

Open 접근은 가장 높은(제한이 가장 적은) 접근 레벨이고, Private 접근은 가장 낮은(제한이 가장 많은) 접근 레벨이다.

Open 접근은 클래스와 클래스 멤버에만 적용되며, Public 접근과 달리 모듈 외부의 코드가 해당 클래스를 서브클래싱하고 오버라이드할 수 있게 한다. 이에 대한 자세한 내용은 <doc:AccessControl#Subclassing>에서 다룬다. 클래스를 Open으로 표시하는 것은 다른 모듈의 코드가 해당 클래스를 슈퍼클래스로 사용하는 것에 대한 영향을 고려했으며, 이에 맞게 클래스 코드를 설계했음을 명시적으로 나타낸다.


### 접근 레벨의 기본 원칙

Swift에서 접근 레벨은 다음과 같은 기본 원칙을 따른다:
**더 낮은(더 제한적인) 접근 레벨을 가진 엔티티를 기반으로 엔티티를 정의할 수 없다.**

예를 들어:

- public 변수는 internal, file-private, private 타입으로 정의할 수 없다. public 변수가 사용되는 모든 곳에서 해당 타입이 접근 가능하지 않을 수 있기 때문이다.
- 함수는 매개변수 타입과 반환 타입보다 더 높은 접근 레벨을 가질 수 없다. 함수가 사용되는 상황에서 해당 구성 타입들이 주변 코드에서 접근 불가능할 수 있기 때문이다.

이 기본 원칙이 언어의 다양한 측면에 미치는 구체적인 영향은 아래에서 자세히 다룬다.


### 기본 접근 레벨

코드 내의 모든 엔티티는  
(이 장 후반부에서 설명하는 몇 가지 특정 예외를 제외하고)  
명시적으로 접근 레벨을 지정하지 않으면 기본적으로 internal 접근 레벨을 가진다.  
따라서 대부분의 경우 코드에서 명시적으로 접근 레벨을 지정할 필요가 없다.


### 단일 타겟 앱의 접근 레벨

단순한 단일 타겟 앱을 작성할 때, 앱 내부의 코드는 주로 앱 자체에 포함되어 있으며 앱 모듈 외부에서 접근할 필요가 없다. 기본 접근 레벨인 internal은 이미 이 요구 사항을 충족한다. 따라서 별도로 커스텀 접근 레벨을 지정할 필요가 없다. 그러나 앱 모듈 내부의 다른 코드로부터 구현 세부 사항을 숨기기 위해 일부 코드를 file private 또는 private로 표시할 수도 있다.


### 프레임워크 접근 레벨

프레임워크를 개발할 때는 프레임워크의 공개 인터페이스를 `open` 또는 `public`으로 표시해야 한다. 이렇게 하면 해당 프레임워크를 임포트하는 앱과 같은 다른 모듈에서 이 인터페이스를 확인하고 접근할 수 있다. 이 공개 인터페이스는 프레임워크의 애플리케이션 프로그래밍 인터페이스(API) 역할을 한다.

> 참고: 프레임워크의 내부 구현 세부 사항은 기본 접근 레벨인 `internal`을 그대로 사용하거나, 프레임워크 내부 코드의 다른 부분에서 숨기고 싶다면 `private` 또는 `fileprivate`로 표시할 수 있다. 엔티티를 `open` 또는 `public`으로 표시해야 하는 경우는 해당 엔티티가 프레임워크의 API의 일부가 되어야 할 때뿐이다.


### 유닛 테스트 타겟의 접근 레벨

앱을 개발하면서 유닛 테스트 타겟을 작성할 때, 테스트를 위해 앱의 코드를 해당 모듈에서 사용할 수 있도록 만들어야 한다. 기본적으로 `open` 또는 `public`으로 표시된 엔티티만 다른 모듈에서 접근할 수 있다. 그러나 유닛 테스트 타겟은 `@testable` 속성을 사용해 제품 모듈의 임포트 선언을 표시하고, 테스트가 활성화된 상태로 해당 제품 모듈을 컴파일하면 내부 엔티티에도 접근할 수 있다.


## 접근 제어 구문

엔티티의 접근 레벨을 정의하려면 `open`, `public`, `internal`, `fileprivate`, `private` 중 하나를 엔티티 선언의 시작 부분에 추가한다.

```swift
open class SomeOpenClass {}
public class SomePublicClass {}
internal class SomeInternalClass {}
fileprivate class SomeFilePrivateClass {}
private class SomePrivateClass {}

open var someOpenVariable = 0
public var somePublicVariable = 0
internal let someInternalConstant = 0
fileprivate func someFilePrivateFunction() {}
private func somePrivateFunction() {}
```

<!--
  - test: `accessControlSyntax`

  ```swifttest
  -> open class SomeOpenClass {}
  -> public class SomePublicClass {}
  -> internal class SomeInternalClass {}
  -> fileprivate class SomeFilePrivateClass {}
  -> private class SomePrivateClass {}

  -> open var someOpenVariable = 0
  -> public var somePublicVariable = 0
  -> internal let someInternalConstant = 0
  -> fileprivate func someFilePrivateFunction() {}
  -> private func somePrivateFunction() {}
  ```
-->

명시적으로 지정하지 않으면 기본 접근 레벨은 internal이다. 이는 <doc:AccessControl#기본-접근-수준>에서 설명한 것과 같다. 따라서 `SomeInternalClass`와 `someInternalConstant`는 접근 레벨 수정자를 명시하지 않아도 internal 접근 레벨을 가진다.

```swift
class SomeInternalClass {}              // 암묵적으로 internal
let someInternalConstant = 0            // 암묵적으로 internal
```

<!--
  - test: `accessControlDefaulted`

  ```swifttest
  -> class SomeInternalClass {}              // implicitly internal
  -> let someInternalConstant = 0            // implicitly internal
  ```
-->


## 커스텀 타입의 접근 제어

커스텀 타입에 명시적인 접근 레벨을 지정하려면 타입을 정의할 때 지정한다. 새로운 타입은 접근 레벨이 허용하는 범위 내에서 사용할 수 있다. 예를 들어, 파일 내부 전용 클래스를 정의하면 해당 클래스는 파일 내부 전용 클래스가 정의된 소스 파일 내에서만 프로퍼티 타입이나 함수의 매개변수 또는 반환 타입으로 사용할 수 있다.

타입의 접근 제어 수준은 해당 타입의 멤버(프로퍼티, 메서드, 이니셜라이저, 서브스크립트)의 기본 접근 레벨에도 영향을 미친다. 타입의 접근 레벨을 private 또는 fileprivate로 정의하면 해당 타입의 멤버도 기본적으로 private 또는 fileprivate가 된다. 타입의 접근 레벨을 internal 또는 public으로 정의하거나(또는 접근 레벨을 명시적으로 지정하지 않고 기본 접근 레벨인 internal을 사용하면), 타입의 멤버는 기본적으로 internal 접근 레벨을 갖는다.

> 중요: public 타입의 멤버는 기본적으로 internal 접근 레벨을 갖는다. public 멤버로 만들려면 명시적으로 public으로 표시해야 한다. 이 요구사항은 타입의 공개 API를 명시적으로 선택하여 공개하도록 보장하고, 실수로 타입의 내부 구현을 공개 API로 노출하는 것을 방지한다.

```swift
public class SomePublicClass {                   // 명시적으로 public 클래스
    public var somePublicProperty = 0            // 명시적으로 public 클래스 멤버
    var someInternalProperty = 0                 // 암묵적으로 internal 클래스 멤버
    fileprivate func someFilePrivateMethod() {}  // 명시적으로 파일 내부 전용 클래스 멤버
    private func somePrivateMethod() {}          // 명시적으로 private 클래스 멤버
}

class SomeInternalClass {                        // 암묵적으로 internal 클래스
    var someInternalProperty = 0                 // 암묵적으로 internal 클래스 멤버
    fileprivate func someFilePrivateMethod() {}  // 명시적으로 파일 내부 전용 클래스 멤버
    private func somePrivateMethod() {}          // 명시적으로 private 클래스 멤버
}

fileprivate class SomeFilePrivateClass {         // 명시적으로 파일 내부 전용 클래스
    func someFilePrivateMethod() {}              // 암묵적으로 파일 내부 전용 클래스 멤버
    private func somePrivateMethod() {}          // 명시적으로 private 클래스 멤버
}

private class SomePrivateClass {                 // 명시적으로 private 클래스
    func somePrivateMethod() {}                  // 암묵적으로 private 클래스 멤버
}
```

<!--
  - test: `accessControl, accessControlWrong`

  ```swifttest
  -> public class SomePublicClass {                  // 명시적으로 public 클래스
        public var somePublicProperty = 0            // 명시적으로 public 클래스 멤버
        var someInternalProperty = 0                 // 암묵적으로 internal 클래스 멤버
        fileprivate func someFilePrivateMethod() {}  // 명시적으로 파일 내부 전용 클래스 멤버
        private func somePrivateMethod() {}          // 명시적으로 private 클래스 멤버
     }

  -> class SomeInternalClass {                       // 암묵적으로 internal 클래스
        var someInternalProperty = 0                 // 암묵적으로 internal 클래스 멤버
        fileprivate func someFilePrivateMethod() {}  // 명시적으로 파일 내부 전용 클래스 멤버
        private func somePrivateMethod() {}          // 명시적으로 private 클래스 멤버
     }

  -> fileprivate class SomeFilePrivateClass {        // 명시적으로 파일 내부 전용 클래스
        func someFilePrivateMethod() {}              // 암묵적으로 파일 내부 전용 클래스 멤버
        private func somePrivateMethod() {}          // 명시적으로 private 클래스 멤버
     }

  -> private class SomePrivateClass {                // 명시적으로 private 클래스
        func somePrivateMethod() {}                  // 암묵적으로 private 클래스 멤버
     }
  ```
-->


### 튜플 타입

튜플 타입의 접근 레벨은 해당 튜플을 구성하는 모든 타입 중 가장 제한적인 접근 레벨을 따른다. 예를 들어, 두 개의 서로 다른 타입으로 튜플을 구성할 때, 하나는 internal 접근 레벨이고 다른 하나는 private 접근 레벨이라면, 이 복합 튜플 타입의 접근 레벨은 private이 된다.

<!--
  - test: `tupleTypes_Module1, tupleTypes_Module1_PublicAndInternal, tupleTypes_Module1_Private`

  ```swifttest
  -> public struct PublicStruct {}
  -> internal struct InternalStruct {}
  -> fileprivate struct FilePrivateStruct {}
  -> public func returnPublicTuple() -> (PublicStruct, PublicStruct) {
        return (PublicStruct(), PublicStruct())
     }
  -> func returnInternalTuple() -> (PublicStruct, InternalStruct) {
        return (PublicStruct(), InternalStruct())
     }
  -> fileprivate func returnFilePrivateTuple() -> (PublicStruct, FilePrivateStruct) {
        return (PublicStruct(), FilePrivateStruct())
     }
  ```
-->

<!--
  - test: `tupleTypes_Module1_PublicAndInternal`

  ```swifttest
  // (적어도) internal 멤버를 가진 튜플은 자신의 모듈 내에서 접근 가능
  -> let publicTuple = returnPublicTuple()
  -> let internalTuple = returnInternalTuple()
  ```
-->

<!--
  - test: `tupleTypes_Module1_Private`

  ```swifttest
  // 하나 이상의 private 멤버를 가진 튜플은 소스 파일 외부에서 접근 불가
  -> let privateTuple = returnFilePrivateTuple()
  !$ error: cannot find 'returnFilePrivateTuple' in scope
  !! let privateTuple = returnFilePrivateTuple()
  !!                    ^~~~~~~~~~~~~~~~~~~~~~
  ```
-->

<!--
  - test: `tupleTypes_Module2_Public`

  ```swifttest
  // 모든 멤버가 public인 public 튜플은 다른 모듈에서 사용 가능
  -> import tupleTypes_Module1
  -> let publicTuple = returnPublicTuple()
  ```
-->

<!--
  - test: `tupleTypes_Module2_InternalAndPrivate`

  ```swifttest
  // internal 또는 private 멤버를 가진 튜플은 자신의 모듈 외부에서 사용 불가
  -> import tupleTypes_Module1
  -> let internalTuple = returnInternalTuple()
  -> let privateTuple = returnFilePrivateTuple()
  !$ error: cannot find 'returnInternalTuple' in scope
  !! let internalTuple = returnInternalTuple()
  !!                     ^~~~~~~~~~~~~~~~~~~
  !$ error: cannot find 'returnFilePrivateTuple' in scope
  !! let privateTuple = returnFilePrivateTuple()
  !!                    ^~~~~~~~~~~~~~~~~~~~~~
  ```
-->

> 주의: 튜플 타입은 클래스, 구조체, 열거형, 함수와 같이 독립적인 정의를 가지지 않는다. 튜플 타입의 접근 레벨은 튜플을 구성하는 타입에 따라 자동으로 결정되며, 명시적으로 지정할 수 없다.


### 함수 타입의 접근 레벨

함수 타입의 접근 레벨은 함수의 매개변수 타입과 반환 타입 중 가장 제한적인 접근 레벨으로 결정된다. 함수의 계산된 접근 레벨이 컨텍스트의 기본값과 일치하지 않으면, 함수 정의 시 접근 레벨을 명시적으로 지정해야 한다.

아래 예제는 `someFunction()`이라는 전역 함수를 정의한다. 이 함수 자체에는 특정 접근 레벨 수식어를 제공하지 않았다. 이 함수가 기본 접근 레벨인 "internal"을 가질 것으로 예상할 수 있지만, 실제로는 그렇지 않다. 사실, 아래와 같이 작성하면 `someFunction()`은 컴파일되지 않는다:

```swift
func someFunction() -> (SomeInternalClass, SomePrivateClass) {
    // 함수 구현 부분
}
```

<!--
  - test: `accessControlWrong`

  ```swifttest
  -> func someFunction() -> (SomeInternalClass, SomePrivateClass) {
        // 함수 구현 부분
  >>    return (SomeInternalClass(), SomePrivateClass())
     }
  !! /tmp/swifttest.swift:19:6: error: 함수는 반환 타입이 private 타입을 사용하므로 private 또는 fileprivate로 선언해야 합니다
  !! func someFunction() -> (SomeInternalClass, SomePrivateClass) {
  !! ^
  ```
-->

이 함수의 반환 타입은 앞서 <doc:AccessControl#Custom-Types>에서 정의한 두 커스텀 클래스로 구성된 튜플 타입이다. 이 클래스 중 하나는 internal로 정의되었고, 다른 하나는 private로 정의되었다. 따라서 복합 튜플 타입의 전체 접근 레벨은 private가 된다 (튜플을 구성하는 타입 중 가장 낮은 접근 레벨).

함수의 반환 타입이 private이므로, 함수 선언을 유효하게 만들려면 함수의 전체 접근 레벨을 `private` 수식어로 명시해야 한다:

```swift
private func someFunction() -> (SomeInternalClass, SomePrivateClass) {
    // 함수 구현 부분
}
```

<!--
  - test: `accessControl`

  ```swifttest
  -> private func someFunction() -> (SomeInternalClass, SomePrivateClass) {
        // 함수 구현 부분
  >>    return (SomeInternalClass(), SomePrivateClass())
     }
  ```
-->

`someFunction()`의 정의를 `public` 또는 `internal` 수식어로 표시하거나, 기본 설정인 internal을 사용하는 것은 유효하지 않다. 이는 함수를 사용하는 public 또는 internal 사용자가 함수의 반환 타입에 사용된 private 클래스에 적절한 접근 권한을 가지고 있지 않을 수 있기 때문이다.


### 열거형 타입

열거형의 각 케이스는 자동으로 해당 열거형과 동일한 접근 레벨을 갖는다. 개별 열거형 케이스에 대해 다른 접근 레벨을 지정할 수 없다.

아래 예제에서 `CompassPoint` 열거형은 명시적으로 public 접근 레벨을 갖는다. 따라서 `north`, `south`, `east`, `west` 열거형 케이스도 모두 public 접근 레벨을 갖는다:

```swift
public enum CompassPoint {
    case north
    case south
    case east
    case west
}
```

<!--
  - test: `enumerationCases`

  ```swifttest
  -> public enum CompassPoint {
        case north
        case south
        case east
        case west
     }
  ```
-->

<!--
  - test: `enumerationCases_Module1`

  ```swifttest
  -> public enum CompassPoint {
        case north
        case south
        case east
        case west
     }
  ```
-->

<!--
  - test: `enumerationCases_Module2`

  ```swifttest
  -> import enumerationCases_Module1
  -> let north = CompassPoint.north
  ```
-->


#### Raw 값과 Associated 값

열거형 정의에서 raw 값이나 associated 값에 사용되는 타입은 열거형의 접근 레벨보다 낮을 수 없다. 예를 들어, internal 접근 레벨을 가진 열거형에서 raw 값 타입으로 private 타입을 사용할 수 없다.


### 중첩 타입

중첩 타입의 접근 레벨은 포함하는 타입과 동일하다. 단, 포함하는 타입이 public인 경우는 예외다. public 타입 내부에 정의된 중첩 타입은 자동으로 internal 접근 레벨을 가진다. public 타입 내부의 중첩 타입을 public으로 사용하려면, 명시적으로 public으로 선언해야 한다.

<!--
  - test: `nestedTypes_Module1, nestedTypes_Module1_PublicAndInternal, nestedTypes_Module1_Private`

  ```swifttest
  -> public struct PublicStruct {
        public enum PublicEnumInsidePublicStruct { case a, b }
        internal enum InternalEnumInsidePublicStruct { case a, b }
        private enum PrivateEnumInsidePublicStruct { case a, b }
        enum AutomaticEnumInsidePublicStruct { case a, b }
     }
  -> internal struct InternalStruct {
        internal enum InternalEnumInsideInternalStruct { case a, b }
        private enum PrivateEnumInsideInternalStruct { case a, b }
        enum AutomaticEnumInsideInternalStruct { case a, b }
     }
  -> private struct FilePrivateStruct {
        enum AutomaticEnumInsideFilePrivateStruct { case a, b }
        private enum PrivateEnumInsideFilePrivateStruct { case a, b }
     }
  -> private struct PrivateStruct {
        enum AutomaticEnumInsidePrivateStruct { case a, b }
        private enum PrivateEnumInsidePrivateStruct { case a, b }
     }
  ```
-->

<!--
  - test: `nestedTypes_Module1_PublicAndInternal`

  ```swifttest
  // 동일 모듈 내에서 성공할 것으로 예상되는 테스트
  -> let publicNestedInsidePublic = PublicStruct.PublicEnumInsidePublicStruct.a
  -> let internalNestedInsidePublic = PublicStruct.InternalEnumInsidePublicStruct.a
  -> let automaticNestedInsidePublic = PublicStruct.AutomaticEnumInsidePublicStruct.a

  -> let internalNestedInsideInternal = InternalStruct.InternalEnumInsideInternalStruct.a
  -> let automaticNestedInsideInternal = InternalStruct.AutomaticEnumInsideInternalStruct.a
  ```
-->

<!--
  - test: `nestedTypes_Module1_Private`

  ```swifttest
  // 다른 파일에서 접근할 수 없으므로 실패할 것으로 예상되는 테스트
  -> let privateNestedInsidePublic = PublicStruct.PrivateEnumInsidePublicStruct.a

  -> let privateNestedInsideInternal = InternalStruct.PrivateEnumInsideInternalStruct.a

  -> let privateNestedInsidePrivate = PrivateStruct.PrivateEnumInsidePrivateStruct.a
  -> let automaticNestedInsidePrivate = PrivateStruct.AutomaticEnumInsidePrivateStruct.a

  !$ error: 'PrivateEnumInsidePublicStruct' is inaccessible due to 'private' protection level
  !! let privateNestedInsidePublic = PublicStruct.PrivateEnumInsidePublicStruct.a
  !!                                              ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  !$ note: 'PrivateEnumInsidePublicStruct' declared here
  !! private enum PrivateEnumInsidePublicStruct { case a, b }
  !! ^
  !$ error: 'PrivateEnumInsideInternalStruct' is inaccessible due to 'private' protection level
  !! let privateNestedInsideInternal = InternalStruct.PrivateEnumInsideInternalStruct.a
  !!                                                  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  !$ note: 'PrivateEnumInsideInternalStruct' declared here
  !! private enum PrivateEnumInsideInternalStruct { case a, b }
  !! ^
  !$ error: cannot find 'PrivateStruct' in scope
  !! let privateNestedInsidePrivate = PrivateStruct.PrivateEnumInsidePrivateStruct.a
  !!                                  ^~~~~~~~~~~~~
  !$ error: cannot find 'PrivateStruct' in scope
  !! let automaticNestedInsidePrivate = PrivateStruct.AutomaticEnumInsidePrivateStruct.a
  !!                                    ^~~~~~~~~~~~~
  ```
-->

<!--
  - test: `nestedTypes_Module2_Public`

  ```swifttest
  // 두 번째 모듈 내에서 성공할 것으로 예상되는 테스트
  -> import nestedTypes_Module1
  -> let publicNestedInsidePublic = PublicStruct.PublicEnumInsidePublicStruct.a
  ```
-->

<!--
  - test: `nestedTypes_Module2_InternalAndPrivate`

  ```swifttest
  // 다른 모듈에서 접근할 수 없으므로 실패할 것으로 예상되는 테스트
  -> import nestedTypes_Module1
  -> let internalNestedInsidePublic = PublicStruct.InternalEnumInsidePublicStruct.a
  -> let automaticNestedInsidePublic = PublicStruct.AutomaticEnumInsidePublicStruct.a
  -> let privateNestedInsidePublic = PublicStruct.PrivateEnumInsidePublicStruct.a

  -> let internalNestedInsideInternal = InternalStruct.InternalEnumInsideInternalStruct.a
  -> let automaticNestedInsideInternal = InternalStruct.AutomaticEnumInsideInternalStruct.a
  -> let privateNestedInsideInternal = InternalStruct.PrivateEnumInsideInternalStruct.a

  -> let privateNestedInsidePrivate = PrivateStruct.PrivateEnumInsidePrivateStruct.a
  -> let automaticNestedInsidePrivate = PrivateStruct.AutomaticEnumInsidePrivateStruct.a

  !$ error: 'InternalEnumInsidePublicStruct' is inaccessible due to 'internal' protection level
  !! let internalNestedInsidePublic = PublicStruct.InternalEnumInsidePublicStruct.a
  !!                                               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  !$ note: 'InternalEnumInsidePublicStruct' declared here
  !! internal enum InternalEnumInsidePublicStruct {
  !!               ^
  !$ error: 'AutomaticEnumInsidePublicStruct' is inaccessible due to 'internal' protection level
  !! let automaticNestedInsidePublic = PublicStruct.AutomaticEnumInsidePublicStruct.a
  !!                                                ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  !$ note: 'AutomaticEnumInsidePublicStruct' declared here
  !! internal enum AutomaticEnumInsidePublicStruct {
  !!               ^
  !$ error: 'PrivateEnumInsidePublicStruct' is inaccessible due to 'private' protection level
  !! let privateNestedInsidePublic = PublicStruct.PrivateEnumInsidePublicStruct.a
  !!                                              ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  !$ note: 'PrivateEnumInsidePublicStruct' declared here
  !! private enum PrivateEnumInsidePublicStruct {
  !!              ^
  !$ error: cannot find 'InternalStruct' in scope
  !! let internalNestedInsideInternal = InternalStruct.InternalEnumInsideInternalStruct.a
  !!                                    ^~~~~~~~~~~~~~
  !$ error: cannot find 'InternalStruct' in scope
  !! let automaticNestedInsideInternal = InternalStruct.AutomaticEnumInsideInternalStruct.a
  !!                                     ^~~~~~~~~~~~~~
  !$ error: cannot find 'InternalStruct' in scope
  !! let privateNestedInsideInternal = InternalStruct.PrivateEnumInsideInternalStruct.a
  !!                                   ^~~~~~~~~~~~~~
  !$ error: cannot find 'PrivateStruct' in scope
  !! let privateNestedInsidePrivate = PrivateStruct.PrivateEnumInsidePrivateStruct.a
  !!                                  ^~~~~~~~~~~~~
  !$ error: cannot find 'PrivateStruct' in scope
  !! let automaticNestedInsidePrivate = PrivateStruct.AutomaticEnumInsidePrivateStruct.a
  !!                                    ^~~~~~~~~~~~~
  ```
-->


## 클래스 상속

현재 접근 가능한 범위 내에 있는 클래스와 동일한 모듈에 정의된 클래스를 상속할 수 있다. 또한 다른 모듈에 정의된 open 클래스도 상속할 수 있다. 단, 서브클래스는 슈퍼클래스보다 높은 접근 레벨을 가질 수 없다. 예를 들어, internal 슈퍼클래스의 public 서브클래스를 작성할 수 없다.

추가로, 동일한 모듈에 정의된 클래스의 경우 특정 접근 범위에서 보이는 클래스 멤버(메서드, 프로퍼티, 초기화자, 서브스크립트)를 재정의할 수 있다. 다른 모듈에 정의된 클래스의 경우 open 클래스 멤버를 재정의할 수 있다.

재정의를 통해 상속된 클래스 멤버를 슈퍼클래스 버전보다 더 접근 가능하게 만들 수 있다. 아래 예제에서 클래스 `A`는 `someMethod()`라는 file-private 메서드를 가진 public 클래스다. 클래스 `B`는 `A`의 서브클래스로, 접근 레벨이 "internal"로 제한되어 있다. 그럼에도 불구하고 클래스 `B`는 `someMethod()`를 "internal" 접근 레벨으로 재정의한다. 이는 원래 `someMethod()`의 구현보다 *더 높은* 접근 레벨이다:

```swift
public class A {
    fileprivate func someMethod() {}
}

internal class B: A {
    override internal func someMethod() {}
}
```

<!--
  - test: `subclassingNoCall`

  ```swifttest
  -> public class A {
        fileprivate func someMethod() {}
     }

  -> internal class B: A {
        override internal func someMethod() {}
     }
  ```
-->

서브클래스 멤버가 슈퍼클래스 멤버보다 낮은 접근 권한을 가진 슈퍼클래스 멤버를 호출하는 것도 유효하다. 단, 슈퍼클래스 멤버 호출이 허용된 접근 레벨 범위 내에서 이루어져야 한다(즉, file-private 멤버 호출의 경우 슈퍼클래스와 동일한 소스 파일 내에서, internal 멤버 호출의 경우 슈퍼클래스와 동일한 모듈 내에서):

```swift
public class A {
    fileprivate func someMethod() {}
}

internal class B: A {
    override internal func someMethod() {
        super.someMethod()
    }
}
```

<!--
  - test: `subclassingWithCall`

  ```swifttest
  -> public class A {
        fileprivate func someMethod() {}
     }

  -> internal class B: A {
        override internal func someMethod() {
           super.someMethod()
        }
     }
  ```
-->

슈퍼클래스 `A`와 서브클래스 `B`가 동일한 소스 파일에 정의되어 있기 때문에, `B`의 `someMethod()` 구현에서 `super.someMethod()`를 호출하는 것이 유효하다.


## 상수, 변수, 프로퍼티, 그리고 서브스크립트

상수, 변수, 프로퍼티는 자신의 타입보다 더 공개적일 수 없다. 예를 들어, private 타입을 가진 public 프로퍼티를 작성하는 것은 유효하지 않다. 마찬가지로, 서브스크립트는 자신의 인덱스 타입이나 반환 타입보다 더 공개적일 수 없다.

만약 상수, 변수, 프로퍼티, 또는 서브스크립트가 private 타입을 사용한다면, 해당 상수, 변수, 프로퍼티, 또는 서브스크립트도 반드시 `private`으로 표시해야 한다:

```swift
private var privateInstance = SomePrivateClass()
```

<!--
  - test: `accessControl`

  ```swifttest
  -> private var privateInstance = SomePrivateClass()
  ```
-->

<!--
  - test: `useOfPrivateTypeRequiresPrivateModifier`

  ```swifttest
  -> class Scope {  // 스코프 내에서 private을 의미 있게 사용하기 위해 필요 (fileprivate와 대조)
  -> private class SomePrivateClass {}
  -> let privateConstant = SomePrivateClass()
  !! /tmp/swifttest.swift:3:5: error: 프로퍼티는 'Scope.SomePrivateClass' 타입이 private 타입을 사용하기 때문에 private으로 선언되어야 합니다
  !! let privateConstant = SomePrivateClass()
  !! ^
  -> var privateVariable = SomePrivateClass()
  !! /tmp/swifttest.swift:4:5: error: 프로퍼티는 'Scope.SomePrivateClass' 타입이 private 타입을 사용하기 때문에 private으로 선언되어야 합니다
  !! var privateVariable = SomePrivateClass()
  !! ^
  -> class C {
        var privateProperty = SomePrivateClass()
        subscript(index: Int) -> SomePrivateClass {
           return SomePrivateClass()
        }
     }
  -> }  // 스코프 종료
  !! /tmp/swifttest.swift:6:8: error: 프로퍼티는 'Scope.SomePrivateClass' 타입이 private 타입을 사용하기 때문에 private으로 선언되어야 합니다
  !! var privateProperty = SomePrivateClass()
  !! ^
  !! /tmp/swifttest.swift:7:4: error: 서브스크립트는 요소 타입이 private 타입을 사용하기 때문에 private으로 선언되어야 합니다
  !! subscript(index: Int) -> SomePrivateClass {
  !! ^                        ~~~~~~~~~~~~~~~~
  !! /tmp/swifttest.swift:2:15: note: 타입이 여기에서 선언되었습니다
  !! private class SomePrivateClass {}
  !! ^
  ```
-->


### 게터와 세터

상수, 변수, 프로퍼티, 서브스크립트의 게터와 세터는 해당 상수, 변수, 프로퍼티, 서브스크립트와 동일한 접근 레벨을 자동으로 가진다.

세터의 접근 레벨을 게터보다 낮게 설정하여 변수, 프로퍼티, 서브스크립트의 읽기-쓰기 범위를 제한할 수 있다. 이를 위해 `var` 또는 `subscript` 키워드 앞에 `fileprivate(set)`, `private(set)`, `internal(set)`, `package(set)`를 명시한다.

> 참고: 이 규칙은 저장 프로퍼티와 계산 프로퍼티 모두에 적용된다. 저장 프로퍼티에 명시적으로 게터와 세터를 작성하지 않더라도, Swift는 저장 프로퍼티의 백업 저장소에 접근하기 위해 암시적 게터와 세터를 자동으로 생성한다. 계산 프로퍼티의 명시적 세터와 마찬가지로, `fileprivate(set)`, `private(set)`, `internal(set)`, `package(set)`를 사용해 이 생성된 세터의 접근 레벨을 변경할 수 있다.

아래 예제는 `TrackedString`이라는 구조체를 정의한다. 이 구조체는 문자열 프로퍼티가 수정된 횟수를 추적한다.

```swift
struct TrackedString {
    private(set) var numberOfEdits = 0
    var value: String = "" {
        didSet {
            numberOfEdits += 1
        }
    }
}
```

`TrackedString` 구조체는 `value`라는 저장 문자열 프로퍼티를 정의하며, 초기값은 빈 문자열(`""`)이다. 또한 `numberOfEdits`라는 저장 정수 프로퍼티를 정의하여 `value`가 수정된 횟수를 추적한다. 이 수정 추적은 `value` 프로퍼티에 `didSet` 프로퍼티 옵저버를 사용해 구현되며, `value` 프로퍼티가 새로운 값으로 설정될 때마다 `numberOfEdits`를 증가시킨다.

`TrackedString` 구조체와 `value` 프로퍼티는 명시적인 접근 레벨 수정자를 제공하지 않으므로, 둘 다 기본 접근 레벨인 internal을 가진다. 그러나 `numberOfEdits` 프로퍼티의 접근 레벨은 `private(set)` 수정자로 표시되어, 프로퍼티의 게터는 기본 접근 레벨인 internal을 유지하지만, 프로퍼티는 `TrackedString` 구조체 내부의 코드에서만 설정할 수 있다. 이를 통해 `TrackedString`은 내부적으로 `numberOfEdits` 프로퍼티를 수정할 수 있지만, 구조체 정의 외부에서는 이 프로퍼티를 읽기 전용으로 제공한다.

`TrackedString` 인스턴스를 생성하고 문자열 값을 몇 번 수정하면, `numberOfEdits` 프로퍼티 값이 수정 횟수와 일치하도록 업데이트되는 것을 확인할 수 있다.

```swift
var stringToEdit = TrackedString()
stringToEdit.value = "This string will be tracked."
stringToEdit.value += " This edit will increment numberOfEdits."
stringToEdit.value += " So will this one."
print("The number of edits is \(stringToEdit.numberOfEdits)")
// Prints "The number of edits is 3"
```

다른 소스 파일에서 `numberOfEdits` 프로퍼티의 현재 값을 조회할 수는 있지만, 다른 소스 파일에서 이 프로퍼티를 수정할 수는 없다. 이 제한은 `TrackedString`의 수정 추적 기능 구현 세부 사항을 보호하면서도, 해당 기능의 일부에 편리하게 접근할 수 있도록 한다.

필요한 경우 게터와 세터 모두에 명시적 접근 레벨을 할당할 수 있다. 아래 예제는 `TrackedString` 구조체를 명시적 접근 레벨 public으로 정의한 버전을 보여준다. 구조체의 멤버( `numberOfEdits` 프로퍼티 포함)는 기본적으로 internal 접근 레벨을 가진다. `public`과 `private(set)` 접근 레벨 수정자를 결합하여 구조체의 `numberOfEdits` 프로퍼티 게터를 public으로, 세터를 private으로 설정할 수 있다.

```swift
public struct TrackedString {
    public private(set) var numberOfEdits = 0
    public var value: String = "" {
        didSet {
            numberOfEdits += 1
        }
    }
    public init() {}
}
```


## 초기화 메서드

커스텀 초기화 메서드는 초기화하는 타입의 접근 레벨보다 낮거나 같게 설정할 수 있다. 이 규칙에서 유일한 예외는 필수 초기화 메서드(<doc:Initialization#Required-Initializers>에서 정의)이다. 필수 초기화 메서드는 해당 클래스와 동일한 접근 레벨을 가져야 한다.

함수와 메서드의 매개변수와 마찬가지로, 초기화 메서드의 매개변수 타입은 초기화 메서드 자체의 접근 레벨보다 더 제한적일 수 없다.


### 기본 초기화 메서드

<doc:Initialization#Default-Initializers>에서 설명한 것처럼,
Swift는 모든 프로퍼티에 기본값이 제공되고,
적어도 하나의 초기화 메서드가 정의되지 않은 구조체나 기본 클래스에 대해
인자가 없는 *기본 초기화 메서드*를 자동으로 제공한다.

기본 초기화 메서드는 초기화하는 타입과 동일한 접근 레벨을 가진다.
단, 해당 타입이 `public`으로 정의된 경우는 예외다.
`public`으로 정의된 타입의 기본 초기화 메서드는 내부(internal)로 간주된다.
다른 모듈에서 public 타입을 인자 없는 초기화 메서드로 초기화할 수 있게 하려면,
타입 정의의 일부로 명시적으로 public no-argument 초기화 메서드를 직접 제공해야 한다.


### 구조체 타입의 기본 멤버별 초기화 구문

구조체 타입의 기본 멤버별 초기화 구문은 구조체의 저장 프로퍼티 중 하나라도 private으로 선언된 경우 private으로 간주한다. 마찬가지로, 구조체의 저장 프로퍼티 중 하나라도 file private으로 선언된 경우 초기화 구문도 file private이 된다. 이 외의 경우에는 초기화 구문의 접근 레벨이 internal로 설정된다.

앞서 설명한 기본 초기화 구문과 마찬가지로, public 구조체 타입을 다른 모듈에서 멤버별 초기화 구문으로 초기화할 수 있게 하려면, 타입 정의의 일부로 public 멤버별 초기화 구문을 직접 제공해야 한다.


## 프로토콜

특정 접근 레벨을 프로토콜 타입에 명시적으로 할당하려면, 프로토콜을 정의할 때 설정한다. 이를 통해 특정 접근 컨텍스트 내에서만 채택할 수 있는 프로토콜을 만들 수 있다.

프로토콜 정의 내의 각 요구 사항의 접근 레벨은 자동으로 프로토콜의 접근 레벨과 동일하게 설정된다. 프로토콜 요구 사항을 프로토콜과 다른 접근 레벨으로 설정할 수 없다. 이는 프로토콜을 채택하는 모든 타입에서 프로토콜의 요구 사항이 명확하게 보이도록 보장한다.

<!--
  - test: `protocolRequirementsCannotBeDifferentThanTheProtocol`

  ```swifttest
  -> public protocol PublicProtocol {
        public var publicProperty: Int { get }
        internal var internalProperty: Int { get }
        fileprivate var filePrivateProperty: Int { get }
        private var privateProperty: Int { get }
     }
  !$ error: 'public' modifier cannot be used in protocols
  !! public var publicProperty: Int { get }
  !! ^~~~~~~
  !!-
  !$ note: protocol requirements implicitly have the same access as the protocol itself
  !! public var publicProperty: Int { get }
  !! ^
  !$ error: 'internal' modifier cannot be used in protocols
  !! internal var internalProperty: Int { get }
  !! ^~~~~~~~~
  !!-
  !$ note: protocol requirements implicitly have the same access as the protocol itself
  !! internal var internalProperty: Int { get }
  !! ^
  !$ error: 'fileprivate' modifier cannot be used in protocols
  !! fileprivate var filePrivateProperty: Int { get }
  !! ^~~~~~~~~~~~
  !!-
  !$ note: protocol requirements implicitly have the same access as the protocol itself
  !! fileprivate var filePrivateProperty: Int { get }
  !! ^
  !$ error: 'private' modifier cannot be used in protocols
  !! private var privateProperty: Int { get }
  !! ^~~~~~~~
  !!-
  !$ note: protocol requirements implicitly have the same access as the protocol itself
  !! private var privateProperty: Int { get }
  !! ^
  ```
-->

> 참고: 공개(public) 프로토콜을 정의하면, 해당 프로토콜의 요구 사항은 구현 시 공개 접근 레벨을 필요로 한다. 이는 다른 타입과 달리, 공개 타입 정의가 타입의 멤버에 대해 내부(internal) 접근 레벨을 의미하는 것과는 다르다.

<!--
  - test: `protocols_Module1, protocols_Module1_PublicAndInternal, protocols_Module1_Private`

  ```swifttest
  -> public protocol PublicProtocol {
        var publicProperty: Int { get }
        func publicMethod()
     }
  -> internal protocol InternalProtocol {
        var internalProperty: Int { get }
        func internalMethod()
     }
  -> fileprivate protocol FilePrivateProtocol {
        var filePrivateProperty: Int { get }
        func filePrivateMethod()
     }
  -> private protocol PrivateProtocol {
        var privateProperty: Int { get }
        func privateMethod()
     }
  ```
-->

<!--
  - test: `protocols_Module1_PublicAndInternal`

  ```swifttest
  // 이들은 모두 문제 없이 허용되어야 함
  -> public class PublicClassConformingToPublicProtocol: PublicProtocol {
        public var publicProperty = 0
        public func publicMethod() {}
     }
  -> internal class InternalClassConformingToPublicProtocol: PublicProtocol {
        var publicProperty = 0
        func publicMethod() {}
     }
  -> private class PrivateClassConformingToPublicProtocol: PublicProtocol {
        var publicProperty = 0
        func publicMethod() {}
     }

  -> public class PublicClassConformingToInternalProtocol: InternalProtocol {
        var internalProperty = 0
        func internalMethod() {}
     }
  -> internal class InternalClassConformingToInternalProtocol: InternalProtocol {
        var internalProperty = 0
        func internalMethod() {}
     }
  -> private class PrivateClassConformingToInternalProtocol: InternalProtocol {
        var internalProperty = 0
        func internalMethod() {}
     }
  ```
-->

<!--
  - test: `protocols_Module1_Private`

  ```swifttest
  // 이들은 실패해야 함. FilePrivateProtocol은 파일 외부에서 보이지 않기 때문
  -> public class PublicClassConformingToFilePrivateProtocol: FilePrivateProtocol {
        var filePrivateProperty = 0
        func filePrivateMethod() {}
     }
  !$ error: cannot find type 'FilePrivateProtocol' in scope
  !! public class PublicClassConformingToFilePrivateProtocol: FilePrivateProtocol {
  !! ^~~~~~~~~~~~~~~~~~~

  // 이들은 실패해야 함. PrivateProtocol은 파일 외부에서 보이지 않기 때문
  -> public class PublicClassConformingToPrivateProtocol: PrivateProtocol {
        var privateProperty = 0
        func privateMethod() {}
     }
  !$ error: cannot find type 'PrivateProtocol' in scope
  !! public class PublicClassConformingToPrivateProtocol: PrivateProtocol {
  !! ^~~~~~~~~~~~~~~
  ```
-->

<!--
  - test: `protocols_Module2_Public`

  ```swifttest
  // 이들은 모두 문제 없이 허용되어야 함
  -> import protocols_Module1
  -> public class PublicClassConformingToPublicProtocol: PublicProtocol {
        public var publicProperty = 0
        public func publicMethod() {}
     }
  -> internal class InternalClassConformingToPublicProtocol: PublicProtocol {
        var publicProperty = 0
        func publicMethod() {}
     }
  -> private class PrivateClassConformingToPublicProtocol: PublicProtocol {
        var publicProperty = 0
        func publicMethod() {}
     }
  ```
-->

<!--
  - test: `protocols_Module2_InternalAndPrivate`

  ```swifttest
  // 이들은 모두 실패해야 함. InternalProtocol, FilePrivateProtocol, PrivateProtocol은
  // 다른 모듈에서 보이지 않기 때문
  -> import protocols_Module1
  -> public class PublicClassConformingToInternalProtocol: InternalProtocol {
        var internalProperty = 0
        func internalMethod() {}
     }
  -> public class PublicClassConformingToFilePrivateProtocol: FilePrivateProtocol {
        var filePrivateProperty = 0
        func filePrivateMethod() {}
     }
  -> public class PublicClassConformingToPrivateProtocol: PrivateProtocol {
        var privateProperty = 0
        func privateMethod() {}
     }
  !$ error: cannot find type 'InternalProtocol' in scope
  !! public class PublicClassConformingToInternalProtocol: InternalProtocol {
  !! ^~~~~~~~~~~~~~~~
  !$ error: cannot find type 'FilePrivateProtocol' in scope
  !! public class PublicClassConformingToFilePrivateProtocol: FilePrivateProtocol {
  !! ^~~~~~~~~~~~~~~~~~~
  !$ error: cannot find type 'PrivateProtocol' in scope
  !! public class PublicClassConformingToPrivateProtocol: PrivateProtocol {
  !! ^~~~~~~~~~~~~~~
  ```
-->


### 프로토콜 상속

기존 프로토콜을 상속받아 새로운 프로토콜을 정의할 때, 새 프로토콜은 상속받은 프로토콜과 동일하거나 더 낮은 접근 레벨을 가져야 한다. 예를 들어, 내부(internal) 프로토콜을 상속받아 공개(public) 프로토콜을 정의할 수 없다.


### 프로토콜 준수성

타입은 자신보다 낮은 접근 레벨의 프로토콜을 준수할 수 있다. 예를 들어, 다른 모듈에서 사용할 수 있는 public 타입을 정의하면서, 해당 타입이 internal 프로토콜을 준수하도록 설정할 수 있다. 이 경우, 프로토콜 준수성은 internal 프로토콜을 정의한 모듈 내에서만 사용 가능하다.

특정 프로토콜에 대한 타입의 준수성은 타입의 접근 레벨과 프로토콜의 접근 레벨 중 더 낮은 수준으로 결정된다. 예를 들어, 타입이 public이고 준수하는 프로토콜이 internal이라면, 해당 프로토콜에 대한 타입의 준수성도 internal이 된다.

타입을 작성하거나 확장하여 프로토콜을 준수하도록 할 때, 각 프로토콜 요구사항을 구현한 부분은 해당 프로토콜에 대한 타입의 준수성과 동일하거나 더 높은 접근 레벨을 가져야 한다. 예를 들어, public 타입이 internal 프로토콜을 준수한다면, 각 프로토콜 요구사항을 구현한 부분도 최소한 internal 접근 레벨을 유지해야 한다.

> 참고: Swift에서는 Objective-C와 마찬가지로 프로토콜 준수성은 전역적이다. 즉, 동일한 프로그램 내에서 타입이 한 프로토콜을 두 가지 다른 방식으로 준수하는 것은 불가능하다.


## 확장

클래스, 구조체, 열거형은 해당 타입이 접근 가능한 모든 컨텍스트에서 확장할 수 있다. 확장에서 추가한 멤버는 원본 타입에서 선언한 멤버와 동일한 기본 접근 레벨을 가진다. public이나 internal 타입을 확장하면, 추가한 새로운 멤버의 기본 접근 레벨은 internal이 된다. file-private 타입을 확장하면, 새로운 멤버의 기본 접근 레벨은 file private이 된다. private 타입을 확장하면, 새로운 멤버의 기본 접근 레벨은 private이 된다.

또한, 확장에 명시적 접근 레벨 수정자(예: `private`)를 붙여 확장 내에서 정의된 모든 멤버의 기본 접근 레벨을 새로 설정할 수 있다. 이 새로운 기본값은 확장 내에서 개별 멤버에 대해 재정의할 수 있다.

프로토콜 준수를 추가하기 위해 확장을 사용하는 경우, 확장에 명시적 접근 레벨 수정자를 제공할 수 없다. 대신, 프로토콜 자체의 접근 레벨이 확장 내의 각 프로토콜 요구 사항 구현에 대한 기본 접근 레벨으로 사용된다.

<!--
  - test: `extensions_Module1, extensions_Module1_PublicAndInternal, extensions_Module1_Private`

  ```swifttest
  -> public struct PublicStruct {
        public init() {}
        func implicitlyInternalMethodFromStruct() -> Int { return 0 }
     }
  -> extension PublicStruct {
        func implicitlyInternalMethodFromExtension() -> Int { return 0 }
     }
  -> fileprivate extension PublicStruct {
        func filePrivateMethod() -> Int { return 0 }
     }
  -> var publicStructInSameFile = PublicStruct()
  -> let sameFileA = publicStructInSameFile.implicitlyInternalMethodFromStruct()
  -> let sameFileB = publicStructInSameFile.implicitlyInternalMethodFromExtension()
  -> let sameFileC = publicStructInSameFile.filePrivateMethod()
  ```
-->

<!--
  - test: `extensions_Module1_PublicAndInternal`

  ```swifttest
  -> var publicStructInDifferentFile = PublicStruct()
  -> let differentFileA = publicStructInDifferentFile.implicitlyInternalMethodFromStruct()
  -> let differentFileB = publicStructInDifferentFile.implicitlyInternalMethodFromExtension()
  ```
-->

<!--
  - test: `extensions_Module1_Private`

  ```swifttest
  -> var publicStructInDifferentFile = PublicStruct()
  -> let differentFileC = publicStructInDifferentFile.filePrivateMethod()
  !$ error: 'filePrivateMethod' is inaccessible due to 'fileprivate' protection level
  !! let differentFileC = publicStructInDifferentFile.filePrivateMethod()
  !!                                                  ^~~~~~~~~~~~~~~~~
  !$ note: 'filePrivateMethod()' declared here
  !! func filePrivateMethod() -> Int { return 0 }
  !! ^
  ```
-->

<!--
  - test: `extensions_Module2`

  ```swifttest
  -> import extensions_Module1
  -> var publicStructInDifferentModule = PublicStruct()
  -> let differentModuleA = publicStructInDifferentModule.implicitlyInternalMethodFromStruct()
  !$ error: 'implicitlyInternalMethodFromStruct' is inaccessible due to 'internal' protection level
  !! let differentModuleA = publicStructInDifferentModule.implicitlyInternalMethodFromStruct()
  !!                                                      ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  !$ note: 'implicitlyInternalMethodFromStruct()' declared here
  !! internal func implicitlyInternalMethodFromStruct() -> Int
  !!               ^
  -> let differentModuleB = publicStructInDifferentModule.implicitlyInternalMethodFromExtension()
  !$ error: 'implicitlyInternalMethodFromExtension' is inaccessible due to 'internal' protection level
  !! let differentModuleB = publicStructInDifferentModule.implicitlyInternalMethodFromExtension()
  !!                                                      ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  !$ note: 'implicitlyInternalMethodFromExtension()' declared here
  !! internal func implicitlyInternalMethodFromExtension() -> Int
  !!               ^
  -> let differentModuleC = publicStructInDifferentModule.filePrivateMethod()
  !$ error: 'filePrivateMethod' is inaccessible due to 'fileprivate' protection level
  !! let differentModuleC = publicStructInDifferentModule.filePrivateMethod()
  !!                                                      ^~~~~~~~~~~~~~~~~
  !$ note: 'filePrivateMethod()' declared here
  !! fileprivate func filePrivateMethod() -> Int
  !!                  ^
  ```
-->


### 확장에서의 private 멤버 사용

확장(extension)은 클래스, 구조체, 열거형과 같은 타입을 확장하는 기능을 제공한다. 만약 확장이 원본 타입과 같은 파일에 위치한다면, 확장 내부의 코드는 원본 타입 선언의 일부로 간주된다. 이로 인해 다음과 같은 동작이 가능하다:

- 원본 타입 선언에서 private 멤버를 선언하고, 같은 파일 내의 확장에서 해당 멤버에 접근할 수 있다.
- 하나의 확장에서 private 멤버를 선언하고, 같은 파일 내의 다른 확장에서 해당 멤버에 접근할 수 있다.
- 확장에서 private 멤버를 선언하고, 같은 파일 내의 원본 타입 선언에서 해당 멤버에 접근할 수 있다.

이러한 동작은 private 멤버의 존재 여부와 상관없이 확장을 사용해 코드를 조직화할 수 있음을 의미한다. 예를 들어, 다음과 같은 간단한 프로토콜이 있다고 가정해 보자:

```swift
protocol SomeProtocol {
    func doSomething()
}
```

<!--
  - test: `extensions_privatemembers`

  ```swifttest
  -> protocol SomeProtocol {
         func doSomething()
     }
  ```
-->

이 프로토콜을 준수하는 기능을 확장을 통해 추가할 수 있다. 다음은 그 예시이다:

```swift
struct SomeStruct {
    private var privateVariable = 12
}

extension SomeStruct: SomeProtocol {
    func doSomething() {
        print(privateVariable)
    }
}
```

<!--
  - test: `extensions_privatemembers`

  ```swifttest
  -> struct SomeStruct {
         private var privateVariable = 12
     }

  -> extension SomeStruct: SomeProtocol {
         func doSomething() {
             print(privateVariable)
         }
     }
  >> let s = SomeStruct()
  >> s.doSomething()
  << 12
  ```
-->


## 제네릭

제네릭 타입이나 제네릭 함수의 접근 레벨은 해당 제네릭 타입 또는 함수 자체의 접근 레벨과 타입 매개변수에 적용된 타입 제약 조건의 접근 레벨 중 더 낮은 값으로 결정된다.


## 타입 별칭

타입 별칭을 정의하면 접근 제어 목적에서 별개의 타입으로 간주한다. 타입 별칭은 원본 타입의 접근 레벨보다 낮거나 같은 수준을 가져야 한다. 예를 들어, private 타입 별칭은 private, file-private, internal, public, open 타입을 별칭으로 가질 수 있지만, public 타입 별칭은 internal, file-private, private 타입을 별칭으로 가질 수 없다.

> 참고: 이 규칙은 프로토콜 준수를 위해 사용되는 연관 타입의 타입 별칭에도 동일하게 적용된다.

<!--
  - test: `typeAliases`

  ```swifttest
  -> public struct PublicStruct {}
  -> internal struct InternalStruct {}
  -> private struct PrivateStruct {}

  -> public typealias PublicAliasOfPublicType = PublicStruct
  -> internal typealias InternalAliasOfPublicType = PublicStruct
  -> private typealias PrivateAliasOfPublicType = PublicStruct

  -> public typealias PublicAliasOfInternalType = InternalStruct     // 허용되지 않음
  -> internal typealias InternalAliasOfInternalType = InternalStruct
  -> private typealias PrivateAliasOfInternalType = InternalStruct

  -> public typealias PublicAliasOfPrivateType = PrivateStruct       // 허용되지 않음
  -> internal typealias InternalAliasOfPrivateType = PrivateStruct   // 허용되지 않음
  -> private typealias PrivateAliasOfPrivateType = PrivateStruct

  !$ error: 타입 별칭을 public으로 선언할 수 없음. 내부 타입을 사용하기 때문
  !! public typealias PublicAliasOfInternalType = InternalStruct     // 허용되지 않음
  !! ^                           ~~~~~~~~~~~~~~
  !$ note: 타입이 여기에서 선언됨
  !! internal struct InternalStruct {}
  !! ^
  !$ error: 타입 별칭을 public으로 선언할 수 없음. private 타입을 사용하기 때문
  !! public typealias PublicAliasOfPrivateType = PrivateStruct       // 허용되지 않음
  !! ^                          ~~~~~~~~~~~~~
  !$ note: 타입이 여기에서 선언됨
  !! private struct PrivateStruct {}
  !! ^
  !$ error: 타입 별칭을 internal으로 선언할 수 없음. private 타입을 사용하기 때문
  !! internal typealias InternalAliasOfPrivateType = PrivateStruct   // 허용되지 않음
  !! ^                            ~~~~~~~~~~~~~
  !$ note: 타입이 여기에서 선언됨
  !! private struct PrivateStruct {}
  !! ^
  ```
-->

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


