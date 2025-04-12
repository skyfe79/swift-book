# 서브스크립트

컬렉션의 요소에 접근할 때 사용한다.

클래스, 구조체, 열거형은 *서브스크립트*를 정의할 수 있다. 서브스크립트는 컬렉션, 리스트, 시퀀스의 멤버 요소에 접근하기 위한 단축 경로 역할을 한다. 별도의 메서드를 사용하지 않고도 인덱스를 통해 값을 설정하거나 가져올 수 있다. 예를 들어, `Array` 인스턴스의 요소는 `someArray[index]`로, `Dictionary` 인스턴스의 요소는 `someDictionary[key]`로 접근한다.

하나의 타입에 여러 서브스크립트를 정의할 수 있다. 서브스크립트에 전달하는 인덱스 값의 타입에 따라 적절한 서브스크립트 오버로드가 선택된다. 서브스크립트는 단일 차원에 국한되지 않으며, 커스텀 타입의 필요에 따라 여러 입력 매개변수를 가진 서브스크립트를 정의할 수도 있다.

<!--
  TODO: 이 장에서는 열거형을 서브스크립트로 사용하는 예제를 제공해야 한다.
  Joe Groff의 예제를 참고하라. (rdar://16555559)
-->


## 서브스크립트 구문

서브스크립트를 사용하면 타입의 인스턴스를 대괄호 안에 하나 이상의 값을 넣어 쿼리할 수 있다. 이 구문은 인스턴스 메서드와 계산 프로퍼티 구문과 유사하다. 서브스크립트를 정의할 때는 `subscript` 키워드를 사용하며, 인스턴스 메서드와 동일한 방식으로 하나 이상의 입력 매개변수와 반환 타입을 지정한다. 단, 인스턴스 메서드와 달리 서브스크립트는 읽기-쓰기 또는 읽기 전용으로 설정할 수 있다. 이 동작은 계산 프로퍼티와 마찬가지로 getter와 setter를 통해 표현된다:

```swift
subscript(index: Int) -> Int {
    get {
        // 여기에 적절한 서브스크립트 값을 반환한다.
    }
    set(newValue) {
        // 여기에 적절한 설정 작업을 수행한다.
    }
}
```

<!--
  - test: `subscriptSyntax`

  ```swifttest
  >> class Test1 {
  -> subscript(index: Int) -> Int {
        get {
           // 여기에 적절한 서브스크립트 값을 반환한다.
  >>       return 1
        }
        set(newValue) {
           // 여기에 적절한 설정 작업을 수행한다.
        }
     }
  >> }
  ```
-->

`newValue`의 타입은 서브스크립트의 반환 값과 동일하다. 계산 프로퍼티와 마찬가지로 setter의 `(newValue)` 매개변수를 생략할 수 있다. 만약 직접 매개변수를 제공하지 않으면 `newValue`라는 기본 매개변수가 setter에 자동으로 제공된다.

읽기 전용 계산 프로퍼티와 마찬가지로, 읽기 전용 서브스크립트의 선언을 단순화할 수 있다. `get` 키워드와 중괄호를 제거하면 된다:

```swift
subscript(index: Int) -> Int {
    // 여기에 적절한 서브스크립트 값을 반환한다.
}
```

<!--
  - test: `subscriptSyntax`

  ```swifttest
  >> class Test2 {
  -> subscript(index: Int) -> Int {
        // 여기에 적절한 서브스크립트 값을 반환한다.
  >>    return 1
     }
  >> }
  ```
-->

다음은 읽기 전용 서브스크립트 구현 예제이다. 이 예제는 정수의 *n*배수 테이블을 나타내는 `TimesTable` 구조체를 정의한다:

```swift
struct TimesTable {
    let multiplier: Int
    subscript(index: Int) -> Int {
        return multiplier * index
    }
}
let threeTimesTable = TimesTable(multiplier: 3)
print("six times three is \(threeTimesTable[6])")
// "six times three is 18" 출력
```

<!--
  - test: `timesTable`

  ```swifttest
  -> struct TimesTable {
        let multiplier: Int
        subscript(index: Int) -> Int {
           return multiplier * index
        }
     }
  -> let threeTimesTable = TimesTable(multiplier: 3)
  -> print("six times three is \(threeTimesTable[6])")
  <- six times three is 18
  ```
-->

이 예제에서 `TimesTable`의 새 인스턴스를 생성해 3의 배수 테이블을 나타낸다. 인스턴스의 `multiplier` 매개변수로 사용할 값으로 `3`을 구조체의 초기화 메서드에 전달한다.

`threeTimesTable` 인스턴스의 서브스크립트를 호출해 쿼리할 수 있다. 예를 들어 `threeTimesTable[6]`을 호출하면 3의 배수 테이블에서 6번째 항목을 요청한다. 이 경우 `18`을 반환하며, 이는 `3` 곱하기 `6`의 결과이다.

> 참고: *n*배수 테이블은 고정된 수학적 규칙을 기반으로 한다. 따라서 `threeTimesTable[someIndex]`를 새 값으로 설정하는 것은 적절하지 않다. 그래서 `TimesTable`의 서브스크립트는 읽기 전용으로 정의된다.


## 서브스크립트 사용법

"서브스크립트"의 정확한 의미는 사용되는 문맥에 따라 달라진다. 일반적으로 서브스크립트는 컬렉션, 리스트, 시퀀스의 멤버 엘리먼트에 접근하기 위한 단축키로 사용된다. 여러분은 특정 클래스나 구조체의 기능에 가장 적합한 방식으로 서브스크립트를 자유롭게 구현할 수 있다.

예를 들어, Swift의 `Dictionary` 타입은 `Dictionary` 인스턴스에 저장된 값을 설정하고 검색하기 위해 서브스크립트를 구현한다. 딕셔너리의 키 타입에 해당하는 키를 서브스크립트 대괄호 안에 제공하고, 딕셔너리의 값 타입에 해당하는 값을 서브스크립트에 할당함으로써 딕셔너리에 값을 설정할 수 있다:

```swift
var numberOfLegs = ["spider": 8, "ant": 6, "cat": 4]
numberOfLegs["bird"] = 2
```

<!--
  - test: `dictionarySubscript`

  ```swifttest
  -> var numberOfLegs = ["spider": 8, "ant": 6, "cat": 4]
  -> numberOfLegs["bird"] = 2
  ```
-->

위 예제는 `numberOfLegs`라는 변수를 정의하고, 세 개의 키-값 쌍을 포함하는 딕셔너리 리터럴로 초기화한다. `numberOfLegs` 딕셔너리의 타입은 `[String: Int]`로 추론된다. 딕셔너리를 생성한 후, 이 예제는 서브스크립트 할당을 사용해 `"bird"`라는 `String` 키와 `2`라는 `Int` 값을 딕셔너리에 추가한다.

`Dictionary` 서브스크립트에 대한 더 자세한 정보는 <doc:CollectionTypes#Accessing-and-Modifying-a-Dictionary>를 참고한다.

> 참고: Swift의 `Dictionary` 타입은 키-값 서브스크립트를 *옵셔널* 타입을 받고 반환하는 서브스크립트로 구현한다. 위의 `numberOfLegs` 딕셔너리의 경우, 키-값 서브스크립트는 `Int?` 타입, 즉 "옵셔널 정수"를 받고 반환한다. `Dictionary` 타입은 모든 키가 값을 가지지 않을 수 있다는 사실을 모델링하고, 키에 대한 값을 삭제하기 위해 해당 키에 `nil` 값을 할당할 수 있는 방법을 제공하기 위해 옵셔널 서브스크립트 타입을 사용한다.


## 서브스크립트 옵션

서브스크립트는 여러 개의 입력 인자를 받을 수 있으며, 이 인자는 어떤 타입이든 가능하다. 또한 서브스크립트는 어떤 타입의 값이든 반환할 수 있다.

함수와 마찬가지로, 서브스크립트도 가변 인자를 받거나 기본값을 설정할 수 있다. 이에 대한 자세한 내용은 <doc:Functions#Variadic-Parameters>와 <doc:Functions#Default-Parameter-Values>에서 다룬다. 하지만 함수와 달리, 서브스크립트는 in-out 인자를 사용할 수 없다.

<!--
  - test: `subscripts-can-have-default-arguments`

  ```swifttest
  >> struct Subscriptable {
  >>     subscript(x: Int, y: Int = 0) -> Int {
  >>         return 100
  >>     }
  >> }
  >> let s = Subscriptable()
  >> print(s[0])
  << 100
  ```
-->

클래스나 구조체는 필요한 만큼 서브스크립트를 정의할 수 있다. 이때, 서브스크립트 대괄호 안에 포함된 값의 타입을 기반으로 적절한 서브스크립트를 추론한다. 이러한 여러 서브스크립트를 정의하는 방식을 *서브스크립트 오버로딩*이라고 한다.

서브스크립트가 단일 인자를 받는 것이 일반적이지만, 타입에 적합하다면 여러 인자를 받는 서브스크립트를 정의할 수도 있다. 다음 예제는 `Double` 값으로 이루어진 2차원 행렬을 나타내는 `Matrix` 구조체를 정의한다. 이 `Matrix` 구조체의 서브스크립트는 두 개의 정수 인자를 받는다:

```swift
struct Matrix {
    let rows: Int, columns: Int
    var grid: [Double]
    init(rows: Int, columns: Int) {
        self.rows = rows
        self.columns = columns
        grid = Array(repeating: 0.0, count: rows * columns)
    }
    func indexIsValid(row: Int, column: Int) -> Bool {
        return row >= 0 && row < rows && column >= 0 && column < columns
    }
    subscript(row: Int, column: Int) -> Double {
        get {
            assert(indexIsValid(row: row, column: column), "Index out of range")
            return grid[(row * columns) + column]
        }
        set {
            assert(indexIsValid(row: row, column: column), "Index out of range")
            grid[(row * columns) + column] = newValue
        }
    }
}
```

<!--
  - test: `matrixSubscript, matrixSubscriptAssert`

  ```swifttest
  -> struct Matrix {
        let rows: Int, columns: Int
        var grid: [Double]
        init(rows: Int, columns: Int) {
           self.rows = rows
           self.columns = columns
           grid = Array(repeating: 0.0, count: rows * columns)
        }
        func indexIsValid(row: Int, column: Int) -> Bool {
           return row >= 0 && row < rows && column >= 0 && column < columns
        }
        subscript(row: Int, column: Int) -> Double {
           get {
              assert(indexIsValid(row: row, column: column), "Index out of range")
              return grid[(row * columns) + column]
           }
           set {
              assert(indexIsValid(row: row, column: column), "Index out of range")
              grid[(row * columns) + column] = newValue
           }
        }
     }
  ```
-->

`Matrix`는 `rows`와 `columns` 두 개의 인자를 받는 초기화 메서드를 제공한다. 이 초기화 메서드는 `rows * columns` 크기의 `Double` 타입 배열을 생성한다. 행렬의 각 위치는 `0.0`으로 초기화된다. 이를 위해 배열의 크기와 초기값 `0.0`을 배열 초기화 메서드에 전달한다. 이 초기화 메서드에 대한 자세한 내용은 <doc:CollectionTypes#Creating-an-Array-with-a-Default-Value>에서 확인할 수 있다.

초기화 메서드에 적절한 행과 열의 수를 전달해 새로운 `Matrix` 인스턴스를 생성할 수 있다:

```swift
var matrix = Matrix(rows: 2, columns: 2)
```

<!--
  - test: `matrixSubscript, matrixSubscriptAssert`

  ```swifttest
  -> var matrix = Matrix(rows: 2, columns: 2)
  >> assert(matrix.grid == [0.0, 0.0, 0.0, 0.0])
  ```
-->

위 예제는 두 행과 두 열로 이루어진 새로운 `Matrix` 인스턴스를 생성한다. 이 `Matrix` 인스턴스의 `grid` 배열은 행렬을 왼쪽 위에서 오른쪽 아래로 읽은 평면화된 형태다:

![](subscriptMatrix01)

행렬의 값은 행과 열 값을 쉼표로 구분해 서브스크립트에 전달함으로써 설정할 수 있다:

```swift
matrix[0, 1] = 1.5
matrix[1, 0] = 3.2
```

<!--
  - test: `matrixSubscript, matrixSubscriptAssert`

  ```swifttest
  -> matrix[0, 1] = 1.5
  >> print(matrix[0, 1])
  << 1.5
  -> matrix[1, 0] = 3.2
  >> print(matrix[1, 0])
  << 3.2
  ```
-->

이 두 문장은 서브스크립트의 설정자를 호출해 행렬의 오른쪽 위 위치(`row`가 `0`, `column`이 `1`)에 `1.5`를, 왼쪽 아래 위치(`row`가 `1`, `column`이 `0`)에 `3.2`를 설정한다:

![](subscriptMatrix02)

`Matrix` 서브스크립트의 getter와 setter는 모두 `row`와 `column` 값이 유효한지 확인하기 위해 assertion을 포함한다. 이를 돕기 위해 `Matrix`는 `indexIsValid(row:column:)`이라는 편의 메서드를 제공한다. 이 메서드는 요청된 `row`와 `column`이 행렬의 범위 내에 있는지 확인한다:

```swift
func indexIsValid(row: Int, column: Int) -> Bool {
    return row >= 0 && row < rows && column >= 0 && column < columns
}
```

<!--
  - test: `matrixSubscript`

  ```swifttest
  >> var rows = 2
  >> var columns = 2
  -> func indexIsValid(row: Int, column: Int) -> Bool {
        return row >= 0 && row < rows && column >= 0 && column < columns
     }
  ```
-->

행렬 범위를 벗어나는 서브스크립트에 접근하려고 하면 assertion이 발생한다:

```swift
let someValue = matrix[2, 2]
// [2, 2]는 행렬 범위를 벗어나므로 assertion이 발생한다.
```

<!--
  - test: `matrixSubscriptAssert`

  ```swifttest
  -> let someValue = matrix[2, 2]
  xx assert
  // [2, 2]는 행렬 범위를 벗어나므로 assertion이 발생한다.
  ```
-->


## 타입 서브스크립트

앞서 설명한 인스턴스 서브스크립트는 특정 타입의 인스턴스에서 호출하는 서브스크립트이다. 반면, 타입 자체에서 호출하는 서브스크립트도 정의할 수 있다. 이를 *타입 서브스크립트*라고 한다. 타입 서브스크립트를 정의할 때는 `subscript` 키워드 앞에 `static` 키워드를 붙인다. 클래스의 경우 `class` 키워드를 사용해 서브클래스가 슈퍼클래스의 서브스크립트 구현을 재정의할 수 있도록 허용한다. 아래 예제는 타입 서브스크립트를 정의하고 호출하는 방법을 보여준다:

```swift
enum Planet: Int {
    case mercury = 1, venus, earth, mars, jupiter, saturn, uranus, neptune
    static subscript(n: Int) -> Planet {
        return Planet(rawValue: n)!
    }
}
let mars = Planet[4]
print(mars)
```

<!--
  - test: `static-subscript`

  ```swifttest
  -> enum Planet: Int {
        case mercury = 1, venus, earth, mars, jupiter, saturn, uranus, neptune
        static subscript(n: Int) -> Planet {
           return Planet(rawValue: n)!
        }
     }
  -> let mars = Planet[4]
  >> assert(mars == Planet.mars)
  -> print(mars)
  << mars
  ```
-->

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


