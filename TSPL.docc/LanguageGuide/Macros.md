# 매크로

컴파일 시점에 코드를 생성하기 위해 매크로를 사용한다. 매크로는 컴파일할 때 소스 코드를 변환하므로, 반복적인 코드를 직접 작성하지 않아도 된다. 컴파일 과정에서 Swift는 일반적인 코드 빌드 전에 매크로를 확장한다.

![매크로 확장 과정을 보여주는 다이어그램. 왼쪽에는 Swift 코드를 스타일화한 표현이 있고, 오른쪽에는 매크로가 추가한 여러 줄이 포함된 동일한 코드가 있다.](macro-expansion)

매크로를 확장하는 작업은 항상 추가적인 작업이다. 매크로는 새로운 코드를 추가하지만, 기존 코드를 삭제하거나 수정하지 않는다.

매크로에 입력되는 값과 매크로 확장의 결과물은 모두 Swift 코드로 문법적으로 유효한지 확인한다. 마찬가지로, 매크로에 전달하는 값과 매크로가 생성한 코드의 값도 올바른 타입을 가지고 있는지 검사한다. 또한, 매크로 구현에서 확장 중 오류가 발생하면 컴파일러는 이를 컴파일 오류로 처리한다. 이러한 보장 덕분에 매크로를 사용한 코드를 더 쉽게 이해할 수 있고, 매크로를 잘못 사용하거나 매크로 구현에 버그가 있는 문제도 더 쉽게 발견할 수 있다.

Swift에는 두 가지 종류의 매크로가 있다:

- **독립형 매크로**는 선언에 연결되지 않고 단독으로 나타난다.
- **부착형 매크로**는 연결된 선언을 수정한다.

독립형 매크로와 부착형 매크로를 호출하는 방식은 약간 다르지만, 둘 다 동일한 매크로 확장 모델을 따르며 동일한 방식으로 구현한다. 다음 섹션에서 두 종류의 매크로를 더 자세히 설명한다.


## 독립형 매크로

독립형 매크로를 호출하려면, 매크로 이름 앞에 숫자 기호(`#`)를 붙이고, 이름 뒤에 괄호 안에 인자를 전달한다. 예를 들어:

```swift
func myFunction() {
    print("Currently running \(#function)")
    #warning("Something's wrong")
}
```

첫 번째 줄에서 `#function`은 Swift 표준 라이브러리의 [`function()`][] 매크로를 호출한다. 코드를 컴파일할 때 Swift는 이 매크로의 구현을 호출하여 `#function`을 현재 함수의 이름으로 대체한다. 이 코드를 실행하고 `myFunction()`을 호출하면 "Currently running myFunction()"이 출력된다. 두 번째 줄에서 `#warning`은 Swift 표준 라이브러리의 [`warning(_:)`][] 매크로를 호출하여 커스텀 컴파일 타임 경고를 생성한다.

[`function()`]: https://developer.apple.com/documentation/swift/function()
[`warning(_:)`]: https://developer.apple.com/documentation/swift/warning(_:)

독립형 매크로는 `#function`처럼 값을 생성할 수도 있고, `#warning`처럼 컴파일 타임에 특정 동작을 수행할 수도 있다.


## 부착형 매크로

부착형 매크로를 호출하려면, 매크로 이름 앞에 `@` 기호를 붙이고, 이름 뒤에 괄호를 사용해 인자를 전달한다. 부착형 매크로는 해당 선언을 수정하며, 새로운 메서드를 정의하거나 프로토콜을 준수하도록 코드를 추가한다.

예를 들어, 매크로를 사용하지 않은 다음 코드를 살펴보자:

```swift
struct SundaeToppings: OptionSet {
    let rawValue: Int
    static let nuts = SundaeToppings(rawValue: 1 << 0)
    static let cherry = SundaeToppings(rawValue: 1 << 1)
    static let fudge = SundaeToppings(rawValue: 1 << 2)
}
```

이 코드에서 `SundaeToppings` 옵션 세트의 각 옵션은 초기화자를 호출하는데, 이는 반복적이고 수동적인 작업이다. 새로운 옵션을 추가할 때 실수를 하기 쉽다. 예를 들어, 줄 끝에 잘못된 숫자를 입력할 수 있다.

다음은 매크로를 사용한 버전이다:

```swift
@OptionSet<Int>
struct SundaeToppings {
    private enum Options: Int {
        case nuts
        case cherry
        case fudge
    }
}
```

이 버전의 `SundaeToppings`는 `@OptionSet` 매크로를 호출한다. 이 매크로는 private 열거형의 케이스 목록을 읽고, 각 옵션에 대한 상수 목록을 생성하며, [`OptionSet`][] 프로토콜을 준수하도록 코드를 추가한다.

[`OptionSet`]: https://developer.apple.com/documentation/swift/optionset

<!--
@OptionSet 매크로가 도착하면, 두 링크를 다시 변경한다:

[`@OptionSet`]: https://developer.apple.com/documentation/swift/optionset-swift.macro
[`OptionSet`]: https://developer.apple.com/documentation/swift/optionset-swift.protocol
-->

비교를 위해, `@OptionSet` 매크로가 확장된 버전을 살펴보자. 이 코드를 직접 작성하지는 않으며, Swift에 매크로 확장을 명시적으로 요청한 경우에만 볼 수 있다.

```swift
struct SundaeToppings {
    private enum Options: Int {
        case nuts
        case cherry
        case fudge
    }

    typealias RawValue = Int
    var rawValue: RawValue
    init() { self.rawValue = 0 }
    init(rawValue: RawValue) { self.rawValue = rawValue }
    static let nuts: Self = Self(rawValue: 1 << Options.nuts.rawValue)
    static let cherry: Self = Self(rawValue: 1 << Options.cherry.rawValue)
    static let fudge: Self = Self(rawValue: 1 << Options.fudge.rawValue)
}
extension SundaeToppings: OptionSet { }
```

private 열거형 이후의 모든 코드는 `@OptionSet` 매크로에서 생성된다. 매크로를 사용해 모든 정적 변수를 생성하는 `SundaeToppings` 버전은 이전의 수동으로 작성된 버전보다 읽기 쉽고 유지보수하기 편리하다.


## 매크로 선언

대부분의 Swift 코드에서는 함수나 타입과 같은 심볼을 구현할 때 별도의 선언이 필요하지 않다. 하지만 매크로의 경우 선언과 구현이 분리되어 있다. 매크로 선언에는 매크로의 이름, 매개변수, 사용 가능한 위치, 생성하는 코드의 종류 등이 포함된다. 매크로 구현에는 Swift 코드를 생성해 매크로를 확장하는 코드가 들어 있다.

`macro` 키워드를 사용해 매크로를 선언한다. 예를 들어, 앞서 예제에서 사용한 `@OptionSet` 매크로의 선언 일부는 다음과 같다:

```swift
public macro OptionSet<RawType>() =
        #externalMacro(module: "SwiftMacros", type: "OptionSetMacro")
```

첫 번째 줄은 매크로의 이름과 인자를 지정한다. 여기서 이름은 `OptionSet`이고, 인자는 없다. 두 번째 줄은 Swift 표준 라이브러리의 [`externalMacro(module:type:)`][] 매크로를 사용해 매크로 구현의 위치를 알려준다. 이 경우 `SwiftMacros` 모듈에 `OptionSetMacro`라는 타입이 있고, 이 타입이 `@OptionSet` 매크로를 구현한다.

[`externalMacro(module:type:)`]: https://developer.apple.com/documentation/swift/externalmacro(module:type:)

`OptionSet`은 부착형 매크로이므로, 구조체와 클래스 이름처럼 대문자 카멜 케이스를 사용한다. 독립형 매크로는 변수와 함수 이름처럼 소문자 카멜 케이스를 사용한다.

> 참고:
> 매크로는 항상 `public`으로 선언한다. 매크로를 선언하는 코드와 매크로를 사용하는 코드가 다른 모듈에 있기 때문에, 비공개 매크로를 적용할 수 있는 곳이 없다.

매크로 선언은 매크로의 *역할*을 정의한다. 즉, 소스 코드에서 매크로를 호출할 수 있는 위치와 매크로가 생성할 수 있는 코드의 종류를 지정한다. 모든 매크로는 하나 이상의 역할을 가지며, 이는 매크로 선언의 시작 부분에 속성으로 작성된다. 다음은 `@OptionSet` 매크로의 역할 속성을 포함한 선언의 일부다:

```swift
@attached(member)
@attached(extension, conformances: OptionSet)
public macro OptionSet<RawType>() =
        #externalMacro(module: "SwiftMacros", type: "OptionSetMacro")
```

이 선언에서 `@attached` 속성은 두 번 사용된다. 첫 번째 사용인 `@attached(member)`는 매크로가 적용된 타입에 새로운 멤버를 추가한다는 것을 나타낸다. `@OptionSet` 매크로는 `OptionSet` 프로토콜에 필요한 `init(rawValue:)` 초기화 구문과 몇 가지 추가 멤버를 생성한다. 두 번째 사용인 `@attached(extension, conformances: OptionSet)`는 `@OptionSet` 매크로가 `OptionSet` 프로토콜을 준수하도록 확장한다는 것을 알려준다.

독립형 매크로의 경우 `@freestanding` 속성을 사용해 역할을 지정한다:

```swift
@freestanding(expression)
public macro line<T: ExpressibleByIntegerLiteral>() -> T =
        /* ... 매크로 구현 위치... */
```

위의 `#line` 매크로는 `expression` 역할을 가진다. 표현식 매크로는 값을 생성하거나, 컴파일 타임에 경고를 생성하는 등의 작업을 수행한다.

매크로의 역할 외에도, 매크로 선언은 매크로가 생성하는 심볼의 이름에 대한 정보를 제공한다. 매크로 선언이 이름 목록을 제공하면, 해당 이름을 사용하는 선언만 생성한다는 것이 보장된다. 이는 생성된 코드를 이해하고 디버깅하는 데 도움이 된다. 다음은 `@OptionSet` 매크로의 전체 선언이다:

```swift
@attached(member, names: named(RawValue), named(rawValue),
        named(`init`), arbitrary)
@attached(extension, conformances: OptionSet)
public macro OptionSet<RawType>() =
        #externalMacro(module: "SwiftMacros", type: "OptionSetMacro")
```

위의 선언에서 `@attached(member)` 매크로는 `names:` 레이블 뒤에 `@OptionSet` 매크로가 생성하는 각 심볼의 이름을 나열한다. 매크로는 `RawValue`, `rawValue`, `init`이라는 이름의 선언을 추가하며, 이러한 이름은 미리 알려져 있으므로 매크로 선언에서 명시적으로 나열한다.

매크로 선언은 이름 목록 뒤에 `arbitrary`를 포함해, 매크로를 사용할 때까지 알 수 없는 이름의 선언도 생성할 수 있도록 한다. 예를 들어, 위의 `SundaeToppings`에 `@OptionSet` 매크로를 적용하면 열거형 케이스에 해당하는 타입 프로퍼티인 `nuts`, `cherry`, `fudge`를 생성한다.

더 자세한 정보와 매크로 역할의 전체 목록은 <doc:Attributes#attached>와 <doc:Attributes#freestanding>를 참고한다.


## 매크로 확장

Swift 코드에서 매크로를 사용할 때, 컴파일러는 매크로의 구현을 호출해 이를 확장한다.

![매크로 확장의 네 단계를 보여주는 다이어그램. 입력은 Swift 소스 코드이며, 이는 코드의 구조를 나타내는 트리로 변환된다. 매크로 구현이 트리에 새로운 가지를 추가하고, 결과적으로 추가 코드가 포함된 Swift 소스 코드가 생성된다.](macro-expansion-full)

구체적으로, Swift는 다음과 같은 방식으로 매크로를 확장한다:

1. 컴파일러가 코드를 읽고, 문법의 메모리 내 표현을 생성한다.

1. 컴파일러가 메모리 내 표현의 일부를 매크로 구현으로 전달하고, 매크로를 확장한다.

1. 컴파일러가 매크로 호출을 확장된 형태로 대체한다.

1. 컴파일러가 확장된 소스 코드를 사용해 컴파일을 계속 진행한다.

구체적인 단계를 살펴보기 위해 다음 예제를 고려해 보자:

```swift
let magicNumber = #fourCharacterCode("ABCD")
```

`#fourCharacterCode` 매크로는 4글자 길이의 문자열을 받아, 문자열의 ASCII 값을 연결한 부호 없는 32비트 정수를 반환한다. 일부 파일 형식은 디버거에서 읽을 수 있으면서도 간결한 이런 정수를 데이터 식별자로 사용한다. 아래의 <doc:Macros#Implementing-a-Macro> 섹션에서 이 매크로를 구현하는 방법을 설명한다.

위 코드의 매크로를 확장하기 위해, 컴파일러는 Swift 파일을 읽고 *추상 구문 트리*(Abstract Syntax Tree, AST)라는 메모리 내 표현을 생성한다. AST는 코드의 구조를 명시적으로 표현하므로, 컴파일러나 매크로 구현과 같은 코드와 상호작용하는 프로그램을 작성하기 쉽게 만든다. 위 코드의 AST를 간단히 표현하면 다음과 같다:

![루트 엘리먼트로 상수를 포함한 트리 다이어그램. 상수는 이름(magicNumber)과 값을 가진다. 상수의 값은 매크로 호출이다. 매크로 호출은 이름(fourCharacterCode)과 인자를 가진다. 인자는 문자열 리터럴 "ABCD"이다.](macro-ast-original)

위 다이어그램은 이 코드의 구조가 메모리에서 어떻게 표현되는지 보여준다. AST의 각 엘리먼트는 소스 코드의 일부에 해당한다. "상수 선언" AST 엘리먼트는 두 개의 자식 엘리먼트를 가지며, 이는 상수 선언의 두 부분(이름과 값)을 나타낸다. "매크로 호출" 엘리먼트는 매크로의 이름과 매크로에 전달된 인자 목록을 나타내는 자식 엘리먼트를 가진다.

이 AST를 구성하는 과정에서, 컴파일러는 소스 코드가 유효한 Swift 코드인지 확인한다. 예를 들어, `#fourCharacterCode`는 단일 인자를 받으며, 이 인자는 문자열이어야 한다. 정수 인자를 전달하거나 문자열 리터럴의 끝에 따옴표(`"`)를 빠뜨리면 이 시점에서 오류가 발생한다.

컴파일러는 코드에서 매크로를 호출하는 부분을 찾고, 해당 매크로를 구현하는 외부 바이너리를 로드한다. 각 매크로 호출에 대해, 컴파일러는 AST의 일부를 매크로 구현으로 전달한다. 다음은 그 부분 AST를 나타낸다:

![루트 엘리먼트로 매크로 호출을 포함한 트리 다이어그램. 매크로 호출은 이름(fourCharacterCode)과 인자를 가진다. 인자는 문자열 리터럴 "ABCD"이다.](macro-ast-input)

`#fourCharacterCode` 매크로의 구현은 매크로를 확장할 때 이 부분 AST를 입력으로 읽는다. 매크로 구현은 입력으로 받은 부분 AST에만 작동하므로, 매크로는 항상 동일한 방식으로 확장된다. 이 제한은 매크로 확장을 이해하기 쉽게 만들고, 변경되지 않은 매크로를 확장하지 않음으로써 코드 빌드 속도를 높이는 데 도움이 된다.

Swift는 매크로 구현 코드를 제한함으로써, 매크로 작성자가 실수로 다른 입력을 읽지 않도록 돕는다:

- 매크로 구현으로 전달되는 AST는 매크로를 나타내는 AST 엘리먼트만 포함하며, 그 앞뒤의 코드는 포함하지 않는다.

- 매크로 구현은 파일 시스템이나 네트워크에 접근할 수 없는 샌드박스 환경에서 실행된다.

이러한 안전장치 외에도, 매크로 작성자는 매크로 입력 외부의 어떤 것도 읽거나 수정하지 않도록 책임져야 한다. 예를 들어, 매크로 확장은 현재 시간에 의존해서는 안 된다.

`#fourCharacterCode`의 구현은 확장된 코드를 포함하는 새로운 AST를 생성한다. 다음은 컴파일러로 반환되는 코드이다:

![UInt32 타입의 정수 리터럴 1145258561을 포함한 트리 다이어그램.](macro-ast-output)

컴파일러가 이 확장을 받으면, 매크로 호출을 포함하는 AST 엘리먼트를 매크로 확장을 포함하는 엘리먼트로 대체한다. 매크로 확장 후, 컴파일러는 프로그램이 여전히 문법적으로 유효한 Swift 코드인지, 모든 타입이 올바른지 다시 확인한다. 그 결과 일반적으로 컴파일할 수 있는 최종 AST가 생성된다:

![루트 엘리먼트로 상수를 포함한 트리 다이어그램. 상수는 이름(magicNumber)과 값을 가진다. 상수의 값은 UInt32 타입의 정수 리터럴 1145258561이다.](macro-ast-result)

이 AST는 다음과 같은 Swift 코드에 해당한다:

```swift
let magicNumber = 1145258561 as UInt32
```

이 예제에서는 입력 소스 코드에 하나의 매크로만 있지만, 실제 프로그램에는 동일한 매크로의 여러 인스턴스와 다른 매크로에 대한 여러 호출이 있을 수 있다. 컴파일러는 매크로를 하나씩 확장한다.

한 매크로가 다른 매크로 안에 나타나면, 외부 매크로가 먼저 확장된다. 이렇게 하면 외부 매크로가 내부 매크로를 확장하기 전에 수정할 수 있다.


## 매크로 구현하기

매크로를 구현하려면 두 가지 컴포넌트를 만들어야 한다:
매크로 확장을 수행하는 타입과,
매크로를 API로 노출시키는 라이브러리다.
이 두 부분은 매크로를 사용하는 코드와 별도로 빌드된다.
매크로와 이를 사용하는 클라이언트를 함께 개발하더라도,
매크로 구현은 클라이언트 빌드 과정의 일부로 실행되기 때문이다.

Swift Package Manager를 사용해 새로운 매크로를 생성하려면,
`swift package init --type macro` 명령어를 실행한다.
이 명령어는 매크로 구현과 선언을 위한 템플릿을 포함한 여러 파일을 생성한다.

기존 프로젝트에 매크로를 추가하려면,
`Package.swift` 파일의 시작 부분을 다음과 같이 수정한다:

- `swift-tools-version` 주석에서 Swift 도구 버전을 5.9 이상으로 설정한다.
- `CompilerPluginSupport` 모듈을 임포트한다.
- `platforms` 목록에 macOS 10.15 이상을 최소 배포 대상으로 포함한다.

아래 코드는 예시 `Package.swift` 파일의 시작 부분을 보여준다.

```swift
// swift-tools-version: 5.9

import PackageDescription
import CompilerPluginSupport

let package = Package(
    name: "MyPackage",
    platforms: [ .iOS(.v17), .macOS(.v13)],
    // ...
)
```

다음으로, 매크로 구현을 위한 타겟과 매크로 라이브러리를 위한 타겟을
기존 `Package.swift` 파일에 추가한다.
예를 들어, 프로젝트 이름에 맞게 변경하여 다음과 같이 추가할 수 있다:

```swift
targets: [
    // 소스 변환을 수행하는 매크로 구현.
    .macro(
        name: "MyProjectMacros",
        dependencies: [
            .product(name: "SwiftSyntaxMacros", package: "swift-syntax"),
            .product(name: "SwiftCompilerPlugin", package: "swift-syntax")
        ]
    ),

    // 매크로를 API의 일부로 노출하는 라이브러리.
    .target(name: "MyProject", dependencies: ["MyProjectMacros"]),
]
```

위 코드는 두 가지 타겟을 정의한다:
`MyProjectMacros`는 매크로의 구현을 포함하고,
`MyProject`는 이 매크로를 사용할 수 있게 한다.

매크로의 구현은 [SwiftSyntax][] 모듈을 사용해
Swift 코드와 구조적으로 상호작용하며, AST를 활용한다.
Swift Package Manager로 새로운 매크로 패키지를 생성했다면,
생성된 `Package.swift` 파일은 자동으로 SwiftSyntax에 대한 의존성을 포함한다.
기존 프로젝트에 매크로를 추가하는 경우,
`Package.swift` 파일에 SwiftSyntax 의존성을 추가한다:

[SwiftSyntax]: https://github.com/swiftlang/swift-syntax

```swift
dependencies: [
    .package(url: "https://github.com/swiftlang/swift-syntax", from: "509.0.0")
],
```

매크로의 역할에 따라,
SwiftSyntax에서 제공하는 해당 프로토콜에 매크로 구현이 준수해야 한다.
예를 들어, 이전 섹션의 `#fourCharacterCode`를 고려해보자.
이 매크로를 구현하는 구조체는 다음과 같다:

```swift
import SwiftSyntax
import SwiftSyntaxMacros

public struct FourCharacterCode: ExpressionMacro {
    public static func expansion(
        of node: some FreestandingMacroExpansionSyntax,
        in context: some MacroExpansionContext
    ) throws -> ExprSyntax {
        guard let argument = node.argumentList.first?.expression,
              let segments = argument.as(StringLiteralExprSyntax.self)?.segments,
              segments.count == 1,
              case .stringSegment(let literalSegment)? = segments.first
        else {
            throw CustomError.message("Need a static string")
        }

        let string = literalSegment.content.text
        guard let result = fourCharacterCode(for: string) else {
            throw CustomError.message("Invalid four-character code")
        }

        return "\(raw: result) as UInt32"
    }
}

private func fourCharacterCode(for characters: String) -> UInt32? {
    guard characters.count == 4 else { return nil }

    var result: UInt32 = 0
    for character in characters {
        result = result << 8
        guard let asciiValue = character.asciiValue else { return nil }
        result += UInt32(asciiValue)
    }
    return result
}
enum CustomError: Error { case message(String) }
```

이 매크로를 기존 Swift Package Manager 프로젝트에 추가하는 경우,
매크로 타겟의 진입점 역할을 하는 타입을 추가하고,
해당 타겟이 정의하는 매크로를 나열한다:

```swift
import SwiftCompilerPlugin

@main
struct MyProjectMacros: CompilerPlugin {
    var providingMacros: [Macro.Type] = [FourCharacterCode.self]
}
```

`#fourCharacterCode` 매크로는
표현식을 생성하는 독립형 매크로이므로,
이를 구현하는 `FourCharacterCode` 타입은
`ExpressionMacro` 프로토콜을 준수한다.
`ExpressionMacro` 프로토콜은 하나의 요구사항을 갖는데,
AST를 확장하는 `expansion(of:in:)` 메서드다.
매크로 역할과 해당 SwiftSyntax 프로토콜 목록은
<doc:Attributes#attached> 및 <doc:Attributes#freestanding>에서 확인할 수 있다.

`#fourCharacterCode` 매크로를 확장하기 위해,
Swift는 이 매크로를 사용하는 코드의 AST를
매크로 구현이 포함된 라이브러리로 보낸다.
라이브러리 내부에서 Swift는 `FourCharacterCode.expansion(of:in:)`을 호출하며,
AST와 컨텍스트를 메서드의 인자로 전달한다.
`expansion(of:in:)`의 구현은
`#fourCharacterCode`에 전달된 문자열 인자를 찾아
해당하는 32비트 부호 없는 정수 리터럴 값을 계산한다.

위 예제에서,
첫 번째 `guard` 블록은 AST에서 문자열 리터럴을 추출해
`literalSegment`에 할당한다.
두 번째 `guard` 블록은
`fourCharacterCode(for:)` 함수를 호출한다.
이 두 블록은 매크로가 잘못 사용된 경우 에러를 던지며,
에러 메시지는 잘못된 호출 위치에서 컴파일러 에러로 표시된다.
예를 들어,
`#fourCharacterCode("AB" + "CD")`와 같이 매크로를 호출하면
컴파일러는 "Need a static string" 에러를 표시한다.

`expansion(of:in:)` 메서드는 `ExprSyntax`의 인스턴스를 반환한다.
`ExprSyntax`는 AST에서 표현식을 나타내는 SwiftSyntax 타입이다.
이 타입은 `StringLiteralConvertible` 프로토콜을 준수하므로,
매크로 구현은 결과를 생성하기 위해 문자열 리터럴을 간단한 구문으로 사용한다.
매크로 구현에서 반환하는 모든 SwiftSyntax 타입은
`StringLiteralConvertible`을 준수하므로,
어떤 종류의 매크로를 구현할 때도 이 방식을 사용할 수 있다.

<!-- TODO `\(raw:)`와 non-raw 버전을 비교하세요.  -->

<!--
문자열 반환 API는 여기에서 제공됩니다

https://github.com/swiftlang/swift-syntax/blob/main/Sources/SwiftSyntaxBuilder/Syntax%2BStringInterpolation.swift
-->


## 매크로 개발 및 디버깅

매크로는 테스트를 통한 개발에 적합하다. 매크로는 외부 상태에 의존하지 않고, 외부 상태를 변경하지 않으면서 하나의 AST를 다른 AST로 변환한다. 또한 문자열 리터럴로부터 구문 노드를 생성할 수 있어 테스트 입력을 설정하는 작업이 간단해진다. AST의 `description` 프로퍼티를 읽어 기대값과 비교할 문자열을 얻을 수도 있다.

예를 들어, 이전 섹션에서 다룬 `#fourCharacterCode` 매크로를 테스트하는 코드는 다음과 같다:

```swift
let source: SourceFileSyntax =
    """
    let abcd = #fourCharacterCode("ABCD")
    """

let file = BasicMacroExpansionContext.KnownSourceFile(
    moduleName: "MyModule",
    fullFilePath: "test.swift"
)

let context = BasicMacroExpansionContext(sourceFiles: [source: file])

let transformedSF = source.expand(
    macros:["fourCharacterCode": FourCharacterCode.self],
    in: context
)

let expectedDescription =
    """
    let abcd = 1145258561 as UInt32
    """

precondition(transformedSF.description == expectedDescription)
```

위 예제는 매크로를 테스트하기 위해 전제조건(precondition)을 사용했지만, 테스트 프레임워크를 사용할 수도 있다.

<!-- OUTLINE:

- 디버깅 중 매크로 확장을 확인하는 방법.
  SE 프로토타입은 이를 위해 `-Xfrontend -dump-macro-expansions` 옵션을 제공한다.
  [TR: 이 플래그를 사용하도록 권장해야 할지, 아니면 더 나은 커맨드라인 옵션이 나올지?]

- 제약 조건이 있는 매크로의 경우 진단 기능을 사용해,
  조건이 충족되지 않을 때 컴파일러가 생성한 코드를 빌드하려고 시도하고 실패하는 대신,
  사용자에게 의미 있는 오류 메시지를 제공할 수 있다.

추후 소개할 추가 API와 개념들(순서 무관):

- `SyntaxRewriter`와 방문자 패턴을 사용해 AST를 수정하는 방법

- `FixIt`을 사용해 수정 제안을 추가하는 방법

- 트리비아(trivia) 개념

- `TokenSyntax`
-->

<!--
이 소스 파일은 Swift.org 오픈 소스 프로젝트의 일부이다

Copyright (c) 2014 - 2023 Apple Inc. and the Swift 프로젝트 저자들
Apache License v2.0 및 Runtime Library Exception에 따라 라이선스가 부여됨

라이선스 정보는 https://swift.org/LICENSE.txt에서 확인할 수 있다
Swift 프로젝트 저자 목록은 https://swift.org/CONTRIBUTORS.txt에서 확인할 수 있다
-->


