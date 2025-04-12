# 열거형

열거형은 가능한 값들의 목록을 정의하는 커스텀 타입을 모델링한다.

*열거형*은 관련된 값들의 그룹을 위한 공통 타입을 정의하고, 코드 내에서 타입 안전한 방식으로 이러한 값을 다룰 수 있게 한다.

C 언어에 익숙하다면, C의 열거형이 관련된 이름들을 정수 값들의 집합에 할당한다는 것을 알고 있을 것이다. Swift의 열거형은 훨씬 더 유연하며, 각 케이스에 값을 제공할 필요가 없다. 각 열거형 케이스에 값(*원시* 값)이 제공된다면, 이 값은 문자열, 문자, 정수 또는 부동소수점 타입의 값이 될 수 있다.

또는, 열거형 케이스는 각기 다른 케이스 값과 함께 저장될 *어떤* 타입의 연관된 값을 지정할 수 있다. 이는 다른 언어에서의 공용체나 변형체와 유사하다. 하나의 열거형의 일부로 관련된 케이스들의 공통 집합을 정의할 수 있으며, 각 케이스는 적절한 타입의 다른 값 집합을 연관시킬 수 있다.

Swift의 열거형은 그 자체로 퍼스트클래스 타입이다. 열거형은 전통적으로 클래스에서만 지원되던 많은 기능을 채택한다. 예를 들어, 열거형의 현재 값에 대한 추가 정보를 제공하는 계산된 프로퍼티와, 열거형이 나타내는 값과 관련된 기능을 제공하는 인스턴스 메서드가 있다. 열거형은 초기 케이스 값을 제공하기 위해 초기화자를 정의할 수도 있고, 원래 구현을 넘어 기능을 확장하기 위해 확장될 수도 있으며, 표준 기능을 제공하기 위해 프로토콜을 준수할 수도 있다.

이러한 기능에 대한 자세한 내용은 <doc:Properties>, <doc:Methods>, <doc:Initialization>, <doc:Extensions>, 그리고 <doc:Protocols>를 참고한다.

<!--
  TODO: 이 장은 연관된 값이 없는 열거형이 기본적으로 Hashable과 Equatable을 준수한다는 점(그리고 이것이 실제로 무엇을 의미하는지)을 언급해야 할 것이다.
-->


## 열거형 문법

열거형은 `enum` 키워드로 정의하며, 전체 정의를 중괄호(`{}`) 안에 작성한다:

```swift
enum SomeEnumeration {
    // 열거형 정의가 여기에 들어간다
}
```

<!--
  - test: `enums`

  ```swifttest
  -> enum SomeEnumeration {
        // 열거형 정의가 여기에 들어간다
     }
  ```
-->

다음은 나침반의 네 가지 주요 방향을 나타내는 열거형 예제다:

```swift
enum CompassPoint {
    case north
    case south
    case east
    case west
}
```

<!--
  - test: `enums`

  ```swifttest
  -> enum CompassPoint {
        case north
        case south
        case east
        case west
     }
  ```
-->

열거형에서 정의된 값(예: `north`, `south`, `east`, `west`)을 *열거형 케이스*라고 한다. 새로운 열거형 케이스를 정의할 때는 `case` 키워드를 사용한다.

> 주의: Swift의 열거형 케이스는 C나 Objective-C와 달리 기본적으로 정수값을 가지지 않는다. 위의 `CompassPoint` 예제에서 `north`, `south`, `east`, `west`는 암시적으로 `0`, `1`, `2`, `3`과 같은 값을 가지지 않는다. 대신, 각 열거형 케이스는 그 자체로 `CompassPoint` 타입의 독립적인 값이다.

여러 케이스를 한 줄에 작성할 때는 쉼표로 구분한다:

```swift
enum Planet {
    case mercury, venus, earth, mars, jupiter, saturn, uranus, neptune
}
```

<!--
  - test: `enums`

  ```swifttest
  -> enum Planet {
        case mercury, venus, earth, mars, jupiter, saturn, uranus, neptune
     }
  ```
-->

각 열거형 정의는 새로운 타입을 만든다. Swift의 다른 타입과 마찬가지로 열거형 이름(`CompassPoint`, `Planet` 등)은 대문자로 시작한다. 열거형 타입의 이름은 단수형으로 짓는 것이 일반적이며, 이는 코드의 가독성을 높인다:

```swift
var directionToHead = CompassPoint.west
```

<!--
  - test: `enums`

  ```swifttest
  -> var directionToHead = CompassPoint.west
  ```
-->

`directionToHead`의 타입은 `CompassPoint`의 가능한 값 중 하나로 초기화될 때 추론된다. `directionToHead`가 `CompassPoint` 타입으로 선언되면, 더 짧은 점 문법을 사용해 다른 `CompassPoint` 값을 할당할 수 있다:

```swift
directionToHead = .east
```

<!--
  - test: `enums`

  ```swifttest
  -> directionToHead = .east
  ```
-->

`directionToHead`의 타입이 이미 명확하기 때문에, 값을 설정할 때 타입을 생략할 수 있다. 이는 명시적으로 타입이 지정된 열거형 값을 다룰 때 코드의 가독성을 크게 향상시킨다.


## 열거형 값을 Switch 문으로 매칭하기

`switch` 문을 사용해 개별 열거형 값을 매칭할 수 있다:

```swift
directionToHead = .south
switch directionToHead {
case .north:
    print("Lots of planets have a north")
case .south:
    print("Watch out for penguins")
case .east:
    print("Where the sun rises")
case .west:
    print("Where the skies are blue")
}
// Prints "Watch out for penguins"
```

<!--
  - test: `enums`

  ```swifttest
  -> directionToHead = .south
  -> switch directionToHead {
        case .north:
           print("Lots of planets have a north")
        case .south:
           print("Watch out for penguins")
        case .east:
           print("Where the sun rises")
        case .west:
           print("Where the skies are blue")
     }
  <- Watch out for penguins
  ```
-->

이 코드를 다음과 같이 해석할 수 있다:

"`directionToHead`의 값을 고려하라.  
값이 `.north`인 경우, `"Lots of planets have a north"`를 출력한다.  
값이 `.south`인 경우, `"Watch out for penguins"`를 출력한다."

이런 식으로 각 경우를 처리한다.

<doc:ControlFlow>에서 설명한 것처럼, 열거형의 모든 케이스를 고려할 때 `switch` 문은 반드시 완전해야 한다. 만약 `.west` 케이스를 생략하면, 이 코드는 컴파일되지 않는다. `CompassPoint`의 모든 케이스를 고려하지 않았기 때문이다. 이렇게 완전성을 요구함으로써 열거형 케이스가 실수로 누락되는 것을 방지한다.

모든 열거형 케이스에 대해 `case`를 제공하는 것이 적절하지 않은 경우, 명시적으로 처리되지 않은 케이스를 다루기 위해 `default` 케이스를 제공할 수 있다:

```swift
let somePlanet = Planet.earth
switch somePlanet {
case .earth:
    print("Mostly harmless")
default:
    print("Not a safe place for humans")
}
// Prints "Mostly harmless"
```

<!--
  - test: `enums`

  ```swifttest
  -> let somePlanet = Planet.earth
  -> switch somePlanet {
        case .earth:
           print("Mostly harmless")
        default:
           print("Not a safe place for humans")
     }
  <- Mostly harmless
  ```
-->


## 열거형 케이스 순회하기

특정 열거형의 모든 케이스를 모아 컬렉션으로 활용할 때가 있다. 이를 위해 열거형 이름 뒤에 `: CaseIterable`을 추가한다. Swift는 열거형 타입의 `allCases` 프로퍼티를 통해 모든 케이스를 컬렉션으로 제공한다. 다음 예제를 살펴보자:

```swift
enum Beverage: CaseIterable {
    case coffee, tea, juice
}
let numberOfChoices = Beverage.allCases.count
print("\(numberOfChoices) beverages available")
// Prints "3 beverages available"
```

<!--
  - test: `enums`

  ```swifttest
  -> enum Beverage: CaseIterable {
         case coffee, tea, juice
     }
  -> let numberOfChoices = Beverage.allCases.count
  -> print("\(numberOfChoices) beverages available")
  <- 3 beverages available
  ```
-->

위 예제에서 `Beverage.allCases`를 사용해 `Beverage` 열거형의 모든 케이스를 담은 컬렉션에 접근한다. `allCases`는 일반 컬렉션처럼 사용할 수 있다. 컬렉션의 각 요소는 열거형 타입의 인스턴스로, 이 경우 `Beverage` 값이다. 위 예제는 케이스의 개수를 세고, 아래 예제는 `for`-`in` 루프를 사용해 모든 케이스를 순회한다.

```swift
for beverage in Beverage.allCases {
    print(beverage)
}
// coffee
// tea
// juice
```

<!--
  - test: `enums`

  ```swifttest
  -> for beverage in Beverage.allCases {
         print(beverage)
     }
  << coffee
  << tea
  << juice
  // coffee
  // tea
  // juice
  ```
-->

위 예제에서 사용한 구문은 열거형이 [`CaseIterable`](https://developer.apple.com/documentation/swift/caseiterable) 프로토콜을 준수하도록 표시한다. 프로토콜에 대한 자세한 내용은 <doc:Protocols>를 참고한다.


## 연관 값

이전 섹션의 예제들은 열거형의 각 케이스가 독립적으로 정의되고 타입이 지정된 값임을 보여준다. 상수나 변수를 `Planet.earth`로 설정하고, 나중에 이 값을 확인할 수 있다. 하지만 때로는 이러한 케이스 값과 함께 다른 타입의 값을 저장할 수 있으면 유용할 때가 있다. 이 추가 정보를 *연관 값*이라고 부르며, 코드에서 해당 케이스를 값으로 사용할 때마다 달라질 수 있다.

Swift 열거형은 주어진 타입의 연관 값을 저장하도록 정의할 수 있으며, 필요에 따라 열거형의 각 케이스마다 다른 타입의 값을 사용할 수 있다. 이러한 열거형은 다른 프로그래밍 언어에서 *구별된 공용체*, *태그된 공용체*, 또는 *변형체*로 알려져 있다.

예를 들어, 재고 추적 시스템이 두 가지 다른 타입의 바코드로 제품을 추적해야 한다고 가정해 보자. 일부 제품은 UPC 형식의 1D 바코드로 라벨링되어 있으며, 이는 `0`부터 `9`까지의 숫자를 사용한다. 각 바코드는 숫자 시스템 숫자, 제조업체 코드 다섯 자리, 제품 코드 다섯 자리로 구성된다. 그리고 코드가 올바르게 스캔되었는지 확인하기 위한 검증 숫자가 뒤따른다:

![](barcode_UPC)

다른 제품들은 QR 코드 형식의 2D 바코드로 라벨링되어 있으며, ISO 8859-1 문자를 사용할 수 있고 최대 2,953자 길이의 문자열을 인코딩할 수 있다:

![](barcode_QR)

재고 추적 시스템에서 UPC 바코드를 네 개의 정수로 구성된 튜플로 저장하고, QR 코드 바코드는 임의 길이의 문자열로 저장하는 것이 편리하다.

Swift에서는 두 가지 타입의 제품 바코드를 정의하는 열거형을 다음과 같이 작성할 수 있다:

```swift
enum Barcode {
    case upc(Int, Int, Int, Int)
    case qrCode(String)
}
```

이것은 다음과 같이 읽을 수 있다:

"`Barcode`라는 열거형 타입을 정의한다. 이 타입은 `upc` 값과 함께 (`Int`, `Int`, `Int`, `Int`) 타입의 연관 값을 가질 수 있거나, `qrCode` 값과 함께 `String` 타입의 연관 값을 가질 수 있다."

이 정의는 실제 `Int`나 `String` 값을 제공하지 않는다. 단지 `Barcode` 상수나 변수가 `Barcode.upc` 또는 `Barcode.qrCode`와 같을 때 저장할 수 있는 연관 값의 *타입*을 정의할 뿐이다.

그런 다음 두 가지 타입 중 하나를 사용해 새로운 바코드를 생성할 수 있다:

```swift
var productBarcode = Barcode.upc(8, 85909, 51226, 3)
```

이 예제는 `productBarcode`라는 새로운 변수를 생성하고, `Barcode.upc` 값과 함께 `(8, 85909, 51226, 3)`이라는 연관 튜플 값을 할당한다.

동일한 제품에 다른 타입의 바코드를 할당할 수도 있다:

```swift
productBarcode = .qrCode("ABCDEFGHIJKLMNOP")
```

이 시점에서 원래의 `Barcode.upc`와 그 정수 값들은 새로운 `Barcode.qrCode`와 그 문자열 값으로 대체된다. `Barcode` 타입의 상수와 변수는 `.upc` 또는 `.qrCode` 중 하나를 저장할 수 있지만, 동시에 둘 다 저장할 수는 없다.

<doc:Enumerations#Matching-Enumeration-Values-with-a-Switch-Statement>의 예제와 유사하게, switch 문을 사용해 다른 바코드 타입을 확인할 수 있다. 그러나 이번에는 연관 값들이 switch 문의 일부로 추출된다. 각 연관 값을 상수(`let` 접두사 사용) 또는 변수(`var` 접두사 사용)로 추출하여 `switch` 케이스의 본문 내에서 사용할 수 있다:

```swift
switch productBarcode {
case .upc(let numberSystem, let manufacturer, let product, let check):
    print("UPC: \(numberSystem), \(manufacturer), \(product), \(check).")
case .qrCode(let productCode):
    print("QR code: \(productCode).")
}
// Prints "QR code: ABCDEFGHIJKLMNOP."
```

열거형 케이스의 모든 연관 값이 상수로 추출되거나 모두 변수로 추출되는 경우, 간결함을 위해 케이스 이름 앞에 단일 `let` 또는 `var` 어노테이션을 배치할 수 있다:

```swift
switch productBarcode {
case let .upc(numberSystem, manufacturer, product, check):
    print("UPC : \(numberSystem), \(manufacturer), \(product), \(check).")
case let .qrCode(productCode):
    print("QR code: \(productCode).")
}
// Prints "QR code: ABCDEFGHIJKLMNOP."
```


## 원시 값(Raw Values)

<doc:Enumerations#Associated-Values>의 바코드 예제는 열거형의 각 케이스가 서로 다른 타입의 연관 값을 저장할 수 있음을 보여준다. 연관 값 대신, 열거형 케이스는 기본값으로 미리 채워진 원시 값(*raw values*)을 가질 수 있다. 이때 모든 원시 값은 동일한 타입이어야 한다.

다음은 명명된 열거형 케이스와 함께 원시 ASCII 값을 저장하는 예제다:

```swift
enum ASCIIControlCharacter: Character {
    case tab = "\t"
    case lineFeed = "\n"
    case carriageReturn = "\r"
}
```

<!--
  - test: `rawValues`

  ```swifttest
  -> enum ASCIIControlCharacter: Character {
        case tab = "\t"
        case lineFeed = "\n"
        case carriageReturn = "\r"
     }
  ```
-->

여기서 `ASCIIControlCharacter`라는 열거형의 원시 값은 `Character` 타입으로 정의되며, 일반적인 ASCII 제어 문자들로 설정된다. `Character` 값에 대한 자세한 설명은 <doc:StringsAndCharacters>에서 확인할 수 있다.

원시 값은 문자열, 문자, 정수 또는 부동소수점 숫자 타입 중 하나일 수 있다. 각 원시 값은 열거형 선언 내에서 고유해야 한다.

> 주의: 원시 값은 연관 값과 다르다. 원시 값은 코드에서 열거형을 처음 정의할 때 미리 설정된 값이다. 위의 세 ASCII 코드처럼 특정 열거형 케이스의 원시 값은 항상 동일하다. 반면, 연관 값은 열거형 케이스를 기반으로 새로운 상수나 변수를 생성할 때 설정되며, 매번 다른 값을 가질 수 있다.


### 암시적으로 할당된 Raw 값

정수나 문자열 타입의 raw 값을 저장하는 열거형을 다룰 때, 각 케이스에 대한 raw 값을 명시적으로 할당할 필요가 없다. 값을 할당하지 않으면 Swift가 자동으로 값을 할당해 준다.

예를 들어, 정수를 raw 값으로 사용하는 경우, 각 케이스의 암시적 값은 이전 케이스보다 1씩 증가한다. 첫 번째 케이스에 값을 설정하지 않으면 해당 값은 `0`이 된다.

아래 열거형은 이전 `Planet` 열거형을 개선한 것으로, 각 행성의 태양으로부터의 순서를 나타내기 위해 정수 raw 값을 사용한다:

```swift
enum Planet: Int {
    case mercury = 1, venus, earth, mars, jupiter, saturn, uranus, neptune
}
```

<!--
  - test: `rawValues`

  ```swifttest
  -> enum Planet: Int {
        case mercury = 1, venus, earth, mars, jupiter, saturn, uranus, neptune
     }
  ```
-->

위 예제에서 `Planet.mercury`는 명시적으로 `1`이라는 raw 값을 가지고, `Planet.venus`는 암시적으로 `2`라는 raw 값을 가지며, 나머지도 이와 같이 증가한다.

문자열을 raw 값으로 사용하는 경우, 각 케이스의 암시적 값은 해당 케이스 이름의 텍스트가 된다.

아래 열거형은 이전 `CompassPoint` 열거형을 개선한 것으로, 각 방향의 이름을 나타내기 위해 문자열 raw 값을 사용한다:

```swift
enum CompassPoint: String {
    case north, south, east, west
}
```

<!--
  - test: `rawValues`

  ```swifttest
  -> enum CompassPoint: String {
        case north, south, east, west
     }
  ```
-->

위 예제에서 `CompassPoint.south`는 암시적으로 `"south"`라는 raw 값을 가지며, 나머지도 이와 같이 처리된다.

열거형 케이스의 raw 값은 `rawValue` 프로퍼티를 통해 접근할 수 있다:

```swift
let earthsOrder = Planet.earth.rawValue
// earthsOrder는 3

let sunsetDirection = CompassPoint.west.rawValue
// sunsetDirection은 "west"
```

<!--
  - test: `rawValues`

  ```swifttest
  -> let earthsOrder = Planet.earth.rawValue
  /> earthsOrder is \(earthsOrder)
  </ earthsOrder is 3

  -> let sunsetDirection = CompassPoint.west.rawValue
  /> sunsetDirection is \"\(sunsetDirection)\"
  </ sunsetDirection is "west"
  ```
-->


### 원시 값으로 초기화하기

열거형을 원시 값 타입과 함께 정의하면,
열거형은 자동으로 `rawValue`라는 매개변수를 받는 초기화 메서드를 제공한다.
이 초기화 메서드는 원시 값 타입의 값을 받아서 해당하는 열거형 케이스 또는 `nil`을 반환한다.
이 초기화 메서드를 사용해 새로운 열거형 인스턴스를 생성할 수 있다.

다음 예제는 원시 값 `7`을 사용해 천왕성(`Uranus`)을 식별한다:

```swift
let possiblePlanet = Planet(rawValue: 7)
// possiblePlanet은 Planet? 타입이며 Planet.uranus와 같다
```

<!--
  - test: `rawValues`

  ```swifttest
  -> let possiblePlanet = Planet(rawValue: 7)
  >> print(type(of: possiblePlanet))
  << Optional<Planet>
  >> assert(possiblePlanet == .uranus)
  // possiblePlanet은 Planet? 타입이며 Planet.uranus와 같다
  ```
-->

그러나 모든 `Int` 값이 해당하는 행성을 찾을 수 있는 것은 아니다.
따라서 원시 값 초기화 메서드는 항상 *옵셔널* 열거형 케이스를 반환한다.
위 예제에서 `possiblePlanet`은 `Planet?` 타입,
즉 "옵셔널 `Planet`"이다.

> 참고: 원시 값 초기화 메서드는 실패 가능한 초기화 메서드(failable initializer)이다.
> 모든 원시 값이 열거형 케이스를 반환하지 않기 때문이다.
> 자세한 내용은 <doc:Declarations#Failable-Initializers>를 참고한다.

위치 `11`에 해당하는 행성을 찾으려고 하면,
원시 값 초기화 메서드가 반환하는 옵셔널 `Planet` 값은 `nil`이 된다:

```swift
let positionToFind = 11
if let somePlanet = Planet(rawValue: positionToFind) {
    switch somePlanet {
    case .earth:
        print("대체로 무해함")
    default:
        print("인간에게 안전하지 않은 장소")
    }
} else {
    print("위치 \(positionToFind)에는 행성이 없음")
}
// "위치 11에는 행성이 없음"을 출력
```

<!--
  - test: `rawValues`

  ```swifttest
  -> let positionToFind = 11
  -> if let somePlanet = Planet(rawValue: positionToFind) {
        switch somePlanet {
           case .earth:
              print("대체로 무해함")
           default:
              print("인간에게 안전하지 않은 장소")
        }
     } else {
        print("위치 \(positionToFind)에는 행성이 없음")
     }
  <- 위치 11에는 행성이 없음
  ```
-->

이 예제는 옵셔널 바인딩을 사용해 원시 값 `11`에 해당하는 행성에 접근하려고 시도한다.
`if let somePlanet = Planet(rawValue: 11)` 문은 옵셔널 `Planet`을 생성하고,
`somePlanet`을 해당 옵셔널 `Planet`의 값으로 설정한다.
이 경우, 위치 `11`에 해당하는 행성을 찾을 수 없으므로,
대신 `else` 분기가 실행된다.

<!--
  TODO: 이 장의 순서를 조정해 비연합(non-union) 관련 내용을 모두 함께 묶고,
  연합(Associated Values) 관련 내용을 마지막으로 이동한다.
-->


## 재귀 열거형

*재귀 열거형*은 하나 이상의 열거형 케이스가 연관 값으로 동일한 열거형의 인스턴스를 가지는 열거형이다. 재귀 열거형을 정의할 때는 `indirect` 키워드를 사용해 특정 케이스가 재귀적임을 표시한다. 이 키워드를 사용하면 컴파일러가 필요한 간접 참조 계층을 자동으로 추가한다.

예를 들어, 간단한 산술 표현식을 저장하는 열거형을 살펴보자:

```swift
enum ArithmeticExpression {
    case number(Int)
    indirect case addition(ArithmeticExpression, ArithmeticExpression)
    indirect case multiplication(ArithmeticExpression, ArithmeticExpression)
}
```

<!--
  - test: `recursive-enum-intro`

  ```swifttest
  -> enum ArithmeticExpression {
         case number(Int)
         indirect case addition(ArithmeticExpression, ArithmeticExpression)
         indirect case multiplication(ArithmeticExpression, ArithmeticExpression)
     }
  ```
-->

또한, 열거형 전체에 `indirect` 키워드를 적용해 모든 연관 값을 가진 케이스에 대해 간접 참조를 활성화할 수도 있다:

```swift
indirect enum ArithmeticExpression {
    case number(Int)
    case addition(ArithmeticExpression, ArithmeticExpression)
    case multiplication(ArithmeticExpression, ArithmeticExpression)
}
```

<!--
  - test: `recursive-enum`

  ```swifttest
  -> indirect enum ArithmeticExpression {
         case number(Int)
         case addition(ArithmeticExpression, ArithmeticExpression)
         case multiplication(ArithmeticExpression, ArithmeticExpression)
     }
  ```
-->

이 열거형은 세 가지 종류의 산술 표현식을 저장할 수 있다: 일반 숫자, 두 표현식의 덧셈, 두 표현식의 곱셈. `addition`과 `multiplication` 케이스는 연관 값으로 산술 표현식을 가지며, 이로 인해 표현식을 중첩할 수 있다. 예를 들어, `(5 + 4) * 2`라는 표현식은 곱셈의 오른쪽에 숫자가 있고, 왼쪽에 또 다른 표현식이 있다. 데이터가 중첩되기 때문에, 이를 저장하기 위한 열거형도 중첩을 지원해야 한다. 즉, 열거형은 재귀적이어야 한다. 아래 코드는 `(5 + 4) * 2`를 위해 `ArithmeticExpression` 재귀 열거형을 생성하는 방법을 보여준다:

```swift
let five = ArithmeticExpression.number(5)
let four = ArithmeticExpression.number(4)
let sum = ArithmeticExpression.addition(five, four)
let product = ArithmeticExpression.multiplication(sum, ArithmeticExpression.number(2))
```

<!--
  - test: `recursive-enum`

  ```swifttest
  -> let five = ArithmeticExpression.number(5)
  -> let four = ArithmeticExpression.number(4)
  -> let sum = ArithmeticExpression.addition(five, four)
  -> let product = ArithmeticExpression.multiplication(sum, ArithmeticExpression.number(2))
  ```
-->

재귀 구조를 가진 데이터를 다룰 때는 재귀 함수를 사용하는 것이 간단한 방법이다. 예를 들어, 산술 표현식을 평가하는 함수는 다음과 같이 작성할 수 있다:

```swift
func evaluate(_ expression: ArithmeticExpression) -> Int {
    switch expression {
    case let .number(value):
        return value
    case let .addition(left, right):
        return evaluate(left) + evaluate(right)
    case let .multiplication(left, right):
        return evaluate(left) * evaluate(right)
    }
}

print(evaluate(product))
// Prints "18"
```

<!--
  - test: `recursive-enum`

  ```swifttest
  -> func evaluate(_ expression: ArithmeticExpression) -> Int {
         switch expression {
             case let .number(value):
                 return value
             case let .addition(left, right):
                 return evaluate(left) + evaluate(right)
             case let .multiplication(left, right):
                 return evaluate(left) * evaluate(right)
         }
     }

  -> print(evaluate(product))
  <- 18
  ```
-->

이 함수는 일반 숫자를 평가할 때는 연관 값을 그대로 반환한다. 덧셈이나 곱셈을 평가할 때는 왼쪽 표현식을 평가하고, 오른쪽 표현식을 평가한 다음, 두 결과를 더하거나 곱한다.

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


