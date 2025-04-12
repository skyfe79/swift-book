# 프로퍼티

프로퍼티는 인스턴스나 타입에 속한 저장된 값이나 계산된 값을 나타낸다. 프로퍼티는 특정 클래스, 구조체, 열거형과 값을 연결한다. 저장 프로퍼티는 인스턴스의 일부로 상수나 변수 값을 저장한다. 반면 계산 프로퍼티는 값을 저장하지 않고 계산한다. 계산 프로퍼티는 클래스, 구조체, 열거형에서 제공한다. 저장 프로퍼티는 클래스와 구조체에서만 제공한다.

<!--
  - test: `enumerationsCantProvideStoredProperties`

  ```swifttest
  -> enum E { case a, b; var x = 0 }
  !$ error: enums must not contain stored properties
  !! enum E { case a, b; var x = 0 }
  !! ^
  ```
-->

저장 프로퍼티와 계산 프로퍼티는 보통 특정 타입의 인스턴스와 연결된다. 하지만 프로퍼티는 타입 자체와도 연결할 수 있다. 이러한 프로퍼티를 타입 프로퍼티라고 한다.

추가로, 프로퍼티 옵저버를 정의해 프로퍼티 값의 변화를 감시하고, 이에 맞춰 커스텀 동작을 수행할 수 있다. 프로퍼티 옵저버는 직접 정의한 저장 프로퍼티에 추가할 수 있으며, 서브클래스가 슈퍼클래스로부터 상속받은 프로퍼티에도 추가할 수 있다.

<!--
  - test: `propertyObserverIntroClaims`

  ```swifttest
  -> class C {
        var x: Int = 0 {
           willSet { print("C willSet x to \(newValue)") }
           didSet { print("C didSet x from \(oldValue)") }
        }
     }
  -> class D: C {
        override var x: Int {
           willSet { print("D willSet x to \(newValue)") }
           didSet { print("D didSet x from \(oldValue)") }
        }
     }
  -> var c = C(); c.x = 42
  <- C willSet x to 42
  <- C didSet x from 0
  -> var d = D(); d.x = 42
  <- D willSet x to 42
  <- C willSet x to 42
  <- C didSet x from 0
  <- D didSet x from 0
  ```
-->

또한 프로퍼티 래퍼를 사용해 여러 프로퍼티의 getter와 setter에서 코드를 재사용할 수 있다.


## 저장 프로퍼티

가장 기본적인 형태에서 저장 프로퍼티는 특정 클래스나 구조체의 인스턴스의 일부로 저장되는 상수나 변수를 의미한다. 저장 프로퍼티는 **변수 저장 프로퍼티**(`var` 키워드로 선언)와 **상수 저장 프로퍼티**(`let` 키워드로 선언)로 구분된다.

저장 프로퍼티를 정의할 때 기본값을 지정할 수 있으며, 이는 <doc:Initialization#Default-Property-Values>에서 설명한 바와 같다. 또한 초기화 과정에서 저장 프로퍼티의 초기값을 설정하거나 수정할 수 있다. 이는 상수 저장 프로퍼티에도 적용되며, <doc:Initialization#Assigning-Constant-Properties-During-Initialization>에서 자세히 다룬다.

아래 예제는 `FixedLengthRange`라는 구조체를 정의한다. 이 구조체는 생성된 후 범위 길이를 변경할 수 없는 정수 범위를 나타낸다:

```swift
struct FixedLengthRange {
    var firstValue: Int
    let length: Int
}
var rangeOfThreeItems = FixedLengthRange(firstValue: 0, length: 3)
// 이 범위는 정수 값 0, 1, 2를 나타낸다
rangeOfThreeItems.firstValue = 6
// 이제 범위는 정수 값 6, 7, 8을 나타낸다
```

<!--
  - test: `storedProperties, storedProperties-err`

  ```swifttest
  -> struct FixedLengthRange {
        var firstValue: Int
        let length: Int
     }
  -> var rangeOfThreeItems = FixedLengthRange(firstValue: 0, length: 3)
  // 이 범위는 정수 값 0, 1, 2를 나타낸다
  -> rangeOfThreeItems.firstValue = 6
  // 이제 범위는 정수 값 6, 7, 8을 나타낸다
  ```
-->

`FixedLengthRange`의 인스턴스는 `firstValue`라는 변수 저장 프로퍼티와 `length`라는 상수 저장 프로퍼티를 가진다. 위 예제에서 `length`는 새로운 범위가 생성될 때 초기화되며, 상수 프로퍼티이기 때문에 이후 변경할 수 없다.


### 상수 구조체 인스턴스의 저장 프로퍼티

구조체의 인스턴스를 생성하고, 그 인스턴스를 상수에 할당하면, 해당 인스턴스의 프로퍼티가 변수 프로퍼티로 선언되었더라도 수정할 수 없다:

```swift
let rangeOfFourItems = FixedLengthRange(firstValue: 0, length: 4)
// 이 범위는 정수 값 0, 1, 2, 3을 나타냄
rangeOfFourItems.firstValue = 6
// firstValue가 변수 프로퍼티임에도 불구하고, 이 코드는 오류를 발생시킴
```

<!--
  - test: `storedProperties-err`

  ```swifttest
  -> let rangeOfFourItems = FixedLengthRange(firstValue: 0, length: 4)
  // 이 범위는 정수 값 0, 1, 2, 3을 나타냄
  -> rangeOfFourItems.firstValue = 6
  !$ error: cannot assign to property: 'rangeOfFourItems' is a 'let' constant
  !! rangeOfFourItems.firstValue = 6
  !! ~~~~~~~~~~~~~~~~ ^
  !$ note: change 'let' to 'var' to make it mutable
  !! let rangeOfFourItems = FixedLengthRange(firstValue: 0, length: 4)
  !! ^~~
  !! var
  // firstValue가 변수 프로퍼티임에도 불구하고, 이 코드는 오류를 발생시킴
  ```
-->

`rangeOfFourItems`가 상수(`let` 키워드)로 선언되었기 때문에, `firstValue`가 변수 프로퍼티임에도 불구하고 이를 변경할 수 없다.

이러한 동작은 구조체가 *값 타입*이기 때문이다. 값 타입의 인스턴스가 상수로 표시되면, 그 인스턴스의 모든 프로퍼티도 상수가 된다.

이와 달리 클래스는 *참조 타입*이다. 참조 타입의 인스턴스를 상수에 할당하더라도, 그 인스턴스의 변수 프로퍼티는 여전히 변경할 수 있다.

<!--
  TODO: 이 설명은 여전히 개선의 여지가 있음
-->


### 지연 저장 프로퍼티

<!--
  QUESTION: is this section too complex for this point in the book?
  Should it go in the Default Property Values section of Initialization instead?
-->

*지연 저장 프로퍼티*는 처음 사용될 때까지 초기값이 계산되지 않는 프로퍼티다. 프로퍼티 선언 앞에 `lazy` 수식어를 붙여 지연 저장 프로퍼티를 표시한다.

> 참고: 지연 프로퍼티는 반드시 변수(`var` 키워드)로 선언해야 한다. 초기값이 인스턴스 초기화가 완료된 후에야 가져올 수 있기 때문이다. 상수 프로퍼티는 초기화가 완료되기 전에 반드시 값을 가져야 하므로, 지연 프로퍼티로 선언할 수 없다.

<!--
  - test: `lazyPropertiesMustAlwaysBeVariables`

  ```swifttest
  -> class C { lazy let x = 0 }
  !$ error: 'lazy' cannot be used on a let
  !! class C { lazy let x = 0 }
  !! ^~~~~
  !!-
  ```
-->

지연 프로퍼티는 초기값이 외부 요인에 의존적이고, 해당 값이 인스턴스 초기화가 완료된 후에야 알려질 때 유용하다. 또한 초기값 설정이 복잡하거나 계산 비용이 높아서 필요할 때까지 수행하지 않아야 하는 경우에도 지연 프로퍼티를 사용한다.

<!--
  TODO: add a note that if you assign a value to a lazy property before first access,
  the initial value you give in your code will be ignored.
-->

아래 예제는 지연 저장 프로퍼티를 사용해 복잡한 클래스의 불필요한 초기화를 피하는 방법을 보여준다. 이 예제에서는 `DataImporter`와 `DataManager`라는 두 클래스를 정의하며, 두 클래스 모두 전체 코드를 보여주지는 않는다:

```swift
class DataImporter {
    /*
    DataImporter는 외부 파일에서 데이터를 가져오는 클래스다.
    이 클래스는 초기화에 상당한 시간이 걸리는 것으로 가정한다.
    */
    var filename = "data.txt"
    // DataImporter 클래스는 여기서 데이터 가져오기 기능을 제공한다.
}

class DataManager {
    lazy var importer = DataImporter()
    var data: [String] = []
    // DataManager 클래스는 여기서 데이터 관리 기능을 제공한다.
}

let manager = DataManager()
manager.data.append("Some data")
manager.data.append("Some more data")
// importer 프로퍼티의 DataImporter 인스턴스는 아직 생성되지 않았다.
```

<!--
  - test: `lazyProperties`

  ```swifttest
  -> class DataImporter {
        /*
        DataImporter is a class to import data from an external file.
        The class is assumed to take a nontrivial amount of time to initialize.
        */
        var filename = "data.txt"
        // the DataImporter class would provide data importing functionality here
  >>    init() {
  >>       print("the DataImporter instance for the importer property has now been created")
  >>    }
     }

  -> class DataManager {
        lazy var importer = DataImporter()
        var data: [String] = []
        // the DataManager class would provide data management functionality here
     }

  -> let manager = DataManager()
  -> manager.data.append("Some data")
  -> manager.data.append("Some more data")
  // the DataImporter instance for the importer property hasn't yet been created
  ```
-->

`DataManager` 클래스는 `data`라는 저장 프로퍼티를 가지며, 이 프로퍼티는 빈 `String` 배열로 초기화된다. 나머지 기능은 보여주지 않지만, `DataManager` 클래스의 목적은 이 `String` 데이터 배열을 관리하고 접근을 제공하는 것이다.

`DataManager` 클래스의 기능 중 하나는 파일에서 데이터를 가져오는 것이다. 이 기능은 `DataImporter` 클래스에서 제공하며, `DataImporter` 클래스는 초기화에 상당한 시간이 걸리는 것으로 가정한다. 이는 `DataImporter` 인스턴스가 초기화될 때 파일을 열고 메모리로 내용을 읽어야 하기 때문일 수 있다.

`DataManager` 인스턴스가 파일에서 데이터를 가져오지 않고도 데이터를 관리할 수 있기 때문에, `DataManager`는 자신이 생성될 때 `DataImporter` 인스턴스를 생성하지 않는다. 대신, `DataImporter` 인스턴스가 처음 사용될 때 생성하는 것이 더 합리적이다.

`lazy` 수식어가 붙어 있기 때문에, `importer` 프로퍼티의 `DataImporter` 인스턴스는 `importer` 프로퍼티가 처음 접근될 때 생성된다. 예를 들어, `filename` 프로퍼티를 조회할 때 생성된다:

```swift
print(manager.importer.filename)
// importer 프로퍼티의 DataImporter 인스턴스가 이제 생성되었다.
// "data.txt"를 출력한다.
```

<!--
  - test: `lazyProperties`

  ```swifttest
  -> print(manager.importer.filename)
  </ the DataImporter instance for the importer property has now been created
  <- data.txt
  ```
-->

> 참고: `lazy` 수식어가 붙은 프로퍼티가 여러 스레드에서 동시에 접근되고, 아직 초기화되지 않았다면, 프로퍼티가 단 한 번만 초기화된다는 보장은 없다.

<!--
  6/19/14, 10:54 PM [Contributor 7746]: @lazy isn't thread safe.  Global variables (and static struct/enum fields) *are*.
-->


### 저장 프로퍼티와 인스턴스 변수

Objective-C 경험이 있다면, 클래스 인스턴스의 일부로 값을 저장하고 참조할 수 있는 *두 가지* 방법을 알고 있을 것이다. 프로퍼티 외에도, 프로퍼티에 저장된 값을 위한 백업 저장소로 인스턴스 변수를 사용할 수 있다.

Swift는 이러한 개념을 단일 프로퍼티 선언으로 통합한다. Swift 프로퍼티는 해당 인스턴스 변수를 가지지 않으며, 프로퍼티의 백업 저장소에 직접 접근하지 않는다. 이 접근 방식은 값이 다양한 상황에서 어떻게 접근되는지에 대한 혼란을 피하고, 프로퍼티 선언을 단일 명확한 문장으로 단순화한다. 프로퍼티에 대한 모든 정보 --- 이름, 타입, 메모리 관리 특성 등 --- 은 타입 정의의 일부로 단일 위치에 정의된다.

<!--
  TODO: 상수 구조체의 프로퍼티 중 하나가 객체 참조인 경우 어떻게 되는가?
-->


## 계산 프로퍼티

저장 프로퍼티 외에도, 클래스, 구조체, 열거형은 *계산 프로퍼티*를 정의할 수 있다. 계산 프로퍼티는 실제로 값을 저장하지 않는다. 대신, 다른 프로퍼티와 값을 간접적으로 검색하거나 설정하기 위해 getter와 선택적인 setter를 제공한다.

```swift
struct Point {
    var x = 0.0, y = 0.0
}
struct Size {
    var width = 0.0, height = 0.0
}
struct Rect {
    var origin = Point()
    var size = Size()
    var center: Point {
        get {
            let centerX = origin.x + (size.width / 2)
            let centerY = origin.y + (size.height / 2)
            return Point(x: centerX, y: centerY)
        }
        set(newCenter) {
            origin.x = newCenter.x - (size.width / 2)
            origin.y = newCenter.y - (size.height / 2)
        }
    }
}
var square = Rect(origin: Point(x: 0.0, y: 0.0),
    size: Size(width: 10.0, height: 10.0))
let initialSquareCenter = square.center
// initialSquareCenter는 (5.0, 5.0) 위치에 있다.
square.center = Point(x: 15.0, y: 15.0)
print("square.origin은 이제 (\(square.origin.x), \(square.origin.y)) 위치에 있다.")
// 출력: "square.origin은 이제 (10.0, 10.0) 위치에 있다."
```

<!--
  - test: `computedProperties`

  ```swifttest
  -> struct Point {
        var x = 0.0, y = 0.0
     }
  -> struct Size {
        var width = 0.0, height = 0.0
     }
  -> struct Rect {
        var origin = Point()
        var size = Size()
        var center: Point {
           get {
              let centerX = origin.x + (size.width / 2)
              let centerY = origin.y + (size.height / 2)
              return Point(x: centerX, y: centerY)
           }
           set(newCenter) {
              origin.x = newCenter.x - (size.width / 2)
              origin.y = newCenter.y - (size.height / 2)
           }
        }
     }
  -> var square = Rect(origin: Point(x: 0.0, y: 0.0),
        size: Size(width: 10.0, height: 10.0))
  -> let initialSquareCenter = square.center
  /> initialSquareCenter is at (\(initialSquareCenter.x), \(initialSquareCenter.y))
  </ initialSquareCenter is at (5.0, 5.0)
  -> square.center = Point(x: 15.0, y: 15.0)
  -> print("square.origin is now at (\(square.origin.x), \(square.origin.y))")
  <- square.origin is now at (10.0, 10.0)
  ```
-->

이 예제는 기하학적 도형을 다루기 위해 세 가지 구조체를 정의한다:

- `Point`는 점의 x 좌표와 y 좌표를 캡슐화한다.
- `Size`는 `width`와 `height`를 캡슐화한다.
- `Rect`는 원점과 크기를 통해 사각형을 정의한다.

`Rect` 구조체는 `center`라는 계산 프로퍼티를 제공한다. `Rect`의 현재 중심 위치는 항상 `origin`과 `size`를 통해 결정할 수 있으므로, 중심점을 명시적인 `Point` 값으로 저장할 필요가 없다. 대신, `Rect`는 `center`라는 계산 변수에 대해 커스텀 getter와 setter를 정의하여, 사각형의 `center`를 마치 실제 저장 프로퍼티처럼 다룰 수 있게 한다.

위 예제는 `square`라는 새로운 `Rect` 변수를 생성한다. `square` 변수는 원점 `(0, 0)`과 너비 및 높이 `10`으로 초기화된다. 이 사각형은 아래 다이어그램에서 연두색 사각형으로 표시된다.

`square` 변수의 `center` 프로퍼티는 점 표기법(`square.center`)을 통해 접근되며, 이는 `center`의 getter를 호출하여 현재 프로퍼티 값을 검색한다. getter는 기존 값을 반환하는 대신, 사각형의 중심을 나타내는 새로운 `Point`를 계산하여 반환한다. 위에서 볼 수 있듯이, getter는 정확히 `(5, 5)`의 중심점을 반환한다.

그런 다음 `center` 프로퍼티를 `(15, 15)`로 설정하여 사각형을 오른쪽 위로 이동시킨다. 이는 아래 다이어그램에서 진한 초록색 사각형으로 표시된 새로운 위치로 이동한다. `center` 프로퍼티를 설정하면 `center`의 setter가 호출되어 저장된 `origin` 프로퍼티의 `x`와 `y` 값을 수정하고, 사각형을 새로운 위치로 이동시킨다.

<!-- Apple Books screenshot begins here. -->

![](computedProperties)


### 짧은 세터 선언

계산 프로퍼티의 세터가 새로운 값에 대한 이름을 정의하지 않으면, 기본적으로 `newValue`라는 이름이 사용된다. 이 짧은 표기법을 활용한 `Rect` 구조체의 대안 버전은 다음과 같다:

```swift
struct AlternativeRect {
    var origin = Point()
    var size = Size()
    var center: Point {
        get {
            let centerX = origin.x + (size.width / 2)
            let centerY = origin.y + (size.height / 2)
            return Point(x: centerX, y: centerY)
        }
        set {
            origin.x = newValue.x - (size.width / 2)
            origin.y = newValue.y - (size.height / 2)
        }
    }
}
```

<!--
  - test: `computedProperties`

  ```swifttest
  -> struct AlternativeRect {
        var origin = Point()
        var size = Size()
        var center: Point {
           get {
              let centerX = origin.x + (size.width / 2)
              let centerY = origin.y + (size.height / 2)
              return Point(x: centerX, y: centerY)
           }
           set {
              origin.x = newValue.x - (size.width / 2)
              origin.y = newValue.y - (size.height / 2)
           }
        }
     }
  ```
-->

<!-- Apple Books screenshot ends here. -->


### 짧은 Getter 선언

Getter의 전체 본문이 단일 표현식으로 이루어진 경우, getter는 암시적으로 해당 표현식을 반환한다. 다음은 이 짧은 표기법과 세터의 짧은 표기법을 활용한 `Rect` 구조체의 또 다른 버전이다:

```swift
struct CompactRect {
    var origin = Point()
    var size = Size()
    var center: Point {
        get {
            Point(x: origin.x + (size.width / 2),
                  y: origin.y + (size.height / 2))
        }
        set {
            origin.x = newValue.x - (size.width / 2)
            origin.y = newValue.y - (size.height / 2)
        }
    }
}
```

<!--
  - test: `computedProperties`

  ```swifttest
  -> struct CompactRect {
        var origin = Point()
        var size = Size()
        var center: Point {
           get {
              Point(x: origin.x + (size.width / 2),
                    y: origin.y + (size.height / 2))
           }
           set {
              origin.x = newValue.x - (size.width / 2)
              origin.y = newValue.y - (size.height / 2)
           }
        }
     }
  ```
-->

Getter에서 `return`을 생략하는 규칙은 함수에서 `return`을 생략하는 규칙과 동일하다. 이에 대한 자세한 내용은 <doc:Functions#Functions-With-an-Implicit-Return>에서 확인할 수 있다.


### 읽기 전용 계산 프로퍼티

getter는 있지만 setter가 없는 계산 프로퍼티를 *읽기 전용 계산 프로퍼티*라고 한다.  
읽기 전용 계산 프로퍼티는 항상 값을 반환하며, 점 표기법을 통해 접근할 수 있지만 다른 값으로 설정할 수 없다.

> 주의: 계산 프로퍼티(읽기 전용 계산 프로퍼티 포함)는 값이 고정되어 있지 않기 때문에 `var` 키워드를 사용해 변수 프로퍼티로 선언해야 한다.  
> `let` 키워드는 인스턴스 초기화 시 값이 한 번 설정된 후 변경할 수 없는 상수 프로퍼티에만 사용한다.

<!--
  - test: `readOnlyComputedPropertiesMustBeVariables`

  ```swifttest
  -> class C {
        let x: Int { return 42 }
        let y: Int { get { return 42 } set {} }
     }
  !! /tmp/swifttest.swift:2:15: error: 'let' declarations cannot be computed properties
  !! let x: Int { return 42 }
  !! ~~~        ^
  !! var
  !! /tmp/swifttest.swift:3:15: error: 'let' declarations cannot be computed properties
  !! let y: Int { get { return 42 } set {} }
  !! ~~~        ^
  !! var
  ```
-->

`get` 키워드와 중괄호를 생략하면 읽기 전용 계산 프로퍼티의 선언을 간소화할 수 있다:

```swift
struct Cuboid {
    var width = 0.0, height = 0.0, depth = 0.0
    var volume: Double {
        return width * height * depth
    }
}
let fourByFiveByTwo = Cuboid(width: 4.0, height: 5.0, depth: 2.0)
print("the volume of fourByFiveByTwo is \(fourByFiveByTwo.volume)")
// Prints "the volume of fourByFiveByTwo is 40.0"
```

<!--
  - test: `computedProperties`

  ```swifttest
  -> struct Cuboid {
        var width = 0.0, height = 0.0, depth = 0.0
        var volume: Double {
           return width * height * depth
        }
     }
  -> let fourByFiveByTwo = Cuboid(width: 4.0, height: 5.0, depth: 2.0)
  -> print("the volume of fourByFiveByTwo is \(fourByFiveByTwo.volume)")
  <- the volume of fourByFiveByTwo is 40.0
  ```
-->

이 예제는 `Cuboid`라는 새로운 구조체를 정의한다.  
이 구조체는 `width`, `height`, `depth` 프로퍼티를 가진 3D 직육면체를 나타낸다.  
또한 `volume`이라는 읽기 전용 계산 프로퍼티를 제공하는데, 이는 현재 직육면체의 부피를 계산해 반환한다.  
`volume`을 설정 가능하게 만드는 것은 의미가 없다.  
특정 `volume` 값에 대해 어떤 `width`, `height`, `depth` 값을 사용해야 하는지 모호해지기 때문이다.  
그럼에도 `Cuboid`가 읽기 전용 계산 프로퍼티를 제공하면 외부 사용자가 현재 계산된 부피를 확인할 수 있어 유용하다.

<!--
  NOTE: getters and setters are also allowed for constants and variables
  that aren't associated with a particular class or struct.
  Where should this be mentioned?
-->

<!--
  TODO: Anything else from https://[Internal Staging Server]/docs/StoredAndComputedVariables.html
-->

<!--
  TODO: Add an example of a computed property for an enumeration
  (now that the Enumerations chapter no longer has an example of this itself).
-->


## 프로퍼티 옵저버

프로퍼티 옵저버는 프로퍼티 값의 변화를 관찰하고 이에 반응한다. 프로퍼티 값이 설정될 때마다 프로퍼티 옵저버가 호출되며, 새로운 값이 현재 값과 동일한 경우에도 호출된다.

<!--
  - test: `observersAreCalledEvenIfNewValueIsTheSameAsOldValue`

  ```swifttest
  -> class C { var x: Int = 0 { willSet { print("willSet") } didSet { print("didSet") } } }
  -> let c = C()
  -> c.x = 24
  <- willSet
  <- didSet
  -> c.x = 24
  <- willSet
  <- didSet
  ```
-->

다음과 같은 위치에 프로퍼티 옵저버를 추가할 수 있다:

- 직접 정의한 저장 프로퍼티
- 상속받은 저장 프로퍼티
- 상속받은 계산 프로퍼티

상속받은 프로퍼티의 경우, 서브클래스에서 해당 프로퍼티를 오버라이드하여 프로퍼티 옵저버를 추가한다. 직접 정의한 계산 프로퍼티의 경우, 옵저버를 생성하려고 시도하는 대신 프로퍼티의 setter를 사용해 값의 변화를 관찰하고 반응한다. 프로퍼티 오버라이드에 대한 자세한 내용은 <doc:Inheritance#Overriding>을 참고한다.

<!--
  - test: `lazyPropertiesCanHaveObservers`

  ```swifttest
  >> class C {
        lazy var x: Int = 0 {
           willSet { print("C willSet x to \(newValue)") }
           didSet { print("C didSet x from \(oldValue)") }
        }
     }
  >> let c = C()
  >> print(c.x)
  << 0
  >> c.x = 12
  << C willSet x to 12
  << C didSet x from 0
  >> print(c.x)
  << 12
  ```
-->

<!--
  - test: `storedAndComputedInheritedPropertiesCanBeObserved`

  ```swifttest
  -> class C {
        var x = 0
        var y: Int { get { return 42 } set {} }
     }
  -> class D: C {
        override var x: Int {
           willSet { print("D willSet x to \(newValue)") }
           didSet { print("D didSet x from \(oldValue)") }
        }
        override var y: Int {
           willSet { print("D willSet y to \(newValue)") }
           didSet { print("D didSet y from \(oldValue)") }
        }
     }
  -> var d = D()
  -> d.x = 42
  <- D willSet x to 42
  <- D didSet x from 0
  -> d.y = 42
  <- D willSet y to 42
  <- D didSet y from 42
  ```
-->

프로퍼티에 다음과 같은 옵저버를 정의할 수 있다:

- `willSet`: 값이 저장되기 직전에 호출된다.
- `didSet`: 새로운 값이 저장된 직후에 호출된다.

`willSet` 옵저버를 구현하면, 새로운 프로퍼티 값이 상수 파라미터로 전달된다. 이 파라미터의 이름을 `willSet` 구현의 일부로 지정할 수 있다. 파라미터 이름과 괄호를 생략하면, 기본 파라미터 이름인 `newValue`를 사용할 수 있다.

마찬가지로, `didSet` 옵저버를 구현하면, 이전 프로퍼티 값이 상수 파라미터로 전달된다. 파라미터 이름을 지정하거나 기본 파라미터 이름인 `oldValue`를 사용할 수 있다. `didSet` 옵저버 내에서 프로퍼티에 값을 할당하면, 방금 설정된 값을 대체한다.

<!--
  - test: `assigningANewValueInADidSetReplacesTheNewValue`

  ```swifttest
  -> class C { var x: Int = 0 { didSet { x = -273 } } }
  -> let c = C()
  -> c.x = 24
  -> print(c.x)
  <- -273
  ```
-->

> Note: 서브클래스 초기화에서 프로퍼티를 설정할 때, 슈퍼클래스 초기화가 호출된 후에 슈퍼클래스 프로퍼티의 `willSet`과 `didSet` 옵저버가 호출된다. 슈퍼클래스 초기화가 호출되기 전에 클래스가 자신의 프로퍼티를 설정하는 동안에는 옵저버가 호출되지 않는다.
>
> 초기화 위임에 대한 자세한 내용은 <doc:Initialization#Initializer-Delegation-for-Value-Types>와 <doc:Initialization#Initializer-Delegation-for-Class-Types>를 참고한다.

<!--
  - test: `observersDuringInitialization`

  ```swifttest
  -> class C {
        var x: Int { willSet { print("willSet x") } didSet { print("didSet x") } }
        init(x: Int) { self.x = x }
     }
  -> let c = C(x: 42)
  -> c.x = 24
  <- willSet x
  <- didSet x
  -> class C2: C {
        var y: Int { willSet { print("willSet y") } didSet { print("didSet y") } }
        init() {
            self.y = 1
            print("calling super")
            super.init(x: 100)
            self.x = 10
        }
     }
  -> let c2 = C2()
  <- calling super
  <- willSet x
  <- didSet x
  ```
-->

다음은 `willSet`과 `didSet`이 동작하는 예시다. 아래 예시는 `StepCounter`라는 새로운 클래스를 정의하며, 이 클래스는 사람이 걷는 동안의 총 걸음 수를 추적한다. 이 클래스는 만보기나 다른 걸음 수 측정기의 입력 데이터와 함께 사용해 일상적인 운동량을 추적하는 데 활용할 수 있다.

```swift
class StepCounter {
    var totalSteps: Int = 0 {
        willSet(newTotalSteps) {
            print("About to set totalSteps to \(newTotalSteps)")
        }
        didSet {
            if totalSteps > oldValue  {
                print("Added \(totalSteps - oldValue) steps")
            }
        }
    }
}
let stepCounter = StepCounter()
stepCounter.totalSteps = 200
// About to set totalSteps to 200
// Added 200 steps
stepCounter.totalSteps = 360
// About to set totalSteps to 360
// Added 160 steps
stepCounter.totalSteps = 896
// About to set totalSteps to 896
// Added 536 steps
```

<!--
  - test: `storedProperties`

  ```swifttest
  -> class StepCounter {
        var totalSteps: Int = 0 {
           willSet(newTotalSteps) {
              print("About to set totalSteps to \(newTotalSteps)")
           }
           didSet {
              if totalSteps > oldValue  {
                 print("Added \(totalSteps - oldValue) steps")
              }
           }
        }
     }
  -> let stepCounter = StepCounter()
  -> stepCounter.totalSteps = 200
  </ About to set totalSteps to 200
  </ Added 200 steps
  -> stepCounter.totalSteps = 360
  </ About to set totalSteps to 360
  </ Added 160 steps
  -> stepCounter.totalSteps = 896
  </ About to set totalSteps to 896
  </ Added 536 steps
  ```
-->

`StepCounter` 클래스는 `Int` 타입의 `totalSteps` 프로퍼티를 선언한다. 이 프로퍼티는 `willSet`과 `didSet` 옵저버가 있는 저장 프로퍼티다.

`totalSteps` 프로퍼티의 `willSet`과 `didSet` 옵저버는 프로퍼티에 새로운 값이 할당될 때마다 호출된다. 새로운 값이 현재 값과 동일한 경우에도 호출된다.

이 예시에서 `willSet` 옵저버는 새로운 값에 대해 `newTotalSteps`라는 커스텀 파라미터 이름을 사용한다. 이 옵저버는 설정될 값을 단순히 출력한다.

`didSet` 옵저버는 `totalSteps` 값이 업데이트된 후에 호출된다. 이 옵저버는 `totalSteps`의 새로운 값과 이전 값을 비교한다. 총 걸음 수가 증가한 경우, 추가된 걸음 수를 나타내는 메시지를 출력한다. `didSet` 옵저버는 이전 값에 대해 커스텀 파라미터 이름을 제공하지 않으며, 기본 이름인 `oldValue`를 사용한다.

> Note: 옵저버가 있는 프로퍼티를 함수에 in-out 파라미터로 전달하면, `willSet`과 `didSet` 옵저버가 항상 호출된다. 이는 in-out 파라미터의 copy-in copy-out 메모리 모델 때문이다: 함수가 끝날 때 항상 프로퍼티에 값이 다시 쓰여진다. in-out 파라미터의 동작에 대한 자세한 설명은 <doc:Declarations#In-Out-Parameters>를 참고한다.

<!--
  - test: `observersCalledAfterInout`

  ```swifttest
  -> var a: Int = 0 {
         willSet { print("willSet") }
         didSet { print("didSet") }
     }
  -> func f(b: inout Int) { print("in f") }
  -> f(b: &a)
  << in f
  << willSet
  << didSet
  ```
-->

<!--
  TODO: If you add a property observer to a stored property of structure type,
  that property observer is fired whenever any of the subproperties
  of that structure instance are set. This is cool, but nonobvious.
  Provide an example of it here.
-->


## 프로퍼티 래퍼

프로퍼티 래퍼는 프로퍼티의 저장 방식을 관리하는 코드와 프로퍼티를 정의하는 코드 사이에 분리 계층을 추가한다. 예를 들어, 스레드 안전성 검사를 제공하거나 기본 데이터를 데이터베이스에 저장하는 프로퍼티가 있다면, 매번 해당 코드를 작성해야 한다. 프로퍼티 래퍼를 사용하면 래퍼를 정의할 때 관리 코드를 한 번 작성하고, 이를 여러 프로퍼티에 재사용할 수 있다.

프로퍼티 래퍼를 정의하려면 `wrappedValue` 프로퍼티를 정의하는 구조체, 열거형, 또는 클래스를 만든다. 아래 코드에서 `TwelveOrLess` 구조체는 래핑된 값이 항상 12 이하의 숫자를 포함하도록 보장한다. 더 큰 숫자를 저장하려고 하면 대신 12를 저장한다.

```swift
@propertyWrapper
struct TwelveOrLess {
    private var number = 0
    var wrappedValue: Int {
        get { return number }
        set { number = min(newValue, 12) }
    }
}
```

<!--
  - test: `small-number-wrapper, property-wrapper-expansion`

  ```swifttest
  -> @propertyWrapper
  -> struct TwelveOrLess {
         private var number = 0
         var wrappedValue: Int {
             get { return number }
             set { number = min(newValue, 12) }
         }
     }
  ```
-->

<!--
  이 예제에서는 init(wrappedValue:)가 없음. 이는 나중 예제에서 다룸.
  래핑된 값을 항상 초기화하는 것이 더 간단한 시작점임.
-->

세터는 새로운 값이 12 이하인지 확인하고, 게터는 저장된 값을 반환한다.

> 참고: 위 예제에서 `number`의 선언은 변수를 `private`로 표시하여, `number`가 `TwelveOrLess`의 구현에서만 사용되도록 보장한다. 다른 곳에서 작성된 코드는 `wrappedValue`의 게터와 세터를 통해 값에 접근하며, `number`에 직접 접근할 수 없다. `private`에 대한 자세한 정보는 <doc:AccessControl>을 참고한다.

<!--
  이 예제에서,
  숫자는 래퍼의 private ``number`` 프로퍼티에 저장되지만,
  ``wrappedValue``를 저장 프로퍼티로 구현하고
  ``didSet``을 사용하여 숫자가 항상 짝수가 되도록 보장하는
  ``EvenNumber`` 버전을 작성할 수도 있다.

  그러나 문서에서 사용하는 일반적인 프레임은
  didSet이 주로 새로운 값에 반응하는 데 사용되며,
  값을 변경하는 데 사용되지 않는다는 것이므로,
  여기서는 그 사실을 강조하지 않는다.
  willSet, set, didSet의 작업 순서는 잘 정의되어 있지만,
  주의해야 할 사항일 수 있다.
-->

<!--
  - test: `stored-property-wrappedValue`

  ```swifttest
  >> @propertyWrapper
  >> struct TwelveOrLess {
  >>     var wrappedValue: Int = 0 {
  >>         didSet {
  >>             if wrappedValue > 12 {
  >>                 wrappedValue = 12
  >>             }
  >>         }
  >>     }
  >> }
  >> struct SomeStructure {
  >>     @TwelveOrLess var someNumber: Int
  >> }
  >> var s = SomeStructure()
  >> print(s.someNumber)
  << 0
  >> s.someNumber = 10
  >> print(s.someNumber)
  << 10
  >> s.someNumber = 21
  >> print(s.someNumber)
  << 12
  ```
-->

프로퍼티 래퍼를 프로퍼티에 적용하려면, 프로퍼티 앞에 래퍼 이름을 속성으로 작성한다. 다음은 `TwelveOrLess` 프로퍼티 래퍼를 사용하여 사각형의 크기가 항상 12 이하가 되도록 보장하는 구조체이다:

```swift
struct SmallRectangle {
    @TwelveOrLess var height: Int
    @TwelveOrLess var width: Int
}

var rectangle = SmallRectangle()
print(rectangle.height)
// Prints "0"

rectangle.height = 10
print(rectangle.height)
// Prints "10"

rectangle.height = 24
print(rectangle.height)
// Prints "12"
```

<!--
  - test: `small-number-wrapper`

  ```swifttest
  -> struct SmallRectangle {
  ->     @TwelveOrLess var height: Int
  ->     @TwelveOrLess var width: Int
  -> }

  -> var rectangle = SmallRectangle()
  -> print(rectangle.height)
  <- 0

  -> rectangle.height = 10
  -> print(rectangle.height)
  <- 10

  -> rectangle.height = 24
  -> print(rectangle.height)
  <- 12
  ```
-->

`height`와 `width` 프로퍼티는 `TwelveOrLess`의 정의에서 초기값을 가져오며, `TwelveOrLess.number`를 0으로 설정한다. `TwelveOrLess`의 세터는 10을 유효한 값으로 처리하므로, `rectangle.height`에 10을 저장하는 것은 정상적으로 진행된다. 그러나 24는 `TwelveOrLess`가 허용하는 값보다 크므로, 24를 저장하려고 하면 `rectangle.height`가 허용된 최대값인 12로 설정된다.

프로퍼티 래퍼를 프로퍼티에 적용하면, 컴파일러는 래퍼를 위한 저장소를 제공하는 코드와 래퍼를 통해 프로퍼티에 접근하는 코드를 합성한다. (프로퍼티 래퍼는 래핑된 값을 저장하는 역할을 하므로, 이를 위한 합성 코드는 없다.) 특별한 속성 구문을 사용하지 않고도 프로퍼티 래퍼의 동작을 사용하는 코드를 작성할 수 있다. 예를 들어, 다음은 이전 코드 목록에서 `@TwelveOrLess`를 속성으로 작성하는 대신, `TwelveOrLess` 구조체로 프로퍼티를 명시적으로 래핑한 `SmallRectangle`의 버전이다:

```swift
struct SmallRectangle {
    private var _height = TwelveOrLess()
    private var _width = TwelveOrLess()
    var height: Int {
        get { return _height.wrappedValue }
        set { _height.wrappedValue = newValue }
    }
    var width: Int {
        get { return _width.wrappedValue }
        set { _width.wrappedValue = newValue }
    }
}
```

<!--
  - test: `property-wrapper-expansion`

  ```swifttest
  -> struct SmallRectangle {
         private var _height = TwelveOrLess()
         private var _width = TwelveOrLess()
         var height: Int {
             get { return _height.wrappedValue }
             set { _height.wrappedValue = newValue }
         }
         var width: Int {
             get { return _width.wrappedValue }
             set { _width.wrappedValue = newValue }
         }
     }
  ```
-->

`_height`와 `_width` 프로퍼티는 프로퍼티 래퍼인 `TwelveOrLess`의 인스턴스를 저장한다. `height`와 `width`의 게터와 세터는 `wrappedValue` 프로퍼티에 대한 접근을 래핑한다.


### 래핑된 프로퍼티의 초기값 설정

위 예제의 코드는 `TwelveOrLess` 정의에서 `number`에 초기값을 할당함으로써 래핑된 프로퍼티의 초기값을 설정한다. `TwelveOrLess`로 래핑된 프로퍼티를 사용하는 코드는 해당 프로퍼티에 다른 초기값을 지정할 수 없다. 예를 들어, `SmallRectangle`의 정의에서 `height`나 `width`에 초기값을 할당할 수 없다. 초기값을 설정하거나 다른 커스터마이징을 지원하기 위해, 프로퍼티 래퍼는 초기화자를 추가해야 한다. 다음은 `SmallNumber`라는 이름으로 확장된 버전의 `TwelveOrLess`로, 래핑된 값과 최대값을 설정하는 초기화자를 정의한다.

```swift
@propertyWrapper
struct SmallNumber {
    private var maximum: Int
    private var number: Int

    var wrappedValue: Int {
        get { return number }
        set { number = min(newValue, maximum) }
    }

    init() {
        maximum = 12
        number = 0
    }
    init(wrappedValue: Int) {
        maximum = 12
        number = min(wrappedValue, maximum)
    }
    init(wrappedValue: Int, maximum: Int) {
        self.maximum = maximum
        number = min(wrappedValue, maximum)
    }
}
```

`SmallNumber`의 정의는 세 가지 초기화자(`init()`, `init(wrappedValue:)`, `init(wrappedValue:maximum:)`)를 포함한다. 아래 예제들은 이러한 초기화자를 사용해 래핑된 값과 최대값을 설정한다. 초기화와 초기화자 문법에 대한 자세한 내용은 <doc:Initialization>을 참고한다.

프로퍼티에 래퍼를 적용하고 초기값을 지정하지 않으면, Swift는 `init()` 초기화자를 사용해 래퍼를 설정한다. 예를 들어:

```swift
struct ZeroRectangle {
    @SmallNumber var height: Int
    @SmallNumber var width: Int
}

var zeroRectangle = ZeroRectangle()
print(zeroRectangle.height, zeroRectangle.width)
// Prints "0 0"
```

`height`와 `width`를 래핑하는 `SmallNumber` 인스턴스는 `SmallNumber()`를 호출해 생성된다. 이 초기화자 내부의 코드는 기본값인 0과 12를 사용해 초기 래핑 값과 초기 최대값을 설정한다. 프로퍼티 래퍼는 여전히 모든 초기값을 제공한다. 이전 예제에서 `SmallRectangle`에 `TwelveOrLess`를 사용한 것과 달리, `SmallNumber`는 프로퍼티 선언의 일부로 이러한 초기값을 작성하는 것도 지원한다.

프로퍼티에 초기값을 지정하면, Swift는 `init(wrappedValue:)` 초기화자를 사용해 래퍼를 설정한다. 예를 들어:

```swift
struct UnitRectangle {
    @SmallNumber var height: Int = 1
    @SmallNumber var width: Int = 1
}

var unitRectangle = UnitRectangle()
print(unitRectangle.height, unitRectangle.width)
// Prints "1 1"
```

프로퍼티에 `= 1`을 작성하면, 이는 `init(wrappedValue:)` 초기화자를 호출하는 것으로 변환된다. `height`와 `width`를 래핑하는 `SmallNumber` 인스턴스는 `SmallNumber(wrappedValue: 1)`을 호출해 생성된다. 초기화자는 여기서 지정한 래핑 값을 사용하고, 기본 최대값인 12를 사용한다.

커스텀 속성 뒤에 괄호 안에 인수를 작성하면, Swift는 해당 인수를 받는 초기화자를 사용해 래퍼를 설정한다. 예를 들어, 초기값과 최대값을 제공하면 Swift는 `init(wrappedValue:maximum:)` 초기화자를 사용한다:

```swift
struct NarrowRectangle {
    @SmallNumber(wrappedValue: 2, maximum: 5) var height: Int
    @SmallNumber(wrappedValue: 3, maximum: 4) var width: Int
}

var narrowRectangle = NarrowRectangle()
print(narrowRectangle.height, narrowRectangle.width)
// Prints "2 3"

narrowRectangle.height = 100
narrowRectangle.width = 100
print(narrowRectangle.height, narrowRectangle.width)
// Prints "5 4"
```

`height`를 래핑하는 `SmallNumber` 인스턴스는 `SmallNumber(wrappedValue: 2, maximum: 5)`를 호출해 생성되고, `width`를 래핑하는 인스턴스는 `SmallNumber(wrappedValue: 3, maximum: 4)`를 호출해 생성된다.

프로퍼티 래퍼에 인수를 포함하면, 래퍼를 생성할 때 초기 상태를 설정하거나 다른 옵션을 전달할 수 있다. 이 구문은 프로퍼티 래퍼를 사용하는 가장 일반적인 방법이다. 속성에 필요한 인수를 제공하면, 이는 초기화자로 전달된다.

프로퍼티 래퍼 인수를 포함할 때, 할당을 사용해 초기값을 지정할 수도 있다. Swift는 이 할당을 `wrappedValue` 인수처럼 취급하고, 포함한 인수를 받는 초기화자를 사용한다. 예를 들어:

```swift
struct MixedRectangle {
    @SmallNumber var height: Int = 1
    @SmallNumber(maximum: 9) var width: Int = 2
}

var mixedRectangle = MixedRectangle()
print(mixedRectangle.height)
// Prints "1"

mixedRectangle.height = 20
print(mixedRectangle.height)
// Prints "12"
```

`height`를 래핑하는 `SmallNumber` 인스턴스는 `SmallNumber(wrappedValue: 1)`을 호출해 생성되며, 이는 기본 최대값인 12를 사용한다. `width`를 래핑하는 인스턴스는 `SmallNumber(wrappedValue: 2, maximum: 9)`를 호출해 생성된다.


### 프로퍼티 래퍼에서 값 투영하기

프로퍼티 래퍼는 래핑된 값 외에도 추가 기능을 제공할 수 있다. 이를 위해 *투영된 값(projected value)*을 정의한다. 예를 들어, 데이터베이스 접근을 관리하는 프로퍼티 래퍼는 투영된 값에 `flushDatabaseConnection()` 메서드를 노출할 수 있다. 투영된 값의 이름은 래핑된 값과 동일하지만, 달러 기호(`$`)로 시작한다. 코드에서 `$`로 시작하는 프로퍼티를 정의할 수 없기 때문에, 투영된 값은 정의한 프로퍼티와 충돌하지 않는다.

앞서 살펴본 `SmallNumber` 예제에서, 프로퍼티에 너무 큰 값을 설정하려고 하면 프로퍼티 래퍼는 값을 조정한 후 저장한다. 아래 코드는 `SmallNumber` 구조체에 `projectedValue` 프로퍼티를 추가하여, 프로퍼티 래퍼가 새 값을 저장하기 전에 값을 조정했는지 여부를 추적한다.

```swift
@propertyWrapper
struct SmallNumber {
    private var number: Int
    private(set) var projectedValue: Bool

    var wrappedValue: Int {
        get { return number }
        set {
            if newValue > 12 {
                number = 12
                projectedValue = true
            } else {
                number = newValue
                projectedValue = false
            }
        }
    }

    init() {
        self.number = 0
        self.projectedValue = false
    }
}
struct SomeStructure {
    @SmallNumber var someNumber: Int
}
var someStructure = SomeStructure()

someStructure.someNumber = 4
print(someStructure.$someNumber)
// Prints "false"

someStructure.someNumber = 55
print(someStructure.$someNumber)
// Prints "true"
```

`someStructure.$someNumber`를 작성하면 래퍼의 투영된 값에 접근한다. 4와 같은 작은 숫자를 저장한 후에는 `someStructure.$someNumber`의 값이 `false`이다. 하지만 55와 같이 너무 큰 숫자를 저장하려고 하면 투영된 값은 `true`가 된다.

프로퍼티 래퍼는 투영된 값으로 어떤 타입의 값이든 반환할 수 있다. 이 예제에서는 프로퍼티 래퍼가 숫자가 조정되었는지 여부만 노출하므로, 불리언 값을 투영된 값으로 노출한다. 더 많은 정보를 노출해야 하는 래퍼는 다른 타입의 인스턴스를 반환하거나, `self`를 반환하여 래퍼 인스턴스 자체를 투영된 값으로 노출할 수 있다.

타입의 일부인 코드(예: 프로퍼티 게터나 인스턴스 메서드)에서 투영된 값에 접근할 때는, 다른 프로퍼티에 접근할 때와 마찬가지로 프로퍼티 이름 앞에 `self.`를 생략할 수 있다. 다음 예제의 코드는 `height`와 `width` 주변의 래퍼의 투영된 값을 `$height`와 `$width`로 참조한다:

```swift
enum Size {
    case small, large
}

struct SizedRectangle {
    @SmallNumber var height: Int
    @SmallNumber var width: Int

    mutating func resize(to size: Size) -> Bool {
        switch size {
        case .small:
            height = 10
            width = 20
        case .large:
            height = 100
            width = 100
        }
        return $height || $width
    }
}
```

프로퍼티 래퍼 구문은 게터와 세터가 있는 프로퍼티에 대한 문법적 설탕(syntactic sugar)일 뿐이므로, `height`와 `width`에 접근하는 것은 다른 프로퍼티에 접근하는 것과 동일하게 동작한다. 예를 들어, `resize(to:)`의 코드는 프로퍼티 래퍼를 사용하여 `height`와 `width`에 접근한다. `resize(to: .large)`를 호출하면, `.large`에 대한 스위치 케이스가 사각형의 높이와 너비를 100으로 설정한다. 래퍼는 이 프로퍼티의 값이 12보다 크지 않도록 방지하고, 값을 조정했다는 사실을 기록하기 위해 투영된 값을 `true`로 설정한다. `resize(to:)`의 끝에서, 반환문은 `$height`와 `$width`를 확인하여 프로퍼티 래퍼가 `height` 또는 `width`를 조정했는지 여부를 결정한다.


## 전역 변수와 지역 변수

앞서 설명한 계산 프로퍼티와 프로퍼티 관찰 기능은 *전역 변수*와 *지역 변수*에서도 사용할 수 있다. 전역 변수는 함수, 메서드, 클로저, 타입 컨텍스트 외부에서 정의된 변수를 의미한다. 반면 지역 변수는 함수, 메서드, 클로저 컨텍스트 내부에서 정의된 변수를 말한다.

지금까지 다룬 전역 변수와 지역 변수는 모두 *저장 변수*였다. 저장 변수는 저장 프로퍼티와 마찬가지로 특정 타입의 값을 저장하고, 그 값을 설정하거나 가져올 수 있다.

하지만 전역 또는 지역 범위에서 *계산 변수*를 정의하거나 저장 변수에 관찰자를 추가할 수도 있다. 계산 변수는 값을 저장하지 않고 계산하며, 계산 프로퍼티와 동일한 방식으로 작성한다.

<!--
  - test: `computedVariables`

  ```swifttest
  -> var a: Int { get { return 42 } set { print("set a to \(newValue)") } }
  -> a = 37
  <- set a to 37
  -> print(a)
  <- 42
  ```
-->

<!--
  - test: `observersForStoredVariables`

  ```swifttest
  -> var a: Int = 0 { willSet { print("willSet") } didSet { print("didSet") } }
  -> a = 42
  <- willSet
  <- didSet
  ```
-->

> 참고: 전역 상수와 변수는 지연 계산 프로퍼티와 유사한 방식으로 항상 지연 계산된다. 하지만 지연 저장 프로퍼티와 달리 전역 상수와 변수는 `lazy` 수식어를 붙일 필요가 없다.
>
> 반면 지역 상수와 변수는 절대 지연 계산되지 않는다.

프로퍼티 래퍼는 지역 저장 변수에 적용할 수 있지만, 전역 변수나 계산 변수에는 적용할 수 없다. 예를 들어, 아래 코드에서 `myNumber`는 `SmallNumber`를 프로퍼티 래퍼로 사용한다.

```swift
func someFunction() {
    @SmallNumber var myNumber: Int = 0

    myNumber = 10
    // 이제 myNumber는 10

    myNumber = 24
    // 이제 myNumber는 12
}
```

<!--
  - test: `property-wrapper-init`

  ```swifttest
  -> func someFunction() {
  ->     @SmallNumber var myNumber: Int = 0

         myNumber = 10
         // 이제 myNumber는 10
  >>     print(myNumber)

         myNumber = 24
         // 이제 myNumber는 12
  >>     print(myNumber)
     }
  >> someFunction()
  << 10
  << 12
  ```
-->

프로퍼티에 `SmallNumber`를 적용할 때와 마찬가지로, `myNumber`의 값을 10으로 설정하는 것은 유효하다. 하지만 프로퍼티 래퍼가 12보다 큰 값을 허용하지 않기 때문에, `myNumber`는 24 대신 12로 설정된다.

<!--
  프로퍼티 래퍼를 사용한 지역 변수에 대한 논의는 나중에 진행한다.
  <rdar://problem/74616133> 문제를 해결하기 위해 init(wrappedValue:)를 사용해야 하기 때문이다.
-->

<!--
  TODO: 여기서 말하는 "전역 변수"가 정확히 무엇을 의미하는지 명확히 해야 한다.
  [Contributor 6004]에 따르면, 플레이그라운드, REPL, main.swift에서 정의된 모든 것은 전역 변수가 아니라 최상위 코드의 지역 변수다.
-->

<!--
  TODO: 이로 인해 현재 "항상 지연 계산" 주장을 테스트할 수 없다.
-->


## 타입 프로퍼티

인스턴스 프로퍼티는 특정 타입의 인스턴스에 속하는 프로퍼티다. 해당 타입의 새로운 인스턴스를 생성할 때마다, 각 인스턴스는 다른 인스턴스와 독립적인 프로퍼티 값을 가진다.

타입 자체에 속하는 프로퍼티를 정의할 수도 있다. 이러한 프로퍼티는 타입의 인스턴스가 아닌 타입 자체에 속하며, 해당 타입의 인스턴스를 아무리 많이 생성하더라도 단 하나의 복사본만 존재한다. 이런 종류의 프로퍼티를 *타입 프로퍼티*라고 한다.

타입 프로퍼티는 특정 타입의 *모든* 인스턴스에 공통적으로 적용되는 값을 정의하는 데 유용하다. 예를 들어, 모든 인스턴스가 사용할 수 있는 상수 프로퍼티(C의 정적 상수와 유사)나, 해당 타입의 모든 인스턴스에 전역적으로 적용되는 값을 저장하는 변수 프로퍼티(C의 정적 변수와 유사)를 정의할 때 사용할 수 있다.

저장된 타입 프로퍼티는 변수나 상수로 선언할 수 있다. 계산된 타입 프로퍼티는 계산된 인스턴스 프로퍼티와 마찬가지로 항상 변수 프로퍼티로 선언된다.

> 주의: 저장된 인스턴스 프로퍼티와 달리, 저장된 타입 프로퍼티는 항상 기본값을 지정해야 한다. 이는 타입 자체가 초기화 시 저장된 타입 프로퍼티에 값을 할당할 수 있는 초기화 메서드를 가지고 있지 않기 때문이다.
>
> 저장된 타입 프로퍼티는 처음 접근할 때 지연 초기화된다. 여러 스레드가 동시에 접근하더라도 단 한 번만 초기화되도록 보장되며, `lazy` 수정자로 표시할 필요가 없다.


### 타입 프로퍼티 문법

C와 Objective-C에서는 타입과 관련된 정적 상수와 변수를 *전역* 정적 변수로 정의한다. 반면 Swift에서는 타입 프로퍼티를 타입 정의의 일부로 작성하며, 타입의 외부 중괄호 안에 위치한다. 각 타입 프로퍼티는 해당 타입에 명시적으로 범위가 지정된다.

타입 프로퍼티는 `static` 키워드로 정의한다. 클래스 타입의 계산된 타입 프로퍼티의 경우, `class` 키워드를 사용해 서브클래스가 슈퍼클래스의 구현을 재정의할 수 있게 한다. 아래 예제는 저장된 타입 프로퍼티와 계산된 타입 프로퍼티의 문법을 보여준다:

```swift
struct SomeStructure {
    static var storedTypeProperty = "Some value."
    static var computedTypeProperty: Int {
        return 1
    }
}
enum SomeEnumeration {
    static var storedTypeProperty = "Some value."
    static var computedTypeProperty: Int {
        return 6
    }
}
class SomeClass {
    static var storedTypeProperty = "Some value."
    static var computedTypeProperty: Int {
        return 27
    }
    class var overrideableComputedTypeProperty: Int {
        return 107
    }
}
```

<!--
  - test: `typePropertySyntax`

  ```swifttest
  -> struct SomeStructure {
        static var storedTypeProperty = "Some value."
        static var computedTypeProperty: Int {
           return 1
        }
     }
  -> enum SomeEnumeration {
        static var storedTypeProperty = "Some value."
        static var computedTypeProperty: Int {
           return 6
        }
     }
  -> class SomeClass {
        static var storedTypeProperty = "Some value."
        static var computedTypeProperty: Int {
           return 27
        }
        class var overrideableComputedTypeProperty: Int {
           return 107
        }
     }
  ```
-->

<!--
  - test: `classComputedTypePropertiesAreOverrideable`

  ```swifttest
  -> class A { class var cp: String { return "A" } }
  -> class B: A { override class var cp: String { return "B" } }
  -> assert(A.cp == "A")
  -> assert(B.cp == "B")
  ```
-->

<!--
  - test: `staticComputedTypePropertiesAreFinal`

  ```swifttest
  -> class A { static var cp: String { return "A" } }
  -> class B: A { override static var cp: String { return "B" } }
  !$ error: cannot override static property
  !! class B: A { override static var cp: String { return "B" } }
  !!                                  ^
  !$ note: overridden declaration is here
  !! class A { static var cp: String { return "A" } }
  !!                      ^
  ```
-->

> 참고: 위의 계산된 타입 프로퍼티 예제는 읽기 전용 계산된 타입 프로퍼티를 보여준다. 하지만 계산된 인스턴스 프로퍼티와 동일한 문법으로 읽기-쓰기 계산된 타입 프로퍼티도 정의할 수 있다.


### 타입 프로퍼티 조회 및 설정

타입 프로퍼티는 인스턴스 프로퍼티와 마찬가지로 점 문법을 사용해 조회하고 설정한다. 하지만 타입 프로퍼티는 인스턴스가 아닌 타입 자체에 대해 조회하고 설정한다. 예를 들어:

```swift
print(SomeStructure.storedTypeProperty)
// "Some value." 출력
SomeStructure.storedTypeProperty = "Another value."
print(SomeStructure.storedTypeProperty)
// "Another value." 출력
print(SomeEnumeration.computedTypeProperty)
// "6" 출력
print(SomeClass.computedTypeProperty)
// "27" 출력
```

<!--
  - test: `typePropertySyntax`

  ```swifttest
  -> print(SomeStructure.storedTypeProperty)
  <- Some value.
  -> SomeStructure.storedTypeProperty = "Another value."
  -> print(SomeStructure.storedTypeProperty)
  <- Another value.
  -> print(SomeEnumeration.computedTypeProperty)
  <- 6
  -> print(SomeClass.computedTypeProperty)
  <- 27
  ```
-->

다음 예제에서는 오디오 채널의 음량을 측정하는 오디오 레벨 미터를 모델링하는 구조체의 일부로 두 개의 저장 타입 프로퍼티를 사용한다. 각 채널은 `0`부터 `10`까지의 정수 값을 가진다.

아래 그림은 두 오디오 채널을 결합해 스테레오 오디오 레벨 미터를 모델링하는 방법을 보여준다. 채널의 음량이 `0`이면 해당 채널의 모든 불이 꺼진다. 음량이 `10`이면 모든 불이 켜진다. 이 그림에서 왼쪽 채널의 현재 레벨은 `9`, 오른쪽 채널의 현재 레벨은 `7`이다:

![](staticPropertiesVUMeter)

위에서 설명한 오디오 채널은 `AudioChannel` 구조체의 인스턴스로 표현된다:

```swift
struct AudioChannel {
    static let thresholdLevel = 10
    static var maxInputLevelForAllChannels = 0
    var currentLevel: Int = 0 {
        didSet {
            if currentLevel > AudioChannel.thresholdLevel {
                // 새 오디오 레벨을 임계값으로 제한
                currentLevel = AudioChannel.thresholdLevel
            }
            if currentLevel > AudioChannel.maxInputLevelForAllChannels {
                // 이를 새로운 전체 최대 입력 레벨로 저장
                AudioChannel.maxInputLevelForAllChannels = currentLevel
            }
        }
    }
}
```

<!--
  - test: `staticProperties`

  ```swifttest
  -> struct AudioChannel {
        static let thresholdLevel = 10
        static var maxInputLevelForAllChannels = 0
        var currentLevel: Int = 0 {
           didSet {
              if currentLevel > AudioChannel.thresholdLevel {
                 // 새 오디오 레벨을 임계값으로 제한
                 currentLevel = AudioChannel.thresholdLevel
              }
              if currentLevel > AudioChannel.maxInputLevelForAllChannels {
                 // 이를 새로운 전체 최대 입력 레벨로 저장
                 AudioChannel.maxInputLevelForAllChannels = currentLevel
              }
           }
        }
     }
  ```
-->

`AudioChannel` 구조체는 기능을 지원하기 위해 두 개의 저장 타입 프로퍼티를 정의한다. 첫 번째는 `thresholdLevel`로, 오디오 레벨이 가질 수 있는 최대 임계값을 정의한다. 이 값은 모든 `AudioChannel` 인스턴스에 대해 `10`으로 고정된다. 만약 `10`보다 높은 값이 들어오면 이 임계값으로 제한된다(아래에서 설명).

두 번째 타입 프로퍼티는 `maxInputLevelForAllChannels`라는 변수 저장 프로퍼티다. 이 프로퍼티는 *모든* `AudioChannel` 인스턴스가 받은 최대 입력 값을 추적한다. 초기값은 `0`이다.

`AudioChannel` 구조체는 또한 `currentLevel`이라는 저장 인스턴스 프로퍼티를 정의한다. 이 프로퍼티는 `0`부터 `10`까지의 스케일로 채널의 현재 오디오 레벨을 나타낸다.

`currentLevel` 프로퍼티는 값이 설정될 때마다 `currentLevel`의 값을 확인하는 `didSet` 프로퍼티 옵저버를 가지고 있다. 이 옵저버는 두 가지 검사를 수행한다:

- `currentLevel`의 새 값이 허용된 `thresholdLevel`보다 크면, 프로퍼티 옵저버는 `currentLevel`을 `thresholdLevel`로 제한한다.
- (제한 후) `currentLevel`의 새 값이 *모든* `AudioChannel` 인스턴스가 이전에 받은 값보다 크면, 프로퍼티 옵저버는 새 `currentLevel` 값을 `maxInputLevelForAllChannels` 타입 프로퍼티에 저장한다.

> 참고: 두 검사 중 첫 번째에서 `didSet` 옵저버는 `currentLevel`을 다른 값으로 설정한다. 하지만 이로 인해 옵저버가 다시 호출되지는 않는다.

`AudioChannel` 구조체를 사용해 스테레오 사운드 시스템의 오디오 레벨을 나타내는 `leftChannel`과 `rightChannel`이라는 두 개의 새 오디오 채널을 생성할 수 있다:

```swift
var leftChannel = AudioChannel()
var rightChannel = AudioChannel()
```

<!--
  - test: `staticProperties`

  ```swifttest
  -> var leftChannel = AudioChannel()
  -> var rightChannel = AudioChannel()
  ```
-->

*왼쪽* 채널의 `currentLevel`을 `7`로 설정하면, `maxInputLevelForAllChannels` 타입 프로퍼티가 `7`로 업데이트되는 것을 확인할 수 있다:

```swift
leftChannel.currentLevel = 7
print(leftChannel.currentLevel)
// "7" 출력
print(AudioChannel.maxInputLevelForAllChannels)
// "7" 출력
```

<!--
  - test: `staticProperties`

  ```swifttest
  -> leftChannel.currentLevel = 7
  -> print(leftChannel.currentLevel)
  <- 7
  -> print(AudioChannel.maxInputLevelForAllChannels)
  <- 7
  ```
-->

*오른쪽* 채널의 `currentLevel`을 `11`로 설정하려고 하면, 오른쪽 채널의 `currentLevel` 프로퍼티가 최대값인 `10`으로 제한되고, `maxInputLevelForAllChannels` 타입 프로퍼티가 `10`으로 업데이트되는 것을 확인할 수 있다:

```swift
rightChannel.currentLevel = 11
print(rightChannel.currentLevel)
// "10" 출력
print(AudioChannel.maxInputLevelForAllChannels)
// "10" 출력
```

<!--
  - test: `staticProperties`

  ```swifttest
  -> rightChannel.currentLevel = 11
  -> print(rightChannel.currentLevel)
  <- 10
  -> print(AudioChannel.maxInputLevelForAllChannels)
  <- 10
  ```
-->

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


