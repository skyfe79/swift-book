# 함수

특정 작업을 수행하는 독립적인 코드 블록인 함수를 정의하고 호출한다. 또한 함수의 인자에 레이블을 붙이고 반환 값을 사용하는 방법을 알아본다.

**함수**는 특정 작업을 수행하는 독립적인 코드 블록이다. 함수에 작업 내용을 나타내는 이름을 붙이고, 이 이름을 사용해 필요할 때 함수를 "호출"하여 작업을 수행한다.

Swift의 통합 함수 문법은 단순한 C 스타일 함수부터 각 매개변수에 이름과 인자 레이블이 있는 복잡한 Objective-C 스타일 메서드까지 표현할 수 있을 만큼 유연하다. 매개변수는 기본값을 제공해 함수 호출을 단순화할 수 있으며, 함수 실행이 완료된 후 전달된 변수를 수정하는 입출력(in-out) 매개변수로 전달할 수도 있다.

Swift의 모든 함수는 매개변수 타입과 반환 타입으로 구성된 타입을 가진다. 이 타입을 Swift의 다른 타입처럼 사용할 수 있어, 함수를 다른 함수의 매개변수로 전달하거나 함수에서 함수를 반환하는 것이 쉽다. 또한 유용한 기능을 중첩 함수 범위 내에 캡슐화하기 위해 다른 함수 내부에 함수를 작성할 수도 있다.


## 함수 정의와 호출

함수를 정의할 때, 입력으로 사용할 하나 이상의 이름과 타입을 가진 값(파라미터)을 선택적으로 정의할 수 있다. 또한 함수가 작업을 마친 후 출력으로 반환할 값의 타입(반환 타입)도 선택적으로 정의할 수 있다.

모든 함수는 수행할 작업을 설명하는 *함수 이름*을 가진다. 함수를 사용하려면 함수 이름을 "호출"하고, 함수의 파라미터 타입과 일치하는 입력 값(인자)을 전달한다. 함수의 인자는 항상 파라미터 목록의 순서와 동일하게 제공해야 한다.

아래 예제의 함수는 `greet(person:)`이라는 이름을 가진다. 이 함수는 사람의 이름을 입력으로 받아 해당 사람에게 보낼 인사말을 반환한다. 이를 위해 하나의 입력 파라미터(`person`이라는 `String` 값)와 반환 타입(`String`)을 정의한다. 반환 타입은 해당 사람에게 보낼 인사말을 포함한다.

```swift
func greet(person: String) -> String {
    let greeting = "Hello, " + person + "!"
    return greeting
}
```

<!--
  - test: `definingAndCalling`

  ```swifttest
  -> func greet(person: String) -> String {
        let greeting = "Hello, " + person + "!"
        return greeting
     }
  ```
-->

이 모든 정보는 `func` 키워드로 시작하는 함수의 *정의*에 포함된다. 함수의 반환 타입은 *반환 화살표* `->`(하이픈과 오른쪽 꺾쇠 괄호)로 표시하며, 그 뒤에 반환할 타입의 이름을 적는다.

함수 정의는 함수가 수행하는 작업, 받을 것으로 예상되는 입력, 작업을 마친 후 반환할 내용을 설명한다. 이 정의는 코드의 다른 부분에서 함수를 명확하게 호출할 수 있게 한다.

```swift
print(greet(person: "Anna"))
// "Hello, Anna!" 출력
print(greet(person: "Brian"))
// "Hello, Brian!" 출력
```

<!--
  - test: `definingAndCalling`

  ```swifttest
  -> print(greet(person: "Anna"))
  <- Hello, Anna!
  -> print(greet(person: "Brian"))
  <- Hello, Brian!
  ```
-->

`greet(person:)` 함수를 호출할 때는 `person` 인자 레이블 뒤에 `String` 값을 전달한다(예: `greet(person: "Anna")`). 이 함수는 `String` 값을 반환하므로, `greet(person:)`을 `print(_:separator:terminator:)` 함수 호출로 감싸 문자열을 출력하고 반환 값을 확인할 수 있다.

> 참고: `print(_:separator:terminator:)` 함수는 첫 번째 인자에 대한 레이블이 없으며, 다른 인자들은 기본값이 있기 때문에 선택적이다. 이러한 함수 문법의 변형은 아래 <doc:Functions#Function-Argument-Labels-and-Parameter-Names>와 <doc:Functions#Default-Parameter-Values>에서 다룬다.

`greet(person:)` 함수의 본문은 `greeting`이라는 새로운 `String` 상수를 정의하고 간단한 인사말로 설정하는 것으로 시작한다. 이 인사말은 `return` 키워드를 사용해 함수 밖으로 전달된다. `return greeting` 코드 줄에서 함수는 실행을 마치고 `greeting`의 현재 값을 반환한다.

`greet(person:)` 함수를 다른 입력 값으로 여러 번 호출할 수 있다. 위 예제는 입력 값으로 `"Anna"`와 `"Brian"`을 전달했을 때의 결과를 보여준다. 함수는 각 경우에 맞춤형 인사말을 반환한다.

함수 본문을 더 짧게 만들려면 메시지 생성과 반환 문을 한 줄로 결합할 수 있다.

```swift
func greetAgain(person: String) -> String {
    return "Hello again, " + person + "!"
}
print(greetAgain(person: "Anna"))
// "Hello again, Anna!" 출력
```

<!--
  - test: `definingAndCalling`

  ```swifttest
  -> func greetAgain(person: String) -> String {
        return "Hello again, " + person + "!"
     }
  -> print(greetAgain(person: "Anna"))
  <- Hello again, Anna!
  ```
-->


## 함수 매개변수와 반환 값

Swift에서 함수 매개변수와 반환 값은 매우 유연하게 정의할 수 있다. 단순한 유틸리티 함수부터 복잡한 함수까지 다양한 형태로 작성할 수 있다. 예를 들어, 이름 없는 단일 매개변수를 가진 간단한 함수부터, 표현력 있는 매개변수 이름과 다양한 옵션을 가진 복잡한 함수까지 만들 수 있다.


### 매개변수가 없는 함수

함수는 반드시 입력 매개변수를 정의할 필요가 없다. 다음은 입력 매개변수가 없는 함수로, 호출할 때마다 항상 동일한 `String` 메시지를 반환한다:

```swift
func sayHelloWorld() -> String {
    return "hello, world"
}
print(sayHelloWorld())
// "hello, world" 출력
```

<!--
  - test: `functionsWithoutParameters`

  ```swifttest
  -> func sayHelloWorld() -> String {
        return "hello, world"
     }
  -> print(sayHelloWorld())
  <- hello, world
  ```
-->

함수 정의에서는 매개변수를 받지 않더라도 함수 이름 뒤에 괄호를 반드시 포함해야 한다. 함수를 호출할 때도 함수 이름 뒤에 빈 괄호 쌍을 붙인다.


### 여러 매개변수를 가진 함수

함수는 여러 개의 입력 매개변수를 가질 수 있다. 매개변수는 함수의 괄호 안에 쉼표로 구분하여 작성한다.

이 함수는 사람의 이름과 이미 인사했는지 여부를 입력으로 받아, 해당 사람에게 적절한 인사말을 반환한다:

```swift
func greet(person: String, alreadyGreeted: Bool) -> String {
    if alreadyGreeted {
        return greetAgain(person: person)
    } else {
        return greet(person: person)
    }
}
print(greet(person: "Tim", alreadyGreeted: true))
// Prints "Hello again, Tim!"
```

<!--
  - test: `definingAndCalling`

  ```swifttest
  -> func greet(person: String, alreadyGreeted: Bool) -> String {
         if alreadyGreeted {
             return greetAgain(person: person)
         } else {
             return greet(person: person)
         }
     }
  -> print(greet(person: "Tim", alreadyGreeted: true))
  <- Hello again, Tim!
  ```
-->

`greet(person:alreadyGreeted:)` 함수를 호출할 때는 `person` 레이블이 붙은 `String` 타입의 인자 값과 `alreadyGreeted` 레이블이 붙은 `Bool` 타입의 인자 값을 괄호 안에 쉼표로 구분하여 전달한다. 이 함수는 이전 섹션에서 보여준 `greet(person:)` 함수와는 다른 함수다. 두 함수 모두 이름이 `greet`으로 시작하지만, `greet(person:alreadyGreeted:)` 함수는 두 개의 인자를 받는 반면 `greet(person:)` 함수는 하나의 인자만 받는다.


### 반환 값이 없는 함수

함수는 반드시 반환 타입을 정의할 필요가 없다. 다음은 `greet(person:)` 함수의 한 버전으로, 값을 반환하는 대신 자신의 `String` 값을 출력한다.

```swift
func greet(person: String) {
    print("Hello, \(person)!")
}
greet(person: "Dave")
// Prints "Hello, Dave!"
```

<!--
  - test: `functionsWithoutReturnValues`

  ```swifttest
  -> func greet(person: String) {
        print("Hello, \(person)!")
     }
  -> greet(person: "Dave")
  <- Hello, Dave!
  ```
-->

이 함수는 값을 반환할 필요가 없기 때문에, 함수 정의에 반환 화살표(`->`)나 반환 타입이 포함되지 않는다.

> 참고: 엄밀히 말하면, 이 버전의 `greet(person:)` 함수도 여전히 값을 반환한다. 반환 값이 정의되지 않았더라도, 반환 타입이 정의되지 않은 함수는 `Void` 타입의 특별한 값을 반환한다. 이는 단순히 빈 튜플로, `()`로 표기된다.

함수의 반환 값은 호출 시 무시할 수 있다.

```swift
func printAndCount(string: String) -> Int {
    print(string)
    return string.count
}
func printWithoutCounting(string: String) {
    let _ = printAndCount(string: string)
}
printAndCount(string: "hello, world")
// prints "hello, world" and returns a value of 12
printWithoutCounting(string: "hello, world")
// prints "hello, world" but doesn't return a value
```

<!--
  - test: `functionsWithoutReturnValues`

  ```swifttest
  -> func printAndCount(string: String) -> Int {
        print(string)
        return string.count
     }
  -> func printWithoutCounting(string: String) {
        let _ = printAndCount(string: string)
     }
  >> let a =
  -> printAndCount(string: "hello, world")
  << hello, world
  >> assert(a == 12)
  // prints "hello, world" and returns a value of 12
  -> printWithoutCounting(string: "hello, world")
  << hello, world
  // prints "hello, world" but doesn't return a value
  ```
-->

첫 번째 함수인 `printAndCount(string:)`는 문자열을 출력한 후, 그 문자열의 문자 수를 `Int`로 반환한다. 두 번째 함수인 `printWithoutCounting(string:)`는 첫 번째 함수를 호출하지만, 반환 값을 무시한다. 두 번째 함수가 호출되면, 첫 번째 함수에 의해 메시지가 여전히 출력되지만, 반환된 값은 사용되지 않는다.

> 참고: 반환 값은 무시할 수 있지만, 반환 값이 있다고 선언한 함수는 항상 값을 반환해야 한다. 반환 타입이 정의된 함수는 값을 반환하지 않고 함수의 끝에 도달할 수 없으며, 이를 시도하면 컴파일 타임 오류가 발생한다.

<!--
FIXME 함수가 @discardableResult로 표시되지 않은 경우,
반환 값을 무시하면 컴파일 타임 경고가 발생한다.

반환 값이 부수적인 경우 @discardableResult를 사용하는 것이 좋다.
예를 들어 array.removeFirst(...)와 같은 경우다.
그렇지 않으면 호출 시점에 `_ = foo()`를 사용하는 것이 더 낫다.
-->


### 여러 값을 반환하는 함수

함수에서 튜플 타입을 반환 타입으로 사용하면 하나의 복합 반환 값으로 여러 값을 반환할 수 있다.

아래 예제는 `minMax(array:)`라는 함수를 정의한다. 이 함수는 `Int` 값 배열에서 가장 작은 수와 가장 큰 수를 찾는다:

```swift
func minMax(array: [Int]) -> (min: Int, max: Int) {
    var currentMin = array[0]
    var currentMax = array[0]
    for value in array[1..<array.count] {
        if value < currentMin {
            currentMin = value
        } else if value > currentMax {
            currentMax = value
        }
    }
    return (currentMin, currentMax)
}
```

<!--
  - test: `tupleTypesAsReturnTypes`

  ```swifttest
  -> func minMax(array: [Int]) -> (min: Int, max: Int) {
        var currentMin = array[0]
        var currentMax = array[0]
        for value in array[1..<array.count] {
           if value < currentMin {
              currentMin = value
           } else if value > currentMax {
              currentMax = value
           }
        }
        return (currentMin, currentMax)
     }
  ```
-->

`minMax(array:)` 함수는 두 개의 `Int` 값을 포함하는 튜플을 반환한다. 이 값들은 `min`과 `max`라는 이름으로 레이블링되어 있어, 함수의 반환 값을 조회할 때 이름으로 접근할 수 있다.

`minMax(array:)` 함수의 본문은 먼저 `currentMin`과 `currentMax`라는 두 작업 변수를 배열의 첫 번째 정수 값으로 설정한다. 그런 다음 함수는 배열의 나머지 값을 순회하며 각 값이 `currentMin`과 `currentMax`보다 작은지 또는 큰지 확인한다. 마지막으로 전체 최소값과 최대값이 두 `Int` 값의 튜플로 반환된다.

튜플의 멤버 값은 함수의 반환 타입의 일부로 이름이 지정되어 있기 때문에, 점 표기법을 사용해 찾은 최소값과 최대값을 검색할 수 있다:

```swift
let bounds = minMax(array: [8, -6, 2, 109, 3, 71])
print("min is \(bounds.min) and max is \(bounds.max)")
// Prints "min is -6 and max is 109"
```

<!--
  - test: `tupleTypesAsReturnTypes`

  ```swifttest
  -> let bounds = minMax(array: [8, -6, 2, 109, 3, 71])
  -> print("min is \(bounds.min) and max is \(bounds.max)")
  <- min is -6 and max is 109
  ```
-->

튜플의 멤버는 함수에서 튜플이 반환될 때 이름을 지정할 필요가 없다. 왜냐하면 그 이름들은 이미 함수의 반환 타입의 일부로 지정되어 있기 때문이다.


#### 옵셔널 튜플 반환 타입

함수에서 반환할 튜플 타입이 전체적으로 "값이 없을" 가능성이 있다면,  
전체 튜플이 `nil`이 될 수 있다는 사실을 반영하기 위해 *옵셔널* 튜플 반환 타입을 사용할 수 있다.  
옵셔널 튜플 반환 타입은 튜플 타입의 닫는 괄호 뒤에 물음표를 붙여서 표현한다.  
예를 들어 `(Int, Int)?` 또는 `(String, Int, Bool)?`과 같이 작성한다.

> 참고: `(Int, Int)?`와 같은 옵셔널 튜플 타입은  
> `(Int?, Int?)`처럼 각 값이 옵셔널인 튜플과 다르다.  
> 옵셔널 튜플 타입은 튜플 전체가 옵셔널이며,  
> 튜플 내의 각 값이 옵셔널인 것은 아니다.

앞서 살펴본 `minMax(array:)` 함수는 두 개의 `Int` 값을 포함하는 튜플을 반환한다.  
하지만 이 함수는 전달받은 배열에 대한 안전성 검사를 수행하지 않는다.  
만약 `array` 인자로 빈 배열이 전달되면,  
위에서 정의한 `minMax(array:)` 함수는 `array[0]`에 접근하려고 시도할 때 런타임 오류를 발생시킨다.

빈 배열을 안전하게 처리하기 위해,  
`minMax(array:)` 함수를 옵셔널 튜플 반환 타입으로 작성하고  
배열이 비어 있을 때 `nil`을 반환할 수 있다:

```swift
func minMax(array: [Int]) -> (min: Int, max: Int)? {
    if array.isEmpty { return nil }
    var currentMin = array[0]
    var currentMax = array[0]
    for value in array[1..<array.count] {
        if value < currentMin {
            currentMin = value
        } else if value > currentMax {
            currentMax = value
        }
    }
    return (currentMin, currentMax)
}
```

<!--
  - test: `tupleTypesAsReturnTypes2`

  ```swifttest
  -> func minMax(array: [Int]) -> (min: Int, max: Int)? {
        if array.isEmpty { return nil }
        var currentMin = array[0]
        var currentMax = array[0]
        for value in array[1..<array.count] {
           if value < currentMin {
              currentMin = value
           } else if value > currentMax {
              currentMax = value
           }
        }
        return (currentMin, currentMax)
     }
  ```
-->

옵셔널 바인딩을 사용해 이 버전의 `minMax(array:)` 함수가  
실제 튜플 값을 반환하는지 아니면 `nil`을 반환하는지 확인할 수 있다:

```swift
if let bounds = minMax(array: [8, -6, 2, 109, 3, 71]) {
    print("min is \(bounds.min) and max is \(bounds.max)")
}
// Prints "min is -6 and max is 109"
```

<!--
  - test: `tupleTypesAsReturnTypes2`

  ```swifttest
  -> if let bounds = minMax(array: [8, -6, 2, 109, 3, 71]) {
        print("min is \(bounds.min) and max is \(bounds.max)")
     }
  <- min is -6 and max is 109
  ```
-->


### 암시적 반환 함수

함수 전체 본문이 단일 표현식으로 이루어진 경우, 해당 함수는 암시적으로 그 표현식을 반환한다. 예를 들어, 아래 두 함수는 동일한 동작을 수행한다:

```swift
func greeting(for person: String) -> String {
    "Hello, " + person + "!"
}
print(greeting(for: "Dave"))
// Prints "Hello, Dave!"

func anotherGreeting(for person: String) -> String {
    return "Hello, " + person + "!"
}
print(anotherGreeting(for: "Dave"))
// Prints "Hello, Dave!"
```

<!--
  - test: `implicit-func-return`

  ```swifttest
  -> func greeting(for person: String) -> String {
        "Hello, " + person + "!"
     }
  -> print(greeting(for: "Dave"))
  <- Hello, Dave!

  -> func anotherGreeting(for person: String) -> String {
        return "Hello, " + person + "!"
     }
  -> print(anotherGreeting(for: "Dave"))
  <- Hello, Dave!
  ```
-->

`greeting(for:)` 함수의 전체 정의는 반환하는 인사 메시지이다. 이는 더 짧은 형태로 작성할 수 있음을 의미한다. `anotherGreeting(for:)` 함수는 더 긴 함수처럼 `return` 키워드를 사용해 동일한 인사 메시지를 반환한다. `return` 한 줄로 작성할 수 있는 모든 함수는 `return`을 생략할 수 있다.

<doc:Properties#Shorthand-Getter-Declaration>에서 살펴보겠지만, 프로퍼티 게터도 암시적 반환을 사용할 수 있다.

> 참고: 암시적 반환 값으로 작성하는 코드는 반드시 어떤 값을 반환해야 한다. 예를 들어, `print(13)`을 암시적 반환 값으로 사용할 수는 없다. 그러나 Swift는 암시적 반환이 발생하지 않음을 알고 있기 때문에, `fatalError("Oh no!")`와 같이 반환하지 않는 함수를 암시적 반환 값으로 사용할 수 있다.

<!--
  - test: `implicit-return-print-instead`

  ```swifttest
  // This is ok:
  >> func testFatal() -> Int {
  >>     fatalError("Oh no!")
  >> }

  // But not this:
  >> func testPrint() -> Int {
  >>     print(13)
  >> }
  !$ error: cannot convert return expression of type '()' to return type 'Int'
  !! print(13)
  !! ^~~~~~~~~
  ```
-->


## 함수 인자 라벨과 파라미터 이름

각 함수 파라미터는 *인자 라벨*과 *파라미터 이름*을 가진다. 인자 라벨은 함수를 호출할 때 사용되며, 각 인자는 함수 호출 시 해당 라벨 앞에 표시된다. 파라미터 이름은 함수 구현 내부에서 사용된다. 기본적으로 파라미터는 파라미터 이름을 인자 라벨로 사용한다.

```swift
func someFunction(firstParameterName: Int, secondParameterName: Int) {
    // 함수 본문에서 firstParameterName과 secondParameterName은
    // 첫 번째와 두 번째 파라미터의 인자 값을 참조한다.
}
someFunction(firstParameterName: 1, secondParameterName: 2)
```

<!--
  - test: `functionParameterNames`

  ```swifttest
  -> func someFunction(firstParameterName: Int, secondParameterName: Int) {
        // 함수 본문에서 firstParameterName과 secondParameterName은
        // 첫 번째와 두 번째 파라미터의 인자 값을 참조한다.
     }
  -> someFunction(firstParameterName: 1, secondParameterName: 2)
  ```
-->

모든 파라미터는 고유한 이름을 가져야 한다. 여러 파라미터가 동일한 인자 라벨을 가질 수 있지만, 고유한 인자 라벨을 사용하면 코드의 가독성을 높일 수 있다.

<!--
  - test: `non-unique-external-name`

  ```swifttest
  -> func foo(external a: Int, external b: Int) {}
  -> foo(external: 7, external: 12)
  ```
-->


### 인자 레이블 지정하기

인자 레이블은 파라미터 이름 앞에 공백으로 구분하여 작성한다:

```swift
func someFunction(argumentLabel parameterName: Int) {
    // 함수 내부에서 parameterName은 해당 파라미터의 인자 값을 참조한다.
}
```

<!--
  - test: `externalParameterNames`

  ```swifttest
  -> func someFunction(argumentLabel parameterName: Int) {
        // In the function body, parameterName refers to the argument value
        // for that parameter.
     }
  ```
-->

다음은 `greet(person:)` 함수를 변형한 예제로, 사람의 이름과 고향을 받아 인사말을 반환한다:

```swift
func greet(person: String, from hometown: String) -> String {
    return "Hello \(person)!  Glad you could visit from \(hometown)."
}
print(greet(person: "Bill", from: "Cupertino"))
// Prints "Hello Bill!  Glad you could visit from Cupertino."
```

<!--
  - test: `externalParameterNames`

  ```swifttest
  -> func greet(person: String, from hometown: String) -> String {
         return "Hello \(person)!  Glad you could visit from \(hometown)."
     }
  -> print(greet(person: "Bill", from: "Cupertino"))
  <- Hello Bill!  Glad you could visit from Cupertino.
  ```
-->

인자 레이블을 사용하면 함수를 호출할 때 문장처럼 자연스럽게 표현할 수 있으며, 함수 본문도 읽기 쉽고 의도가 명확해진다.


### 인자 라벨 생략하기

함수에서 특정 파라미터의 인자 라벨을 생략하고 싶다면, 해당 파라미터에 대해 명시적인 인자 라벨 대신 언더스코어(`_`)를 사용한다.

```swift
func someFunction(_ firstParameterName: Int, secondParameterName: Int) {
    // 함수 본문에서 firstParameterName과 secondParameterName은
    // 각각 첫 번째와 두 번째 파라미터의 인자 값을 나타낸다.
}
someFunction(1, secondParameterName: 2)
```

<!--
  - test: `omittedExternalParameterNames`

  ```swifttest
  -> func someFunction(_ firstParameterName: Int, secondParameterName: Int) {
        // 함수 본문에서 firstParameterName과 secondParameterName은
        // 각각 첫 번째와 두 번째 파라미터의 인자 값을 나타낸다.
     }
  -> someFunction(1, secondParameterName: 2)
  ```
-->

함수의 파라미터에 인자 라벨이 지정되어 있다면, 함수를 호출할 때 반드시 해당 라벨을 사용해야 한다.


### 기본 매개변수 값

함수의 매개변수에 기본값을 정의할 수 있다. 매개변수의 타입 뒤에 값을 할당하면 된다. 기본값이 정의된 경우, 함수를 호출할 때 해당 매개변수를 생략할 수 있다.

```swift
func someFunction(parameterWithoutDefault: Int, parameterWithDefault: Int = 12) {
    // 이 함수를 호출할 때 두 번째 인수를 생략하면,
    // 함수 내부에서 parameterWithDefault의 값은 12가 된다.
}
someFunction(parameterWithoutDefault: 3, parameterWithDefault: 6) // parameterWithDefault는 6
someFunction(parameterWithoutDefault: 4) // parameterWithDefault는 12
```

<!--
  - test: `omittedExternalParameterNames`

  ```swifttest
  -> func someFunction(parameterWithoutDefault: Int, parameterWithDefault: Int = 12) {
        // 이 함수를 호출할 때 두 번째 인수를 생략하면,
        // 함수 내부에서 parameterWithDefault의 값은 12가 된다.
     }
  -> someFunction(parameterWithoutDefault: 3, parameterWithDefault: 6) // parameterWithDefault는 6
  -> someFunction(parameterWithoutDefault: 4) // parameterWithDefault는 12
  ```
-->

기본값이 없는 매개변수는 함수 매개변수 목록의 앞쪽에 위치시킨다. 기본값이 없는 매개변수는 일반적으로 함수의 의미에 더 중요하다. 기본값이 없는 매개변수를 먼저 작성하면, 기본 매개변수를 생략하더라도 동일한 함수가 호출된다는 것을 쉽게 인식할 수 있다.


### 가변 인자 (Variadic Parameters)

*가변 인자*는 특정 타입의 값을 0개 이상 받을 수 있다. 함수를 호출할 때 입력값의 개수가 변할 수 있는 매개변수를 지정하려면 가변 인자를 사용한다. 가변 인자를 정의하려면 매개변수 타입 이름 뒤에 점 세 개(`...`)를 추가한다.

가변 인자로 전달된 값은 함수 본문 내에서 적절한 타입의 배열로 사용할 수 있다. 예를 들어, `numbers`라는 이름의 가변 인자가 `Double...` 타입으로 정의되었다면, 함수 본문 내에서 `[Double]` 타입의 `numbers`라는 상수 배열로 사용할 수 있다.

아래 예제는 임의의 길이를 가진 숫자 목록의 *산술 평균*(*평균*)을 계산한다:

```swift
func arithmeticMean(_ numbers: Double...) -> Double {
    var total: Double = 0
    for number in numbers {
        total += number
    }
    return total / Double(numbers.count)
}
arithmeticMean(1, 2, 3, 4, 5)
// 이 다섯 숫자의 산술 평균인 3.0을 반환한다
arithmeticMean(3, 8.25, 18.75)
// 이 세 숫자의 산술 평균인 10.0을 반환한다
```

<!--
  - test: `variadicParameters`

  ```swifttest
  -> func arithmeticMean(_ numbers: Double...) -> Double {
        var total: Double = 0
        for number in numbers {
           total += number
        }
        return total / Double(numbers.count)
     }
  >> let r0 =
  -> arithmeticMean(1, 2, 3, 4, 5)
  /> returns \(r0), which is the arithmetic mean of these five numbers
  </ returns 3.0, which is the arithmetic mean of these five numbers
  >> let r1 =
  -> arithmeticMean(3, 8.25, 18.75)
  /> returns \(r1), which is the arithmetic mean of these three numbers
  </ returns 10.0, which is the arithmetic mean of these three numbers
  ```
-->

<!--
  Rewrite the above to avoid bare expressions.
  Tracking bug is <rdar://problem/35301593>
-->

하나의 함수는 여러 개의 가변 인자를 가질 수 있다. 가변 인자 뒤에 오는 첫 번째 매개변수는 반드시 인자 레이블을 가져야 한다. 이 레이블은 어떤 인자가 가변 인자에 전달되고, 어떤 인자가 가변 인자 뒤의 매개변수에 전달되는지를 명확히 구분한다.

<!--
  - test: `variadic-parameters-and-labels`

  ```swifttest
  // Labeled, immediately after
  >> func f(_ a: Int..., b: String) {}

  // Unlabeled, not immediately after
  >> func g(_ a: Int..., b: String, _ c: Int) {}

  // Multiple
  >> func h(_a: Int..., b: String, _ c: Int..., d: String) {}
  ```
-->

<!--
  - test: `variadic-parameters-and-labels-failure`

  ```swifttest
  // Unlabeled, immediately after
  >> func f(_ a: Int..., _ b: String) {}
  !$ error: a parameter following a variadic parameter requires a label
  !! func f(_ a: Int..., _ b: String) {}
  !! ^
  ```
-->


### 입출력 매개변수

함수의 매개변수는 기본적으로 상수로 취급된다. 함수 내부에서 매개변수의 값을 변경하려고 하면 컴파일 타임 에러가 발생한다. 이는 실수로 매개변수의 값을 변경하는 것을 방지한다. 만약 함수가 매개변수의 값을 수정하고, 그 변경 사항이 함수 호출이 끝난 후에도 유지되도록 하고 싶다면, 해당 매개변수를 *입출력 매개변수*로 정의해야 한다.

입출력 매개변수는 매개변수의 타입 앞에 `inout` 키워드를 붙여서 선언한다. 입출력 매개변수는 함수에 값이 *전달*되고, 함수에 의해 수정된 후, 수정된 값이 함수 밖으로 *반환*되어 원래 값을 대체한다. 입출력 매개변수의 동작과 관련된 컴파일러 최적화에 대한 자세한 내용은 <doc:Declarations#In-Out-Parameters>를 참고한다.

입출력 매개변수에는 변수만 인자로 전달할 수 있다. 상수나 리터럴 값은 수정할 수 없기 때문에 인자로 전달할 수 없다. 입출력 매개변수에 변수를 전달할 때는 변수 이름 앞에 앰퍼샌드(`&`)를 붙여서 함수가 해당 변수를 수정할 수 있음을 나타낸다.

> 참고: 입출력 매개변수는 기본값을 가질 수 없으며, 가변 인자 매개변수는 `inout`으로 표시할 수 없다.

다음은 두 개의 입출력 정수 매개변수 `a`와 `b`를 가진 `swapTwoInts(_:_:)` 함수의 예제이다:

```swift
func swapTwoInts(_ a: inout Int, _ b: inout Int) {
    let temporaryA = a
    a = b
    b = temporaryA
}
```

<!--
  - test: `inoutParameters`

  ```swifttest
  -> func swapTwoInts(_ a: inout Int, _ b: inout Int) {
        let temporaryA = a
        a = b
        b = temporaryA
     }
  ```
-->

`swapTwoInts(_:_:)` 함수는 단순히 `b`의 값을 `a`에, `a`의 값을 `b`에 교환한다. 이 함수는 `a`의 값을 `temporaryA`라는 임시 상수에 저장하고, `b`의 값을 `a`에 할당한 다음, `temporaryA`의 값을 `b`에 할당하여 교환을 수행한다.

`swapTwoInts(_:_:)` 함수를 호출할 때 `Int` 타입의 두 변수를 전달하여 값을 교환할 수 있다. `someInt`와 `anotherInt`의 이름 앞에 앰퍼샌드(`&`)를 붙여서 함수에 전달한다:

```swift
var someInt = 3
var anotherInt = 107
swapTwoInts(&someInt, &anotherInt)
print("someInt is now \(someInt), and anotherInt is now \(anotherInt)")
// Prints "someInt is now 107, and anotherInt is now 3"
```

<!--
  - test: `inoutParameters`

  ```swifttest
  -> var someInt = 3
  -> var anotherInt = 107
  -> swapTwoInts(&someInt, &anotherInt)
  -> print("someInt is now \(someInt), and anotherInt is now \(anotherInt)")
  <- someInt is now 107, and anotherInt is now 3
  ```
-->

위 예제는 `someInt`와 `anotherInt`의 원래 값이 `swapTwoInts(_:_:)` 함수에 의해 수정되는 것을 보여준다. 이 값들은 원래 함수 외부에서 정의되었지만, 함수 내에서 변경되었다.

> 참고: 입출력 매개변수는 함수에서 값을 반환하는 것과 다르다. 위의 `swapTwoInts` 예제는 반환 타입을 정의하지 않았고 값을 반환하지도 않았지만, `someInt`와 `anotherInt`의 값을 수정했다. 입출력 매개변수는 함수가 함수 본문의 범위를 벗어나서 영향을 미칠 수 있는 또 다른 방법이다.

<!--
  TODO: you can pass a subproperty of something as an inout reference.
  Would be great to show an example of this as a way to avoid temporary variables.
-->


## 함수 타입

모든 함수는 특정한 *함수 타입*을 가진다. 이 타입은 함수의 매개변수 타입과 반환 타입으로 구성된다.

예를 들어:

```swift
func addTwoInts(_ a: Int, _ b: Int) -> Int {
    return a + b
}
func multiplyTwoInts(_ a: Int, _ b: Int) -> Int {
    return a * b
}
```

<!--
  - test: `functionTypes`

  ```swifttest
  -> func addTwoInts(_ a: Int, _ b: Int) -> Int {
        return a + b
     }
  >> print(type(of: addTwoInts))
  << (Int, Int) -> Int
  -> func multiplyTwoInts(_ a: Int, _ b: Int) -> Int {
        return a * b
     }
  >> print(type(of: multiplyTwoInts))
  << (Int, Int) -> Int
  ```
-->

이 예제는 `addTwoInts`와 `multiplyTwoInts`라는 두 개의 간단한 수학 함수를 정의한다. 이 함수들은 각각 두 개의 `Int` 값을 받아서 적절한 수학 연산을 수행한 결과를 `Int` 값으로 반환한다.

이 두 함수의 타입은 `(Int, Int) -> Int`이다. 이는 다음과 같이 읽을 수 있다:

"두 개의 `Int` 타입 매개변수를 가지고 `Int` 타입의 값을 반환하는 함수."

다음은 매개변수와 반환 값이 없는 함수의 예제이다:

```swift
func printHelloWorld() {
    print("hello, world")
}
```

<!--
  - test: `functionTypes`

  ```swifttest
  -> func printHelloWorld() {
        print("hello, world")
     }
  >> print(type(of: printHelloWorld))
  << () -> ()
  ```
-->

이 함수의 타입은 `() -> Void`이다. 이는 "매개변수가 없고 `Void`를 반환하는 함수"라고 읽을 수 있다.


### 함수 타입 사용하기

Swift에서 함수 타입은 다른 타입과 동일하게 사용한다. 예를 들어, 상수나 변수를 함수 타입으로 정의하고 해당 변수에 적절한 함수를 할당할 수 있다:

```swift
var mathFunction: (Int, Int) -> Int = addTwoInts
```

<!--
  - test: `functionTypes`

  ```swifttest
  -> var mathFunction: (Int, Int) -> Int = addTwoInts
  ```
-->

이 코드는 다음과 같이 해석할 수 있다:

"`mathFunction`이라는 변수를 정의한다. 이 변수는 두 개의 `Int` 값을 받아서 `Int` 값을 반환하는 함수 타입이다. 이 새로운 변수에 `addTwoInts`라는 함수를 참조하도록 설정한다."

`addTwoInts(_:_:)` 함수는 `mathFunction` 변수와 동일한 타입을 가지므로, Swift의 타입 검사기는 이 할당을 허용한다.

이제 `mathFunction`이라는 이름으로 할당된 함수를 호출할 수 있다:

```swift
print("Result: \(mathFunction(2, 3))")
// Prints "Result: 5"
```

<!--
  - test: `functionTypes`

  ```swifttest
  -> print("Result: \(mathFunction(2, 3))")
  <- Result: 5
  ```
-->

동일한 타입을 가진 다른 함수도 비함수 타입과 마찬가지로 같은 변수에 할당할 수 있다:

```swift
mathFunction = multiplyTwoInts
print("Result: \(mathFunction(2, 3))")
// Prints "Result: 6"
```

<!--
  - test: `functionTypes`

  ```swifttest
  -> mathFunction = multiplyTwoInts
  -> print("Result: \(mathFunction(2, 3))")
  <- Result: 6
  ```
-->

다른 타입과 마찬가지로, 함수를 상수나 변수에 할당할 때 Swift가 함수 타입을 추론하도록 할 수도 있다:

```swift
let anotherMathFunction = addTwoInts
// anotherMathFunction은 (Int, Int) -> Int 타입으로 추론된다
```

<!--
  - test: `functionTypes`

  ```swifttest
  -> let anotherMathFunction = addTwoInts
  >> print(type(of: anotherMathFunction))
  << (Int, Int) -> Int
  // anotherMathFunction is inferred to be of type (Int, Int) -> Int
  ```
-->


### 함수 타입을 매개변수 타입으로 사용하기

`(Int, Int) -> Int`와 같은 함수 타입을 다른 함수의 매개변수 타입으로 사용할 수 있다. 이를 통해 함수의 일부 구현을 호출자가 함수를 호출할 때 제공하도록 할 수 있다.

다음은 위에서 정의한 수학 함수의 결과를 출력하는 예제이다:

```swift
func printMathResult(_ mathFunction: (Int, Int) -> Int, _ a: Int, _ b: Int) {
    print("Result: \(mathFunction(a, b))")
}
printMathResult(addTwoInts, 3, 5)
// Prints "Result: 8"
```

<!--
  - test: `functionTypes`

  ```swifttest
  -> func printMathResult(_ mathFunction: (Int, Int) -> Int, _ a: Int, _ b: Int) {
        print("Result: \(mathFunction(a, b))")
     }
  -> printMathResult(addTwoInts, 3, 5)
  <- Result: 8
  ```
-->

이 예제는 `printMathResult(_:_:_:)`라는 함수를 정의한다. 이 함수는 세 개의 매개변수를 가진다. 첫 번째 매개변수는 `mathFunction`이라고 하며, 타입은 `(Int, Int) -> Int`이다. 이 첫 번째 매개변수로 해당 타입의 어떤 함수든 전달할 수 있다. 두 번째와 세 번째 매개변수는 각각 `a`와 `b`라고 하며, 둘 다 `Int` 타입이다. 이 두 값은 제공된 수학 함수의 입력 값으로 사용된다.

`printMathResult(_:_:_:)`를 호출할 때, `addTwoInts(_:_:)` 함수와 정수 값 `3`과 `5`를 전달한다. 이 함수는 `3`과 `5`를 사용해 제공된 함수를 호출하고, 결과 값 `8`을 출력한다.

`printMathResult(_:_:_:)`의 역할은 적절한 타입의 수학 함수 호출 결과를 출력하는 것이다. 이 함수의 실제 구현이 무엇인지는 중요하지 않다. 단지 함수가 올바른 타입이기만 하면 된다. 이를 통해 `printMathResult(_:_:_:)`는 타입 안전한 방식으로 일부 기능을 함수 호출자에게 넘길 수 있다.


### 함수 타입을 반환 타입으로 사용하기

함수 타입을 다른 함수의 반환 타입으로 사용할 수 있다. 이를 위해 반환 화살표(`->`) 뒤에 완전한 함수 타입을 작성한다.

다음 예제는 `stepForward(_:)`와 `stepBackward(_:)`라는 두 가지 간단한 함수를 정의한다. `stepForward(_:)` 함수는 입력값보다 1 큰 값을 반환하고, `stepBackward(_:)` 함수는 입력값보다 1 작은 값을 반환한다. 두 함수 모두 `(Int) -> Int` 타입을 가진다:

```swift
func stepForward(_ input: Int) -> Int {
    return input + 1
}
func stepBackward(_ input: Int) -> Int {
    return input - 1
}
```

<!--
  - test: `functionTypes`

  ```swifttest
  -> func stepForward(_ input: Int) -> Int {
        return input + 1
     }
  -> func stepBackward(_ input: Int) -> Int {
        return input - 1
     }
  ```
-->

다음은 `chooseStepFunction(backward:)`라는 함수로, 반환 타입이 `(Int) -> Int`이다. 이 함수는 `backward`라는 불리언 매개변수를 기반으로 `stepForward(_:)` 함수 또는 `stepBackward(_:)` 함수를 반환한다:

```swift
func chooseStepFunction(backward: Bool) -> (Int) -> Int {
    return backward ? stepBackward : stepForward
}
```

<!--
  - test: `functionTypes`

  ```swifttest
  -> func chooseStepFunction(backward: Bool) -> (Int) -> Int {
        return backward ? stepBackward : stepForward
     }
  ```
-->

이제 `chooseStepFunction(backward:)`를 사용해 한 방향으로 이동하는 함수를 얻을 수 있다:

```swift
var currentValue = 3
let moveNearerToZero = chooseStepFunction(backward: currentValue > 0)
// moveNearerToZero는 이제 stepBackward() 함수를 참조한다
```

<!--
  - test: `functionTypes`

  ```swifttest
  -> var currentValue = 3
  -> let moveNearerToZero = chooseStepFunction(backward: currentValue > 0)
  >> print(type(of: moveNearerToZero))
  << (Int) -> Int
  // moveNearerToZero는 이제 stepBackward() 함수를 참조한다
  ```
-->

위 예제는 `currentValue`라는 변수를 점점 0에 가깝게 이동시키기 위해 양수 또는 음수 단계가 필요한지 결정한다. `currentValue`의 초기값은 `3`이므로 `currentValue > 0`은 `true`를 반환하고, 이에 따라 `chooseStepFunction(backward:)`는 `stepBackward(_:)` 함수를 반환한다. 반환된 함수의 참조는 `moveNearerToZero`라는 상수에 저장된다.

이제 `moveNearerToZero`가 올바른 함수를 참조하므로 이를 사용해 0까지 세는 것이 가능하다:

```swift
print("Counting to zero:")
// Counting to zero:
while currentValue != 0 {
    print("\(currentValue)... ")
    currentValue = moveNearerToZero(currentValue)
}
print("zero!")
// 3...
// 2...
// 1...
// zero!
```

<!--
  - test: `functionTypes`

  ```swifttest
  -> print("Counting to zero:")
  </ Counting to zero:
  -> while currentValue != 0 {
        print("\(currentValue)... ")
        currentValue = moveNearerToZero(currentValue)
     }
  -> print("zero!")
  </ 3...
  </ 2...
  </ 1...
  </ zero!
  ```
-->


## 중첩 함수

이번 장에서 여러분이 접한 모든 함수는 *전역 함수*의 예제였다. 이 함수들은 전역 범위에서 정의된다. 하지만 다른 함수의 본문 안에서도 함수를 정의할 수 있는데, 이를 *중첩 함수*라고 부른다.

중첩 함수는 기본적으로 외부에서 접근할 수 없지만, 이를 감싸는 함수 내에서는 호출하고 사용할 수 있다. 감싸는 함수는 중첩 함수 중 하나를 반환할 수도 있으며, 이렇게 하면 중첩 함수를 다른 범위에서 사용할 수 있게 된다.

앞서 살펴본 `chooseStepFunction(backward:)` 예제를 중첩 함수를 사용하고 반환하도록 다시 작성할 수 있다:

```swift
func chooseStepFunction(backward: Bool) -> (Int) -> Int {
    func stepForward(input: Int) -> Int { return input + 1 }
    func stepBackward(input: Int) -> Int { return input - 1 }
    return backward ? stepBackward : stepForward
}
var currentValue = -4
let moveNearerToZero = chooseStepFunction(backward: currentValue > 0)
// moveNearerToZero는 이제 중첩 함수 stepForward()를 참조한다
while currentValue != 0 {
    print("\(currentValue)... ")
    currentValue = moveNearerToZero(currentValue)
}
print("zero!")
// -4...
// -3...
// -2...
// -1...
// zero!
```

<!--
  - test: `nestedFunctions`

  ```swifttest
  -> func chooseStepFunction(backward: Bool) -> (Int) -> Int {
        func stepForward(input: Int) -> Int { return input + 1 }
        func stepBackward(input: Int) -> Int { return input - 1 }
        return backward ? stepBackward : stepForward
     }
  -> var currentValue = -4
  -> let moveNearerToZero = chooseStepFunction(backward: currentValue > 0)
  >> print(type(of: moveNearerToZero))
  << (Int) -> Int
  // moveNearerToZero now refers to the nested stepForward() function
  -> while currentValue != 0 {
        print("\(currentValue)... ")
        currentValue = moveNearerToZero(currentValue)
     }
  -> print("zero!")
  </ -4...
  </ -3...
  </ -2...
  </ -1...
  </ zero!
  ```
-->

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


