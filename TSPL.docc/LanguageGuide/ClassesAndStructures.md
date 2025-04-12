# 구조체와 클래스


데이터를 캡슐화하는 커스텀 타입을 정의한다.

**구조체**와 **클래스**는 프로그램 코드의 기본 구성 요소로, 다양한 용도로 유연하게 사용할 수 있다. 상수, 변수, 함수를 정의할 때와 동일한 문법을 사용하여 구조체와 클래스에 프로퍼티와 메서드를 추가해 기능을 확장할 수 있다.

다른 프로그래밍 언어와 달리, Swift에서는 커스텀 구조체와 클래스를 위해 별도의 인터페이스 파일과 구현 파일을 만들 필요가 없다. Swift에서는 단일 파일 안에 구조체나 클래스를 정의하면, 해당 클래스나 구조체의 외부 인터페이스가 자동으로 다른 코드에서 사용할 수 있게 된다.

> 참고: 클래스의 인스턴스는 전통적으로 *객체*라고 불린다. 하지만 Swift에서 구조체와 클래스는 다른 언어에 비해 기능적으로 훨씬 유사하며, 이 장에서 설명하는 대부분의 기능은 클래스나 구조체 타입의 *인스턴스*에 모두 적용된다. 따라서 더 일반적인 용어인 *인스턴스*를 사용한다.


## 구조체와 클래스 비교

Swift의 구조체와 클래스는 많은 공통점을 가지고 있다. 둘 다 다음 기능을 제공한다:

- 값을 저장하기 위한 프로퍼티 정의
- 기능을 제공하기 위한 메서드 정의
- 서브스크립트 문법을 사용해 값에 접근할 수 있도록 서브스크립트 정의
- 초기 상태를 설정하기 위한 이니셜라이저 정의
- 기본 구현을 확장하기 위한 익스텐션 정의
- 특정 유형의 표준 기능을 제공하기 위한 프로토콜 준수

더 자세한 정보는 <doc:Properties>, <doc:Methods>, <doc:Subscripts>, <doc:Initialization>, <doc:Extensions>, <doc:Protocols>를 참고한다.

클래스는 구조체에 없는 추가 기능을 제공한다:

- 상속을 통해 한 클래스가 다른 클래스의 특성을 물려받을 수 있다.
- 타입 캐스팅을 통해 런타임에 클래스 인스턴스의 타입을 확인하고 해석할 수 있다.
- 디이니셜라이저를 통해 클래스 인스턴스가 할당한 리소스를 해제할 수 있다.
- 참조 카운팅을 통해 클래스 인스턴스에 여러 참조를 허용한다.

더 자세한 정보는 <doc:Inheritance>, <doc:TypeCasting>, <doc:Deinitialization>, <doc:AutomaticReferenceCounting>를 참고한다.

클래스가 제공하는 추가 기능은 복잡성을 증가시키는 대가를 치러야 한다. 일반적으로 구조체를 더 쉽게 이해할 수 있기 때문에 구조체를 우선적으로 사용하고, 클래스는 적절하거나 필요할 때만 사용한다. 실제로는 대부분의 커스텀 타입을 구조체와 열거형으로 정의하게 된다. 더 자세한 비교는 [Choosing Between Structures and Classes](https://developer.apple.com/documentation/swift/choosing_between_structures_and_classes)를 참고한다.

> 참고: 클래스와 액터는 많은 특성과 동작을 공유한다. 액터에 대한 정보는 <doc:Concurrency>를 참고한다.


### 구조체와 클래스 정의 구문

구조체와 클래스는 정의 구문이 유사하다. 구조체는 `struct` 키워드로, 클래스는 `class` 키워드로 선언한다. 둘 다 정의 전체를 중괄호(`{}`) 안에 작성한다.

```swift
struct SomeStructure {
    // 구조체 정의
}
class SomeClass {
    // 클래스 정의
}
```

<!--
  - test: `ClassesAndStructures`

  ```swifttest
  -> struct SomeStructure {
        // 구조체 정의
     }
  -> class SomeClass {
        // 클래스 정의
     }
  ```
-->

> 참고: 새로운 구조체나 클래스를 정의할 때마다 새로운 Swift 타입을 정의하는 것이다. 타입 이름은 `UpperCamelCase`로 작성한다(예: `SomeStructure`, `SomeClass`). 이는 Swift의 표준 타입(`String`, `Int`, `Bool` 등)의 대소문자 규칙과 일치한다. 프로퍼티와 메서드 이름은 `lowerCamelCase`로 작성한다(예: `frameRate`, `incrementCount`). 이렇게 하면 타입 이름과 구분할 수 있다.

다음은 구조체와 클래스를 정의한 예제다.

```swift
struct Resolution {
    var width = 0
    var height = 0
}
class VideoMode {
    var resolution = Resolution()
    var interlaced = false
    var frameRate = 0.0
    var name: String?
}
```

<!--
  - test: `ClassesAndStructures`

  ```swifttest
  -> struct Resolution {
        var width = 0
        var height = 0
     }
  -> class VideoMode {
        var resolution = Resolution()
        var interlaced = false
        var frameRate = 0.0
        var name: String?
     }
  ```
-->

위 예제는 `Resolution`이라는 새로운 구조체를 정의한다. 이 구조체는 픽셀 기반의 디스플레이 해상도를 설명한다. `width`와 `height`라는 두 개의 저장 프로퍼티를 가지고 있다. 저장 프로퍼티는 구조체나 클래스의 일부로 묶여 저장되는 상수나 변수다. 두 프로퍼티는 초기값으로 `0`이 할당되었기 때문에 `Int` 타입으로 추론된다.

또한 위 예제는 `VideoMode`라는 새로운 클래스를 정의한다. 이 클래스는 비디오 디스플레이를 위한 특정 비디오 모드를 설명한다. 이 클래스는 네 개의 저장 프로퍼티를 가지고 있다. 첫 번째 프로퍼티인 `resolution`은 새로운 `Resolution` 구조체 인스턴스로 초기화되며, `Resolution` 타입으로 추론된다. 다른 세 프로퍼티는 `VideoMode` 인스턴스가 생성될 때 `interlaced`는 `false`(비인터레이스 비디오를 의미), `frameRate`는 `0.0`, `name`은 옵셔널 `String` 값으로 초기화된다. `name` 프로퍼티는 옵셔널 타입이기 때문에 기본값으로 `nil`이 할당된다. 즉, "`name` 값이 없음"을 의미한다.


### 구조체와 클래스 인스턴스

`Resolution` 구조체와 `VideoMode` 클래스 정의는 단지 `Resolution`이나 `VideoMode`가 어떻게 생겼는지를 설명할 뿐이다. 이 정의 자체로는 특정한 해상도나 비디오 모드를 설명하지 않는다. 이를 위해서는 구조체나 클래스의 인스턴스를 생성해야 한다.

구조체와 클래스의 인스턴스를 생성하는 문법은 매우 유사하다:

```swift
let someResolution = Resolution()
let someVideoMode = VideoMode()
```

<!--
  - test: `ClassesAndStructures`

  ```swifttest
  -> let someResolution = Resolution()
  -> let someVideoMode = VideoMode()
  ```
-->

구조체와 클래스 모두 새로운 인스턴스를 생성하기 위해 초기화 문법을 사용한다. 가장 간단한 초기화 문법은 클래스나 구조체의 타입 이름 뒤에 빈 괄호를 붙이는 것이다. 예를 들어 `Resolution()`이나 `VideoMode()`와 같은 방식이다. 이렇게 하면 클래스나 구조체의 새로운 인스턴스가 생성되며, 모든 프로퍼티는 기본값으로 초기화된다. 클래스와 구조체의 초기화에 대한 더 자세한 내용은 <doc:Initialization>에서 다룬다.

<!--
  TODO: note that you can only use the default constructor if you provide default values
  for all properties on a structure or class.
-->


### 프로퍼티 접근


인스턴스의 프로퍼티에 접근할 때는 *점 문법(dot syntax)*을 사용한다. 점 문법에서는 인스턴스 이름 뒤에 마침표(`.`)를 붙이고, 공백 없이 프로퍼티 이름을 바로 이어서 작성한다:

```swift
print("The width of someResolution is \(someResolution.width)")
// Prints "The width of someResolution is 0"
```

<!--
  - test: `ClassesAndStructures`

  ```swifttest
  -> print("The width of someResolution is \(someResolution.width)")
  <- The width of someResolution is 0
  ```
-->

이 예제에서 `someResolution.width`는 `someResolution`의 `width` 프로퍼티를 참조하며, 기본 초기값인 `0`을 반환한다.

프로퍼티의 하위 프로퍼티에도 접근할 수 있다. 예를 들어 `VideoMode`의 `resolution` 프로퍼티 안에 있는 `width` 프로퍼티에 접근하는 경우다:

```swift
print("The width of someVideoMode is \(someVideoMode.resolution.width)")
// Prints "The width of someVideoMode is 0"
```

<!--
  - test: `ClassesAndStructures`

  ```swifttest
  -> print("The width of someVideoMode is \(someVideoMode.resolution.width)")
  <- The width of someVideoMode is 0
  ```
-->

또한 점 문법을 사용해 변수 프로퍼티에 새로운 값을 할당할 수도 있다:

```swift
someVideoMode.resolution.width = 1280
print("The width of someVideoMode is now \(someVideoMode.resolution.width)")
// Prints "The width of someVideoMode is now 1280"
```

<!--
  - test: `ClassesAndStructures`

  ```swifttest
  -> someVideoMode.resolution.width = 1280
  -> print("The width of someVideoMode is now \(someVideoMode.resolution.width)")
  <- The width of someVideoMode is now 1280
  ```
-->


### 구조체 타입의 멤버 초기화

모든 구조체는 자동으로 *멤버 초기화* 기능을 제공한다. 이 기능을 사용해 새로운 구조체 인스턴스의 멤버 속성을 초기화할 수 있다. 새로운 인스턴스의 속성 초기값을 이름을 통해 멤버 초기화에 전달할 수 있다.

```swift
let vga = Resolution(width: 640, height: 480)
```

<!--
  - test: `ClassesAndStructures`

  ```swifttest
  -> let vga = Resolution(width: 640, height: 480)
  ```
-->

구조체와 달리, 클래스 인스턴스는 기본 멤버 초기화 기능을 제공하지 않는다. 초기화에 대한 자세한 내용은 <doc:Initialization>에서 확인할 수 있다.

<!--
  - test: `classesDontHaveADefaultMemberwiseInitializer`

  ```swifttest
  -> class C { var x = 0, y = 0 }
  -> let c = C(x: 1, y: 1)
  !$ error: argument passed to call that takes no arguments
  !! let c = C(x: 1, y: 1)
  !!         ^~~~~~~~~~~~
  !!-
  ```
-->


## 구조체와 열거형은 값 타입이다

*값 타입*은 변수나 상수에 할당하거나 함수에 전달할 때 값이 *복사*되는 타입을 말한다.

<!--
  대체 정의:
  값 타입은 한 변수의 변경이 동일 타입의 다른 변수에 영향을 미치지 않는 타입이다.
-->

이전 장에서 이미 값 타입을 광범위하게 사용했다. 실제로 Swift의 모든 기본 타입 --- 정수, 부동 소수점 숫자, 불리언, 문자열, 배열, 딕셔너리 --- 은 값 타입이며, 내부적으로 구조체로 구현되어 있다.

Swift에서 모든 구조체와 열거형은 값 타입이다. 이는 여러분이 생성한 모든 구조체와 열거형 인스턴스, 그리고 그들이 프로퍼티로 가지고 있는 모든 값 타입이 코드 내에서 전달될 때 항상 복사됨을 의미한다.

> 참고: Swift 표준 라이브러리에서 정의한 컬렉션(배열, 딕셔너리, 문자열 등)은 복사 성능 비용을 줄이기 위해 최적화를 사용한다. 이 컬렉션들은 즉시 복사를 만들지 않고, 원본 인스턴스와 복사본 간에 요소가 저장된 메모리를 공유한다. 만약 컬렉션의 복사본 중 하나가 수정되면, 수정 직전에 요소가 복사된다. 코드에서 보이는 동작은 항상 즉시 복사가 발생한 것처럼 보인다.

이전 예제에서 사용한 `Resolution` 구조체를 활용한 예제를 살펴보자:

```swift
let hd = Resolution(width: 1920, height: 1080)
var cinema = hd
```

이 예제는 `hd`라는 상수를 선언하고, 풀 HD 비디오의 너비와 높이(1920 픽셀 너비, 1080 픽셀 높이)로 초기화된 `Resolution` 인스턴스로 설정한다.

그런 다음 `cinema`라는 변수를 선언하고 `hd`의 현재 값으로 설정한다. `Resolution`이 구조체이기 때문에, 기존 인스턴스의 *복사본*이 만들어지고, 이 새로운 복사본이 `cinema`에 할당된다. `hd`와 `cinema`가 동일한 너비와 높이를 가지고 있더라도, 이 둘은 내부적으로 완전히 다른 인스턴스이다.

다음으로, `cinema`의 `width` 프로퍼티를 디지털 시네마 프로젝션에 사용되는 약간 더 넓은 2K 표준의 너비(2048 픽셀 너비, 1080 픽셀 높이)로 수정한다:

```swift
cinema.width = 2048
```

`cinema`의 `width` 프로퍼티를 확인하면, 실제로 `2048`로 변경되었음을 확인할 수 있다:

```swift
print("cinema is now \(cinema.width) pixels wide")
// Prints "cinema is now 2048 pixels wide"
```

하지만 원본 `hd` 인스턴스의 `width` 프로퍼티는 여전히 이전 값인 `1920`을 유지한다:

```swift
print("hd is still \(hd.width) pixels wide")
// Prints "hd is still 1920 pixels wide"
```

`cinema`에 `hd`의 현재 값을 할당했을 때, `hd`에 저장된 *값*이 새로운 `cinema` 인스턴스로 복사되었다. 결과적으로 동일한 숫자 값을 포함하지만 완전히 분리된 두 인스턴스가 생성되었다. 그러나 이들은 별개의 인스턴스이기 때문에, `cinema`의 너비를 `2048`로 설정해도 `hd`에 저장된 너비에는 영향을 미치지 않는다. 아래 그림에서 이를 확인할 수 있다:

![](sharedStateStruct)

동일한 동작이 열거형에도 적용된다:

```swift
enum CompassPoint {
    case north, south, east, west
    mutating func turnNorth() {
        self = .north
    }
}
var currentDirection = CompassPoint.west
let rememberedDirection = currentDirection
currentDirection.turnNorth()

print("The current direction is \(currentDirection)")
print("The remembered direction is \(rememberedDirection)")
// Prints "The current direction is north"
// Prints "The remembered direction is west"
```

`rememberedDirection`에 `currentDirection`의 값을 할당했을 때, 실제로는 그 값의 복사본이 설정된다. 이후 `currentDirection`의 값을 변경해도 `rememberedDirection`에 저장된 원본 값의 복사본에는 영향을 미치지 않는다.


## 클래스는 참조 타입이다

값 타입과 달리, *참조 타입*은 변수나 상수에 할당되거나 함수에 전달될 때 복사되지 않는다. 대신, 동일한 기존 인스턴스에 대한 참조가 사용된다.

위에서 정의한 `VideoMode` 클래스를 사용한 예제를 살펴보자:

```swift
let tenEighty = VideoMode()
tenEighty.resolution = hd
tenEighty.interlaced = true
tenEighty.name = "1080i"
tenEighty.frameRate = 25.0
```

<!--
  - test: `ClassesAndStructures`

  ```swifttest
  -> let tenEighty = VideoMode()
  -> tenEighty.resolution = hd
  -> tenEighty.interlaced = true
  -> tenEighty.name = "1080i"
  -> tenEighty.frameRate = 25.0
  ```
-->

이 예제는 `tenEighty`라는 새로운 상수를 선언하고, `VideoMode` 클래스의 새 인스턴스를 참조하도록 설정한다. 비디오 모드는 이전에 정의된 `1920` x `1080` 해상도의 HD 복사본을 할당받고, 인터레이스로 설정되며, 이름은 `"1080i"`로, 프레임 속도는 초당 `25.0` 프레임으로 설정된다.

다음으로, `tenEighty`는 `alsoTenEighty`라는 새로운 상수에 할당되고, `alsoTenEighty`의 프레임 속도가 수정된다:

```swift
let alsoTenEighty = tenEighty
alsoTenEighty.frameRate = 30.0
```

<!--
  - test: `ClassesAndStructures`

  ```swifttest
  -> let alsoTenEighty = tenEighty
  -> alsoTenEighty.frameRate = 30.0
  ```
-->

클래스는 참조 타입이기 때문에, `tenEighty`와 `alsoTenEighty`는 실제로 동일한 `VideoMode` 인스턴스를 참조한다. 효과적으로, 이들은 동일한 단일 인스턴스에 대한 두 개의 다른 이름일 뿐이다. 아래 그림에서 이를 확인할 수 있다:

![](sharedStateClass)

`tenEighty`의 `frameRate` 속성을 확인하면, 기본 `VideoMode` 인스턴스의 새로운 프레임 속도인 `30.0`이 올바르게 반영된 것을 볼 수 있다:

```swift
print("The frameRate property of tenEighty is now \(tenEighty.frameRate)")
// Prints "The frameRate property of tenEighty is now 30.0"
```

<!--
  - test: `ClassesAndStructures`

  ```swifttest
  -> print("The frameRate property of tenEighty is now \(tenEighty.frameRate)")
  <- The frameRate property of tenEighty is now 30.0
  ```
-->

이 예제는 참조 타입이 코드를 이해하기 어렵게 만들 수 있다는 점도 보여준다. `tenEighty`와 `alsoTenEighty`가 프로그램 코드에서 멀리 떨어져 있다면, 비디오 모드가 어떻게 변경되는지 모든 경로를 찾기 어려울 수 있다. `tenEighty`를 사용하는 곳에서는 `alsoTenEighty`를 사용하는 코드도 고려해야 하며, 그 반대도 마찬가지다. 반면, 값 타입은 동일한 값을 다루는 모든 코드가 소스 파일에서 가까이 위치하기 때문에 이해하기 더 쉽다.

`tenEighty`와 `alsoTenEighty`는 변수가 아닌 *상수*로 선언되었다는 점에 유의하자. 그러나 여전히 `tenEighty.frameRate`와 `alsoTenEighty.frameRate`를 변경할 수 있다. 이는 `tenEighty`와 `alsoTenEighty` 상수 자체의 값이 실제로 변경되는 것이 아니기 때문이다. `tenEighty`와 `alsoTenEighty`는 `VideoMode` 인스턴스를 "저장"하지 않는다. 대신, 이들은 모두 배후에서 `VideoMode` 인스턴스를 *참조*한다. 변경되는 것은 기본 `VideoMode`의 `frameRate` 속성이지, `VideoMode`에 대한 상수 참조의 값이 아니다.

<!--
  TODO: 여기에서 배열과 딕셔너리가 값 타입이며, 이들이 값 타입이나 참조 타입을 저장할 때 어떤 의미가 있는지 설명하고,
  키 복사에 대한 내용도 추가하자. 이는 Alex Migicovsky가 2014년 3월 1일에 시작한 "Dictionaries and key copying" 스위프트 논의 이메일 스레드를 참고하자.
-->

<!--
  TODO: 참조 타입의 멤버를 가진 구조체가 실제로는 참조 타입이며,
  값 타입인 클래스를 만드는 방법에 대한 논의를 추가하자.
-->


### 식별 연산자

클래스는 참조 타입이기 때문에, 여러 상수나 변수가 동일한 클래스 인스턴스를 참조할 수 있다. (구조체와 열거형은 상수나 변수에 할당되거나 함수에 전달될 때 항상 복사되기 때문에 이와 같은 동작을 지원하지 않는다.)

<!--
  - test: `structuresDontSupportTheIdentityOperators`

  ```swifttest
  -> struct S { var x = 0, y = 0 }
  -> let s1 = S()
  -> let s2 = S()
  -> if s1 === s2 { print("s1 === s2") } else { print("s1 !== s2") }
  !$ error: argument type 'S' expected to be an instance of a class or class-constrained type
  !! if s1 === s2 { print("s1 === s2") } else { print("s1 !== s2") }
  !!       ^
  !$ error: argument type 'S' expected to be an instance of a class or class-constrained type
  !! if s1 === s2 { print("s1 === s2") } else { print("s1 !== s2") }
  !!       ^
  ```
-->

<!--
  - test: `enumerationsDontSupportTheIdentityOperators`

  ```swifttest
  -> enum E { case a, b }
  -> let e1 = E.a
  -> let e2 = E.b
  -> if e1 === e2 { print("e1 === e2") } else { print("e1 !== e2") }
  !$ error: argument type 'E' expected to be an instance of a class or class-constrained type
  !! if e1 === e2 { print("e1 === e2") } else { print("e1 !== e2") }
  !!       ^
  !$ error: argument type 'E' expected to be an instance of a class or class-constrained type
  !! if e1 === e2 { print("e1 === e2") } else { print("e1 !== e2") }
  !!       ^
  ```
-->

두 상수나 변수가 정확히 동일한 클래스 인스턴스를 참조하는지 확인하는 것이 유용할 때가 있다. 이를 위해 Swift는 두 가지 식별 연산자를 제공한다:

- 동일함 (`===`)
- 동일하지 않음 (`!==`)

이 연산자를 사용해 두 상수나 변수가 동일한 인스턴스를 참조하는지 확인할 수 있다:

```swift
if tenEighty === alsoTenEighty {
    print("tenEighty and alsoTenEighty refer to the same VideoMode instance.")
}
// Prints "tenEighty and alsoTenEighty refer to the same VideoMode instance."
```

<!--
  - test: `ClassesAndStructures`

  ```swifttest
  -> if tenEighty === alsoTenEighty {
        print("tenEighty and alsoTenEighty refer to the same VideoMode instance.")
     }
  <- tenEighty and alsoTenEighty refer to the same VideoMode instance.
  ```
-->

*동일함* (세 개의 등호, `===`)은 *같음* (두 개의 등호, `==`)과 같은 의미가 아니다. *동일함*은 두 상수나 변수가 동일한 클래스 인스턴스를 참조한다는 의미이다. 반면 *같음*은 두 인스턴스가 값이 동일하거나 동등하다는 의미로, 타입 설계자가 정의한 적절한 기준에 따라 결정된다.

커스텀 구조체와 클래스를 정의할 때, 두 인스턴스가 같은지 여부를 결정하는 것은 개발자의 책임이다. `==`와 `!=` 연산자를 직접 구현하는 방법은 <doc:AdvancedOperators#Equivalence-Operators>에서 설명한다.

<!--
  - test: `classesDontGetEqualityByDefault`

  ```swifttest
  -> class C { var x = 0, y = 0 }
  -> let c1 = C()
  -> let c2 = C()
  -> if c1 == c2 { print("c1 == c2") } else { print("c1 != c2") }
  !$ error: binary operator '==' cannot be applied to two 'C' operands
  !! if c1 == c2 { print("c1 == c2") } else { print("c1 != c2") }
  !!    ~~ ^  ~~
  ```
-->

<!--
  - test: `structuresDontGetEqualityByDefault`

  ```swifttest
  -> struct S { var x = 0, y = 0 }
  -> let s1 = S()
  -> let s2 = S()
  -> if s1 == s2 { print("s1 == s2") } else { print("s1 != s2") }
  !$ error: binary operator '==' cannot be applied to two 'S' operands
  !! if s1 == s2 { print("s1 == s2") } else { print("s1 != s2") }
  !!    ~~ ^  ~~
  ```
-->

<!--
  TODO: This needs clarifying with regards to function references.
-->


### 포인터

C, C++, Objective-C 경험이 있다면, 이러한 언어들이 메모리 주소를 참조하기 위해 *포인터*를 사용한다는 것을 알고 있을 것이다. Swift에서 참조 타입의 인스턴스를 가리키는 상수나 변수는 C 언어의 포인터와 유사하지만, 메모리 주소를 직접 가리키는 포인터는 아니다. 또한 참조를 생성할 때 별표(`*`)를 사용할 필요도 없다. 대신, Swift에서는 다른 상수나 변수를 정의하는 방식과 동일하게 참조를 정의한다. Swift 표준 라이브러리는 포인터를 직접 다뤄야 할 때 사용할 수 있는 포인터와 버퍼 타입을 제공한다. 자세한 내용은 [메모리 관리 매뉴얼](https://developer.apple.com/documentation/swift/swift_standard_library/manual_memory_management)을 참고한다.

<!--
  TODO: 함수는 "인스턴스"가 아니다. 이 부분을 명확히 해야 한다.
-->

<!--
  TODO: 왜 이것이 좋은 것인지에 대한 설명을 추가해야 한다.
-->

<!--
  QUESTION: 튜플과 참조 타입/값 타입의 관계는 어떻게 되는가?
-->

<!--
이 소스 파일은 Swift.org 오픈 소스 프로젝트의 일부입니다.

Copyright (c) 2014 - 2022 Apple Inc. and the Swift 프로젝트 저자들
Apache License v2.0 및 Runtime Library 예외와 함께 라이선스가 부여됨

라이선스 정보는 https://swift.org/LICENSE.txt에서 확인할 수 있습니다.
Swift 프로젝트 저자 목록은 https://swift.org/CONTRIBUTORS.txt에서 확인할 수 있습니다.
-->


