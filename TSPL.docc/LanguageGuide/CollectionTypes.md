# 컬렉션 타입

배열, 집합, 딕셔너리를 활용해 데이터를 구조화한다.

Swift는 값의 컬렉션을 저장하기 위해 세 가지 주요 *컬렉션 타입*을 제공한다. 이는 배열, 집합, 딕셔너리로 알려져 있다. 배열은 값의 순서 있는 컬렉션이고, 집합은 중복 없는 값의 순서 없는 컬렉션이다. 딕셔너리는 키-값 쌍의 순서 없는 컬렉션이다.

![](CollectionTypes_intro)

Swift의 배열, 집합, 딕셔너리는 저장할 수 있는 값과 키의 타입을 항상 명확히 정의한다. 따라서 잘못된 타입의 값을 실수로 컬렉션에 삽입할 수 없다. 또한 컬렉션에서 어떤 타입의 값을 가져올지 확신할 수 있다.

> 참고: Swift의 배열, 집합, 딕셔너리 타입은 *제네릭 컬렉션*으로 구현된다. 제네릭 타입과 컬렉션에 대한 자세한 내용은 <doc:Generics>를 참고한다.

<!--
  TODO: should I mention the Collection protocol, to which both of these conform?
-->

<!--
  TODO: mention for i in indices(collection) { collection[i] }
-->

<!--
  TODO: discuss collection equality
-->


## 컬렉션의 변경 가능성

배열, 집합, 또는 딕셔너리를 생성하고 변수에 할당하면, 해당 컬렉션은 *변경 가능* 상태가 된다. 즉, 컬렉션을 생성한 후에도 내부의 항목을 추가, 삭제, 또는 수정할 수 있다. 반면, 배열, 집합, 또는 딕셔너리를 상수에 할당하면, 그 컬렉션은 *변경 불가능* 상태가 되며, 크기와 내용을 변경할 수 없다.

> 참고: 컬렉션을 변경할 필요가 없는 경우에는 불변 컬렉션을 생성하는 것이 좋다. 이렇게 하면 코드를 더 쉽게 이해할 수 있고, Swift 컴파일러가 생성한 컬렉션의 성능을 최적화할 수 있다.


## 배열

*배열*은 동일한 타입의 값을 순서대로 저장한다. 배열에서는 같은 값이 서로 다른 위치에 여러 번 나타날 수 있다.

> 참고: Swift의 `Array` 타입은 Foundation의 `NSArray` 클래스와 연결된다.
>
> Foundation과 Cocoa에서 `Array`를 사용하는 방법에 대한 자세한 내용은 [Array와 NSArray 연결하기](https://developer.apple.com/documentation/swift/array#2846730)를 참고한다.


### 배열 타입의 축약형 문법

Swift에서 배열의 타입은 `Array<Element>` 형태로 작성한다. 여기서 `Element`는 배열이 저장할 수 있는 값의 타입을 나타낸다. 배열의 타입은 `[Element]` 형태로 축약해서 쓸 수도 있다. 두 형태는 기능적으로 동일하지만, 이 가이드에서는 배열 타입을 언급할 때 축약형을 주로 사용한다.


### 빈 배열 생성하기

Swift에서 빈 배열을 만드는 방법은 두 가지다.  
컨텍스트가 이미 타입 정보를 제공하는 경우, 예를 들어 함수 인자나 이미 타입이 지정된 변수 또는 상수라면,  
빈 배열 리터럴을 사용할 수 있다. 빈 배열 리터럴은 `[]`(빈 대괄호 쌍)으로 표기한다:

```swift
var someInts: [Int] = []
print("someInts is of type [Int] with \(someInts.count) items.")
// Prints "someInts is of type [Int] with 0 items."
```

<!--
  - test: `arraysEmpty`

  ```swifttest
  -> var someInts: [Int] = []
  -> print("someInts is of type [Int] with \(someInts.count) items.")
  <- someInts is of type [Int] with 0 items.
  ```
-->

또는 특정 타입의 빈 배열을 생성할 때 명시적 초기화 구문을 사용할 수도 있다.  
이 경우, 대괄호 안에 요소 타입을 쓰고 괄호를 붙인다.  
예를 들어, 아래 코드에서 `[Int]()`와 같이 작성한다:

```swift
var someInts = [Int]()
print("someInts is of type [Int] with \(someInts.count) items.")
// Prints "someInts is of type [Int] with 0 items."
```

두 방법 모두 동일한 결과를 만든다.  
하지만 빈 배열 리터럴이 더 짧고 일반적으로 읽기 쉽다.

두 경우 모두, 빈 배열 리터럴(`[]`)을 사용해 기존 변수에 빈 배열을 재할당할 수 있다:

```swift
someInts.append(3)
// someInts now contains 1 value of type Int
someInts = []
// someInts is now an empty array, but is still of type [Int]
```

<!--
  - test: `arraysEmpty`

  ```swifttest
  -> someInts.append(3)
  /> someInts now contains \(someInts.count) value of type Int
  </ someInts now contains 1 value of type Int
  -> someInts = []
  // someInts is now an empty array, but is still of type [Int]
  ```
-->


### 기본값으로 배열 생성하기

Swift의 `Array` 타입은 특정 크기의 배열을 생성하고 모든 값을 동일한 기본값으로 설정할 수 있는 초기화 메서드를 제공한다. 이 초기화 메서드에는 적절한 타입의 기본값(`repeating` 매개변수)과 새 배열에서 해당 값이 반복되는 횟수(`count` 매개변수)를 전달한다:

```swift
var threeDoubles = Array(repeating: 0.0, count: 3)
// threeDoubles는 [Double] 타입이며, [0.0, 0.0, 0.0]과 같다
```

<!--
  - test: `arraysEmpty`

  ```swifttest
  -> var threeDoubles = Array(repeating: 0.0, count: 3)
  /> threeDoubles is of type [Double], and equals [\(threeDoubles[0]), \(threeDoubles[1]), \(threeDoubles[2])]
  </ threeDoubles is of type [Double], and equals [0.0, 0.0, 0.0]
  ```
-->


### 두 배열을 더해 새로운 배열 생성하기

호환 가능한 타입을 가진 두 배열을 더하기 연산자(`+`)로 결합해 새로운 배열을 만들 수 있다. 새 배열의 타입은 두 배열의 타입으로부터 추론된다:

```swift
var anotherThreeDoubles = Array(repeating: 2.5, count: 3)
// anotherThreeDoubles는 [Double] 타입이며, [2.5, 2.5, 2.5]와 같다

var sixDoubles = threeDoubles + anotherThreeDoubles
// sixDoubles는 [Double] 타입으로 추론되며, [0.0, 0.0, 0.0, 2.5, 2.5, 2.5]와 같다
```

<!--
  - test: `arraysEmpty`

  ```swifttest
  -> var anotherThreeDoubles = Array(repeating: 2.5, count: 3)
  /> anotherThreeDoubles is of type [Double], and equals [\(anotherThreeDoubles[0]), \(anotherThreeDoubles[1]), \(anotherThreeDoubles[2])]
  </ anotherThreeDoubles is of type [Double], and equals [2.5, 2.5, 2.5]

  -> var sixDoubles = threeDoubles + anotherThreeDoubles
  /> sixDoubles is inferred as [Double], and equals \(sixDoubles)
  </ sixDoubles is inferred as [Double], and equals [0.0, 0.0, 0.0, 2.5, 2.5, 2.5]
  ```
-->

<!--
  TODO: func find<T: Equatable>(array: [T], value: T) -> Int?
  This is defined in Algorithm.swift,
  and gives a way to find the index of a value in an array if it exists.
  I'm holding off writing about it until NewArray lands.
-->

<!--
  TODO: mutating func sort(by: (T, T) -> Bool)
  This is defined in Array.swift.
  Likewise I'm holding off writing about it until NewArray lands.
-->


### 배열 리터럴로 배열 생성하기

배열을 생성할 때는 *배열 리터럴*을 사용할 수도 있다. 배열 리터럴은 하나 이상의 값을 배열로 간단히 표현하는 방법이다. 배열 리터럴은 쉼표로 구분된 값의 목록을 대괄호로 감싸서 작성한다:

```swift
[<#value 1#>, <#value 2#>, <#value 3#>]
```

아래 예제는 `String` 타입의 값을 저장하는 `shoppingList`라는 배열을 생성한다:

```swift
var shoppingList: [String] = ["Eggs", "Milk"]
// shoppingList는 두 개의 초기 값으로 초기화됨
```

<!--
  - test: `arrays`

  ```swifttest
  -> var shoppingList: [String] = ["Eggs", "Milk"]
  // shoppingList has been initialized with two initial items
  ```
-->

`shoppingList` 변수는 `[String]`으로 선언되어 "문자열 값의 배열"임을 나타낸다. 이 배열은 `String` 타입의 값만 저장할 수 있다. 여기서 `shoppingList` 배열은 배열 리터럴 안에 작성된 두 개의 `String` 값(`"Eggs"`와 `"Milk"`)으로 초기화된다.

> 참고: `shoppingList` 배열은 `var` 키워드로 선언되었으며, `let` 키워드로 선언된 상수가 아니다. 이는 아래 예제에서 쇼핑 목록에 더 많은 항목을 추가할 수 있도록 하기 위함이다.

이 경우, 배열 리터럴은 두 개의 `String` 값만 포함하고 있다. 이는 `shoppingList` 변수의 선언 타입(오직 `String` 값만 포함할 수 있는 배열)과 일치하므로, 배열 리터럴을 사용해 `shoppingList`를 두 개의 초기 값으로 초기화할 수 있다.

Swift의 타입 추론 덕분에, 배열 리터럴이 동일한 타입의 값으로 초기화된다면 배열의 타입을 명시적으로 작성하지 않아도 된다. `shoppingList`의 초기화는 더 짧은 형태로 작성할 수 있다:

```swift
var shoppingList = ["Eggs", "Milk"]
```

<!--
  - test: `arraysInferred`

  ```swifttest
  -> var shoppingList = ["Eggs", "Milk"]
  ```
-->

배열 리터럴의 모든 값이 동일한 타입이기 때문에, Swift는 `shoppingList` 변수에 `[String]` 타입을 사용하는 것이 적절하다고 추론할 수 있다.


### 배열 접근 및 수정

배열에 접근하고 수정하려면 메서드와 프로퍼티를 사용하거나, 서브스크립트 문법을 활용한다.

배열의 아이템 개수를 확인하려면 읽기 전용 프로퍼티인 `count`를 사용한다:

```swift
print("The shopping list contains \(shoppingList.count) items.")
// "The shopping list contains 2 items." 출력
```

<!--
  - test: `arraysInferred`

  ```swifttest
  -> print("The shopping list contains \(shoppingList.count) items.")
  <- The shopping list contains 2 items.
  ```
-->

`count` 프로퍼티가 `0`인지 확인하는 단축키로 `isEmpty` 불리언 프로퍼티를 사용한다:

```swift
if shoppingList.isEmpty {
    print("The shopping list is empty.")
} else {
    print("The shopping list isn't empty.")
}
// "The shopping list isn't empty." 출력
```

<!--
  - test: `arraysInferred`

  ```swifttest
  -> if shoppingList.isEmpty {
        print("The shopping list is empty.")
     } else {
        print("The shopping list isn't empty.")
     }
  <- The shopping list isn't empty.
  ```
-->

배열의 끝에 새로운 아이템을 추가하려면 `append(_:)` 메서드를 호출한다:

```swift
shoppingList.append("Flour")
// shoppingList는 이제 3개의 아이템을 포함하며, 누군가 팬케이크를 만들고 있다
```

<!--
  - test: `arraysInferred`

  ```swifttest
  -> shoppingList.append("Flour")
  /> shoppingList now contains \(shoppingList.count) items, and someone is making pancakes
  </ shoppingList now contains 3 items, and someone is making pancakes
  ```
-->

또는, 호환 가능한 하나 이상의 아이템을 담은 배열을 덧셈 할당 연산자(`+=`)를 사용해 추가한다:

```swift
shoppingList += ["Baking Powder"]
// shoppingList는 이제 4개의 아이템을 포함한다
shoppingList += ["Chocolate Spread", "Cheese", "Butter"]
// shoppingList는 이제 7개의 아이템을 포함한다
```

<!--
  - test: `arraysInferred`

  ```swifttest
  -> shoppingList += ["Baking Powder"]
  /> shoppingList now contains \(shoppingList.count) items
  </ shoppingList now contains 4 items
  -> shoppingList += ["Chocolate Spread", "Cheese", "Butter"]
  /> shoppingList now contains \(shoppingList.count) items
  </ shoppingList now contains 7 items
  ```
-->

배열에서 값을 가져오려면 *서브스크립트 문법*을 사용한다. 배열 이름 바로 뒤에 대괄호 안에 원하는 값의 인덱스를 전달한다:

```swift
var firstItem = shoppingList[0]
// firstItem은 "Eggs"와 같다
```

<!--
  - test: `arraysInferred`

  ```swifttest
  -> var firstItem = shoppingList[0]
  /> firstItem is equal to \"\(firstItem)\"
  </ firstItem is equal to "Eggs"
  ```
-->

> 참고: 배열의 첫 번째 아이템은 인덱스 `0`을 가진다. Swift에서 배열은 항상 0부터 시작한다.

서브스크립트 문법을 사용해 특정 인덱스의 기존 값을 변경할 수 있다:

```swift
shoppingList[0] = "Six eggs"
// 리스트의 첫 번째 아이템은 이제 "Eggs" 대신 "Six eggs"와 같다
```

<!--
  - test: `arraysInferred`

  ```swifttest
  -> shoppingList[0] = "Six eggs"
  /> the first item in the list is now equal to \"\(shoppingList[0])\" rather than \"Eggs\"
  </ the first item in the list is now equal to "Six eggs" rather than "Eggs"
  ```
-->

서브스크립트 문법을 사용할 때는 지정한 인덱스가 유효해야 한다. 예를 들어, `shoppingList[shoppingList.count] = "Salt"`를 사용해 배열의 끝에 아이템을 추가하려고 하면 런타임 오류가 발생한다.

서브스크립트 문법을 사용해 한 번에 여러 값을 변경할 수도 있다. 대체할 값의 길이가 원래 범위와 다르더라도 가능하다. 다음 예제는 `"Chocolate Spread"`, `"Cheese"`, `"Butter"`를 `"Bananas"`와 `"Apples"`로 대체한다:

```swift
shoppingList[4...6] = ["Bananas", "Apples"]
// shoppingList는 이제 6개의 아이템을 포함한다
```

<!--
  - test: `arraysInferred`

  ```swifttest
  -> shoppingList[4...6] = ["Bananas", "Apples"]
  /> shoppingList now contains \(shoppingList.count) items
  </ shoppingList now contains 6 items
  ```
-->

특정 인덱스에 아이템을 삽입하려면 `insert(_:at:)` 메서드를 호출한다:

```swift
shoppingList.insert("Maple Syrup", at: 0)
// shoppingList는 이제 7개의 아이템을 포함한다
// "Maple Syrup"가 이제 리스트의 첫 번째 아이템이다
```

<!--
  - test: `arraysInferred`

  ```swifttest
  -> shoppingList.insert("Maple Syrup", at: 0)
  /> shoppingList now contains \(shoppingList.count) items
  </ shoppingList now contains 7 items
  /> \"\(shoppingList[0])\" is now the first item in the list
  </ "Maple Syrup" is now the first item in the list
  ```
-->

`insert(_:at:)` 메서드를 호출하면 `"Maple Syrup"`라는 새 아이템이 쇼핑 리스트의 맨 앞에 삽입된다. 이때 인덱스는 `0`이다.

마찬가지로, `remove(at:)` 메서드를 사용해 배열에서 아이템을 제거할 수 있다. 이 메서드는 지정한 인덱스의 아이템을 제거하고 제거된 아이템을 반환한다 (반환된 값이 필요하지 않다면 무시해도 된다):

```swift
let mapleSyrup = shoppingList.remove(at: 0)
// 인덱스 0에 있던 아이템이 방금 제거되었다
// shoppingList는 이제 6개의 아이템을 포함하며, "Maple Syrup"는 없다
// mapleSyrup 상수는 이제 제거된 "Maple Syrup" 문자열과 같다
```

<!--
  - test: `arraysInferred`

  ```swifttest
  -> let mapleSyrup = shoppingList.remove(at: 0)
  // the item that was at index 0 has just been removed
  /> shoppingList now contains \(shoppingList.count) items, and no Maple Syrup
  </ shoppingList now contains 6 items, and no Maple Syrup
  /> the mapleSyrup constant is now equal to the removed \"\(mapleSyrup)\" string
  </ the mapleSyrup constant is now equal to the removed "Maple Syrup" string
  ```
-->

> 참고: 배열의 현재 범위를 벗어난 인덱스로 값을 접근하거나 수정하려고 하면 런타임 오류가 발생한다. 인덱스를 사용하기 전에 배열의 `count` 프로퍼티와 비교해 유효한지 확인할 수 있다. 배열의 가장 큰 유효한 인덱스는 `count - 1`이다. 배열은 0부터 인덱싱되기 때문이다. 그러나 `count`가 `0`인 경우 (즉, 배열이 비어 있는 경우) 유효한 인덱스는 없다.

아이템을 제거하면 배열의 빈 공간이 채워지므로, 인덱스 `0`의 값은 다시 `"Six eggs"`가 된다:

```swift
firstItem = shoppingList[0]
// firstItem은 이제 "Six eggs"와 같다
```

<!--
  - test: `arraysInferred`

  ```swifttest
  -> firstItem = shoppingList[0]
  /> firstItem is now equal to \"\(firstItem)\"
  </ firstItem is now equal to "Six eggs"
  ```
-->

배열의 마지막 아이템을 제거하려면 `remove(at:)` 메서드 대신 `removeLast()` 메서드를 사용한다. 이렇게 하면 배열의 `count` 프로퍼티를 쿼리할 필요가 없다. `remove(at:)` 메서드와 마찬가지로, `removeLast()`는 제거된 아이템을 반환한다:

```swift
let apples = shoppingList.removeLast()
// 배열의 마지막 아이템이 방금 제거되었다
// shoppingList는 이제 5개의 아이템을 포함하며, "Apples"는 없다
// apples 상수는 이제 제거된 "Apples" 문자열과 같다
```

<!--
  - test: `arraysInferred`

  ```swifttest
  -> let apples = shoppingList.removeLast()
  // the last item in the array has just been removed
  /> shoppingList now contains \(shoppingList.count) items, and no apples
  </ shoppingList now contains 5 items, and no apples
  /> the apples constant is now equal to the removed \"\(apples)\" string
  </ the apples constant is now equal to the removed "Apples" string
  ```
-->


### 배열 순회하기

배열에 있는 모든 값을 순회하려면 `for`-`in` 루프를 사용한다:

```swift
for item in shoppingList {
    print(item)
}
// Six eggs
// Milk
// Flour
// Baking Powder
// Bananas
```

<!--
  - test: `arraysInferred`

  ```swifttest
  -> for item in shoppingList {
        print(item)
     }
  </ Six eggs
  </ Milk
  </ Flour
  </ Baking Powder
  </ Bananas
  ```
-->

각 항목의 값과 함께 정수 인덱스도 필요하다면, `enumerated()` 메서드를 사용해 배열을 순회한다. 배열의 각 항목에 대해 `enumerated()` 메서드는 정수와 항목으로 구성된 튜플을 반환한다. 정수는 0부터 시작해 각 항목마다 1씩 증가한다. 전체 배열을 순회하면 이 정수는 항목의 인덱스와 일치한다. 순회 과정에서 튜플을 임시 상수나 변수로 분해할 수 있다:

```swift
for (index, value) in shoppingList.enumerated() {
    print("Item \(index + 1): \(value)")
}
// Item 1: Six eggs
// Item 2: Milk
// Item 3: Flour
// Item 4: Baking Powder
// Item 5: Bananas
```

<!--
  - test: `arraysInferred`

  ```swifttest
  -> for (index, value) in shoppingList.enumerated() {
        print("Item \(index + 1): \(value)")
     }
  </ Item 1: Six eggs
  </ Item 2: Milk
  </ Item 3: Flour
  </ Item 4: Baking Powder
  </ Item 5: Bananas
  ```
-->

`for`-`in` 루프에 대한 자세한 내용은 <doc:ControlFlow#For-In-Loops>를 참고한다.


## 집합(Set)

*집합(Set)*은 순서가 정의되지 않은 컬렉션에 동일한 타입의 고유한 값들을 저장한다. 항목의 순서가 중요하지 않거나, 특정 항목이 단 한 번만 나타나도록 보장해야 할 때 배열 대신 집합을 사용할 수 있다.

> 참고: Swift의 `Set` 타입은 Foundation의 `NSSet` 클래스와 브리징된다.  
> Foundation 및 Cocoa에서 `Set`을 사용하는 방법에 대한 자세한 내용은 [Bridging Between Set and NSSet](https://developer.apple.com/documentation/swift/set#2845530)을 참고한다.

<!--
  TODO: 집합과 배열에서 contains 메서드의 성능 특성에 대한 설명을 추가할지 고려 중
-->


### 집합 타입의 해시 값

어떤 타입을 집합에 저장하려면 *해시 가능* 해야 한다. 즉, 해당 타입은 자신의 *해시 값*을 계산할 수 있는 방법을 제공해야 한다. 해시 값은 동일한 객체에 대해 항상 같은 `Int` 값이다. 예를 들어 `a == b`일 때, `a`의 해시 값은 `b`의 해시 값과 같다.

Swift의 기본 타입들(예: `String`, `Int`, `Double`, `Bool`)은 기본적으로 해시 가능하며, 집합의 값 타입이나 딕셔너리의 키 타입으로 사용할 수 있다. 또한, 연관 값을 가지지 않는 열거형 케이스 값들도 기본적으로 해시 가능하다.

> 참고: 커스텀 타입을 집합의 값 타입이나 딕셔너리의 키 타입으로 사용하려면 Swift 표준 라이브러리의 `Hashable` 프로토콜을 준수하게 만들면 된다. 필요한 `hash(into:)` 메서드를 구현하는 방법에 대한 자세한 내용은 [`Hashable`](https://developer.apple.com/documentation/swift/hashable)을 참고하라. 프로토콜 준수에 대한 정보는 <doc:Protocols>에서 확인할 수 있다.


### Set 타입 구문

Swift에서 Set의 타입은 `Set<Element>`로 작성한다. 여기서 `Element`는 Set이 저장할 수 있는 값의 타입을 나타낸다. 배열과 달리 Set은 간단한 축약 형태가 없다.


### 빈 Set 생성 및 초기화

특정 타입의 빈 Set을 생성하려면 초기화 구문을 사용한다:

```swift
var letters = Set<Character>()
print("letters is of type Set<Character> with \(letters.count) items.")
// Prints "letters is of type Set<Character> with 0 items."
```

<!--
  - test: `setsEmpty`

  ```swifttest
  -> var letters = Set<Character>()
  -> print("letters is of type Set<Character> with \(letters.count) items.")
  <- letters is of type Set<Character> with 0 items.
  ```
-->

> 참고: `letters` 변수의 타입은 초기화 구문의 타입에서 `Set<Character>`로 추론된다.

또한, 함수 인자나 이미 타입이 지정된 변수 또는 상수와 같이 컨텍스트가 이미 타입 정보를 제공하는 경우, 빈 배열 리터럴을 사용해 빈 Set을 생성할 수 있다:

```swift
letters.insert("a")
// letters now contains 1 value of type Character
letters = []
// letters is now an empty set, but is still of type Set<Character>
```

<!--
  - test: `setsEmpty`

  ```swifttest
  -> letters.insert("a")
  /> letters now contains \(letters.count) value of type Character
  </ letters now contains 1 value of type Character
  -> letters = []
  // letters is now an empty set, but is still of type Set<Character>
  ```
-->


### 배열 리터럴로 Set 생성하기

배열 리터럴을 사용해 Set을 초기화할 수 있다. 이는 하나 이상의 값을 Set 컬렉션으로 간단히 표현하는 방법이다.

아래 예제는 `String` 타입의 값을 저장하는 `favoriteGenres`라는 Set을 생성한다:

```swift
var favoriteGenres: Set<String> = ["Rock", "Classical", "Hip hop"]
// favoriteGenres는 초기값으로 세 개의 항목을 가지고 있다
```

<!--
  - test: `sets`

  ```swifttest
  -> var favoriteGenres: Set<String> = ["Rock", "Classical", "Hip hop"]
  // favoriteGenres has been initialized with three initial items
  ```
-->

`favoriteGenres` 변수는 "`String` 값들의 Set"으로 선언되었으며, 이는 `Set<String>`으로 표기된다. 이 특정 Set은 `String` 타입의 값만 저장할 수 있다. 여기서 `favoriteGenres` Set은 배열 리터럴 안에 작성된 세 개의 `String` 값(`"Rock"`, `"Classical"`, `"Hip hop"`)으로 초기화되었다.

> 참고: `favoriteGenres` Set은 변수로 선언되었으며(`var` 키워드 사용), 상수가 아니다(`let` 키워드 사용). 이는 아래 예제에서 항목을 추가하고 제거하기 때문이다.

Set 타입은 배열 리터럴만으로는 추론할 수 없으므로, `Set` 타입을 명시적으로 선언해야 한다. 그러나 Swift의 타입 추론 덕분에, 배열 리터럴이 단일 타입의 값만 포함하고 있다면 Set의 요소 타입을 작성하지 않아도 된다. `favoriteGenres`의 초기화는 다음과 같이 더 짧게 작성할 수 있다:

```swift
var favoriteGenres: Set = ["Rock", "Classical", "Hip hop"]
```

<!--
  - test: `setsInferred`

  ```swifttest
  -> var favoriteGenres: Set = ["Rock", "Classical", "Hip hop"]
  ```
-->

배열 리터럴의 모든 값이 동일한 타입이기 때문에, Swift는 `favoriteGenres` 변수에 사용할 타입이 `Set<String>`임을 추론할 수 있다.


### 집합(Set) 접근 및 수정

집합을 다루려면 메서드와 프로퍼티를 사용한다.

집합에 포함된 항목의 개수를 확인하려면 `count` 프로퍼티를 사용한다:

```swift
print("I have \(favoriteGenres.count) favorite music genres.")
// Prints "I have 3 favorite music genres."
```

<!--
  - test: `setUsage`

  ```swifttest
  >> var favoriteGenres: Set = ["Rock", "Classical", "Hip hop"]
  -> print("I have \(favoriteGenres.count) favorite music genres.")
  <- I have 3 favorite music genres.
  ```
-->

`count` 프로퍼티가 `0`인지 확인하는 단축키로 `isEmpty` 프로퍼티를 사용한다:

```swift
if favoriteGenres.isEmpty {
    print("As far as music goes, I'm not picky.")
} else {
    print("I have particular music preferences.")
}
// Prints "I have particular music preferences."
```

<!--
  - test: `setUsage`

  ```swifttest
  -> if favoriteGenres.isEmpty {
        print("As far as music goes, I'm not picky.")
     } else {
        print("I have particular music preferences.")
     }
  <- I have particular music preferences.
  ```
-->

새 항목을 추가하려면 `insert(_:)` 메서드를 호출한다:

```swift
favoriteGenres.insert("Jazz")
// favoriteGenres now contains 4 items
```

<!--
  - test: `setUsage`

  ```swifttest
  -> favoriteGenres.insert("Jazz")
  /> favoriteGenres now contains \(favoriteGenres.count) items
  </ favoriteGenres now contains 4 items
  ```
-->

항목을 제거하려면 `remove(_:)` 메서드를 호출한다. 이 메서드는 집합에 해당 항목이 있으면 제거하고 제거된 값을 반환하며, 항목이 없으면 `nil`을 반환한다. 모든 항목을 한 번에 제거하려면 `removeAll()` 메서드를 사용한다.

```swift
if let removedGenre = favoriteGenres.remove("Rock") {
    print("\(removedGenre)? I'm over it.")
} else {
    print("I never much cared for that.")
}
// Prints "Rock? I'm over it."
```

<!--
  - test: `setUsage`

  ```swifttest
  -> if let removedGenre = favoriteGenres.remove("Rock") {
        print("\(removedGenre)? I'm over it.")
     } else {
        print("I never much cared for that.")
     }
  <- Rock? I'm over it.
  ```
-->

특정 항목이 집합에 포함되어 있는지 확인하려면 `contains(_:)` 메서드를 사용한다.

```swift
if favoriteGenres.contains("Funk") {
    print("I get up on the good foot.")
} else {
    print("It's too funky in here.")
}
// Prints "It's too funky in here."
```

<!--
  - test: `setUsage`

  ```swifttest
  -> if favoriteGenres.contains("Funk") {
         print("I get up on the good foot.")
     } else {
         print("It's too funky in here.")
     }
  <- It's too funky in here.
  ```
-->


### Set 순회하기

`for-in` 루프를 사용해 Set의 값을 순회할 수 있다.

```swift
for genre in favoriteGenres {
    print("\(genre)")
}
// Classical
// Jazz
// Hip hop
```

<!--
  - test: `setUsage`

  ```swifttest
  -> for genre in favoriteGenres {
        print("\(genre)")
     }
  </ Classical
  </ Jazz
  </ Hip hop
  ```
-->

`for-in` 루프에 대한 자세한 내용은 <doc:ControlFlow#For-In-Loops>를 참고한다.

Swift의 `Set` 타입은 정의된 순서가 없다. 특정 순서로 Set의 값을 순회하려면 `sorted()` 메서드를 사용한다. 이 메서드는 `<` 연산자를 사용해 정렬된 배열로 Set의 요소를 반환한다.

```swift
for genre in favoriteGenres.sorted() {
    print("\(genre)")
}
// Classical
// Hip hop
// Jazz
```

<!--
  - test: `setUsage`

  ```swifttest
  -> for genre in favoriteGenres.sorted() {
        print("\(genre)")
     }
  </ Classical
  </ Hip hop
  </ Jazz
  ```
-->


## 집합 연산 수행하기

두 집합을 효율적으로 결합하거나, 두 집합이 공통으로 가지는 값을 찾거나, 두 집합이 같은 값을 모두 포함하는지, 일부만 포함하는지, 아니면 전혀 포함하지 않는지 확인하는 등 기본적인 집합 연산을 수행할 수 있다.


### 기본 집합 연산

아래 그림은 두 집합 `a`와 `b`를 보여주며, 다양한 집합 연산의 결과를 음영 처리된 영역으로 표현한다.

![](setVennDiagram)

- `intersection(_:)` 메서드를 사용해 두 집합에 공통된 값만 포함된 새로운 집합을 생성한다.
- `symmetricDifference(_:)` 메서드를 사용해 두 집합 중 하나에만 포함된 값을 가진 새로운 집합을 생성한다.
- `union(_:)` 메서드를 사용해 두 집합의 모든 값을 포함한 새로운 집합을 생성한다.
- `subtracting(_:)` 메서드를 사용해 지정된 집합에 없는 값을 가진 새로운 집합을 생성한다.

```swift
let oddDigits: Set = [1, 3, 5, 7, 9]
let evenDigits: Set = [0, 2, 4, 6, 8]
let singleDigitPrimeNumbers: Set = [2, 3, 5, 7]

oddDigits.union(evenDigits).sorted()
// [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
oddDigits.intersection(evenDigits).sorted()
// []
oddDigits.subtracting(singleDigitPrimeNumbers).sorted()
// [1, 9]
oddDigits.symmetricDifference(singleDigitPrimeNumbers).sorted()
// [1, 2, 9]
```

<!--
  - test: `setOperations`

  ```swifttest
  -> let oddDigits: Set = [1, 3, 5, 7, 9]
  -> let evenDigits: Set = [0, 2, 4, 6, 8]
  -> let singleDigitPrimeNumbers: Set = [2, 3, 5, 7]

  >> let a =
  -> oddDigits.union(evenDigits).sorted()
  >> assert(a == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
  // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  >> let b =
  -> oddDigits.intersection(evenDigits).sorted()
  >> assert(b == [])
  // []
  >> let c =
  -> oddDigits.subtracting(singleDigitPrimeNumbers).sorted()
  >> assert(c == [1, 9])
  // [1, 9]
  >> let d =
  -> oddDigits.symmetricDifference(singleDigitPrimeNumbers).sorted()
  >> assert(d == [1, 2, 9])
  // [1, 2, 9]
  ```
-->

<!--
  Rewrite the above to avoid bare expressions.
  Tracking bug is <rdar://problem/35301593>
-->


### 집합의 포함 관계와 동등성

아래 그림은 세 개의 집합 `a`, `b`, `c`를 보여준다. 겹치는 영역은 집합 간 공유되는 요소를 나타낸다. 집합 `a`는 집합 `b`의 *상위 집합(superset)*이다. 왜냐하면 `a`는 `b`의 모든 요소를 포함하기 때문이다. 반대로, 집합 `b`는 집합 `a`의 *하위 집합(subset)*이다. `b`의 모든 요소가 `a`에 포함되기 때문이다. 집합 `b`와 `c`는 서로 *서로소(disjoint)* 관계이다. 두 집합 간 공통 요소가 없기 때문이다.

![](setEulerDiagram)

- 두 집합이 동일한 값을 모두 포함하는지 확인하려면 "is equal" 연산자(`==`)를 사용한다.
- 한 집합의 모든 값이 특정 집합에 포함되는지 확인하려면 `isSubset(of:)` 메서드를 사용한다.
- 한 집합이 특정 집합의 모든 값을 포함하는지 확인하려면 `isSuperset(of:)` 메서드를 사용한다.
- 한 집합이 특정 집합의 하위 집합 또는 상위 집합이지만 동일하지는 않은지 확인하려면 `isStrictSubset(of:)` 또는 `isStrictSuperset(of:)` 메서드를 사용한다.
- 두 집합이 공통된 값을 전혀 가지고 있지 않은지 확인하려면 `isDisjoint(with:)` 메서드를 사용한다.

```swift
let houseAnimals: Set = ["🐶", "🐱"]
let farmAnimals: Set = ["🐮", "🐔", "🐑", "🐶", "🐱"]
let cityAnimals: Set = ["🐦", "🐭"]

houseAnimals.isSubset(of: farmAnimals)
// true
farmAnimals.isSuperset(of: houseAnimals)
// true
farmAnimals.isDisjoint(with: cityAnimals)
// true
```

<!--
  - test: `setOperations`

  ```swifttest
  -> let houseAnimals: Set = ["🐶", "🐱"]
  -> let farmAnimals: Set = ["🐮", "🐔", "🐑", "🐶", "🐱"]
  -> let cityAnimals: Set = ["🐦", "🐭"]

  >> let aa =
  -> houseAnimals.isSubset(of: farmAnimals)
  >> assert(aa == true)
  // true
  >> let bb =
  -> farmAnimals.isSuperset(of: houseAnimals)
  >> assert(bb == true)
  // true
  >> let cc =
  -> farmAnimals.isDisjoint(with: cityAnimals)
  >> assert(cc == true)
  // true
  ```
-->

<!--
  Rewrite the above to avoid bare expressions.
  Tracking bug is <rdar://problem/35301593>
-->


## 딕셔너리

*딕셔너리*는 동일한 타입의 키와 동일한 타입의 값 사이의 연관 관계를 저장하는 컬렉션이다. 딕셔너리에서는 순서가 정의되지 않는다. 각 값은 고유한 *키*와 연결되며, 이 키는 딕셔너리 내에서 해당 값을 식별하는 역할을 한다. 배열의 항목과 달리 딕셔너리의 항목은 특정 순서를 가지지 않는다. 딕셔너리는 식별자를 기반으로 값을 조회해야 할 때 사용한다. 실제 사전에서 특정 단어의 정의를 찾는 방식과 유사하다.

> 참고: Swift의 `Dictionary` 타입은 Foundation의 `NSDictionary` 클래스와 연결된다.
>
> Foundation과 Cocoa에서 `Dictionary`를 사용하는 방법에 대한 자세한 내용은 [Bridging Between Dictionary and NSDictionary](https://developer.apple.com/documentation/swift/dictionary#2846239)를 참고한다.


### 딕셔너리 타입의 축약형 문법

스위프트에서 딕셔너리의 타입은 `Dictionary<Key, Value>`로 작성한다. 여기서 `Key`는 딕셔너리의 키로 사용할 수 있는 값의 타입을 나타내고, `Value`는 해당 키에 저장될 값의 타입을 나타낸다.

> 참고: 딕셔너리의 `Key` 타입은 `Hashable` 프로토콜을 준수해야 한다. 이는 세트의 값 타입과 동일한 요구사항이다.

딕셔너리의 타입을 `[Key: Value]`와 같은 축약형으로 작성할 수도 있다. 두 형식은 기능적으로 동일하지만, 가이드 전반에 걸쳐 딕셔너리 타입을 언급할 때는 축약형을 주로 사용한다.


### 빈 딕셔너리 생성하기

배열과 마찬가지로, 특정 타입의 빈 `딕셔너리`를 초기화 구문을 사용해 생성할 수 있다:

```swift
var namesOfIntegers: [Int: String] = [:]
// namesOfIntegers는 빈 [Int: String] 딕셔너리다
```

<!--
  - test: `dictionariesEmpty`

  ```swifttest
  -> var namesOfIntegers: [Int: String] = [:]
  // namesOfIntegers is an empty [Int: String] dictionary
  ```
-->

이 예제는 정수 값의 사람이 읽을 수 있는 이름을 저장하기 위해 `[Int: String]` 타입의 빈 딕셔너리를 생성한다. 키는 `Int` 타입이고, 값은 `String` 타입이다.

만약 컨텍스트가 이미 타입 정보를 제공한다면, 빈 딕셔너리 리터럴(`[:]`, 즉 대괄호 안에 콜론)을 사용해 빈 딕셔너리를 생성할 수 있다:

```swift
namesOfIntegers[16] = "sixteen"
// namesOfIntegers는 이제 1개의 키-값 쌍을 포함한다
namesOfIntegers = [:]
// namesOfIntegers는 다시 [Int: String] 타입의 빈 딕셔너리가 된다
```

<!--
  - test: `dictionariesEmpty`

  ```swifttest
  -> namesOfIntegers[16] = "sixteen"
  /> namesOfIntegers now contains \(namesOfIntegers.count) key-value pair
  </ namesOfIntegers now contains 1 key-value pair
  -> namesOfIntegers = [:]
  // namesOfIntegers is once again an empty dictionary of type [Int: String]
  ```
-->


### 딕셔너리 리터럴로 딕셔너리 생성하기

이전에 살펴본 배열 리터럴과 유사한 문법을 사용해 딕셔너리를 초기화할 수도 있다. 딕셔너리 리터럴은 하나 이상의 키-값 쌍을 `Dictionary` 컬렉션으로 간단히 표현하는 방법이다.

키-값 쌍은 키와 값의 조합이다. 딕셔너리 리터럴에서 각 키-값 쌍은 콜론으로 구분되며, 여러 쌍은 쉼표로 구분된 목록 형태로 작성된다. 전체는 대괄호로 둘러싸인다:

```swift
[<#key 1#>: <#value 1#>, <#key 2#>: <#value 2#>, <#key 3#>: <#value 3#>]
```

아래 예제는 국제 공항의 이름을 저장하기 위한 딕셔너리를 생성한다. 이 딕셔너리에서 키는 국제 항공 운송 협회(IATA) 코드이며, 값은 공항 이름이다:

```swift
var airports: [String: String] = ["YYZ": "Toronto Pearson", "DUB": "Dublin"]
```

<!--
  - test: `dictionaries`

  ```swifttest
  -> var airports: [String: String] = ["YYZ": "Toronto Pearson", "DUB": "Dublin"]
  ```
-->

`airports` 딕셔너리는 `[String: String]` 타입으로 선언되었다. 이는 "키가 `String` 타입이고, 값도 `String` 타입인 `Dictionary`"를 의미한다.

> 참고: `airports` 딕셔너리는 `var` 키워드로 변수로 선언되었으며, `let` 키워드로 상수로 선언되지 않았다. 이는 아래 예제에서 더 많은 공항을 딕셔너리에 추가하기 위함이다.

`airports` 딕셔너리는 두 개의 키-값 쌍을 포함하는 딕셔너리 리터럴로 초기화되었다. 첫 번째 쌍은 키가 `"YYZ"`이고 값이 `"Toronto Pearson"`이다. 두 번째 쌍은 키가 `"DUB"`이고 값이 `"Dublin"`이다.

이 딕셔너리 리터럴은 두 개의 `String: String` 쌍을 포함한다. 이 키-값 타입은 `airports` 변수 선언의 타입(키와 값이 모두 `String`인 딕셔너리)과 일치하므로, 딕셔너리 리터럴을 `airports` 딕셔너리를 초기화하는 데 사용할 수 있다.

배열과 마찬가지로, 딕셔너리를 키와 값의 타입이 일관된 딕셔너리 리터럴로 초기화할 때는 타입을 명시적으로 작성하지 않아도 된다. `airports` 초기화를 더 짧은 형태로 작성할 수 있다:

```swift
var airports = ["YYZ": "Toronto Pearson", "DUB": "Dublin"]
```

<!--
  - test: `dictionariesInferred`

  ```swifttest
  -> var airports = ["YYZ": "Toronto Pearson", "DUB": "Dublin"]
  ```
-->

리터럴의 모든 키가 동일한 타입이고, 모든 값도 동일한 타입이므로, Swift는 `[String: String]`이 `airports` 딕셔너리에 적합한 타입임을 추론할 수 있다.


### 딕셔너리 접근 및 수정

딕셔너리에 접근하고 수정할 때는 메서드와 프로퍼티를 사용하거나, 서브스크립트 문법을 활용한다.

배열과 마찬가지로, `Dictionary`의 항목 수를 확인하려면 읽기 전용 프로퍼티인 `count`를 사용한다:

```swift
print("The airports dictionary contains \(airports.count) items.")
// Prints "The airports dictionary contains 2 items."
```

<!--
  - test: `dictionariesInferred`

  ```swifttest
  -> print("The airports dictionary contains \(airports.count) items.")
  <- The airports dictionary contains 2 items.
  ```
-->

`count` 프로퍼티가 `0`인지 확인하는 단축키로, 불리언 프로퍼티인 `isEmpty`를 사용한다:

```swift
if airports.isEmpty {
    print("The airports dictionary is empty.")
} else {
    print("The airports dictionary isn't empty.")
}
// Prints "The airports dictionary isn't empty."
```

<!--
  - test: `dictionariesInferred`

  ```swifttest
  -> if airports.isEmpty {
        print("The airports dictionary is empty.")
     } else {
        print("The airports dictionary isn't empty.")
     }
  <- The airports dictionary isn't empty.
  ```
-->

서브스크립트 문법을 사용해 딕셔너리에 새로운 항목을 추가할 수 있다. 적절한 타입의 새로운 키를 서브스크립트 인덱스로 사용하고, 적절한 타입의 새로운 값을 할당한다:

```swift
airports["LHR"] = "London"
// the airports dictionary now contains 3 items
```

<!--
  - test: `dictionariesInferred`

  ```swifttest
  -> airports["LHR"] = "London"
  /> the airports dictionary now contains \(airports.count) items
  </ the airports dictionary now contains 3 items
  ```
-->

특정 키와 연결된 값을 변경할 때도 서브스크립트 문법을 사용할 수 있다:

```swift
airports["LHR"] = "London Heathrow"
// the value for "LHR" has been changed to "London Heathrow"
```

<!--
  - test: `dictionariesInferred`

  ```swifttest
  -> airports["LHR"] = "London Heathrow"
  /> the value for \"LHR\" has been changed to \"\(airports["LHR"]!)\"
  </ the value for "LHR" has been changed to "London Heathrow"
  ```
-->

서브스크립트 대신 딕셔너리의 `updateValue(_:forKey:)` 메서드를 사용해 특정 키에 대한 값을 설정하거나 업데이트할 수 있다. 위의 서브스크립트 예제와 마찬가지로, `updateValue(_:forKey:)` 메서드는 키가 존재하지 않으면 값을 설정하고, 키가 이미 존재하면 값을 업데이트한다. 하지만 서브스크립트와 달리, `updateValue(_:forKey:)` 메서드는 업데이트 후 *이전* 값을 반환한다. 이를 통해 업데이트가 발생했는지 확인할 수 있다.

`updateValue(_:forKey:)` 메서드는 딕셔너리의 값 타입에 대한 옵셔널 값을 반환한다. 예를 들어, `String` 값을 저장하는 딕셔너리의 경우, 이 메서드는 `String?` 타입, 즉 "옵셔널 `String`" 값을 반환한다. 이 옵셔널 값은 업데이트 전 해당 키에 대한 이전 값을 포함하거나, 값이 존재하지 않았다면 `nil`을 포함한다:

```swift
if let oldValue = airports.updateValue("Dublin Airport", forKey: "DUB") {
    print("The old value for DUB was \(oldValue).")
}
// Prints "The old value for DUB was Dublin."
```

<!--
  - test: `dictionariesInferred`

  ```swifttest
  -> if let oldValue = airports.updateValue("Dublin Airport", forKey: "DUB") {
        print("The old value for DUB was \(oldValue).")
     }
  <- The old value for DUB was Dublin.
  ```
-->

특정 키에 대한 값을 딕셔너리에서 가져올 때도 서브스크립트 문법을 사용할 수 있다. 값이 존재하지 않는 키를 요청할 가능성이 있기 때문에, 딕셔너리의 서브스크립트는 딕셔너리의 값 타입에 대한 옵셔널 값을 반환한다. 요청한 키에 대한 값이 딕셔너리에 존재한다면, 서브스크립트는 해당 키의 기존 값을 포함한 옵셔널 값을 반환한다. 그렇지 않으면 `nil`을 반환한다:

```swift
if let airportName = airports["DUB"] {
    print("The name of the airport is \(airportName).")
} else {
    print("That airport isn't in the airports dictionary.")
}
// Prints "The name of the airport is Dublin Airport."
```

<!--
  - test: `dictionariesInferred`

  ```swifttest
  -> if let airportName = airports["DUB"] {
        print("The name of the airport is \(airportName).")
     } else {
        print("That airport isn't in the airports dictionary.")
     }
  <- The name of the airport is Dublin Airport.
  ```
-->

서브스크립트 문법을 사용해 딕셔너리에서 키-값 쌍을 제거할 수 있다. 해당 키에 `nil` 값을 할당하면 된다:

```swift
airports["APL"] = "Apple International"
// "Apple International" isn't the real airport for APL, so delete it
airports["APL"] = nil
// APL has now been removed from the dictionary
```

<!--
  - test: `dictionariesInferred`

  ```swifttest
  -> airports["APL"] = "Apple International"
  // "Apple International" isn't the real airport for APL, so delete it
  -> airports["APL"] = nil
  // APL has now been removed from the dictionary
  >> if let deletedName = airports["APL"] {
  >>    print("The key-value pair for APL has *not* been deleted, but it should have been!")
  >>    print("It still has a value of \(deletedName)")
  >> } else {
  >>    print("APL has now been removed from the dictionary")
  >> }
  << APL has now been removed from the dictionary
  ```
-->

또는 `removeValue(forKey:)` 메서드를 사용해 딕셔너리에서 키-값 쌍을 제거할 수 있다. 이 메서드는 키-값 쌍이 존재하면 제거하고 제거된 값을 반환하며, 값이 존재하지 않으면 `nil`을 반환한다:

```swift
if let removedValue = airports.removeValue(forKey: "DUB") {
    print("The removed airport's name is \(removedValue).")
} else {
    print("The airports dictionary doesn't contain a value for DUB.")
}
// Prints "The removed airport's name is Dublin Airport."
```

<!--
  - test: `dictionariesInferred`

  ```swifttest
  -> if let removedValue = airports.removeValue(forKey: "DUB") {
        print("The removed airport's name is \(removedValue).")
     } else {
        print("The airports dictionary doesn't contain a value for DUB.")
     }
  <- The removed airport's name is Dublin Airport.
  ```
-->


### 딕셔너리 순회하기

`for`-`in` 루프를 사용해 딕셔너리의 키-값 쌍을 순회할 수 있다. 딕셔너리의 각 항목은 `(key, value)` 튜플로 반환되며, 순회 과정에서 튜플의 멤버를 임시 상수나 변수로 분해할 수 있다:

```swift
for (airportCode, airportName) in airports {
    print("\(airportCode): \(airportName)")
}
// LHR: London Heathrow
// YYZ: Toronto Pearson
```

<!--
  - test: `dictionariesInferred`

  ```swifttest
  -> for (airportCode, airportName) in airports {
        print("\(airportCode): \(airportName)")
     }
  </ LHR: London Heathrow
  </ YYZ: Toronto Pearson
  ```
-->

`for`-`in` 루프에 대해 더 자세히 알아보려면 <doc:ControlFlow#For-In-Loops>를 참고한다.

딕셔너리의 `keys`와 `values` 프로퍼티에 접근해 키나 값의 컬렉션을 가져와 순회할 수도 있다:

```swift
for airportCode in airports.keys {
    print("Airport code: \(airportCode)")
}
// Airport code: LHR
// Airport code: YYZ

for airportName in airports.values {
    print("Airport name: \(airportName)")
}
// Airport name: London Heathrow
// Airport name: Toronto Pearson
```

<!--
  - test: `dictionariesInferred`

  ```swifttest
  -> for airportCode in airports.keys {
        print("Airport code: \(airportCode)")
     }
  </ Airport code: LHR
  </ Airport code: YYZ

  -> for airportName in airports.values {
        print("Airport name: \(airportName)")
     }
  </ Airport name: London Heathrow
  </ Airport name: Toronto Pearson
  ```
-->

`Array` 타입을 인자로 받는 API와 함께 딕셔너리의 키나 값을 사용해야 한다면, `keys`나 `values` 프로퍼티로 새로운 배열을 초기화한다:

```swift
let airportCodes = [String](airports.keys)
// airportCodes is ["LHR", "YYZ"]

let airportNames = [String](airports.values)
// airportNames is ["London Heathrow", "Toronto Pearson"]
```

<!--
  - test: `dictionariesInferred`

  ```swifttest
  -> let airportCodes = [String](airports.keys)
  /> airportCodes is [\"\(airportCodes[0])\", \"\(airportCodes[1])\"]
  </ airportCodes is ["LHR", "YYZ"]

  -> let airportNames = [String](airports.values)
  /> airportNames is [\"\(airportNames[0])\", \"\(airportNames[1])\"]
  </ airportNames is ["London Heathrow", "Toronto Pearson"]
  ```
-->

Swift의 `Dictionary` 타입은 정의된 순서가 없다. 특정 순서로 딕셔너리의 키나 값을 순회하려면, `keys`나 `values` 프로퍼티에 `sorted()` 메서드를 사용한다.

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


