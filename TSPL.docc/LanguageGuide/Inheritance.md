# 상속

기능을 추가하거나 재정의하기 위해 서브클래스를 사용한다.

클래스는 다른 클래스로부터 메서드, 프로퍼티, 그리고 다른 특성들을 *상속*받을 수 있다.  
한 클래스가 다른 클래스로부터 상속받을 때, 상속받는 클래스를 *서브클래스*라고 부르고, 상속해주는 클래스를 *슈퍼클래스*라고 부른다.  
상속은 Swift에서 클래스를 다른 타입과 구분짓는 핵심적인 동작이다.

Swift의 클래스는 슈퍼클래스에 속한 메서드, 프로퍼티, 그리고 서브스크립트를 호출하고 접근할 수 있으며,  
이러한 메서드, 프로퍼티, 서브스크립트의 동작을 개선하거나 수정하기 위해 자신만의 재정의 버전을 제공할 수 있다.  
Swift는 재정의가 올바른지 확인하기 위해 재정의 정의가 슈퍼클래스의 정의와 일치하는지 검사한다.

클래스는 상속받은 프로퍼티에 프로퍼티 옵저버를 추가하여 프로퍼티 값이 변경될 때 알림을 받을 수도 있다.  
프로퍼티 옵저버는 원래 저장 프로퍼티로 정의되었는지, 계산 프로퍼티로 정의되었는지와 관계없이 모든 프로퍼티에 추가할 수 있다.


## 기본 클래스 정의하기

다른 클래스로부터 상속받지 않는 모든 클래스를 *기본 클래스*라고 부른다.

> 주의: Swift 클래스는 공통의 기본 클래스에서 상속받지 않는다. 
> 슈퍼클래스를 지정하지 않고 정의한 클래스는 자동으로 기본 클래스가 된다. 
> 이 기본 클래스를 바탕으로 더 복잡한 클래스를 구축할 수 있다.

아래 예제는 `Vehicle`이라는 기본 클래스를 정의한다. 
이 기본 클래스는 `currentSpeed`라는 저장 프로퍼티를 가지며, 기본값은 `0.0`이다(프로퍼티 타입은 `Double`로 추론됨). 
`currentSpeed` 프로퍼티의 값은 읽기 전용 계산 프로퍼티인 `description`에서 사용된다. 
`description`은 차량의 현재 속도를 설명하는 문자열을 반환한다.

`Vehicle` 기본 클래스는 `makeNoise`라는 메서드도 정의한다. 
이 메서드는 기본 `Vehicle` 인스턴스에서는 아무런 동작을 하지 않지만, 
나중에 `Vehicle`의 하위 클래스에서 이 메서드를 커스터마이징할 수 있다.

```swift
class Vehicle {
    var currentSpeed = 0.0
    var description: String {
        return "traveling at \(currentSpeed) miles per hour"
    }
    func makeNoise() {
        // 아무 동작도 하지 않음 - 일반적인 차량은 반드시 소음을 내지 않음
    }
}
```

<!--
  - test: `inheritance`

  ```swifttest
  -> class Vehicle {
        var currentSpeed = 0.0
        var description: String {
           return "traveling at \(currentSpeed) miles per hour"
        }
        func makeNoise() {
           // do nothing - an arbitrary vehicle doesn't necessarily make a noise
        }
     }
  ```
-->

*초기화 구문*을 사용해 `Vehicle`의 새로운 인스턴스를 생성한다. 
초기화 구문은 타입 이름 뒤에 빈 괄호를 붙여 작성한다.

```swift
let someVehicle = Vehicle()
```

<!--
  - test: `inheritance`

  ```swifttest
  -> let someVehicle = Vehicle()
  ```
-->

새로운 `Vehicle` 인스턴스를 생성한 후, 
`description` 프로퍼티에 접근해 차량의 현재 속도를 사람이 읽기 쉬운 형태로 출력할 수 있다.

```swift
print("Vehicle: \(someVehicle.description)")
// Vehicle: traveling at 0.0 miles per hour
```

<!--
  - test: `inheritance`

  ```swifttest
  -> print("Vehicle: \(someVehicle.description)")
  </ Vehicle: traveling at 0.0 miles per hour
  ```
-->

`Vehicle` 클래스는 일반적인 차량의 공통 특성을 정의하지만, 
그 자체로는 큰 유용성이 없다. 
더 유용하게 만들려면, 더 구체적인 종류의 차량을 설명하도록 클래스를 세분화해야 한다.


## 서브클래싱

*서브클래싱*은 기존 클래스를 기반으로 새로운 클래스를 만드는 과정이다.  
서브클래스는 기존 클래스의 특성을 상속받아 이를 세부적으로 조정할 수 있다.  
또한 서브클래스에 새로운 특성을 추가할 수도 있다.

서브클래스가 슈퍼클래스를 가짐을 나타내려면,  
서브클래스 이름 뒤에 콜론(:)을 붙이고 슈퍼클래스 이름을 적는다:

```swift
class SomeSubclass: SomeSuperclass {
    // 서브클래스 정의
}
```

다음 예제는 `Vehicle`을 슈퍼클래스로 하는 `Bicycle` 서브클래스를 정의한다:

```swift
class Bicycle: Vehicle {
    var hasBasket = false
}
```

새로운 `Bicycle` 클래스는 `Vehicle`의 모든 특성을 자동으로 상속받는다.  
예를 들어 `currentSpeed`, `description` 프로퍼티와 `makeNoise()` 메서드 등이 포함된다.

상속받은 특성 외에도, `Bicycle` 클래스는 `hasBasket`이라는 새로운 저장 프로퍼티를 정의한다.  
이 프로퍼티는 기본값으로 `false`를 가지며, 타입은 `Bool`로 추론된다.

기본적으로 새로 생성된 `Bicycle` 인스턴스는 바구니를 갖지 않는다.  
인스턴스 생성 후 특정 `Bicycle` 인스턴스의 `hasBasket` 프로퍼티를 `true`로 설정할 수 있다:

```swift
let bicycle = Bicycle()
bicycle.hasBasket = true
```

상속받은 `currentSpeed` 프로퍼티를 수정하거나,  
`description` 프로퍼티를 조회할 수도 있다:

```swift
bicycle.currentSpeed = 15.0
print("Bicycle: \(bicycle.description)")
// Bicycle: traveling at 15.0 miles per hour
```

서브클래스는 다시 다른 클래스의 슈퍼클래스가 될 수 있다.  
다음 예제는 두 명이 탈 수 있는 자전거인 "탠덤"을 위해 `Bicycle`의 서브클래스를 만든다:

```swift
class Tandem: Bicycle {
    var currentNumberOfPassengers = 0
}
```

`Tandem`은 `Bicycle`의 모든 프로퍼티와 메서드를 상속받고,  
`Bicycle`은 차례로 `Vehicle`의 모든 프로퍼티와 메서드를 상속받는다.  
`Tandem` 서브클래스는 `currentNumberOfPassengers`라는 새로운 저장 프로퍼티를 추가하며,  
이 프로퍼티의 기본값은 `0`이다.

`Tandem`의 인스턴스를 생성하면,  
새로 추가된 프로퍼티와 상속받은 프로퍼티를 모두 사용할 수 있다.  
또한 `Vehicle`에서 상속받은 읽기 전용 `description` 프로퍼티를 조회할 수도 있다:

```swift
let tandem = Tandem()
tandem.hasBasket = true
tandem.currentNumberOfPassengers = 2
tandem.currentSpeed = 22.0
print("Tandem: \(tandem.description)")
// Tandem: traveling at 22.0 miles per hour
```


## 오버라이딩

서브클래스는 슈퍼클래스로부터 상속받은 인스턴스 메서드, 타입 메서드, 인스턴스 프로퍼티, 타입 프로퍼티, 또는 서브스크립트에 대해 자체적인 커스텀 구현을 제공할 수 있다. 이를 *오버라이딩*이라고 한다.

상속받은 특성을 오버라이드하려면, 오버라이딩 정의 앞에 `override` 키워드를 붙여야 한다. 이 키워드는 의도적으로 오버라이드를 제공한다는 것을 명확히 하고, 실수로 일치하는 정의를 제공하지 않았음을 나타낸다. 실수로 인한 오버라이딩은 예상치 못한 동작을 초래할 수 있으며, `override` 키워드 없이 오버라이딩을 시도하면 코드 컴파일 시 오류로 진단된다.

`override` 키워드는 Swift 컴파일러가 오버라이딩 클래스의 슈퍼클래스(또는 그 상위 클래스 중 하나)가 오버라이드에 제공한 선언과 일치하는지 확인하도록 지시한다. 이 검사를 통해 오버라이딩 정의가 정확한지 보장한다.


### 상위 클래스의 메서드, 프로퍼티, 서브스크립트 접근

서브클래스에서 메서드, 프로퍼티, 또는 서브스크립트를 재정의할 때, 기존 상위 클래스의 구현을 활용하는 것이 유용한 경우가 있다. 예를 들어, 기존 구현의 동작을 개선하거나 상속받은 변수에 수정된 값을 저장할 수 있다.

이러한 경우, `super` 접두사를 사용해 상위 클래스 버전의 메서드, 프로퍼티, 또는 서브스크립트에 접근한다:

- `someMethod()`라는 이름의 재정의된 메서드는 구현 내부에서 `super.someMethod()`를 호출해 상위 클래스 버전의 `someMethod()`를 호출할 수 있다.
- `someProperty`라는 이름의 재정의된 프로퍼티는 게터 또는 세터 구현 내부에서 `super.someProperty`를 통해 상위 클래스 버전의 `someProperty`에 접근할 수 있다.
- `someIndex`에 대한 재정의된 서브스크립트는 구현 내부에서 `super[someIndex]`를 통해 상위 클래스 버전의 동일한 서브스크립트에 접근할 수 있다.


### 메서드 오버라이딩

상속받은 인스턴스 메서드나 타입 메서드를 서브클래스에서 재정의하여 특화된 구현이나 대체 구현을 제공할 수 있다.

다음 예제는 `Vehicle` 클래스의 새로운 서브클래스인 `Train`을 정의한다. `Train`은 `Vehicle`로부터 상속받은 `makeNoise()` 메서드를 재정의한다:

```swift
class Train: Vehicle {
    override func makeNoise() {
        print("Choo Choo")
    }
}
```

<!--
  - test: `inheritance`

  ```swifttest
  -> class Train: Vehicle {
        override func makeNoise() {
           print("Choo Choo")
        }
     }
  ```
-->

`Train`의 새로운 인스턴스를 생성하고 `makeNoise()` 메서드를 호출하면, `Train` 서브클래스의 메서드가 호출되는 것을 확인할 수 있다:

```swift
let train = Train()
train.makeNoise()
// Prints "Choo Choo"
```

<!--
  - test: `inheritance`

  ```swifttest
  -> let train = Train()
  -> train.makeNoise()
  <- Choo Choo
  ```
-->


### 프로퍼티 재정의

상속받은 인스턴스 프로퍼티나 타입 프로퍼티를 재정의할 수 있다. 이를 통해 해당 프로퍼티에 대해 커스텀 getter와 setter를 제공하거나, 기본 프로퍼티 값이 변경될 때 이를 관찰할 수 있도록 프로퍼티 옵저버를 추가할 수 있다.


#### 프로퍼티 Getter와 Setter 재정의하기

상속받은 프로퍼티를 재정의할 때, 커스텀 getter(그리고 필요하다면 setter도)를 제공할 수 있다. 이때 상속받은 프로퍼티가 원본에서 저장 프로퍼티로 구현되었는지, 계산 프로퍼티로 구현되었는지는 중요하지 않다. 하위 클래스는 상속받은 프로퍼티의 이름과 타입만 알고 있을 뿐이다. 프로퍼티를 재정의할 때는 항상 이름과 타입을 명시해야 한다. 이는 컴파일러가 동일한 이름과 타입을 가진 상위 클래스 프로퍼티와 일치하는지 확인할 수 있게 해준다.

읽기 전용 프로퍼티를 읽기-쓰기 프로퍼티로 재정의할 수 있다. 이때 하위 클래스에서 getter와 setter를 모두 제공해야 한다. 하지만 읽기-쓰기 프로퍼티를 읽기 전용 프로퍼티로 재정의할 수는 없다.

> 참고: 프로퍼티 재정의 시 setter를 제공한다면, getter도 반드시 제공해야 한다. 재정의한 getter에서 상속받은 프로퍼티의 값을 수정하지 않으려면, `super.someProperty`를 반환하여 상속받은 값을 그대로 전달할 수 있다. 여기서 `someProperty`는 재정의하는 프로퍼티의 이름이다.

다음 예제는 `Vehicle` 클래스를 상속받은 `Car` 클래스를 정의한다. `Car` 클래스는 기본값이 `1`인 정수 타입의 `gear`라는 새로운 저장 프로퍼티를 도입한다. 또한 `Car` 클래스는 `Vehicle`에서 상속받은 `description` 프로퍼티를 재정의하여, 현재 기어 정보를 포함한 커스텀 설명을 제공한다.

```swift
class Car: Vehicle {
    var gear = 1
    override var description: String {
        return super.description + " in gear \(gear)"
    }
}
```

<!--
  - test: `inheritance`

  ```swifttest
  -> class Car: Vehicle {
        var gear = 1
        override var description: String {
           return super.description + " in gear \(gear)"
        }
     }
  ```
-->

`description` 프로퍼티를 재정할 때, `super.description`을 먼저 호출하여 `Vehicle` 클래스의 `description` 프로퍼티 값을 가져온다. 그런 다음 `Car` 클래스의 `description` 버전은 이 설명 끝에 현재 기어 정보를 추가한다.

`Car` 클래스의 인스턴스를 생성하고 `gear`와 `currentSpeed` 프로퍼티를 설정한 후, `description` 프로퍼티를 출력하면 `Car` 클래스에서 정의한 맞춤 설명이 반환되는 것을 확인할 수 있다.

```swift
let car = Car()
car.currentSpeed = 25.0
car.gear = 3
print("Car: \(car.description)")
// Car: traveling at 25.0 miles per hour in gear 3
```

<!--
  - test: `inheritance`

  ```swifttest
  -> let car = Car()
  -> car.currentSpeed = 25.0
  -> car.gear = 3
  -> print("Car: \(car.description)")
  </ Car: traveling at 25.0 miles per hour in gear 3
  ```
-->


#### 프로퍼티 옵저버 오버라이딩

상속받은 프로퍼티에 프로퍼티 옵저버를 추가하기 위해 프로퍼티 오버라이딩을 사용할 수 있다. 이를 통해 상속받은 프로퍼티의 값이 변경될 때마다 알림을 받을 수 있으며, 해당 프로퍼티가 원래 어떻게 구현되었는지와 상관없이 동작한다. 프로퍼티 옵저버에 대한 자세한 내용은 <doc:Properties#Property-Observers>를 참고한다.

> 주의: 상속받은 상수 저장 프로퍼티나 상속받은 읽기 전용 계산 프로퍼티에는 프로퍼티 옵저버를 추가할 수 없다. 이러한 프로퍼티의 값은 설정할 수 없기 때문에, 오버라이드의 일부로 `willSet`이나 `didSet`을 제공하는 것은 적절하지 않다.
>
> 또한, 동일한 프로퍼티에 대해 오버라이딩 세터와 오버라이딩 프로퍼티 옵저버를 동시에 제공할 수 없다. 프로퍼티의 값 변경을 관찰하고 싶고, 이미 커스텀 세터를 제공하고 있다면, 커스텀 세터 내부에서 값 변경을 관찰하면 된다.

다음 예제는 `Car` 클래스의 서브클래스인 `AutomaticCar`라는 새로운 클래스를 정의한다. `AutomaticCar` 클래스는 자동 변속기가 장착된 자동차를 나타내며, 현재 속도에 따라 적절한 기어를 자동으로 선택한다:

```swift
class AutomaticCar: Car {
    override var currentSpeed: Double {
        didSet {
            gear = Int(currentSpeed / 10.0) + 1
        }
    }
}
```

<!--
  - test: `inheritance`

  ```swifttest
  -> class AutomaticCar: Car {
        override var currentSpeed: Double {
           didSet {
              gear = Int(currentSpeed / 10.0) + 1
           }
        }
     }
  ```
-->

`AutomaticCar` 인스턴스의 `currentSpeed` 프로퍼티를 설정할 때마다, 프로퍼티의 `didSet` 옵저버가 인스턴스의 `gear` 프로퍼티를 새로운 속도에 맞는 적절한 기어로 설정한다. 구체적으로, 프로퍼티 옵저버는 새로운 `currentSpeed` 값을 `10`으로 나누고, 가장 가까운 정수로 내림한 후 `1`을 더한 값을 기어로 선택한다. 속도가 `35.0`일 경우 기어는 `4`가 된다:

```swift
let automatic = AutomaticCar()
automatic.currentSpeed = 35.0
print("AutomaticCar: \(automatic.description)")
// AutomaticCar: traveling at 35.0 miles per hour in gear 4
```

<!--
  - test: `inheritance`

  ```swifttest
  -> let automatic = AutomaticCar()
  -> automatic.currentSpeed = 35.0
  -> print("AutomaticCar: \(automatic.description)")
  </ AutomaticCar: traveling at 35.0 miles per hour in gear 4
  ```
-->


## 오버라이드 방지

메서드, 프로퍼티, 서브스크립트를 오버라이드하지 못하도록 막으려면 *final*로 표시한다. 이를 위해 `final` 수정자를 메서드, 프로퍼티, 서브스크립트의 키워드 앞에 추가한다. 예를 들어 `final var`, `final func`, `final class func`, `final subscript`와 같이 작성한다.

서브클래스에서 final로 표시된 메서드, 프로퍼티, 서브스크립트를 오버라이드하려고 하면 컴파일 타임 오류가 발생한다. 익스텐션에서 클래스에 추가한 메서드, 프로퍼티, 서브스크립트도 익스텐션 정의 내에서 final로 표시할 수 있다. 자세한 내용은 <doc:Extensions>를 참고한다.

<!--
  - test: `finalPreventsOverriding`

  ```swifttest
  -> class C {
        final var someVar = 0
        final func someFunction() {
           print("In someFunction")
        }
     }
  -> class D : C {
        override var someVar: Int {
           get { return 1 }
           set {}
        }
        override func someFunction() {
           print("In overridden someFunction")
        }
     }
  !$ error: property overrides a 'final' property
  !! override var someVar: Int {
  !! ^
  !$ note: overridden declaration is here
  !! final var someVar = 0
  !! ^
  !$ error: instance method overrides a 'final' instance method
  !! override func someFunction() {
  !! ^
  !$ note: overridden declaration is here
  !! final func someFunction() {
  !! ^
  ```
-->

클래스 전체를 final로 표시하려면 클래스 정의에서 `class` 키워드 앞에 `final` 수정자를 추가한다(`final class`). final 클래스를 서브클래싱하려고 하면 컴파일 타임 오류가 발생한다.

<!--
  - test: `finalClassPreventsOverriding`

  ```swifttest
  -> final class C {
        var someVar = 0
        func someFunction() {
           print("In someFunction")
        }
     }
  -> class D : C {
        override var someVar: Int {
           get { return 1 }
           set {}
        }
        override func someFunction() {
           print("In overridden someFunction")
        }
     }
  !$ error: property overrides a 'final' property
  !!      override var someVar: Int {
  !!                   ^
  !$ note: overridden declaration is here
  !!      var someVar = 0
  !!          ^
  !$ error: instance method overrides a 'final' instance method
  !!      override func someFunction() {
  !!                    ^
  !$ note: overridden declaration is here
  !!      func someFunction() {
  !!           ^
  !$ error: inheritance from a final class 'C'
  !! class D : C {
  !!       ^
  ```
-->

<!--
  TODO: I should probably provide an example here.
-->

<!--
  TODO: provide more information about function signatures,
  and what does / doesn't make them unique.
  For example, the parameter names don't have to match
  in order for a function to override a similar signature in its parent.
  (This is true for both of the function declaration syntaxes.)
-->

<!--
  TODO: Mention that you can return more-specific types, and take less-specific types,
  when overriding methods that use optionals / unchecked optionals.

  TODO: Overriding Type Methods
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-->

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


