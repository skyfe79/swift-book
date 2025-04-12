# 초기화

타입의 저장 프로퍼티에 초기값을 설정하고, 한 번만 실행되는 설정 작업을 수행한다.

*초기화*는 클래스, 구조체, 열거형의 인스턴스를 사용할 준비를 하는 과정이다. 이 과정은 인스턴스의 각 저장 프로퍼티에 초기값을 할당하고, 새로운 인스턴스가 사용되기 전에 필요한 추가 설정 작업을 수행하는 것을 포함한다.

이 초기화 과정은 *초기화 메서드*를 정의해 구현한다. 초기화 메서드는 특정 타입의 새 인스턴스를 생성하기 위해 호출할 수 있는 특수한 메서드와 같다. Objective-C의 초기화 메서드와 달리 Swift의 초기화 메서드는 값을 반환하지 않는다. 주요 역할은 타입의 새 인스턴스가 처음 사용되기 전에 올바르게 초기화되는 것을 보장하는 것이다.

클래스 타입의 인스턴스는 *디이니셜라이저*도 구현할 수 있다. 디이니셜라이저는 클래스 인스턴스가 메모리에서 해제되기 직전에 커스텀 정리 작업을 수행한다. 디이니셜라이저에 대한 자세한 내용은 <doc:Deinitialization>을 참고한다.


## 저장 프로퍼티의 초기값 설정

클래스와 구조체는 해당 클래스나 구조체의 인스턴스가 생성될 때, 모든 저장 프로퍼티에 적절한 초기값을 반드시 설정해야 한다. 저장 프로퍼티를 불확실한 상태로 둘 수 없다.

저장 프로퍼티의 초기값은 이니셜라이저 내부에서 설정하거나, 프로퍼티 정의의 일부로 기본값을 할당하는 방식으로 설정할 수 있다. 이 두 가지 방법에 대해 다음 섹션에서 자세히 설명한다.

> 주의: 저장 프로퍼티에 기본값을 할당하거나 이니셜라이저 내부에서 초기값을 설정할 때, 해당 프로퍼티의 값은 프로퍼티 옵저버를 호출하지 않고 직접 설정된다.


### 초기화 메서드

*초기화 메서드*는 특정 타입의 새 인스턴스를 생성하기 위해 호출된다. 가장 간단한 형태의 초기화 메서드는 매개변수가 없는 인스턴스 메서드와 같으며, `init` 키워드를 사용해 작성한다:

```swift
init() {
    // 초기화 작업을 여기에 수행
}
```

<!--
  - test: `initializerSyntax`

  ```swifttest
  >> class Test {
  -> init() {
        // 초기화 작업을 여기에 수행
     }
  >> }
  ```
-->

아래 예제는 화씨 온도를 저장하기 위해 `Fahrenheit`라는 새로운 구조체를 정의한다. `Fahrenheit` 구조체는 `Double` 타입의 저장 프로퍼티인 `temperature`를 하나 가지고 있다:

```swift
struct Fahrenheit {
    var temperature: Double
    init() {
        temperature = 32.0
    }
}
var f = Fahrenheit()
print("The default temperature is \(f.temperature)° Fahrenheit")
// "The default temperature is 32.0° Fahrenheit" 출력
```

<!--
  - test: `fahrenheitInit`

  ```swifttest
  -> struct Fahrenheit {
        var temperature: Double
        init() {
           temperature = 32.0
        }
     }
  -> var f = Fahrenheit()
  -> print("The default temperature is \(f.temperature)° Fahrenheit")
  <- The default temperature is 32.0° Fahrenheit
  ```
-->

이 구조체는 매개변수가 없는 단일 초기화 메서드 `init`을 정의하며, 이 메서드는 저장된 온도를 `32.0`(화씨 온도에서 물의 어는점)으로 초기화한다.


### 기본 프로퍼티 값

저장 프로퍼티의 초기값은 이니셜라이저 내부에서 설정할 수 있다. 
또는 프로퍼티 선언 시 *기본 프로퍼티 값*을 지정할 수도 있다. 
프로퍼티를 정의할 때 초기값을 할당함으로써 기본 프로퍼티 값을 지정한다.

> 참고: 프로퍼티가 항상 동일한 초기값을 가지는 경우, 이니셜라이저 내부에서 값을 설정하는 대신 기본값을 제공하는 것이 좋다. 
> 최종 결과는 동일하지만, 기본값을 사용하면 프로퍼티 초기화를 선언부와 더 밀접하게 연결할 수 있다. 
> 이렇게 하면 이니셜라이저가 더 짧고 명확해지며, 기본값으로부터 프로퍼티의 타입을 추론할 수 있다. 
> 또한 기본값을 사용하면 기본 이니셜라이저와 이니셜라이저 상속을 더 쉽게 활용할 수 있다. 
> 이에 대해서는 이 장의 뒷부분에서 자세히 설명한다.

앞서 살펴본 `Fahrenheit` 구조체를 더 간단하게 작성할 수 있다. 
프로퍼티 선언 시점에 `temperature` 프로퍼티의 기본값을 제공하면 된다:

```swift
struct Fahrenheit {
    var temperature = 32.0
}
```

<!--
  - test: `fahrenheitDefault`

  ```swifttest
  -> struct Fahrenheit {
        var temperature = 32.0
     }
  ```
-->


## 초기화 과정 커스텀하기

다음 섹션에서 설명하는 대로, 입력 인자와 선택적 프로퍼티 타입을 사용하거나 초기화 과정에서 상수 프로퍼티를 할당하는 방식으로 초기화 과정을 커스텀할 수 있다.


### 초기화 매개변수

초기화 매개변수는 초기화 과정을 커스텀화하기 위해 초기화 정의의 일부로 제공할 수 있다. 초기화 매개변수는 함수와 메서드 매개변수와 동일한 기능과 문법을 가진다.

다음 예제는 섭씨 온도를 저장하는 `Celsius` 구조체를 정의한다. `Celsius` 구조체는 두 개의 커스텀 초기화 메서드인 `init(fromFahrenheit:)`와 `init(fromKelvin:)`을 구현한다. 이 초기화 메서드는 다른 온도 단위에서 값을 받아 새로운 구조체 인스턴스를 초기화한다:

```swift
struct Celsius {
    var temperatureInCelsius: Double
    init(fromFahrenheit fahrenheit: Double) {
        temperatureInCelsius = (fahrenheit - 32.0) / 1.8
    }
    init(fromKelvin kelvin: Double) {
        temperatureInCelsius = kelvin - 273.15
    }
}
let boilingPointOfWater = Celsius(fromFahrenheit: 212.0)
// boilingPointOfWater.temperatureInCelsius is 100.0
let freezingPointOfWater = Celsius(fromKelvin: 273.15)
// freezingPointOfWater.temperatureInCelsius is 0.0
```

<!--
  - test: `initialization`

  ```swifttest
  -> struct Celsius {
        var temperatureInCelsius: Double
        init(fromFahrenheit fahrenheit: Double) {
           temperatureInCelsius = (fahrenheit - 32.0) / 1.8
        }
        init(fromKelvin kelvin: Double) {
           temperatureInCelsius = kelvin - 273.15
        }
     }
  -> let boilingPointOfWater = Celsius(fromFahrenheit: 212.0)
  /> boilingPointOfWater.temperatureInCelsius is \(boilingPointOfWater.temperatureInCelsius)
  </ boilingPointOfWater.temperatureInCelsius is 100.0
  -> let freezingPointOfWater = Celsius(fromKelvin: 273.15)
  /> freezingPointOfWater.temperatureInCelsius is \(freezingPointOfWater.temperatureInCelsius)
  </ freezingPointOfWater.temperatureInCelsius is 0.0
  ```
-->

첫 번째 초기화 메서드는 `fromFahrenheit`라는 인자 레이블과 `fahrenheit`라는 매개변수 이름을 가진 단일 초기화 매개변수를 갖는다. 두 번째 초기화 메서드는 `fromKelvin`이라는 인자 레이블과 `kelvin`이라는 매개변수 이름을 가진 단일 초기화 매개변수를 갖는다. 두 초기화 메서드는 각각 단일 인자를 받아 해당하는 섭씨 값으로 변환하고, 이 값을 `temperatureInCelsius`라는 프로퍼티에 저장한다.

<!--
  TODO: 초기화 매개변수의 기본값 예시를 제공하여, 여러 초기화 메서드를 "무료로" 얻는 방법을 보여줄 필요가 있음.
-->


### 파라미터 이름과 인자 레이블

함수와 메서드의 파라미터와 마찬가지로,  
초기화 파라미터도 초기화 본문 내에서 사용할 파라미터 이름과  
초기화를 호출할 때 사용할 인자 레이블을 가질 수 있다.

하지만 초기화는 함수나 메서드와 달리 괄호 앞에 식별 가능한 함수 이름이 없다.  
따라서 초기화 파라미터의 이름과 타입은 어떤 초기화를 호출할지 결정하는 데 중요한 역할을 한다.  
이 때문에 Swift는 초기화 파라미터에 인자 레이블을 명시하지 않으면 *모든* 파라미터에 자동으로 인자 레이블을 제공한다.

아래 예제는 `Color`라는 구조체를 정의한다.  
이 구조체는 `red`, `green`, `blue`라는 세 개의 상수 프로퍼티를 가지며,  
각 프로퍼티는 `0.0`에서 `1.0` 사이의 값을 저장해 색상의 빨강, 초록, 파랑 정도를 나타낸다.

`Color`는 빨강, 초록, 파랑 값을 설정하는 세 개의 `Double` 타입 파라미터를 가진 초기화를 제공한다.  
또한 `white`라는 단일 파라미터를 가진 두 번째 초기화도 제공하는데,  
이 초기화는 세 가지 색상 프로퍼티에 동일한 값을 할당한다.

```swift
struct Color {
    let red, green, blue: Double
    init(red: Double, green: Double, blue: Double) {
        self.red   = red
        self.green = green
        self.blue  = blue
    }
    init(white: Double) {
        red   = white
        green = white
        blue  = white
    }
}
```

<!--
  - test: `externalParameterNames, externalParameterNames-err`

  ```swifttest
  -> struct Color {
        let red, green, blue: Double
        init(red: Double, green: Double, blue: Double) {
           self.red   = red
           self.green = green
           self.blue  = blue
        }
        init(white: Double) {
           red   = white
           green = white
           blue  = white
        }
     }
  ```
-->

두 초기화 모두 각 파라미터에 이름을 붙여 값을 전달함으로써 새로운 `Color` 인스턴스를 생성할 수 있다:

```swift
let magenta = Color(red: 1.0, green: 0.0, blue: 1.0)
let halfGray = Color(white: 0.5)
```

<!--
  - test: `externalParameterNames`

  ```swifttest
  -> let magenta = Color(red: 1.0, green: 0.0, blue: 1.0)
  -> let halfGray = Color(white: 0.5)
  >> assert(halfGray.red == 0.5)
  >> assert(halfGray.green == 0.5)
  >> assert(halfGray.blue == 0.5)
  ```
-->

이 초기화를 호출할 때는 반드시 인자 레이블을 사용해야 한다.  
인자 레이블이 정의된 경우 이를 생략하면 컴파일 타임 오류가 발생한다:

```swift
let veryGreen = Color(0.0, 1.0, 0.0)
// 이 코드는 컴파일 타임 오류를 발생시킨다 - 인자 레이블이 필요하다
```

<!--
  - test: `externalParameterNames-err`

  ```swifttest
  -> let veryGreen = Color(0.0, 1.0, 0.0)
  // 이 코드는 컴파일 타임 오류를 발생시킨다 - 인자 레이블이 필요하다
  !$ error: missing argument labels 'red:green:blue:' in call
  !! let veryGreen = Color(0.0, 1.0, 0.0)
  !! ^
  !! red: green:  blue:
  ```
-->


### 인자 레이블이 없는 초기화 매개변수

초기화 매개변수에 인자 레이블을 사용하고 싶지 않다면, 명시적 인자 레이블 대신 밑줄(`_`)을 사용해 기본 동작을 재정의할 수 있다.

앞서 <doc:Initialization#Initialization-Parameters>에서 다룬 `Celsius` 예제를 확장해, 이미 섭씨 단위인 `Double` 값으로 새로운 `Celsius` 인스턴스를 생성하는 추가 초기화 메서드를 구현해 보자.

```swift
struct Celsius {
    var temperatureInCelsius: Double
    init(fromFahrenheit fahrenheit: Double) {
        temperatureInCelsius = (fahrenheit - 32.0) / 1.8
    }
    init(fromKelvin kelvin: Double) {
        temperatureInCelsius = kelvin - 273.15
    }
    init(_ celsius: Double) {
        temperatureInCelsius = celsius
    }
}
let bodyTemperature = Celsius(37.0)
// bodyTemperature.temperatureInCelsius는 37.0이다
```

<!--
  - test: `initializersWithoutExternalParameterNames`

  ```swifttest
  -> struct Celsius {
        var temperatureInCelsius: Double
        init(fromFahrenheit fahrenheit: Double) {
           temperatureInCelsius = (fahrenheit - 32.0) / 1.8
        }
        init(fromKelvin kelvin: Double) {
           temperatureInCelsius = kelvin - 273.15
        }
        init(_ celsius: Double) {
           temperatureInCelsius = celsius
        }
     }
  -> let bodyTemperature = Celsius(37.0)
  /> bodyTemperature.temperatureInCelsius is \(bodyTemperature.temperatureInCelsius)
  </ bodyTemperature.temperatureInCelsius is 37.0
  ```
-->

`Celsius(37.0)`과 같은 초기화 호출은 인자 레이블 없이도 의도가 명확하다. 따라서 이 초기화 메서드를 `init(_ celsius: Double)`로 작성해 이름 없는 `Double` 값을 제공하는 방식으로 호출할 수 있다.


### 옵셔널 프로퍼티 타입

커스텀 타입에 저장 프로퍼티가 "값 없음"을 허용해야 하는 경우, 이를 옵셔널 타입으로 선언한다. 이는 초기화 중에 값을 설정할 수 없거나, 나중에 "값 없음"이 허용되는 경우에 유용하다. 옵셔널 타입의 프로퍼티는 자동으로 `nil` 값으로 초기화되며, 이는 초기화 시점에 "아직 값이 없음"을 의도적으로 나타낸다.

다음 예제는 `SurveyQuestion`이라는 클래스를 정의하며, 옵셔널 `String` 타입의 `response` 프로퍼티를 가진다:

```swift
class SurveyQuestion {
    var text: String
    var response: String?
    init(text: String) {
        self.text = text
    }
    func ask() {
        print(text)
    }
}
let cheeseQuestion = SurveyQuestion(text: "Do you like cheese?")
cheeseQuestion.ask()
// Prints "Do you like cheese?"
cheeseQuestion.response = "Yes, I do like cheese."
```

<!--
  - test: `surveyQuestionVariable`

  ```swifttest
  -> class SurveyQuestion {
        var text: String
        var response: String?
        init(text: String) {
           self.text = text
        }
        func ask() {
           print(text)
        }
     }
  -> let cheeseQuestion = SurveyQuestion(text: "Do you like cheese?")
  -> cheeseQuestion.ask()
  <- Do you like cheese?
  -> cheeseQuestion.response = "Yes, I do like cheese."
  ```
-->

설문 질문에 대한 응답은 질문이 나오기 전까지 알 수 없기 때문에, `response` 프로퍼티는 `String?` 또는 "옵셔널 `String`" 타입으로 선언된다. `SurveyQuestion`의 새 인스턴스가 초기화될 때, 이 프로퍼티는 자동으로 "아직 문자열 없음"을 의미하는 `nil` 기본값으로 설정된다.


### 초기화 과정에서 상수 프로퍼티 할당하기

상수 프로퍼티는 초기화가 완료될 때까지 명확한 값을 할당하기만 하면, 초기화 과정 중 어느 시점에서든 값을 할당할 수 있다. 상수 프로퍼티에 값이 한 번 할당되면, 이후에는 값을 변경할 수 없다.

<!--
  - test: `constantPropertyAssignment`

  ```swifttest
  >> struct S {
        let c: Int
        init() {
           self.c = 1
           self.c = 2
        }
     }
  !$ error: immutable value 'self.c' may only be initialized once
  !! self.c = 2
  !! ^
  !$ note: change 'let' to 'var' to make it mutable
  !! let c: Int
  !! ^~~
  !! var
  ```
-->

<!--
  - test: `constantPropertyAssignmentWithInitialValue`

  ```swifttest
  >> struct S {
        let c: Int = 0
        init() {
           self.c = 1
        }
     }
  !$ error: immutable value 'self.c' may only be initialized once
  !! self.c = 1
  !! ^
  !$ note: initial value already provided in 'let' declaration
  !! let c: Int = 0
  !! ^
  !$ note: change 'let' to 'var' to make it mutable
  !! let c: Int = 0
  !! ^~~
  !! var
  ```
-->

> 참고: 클래스 인스턴스의 경우, 상수 프로퍼티는 해당 프로퍼티를 선언한 클래스에서만 초기화 과정 중에 수정할 수 있다. 하위 클래스에서는 수정할 수 없다.

앞서 살펴본 `SurveyQuestion` 예제를 수정해 질문의 `text` 프로퍼티를 변수 프로퍼티가 아닌 상수 프로퍼티로 사용할 수 있다. 이렇게 하면 `SurveyQuestion` 인스턴스가 생성된 후 질문이 변경되지 않음을 나타낼 수 있다. `text` 프로퍼티가 상수로 선언되었더라도, 클래스의 초기화 메서드 내에서 값을 설정할 수 있다:

```swift
class SurveyQuestion {
    let text: String
    var response: String?
    init(text: String) {
        self.text = text
    }
    func ask() {
        print(text)
    }
}
let beetsQuestion = SurveyQuestion(text: "How about beets?")
beetsQuestion.ask()
// "How about beets?" 출력
beetsQuestion.response = "I also like beets. (But not with cheese.)"
```

<!--
  - test: `surveyQuestionConstant`

  ```swifttest
  -> class SurveyQuestion {
        let text: String
        var response: String?
        init(text: String) {
           self.text = text
        }
        func ask() {
           print(text)
        }
     }
  -> let beetsQuestion = SurveyQuestion(text: "How about beets?")
  -> beetsQuestion.ask()
  <- How about beets?
  -> beetsQuestion.response = "I also like beets. (But not with cheese.)"
  ```
-->


## 기본 초기화 구문

Swift는 모든 프로퍼티에 기본값이 설정되어 있고, 별도의 초기화 구문을 제공하지 않는 구조체나 클래스에 대해 *기본 초기화 구문*을 자동으로 제공한다. 이 기본 초기화 구문은 모든 프로퍼티를 기본값으로 설정한 새로운 인스턴스를 생성한다.

<!--
  - test: `defaultInitializersForStructAndClass`

  ```swifttest
  -> struct S { var s: String = "s" }
  -> assert(S().s == "s")
  -> class A { var a: String = "a" }
  -> assert(A().a == "a")
  -> class B: A { var b: String = "b" }
  -> assert(B().a == "a")
  -> assert(B().b ==  "b")
  ```
-->

다음 예제는 `ShoppingListItem`이라는 클래스를 정의한다. 이 클래스는 쇼핑 목록에 있는 항목의 이름, 수량, 구매 상태를 캡슐화한다.

```swift
class ShoppingListItem {
    var name: String?
    var quantity = 1
    var purchased = false
}
var item = ShoppingListItem()
```

<!--
  - test: `initialization`

  ```swifttest
  -> class ShoppingListItem {
        var name: String?
        var quantity = 1
        var purchased = false
     }
  -> var item = ShoppingListItem()
  ```
-->

`ShoppingListItem` 클래스의 모든 프로퍼티는 기본값을 가지고 있으며, 슈퍼클래스가 없는 기본 클래스이기 때문에, Swift는 자동으로 기본 초기화 구문을 제공한다. 이 초기화 구문은 모든 프로퍼티를 기본값으로 설정한 새로운 인스턴스를 생성한다. (`name` 프로퍼티는 옵셔널 `String` 타입이므로, 코드에 명시적으로 작성되지 않았더라도 기본값으로 `nil`이 할당된다.) 위 예제에서는 `ShoppingListItem` 클래스의 기본 초기화 구문을 사용해 `ShoppingListItem()` 구문으로 새로운 인스턴스를 생성하고, 이를 `item`이라는 변수에 할당한다.


### 구조체 타입의 멤버 초기화

구조체 타입은 커스텀 초기화를 정의하지 않으면 자동으로 *멤버 초기화*를 제공한다. 기본 초기화와 달리, 구조체는 기본값이 없는 저장 프로퍼티가 있어도 멤버 초기화를 받는다.

<!--
  - test: `memberwiseInitializersDontRequireDefaultStoredPropertyValues`

  ```swifttest
  -> struct S { var int: Int; var string: String }
  -> let s = S(int: 42, string: "hello")

  -> struct SS { var int = 10; var string: String }
  -> let ss = SS(int: 42, string: "hello")
  ```
-->

멤버 초기화는 새로운 구조체 인스턴스의 멤버 프로퍼티를 초기화하는 간편한 방법이다. 새 인스턴스의 프로퍼티 초기값을 이름으로 전달할 수 있다.

아래 예제는 `width`와 `height`라는 두 프로퍼티를 가진 `Size` 구조체를 정의한다. 두 프로퍼티는 기본값 `0.0`을 할당함으로써 `Double` 타입으로 추론된다.

`Size` 구조체는 자동으로 `init(width:height:)` 멤버 초기화를 제공하며, 이를 사용해 새로운 `Size` 인스턴스를 초기화할 수 있다:

```swift
struct Size {
    var width = 0.0, height = 0.0
}
let twoByTwo = Size(width: 2.0, height: 2.0)
```

<!--
  - test: `initialization`

  ```swifttest
  -> struct Size {
        var width = 0.0, height = 0.0
     }
  -> let twoByTwo = Size(width: 2.0, height: 2.0)
  ```
-->

멤버 초기화를 호출할 때, 기본값이 있는 프로퍼티는 생략할 수 있다. 위 예제에서 `Size` 구조체는 `height`와 `width` 프로퍼티 모두 기본값을 가지고 있다. 두 프로퍼티 중 하나 또는 둘 다 생략할 수 있으며, 초기화는 생략된 프로퍼티에 대해 기본값을 사용한다. 예를 들어:

```swift
let zeroByTwo = Size(height: 2.0)
print(zeroByTwo.width, zeroByTwo.height)
// Prints "0.0 2.0"

let zeroByZero = Size()
print(zeroByZero.width, zeroByZero.height)
// Prints "0.0 0.0"
```

<!--
  - test: `initialization`

  ```swifttest
  -> let zeroByTwo = Size(height: 2.0)
  -> print(zeroByTwo.width, zeroByTwo.height)
  <- 0.0 2.0

  -> let zeroByZero = Size()
  -> print(zeroByZero.width, zeroByZero.height)
  <- 0.0 0.0
  ```
-->


## 값 타입의 이니셜라이저 위임

이니셜라이저는 다른 이니셜라이저를 호출해 인스턴스 초기화의 일부를 수행할 수 있다. 이를 *이니셜라이저 위임*이라고 하며, 여러 이니셜라이저 간에 코드 중복을 방지한다.

이니셜라이저 위임이 어떻게 동작하는지, 그리고 어떤 형태의 위임이 허용되는지는 값 타입과 클래스 타입에 따라 다르다. 값 타입(구조체와 열거형)은 상속을 지원하지 않기 때문에, 이니셜라이저 위임 과정이 상대적으로 간단하다. 값 타입은 자신이 제공한 다른 이니셜라이저에게만 위임할 수 있다. 반면 클래스는 다른 클래스를 상속할 수 있으며, 이는 초기화 과정에서 상속된 모든 저장 프로퍼티에 적절한 값을 할당해야 하는 추가적인 책임이 있음을 의미한다. 이러한 책임은 <doc:Initialization#Class-Inheritance-and-Initialization>에서 자세히 설명한다.

값 타입의 경우, 커스텀 이니셜라이저를 작성할 때 동일한 값 타입의 다른 이니셜라이저를 참조하기 위해 `self.init`을 사용한다. `self.init`은 이니셜라이저 내부에서만 호출할 수 있다.

값 타입에 커스텀 이니셜라이저를 정의하면, 해당 타입의 기본 이니셜라이저(또는 구조체인 경우 멤버와이즈 이니셜라이저)에 더 이상 접근할 수 없다. 이 제약은 더 복잡한 이니셜라이저에서 제공하는 추가적인 필수 설정이 자동 이니셜라이저를 사용하는 과정에서 실수로 우회되는 상황을 방지한다.

> 참고: 커스텀 값 타입이 기본 이니셜라이저와 멤버와이즈 이니셜라이저, 그리고 자신의 커스텀 이니셜라이저로 모두 초기화될 수 있도록 하려면, 커스텀 이니셜라이저를 값 타입의 원래 구현 부분이 아닌 익스텐션에 작성해야 한다. 자세한 내용은 <doc:Extensions>를 참고하라.

다음 예제는 기하학적 사각형을 나타내는 커스텀 `Rect` 구조체를 정의한다. 이 예제는 모든 프로퍼티에 기본값 `0.0`을 제공하는 `Size`와 `Point`라는 두 개의 지원 구조체를 필요로 한다:

```swift
struct Size {
    var width = 0.0, height = 0.0
}
struct Point {
    var x = 0.0, y = 0.0
}
```

<!--
  - test: `valueDelegation`

  ```swifttest
  -> struct Size {
        var width = 0.0, height = 0.0
     }
  -> struct Point {
        var x = 0.0, y = 0.0
     }
  ```
-->

아래 `Rect` 구조체는 세 가지 방법으로 초기화할 수 있다. 기본적으로 `origin`과 `size` 프로퍼티 값을 0으로 초기화하거나, 특정 원점과 크기를 제공하거나, 특정 중심점과 크기를 제공하는 방법이다. 이러한 초기화 옵션은 `Rect` 구조체 정의에 포함된 세 가지 커스텀 이니셜라이저로 표현된다:

```swift
struct Rect {
    var origin = Point()
    var size = Size()
    init() {}
    init(origin: Point, size: Size) {
        self.origin = origin
        self.size = size
    }
    init(center: Point, size: Size) {
        let originX = center.x - (size.width / 2)
        let originY = center.y - (size.height / 2)
        self.init(origin: Point(x: originX, y: originY), size: size)
    }
}
```

<!--
  - test: `valueDelegation`

  ```swifttest
  -> struct Rect {
        var origin = Point()
        var size = Size()
        init() {}
        init(origin: Point, size: Size) {
           self.origin = origin
           self.size = size
        }
        init(center: Point, size: Size) {
           let originX = center.x - (size.width / 2)
           let originY = center.y - (size.height / 2)
           self.init(origin: Point(x: originX, y: originY), size: size)
        }
     }
  ```
-->

첫 번째 `Rect` 이니셜라이저인 `init()`은 구조체가 커스텀 이니셜라이저를 가지지 않았을 때 받을 기본 이니셜라이저와 기능적으로 동일하다. 이 이니셜라이저는 빈 본문을 가지며, 빈 중괄호 `{}`로 표현된다. 이 이니셜라이저를 호출하면 `origin`과 `size` 프로퍼티가 각각 `Point(x: 0.0, y: 0.0)`과 `Size(width: 0.0, height: 0.0)`의 기본값으로 초기화된 `Rect` 인스턴스를 반환한다:

```swift
let basicRect = Rect()
// basicRect의 origin은 (0.0, 0.0)이고 size는 (0.0, 0.0)이다
```

<!--
  - test: `valueDelegation`

  ```swifttest
  -> let basicRect = Rect()
  /> basicRect의 origin은 (\(basicRect.origin.x), \(basicRect.origin.y))이고 size는 (\(basicRect.size.width), \(basicRect.size.height))이다
  </ basicRect의 origin은 (0.0, 0.0)이고 size는 (0.0, 0.0)이다
  ```
-->

두 번째 `Rect` 이니셜라이저인 `init(origin:size:)`는 구조체가 커스텀 이니셜라이저를 가지지 않았을 때 받을 멤버와이즈 이니셜라이저와 기능적으로 동일하다. 이 이니셜라이저는 단순히 `origin`과 `size` 인자 값을 해당 저장 프로퍼티에 할당한다:

```swift
let originRect = Rect(origin: Point(x: 2.0, y: 2.0),
    size: Size(width: 5.0, height: 5.0))
// originRect의 origin은 (2.0, 2.0)이고 size는 (5.0, 5.0)이다
```

<!--
  - test: `valueDelegation`

  ```swifttest
  -> let originRect = Rect(origin: Point(x: 2.0, y: 2.0),
        size: Size(width: 5.0, height: 5.0))
  /> originRect의 origin은 (\(originRect.origin.x), \(originRect.origin.y))이고 size는 (\(originRect.size.width), \(originRect.size.height))이다
  </ originRect의 origin은 (2.0, 2.0)이고 size는 (5.0, 5.0)이다
  ```
-->

세 번째 `Rect` 이니셜라이저인 `init(center:size:)`는 조금 더 복잡하다. 이 이니셜라이저는 `center` 점과 `size` 값을 기반으로 적절한 원점을 계산한다. 그런 다음 `init(origin:size:)` 이니셜라이저를 호출(또는 *위임*)하여 새로운 원점과 크기 값을 해당 프로퍼티에 저장한다:

```swift
let centerRect = Rect(center: Point(x: 4.0, y: 4.0),
    size: Size(width: 3.0, height: 3.0))
// centerRect의 origin은 (2.5, 2.5)이고 size는 (3.0, 3.0)이다
```

<!--
  - test: `valueDelegation`

  ```swifttest
  -> let centerRect = Rect(center: Point(x: 4.0, y: 4.0),
        size: Size(width: 3.0, height: 3.0))
  /> centerRect의 origin은 (\(centerRect.origin.x), \(centerRect.origin.y))이고 size는 (\(centerRect.size.width), \(centerRect.size.height))이다
  </ centerRect의 origin은 (2.5, 2.5)이고 size는 (3.0, 3.0)이다
  ```
-->

`init(center:size:)` 이니셜라이저는 새로운 `origin`과 `size` 값을 직접 해당 프로퍼티에 할당할 수도 있었다. 그러나 이미 해당 기능을 제공하는 기존 이니셜라이저를 활용하는 것이 더 편리하고 의도가 명확하다.

> 참고: `init()`과 `init(origin:size:)` 이니셜라이저를 직접 정의하지 않고 이 예제를 작성하는 다른 방법은 <doc:Extensions>를 참고하라.


## 클래스 상속과 초기화

클래스의 모든 저장 프로퍼티는 ---
슈퍼클래스로부터 상속받은 프로퍼티를 포함하여 ---
초기화 과정에서 반드시 초기값을 할당해야 한다.

Swift는 클래스 타입을 위해 두 가지 초기화 메서드를 정의한다.
이를 통해 모든 저장 프로퍼티가 초기값을 받도록 보장한다.
이 두 가지 초기화 메서드는 지정 초기화 메서드(designated initializer)와 편의 초기화 메서드(convenience initializer)로 알려져 있다.


### 지정 이니셜라이저와 편의 이니셜라이저

**지정 이니셜라이저**는 클래스의 주요 초기화 메서드다. 지정 이니셜라이저는 해당 클래스에서 도입한 모든 프로퍼티를 완전히 초기화하고, 슈퍼클래스 체인을 따라 초기화를 계속하기 위해 적절한 슈퍼클래스 이니셜라이저를 호출한다.

클래스는 일반적으로 지정 이니셜라이저를 거의 가지지 않으며, 하나만 갖는 경우가 흔하다. 지정 이니셜라이저는 초기화가 이루어지는 "깔대기" 지점이며, 이를 통해 초기화 프로세스가 슈퍼클래스 체인을 따라 계속된다.

모든 클래스는 최소한 하나의 지정 이니셜라이저를 가져야 한다. 어떤 경우에는 슈퍼클래스로부터 하나 이상의 지정 이니셜라이저를 상속받아 이 요구 사항을 충족한다. 이에 대한 자세한 내용은 아래 <doc:Initialization#Automatic-Initializer-Inheritance>에서 확인할 수 있다.

**편의 이니셜라이저**는 클래스의 보조 초기화 메서드다. 편의 이니셜라이저는 동일한 클래스의 지정 이니셜라이저를 호출하되, 지정 이니셜라이저의 일부 매개변수를 기본값으로 설정할 수 있다. 또한 특정 사용 사례나 입력 값 타입에 맞게 클래스의 인스턴스를 생성하기 위해 편의 이니셜라이저를 정의할 수도 있다.

편의 이니셜라이저는 클래스에 필요하지 않다면 제공하지 않아도 된다. 일반적인 초기화 패턴을 단축하는 것이 시간을 절약하거나 클래스 초기화의 의도를 더 명확히 할 때 편의 이니셜라이저를 생성한다.


### 지정 초기화 메서드와 편의 초기화 메서드 문법

클래스의 지정 초기화 메서드는 값 타입의 간단한 초기화 메서드와 동일한 방식으로 작성한다:

```swift
init(<#parameters#>) {
   <#statements#>
}
```

편의 초기화 메서드는 동일한 스타일로 작성하지만, `init` 키워드 앞에 `convenience` 수식어를 공백으로 구분하여 추가한다:

```swift
convenience init(<#parameters#>) {
   <#statements#>
}
```


### 클래스 타입의 초기화 위임

지정 초기화 메서드와 편의 초기화 메서드 간의 관계를 단순화하기 위해, Swift는 초기화 메서드 간의 위임 호출에 대해 다음과 같은 세 가지 규칙을 적용한다:

- **규칙 1**:
  지정 초기화 메서드는 반드시 바로 위의 슈퍼클래스에 있는 지정 초기화 메서드를 호출해야 한다.

- **규칙 2**:
  편의 초기화 메서드는 반드시 *같은* 클래스 내의 다른 초기화 메서드를 호출해야 한다.

- **규칙 3**:
  편의 초기화 메서드는 궁극적으로 지정 초기화 메서드를 호출해야 한다.

이 규칙을 쉽게 기억하는 방법은 다음과 같다:

- 지정 초기화 메서드는 항상 *위로* 위임한다.
- 편의 초기화 메서드는 항상 *가로로* 위임한다.

이 규칙은 아래 그림에서 설명한다:

![](initializerDelegation01)

이 그림에서 슈퍼클래스는 하나의 지정 초기화 메서드와 두 개의 편의 초기화 메서드를 가지고 있다. 하나의 편의 초기화 메서드는 다른 편의 초기화 메서드를 호출하고, 이 편의 초기화 메서드는 다시 지정 초기화 메서드를 호출한다. 이는 위의 규칙 2와 3을 만족한다. 슈퍼클래스는 더 이상의 슈퍼클래스를 가지지 않으므로, 규칙 1은 적용되지 않는다.

이 그림의 서브클래스는 두 개의 지정 초기화 메서드와 하나의 편의 초기화 메서드를 가지고 있다. 편의 초기화 메서드는 같은 클래스 내의 다른 초기화 메서드만 호출할 수 있으므로, 두 지정 초기화 메서드 중 하나를 호출해야 한다. 이는 위의 규칙 2와 3을 만족한다. 두 지정 초기화 메서드는 모두 슈퍼클래스의 지정 초기화 메서드를 호출해야 하며, 이는 위의 규칙 1을 만족한다.

> 참고: 이 규칙들은 클래스의 사용자가 각 클래스의 인스턴스를 *생성*하는 방식에 영향을 미치지 않는다. 위 그림에 나온 어떤 초기화 메서드도 해당 클래스의 완전히 초기화된 인스턴스를 생성하는 데 사용할 수 있다. 이 규칙들은 단지 클래스의 초기화 메서드를 구현하는 방식에만 영향을 미친다.

아래 그림은 네 개의 클래스로 이루어진 더 복잡한 클래스 계층 구조를 보여준다. 이 그림은 이 계층 구조에서 지정 초기화 메서드가 클래스 초기화의 "깔대기" 역할을 하여, 클래스 간의 상호 관계를 단순화하는 방식을 설명한다:

![](initializerDelegation02)


### 두 단계 초기화

Swift에서 클래스 초기화는 두 단계로 이루어진다. 첫 번째 단계에서는 클래스가 도입한 모든 저장 프로퍼티에 초기값을 할당한다. 모든 저장 프로퍼티의 초기 상태가 결정되면 두 번째 단계가 시작되며, 각 클래스는 새로운 인스턴스가 사용 준비가 되기 전에 저장 프로퍼티를 추가로 커스터마이징할 수 있다.

두 단계 초기화 프로세스는 초기화를 안전하게 만드는 동시에 클래스 계층 구조 내에서 각 클래스에 완전한 유연성을 제공한다. 이 방식은 프로퍼티 값이 초기화되기 전에 접근되는 것을 방지하고, 다른 초기화 메서드에 의해 예기치 않게 값이 변경되는 것을 막는다.

> 참고: Swift의 두 단계 초기화 프로세스는 Objective-C의 초기화와 유사하다. 주요 차이점은 첫 번째 단계에서 Objective-C는 모든 프로퍼티에 `0` 또는 `nil`과 같은 값을 할당한다는 점이다. Swift는 더 유연하게 초기화를 진행하며, 사용자가 커스텀 초기값을 설정할 수 있고, `0` 또는 `nil`이 유효한 기본값이 아닌 타입도 처리할 수 있다.

Swift 컴파일러는 두 단계 초기화가 오류 없이 완료되도록 네 가지 안전 검사를 수행한다:

- **안전 검사 1**: 지정 초기화 메서드는 클래스가 도입한 모든 프로퍼티가 초기화된 후에 상위 클래스 초기화 메서드로 위임해야 한다.

위에서 언급한 대로, 객체의 메모리는 모든 저장 프로퍼티의 초기 상태가 확인된 후에야 완전히 초기화된 것으로 간주된다. 이 규칙을 충족하려면 지정 초기화 메서드는 모든 프로퍼티가 초기화된 후에 상위 클래스 초기화 메서드로 위임해야 한다.

- **안전 검사 2**: 지정 초기화 메서드는 상속된 프로퍼티에 값을 할당하기 전에 상위 클래스 초기화 메서드로 위임해야 한다. 그렇지 않으면 지정 초기화 메서드가 할당한 새로운 값은 상위 클래스의 초기화 과정에서 덮어씌워질 수 있다.

- **안전 검사 3**: 편의 초기화 메서드는 모든 프로퍼티(동일 클래스에서 정의한 프로퍼티 포함)에 값을 할당하기 전에 다른 초기화 메서드로 위임해야 한다. 그렇지 않으면 편의 초기화 메서드가 할당한 새로운 값은 해당 클래스의 지정 초기화 메서드에 의해 덮어씌워질 수 있다.

- **안전 검사 4**: 초기화 메서드는 첫 번째 초기화 단계가 완료될 때까지 인스턴스 메서드를 호출하거나, 인스턴스 프로퍼티 값을 읽거나, `self`를 값으로 참조할 수 없다.

첫 번째 단계가 끝날 때까지 클래스 인스턴스는 완전히 유효하지 않다. 프로퍼티는 첫 번째 단계가 끝난 후에야 접근할 수 있고, 메서드는 첫 번째 단계가 끝난 후에야 호출할 수 있다.

위의 네 가지 안전 검사를 기반으로 두 단계 초기화가 어떻게 진행되는지 살펴보자.

**1단계**

- 클래스의 지정 초기화 메서드 또는 편의 초기화 메서드가 호출된다.
- 클래스의 새로운 인스턴스에 대한 메모리가 할당된다. 이 메모리는 아직 초기화되지 않았다.
- 클래스의 지정 초기화 메서드는 클래스가 도입한 모든 저장 프로퍼티가 값을 가지고 있는지 확인한다. 이 저장 프로퍼티의 메모리가 이제 초기화된다.
- 지정 초기화 메서드는 상위 클래스 초기화 메서드로 위임하여 동일한 작업을 수행한다.
- 이 과정은 클래스 상속 체인의 최상위에 도달할 때까지 계속된다.
- 체인의 최상위에 도달하고, 체인의 마지막 클래스가 모든 저장 프로퍼티가 값을 가지고 있는지 확인하면, 인스턴스의 메모리가 완전히 초기화된 것으로 간주되며 1단계가 완료된다.

**2단계**

- 체인의 최상위에서 다시 아래로 내려가며, 체인의 각 지정 초기화 메서드는 인스턴스를 추가로 커스터마이징할 수 있다. 이제 초기화 메서드는 `self`에 접근할 수 있고, 프로퍼티를 수정하거나 인스턴스 메서드를 호출할 수 있다.
- 마지막으로, 체인의 편의 초기화 메서드는 인스턴스를 커스터마이징하고 `self`를 사용할 수 있다.

다음은 가상의 하위 클래스와 상위 클래스에 대한 초기화 호출의 1단계를 보여준다:

![](twoPhaseInitialization01)

이 예제에서 초기화는 하위 클래스의 편의 초기화 메서드 호출로 시작된다. 이 편의 초기화 메서드는 아직 프로퍼티를 수정할 수 없다. 동일한 클래스의 지정 초기화 메서드로 위임한다.

지정 초기화 메서드는 안전 검사 1에 따라 하위 클래스의 모든 프로퍼티가 값을 가지고 있는지 확인한다. 그런 다음 상위 클래스의 지정 초기화 메서드를 호출하여 초기화를 계속한다.

상위 클래스의 지정 초기화 메서드는 상위 클래스의 모든 프로퍼티가 값을 가지고 있는지 확인한다. 더 이상 초기화할 상위 클래스가 없으므로 추가 위임이 필요하지 않다.

상위 클래스의 모든 프로퍼티가 초기값을 가지면 메모리가 완전히 초기화된 것으로 간주되며 1단계가 완료된다.

다음은 동일한 초기화 호출의 2단계를 보여준다:

![](twoPhaseInitialization02)

상위 클래스의 지정 초기화 메서드는 이제 인스턴스를 추가로 커스터마이징할 수 있다(필수는 아님).

상위 클래스의 지정 초기화 메서드가 완료되면, 하위 클래스의 지정 초기화 메서드도 추가 커스터마이징을 수행할 수 있다(필수는 아님).

마지막으로, 하위 클래스의 지정 초기화 메서드가 완료되면, 처음 호출된 편의 초기화 메서드가 추가 커스터마이징을 수행할 수 있다.


### 초기화 상속과 재정의

Objective-C의 서브클래스와 달리, Swift의 서브클래스는 기본적으로 슈퍼클래스의 초기화 메서드를 상속하지 않는다. 이는 슈퍼클래스의 간단한 초기화 메서드가 더 특수화된 서브클래스에 상속되어, 완전히 또는 올바르게 초기화되지 않은 서브클래스의 인스턴스를 생성하는 상황을 방지하기 위함이다.

> 주의: 특정 상황에서는 슈퍼클래스의 초기화 메서드가 상속되지만, 이는 안전하고 적절한 경우에만 해당한다. 자세한 내용은 아래 <doc:Initialization#Automatic-Initializer-Inheritance>를 참고한다.

커스텀 서브클래스가 슈퍼클래스와 동일한 초기화 메서드를 제공하려면, 서브클래스 내에서 해당 초기화 메서드를 직접 구현해야 한다.

서브클래스의 초기화 메서드가 슈퍼클래스의 **지정 초기화 메서드(designated initializer)**와 일치하면, 해당 지정 초기화 메서드를 재정의하는 것이다. 따라서 서브클래스의 초기화 메서드 정의 앞에 `override` 수식어를 반드시 붙여야 한다. 이는 <doc:Initialization#Default-Initializers>에서 설명한 것처럼, 자동으로 제공된 기본 초기화 메서드를 재정의하는 경우에도 마찬가지다.

재정의된 프로퍼티, 메서드, 서브스크립트와 마찬가지로, `override` 수식어는 Swift가 슈퍼클래스에 재정의할 지정 초기화 메서드가 있는지 확인하고, 재정의 초기화 메서드의 매개변수가 의도한 대로 지정되었는지 검증하도록 한다.

> 주의: 슈퍼클래스의 지정 초기화 메서드를 재정의할 때는 항상 `override` 수식어를 작성해야 한다. 서브클래스의 초기화 메서드 구현이 편의 초기화 메서드(convenience initializer)인 경우에도 마찬가지다.

반대로, 서브클래스의 초기화 메서드가 슈퍼클래스의 **편의 초기화 메서드(convenience initializer)**와 일치하면, 슈퍼클래스의 편의 초기화 메서드는 서브클래스에서 직접 호출할 수 없다. 따라서 서브클래스는 (엄밀히 말하면) 슈퍼클래스의 초기화 메서드를 재정의하는 것이 아니다. 결과적으로, 슈퍼클래스의 편의 초기화 메서드와 일치하는 구현을 제공할 때는 `override` 수식어를 작성하지 않는다.

아래 예제는 `Vehicle`이라는 기본 클래스를 정의한다. 이 클래스는 `numberOfWheels`라는 저장 프로퍼티를 선언하며, 기본값으로 `0`을 가진다. `numberOfWheels` 프로퍼티는 `description`이라는 계산 프로퍼티에서 사용되어 차량의 특성을 설명하는 `String`을 생성한다:

```swift
class Vehicle {
    var numberOfWheels = 0
    var description: String {
        return "\(numberOfWheels) wheel(s)"
    }
}
```

`Vehicle` 클래스는 유일한 저장 프로퍼티에 기본값을 제공하며, 커스텀 초기화 메서드를 직접 구현하지 않는다. 따라서 <doc:Initialization#Default-Initializers>에서 설명한 것처럼, 기본 초기화 메서드를 자동으로 받는다. 기본 초기화 메서드는 (사용 가능한 경우) 항상 클래스의 지정 초기화 메서드이며, `numberOfWheels`가 `0`인 새로운 `Vehicle` 인스턴스를 생성하는 데 사용할 수 있다:

```swift
let vehicle = Vehicle()
print("Vehicle: \(vehicle.description)")
// Vehicle: 0 wheel(s)
```

다음 예제는 `Vehicle`의 서브클래스인 `Bicycle`을 정의한다:

```swift
class Bicycle: Vehicle {
    override init() {
        super.init()
        numberOfWheels = 2
    }
}
```

`Bicycle` 서브클래스는 커스텀 지정 초기화 메서드인 `init()`을 정의한다. 이 지정 초기화 메서드는 `Bicycle`의 슈퍼클래스인 `Vehicle`의 지정 초기화 메서드와 일치하므로, `Bicycle` 버전의 초기화 메서드에는 `override` 수식어가 붙는다.

`Bicycle`의 `init()` 초기화 메서드는 `super.init()`을 호출하여 시작한다. 이는 `Bicycle` 클래스의 슈퍼클래스인 `Vehicle`의 기본 초기화 메서드를 호출한다. 이렇게 하면 `Bicycle`이 프로퍼티를 수정하기 전에 `Vehicle`이 상속된 `numberOfWheels` 프로퍼티를 초기화할 수 있다. `super.init()`을 호출한 후, `numberOfWheels`의 원래 값은 새로운 값인 `2`로 대체된다.

`Bicycle`의 인스턴스를 생성하면, 상속된 `description` 계산 프로퍼티를 호출하여 `numberOfWheels` 프로퍼티가 어떻게 업데이트되었는지 확인할 수 있다:

```swift
let bicycle = Bicycle()
print("Bicycle: \(bicycle.description)")
// Bicycle: 2 wheel(s)
```

서브클래스의 초기화 메서드가 초기화 프로세스의 2단계에서 아무런 커스터마이징을 수행하지 않고, 슈퍼클래스에 동기식이고 매개변수가 없는 지정 초기화 메서드가 있다면, 서브클래스의 모든 저장 프로퍼티에 값을 할당한 후 `super.init()` 호출을 생략할 수 있다. 슈퍼클래스의 초기화 메서드가 비동기식이라면, `await super.init()`을 명시적으로 작성해야 한다.

이 예제는 `Vehicle`의 또 다른 서브클래스인 `Hoverboard`를 정의한다. 초기화 메서드에서 `Hoverboard` 클래스는 `color` 프로퍼티만 설정한다. `super.init()`을 명시적으로 호출하는 대신, 이 초기화 메서드는 슈퍼클래스의 초기화 메서드를 암시적으로 호출하여 프로세스를 완료한다.

```swift
class Hoverboard: Vehicle {
    var color: String
    init(color: String) {
        self.color = color
        // super.init()이 여기서 암시적으로 호출됨
    }
    override var description: String {
        return "\(super.description) in a beautiful \(color)"
    }
}
```

`Hoverboard`의 인스턴스는 `Vehicle` 초기화 메서드에서 제공된 기본 바퀴 수를 사용한다.

```swift
let hoverboard = Hoverboard(color: "silver")
print("Hoverboard: \(hoverboard.description)")
// Hoverboard: 0 wheel(s) in a beautiful silver
```

> 주의: 서브클래스는 초기화 중에 상속된 변수 프로퍼티를 수정할 수 있지만, 상속된 상수 프로퍼티는 수정할 수 없다.


### 자동 초기화 상속

앞서 언급했듯이, 하위 클래스는 기본적으로 상위 클래스의 초기화 메서드를 상속받지 않는다. 하지만 특정 조건을 충족하면 상위 클래스의 초기화 메서드를 자동으로 상속받을 수 있다. 이는 실제로 많은 일반적인 상황에서 초기화 메서드를 재정의할 필요가 없고, 안전한 경우 최소한의 노력으로 상위 클래스의 초기화 메서드를 상속받을 수 있음을 의미한다.

하위 클래스에서 새로 추가한 프로퍼티에 기본값을 제공한다는 전제 하에, 다음 두 가지 규칙이 적용된다:

- **규칙 1**:  
  하위 클래스가 지정 초기화 메서드를 정의하지 않으면, 상위 클래스의 모든 지정 초기화 메서드를 자동으로 상속받는다.

- **규칙 2**:  
  하위 클래스가 상위 클래스의 모든 지정 초기화 메서드를 구현하면(규칙 1에 따라 상속받거나, 하위 클래스 정의의 일부로 커스텀 구현을 제공), 상위 클래스의 모든 편의 초기화 메서드를 자동으로 상속받는다.

이 규칙들은 하위 클래스가 추가적인 편의 초기화 메서드를 정의하는 경우에도 적용된다.

> 참고: 하위 클래스는 규칙 2를 충족하기 위해 상위 클래스의 지정 초기화 메서드를 하위 클래스의 편의 초기화 메서드로 구현할 수 있다.

<!--
  TODO: Beto의 피드백에 따르면 이 설명이 조금 이해하기 어렵다고 합니다.
  이 부분은 나중에 "실제 예제"에서 설명하는 것이 더 나을지 고민 중입니다.
  해당 원칙을 보여주는 예제를 통해 설명하는 게 더 명확할 수 있습니다.
-->

<!--
  TODO: 드물게 super.init() 호출을 자동으로 삽입하는 경우가 있습니다.
  언제 이런 일이 발생하는지 설명이 필요합니다. 어쨌든 이 부분을 여기에 언급해야 합니다.
-->


### 지정 이니셜라이저와 편의 이니셜라이저의 실제 활용

다음 예제는 지정 이니셜라이저, 편의 이니셜라이저, 그리고 자동 이니셜라이저 상속이 어떻게 동작하는지 보여준다. 이 예제에서는 `Food`, `RecipeIngredient`, `ShoppingListItem`이라는 세 클래스의 계층 구조를 정의하고, 이들의 이니셜라이저가 어떻게 상호작용하는지 설명한다.

계층 구조의 기본 클래스는 `Food`로, 음식의 이름을 캡슐화하는 간단한 클래스다. `Food` 클래스는 `name`이라는 단일 `String` 프로퍼티를 가지며, `Food` 인스턴스를 생성하기 위한 두 이니셜라이저를 제공한다:

```swift
class Food {
    var name: String
    init(name: String) {
        self.name = name
    }
    convenience init() {
        self.init(name: "[Unnamed]")
    }
}
```

<!--
  - test: `designatedConvenience`

  ```swifttest
  -> class Food {
        var name: String
        init(name: String) {
           self.name = name
        }
        convenience init() {
           self.init(name: "[Unnamed]")
        }
     }
  ```
-->

아래 그림은 `Food` 클래스의 이니셜라이저 체인을 보여준다:

![](initializersExample01)

클래스는 기본 멤버와이즈 이니셜라이저를 제공하지 않기 때문에, `Food` 클래스는 `name`이라는 단일 인자를 받는 지정 이니셜라이저를 제공한다. 이 이니셜라이저를 사용해 특정 이름을 가진 새로운 `Food` 인스턴스를 생성할 수 있다:

```swift
let namedMeat = Food(name: "Bacon")
// namedMeat의 name은 "Bacon"
```

<!--
  - test: `designatedConvenience`

  ```swifttest
  -> let namedMeat = Food(name: "Bacon")
  /> namedMeat's name is \"\(namedMeat.name)\"
  </ namedMeat's name is "Bacon"
  ```
-->

`Food` 클래스의 `init(name: String)` 이니셜라이저는 *지정* 이니셜라이저로, 새로운 `Food` 인스턴스의 모든 저장 프로퍼티가 완전히 초기화되도록 보장한다. `Food` 클래스는 슈퍼클래스를 가지지 않기 때문에, `init(name: String)` 이니셜라이저는 초기화를 완료하기 위해 `super.init()`을 호출할 필요가 없다.

`Food` 클래스는 또한 인자가 없는 *편의* 이니셜라이저인 `init()`을 제공한다. `init()` 이니셜라이저는 `name` 값으로 `[Unnamed]`를 전달하여 `Food` 클래스의 `init(name: String)` 이니셜라이저를 호출함으로써, 새로운 음식에 대한 기본 이름을 제공한다:

```swift
let mysteryMeat = Food()
// mysteryMeat의 name은 "[Unnamed]"
```

<!--
  - test: `designatedConvenience`

  ```swifttest
  -> let mysteryMeat = Food()
  /> mysteryMeat's name is \"\(mysteryMeat.name)\"
  </ mysteryMeat's name is "[Unnamed]"
  ```
-->

계층 구조의 두 번째 클래스는 `Food`의 서브클래스인 `RecipeIngredient`다. `RecipeIngredient` 클래스는 요리 재료를 모델링한다. 이 클래스는 `Food`로부터 상속받은 `name` 프로퍼티 외에 `quantity`라는 `Int` 프로퍼티를 추가하고, `RecipeIngredient` 인스턴스를 생성하기 위한 두 이니셜라이저를 정의한다:

```swift
class RecipeIngredient: Food {
    var quantity: Int
    init(name: String, quantity: Int) {
        self.quantity = quantity
        super.init(name: name)
    }
    override convenience init(name: String) {
        self.init(name: name, quantity: 1)
    }
}
```

<!--
  - test: `designatedConvenience`

  ```swifttest
  -> class RecipeIngredient: Food {
        var quantity: Int
        init(name: String, quantity: Int) {
           self.quantity = quantity
           super.init(name: name)
        }
        override convenience init(name: String) {
           self.init(name: name, quantity: 1)
        }
     }
  ```
-->

아래 그림은 `RecipeIngredient` 클래스의 이니셜라이저 체인을 보여준다:

![](initializersExample02)

`RecipeIngredient` 클래스는 단일 지정 이니셜라이저인 `init(name: String, quantity: Int)`를 가지며, 이를 통해 새로운 `RecipeIngredient` 인스턴스의 모든 프로퍼티를 초기화할 수 있다. 이 이니셜라이저는 전달된 `quantity` 인자를 `RecipeIngredient`가 추가한 유일한 프로퍼티인 `quantity`에 할당하는 것으로 시작한다. 이후 이 이니셜라이저는 `Food` 클래스의 `init(name: String)` 이니셜라이저를 호출한다. 이 과정은 <doc:Initialization#Two-Phase-Initialization>에서 설명한 안전 검사 1을 충족한다.

`RecipeIngredient`는 또한 `init(name: String)`이라는 편의 이니셜라이저를 정의한다. 이 편의 이니셜라이저는 이름만으로 `RecipeIngredient` 인스턴스를 생성할 때 사용된다. 이 편의 이니셜라이저는 명시적인 수량 없이 생성된 `RecipeIngredient` 인스턴스의 수량을 `1`로 가정한다. 이 편의 이니셜라이저를 정의함으로써, `RecipeIngredient` 인스턴스를 더 빠르고 편리하게 생성할 수 있으며, 여러 단일 수량의 `RecipeIngredient` 인스턴스를 생성할 때 코드 중복을 피할 수 있다. 이 편의 이니셜라이저는 단순히 클래스의 지정 이니셜라이저를 호출하며, `quantity` 값으로 `1`을 전달한다.

`RecipeIngredient`가 제공하는 `init(name: String)` 편의 이니셜라이저는 `Food`의 `init(name: String)` *지정* 이니셜라이저와 동일한 매개변수를 가진다. 이 편의 이니셜라이저는 슈퍼클래스의 지정 이니셜라이저를 오버라이드하기 때문에, `override` 수식어로 표시해야 한다 (이는 <doc:Initialization#Initializer-Inheritance-and-Overriding>에서 설명한 바와 같다).

비록 `RecipeIngredient`가 `init(name: String)` 이니셜라이저를 편의 이니셜라이저로 제공하지만, `RecipeIngredient`는 여전히 슈퍼클래스의 모든 지정 이니셜라이저를 구현했다. 따라서 `RecipeIngredient`는 슈퍼클래스의 모든 편의 이니셜라이저도 자동으로 상속받는다.

이 예제에서 `RecipeIngredient`의 슈퍼클래스는 `Food`이며, `Food`는 `init()`이라는 단일 편의 이니셜라이저를 가진다. 따라서 이 이니셜라이저는 `RecipeIngredient`에 의해 상속된다. 상속된 `init()` 이니셜라이저는 `Food` 버전과 정확히 동일하게 동작하지만, `Food` 버전 대신 `RecipeIngredient` 버전의 `init(name: String)`을 호출한다.

이 세 이니셜라이저를 모두 사용해 새로운 `RecipeIngredient` 인스턴스를 생성할 수 있다:

```swift
let oneMysteryItem = RecipeIngredient()
let oneBacon = RecipeIngredient(name: "Bacon")
let sixEggs = RecipeIngredient(name: "Eggs", quantity: 6)
```

<!--
  - test: `designatedConvenience`

  ```swifttest
  -> let oneMysteryItem = RecipeIngredient()
  -> let oneBacon = RecipeIngredient(name: "Bacon")
  -> let sixEggs = RecipeIngredient(name: "Eggs", quantity: 6)
  ```
-->

계층 구조의 세 번째이자 마지막 클래스는 `RecipeIngredient`의 서브클래스인 `ShoppingListItem`이다. `ShoppingListItem` 클래스는 쇼핑 리스트에 나타나는 요리 재료를 모델링한다.

쇼핑 리스트의 모든 항목은 "구매되지 않음" 상태로 시작한다. 이를 나타내기 위해 `ShoppingListItem`은 기본값이 `false`인 `purchased`라는 불리언 프로퍼티를 추가한다. 또한 `ShoppingListItem`은 `description`이라는 계산 프로퍼티를 추가하는데, 이 프로퍼티는 `ShoppingListItem` 인스턴스에 대한 텍스트 설명을 제공한다:

```swift
class ShoppingListItem: RecipeIngredient {
    var purchased = false
    var description: String {
        var output = "\(quantity) x \(name)"
        output += purchased ? " ✔" : " ✘"
        return output
    }
}
```

<!--
  - test: `designatedConvenience`

  ```swifttest
  -> class ShoppingListItem: RecipeIngredient {
        var purchased = false
        var description: String {
           var output = "\(quantity) x \(name)"
           output += purchased ? " ✔" : " ✘"
           return output
        }
     }
  ```
-->

> 참고: `ShoppingListItem`은 `purchased`에 대한 초기값을 제공하기 위해 이니셜라이저를 정의하지 않는다. 여기서 모델링한 쇼핑 리스트의 항목은 항상 "구매되지 않음" 상태로 시작하기 때문이다.

`ShoppingListItem`은 추가한 모든 프로퍼티에 기본값을 제공하고, 이니셜라이저를 직접 정의하지 않기 때문에, 슈퍼클래스의 *모든* 지정 이니셜라이저와 편의 이니셜라이저를 자동으로 상속받는다.

아래 그림은 세 클래스의 전체 이니셜라이저 체인을 보여준다:

![](initializersExample03)

상속받은 세 이니셜라이저를 모두 사용해 새로운 `ShoppingListItem` 인스턴스를 생성할 수 있다:

```swift
var breakfastList = [
    ShoppingListItem(),
    ShoppingListItem(name: "Bacon"),
    ShoppingListItem(name: "Eggs", quantity: 6),
]
breakfastList[0].name = "Orange juice"
breakfastList[0].purchased = true
for item in breakfastList {
    print(item.description)
}
// 1 x Orange juice ✔
// 1 x Bacon ✘
// 6 x Eggs ✘
```

<!--
  - test: `designatedConvenience`

  ```swifttest
  -> var breakfastList = [
        ShoppingListItem(),
        ShoppingListItem(name: "Bacon"),
        ShoppingListItem(name: "Eggs", quantity: 6),
     ]
  -> breakfastList[0].name = "Orange juice"
  -> breakfastList[0].purchased = true
  -> for item in breakfastList {
        print(item.description)
     }
  </ 1 x Orange juice ✔
  </ 1 x Bacon ✘
  </ 6 x Eggs ✘
  ```
-->

여기서 `breakfastList`라는 새로운 배열은 세 개의 새로운 `ShoppingListItem` 인스턴스를 포함하는 배열 리터럴로 생성된다. 배열의 타입은 `[ShoppingListItem]`으로 추론된다. 배열이 생성된 후, 배열의 첫 번째 `ShoppingListItem`의 이름이 `"[Unnamed]"`에서 `"Orange juice"`로 변경되고, 구매된 것으로 표시된다. 배열의 각 항목에 대한 설명을 출력하면, 기본 상태가 예상대로 설정되었음을 확인할 수 있다.


## 실패 가능한 이니셜라이저

클래스, 구조체, 열거형을 정의할 때 초기화가 실패할 수 있는 상황을 고려해야 할 때가 있다. 이는 잘못된 초기화 매개변수 값, 필요한 외부 리소스의 부재, 또는 초기화를 성공적으로 완료할 수 없는 다른 조건에 의해 발생할 수 있다.

초기화가 실패할 수 있는 상황을 처리하기 위해, 클래스, 구조체, 열거형 정의 내에 하나 이상의 실패 가능한 이니셜라이저를 정의할 수 있다. 실패 가능한 이니셜라이저는 `init` 키워드 뒤에 물음표를 붙여서 작성한다(`init?`).

> 참고: 동일한 매개변수 타입과 이름을 가진 실패 가능한 이니셜라이저와 실패 불가능한 이니셜라이저를 동시에 정의할 수 없다.

<!--
  - test: `failableAndNonFailableInitializersCannotMatch`

  ```swifttest
  -> struct S {
        let s: String
        init(s: String) { self.s = s }
        init?(s: String) { self.s = s }
     }
  !$ error: invalid redeclaration of 'init(s:)'
  !!            init?(s: String) { self.s = s }
  !!            ^
  !$ note: 'init(s:)' previously declared here
  !!            init(s: String) { self.s = s }
  !!            ^
  ```
-->

실패 가능한 이니셜라이저는 초기화하는 타입의 옵셔널 값을 생성한다. 초기화가 실패할 수 있는 지점을 나타내기 위해 이니셜라이저 내부에서 `return nil`을 사용한다.

> 참고: 엄밀히 말하면, 이니셜라이저는 값을 반환하지 않는다. 이니셜라이저의 역할은 초기화가 끝날 때 `self`가 완전하고 올바르게 초기화되도록 보장하는 것이다. 초기화 실패를 나타내기 위해 `return nil`을 사용하지만, 초기화 성공을 나타내기 위해 `return` 키워드를 사용하지는 않는다.

예를 들어, 숫자 타입 변환을 위해 실패 가능한 이니셜라이저가 구현될 수 있다. 숫자 타입 간의 변환에서 값을 정확히 유지하기 위해 `init(exactly:)` 이니셜라이저를 사용한다. 타입 변환이 값을 유지할 수 없는 경우, 이니셜라이저는 실패한다.

```swift
let wholeNumber: Double = 12345.0
let pi = 3.14159

if let valueMaintained = Int(exactly: wholeNumber) {
    print("\(wholeNumber) conversion to Int maintains value of \(valueMaintained)")
}
// Prints "12345.0 conversion to Int maintains value of 12345"

let valueChanged = Int(exactly: pi)
// valueChanged is of type Int?, not Int

if valueChanged == nil {
    print("\(pi) conversion to Int doesn't maintain value")
}
// Prints "3.14159 conversion to Int doesn't maintain value"
```

<!--
  - test: `failableInitializers`

  ```swifttest
  -> let wholeNumber: Double = 12345.0
  -> let pi = 3.14159

  -> if let valueMaintained = Int(exactly: wholeNumber) {
         print("\(wholeNumber) conversion to Int maintains value of \(valueMaintained)")
     }
  <- 12345.0 conversion to Int maintains value of 12345

  -> let valueChanged = Int(exactly: pi)
  // valueChanged is of type Int?, not Int

  -> if valueChanged == nil {
         print("\(pi) conversion to Int doesn't maintain value")
     }
  <- 3.14159 conversion to Int doesn't maintain value
  ```
-->

아래 예제는 `species`라는 상수 `String` 프로퍼티를 가진 `Animal` 구조체를 정의한다. `Animal` 구조체는 `species`라는 단일 매개변수를 받는 실패 가능한 이니셜라이저도 정의한다. 이 이니셜라이저는 전달된 `species` 값이 빈 문자열인지 확인한다. 빈 문자열이 발견되면 초기화가 실패한다. 그렇지 않으면 `species` 프로퍼티의 값이 설정되고 초기화가 성공한다:

```swift
struct Animal {
    let species: String
    init?(species: String) {
        if species.isEmpty { return nil }
        self.species = species
    }
}
```

<!--
  - test: `failableInitializers`

  ```swifttest
  -> struct Animal {
        let species: String
        init?(species: String) {
           if species.isEmpty { return nil }
           self.species = species
        }
     }
  ```
-->

이 실패 가능한 이니셜라이저를 사용해 새로운 `Animal` 인스턴스를 초기화하고 초기화가 성공했는지 확인할 수 있다:

```swift
let someCreature = Animal(species: "Giraffe")
// someCreature is of type Animal?, not Animal

if let giraffe = someCreature {
    print("An animal was initialized with a species of \(giraffe.species)")
}
// Prints "An animal was initialized with a species of Giraffe"
```

<!--
  - test: `failableInitializers`

  ```swifttest
  -> let someCreature = Animal(species: "Giraffe")
  // someCreature is of type Animal?, not Animal

  -> if let giraffe = someCreature {
        print("An animal was initialized with a species of \(giraffe.species)")
     }
  <- An animal was initialized with a species of Giraffe
  ```
-->

실패 가능한 이니셜라이저의 `species` 매개변수에 빈 문자열 값을 전달하면, 이니셜라이저는 초기화 실패를 트리거한다:

```swift
let anonymousCreature = Animal(species: "")
// anonymousCreature is of type Animal?, not Animal

if anonymousCreature == nil {
    print("The anonymous creature couldn't be initialized")
}
// Prints "The anonymous creature couldn't be initialized"
```

<!--
  - test: `failableInitializers`

  ```swifttest
  -> let anonymousCreature = Animal(species: "")
  // anonymousCreature is of type Animal?, not Animal

  -> if anonymousCreature == nil {
        print("The anonymous creature couldn't be initialized")
     }
  <- The anonymous creature couldn't be initialized
  ```
-->

> 참고: 빈 문자열 값(예: `""`)을 확인하는 것은 옵셔널 `String` 값의 부재를 나타내는 `nil`을 확인하는 것과 다르다. 위 예제에서 빈 문자열(`""`)은 유효한, 옵셔널이 아닌 `String` 값이다. 그러나 동물이 `species` 프로퍼티의 값으로 빈 문자열을 갖는 것은 적절하지 않다. 이 제약을 모델링하기 위해, 실패 가능한 이니셜라이저는 빈 문자열이 발견되면 초기화 실패를 트리거한다.


### 열거형의 실패 가능 초기화

실패 가능 초기화를 사용하면 하나 이상의 매개변수에 따라 적절한 열거형 케이스를 선택할 수 있다. 제공된 매개변수가 적절한 열거형 케이스와 일치하지 않으면 초기화가 실패할 수 있다.

아래 예제는 `TemperatureUnit`이라는 열거형을 정의한다. 이 열거형은 세 가지 가능한 상태(`kelvin`, `celsius`, `fahrenheit`)를 가진다. 실패 가능 초기화는 온도 기호를 나타내는 `Character` 값에 대해 적절한 열거형 케이스를 찾는 데 사용된다:

```swift
enum TemperatureUnit {
    case kelvin, celsius, fahrenheit
    init?(symbol: Character) {
        switch symbol {
        case "K":
            self = .kelvin
        case "C":
            self = .celsius
        case "F":
            self = .fahrenheit
        default:
            return nil
        }
    }
}
```

<!--
  - test: `failableInitializers`

  ```swifttest
  -> enum TemperatureUnit {
        case kelvin, celsius, fahrenheit
        init?(symbol: Character) {
           switch symbol {
              case "K":
                 self = .kelvin
              case "C":
                 self = .celsius
              case "F":
                 self = .fahrenheit
              default:
                 return nil
           }
        }
     }
  ```
-->

이 실패 가능 초기화를 사용하여 세 가지 가능한 상태에 대해 적절한 열거형 케이스를 선택할 수 있다. 매개변수가 이 상태 중 하나와 일치하지 않으면 초기화가 실패한다:

```swift
let fahrenheitUnit = TemperatureUnit(symbol: "F")
if fahrenheitUnit != nil {
    print("This is a defined temperature unit, so initialization succeeded.")
}
// Prints "This is a defined temperature unit, so initialization succeeded."

let unknownUnit = TemperatureUnit(symbol: "X")
if unknownUnit == nil {
    print("This isn't a defined temperature unit, so initialization failed.")
}
// Prints "This isn't a defined temperature unit, so initialization failed."
```

<!--
  - test: `failableInitializers`

  ```swifttest
  -> let fahrenheitUnit = TemperatureUnit(symbol: "F")
  -> if fahrenheitUnit != nil {
        print("This is a defined temperature unit, so initialization succeeded.")
     }
  <- This is a defined temperature unit, so initialization succeeded.

  -> let unknownUnit = TemperatureUnit(symbol: "X")
  -> if unknownUnit == nil {
        print("This isn't a defined temperature unit, so initialization failed.")
     }
  <- This isn't a defined temperature unit, so initialization failed.
  ```
-->


### 원시 값을 가진 열거형의 실패 가능 초기화

원시 값을 가진 열거형은 자동으로 실패 가능 초기화 메서드 `init?(rawValue:)`를 제공한다. 이 메서드는 적절한 원시 값 타입의 `rawValue` 매개변수를 받아, 일치하는 열거형 케이스를 찾으면 해당 케이스를 선택하고, 일치하는 값이 없으면 초기화에 실패한다.

앞서 살펴본 `TemperatureUnit` 예제를 `Character` 타입의 원시 값을 사용하도록 수정하고, `init?(rawValue:)` 초기화 메서드를 활용할 수 있다:

```swift
enum TemperatureUnit: Character {
    case kelvin = "K", celsius = "C", fahrenheit = "F"
}

let fahrenheitUnit = TemperatureUnit(rawValue: "F")
if fahrenheitUnit != nil {
    print("This is a defined temperature unit, so initialization succeeded.")
}
// Prints "This is a defined temperature unit, so initialization succeeded."

let unknownUnit = TemperatureUnit(rawValue: "X")
if unknownUnit == nil {
    print("This isn't a defined temperature unit, so initialization failed.")
}
// Prints "This isn't a defined temperature unit, so initialization failed."
```

<!--
  - test: `failableInitializersForEnumerations`

  ```swifttest
  -> enum TemperatureUnit: Character {
        case kelvin = "K", celsius = "C", fahrenheit = "F"
     }

  -> let fahrenheitUnit = TemperatureUnit(rawValue: "F")
  -> if fahrenheitUnit != nil {
        print("This is a defined temperature unit, so initialization succeeded.")
     }
  <- This is a defined temperature unit, so initialization succeeded.

  -> let unknownUnit = TemperatureUnit(rawValue: "X")
  -> if unknownUnit == nil {
        print("This isn't a defined temperature unit, so initialization failed.")
     }
  <- This isn't a defined temperature unit, so initialization failed.
  ```
-->


### 초기화 실패의 전파

클래스, 구조체, 열거형의 실패 가능 초기화 메서드는 동일한 클래스, 구조체, 열거형 내의 다른 실패 가능 초기화 메서드로 위임할 수 있다. 마찬가지로, 하위 클래스의 실패 가능 초기화 메서드는 상위 클래스의 실패 가능 초기화 메서드로 위임할 수 있다.

두 경우 모두, 초기화를 실패하게 만드는 다른 초기화 메서드로 위임하면 초기화 프로세스가 즉시 실패하며, 이후의 초기화 코드는 실행되지 않는다.

<!--
  - test: `delegatingAcrossInAStructurePropagatesInitializationFailureImmediately`

  ```swifttest
  -> struct S {
        init?(string1: String) {
           self.init(string2: string1)
           print("Hello!") // 이 코드는 실행되지 않음. 초기화가 이미 실패했기 때문
        }
        init?(string2: String) { return nil }
     }
  -> let s = S(string1: "bing")
  -> assert(s == nil)
  ```
-->

<!--
  - test: `delegatingAcrossInAClassPropagatesInitializationFailureImmediately`

  ```swifttest
  -> class C {
        convenience init?(string1: String) {
           self.init(string2: string1)
           print("Hello!") // 이 코드는 실행되지 않음. 초기화가 이미 실패했기 때문
        }
        init?(string2: String) { return nil }
     }
  -> let c = C(string1: "bing")
  -> assert(c == nil)
  ```
-->

<!--
  - test: `delegatingUpInAClassPropagatesInitializationFailureImmediately`

  ```swifttest
  -> class C {
        init?(string1: String) { return nil }
     }
  -> class D: C {
        init?(string2: String) {
           super.init(string1: string2)
           print("Hello!") // 이 코드는 실행되지 않음. 초기화가 이미 실패했기 때문
        }
     }
  -> let d = D(string2: "bing")
  -> assert(d == nil)
  ```
-->

> 참고: 실패 가능 초기화 메서드는 실패하지 않는 초기화 메서드로도 위임할 수 있다. 기존의 실패하지 않는 초기화 프로세스에 실패 가능 상태를 추가해야 할 때 이 방식을 사용한다.

아래 예제는 `Product` 클래스의 하위 클래스인 `CartItem`을 정의한다. `CartItem` 클래스는 온라인 쇼핑 카트의 항목을 모델링한다. `CartItem`은 `quantity`라는 저장 상수 프로퍼티를 도입하고, 이 프로퍼티의 값이 항상 `1` 이상이 되도록 보장한다:

```swift
class Product {
    let name: String
    init?(name: String) {
        if name.isEmpty { return nil }
        self.name = name
    }
}

class CartItem: Product {
    let quantity: Int
    init?(name: String, quantity: Int) {
        if quantity < 1 { return nil }
        self.quantity = quantity
        super.init(name: name)
    }
}
```

<!--
  - test: `failableInitializers`

  ```swifttest
  -> class Product {
        let name: String
        init?(name: String) {
           if name.isEmpty { return nil }
           self.name = name
        }
     }
  >> let p = Product(name: "")

  -> class CartItem: Product {
        let quantity: Int
        init?(name: String, quantity: Int) {
           if quantity < 1 { return nil }
           self.quantity = quantity
           super.init(name: name)
        }
     }
  ```
-->

`CartItem`의 실패 가능 초기화 메서드는 먼저 `quantity` 값이 `1` 이상인지 검증한다. `quantity` 값이 유효하지 않으면 초기화 프로세스가 즉시 실패하며, 이후의 초기화 코드는 실행되지 않는다. 마찬가지로, `Product`의 실패 가능 초기화 메서드는 `name` 값을 검사하고, `name`이 빈 문자열이면 초기화 프로세스가 즉시 실패한다.

`CartItem` 인스턴스를 빈 문자열이 아닌 이름과 `1` 이상의 `quantity` 값으로 생성하면 초기화가 성공한다:

```swift
if let twoSocks = CartItem(name: "sock", quantity: 2) {
    print("Item: \(twoSocks.name), quantity: \(twoSocks.quantity)")
}
// 출력: "Item: sock, quantity: 2"
```

<!--
  - test: `failableInitializers`

  ```swifttest
  -> if let twoSocks = CartItem(name: "sock", quantity: 2) {
        print("Item: \(twoSocks.name), quantity: \(twoSocks.quantity)")
     }
  <- Item: sock, quantity: 2
  ```
-->

`quantity` 값이 `0`인 `CartItem` 인스턴스를 생성하려고 하면, `CartItem` 초기화 메서드가 초기화를 실패하게 만든다:

```swift
if let zeroShirts = CartItem(name: "shirt", quantity: 0) {
    print("Item: \(zeroShirts.name), quantity: \(zeroShirts.quantity)")
} else {
    print("Unable to initialize zero shirts")
}
// 출력: "Unable to initialize zero shirts"
```

<!--
  - test: `failableInitializers`

  ```swifttest
  -> if let zeroShirts = CartItem(name: "shirt", quantity: 0) {
        print("Item: \(zeroShirts.name), quantity: \(zeroShirts.quantity)")
     } else {
        print("Unable to initialize zero shirts")
     }
  <- Unable to initialize zero shirts
  ```
-->

마찬가지로, 빈 문자열인 `name` 값으로 `CartItem` 인스턴스를 생성하려고 하면, 상위 클래스인 `Product`의 초기화 메서드가 초기화를 실패하게 만든다:

```swift
if let oneUnnamed = CartItem(name: "", quantity: 1) {
    print("Item: \(oneUnnamed.name), quantity: \(oneUnnamed.quantity)")
} else {
    print("Unable to initialize one unnamed product")
}
// 출력: "Unable to initialize one unnamed product"
```

<!--
  - test: `failableInitializers`

  ```swifttest
  -> if let oneUnnamed = CartItem(name: "", quantity: 1) {
        print("Item: \(oneUnnamed.name), quantity: \(oneUnnamed.quantity)")
     } else {
        print("Unable to initialize one unnamed product")
     }
  <- Unable to initialize one unnamed product
  ```
-->


### 실패 가능한 이니셜라이저 오버라이딩

서브클래스에서 슈퍼클래스의 실패 가능한 이니셜라이저를 오버라이드할 수 있다. 이는 다른 이니셜라이저를 오버라이드하는 것과 동일하다. 또는 슈퍼클래스의 실패 가능한 이니셜라이저를 서브클래스의 **실패 불가능한** 이니셜라이저로 오버라이드할 수도 있다. 이를 통해 슈퍼클래스의 초기화가 실패할 수 있더라도, 서브클래스의 초기화는 실패하지 않도록 정의할 수 있다.

실패 가능한 슈퍼클래스 이니셜라이저를 실패 불가능한 서브클래스 이니셜라이저로 오버라이드하는 경우, 슈퍼클래스 이니셜라이저를 호출하려면 실패 가능한 슈퍼클래스 이니셜라이저의 결과를 강제 언래핑해야 한다.

> 참고: 실패 가능한 이니셜라이저를 실패 불가능한 이니셜라이저로 오버라이드할 수 있지만, 그 반대는 불가능하다.

<!--
  - test: `youCannotOverrideANonFailableInitializerWithAFailableInitializer`

  ```swifttest
  -> class C {
        init() {}
     }
  -> class D: C {
        override init?() {}
     }
  !$ error: failable initializer 'init()' cannot override a non-failable initializer
  !!            override init?() {}
  !!                     ^
  !$ note: non-failable initializer 'init()' overridden here
  !!            init() {}
  !!            ^
  ```
-->

아래 예제는 `Document`라는 클래스를 정의한다. 이 클래스는 `name` 프로퍼티가 비어 있지 않은 문자열 값이거나 `nil`일 때 초기화되는 문서를 모델링한다. 하지만 빈 문자열은 허용하지 않는다.

```swift
class Document {
    var name: String?
    // 이 이니셜라이저는 name 값이 nil인 문서를 생성한다
    init() {}
    // 이 이니셜라이저는 name 값이 비어 있지 않은 문자열인 문서를 생성한다
    init?(name: String) {
        if name.isEmpty { return nil }
        self.name = name
    }
}
```

<!--
  - test: `failableInitializers`

  ```swifttest
  -> class Document {
        var name: String?
        // 이 이니셜라이저는 name 값이 nil인 문서를 생성한다
        init() {}
        // 이 이니셜라이저는 name 값이 비어 있지 않은 문자열인 문서를 생성한다
        init?(name: String) {
           if name.isEmpty { return nil }
           self.name = name
        }
     }
  ```
-->

다음 예제는 `Document`의 서브클래스인 `AutomaticallyNamedDocument`를 정의한다. `AutomaticallyNamedDocument` 서브클래스는 `Document`에서 도입한 모든 지정 이니셜라이저를 오버라이드한다. 이 오버라이드는 `AutomaticallyNamedDocument` 인스턴스가 이름 없이 초기화되거나 `init(name:)` 이니셜라이저에 빈 문자열이 전달된 경우, 초기 `name` 값을 `"[Untitled]"`로 설정한다.

```swift
class AutomaticallyNamedDocument: Document {
    override init() {
        super.init()
        self.name = "[Untitled]"
    }
    override init(name: String) {
        super.init()
        if name.isEmpty {
            self.name = "[Untitled]"
        } else {
            self.name = name
        }
    }
}
```

<!--
  - test: `failableInitializers`

  ```swifttest
  -> class AutomaticallyNamedDocument: Document {
        override init() {
           super.init()
           self.name = "[Untitled]"
        }
        override init(name: String) {
           super.init()
           if name.isEmpty {
              self.name = "[Untitled]"
           } else {
              self.name = name
           }
        }
     }
  ```
-->

`AutomaticallyNamedDocument`는 슈퍼클래스의 실패 가능한 `init?(name:)` 이니셜라이저를 실패 불가능한 `init(name:)` 이니셜라이저로 오버라이드한다. `AutomaticallyNamedDocument`는 빈 문자열 케이스를 슈퍼클래스와 다른 방식으로 처리하므로, 이니셜라이저가 실패할 필요가 없으며, 실패 불가능한 버전의 이니셜라이저를 제공한다.

이니셜라이저 내에서 강제 언래핑을 사용해 슈퍼클래스의 실패 가능한 이니셜라이저를 호출할 수 있다. 이를 통해 서브클래스의 실패 불가능한 이니셜라이저를 구현할 수 있다. 예를 들어, 아래의 `UntitledDocument` 서브클래스는 항상 `"[Untitled]"`라는 이름을 가지며, 초기화 과정에서 슈퍼클래스의 실패 가능한 `init(name:)` 이니셜라이저를 사용한다.

```swift
class UntitledDocument: Document {
    override init() {
        super.init(name: "[Untitled]")!
    }
}
```

<!--
  - test: `failableInitializers`

  ```swifttest
  -> class UntitledDocument: Document {
        override init() {
           super.init(name: "[Untitled]")!
        }
     }
  ```
-->

이 경우, 슈퍼클래스의 `init(name:)` 이니셜라이저에 빈 문자열이 전달되면 강제 언래핑 연산으로 인해 런타임 오류가 발생한다. 하지만 문자열 리터럴을 사용해 호출하므로, 이니셜라이저가 실패하지 않음을 알 수 있으며, 이 경우 런타임 오류가 발생하지 않는다.


### 실패 가능 초기화 구문: init!

일반적으로 실패 가능 초기화 구문을 정의할 때는 `init` 키워드 뒤에 물음표(`init?`)를 붙여 적절한 타입의 옵셔널 인스턴스를 생성한다. 반대로, `init` 키워드 뒤에 느낌표(`init!`)를 붙여 적절한 타입의 암시적 언래핑 옵셔널 인스턴스를 생성하는 초기화 구문을 정의할 수도 있다.

`init?`에서 `init!`로, 또는 `init!`에서 `init?`로 위임할 수 있다. 또한 `init?`를 `init!`로, 또는 `init!`를 `init?`로 재정의할 수도 있다. `init`에서 `init!`로 위임하는 것도 가능하지만, 이 경우 `init!` 초기화 구문이 실패하면 어설션이 발생한다.

<!--
  - test: `structuresCanDelegateAcrossFromOptionalToIUO`

  ```swifttest
  -> struct S {
        init?(optional: Int) { self.init(iuo: optional) }
        init!(iuo: Int) {}
     }
  ```
-->

<!--
  - test: `structuresCanDelegateAcrossFromIUOToOptional`

  ```swifttest
  -> struct S {
        init!(iuo: Int) { self.init(optional: iuo) }
        init?(optional: Int) {}
     }
  ```
-->

<!--
  - test: `classesCanDelegateAcrossFromOptionalToIUO`

  ```swifttest
  -> class C {
        convenience init?(optional: Int) { self.init(iuo: optional) }
        init!(iuo: Int) {}
     }
  ```
-->

<!--
  - test: `classesCanDelegateAcrossFromIUOToOptional`

  ```swifttest
  -> class C {
        convenience init!(iuo: Int) { self.init(optional: iuo) }
        init?(optional: Int) {}
     }
  ```
-->

<!--
  - test: `classesCanDelegateUpFromOptionalToIUO`

  ```swifttest
  -> class C {
        init!(iuo: Int) {}
     }
  -> class D: C {
        init?(optional: Int) { super.init(iuo: optional) }
     }
  ```
-->

<!--
  - test: `classesCanDelegateUpFromIUOToOptional`

  ```swifttest
  -> class C {
        init?(optional: Int) {}
     }
  -> class D: C {
        init!(iuo: Int) { super.init(optional: iuo) }
     }
  ```
-->

<!--
  - test: `classesCanOverrideOptionalWithIUO`

  ```swifttest
  -> class C {
        init?(i: Int) {}
     }
  -> class D: C {
        override init!(i: Int) { super.init(i: i) }
     }
  ```
-->

<!--
  - test: `classesCanOverrideIUOWithOptional`

  ```swifttest
  -> class C {
        init!(i: Int) {}
     }
  -> class D: C {
        override init?(i: Int) { super.init(i: i) }
     }
  ```
-->

<!--
  - test: `structuresCanDelegateAcrossFromNonFailingToIUO`

  ```swifttest
  -> struct S {
        init(nonFailing: Int) { self.init(iuo: nonFailing) }
        init!(iuo: Int) {}
     }
  ```
-->

<!--
  - test: `classesCanDelegateAcrossFromNonFailingToIUO`

  ```swifttest
  -> class C {
        convenience init(nonFailing: Int) { self.init(iuo: nonFailing) }
        init!(iuo: Int) {}
     }
  ```
-->

<!--
  - test: `classesCanDelegateUpFromNonFailingToIUO`

  ```swifttest
  -> class C {
        init!(iuo: Int) {}
     }
  -> class D: C {
        init(nonFailing: Int) { super.init(iuo: nonFailing) }
     }
  ```
-->

<!--
  - test: `structuresAssertWhenDelegatingAcrossFromNonFailingToNilIUO`

  ```swifttest
  -> struct S {
        init(nonFailing: Int) { self.init(iuo: nonFailing) }
        init!(iuo: Int) { return nil }
     }
  -> let s = S(nonFailing: 42)
  xx assertion
  ```
-->

<!--
  - test: `classesAssertWhenDelegatingAcrossFromNonFailingToNilIUO`

  ```swifttest
  -> class C {
        convenience init(nonFailing: Int) { self.init(iuo: nonFailing) }
        init!(iuo: Int) { return nil }
     }
  -> let c = C(nonFailing: 42)
  xx assertion
  ```
-->

<!--
  - test: `classesAssertWhenDelegatingUpFromNonFailingToNilIUO`

  ```swifttest
  -> class C {
        init!(iuo: Int) { return nil }
     }
  -> class D: C {
        init(nonFailing: Int) { super.init(iuo: nonFailing) }
     }
  -> let d = D(nonFailing: 42)
  xx assertion
  ```
-->


## 필수 이니셜라이저

클래스 이니셜라이저 정의 앞에 `required` 수식어를 붙이면, 해당 클래스의 모든 서브클래스가 반드시 이 이니셜라이저를 구현해야 함을 나타낸다:

```swift
class SomeClass {
    required init() {
        // 이니셜라이저 구현
    }
}
```

<!--
  - test: `requiredInitializers`

  ```swifttest
  -> class SomeClass {
        required init() {
           // 이니셜라이저 구현
        }
     }
  ```
-->

<!--
  - test: `requiredDesignatedInitializersMustBeImplementedBySubclasses`

  ```swifttest
  -> class C {
        required init(i: Int) {}
     }
  -> class D: C {
        init() {}
     }
  !$ error: 'C' 클래스의 서브클래스는 'required' 이니셜라이저 'init(i:)'를 제공해야 함
  !! }
  !! ^
  !$ note: 'required' 이니셜라이저는 여기서 선언됨
  !!    required init(i: Int) {}
  !!             ^
  ```
-->

<!--
  - test: `requiredConvenienceInitializersMustBeImplementedBySubclasses`

  ```swifttest
  -> class C {
        init() {}
        required convenience init(i: Int) {
           self.init()
        }
     }
  -> class D: C {
        init(s: String) {}
     }
  !$ error: 'C' 클래스의 서브클래스는 'required' 이니셜라이저 'init(i:)'를 제공해야 함
  !! }
  !! ^
  !$ note: 'required' 이니셜라이저는 여기서 선언됨
  !!    required convenience init(i: Int) {
  !!                         ^
  ```
-->

필수 이니셜라이저를 서브클래스에서 구현할 때도 `required` 수식어를 반드시 붙여야 한다. 이는 이니셜라이저 요구사항이 더 하위의 서브클래스 체인까지 적용됨을 나타낸다. 필수 지정 이니셜라이저를 오버라이드할 때는 `override` 수식어를 붙이지 않는다:

```swift
class SomeSubclass: SomeClass {
    required init() {
        // 필수 이니셜라이저의 서브클래스 구현
    }
}
```

<!--
  - test: `requiredInitializers`

  ```swifttest
  -> class SomeSubclass: SomeClass {
        required init() {
           // 필수 이니셜라이저의 서브클래스 구현
        }
     }
  ```
-->

<!--
  - test: `youCannotWriteOverrideWhenOverridingARequiredDesignatedInitializer`

  ```swifttest
  -> class C {
        required init() {}
     }
  -> class D: C {
        override required init() {}
     }
  !$ warning: 필수 이니셜라이저를 오버라이드할 때 'override'는 암시적으로 적용됨
  !!    override required init() {}
  !! ~~~~~~~~~         ^
  !!-
  !$ note: 오버라이드된 필수 이니셜라이저는 여기에 선언됨
  !!    required init() {}
  !!             ^
  ```
-->

> 참고: 상속된 이니셜라이저로 요구사항을 충족할 수 있다면, 필수 이니셜라이저를 명시적으로 구현할 필요가 없다.

<!--
  - test: `youCanSatisfyARequiredDesignatedInitializerWithAnInheritedInitializer`

  ```swifttest
  -> class C {
        var x = 0
        required init(i: Int) {}
     }
  -> class D: C {
        var y = 0
     }
  ```
-->

<!--
  - test: `youCanSatisfyARequiredConvenienceInitializerWithAnInheritedInitializer`

  ```swifttest
  -> class C {
        var x = 0
        init(i: Int) {}
        required convenience init() {
           self.init(i: 42)
        }
     }
  -> class D: C {
        var y = 0
     }
  ```
-->

<!--
  FIXME: 이 섹션은 아직 필수 이니셜라이저가 왜 유용한지 설명하지 않음.
  이니셜라이저 요구사항이 있는 프로토콜 타입의 메타타입을 통해 생성할 때 유용함.
  이전에는 이 기능이 동작하지 않았음:
  <rdar://problem/13695680> 프로토콜의 생성자 요구사항 (NSCoding에 필요).
  2015년 초에 이 버그가 수정됨.
  프로토콜 챕터 소개의 해당 FIXME도 참고.
-->


## 클로저나 함수를 사용해 기본 프로퍼티 값 설정하기

저장 프로퍼티의 기본값에 특정한 설정이나 초기화가 필요하다면, 클로저나 전역 함수를 사용해 프로퍼티에 맞춤 기본값을 제공할 수 있다. 프로퍼티가 속한 타입의 새 인스턴스가 초기화될 때마다 클로저나 함수가 호출되고, 반환된 값이 프로퍼티의 기본값으로 할당된다.

이런 종류의 클로저나 함수는 일반적으로 프로퍼티와 동일한 타입의 임시 값을 생성하고, 그 값을 원하는 초기 상태에 맞게 조정한 뒤, 임시 값을 반환하여 프로퍼티의 기본값으로 사용한다.

다음은 클로저를 사용해 기본 프로퍼티 값을 제공하는 기본 구조다:

```swift
class SomeClass {
    let someProperty: SomeType = {
        // 클로저 내부에서 someProperty의 기본값 생성
        // someValue는 SomeType과 동일한 타입이어야 함
        return someValue
    }()
}
```

<!--
  - test: `defaultPropertyWithClosure`

  ```swifttest
  >> class SomeType {}
  -> class SomeClass {
        let someProperty: SomeType = {
           // 클로저 내부에서 someProperty의 기본값 생성
           // someValue는 SomeType과 동일한 타입이어야 함
  >>       let someValue = SomeType()
           return someValue
        }()
     }
  ```
-->

클로저의 닫는 중괄호 뒤에 빈 괄호 쌍이 붙어 있다는 점에 주목하자. 이는 Swift에게 클로저를 즉시 실행하라고 지시한다. 이 괄호를 생략하면 클로저 자체를 프로퍼티에 할당하려는 것으로 간주되며, 클로저의 반환값이 아니다.

> 주의: 클로저를 사용해 프로퍼티를 초기화할 때, 클로저가 실행되는 시점에는 인스턴스의 나머지 부분이 아직 초기화되지 않았다는 점을 기억하자. 즉, 클로저 내부에서는 다른 프로퍼티 값에 접근할 수 없으며, 기본값이 설정된 프로퍼티라도 마찬가지다. 또한 암시적인 `self` 프로퍼티를 사용하거나 인스턴스의 메서드를 호출할 수도 없다.

아래 예제는 체스 게임을 위한 보드를 모델링하는 `Chessboard` 구조체를 정의한다. 체스는 8x8 크기의 보드에서 진행되며, 검은색과 흰색 칸이 번갈아 나타난다.

![](chessBoard)

이 게임 보드를 표현하기 위해 `Chessboard` 구조체는 `boardColors`라는 단일 프로퍼티를 가지고 있다. 이 프로퍼티는 64개의 `Bool` 값으로 이루어진 배열이며, 배열의 값이 `true`면 검은색 칸, `false`면 흰색 칸을 나타낸다. 배열의 첫 번째 항목은 보드의 왼쪽 상단 칸을, 마지막 항목은 오른쪽 하단 칸을 나타낸다.

`boardColors` 배열은 클로저를 사용해 초기화되며, 각 칸의 색상을 설정한다:

```swift
struct Chessboard {
    let boardColors: [Bool] = {
        var temporaryBoard: [Bool] = []
        var isBlack = false
        for i in 1...8 {
            for j in 1...8 {
                temporaryBoard.append(isBlack)
                isBlack = !isBlack
            }
            isBlack = !isBlack
        }
        return temporaryBoard
    }()
    func squareIsBlackAt(row: Int, column: Int) -> Bool {
        return boardColors[(row * 8) + column]
    }
}
```

<!--
  - test: `chessboard`

  ```swifttest
  -> struct Chessboard {
        let boardColors: [Bool] = {
           var temporaryBoard: [Bool] = []
           var isBlack = false
           for i in 1...8 {
              for j in 1...8 {
                 temporaryBoard.append(isBlack)
                 isBlack = !isBlack
              }
              isBlack = !isBlack
           }
           return temporaryBoard
        }()
        func squareIsBlackAt(row: Int, column: Int) -> Bool {
           return boardColors[(row * 8) + column]
        }
     }
  ```
-->

새로운 `Chessboard` 인스턴스가 생성될 때마다 클로저가 실행되고, `boardColors`의 기본값이 계산되어 반환된다. 위 예제의 클로저는 `temporaryBoard`라는 임시 배열을 사용해 보드의 각 칸에 적절한 색상을 계산하고 설정한 뒤, 설정이 완료되면 이 임시 배열을 클로저의 반환값으로 반환한다. 반환된 배열 값은 `boardColors`에 저장되며, `squareIsBlackAt(row:column:)` 유틸리티 함수를 통해 조회할 수 있다:

```swift
let board = Chessboard()
print(board.squareIsBlackAt(row: 0, column: 1))
// "true" 출력
print(board.squareIsBlackAt(row: 7, column: 7))
// "false" 출력
```

<!--
  - test: `chessboard`

  ```swifttest
  -> let board = Chessboard()
  >> assert(board.boardColors == [false, true, false, true, false, true, false, true, true, false, true, false, true, false, true, false, false, true, false, true, false, true, false, true, true, false, true, false, true, false, true, false, false, true, false, true, false, true, false, true, true, false, true, false, true, false, true, false, false, true, false, true, false, true, false, true, true, false, true, false, true, false, true, false])
  -> print(board.squareIsBlackAt(row: 0, column: 1))
  <- true
  -> print(board.squareIsBlackAt(row: 7, column: 7))
  <- false
  ```
-->

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


