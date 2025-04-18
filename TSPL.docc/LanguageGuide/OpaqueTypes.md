# 불투명 타입과 박스 프로토콜 타입

값의 타입에 대한 구현 세부사항을 숨기는 방법을 알아본다.

Swift는 값의 타입 정보를 숨기는 두 가지 방법을 제공한다:
불투명 타입과 박스 프로토콜 타입.
타입 정보를 숨기는 것은 모듈과 모듈을 호출하는 코드 사이의 경계에서 유용하다.
반환값의 실제 타입을 비공개로 유지할 수 있기 때문이다.

불투명 타입을 반환하는 함수나 메서드는
반환값의 타입 정보를 숨긴다.
함수의 반환 타입으로 구체적인 타입을 제공하는 대신,
반환값이 지원하는 프로토콜을 기준으로 설명한다.
불투명 타입은 타입 식별성을 유지한다 ---
컴파일러는 타입 정보에 접근할 수 있지만,
모듈을 사용하는 클라이언트는 접근할 수 없다.

박스 프로토콜 타입은 주어진 프로토콜을 준수하는
어떤 타입의 인스턴스든 저장할 수 있다.
박스 프로토콜 타입은 타입 식별성을 유지하지 않는다 ---
값의 구체적인 타입은 런타임에야 알 수 있으며,
다른 값이 저장되면서 시간에 따라 변경될 수 있다.


## 불투명 타입이 해결하는 문제

예를 들어, ASCII 아트 도형을 그리는 모듈을 작성한다고 가정해보자. ASCII 아트 도형의 기본 특징은 `draw()` 함수를 통해 해당 도형의 문자열 표현을 반환하는 것이다. 이를 `Shape` 프로토콜의 요구사항으로 정의할 수 있다:

```swift
protocol Shape {
    func draw() -> String
}

struct Triangle: Shape {
    var size: Int
    func draw() -> String {
       var result: [String] = []
       for length in 1...size {
           result.append(String(repeating: "*", count: length))
       }
       return result.joined(separator: "\n")
    }
}
let smallTriangle = Triangle(size: 3)
print(smallTriangle.draw())
// *
// **
// ***
```

<!--
  - test: `opaque-result`

  ```swifttest
  -> protocol Shape {
         func draw() -> String
     }

  -> struct Triangle: Shape {
        var size: Int
        func draw() -> String {
            var result: [String] = []
            for length in 1...size {
                result.append(String(repeating: "*", count: length))
            }
            return result.joined(separator: "\n")
        }
     }
  -> let smallTriangle = Triangle(size: 3)
  -> print(smallTriangle.draw())
  </ *
  </ **
  </ ***
  ```
-->

도형을 수직으로 뒤집는 연산을 구현하기 위해 제네릭을 사용할 수 있다. 하지만 이 접근 방식에는 중요한 제약이 있다: 뒤집힌 결과는 이를 생성하는 데 사용된 정확한 제네릭 타입을 노출한다.

```swift
struct FlippedShape<T: Shape>: Shape {
    var shape: T
    func draw() -> String {
        let lines = shape.draw().split(separator: "\n")
        return lines.reversed().joined(separator: "\n")
    }
}
let flippedTriangle = FlippedShape(shape: smallTriangle)
print(flippedTriangle.draw())
// ***
// **
// *
```

<!--
  - test: `opaque-result`

  ```swifttest
  -> struct FlippedShape<T: Shape>: Shape {
         var shape: T
         func draw() -> String {
             let lines = shape.draw().split(separator: "\n")
             return lines.reversed().joined(separator: "\n")
         }
     }
  -> let flippedTriangle = FlippedShape(shape: smallTriangle)
  -> print(flippedTriangle.draw())
  </ ***
  </ **
  </ *
  ```
-->

이 방식으로 `JoinedShape<T: Shape, U: Shape>` 구조체를 정의하여 두 도형을 수직으로 결합하면, 삼각형과 뒤집힌 삼각형을 결합할 때 `JoinedShape<Triangle, FlippedShape<Triangle>>`과 같은 타입이 생성된다.

```swift
struct JoinedShape<T: Shape, U: Shape>: Shape {
    var top: T
    var bottom: U
    func draw() -> String {
       return top.draw() + "\n" + bottom.draw()
    }
}
let joinedTriangles = JoinedShape(top: smallTriangle, bottom: flippedTriangle)
print(joinedTriangles.draw())
// *
// **
// ***
// ***
// **
// *
```

<!--
  - test: `opaque-result`

  ```swifttest
  -> struct JoinedShape<T: Shape, U: Shape>: Shape {
        var top: T
        var bottom: U
        func draw() -> String {
            return top.draw() + "\n" + bottom.draw()
        }
     }
  -> let joinedTriangles = JoinedShape(top: smallTriangle, bottom: flippedTriangle)
  -> print(joinedTriangles.draw())
  </ *
  </ **
  </ ***
  </ ***
  </ **
  </ *
  ```
-->

도형 생성에 대한 자세한 정보를 노출하면, ASCII 아트 모듈의 공개 인터페이스에 포함되지 않아야 할 타입이 전체 반환 타입을 명시해야 하는 필요성 때문에 누출될 수 있다. 모듈 내부 코드는 다양한 방식으로 동일한 도형을 구성할 수 있으며, 모듈 외부에서 도형을 사용하는 코드는 변환 목록에 대한 구현 세부 사항을 고려할 필요가 없다. `JoinedShape` 및 `FlippedShape`와 같은 래퍼 타입은 모듈 사용자에게 중요하지 않으며, 노출되어서는 안 된다. 모듈의 공개 인터페이스는 도형을 결합하거나 뒤집는 연산으로 구성되며, 이러한 연산은 다른 `Shape` 값을 반환한다.


## 불투명 타입 반환하기

불투명 타입은 제네릭 타입의 반대 개념으로 생각할 수 있다. 제네릭 타입은 함수를 호출하는 코드가 함수의 파라미터와 반환값의 타입을 선택할 수 있게 한다. 이때 함수의 구현은 호출자로부터 추상화된다. 예를 들어, 다음 코드의 함수는 호출자에 따라 반환 타입이 결정된다:

```swift
func max<T>(_ x: T, _ y: T) -> T where T: Comparable { ... }
```

`max(_:_:)`를 호출하는 코드는 `x`와 `y`의 값을 선택하고, 이 값의 타입이 `T`의 구체적인 타입을 결정한다. 호출자는 `Comparable` 프로토콜을 준수하는 어떤 타입이든 사용할 수 있다. 함수 내부의 코드는 일반적인 방식으로 작성되어 호출자가 제공하는 타입을 처리할 수 있다. `max(_:_:)`의 구현은 모든 `Comparable` 타입이 공유하는 기능만 사용한다.

불투명 반환 타입을 가진 함수에서는 이 역할이 반대로 적용된다. 불투명 타입은 함수 구현이 반환값의 타입을 선택할 수 있게 한다. 이때 호출 코드로부터 추상화된다. 예를 들어, 다음 예제의 함수는 사다리꼴을 반환하지만, 해당 도형의 구체적인 타입을 노출하지 않는다.

```swift
struct Square: Shape {
    var size: Int
    func draw() -> String {
        let line = String(repeating: "*", count: size)
        let result = Array<String>(repeating: line, count: size)
        return result.joined(separator: "\n")
    }
}

func makeTrapezoid() -> some Shape {
    let top = Triangle(size: 2)
    let middle = Square(size: 2)
    let bottom = FlippedShape(shape: top)
    let trapezoid = JoinedShape(
        top: top,
        bottom: JoinedShape(top: middle, bottom: bottom)
    )
    return trapezoid
}
let trapezoid = makeTrapezoid()
print(trapezoid.draw())
// *
// **
// **
// **
// **
// *
```

이 예제에서 `makeTrapezoid()` 함수는 반환 타입을 `some Shape`로 선언한다. 결과적으로 이 함수는 `Shape` 프로토콜을 준수하는 특정 타입의 값을 반환하지만, 구체적인 타입을 지정하지 않는다. 이 방식으로 `makeTrapezoid()`를 작성하면, 반환값이 도형이라는 기본적인 인터페이스를 표현할 수 있으면서도, 도형을 구성하는 구체적인 타입을 공개하지 않을 수 있다. 이 구현은 두 개의 삼각형과 하나의 사각형을 사용하지만, 함수는 반환 타입을 변경하지 않고도 다양한 방식으로 사다리꼴을 그릴 수 있다.

이 예제는 불투명 반환 타입이 제네릭 타입의 반대 개념임을 잘 보여준다. `makeTrapezoid()` 내부의 코드는 `Shape` 프로토콜을 준수하는 어떤 타입이든 반환할 수 있다. 호출 코드는 제네릭 함수의 구현처럼 일반적인 방식으로 작성되어, `makeTrapezoid()`가 반환하는 어떤 `Shape` 값이든 처리할 수 있어야 한다.

불투명 반환 타입은 제네릭과 함께 사용할 수도 있다. 다음 코드의 두 함수는 모두 `Shape` 프로토콜을 준수하는 어떤 타입의 값을 반환한다.

```swift
func flip<T: Shape>(_ shape: T) -> some Shape {
    return FlippedShape(shape: shape)
}
func join<T: Shape, U: Shape>(_ top: T, _ bottom: U) -> some Shape {
    JoinedShape(top: top, bottom: bottom)
}

let opaqueJoinedTriangles = join(smallTriangle, flip(smallTriangle))
print(opaqueJoinedTriangles.draw())
// *
// **
// ***
// ***
// **
// *
```

이 예제에서 `opaqueJoinedTriangles`의 값은 이 장의 앞부분에서 다룬 제네릭 예제의 `joinedTriangles`와 동일하다. 그러나 이 예제에서는 `flip(_:)`과 `join(_:_:)`이 제네릭 도형 연산에서 반환하는 기본 타입을 불투명 반환 타입으로 감싸기 때문에, 해당 타입이 노출되지 않는다. 두 함수는 의존하는 타입이 제네릭이므로 제네릭 함수이며, 함수의 타입 파라미터는 `FlippedShape`와 `JoinedShape`에 필요한 타입 정보를 전달한다.

불투명 반환 타입을 가진 함수가 여러 위치에서 반환할 경우, 모든 가능한 반환값은 동일한 타입을 가져야 한다. 제네릭 함수의 경우, 반환 타입은 함수의 제네릭 타입 파라미터를 사용할 수 있지만, 여전히 단일 타입이어야 한다. 예를 들어, 다음은 사각형에 대한 특수 케이스를 포함한 도형 뒤집기 함수의 *잘못된* 버전이다:

```swift
func invalidFlip<T: Shape>(_ shape: T) -> some Shape {
    if shape is Square {
        return shape // Error: return types don't match
    }
    return FlippedShape(shape: shape) // Error: return types don't match
}
```

이 함수를 `Square`와 함께 호출하면 `Square`를 반환하고, 그렇지 않으면 `FlippedShape`를 반환한다. 이는 단일 타입의 값을 반환해야 한다는 요구사항을 위반하므로 `invalidFlip(_:)`는 유효하지 않은 코드이다. `invalidFlip(_:)`을 수정하는 한 가지 방법은 사각형에 대한 특수 케이스를 `FlippedShape`의 구현으로 옮기는 것이다. 이렇게 하면 함수가 항상 `FlippedShape` 값을 반환할 수 있다:

```swift
struct FlippedShape<T: Shape>: Shape {
    var shape: T
    func draw() -> String {
        if shape is Square {
           return shape.draw()
        }
        let lines = shape.draw().split(separator: "\n")
        return lines.reversed().joined(separator: "\n")
    }
}
```

단일 타입을 반환해야 한다는 요구사항은 불투명 반환 타입에서 제네릭을 사용하는 것을 방해하지 않는다. 다음은 타입 파라미터를 반환값의 기본 타입에 통합한 함수의 예시이다:

```swift
func `repeat`<T: Shape>(shape: T, count: Int) -> some Collection {
    return Array<T>(repeating: shape, count: count)
}
```

이 경우, 반환값의 기본 타입은 `T`에 따라 달라진다. 어떤 도형이 전달되든, `repeat(shape:count:)`는 해당 도형의 배열을 생성하고 반환한다. 그러나 반환값은 항상 `[T]`라는 동일한 기본 타입을 가지므로, 불투명 반환 타입을 가진 함수가 단일 타입의 값을 반환해야 한다는 요구사항을 충족한다.


## 박싱된 프로토콜 타입

박싱된 프로토콜 타입은 때때로 *실존 타입(existential type)*이라고도 불린다. 이 용어는 "프로토콜을 준수하는 타입 *T*가 존재한다"는 문구에서 유래했다. 박싱된 프로토콜 타입을 만들려면 프로토콜 이름 앞에 `any`를 붙이면 된다. 다음은 그 예시다:

```swift
struct VerticalShapes: Shape {
    var shapes: [any Shape]
    func draw() -> String {
        return shapes.map { $0.draw() }.joined(separator: "\n\n")
    }
}

let largeTriangle = Triangle(size: 5)
let largeSquare = Square(size: 5)
let vertical = VerticalShapes(shapes: [largeTriangle, largeSquare])
print(vertical.draw())
```

<!--
  - test: `boxed-protocol-types`

  ```swifttest
   >> protocol Shape {
   >>    func draw() -> String
   >> }
   >> struct Triangle: Shape {
   >>    var size: Int
   >>    func draw() -> String {
   >>        var result: [String] = []
   >>        for length in 1...size {
   >>            result.append(String(repeating: "*", count: length))
   >>        }
   >>        return result.joined(separator: "\n")
   >>    }
   >> }
   >> struct Square: Shape {
   >>     var size: Int
   >>     func draw() -> String {
   >>         let line = String(repeating: "*", count: size)
   >>         let result = Array<String>(repeating: line, count: size)
   >>         return result.joined(separator: "\n")
   >>     }
   >
   -> struct VerticalShapes: Shape {
          var shapes: [any Shape]
          func draw() -> String {
              return shapes.map { $0.draw() }.joined(separator: "\n\n")
          }
      }
   ->
   -> let largeTriangle = Triangle(size: 5)
   -> let largeSquare = Square(size: 5)
   -> let vertical = VerticalShapes(shapes: [largeTriangle, largeSquare])
   -> print(vertical.draw())
   << *
   << **
   << ***
   << ****
   << *****
   <<-
   << *****
   << *****
   << *****
   << *****
   << *****
  ```
-->

위 예시에서 `VerticalShapes`는 `shapes`의 타입을 `[any Shape]`로 선언했다. 이는 박싱된 `Shape` 엘리먼트의 배열을 의미한다. 배열의 각 엘리먼트는 서로 다른 타입일 수 있으며, 각 타입은 `Shape` 프로토콜을 준수해야 한다. 이러한 런타임 유연성을 지원하기 위해 Swift는 필요할 때 간접적인 레이어를 추가한다. 이 간접적인 레이어를 *박스*라고 부르며, 이는 성능상의 비용이 발생한다.

`VerticalShapes` 타입 내부에서는 `Shape` 프로토콜이 요구하는 메서드, 프로퍼티, 서브스크립트를 사용할 수 있다. 예를 들어, `VerticalShapes`의 `draw()` 메서드는 배열의 각 엘리먼트에서 `draw()` 메서드를 호출한다. 이 메서드는 `Shape` 프로토콜이 `draw()` 메서드를 요구하기 때문에 사용 가능하다. 반면, 삼각형의 `size` 프로퍼티나 `Shape` 프로토콜이 요구하지 않는 다른 프로퍼티나 메서드에 접근하려고 하면 오류가 발생한다.

`shapes`에 사용할 수 있는 세 가지 타입을 비교해 보자:

- 제네릭을 사용하는 경우, `struct VerticalShapes<S: Shape>`와 `var shapes: [S]`로 작성하면 배열의 엘리먼트는 특정한 하나의 도형 타입이 되며, 이 특정 타입의 정체성은 배열과 상호작용하는 모든 코드에서 확인할 수 있다.

- 불투명 타입을 사용하는 경우, `var shapes: [some Shape]`로 작성하면 배열의 엘리먼트는 특정한 하나의 도형 타입이 되며, 이 특정 타입의 정체성은 숨겨진다.

- 박싱된 프로토콜 타입을 사용하는 경우, `var shapes: [any Shape]`로 작성하면 배열은 서로 다른 타입의 엘리먼트를 저장할 수 있으며, 이 타입들의 정체성은 숨겨진다.

이 경우, `VerticalShapes`를 호출하는 쪽에서 서로 다른 종류의 도형을 혼합할 수 있게 해주는 유일한 방법은 박싱된 프로토콜 타입을 사용하는 것이다.

박싱된 값의 실제 타입을 알고 있다면 `as` 캐스팅을 사용할 수 있다. 예를 들어:

```swift
if let downcastTriangle = vertical.shapes[0] as? Triangle {
    print(downcastTriangle.size)
}
// Prints "5"
```

더 많은 정보는 <doc:TypeCasting#Downcasting>을 참조하라.


## 불투명 타입과 박스형 프로토콜 타입의 차이

함수의 반환 타입으로 불투명 타입을 사용하는 것과 박스형 프로토콜 타입을 사용하는 것은 겉보기에는 매우 유사하다. 하지만 이 두 반환 타입은 타입 정체성을 보존하는지 여부에서 차이가 있다. 불투명 타입은 특정한 하나의 타입을 가리키지만, 함수를 호출하는 쪽에서는 어떤 타입인지 알 수 없다. 반면 박스형 프로토콜 타입은 프로토콜을 준수하는 어떤 타입이든 가리킬 수 있다. 일반적으로 박스형 프로토콜 타입은 저장하는 값의 실제 타입에 대해 더 많은 유연성을 제공하고, 불투명 타입은 그 실제 타입에 대해 더 강력한 보장을 제공한다.

예를 들어, `flip(_:)` 함수의 박스형 프로토콜 타입을 반환 타입으로 사용한 버전은 다음과 같다:

```swift
func protoFlip<T: Shape>(_ shape: T) -> Shape {
    return FlippedShape(shape: shape)
}
```

이 `protoFlip(_:)` 버전은 `flip(_:)`과 동일한 본문을 가지고 있으며, 항상 동일한 타입의 값을 반환한다. 하지만 `flip(_:)`과 달리 `protoFlip(_:)`이 반환하는 값은 항상 동일한 타입일 필요가 없다. 단지 `Shape` 프로토콜을 준수하기만 하면 된다. 즉, `protoFlip(_:)`은 `flip(_:)`보다 호출자와 더 느슨한 API 계약을 맺는다. 이 함수는 여러 타입의 값을 반환할 수 있는 유연성을 보유한다:

```swift
func protoFlip<T: Shape>(_ shape: T) -> Shape {
    if shape is Square {
        return shape
    }

    return FlippedShape(shape: shape)
}
```

이 수정된 버전은 전달된 `shape`에 따라 `Square` 인스턴스 또는 `FlippedShape` 인스턴스를 반환한다. 이 함수가 반환하는 두 개의 뒤집힌 도형은 완전히 다른 타입일 수 있다. 같은 도형의 여러 인스턴스를 뒤집을 때 다른 타입의 값을 반환하는 것도 가능하다. `protoFlip(_:)`의 덜 구체적인 반환 타입 정보는 반환된 값에 대해 타입 정보에 의존하는 많은 연산을 사용할 수 없음을 의미한다. 예를 들어, 이 함수가 반환한 결과를 비교하는 `==` 연산자를 작성할 수 없다.

```swift
let protoFlippedTriangle = protoFlip(smallTriangle)
let sameThing = protoFlip(smallTriangle)
protoFlippedTriangle == sameThing  // Error
```

예제의 마지막 줄에서 발생한 오류에는 여러 가지 이유가 있다. 가장 직접적인 문제는 `Shape` 프로토콜에 `==` 연산자가 요구 사항으로 포함되어 있지 않다는 점이다. 이를 추가하려고 해도, `==` 연산자는 좌변과 우변의 인자 타입을 알아야 한다. 이런 종류의 연산자는 일반적으로 프로토콜을 채택한 구체적인 타입과 일치하는 `Self` 타입의 인자를 받지만, 프로토콜에 `Self` 요구 사항을 추가하면 프로토콜을 타입으로 사용할 때 발생하는 타입 소거를 허용하지 않는다.

함수의 반환 타입으로 박스형 프로토콜 타입을 사용하면 프로토콜을 준수하는 어떤 타입이든 반환할 수 있는 유연성을 얻을 수 있다. 하지만 이 유연성의 대가는 반환된 값에 대해 일부 연산을 수행할 수 없다는 점이다. 예제는 `==` 연산자를 사용할 수 없는 것을 보여준다. 이 연산자는 박스형 프로토콜 타입을 사용할 때 보존되지 않는 특정 타입 정보에 의존한다.

이 접근 방식의 또 다른 문제는 도형 변환이 중첩되지 않는다는 점이다. 삼각형을 뒤집은 결과는 `Shape` 타입의 값이고, `protoFlip(_:)` 함수는 `Shape` 프로토콜을 준수하는 어떤 타입의 인자를 받는다. 하지만 박스형 프로토콜 타입의 값은 그 프로토콜을 준수하지 않는다. 즉, `protoFlip(_:)`이 반환한 값은 `Shape`을 준수하지 않는다. 따라서 `protoFlip(protoFlip(smallTriangle))`과 같이 여러 변환을 적용하는 코드는 유효하지 않다. 뒤집힌 도형은 `protoFlip(_:)`의 유효한 인자가 아니기 때문이다.

반면, 불투명 타입은 실제 타입의 정체성을 보존한다. Swift는 연관 타입을 추론할 수 있으므로, 박스형 프로토콜 타입을 반환 값으로 사용할 수 없는 곳에서도 불투명 반환 값을 사용할 수 있다. 예를 들어, <doc:Generics>의 `Container` 프로토콜 버전은 다음과 같다:

```swift
protocol Container {
    associatedtype Item
    var count: Int { get }
    subscript(i: Int) -> Item { get }
}
extension Array: Container { }
```

연관 타입이 있는 프로토콜은 함수의 반환 타입으로 사용할 수 없다. 또한 제네릭 반환 타입의 제약으로 사용할 수도 없다. 함수 본문 외부에는 제네릭 타입이 무엇인지 추론하기에 충분한 정보가 없기 때문이다.

```swift
// Error: Protocol with associated types can't be used as a return type.
func makeProtocolContainer<T>(item: T) -> Container {
    return [item]
}

// Error: Not enough information to infer C.
func makeProtocolContainer<T, C: Container>(item: T) -> C {
    return [item]
}
```

불투명 타입 `some Container`를 반환 타입으로 사용하면 원하는 API 계약을 표현할 수 있다. 이 함수는 컨테이너를 반환하지만 컨테이너의 타입은 지정하지 않는다:

```swift
func makeOpaqueContainer<T>(item: T) -> some Container {
    return [item]
}
let opaqueContainer = makeOpaqueContainer(item: 12)
let twelve = opaqueContainer[0]
print(type(of: twelve))
// Prints "Int"
```

`twelve`의 타입은 `Int`로 추론된다. 이는 불투명 타입에서도 타입 추론이 작동한다는 사실을 보여준다. `makeOpaqueContainer(item:)`의 구현에서 불투명 컨테이너의 실제 타입은 `[T]`이다. 이 경우 `T`는 `Int`이므로 반환 값은 정수 배열이고, `Item` 연관 타입은 `Int`로 추론된다. `Container`의 서브스크립트는 `Item`을 반환하므로, `twelve`의 타입도 `Int`로 추론된다.


## 불투명 파라미터 타입

`some` 키워드를 사용해 불투명 타입을 반환하는 것 외에도, 함수, 서브스크립트, 또는 이니셜라이저의 파라미터 타입에 `some`을 사용할 수 있다. 하지만 파라미터 타입에서 `some`을 사용하는 것은 불투명 타입이 아닌 제네릭을 위한 짧은 구문일 뿐이다. 예를 들어, 아래 두 함수는 동일하다:

```swift
func drawTwiceGeneric<SomeShape: Shape>(_ shape: SomeShape) -> String {
    let drawn = shape.draw()
    return drawn + "\n" + drawn
}

func drawTwiceSome(_ shape: some Shape) -> String {
    let drawn = shape.draw()
    return drawn + "\n" + drawn
}
```

`drawTwiceGeneric(_:)` 함수는 `SomeShape`라는 이름의 제네릭 타입 파라미터를 선언하며, `SomeShape`가 `Shape` 프로토콜을 준수하도록 제약을 설정한다. `drawTwiceSome(_:)` 함수는 인자 타입으로 `some Shape`를 사용한다. 이는 `Shape` 프로토콜을 준수해야 하는 새로운 이름 없는 제네릭 타입 파라미터를 생성한다. 제네릭 타입에 이름이 없기 때문에 함수 내 다른 곳에서 이 타입을 참조할 수 없다.

여러 파라미터 타입 앞에 `some`을 사용하면, 각 제네릭 타입은 독립적이다. 예를 들어:

```swift
func combine(shape s1: some Shape, with s2: some Shape) -> String {
    return s1.draw() + "\n" + s2.draw()
}

combine(smallTriangle, trapezoid)
```

`combine(shape:with:)` 함수에서 첫 번째와 두 번째 파라미터의 타입은 모두 `Shape` 프로토콜을 준수해야 하지만, 동일한 타입일 필요는 없다. `combine(shape:with:)`를 호출할 때 두 가지 다른 도형을 전달할 수 있다. 이 경우 한 개의 삼각형과 한 개의 사다리꼴을 전달한다.

<doc:Generics> 장에서 설명한 이름 있는 제네릭 타입 파라미터 구문과 달리, 이 간단한 구문은 제네릭 `where` 절이나 동일 타입 (`==`) 제약을 포함할 수 없다. 또한, 매우 복잡한 제약에 이 간단한 구문을 사용하면 가독성이 떨어질 수 있다.

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


