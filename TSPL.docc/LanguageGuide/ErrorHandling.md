# 에러 처리

프로그램에서 발생하는 에러 상황에 대응하고 복구하는 방법을 알아본다.

*에러 처리*는 프로그램 실행 중 발생한 에러 상황에 대응하고 복구하는 과정이다. Swift는 런타임에서 복구 가능한 에러를 던지고, 잡고, 전파하고, 조작하는 퍼스트클래스 기능을 제공한다.

특정 작업은 항상 완료되거나 유용한 결과를 보장하지 않는다. 옵셔널은 값이 없음을 나타내는 데 사용하지만, 작업이 실패할 때 실패 원인을 이해하는 것이 중요하다. 이를 통해 코드가 적절히 대응할 수 있다.

예를 들어, 디스크에 있는 파일을 읽고 처리하는 작업을 생각해 보자. 이 작업은 여러 이유로 실패할 수 있다. 지정된 경로에 파일이 없거나, 읽기 권한이 없거나, 호환되지 않는 형식으로 인코딩된 경우 등이 있다. 이러한 다양한 상황을 구분하면 프로그램은 일부 에러를 해결하고, 해결할 수 없는 에러는 사용자에게 알릴 수 있다.

> 참고: Swift의 에러 처리는 Cocoa와 Objective-C에서 `NSError` 클래스를 사용하는 에러 처리 패턴과 상호 운용된다. 이 클래스에 대한 자세한 내용은 [Swift에서 Cocoa 에러 처리](https://developer.apple.com/documentation/swift/cocoa_design_patterns/handling_cocoa_errors_in_swift)를 참고한다.


## 오류 표현과 발생

Swift에서 오류는 `Error` 프로토콜을 준수하는 타입의 값으로 표현된다. 이 프로토콜은 해당 타입이 오류 처리에 사용될 수 있음을 나타낸다.

Swift의 열거형은 특히 관련된 오류 조건들을 모델링하는 데 적합하다. 연관된 값을 통해 오류의 특성에 대한 추가 정보를 전달할 수 있다. 예를 들어, 게임 내 자판기를 작동시키는 과정에서 발생할 수 있는 오류 조건을 다음과 같이 표현할 수 있다:

```swift
enum VendingMachineError: Error {
    case invalidSelection
    case insufficientFunds(coinsNeeded: Int)
    case outOfStock
}
```

<!--
  - test: `throw-enum-error`

  ```swifttest
  -> enum VendingMachineError: Error {
         case invalidSelection
         case insufficientFunds(coinsNeeded: Int)
         case outOfStock
     }
  ```
-->

오류를 발생시키면 예기치 않은 상황이 발생했음을 알리고, 일반적인 실행 흐름을 계속할 수 없음을 나타낼 수 있다. `throw` 문을 사용해 오류를 발생시킨다. 예를 들어, 다음 코드는 자판기에 추가로 5개의 동전이 필요하다는 오류를 발생시킨다:

```swift
throw VendingMachineError.insufficientFunds(coinsNeeded: 5)
```

<!--
  - test: `throw-enum-error`

  ```swifttest
  -> throw VendingMachineError.insufficientFunds(coinsNeeded: 5)
  xx fatal error
  ```
-->


## 에러 처리

에러가 발생하면, 
해당 에러를 처리할 주변 코드가 반드시 필요하다.
예를 들어, 문제를 수정하거나, 
다른 방법을 시도하거나, 
사용자에게 실패를 알리는 등의 방식으로 처리할 수 있다.

Swift에서는 에러를 처리하는 네 가지 방법이 있다.
함수에서 발생한 에러를 호출한 코드로 전파하거나, 
`do`-`catch` 문을 사용해 에러를 처리하거나, 
에러를 옵셔널 값으로 처리하거나, 
에러가 발생하지 않을 것이라고 단언하는 방법이 있다. 
각 방법은 아래 섹션에서 자세히 설명한다.

함수가 에러를 던지면 프로그램의 흐름이 바뀌기 때문에, 
에러를 던질 수 있는 코드 위치를 빠르게 파악하는 것이 중요하다. 
에러를 던질 수 있는 함수, 메서드, 또는 초기화 구문을 호출하는 코드 앞에 
`try` 키워드 또는 `try?`, `try!` 변형을 작성하면 
이 위치를 쉽게 식별할 수 있다. 
이 키워드들은 아래 섹션에서 설명한다.

> 참고: Swift의 에러 처리는 다른 언어의 예외 처리와 유사하며, 
> `try`, `catch`, `throw` 키워드를 사용한다. 
> 하지만 Objective-C를 포함한 많은 언어와 달리, 
> Swift의 에러 처리는 호출 스택을 되감는 과정을 포함하지 않는다. 
> 이 과정은 계산 비용이 많이 들 수 있다. 
> 따라서 `throw` 문의 성능 특성은 `return` 문과 유사하다.


### 에러를 전파하는 Throwing 함수 사용

함수, 메서드, 또는 초기화 구문이 에러를 던질 수 있음을 나타내려면, 매개변수 뒤에 `throws` 키워드를 추가한다. `throws`로 표시된 함수를 *throwing 함수*라고 부른다. 함수가 반환 타입을 지정하는 경우, `throws` 키워드를 반환 화살표(`->`) 앞에 작성한다.

```swift
func canThrowErrors() throws -> String

func cannotThrowErrors() -> String
```

Throwing 함수는 내부에서 발생한 에러를 호출한 스코프로 전파한다.

> 주의: 오직 throwing 함수만이 에러를 전파할 수 있다. nonthrowing 함수 내부에서 발생한 에러는 반드시 함수 내부에서 처리해야 한다.

아래 예제에서 `VendingMachine` 클래스는 `vend(itemNamed:)` 메서드를 가지고 있다. 이 메서드는 요청한 아이템이 없거나, 재고가 부족하거나, 현재 입금된 금액을 초과하는 경우 적절한 `VendingMachineError`를 던진다.

```swift
struct Item {
    var price: Int
    var count: Int
}

class VendingMachine {
    var inventory = [
        "Candy Bar": Item(price: 12, count: 7),
        "Chips": Item(price: 10, count: 4),
        "Pretzels": Item(price: 7, count: 11)
    ]
    var coinsDeposited = 0

    func vend(itemNamed name: String) throws {
        guard let item = inventory[name] else {
            throw VendingMachineError.invalidSelection
        }

        guard item.count > 0 else {
            throw VendingMachineError.outOfStock
        }

        guard item.price <= coinsDeposited else {
            throw VendingMachineError.insufficientFunds(coinsNeeded: item.price - coinsDeposited)
        }

        coinsDeposited -= item.price

        var newItem = item
        newItem.count -= 1
        inventory[name] = newItem

        print("Dispensing \(name)")
    }
}
```

`vend(itemNamed:)` 메서드는 `guard` 구문을 사용해 스낵 구매 요구 사항이 충족되지 않으면 메서드를 조기에 종료하고 적절한 에러를 던진다. `throw` 구문은 프로그램 제어를 즉시 전달하므로, 모든 요구 사항이 충족된 경우에만 아이템이 판매된다.

`vend(itemNamed:)` 메서드는 던지는 에러를 전파하므로, 이 메서드를 호출하는 코드는 `do`-`catch` 구문, `try?`, 또는 `try!`를 사용해 에러를 처리하거나 계속 전파해야 한다. 예를 들어, 아래 예제의 `buyFavoriteSnack(person:vendingMachine:)` 함수도 throwing 함수이며, `vend(itemNamed:)` 메서드가 던지는 에러는 `buyFavoriteSnack(person:vendingMachine:)` 함수가 호출된 지점까지 전파된다.

```swift
let favoriteSnacks = [
    "Alice": "Chips",
    "Bob": "Licorice",
    "Eve": "Pretzels",
]
func buyFavoriteSnack(person: String, vendingMachine: VendingMachine) throws {
    let snackName = favoriteSnacks[person] ?? "Candy Bar"
    try vendingMachine.vend(itemNamed: snackName)
}
```

이 예제에서 `buyFavoriteSnack(person: vendingMachine:)` 함수는 주어진 사람이 좋아하는 스낵을 찾아 `vend(itemNamed:)` 메서드를 호출해 구매를 시도한다. `vend(itemNamed:)` 메서드는 에러를 던질 수 있으므로, 앞에 `try` 키워드를 붙여 호출한다.

Throwing 초기화 구문도 throwing 함수와 같은 방식으로 에러를 전파할 수 있다. 예를 들어, 아래 목록의 `PurchasedSnack` 구조체의 초기화 구문은 초기화 과정에서 throwing 함수를 호출하며, 발생한 에러를 호출자에게 전파한다.

```swift
struct PurchasedSnack {
    let name: String
    init(name: String, vendingMachine: VendingMachine) throws {
        try vendingMachine.vend(itemNamed: name)
        self.name = name
    }
}
```


### Do-Catch를 사용한 에러 처리

`do`-`catch` 문을 사용하면 특정 코드 블록을 실행하면서 발생할 수 있는 에러를 처리할 수 있다. `do` 절 내의 코드에서 에러가 발생하면, 해당 에러는 `catch` 절과 비교되어 어떤 절이 에러를 처리할지 결정된다.

다음은 `do`-`catch` 문의 일반적인 형태이다:

```swift
do {
    try <#expression#>
    <#statements#>
} catch <#pattern 1#> {
    <#statements#>
} catch <#pattern 2#> where <#condition#> {
    <#statements#>
} catch <#pattern 3#>, <#pattern 4#> where <#condition#> {
    <#statements#>
} catch {
    <#statements#>
}
```

`catch` 뒤에 패턴을 작성하여 해당 절이 어떤 에러를 처리할지 지정한다. 만약 `catch` 절에 패턴이 없다면, 해당 절은 모든 에러와 일치하며 에러를 `error`라는 로컬 상수에 바인딩한다. 패턴 매칭에 대한 자세한 내용은 <doc:Patterns>를 참고한다.

예를 들어, 다음 코드는 `VendingMachineError` 열거형의 세 가지 케이스에 대해 에러를 처리한다.

```swift
var vendingMachine = VendingMachine()
vendingMachine.coinsDeposited = 8
do {
    try buyFavoriteSnack(person: "Alice", vendingMachine: vendingMachine)
    print("Success! Yum.")
} catch VendingMachineError.invalidSelection {
    print("Invalid Selection.")
} catch VendingMachineError.outOfStock {
    print("Out of Stock.")
} catch VendingMachineError.insufficientFunds(let coinsNeeded) {
    print("Insufficient funds. Please insert an additional \(coinsNeeded) coins.")
} catch {
    print("Unexpected error: \(error).")
}
// Prints "Insufficient funds. Please insert an additional 2 coins."
```

위 예제에서 `buyFavoriteSnack(person:vendingMachine:)` 함수는 에러를 던질 수 있으므로 `try` 표현식으로 호출된다. 만약 에러가 발생하면 실행은 즉시 `catch` 절로 이동하며, 해당 절이 에러를 처리할지 결정한다. 어떤 패턴도 일치하지 않으면 마지막 `catch` 절이 에러를 잡아 `error`라는 로컬 상수에 바인딩한다. 에러가 발생하지 않으면 `do` 문의 나머지 구문이 실행된다.

`catch` 절은 `do` 절에서 발생할 수 있는 모든 에러를 처리할 필요는 없다. 만약 어떤 `catch` 절도 에러를 처리하지 않으면, 에러는 주변 스코프로 전파된다. 그러나 전파된 에러는 반드시 *어떤* 주변 스코프에서 처리되어야 한다. 에러를 던지지 않는 함수에서는 `do`-`catch` 문이 에러를 처리해야 한다. 에러를 던지는 함수에서는 `do`-`catch` 문이나 호출자가 에러를 처리해야 한다. 에러가 최상위 스코프까지 전파되면서 처리되지 않으면 런타임 에러가 발생한다.

예를 들어, 위 예제를 수정하여 `VendingMachineError`가 아닌 에러는 호출 함수에서 처리하도록 할 수 있다:

```swift
func nourish(with item: String) throws {
    do {
        try vendingMachine.vend(itemNamed: item)
    } catch is VendingMachineError {
        print("Couldn't buy that from the vending machine.")
    }
}

do {
    try nourish(with: "Beet-Flavored Chips")
} catch {
    print("Unexpected non-vending-machine-related error: \(error)")
}
// Prints "Couldn't buy that from the vending machine."
```

`nourish(with:)` 함수에서 `vend(itemNamed:)`가 `VendingMachineError` 열거형의 케이스 중 하나를 던지면, `nourish(with:)`는 에러를 처리하여 메시지를 출력한다. 그렇지 않으면 `nourish(with:)`는 에러를 호출 지점으로 전파한다. 이후 에러는 일반 `catch` 절에서 잡힌다.

여러 관련 에러를 처리하는 또 다른 방법은 `catch` 뒤에 쉼표로 구분하여 나열하는 것이다. 예를 들어:

```swift
func eat(item: String) throws {
    do {
        try vendingMachine.vend(itemNamed: item)
    } catch VendingMachineError.invalidSelection, VendingMachineError.insufficientFunds, VendingMachineError.outOfStock {
        print("Invalid selection, out of stock, or not enough money.")
    }
}
```

`eat(item:)` 함수는 자판기 에러를 처리할 목록을 나열하며, 에러 메시지는 해당 목록에 맞춰 출력된다. 나열된 세 가지 에러 중 하나가 발생하면 이 `catch` 절이 에러를 처리하여 메시지를 출력한다. 다른 모든 에러는 주변 스코프로 전파되며, 이후 추가될 수 있는 자판기 에러도 포함된다.


### 에러를 옵셔널 값으로 변환하기

`try?`를 사용하면 에러를 처리하면서 옵셔널 값으로 변환할 수 있다. `try?` 표현식을 평가하는 도중 에러가 발생하면, 해당 표현식의 값은 `nil`이 된다. 예를 들어, 다음 코드에서 `x`와 `y`는 동일한 값과 동작을 가진다:

```swift
func someThrowingFunction() throws -> Int {
    // ...
}

let x = try? someThrowingFunction()

let y: Int?
do {
    y = try someThrowingFunction()
} catch {
    y = nil
}
```

<!--
  - test: `optional-try`

  ```swifttest
  -> func someThrowingFunction() throws -> Int {
        // ...
  >>    return 40
  -> }

  -> let x = try? someThrowingFunction()
  >> print(x as Any)
  << Optional(40)

  -> let y: Int?
     do {
         y = try someThrowingFunction()
     } catch {
         y = nil
     }
  >> print(y as Any)
  << Optional(40)
  ```
-->

만약 `someThrowingFunction()`에서 에러가 발생하면, `x`와 `y`의 값은 `nil`이 된다. 그렇지 않으면, `x`와 `y`의 값은 함수가 반환한 값이 된다. 여기서 `x`와 `y`는 `someThrowingFunction()`이 반환하는 타입의 옵셔널이다. 이 함수는 정수를 반환하므로, `x`와 `y`는 옵셔널 정수 타입이다.

`try?`를 사용하면 모든 에러를 동일한 방식으로 처리할 때 간결한 코드를 작성할 수 있다. 예를 들어, 다음 코드는 여러 방법으로 데이터를 가져오려고 시도하고, 모든 방법이 실패하면 `nil`을 반환한다:

```swift
func fetchData() -> Data? {
    if let data = try? fetchDataFromDisk() { return data }
    if let data = try? fetchDataFromServer() { return data }
    return nil
}
```

<!--
  - test: `optional-try-cached-data`

  ```swifttest
  >> struct Data {}
  >> func fetchDataFromDisk() throws -> Data { return Data() }
  >> func fetchDataFromServer() throws -> Data { return Data() }
  -> func fetchData() -> Data? {
         if let data = try? fetchDataFromDisk() { return data }
         if let data = try? fetchDataFromServer() { return data }
         return nil
     }
  ```
-->


### 에러 전파 비활성화

때로는 특정 함수나 메서드가 실제로 런타임에 에러를 던지지 않는다는 것을 알고 있는 경우가 있다. 이럴 때는 `try!`를 사용해 에러 전파를 비활성화하고, 해당 호출이 에러를 던지지 않을 것이라는 런타임 단언을 추가할 수 있다. 만약 실제로 에러가 발생하면 런타임 에러가 발생한다.

예를 들어, 다음 코드는 `loadImage(atPath:)` 함수를 사용한다. 이 함수는 주어진 경로에서 이미지 리소스를 불러오거나, 이미지를 불러올 수 없을 때 에러를 던진다. 이 경우, 이미지가 애플리케이션과 함께 배포되기 때문에 런타임에 에러가 발생하지 않는다. 따라서 에러 전파를 비활성화하는 것이 적절하다.

```swift
let photo = try! loadImage(atPath: "./Resources/John Appleseed.jpg")
```

<!--
  - test: `forceTryStatement`

  ```swifttest
  >> struct Image {}
  >> func loadImage(atPath path: String) throws -> Image {
  >>     return Image()
  >> }
  -> let photo = try! loadImage(atPath: "./Resources/John Appleseed.jpg")
  ```
-->


## 에러 타입 지정하기

위 예제들은 모두 가장 일반적인 에러 처리 방식을 보여준다. 이 방식에서는 코드가 던지는 에러가 `Error` 프로토콜을 준수하는 모든 타입의 값이 될 수 있다. 이 접근 방식은 코드가 실행되는 동안 발생할 수 있는 모든 에러를 미리 알 수 없는 현실과 잘 맞는다. 특히 다른 곳에서 던져진 에러를 전파할 때 더욱 그렇다. 또한 에러가 시간이 지남에 따라 변할 수 있다는 사실도 반영한다. 라이브러리의 새 버전(의존성으로 사용하는 라이브러리 포함)이 새로운 에러를 던질 수 있고, 실제 사용자 설정의 복잡성 때문에 개발이나 테스트 중에는 보이지 않던 실패 모드가 드러날 수 있다. 위 예제들의 에러 처리 코드는 항상 특정 `catch` 절이 없는 에러를 처리하기 위해 기본 케이스를 포함한다.

대부분의 Swift 코드는 던지는 에러의 타입을 지정하지 않는다. 하지만 다음과 같은 특별한 경우에는 코드가 특정 타입의 에러만 던지도록 제한할 수 있다:

- 동적 메모리 할당을 지원하지 않는 임베디드 시스템에서 코드를 실행할 때. `any Error`나 다른 박스형 프로토콜 타입의 인스턴스를 던지면 런타임에 에러를 저장하기 위해 메모리를 할당해야 한다. 반면, 특정 타입의 에러를 던지면 Swift가 힙 할당을 피할 수 있다.

- 에러가 라이브러리 같은 코드 단위의 구현 세부 사항이고, 그 코드의 인터페이스의 일부가 아닐 때. 에러가 라이브러리에서만 발생하고 다른 의존성이나 라이브러리의 클라이언트에서 발생하지 않는다면, 모든 가능한 실패를 완전히 나열할 수 있다. 그리고 이 에러들이 라이브러리의 구현 세부 사항이기 때문에 항상 그 라이브러리 내에서 처리된다.

- 제네릭 매개변수로 설명된 에러만 전파하는 코드에서. 예를 들어, 클로저 인수를 받아 그 클로저에서 발생하는 모든 에러를 전파하는 함수가 있다. 특정 에러 타입을 전파하는 것과 `rethrows`를 사용하는 것의 비교는 <doc:Declarations#Rethrowing-Functions-and-Methods>를 참고한다.

예를 들어, 평점을 요약하고 다음 에러 타입을 사용하는 코드를 생각해 보자:

```swift
enum StatisticsError: Error {
    case noRatings
    case invalidRating(Int)
}
```

함수가 `StatisticsError` 값만 에러로 던지도록 지정하려면, 함수를 선언할 때 `throws` 대신 `throws(StatisticsError)`를 작성한다. 이 구문은 선언에서 `throws` 뒤에 에러 타입을 작성하기 때문에 *타입 지정 throws*라고도 한다. 예를 들어, 아래 함수는 `StatisticsError` 값을 에러로 던진다.

```swift
func summarize(_ ratings: [Int]) throws(StatisticsError) {
    guard !ratings.isEmpty else { throw .noRatings }

    var counts = [1: 0, 2: 0, 3: 0]
    for rating in ratings {
        guard rating > 0 && rating <= 3 else { throw .invalidRating(rating) }
        counts[rating]! += 1
    }

    print("*", counts[1]!, "-- **", counts[2]!, "-- ***", counts[3]!)
}
```

위 코드에서 `summarize(_:)` 함수는 1부터 3까지의 척도로 표현된 평점 목록을 요약한다. 이 함수는 입력이 유효하지 않으면 `StatisticsError` 인스턴스를 던진다. 위 코드에서 에러를 던지는 두 곳 모두 에러 타입을 생략한다. 왜냐하면 함수의 에러 타입이 이미 정의되어 있기 때문이다. 이와 같은 함수에서 에러를 던질 때 `throw StatisticsError.noRatings` 대신 짧은 형태인 `throw .noRatings`를 사용할 수 있다.

함수 시작 부분에 특정 에러 타입을 작성하면 Swift는 다른 에러를 던지지 않도록 검사한다. 예를 들어, 위의 `summarize(_:)` 함수에서 이 장의 앞부분 예제에서 사용한 `VendingMachineError`를 사용하려고 하면, 그 코드는 컴파일 시간에 에러를 발생시킨다.

타입 지정 throws를 사용하는 함수를 일반적인 throwing 함수 내에서 호출할 수 있다:

```swift
func someThrowingFunction() throws {
    let ratings = [1, 2, 3, 2, 2, 1]
    try summarize(ratings)
}
```

위 코드는 `someThrowingFunction()`에 대해 에러 타입을 지정하지 않았으므로 `any Error`를 던진다. 에러 타입을 명시적으로 `throws(any Error)`로 작성할 수도 있다. 아래 코드는 위 코드와 동일하다:

```swift
func someThrowingFunction() throws(any Error) {
    let ratings = [1, 2, 3, 2, 2, 1]
    try summarize(ratings)
}
```

이 코드에서 `someThrowingFunction()`은 `summarize(_:)`가 던지는 모든 에러를 전파한다. `summarize(_:)`의 에러는 항상 `StatisticsError` 값이며, 이는 `someThrowingFunction()`이 던질 수 있는 유효한 에러이기도 하다.

반환 타입이 `Never`인 함수를 작성할 수 있는 것처럼, `throws(Never)`를 사용하여 절대 에러를 던지지 않는 함수를 작성할 수 있다:

```swift
func nonThrowingFunction() throws(Never) {
  // ...
}
```

이 함수는 `Never` 타입의 값을 생성하여 던질 수 없기 때문에 에러를 던질 수 없다.

함수의 에러 타입을 지정하는 것 외에, `do`-`catch` 문에 대해 특정 에러 타입을 작성할 수도 있다. 예를 들어:

```swift
let ratings = []
do throws(StatisticsError) {
    try summarize(ratings)
} catch {
    switch error {
    case .noRatings:
        print("No ratings available")
    case .invalidRating(let rating):
        print("Invalid rating: \(rating)")
    }
}
// Prints "No ratings available"
```

이 코드에서 `do throws(StatisticsError)`를 작성하면 `do`-`catch` 문이 `StatisticsError` 값을 에러로 던진다는 것을 나타낸다. 다른 `do`-`catch` 문과 마찬가지로, `catch` 절은 모든 가능한 에러를 처리하거나, 처리되지 않은 에러를 주변 범위에서 처리하도록 전파할 수 있다. 이 코드는 모든 에러를 처리하며, 각 열거형 값에 대해 하나의 케이스를 가진 `switch` 문을 사용한다. 패턴이 없는 다른 `catch` 절과 마찬가지로, 이 절은 모든 에러와 일치하며 에러를 `error`라는 로컬 상수에 바인딩한다. `do`-`catch` 문이 `StatisticsError` 값을 던지기 때문에 `error`는 `StatisticsError` 타입의 값이다.

위 `catch` 절은 `switch` 문을 사용하여 각 가능한 에러를 일치시키고 처리한다. `StatisticsError`에 새 케이스를 추가하고 에러 처리 코드를 업데이트하지 않으면, Swift는 `switch` 문이 더 이상 완전하지 않기 때문에 에러를 발생시킨다. 자신의 모든 에러를 처리하는 라이브러리의 경우, 이 접근 방식을 사용하여 새 에러에 대해 해당하는 새 처리 코드가 있는지 확인할 수 있다.

함수나 `do` 블록이 단일 타입의 에러만 던지면 Swift는 이 코드가 타입 지정 throws를 사용한다고 추론한다. 이 짧은 구문을 사용하면 위의 `do`-`catch` 예제를 다음과 같이 작성할 수 있다:

```swift
let ratings = []
do {
    try summarize(ratings)
} catch {
    switch error {
    case .noRatings:
        print("No ratings available")
    case .invalidRating(let rating):
        print("Invalid rating: \(rating)")
    }
}
// Prints "No ratings available"
```

위 `do`-`catch` 블록은 던지는 에러 타입을 지정하지 않았지만, Swift는 `StatisticsError`를 던진다고 추론한다. Swift가 타입 지정 throws를 추론하지 않도록 하려면 `throws(any Error)`를 명시적으로 작성할 수 있다.


## 정리 작업 지정하기

`defer` 문을 사용하면 코드 실행이 현재 코드 블록을 벗어나기 직전에 특정 문장들을 실행할 수 있다. 이 문장은 현재 코드 블록이 어떤 방식으로 종료되든 상관없이 반드시 수행해야 하는 정리 작업을 처리하는 데 유용하다. 예를 들어, 파일 디스크립터를 닫거나 수동으로 할당한 메모리를 해제하는 작업을 `defer` 문으로 보장할 수 있다.

`defer` 문은 현재 스코프가 종료될 때까지 실행을 지연시킨다. 이 문장은 `defer` 키워드와 나중에 실행될 문장들로 구성된다. 지연된 문장들은 `break`나 `return` 문처럼 제어 흐름을 바꾸는 코드를 포함할 수 없으며, 오류를 던지는 코드도 포함할 수 없다. 지연된 작업은 소스 코드에 작성된 순서의 역순으로 실행된다. 즉, 첫 번째 `defer` 문의 코드가 마지막으로 실행되고, 두 번째 `defer` 문의 코드가 두 번째로 마지막에 실행되는 식이다. 소스 코드에서 마지막에 작성된 `defer` 문이 가장 먼저 실행된다.

```swift
func processFile(filename: String) throws {
    if exists(filename) {
        let file = open(filename)
        defer {
            close(file)
        }
        while let line = try file.readline() {
            // 파일 작업 수행
        }
        // close(file)이 여기서 호출됨, 스코프의 끝에서
    }
}
```

<!--
  - test: `defer`

  ```swifttest
  >> func exists(_ file: String) -> Bool { return true }
  >> struct File {
  >>    func readline() throws -> String? { return nil }
  >> }
  >> func open(_ file: String) -> File { return File() }
  >> func close(_ fileHandle: File) {}
  -> func processFile(filename: String) throws {
        if exists(filename) {
           let file = open(filename)
           defer {
              close(file)
           }
           while let line = try file.readline() {
              // 파일 작업 수행
  >>          print(line)
           }
           // close(file)이 여기서 호출됨, 스코프의 끝에서
        }
     }
  ```
-->

위 예제는 `defer` 문을 사용해 `open(_:)` 함수에 대응하는 `close(_:)` 호출이 반드시 수행되도록 보장한다.

오류 처리 코드가 없더라도 `defer` 문을 사용할 수 있다. 더 많은 정보는 <doc:ControlFlow#Deferred-Actions>를 참고한다.

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


