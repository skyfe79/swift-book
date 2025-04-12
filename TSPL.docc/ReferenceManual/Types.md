# 타입

Swift에서 타입은 크게 두 가지로 나뉜다: 이름 있는 타입(named type)과 복합 타입(compound type).  
*이름 있는 타입*은 정의할 때 특정 이름을 부여할 수 있는 타입을 말한다. 클래스, 구조체, 열거형, 프로토콜이 여기에 속한다. 예를 들어, 사용자가 정의한 `MyClass`라는 클래스의 인스턴스는 `MyClass` 타입을 가진다. 사용자가 정의한 이름 있는 타입 외에도, Swift 표준 라이브러리는 배열, 딕셔너리, 옵셔널 값 등을 표현하는 여러 이름 있는 타입을 제공한다.

다른 언어에서 기본형(primitive type)으로 여겨지는 타입들(예: 숫자, 문자, 문자열을 표현하는 타입)도 Swift에서는 이름 있는 타입이다. 이들은 Swift 표준 라이브러리에서 구조체로 정의되고 구현된다. 이름 있는 타입이기 때문에, 프로그램의 필요에 맞게 동작을 확장할 수 있다. 확장 방법은 <doc:Extensions>와 <doc:Declarations#Extension-Declaration>에서 자세히 다룬다.

*복합 타입*은 이름이 없는 타입으로, Swift 언어 자체에서 정의된다. 복합 타입에는 함수 타입과 튜플 타입이 있다. 복합 타입은 이름 있는 타입과 다른 복합 타입을 포함할 수 있다. 예를 들어, 튜플 타입 `(Int, (Int, Int))`은 두 요소를 포함한다: 첫 번째는 이름 있는 타입 `Int`, 두 번째는 또 다른 복합 타입 `(Int, Int)`.

이름 있는 타입이나 복합 타입 주위에 괄호를 추가할 수 있다. 하지만 타입에 괄호를 추가해도 아무런 효과가 없다. 예를 들어, `(Int)`는 `Int`와 동일하다.

이 장에서는 Swift 언어 자체에서 정의된 타입을 설명하고, Swift의 타입 추론 동작에 대해 알아본다.

> 타입 문법:
>
> *type* → *function-type* \
> *type* → *array-type* \
> *type* → *dictionary-type* \
> *type* → *type-identifier* \
> *type* → *tuple-type* \
> *type* → *optional-type* \
> *type* → *implicitly-unwrapped-optional-type* \
> *type* → *protocol-composition-type* \
> *type* → *opaque-type* \
> *type* → *boxed-protocol-type* \
> *type* → *metatype-type* \
> *type* → *any-type* \
> *type* → *self-type* \
> *type* → **`(`** *type* **`)`**


## 타입 어노테이션

*타입 어노테이션*은 변수나 표현식의 타입을 명시적으로 지정한다.  
타입 어노테이션은 콜론(`:`)으로 시작하고 타입으로 끝난다.  
다음 예제를 통해 확인할 수 있다:

```swift
let someTuple: (Double, Double) = (3.14159, 2.71828)
func someFunction(a: Int) { /* ... */ }
```

<!--
  - test: `type-annotation`

  ```swifttest
  -> let someTuple: (Double, Double) = (3.14159, 2.71828)
  -> func someFunction(a: Int) { /* ... */ }
  ```
-->

첫 번째 예제에서 `someTuple` 표현식은 튜플 타입 `(Double, Double)`으로 지정된다.  
두 번째 예제에서는 함수 `someFunction`의 매개변수 `a`가 `Int` 타입으로 지정된다.

타입 어노테이션은 타입 앞에 선택적인 타입 속성 목록을 포함할 수 있다.

> 타입 어노테이션 문법:
>
> *type-annotation* → **`:`** *attributes*_?_ *type*


## 타입 식별자

*타입 식별자*는 이름이 있는 타입이나, 이름이 있거나 복합 타입의 타입 별칭을 가리킨다.

대부분의 경우, 타입 식별자는 해당 식별자와 동일한 이름을 가진 이름이 있는 타입을 직접 참조한다. 예를 들어, `Int`는 이름이 있는 타입 `Int`를 직접 참조하는 타입 식별자이며, `Dictionary<String, Int>`는 이름이 있는 타입 `Dictionary<String, Int>`를 직접 참조하는 타입 식별자이다.

타입 식별자가 동일한 이름의 타입을 참조하지 않는 두 가지 경우가 있다. 첫 번째 경우는 타입 식별자가 이름이 있거나 복합 타입의 타입 별칭을 참조하는 경우이다. 예를 들어, 아래 예제에서 타입 주석에 사용된 `Point`는 튜플 타입 `(Int, Int)`를 참조한다.

```swift
typealias Point = (Int, Int)
let origin: Point = (0, 0)
```

<!--
  - test: `type-identifier`

  ```swifttest
  -> typealias Point = (Int, Int)
  -> let origin: Point = (0, 0)
  ```
-->

두 번째 경우는 타입 식별자가 점(`.`) 문법을 사용해 다른 모듈에 선언된 이름이 있는 타입이나 다른 타입 내에 중첩된 타입을 참조하는 경우이다. 예를 들어, 다음 코드에서 타입 식별자는 `ExampleModule` 모듈에 선언된 이름이 있는 타입 `MyType`을 참조한다.

```swift
var someValue: ExampleModule.MyType
```

<!--
  - test: `type-identifier-dot`

  ```swifttest
  -> var someValue: ExampleModule.MyType
  !$ error: cannot find type 'ExampleModule' in scope
  !! var someValue: ExampleModule.MyType
  !!                ^~~~~~~~~~~~~
  ```
-->

> 타입 식별자의 문법:
>
> *type-identifier* → *type-name* *generic-argument-clause*_?_ | *type-name* *generic-argument-clause*_?_ **`.`** *type-identifier* \
> *type-name* → *identifier*


## 튜플 타입

튜플 타입은 괄호로 둘러싸인 쉼표로 구분된 타입 목록이다. 

함수의 반환 타입으로 튜플 타입을 사용하면 여러 값을 포함한 단일 튜플을 반환할 수 있다. 또한 튜플 타입의 각 요소에 이름을 붙이고, 그 이름을 통해 개별 요소의 값을 참조할 수 있다. 요소 이름은 식별자와 바로 뒤에 오는 콜론(:)으로 구성된다. 이러한 기능을 보여주는 예제는 <doc:Functions#Functions-with-Multiple-Return-Values>를 참고한다.

튜플 타입의 요소에 이름이 붙으면, 그 이름은 타입의 일부가 된다.

```swift
var someTuple = (top: 10, bottom: 12)  // someTuple의 타입은 (top: Int, bottom: Int)
someTuple = (top: 4, bottom: 42) // OK: 이름이 일치함
someTuple = (9, 99)              // OK: 이름이 추론됨
someTuple = (left: 5, right: 5)  // Error: 이름이 일치하지 않음
```

<!--
  - test: `tuple-type-names`

  ```swifttest
  -> var someTuple = (top: 10, bottom: 12)  // someTuple is of type (top: Int, bottom: Int)
  -> someTuple = (top: 4, bottom: 42) // OK: names match
  -> someTuple = (9, 99)              // OK: names are inferred
  -> someTuple = (left: 5, right: 5)  // Error: names don't match
  !$ error: cannot assign value of type '(left: Int, right: Int)' to type '(top: Int, bottom: Int)'
  !! someTuple = (left: 5, right: 5)  // Error: names don't match
  !!             ^~~~~~~~~~~~~~~~~~~
  ```
-->

모든 튜플 타입은 두 개 이상의 타입을 포함한다. 단, `Void`는 빈 튜플 타입인 `()`의 별칭이다.

> 튜플 타입 문법:
>
> *tuple-type* → **`(`** **`)`** | **`(`** *tuple-type-element* **`,`** *tuple-type-element-list* **`)`** \
> *tuple-type-element-list* → *tuple-type-element* | *tuple-type-element* **`,`** *tuple-type-element-list* \
> *tuple-type-element* → *element-name* *type-annotation* | *type* \
> *element-name* → *identifier*


## 함수 타입

*함수 타입*은 함수, 메서드, 클로저의 타입을 나타낸다. 함수 타입은 화살표(`->`)로 구분된 매개변수 타입과 반환 타입으로 구성된다:

```swift
(<#매개변수 타입#>) -> <#반환 타입#>
```

*매개변수 타입*은 쉼표로 구분된 타입 목록이다. *반환 타입*은 튜플 타입일 수 있으므로, 함수 타입은 여러 값을 반환하는 함수와 메서드를 지원한다.

함수 타입 `() -> T`(여기서 `T`는 임의의 타입)의 매개변수는 `autoclosure` 속성을 적용해 호출 지점에서 암시적으로 클로저를 생성할 수 있다. 이를 통해 명시적 클로저 작성 없이도 표현식의 평가를 지연하는 구문적 편의를 제공한다. `autoclosure` 함수 타입 매개변수의 예제는 <doc:Closures#Autoclosures>를 참고한다.

함수 타입의 *매개변수 타입*에는 가변 인자를 사용할 수 있다. 구문적으로 가변 인자는 기본 타입 이름 뒤에 점 세 개(`...`)를 붙여 표현한다. 예를 들어 `Int...`와 같다. 가변 인자는 기본 타입의 요소를 포함하는 배열로 처리된다. 예를 들어 `Int...`는 `[Int]`로 처리된다. 가변 인자를 사용하는 예제는 <doc:Functions#Variadic-Parameters>를 참고한다.

입출력 매개변수를 지정하려면 매개변수 타입 앞에 `inout` 키워드를 붙인다. 가변 인자나 반환 타입에는 `inout` 키워드를 사용할 수 없다. 입출력 매개변수에 대한 자세한 내용은 <doc:Functions#In-Out-Parameters>에서 다룬다.

함수 타입에 매개변수가 하나뿐이고 그 매개변수의 타입이 튜플 타입이라면, 함수 타입을 작성할 때 튜플 타입을 괄호로 감싸야 한다. 예를 들어 `((Int, Int)) -> Void`는 튜플 타입 `(Int, Int)`의 단일 매개변수를 받고 아무 값도 반환하지 않는 함수의 타입이다. 반면 괄호 없이 `(Int, Int) -> Void`는 두 개의 `Int` 매개변수를 받고 아무 값도 반환하지 않는 함수의 타입이다. 마찬가지로 `Void`는 `()`의 타입 별칭이므로 `(Void) -> Void`는 `(()) -> ()`와 같다. 이는 빈 튜플을 단일 인자로 받는 함수를 의미한다. 이 타입들은 인자를 받지 않는 함수인 `() -> ()`와는 다르다.

함수와 메서드의 인자 이름은 해당 함수 타입의 일부가 아니다. 예를 들어:

```swift
func someFunction(left: Int, right: Int) {}
func anotherFunction(left: Int, right: Int) {}
func functionWithDifferentLabels(top: Int, bottom: Int) {}

var f = someFunction // f의 타입은 (Int, Int) -> Void이며, (left: Int, right: Int) -> Void가 아니다.
f = anotherFunction              // OK
f = functionWithDifferentLabels  // OK

func functionWithDifferentArgumentTypes(left: Int, right: String) {}
f = functionWithDifferentArgumentTypes     // Error

func functionWithDifferentNumberOfArguments(left: Int, right: Int, top: Int) {}
f = functionWithDifferentNumberOfArguments // Error
```

인자 레이블은 함수 타입의 일부가 아니므로, 함수 타입을 작성할 때는 이를 생략한다.

```swift
var operation: (lhs: Int, rhs: Int) -> Int     // Error
var operation: (_ lhs: Int, _ rhs: Int) -> Int // OK
var operation: (Int, Int) -> Int               // OK
```

함수 타입에 화살표(`->`)가 여러 개 포함된 경우, 함수 타입은 오른쪽에서 왼쪽으로 그룹화된다. 예를 들어 `(Int) -> (Int) -> Int`는 `(Int) -> ((Int) -> Int)`로 이해된다. 즉, `Int`를 받아 `Int`를 받고 반환하는 또 다른 함수를 반환하는 함수를 의미한다.

에러를 던지거나 다시 던지는 함수의 함수 타입은 `throws` 키워드를 포함해야 한다. `throws` 뒤에 괄호로 에러 타입을 지정할 수 있다. 던지는 에러 타입은 `Error` 프로토콜을 준수해야 한다. 타입을 지정하지 않고 `throws`만 작성하는 것은 `throws(any Error)`와 같다. `throws`를 생략하는 것은 `throws(Never)`와 같다. 함수가 던지는 에러 타입은 `Error`를 준수하는 모든 타입이 될 수 있으며, 제네릭 타입, 박스형 프로토콜 타입, 불투명 타입을 포함한다.

함수가 던지는 에러 타입은 해당 함수 타입의 일부이며, 에러 타입 간의 하위 타입 관계는 해당 함수 타입 간의 하위 타입 관계를 의미한다. 예를 들어 커스텀 `MyError` 타입을 선언하면, 일부 함수 타입 간의 관계는 다음과 같이 상위 타입에서 하위 타입 순으로 나열된다:

1. 모든 에러를 던지는 함수, `throws(any Error)`로 표시
1. 특정 에러를 던지는 함수, `throws(MyError)`로 표시
1. 에러를 던지지 않는 함수, `throws(Never)`로 표시

이러한 하위 타입 관계의 결과로:

- 에러를 던지지 않는 함수는 에러를 던지는 함수와 동일한 위치에서 사용할 수 있다.
- 구체적인 에러 타입을 던지는 함수는 에러를 던지는 함수와 동일한 위치에서 사용할 수 있다.
- 더 구체적인 에러 타입을 던지는 함수는 더 일반적인 에러 타입을 던지는 함수와 동일한 위치에서 사용할 수 있다.

함수 타입에서 던지는 에러 타입으로 연관 타입이나 제네릭 타입 매개변수를 사용하면, 해당 연관 타입이나 제네릭 타입 매개변수는 암시적으로 `Error` 프로토콜을 준수해야 한다.

에러를 던지고 다시 던지는 함수에 대한 자세한 내용은 <doc:Declarations#Throwing-Functions-and-Methods>와 <doc:Declarations#Rethrowing-Functions-and-Methods>를 참고한다.

비동기 함수의 함수 타입은 `async` 키워드로 표시해야 한다. `async` 키워드는 함수 타입의 일부이며, 동기 함수는 비동기 함수의 하위 타입이다. 따라서 동기 함수는 비동기 함수와 동일한 위치에서 사용할 수 있다. 비동기 함수에 대한 자세한 내용은 <doc:Declarations#Asynchronous-Functions-and-Methods>를 참고한다.


### 논에스케이핑 클로저의 제약 사항

논에스케이핑 함수 타입의 파라미터는 `Any` 타입의 프로퍼티, 변수, 상수에 저장할 수 없다. 이는 값이 탈출할 가능성을 열어두기 때문이다.

<!--
  - test: `cant-store-nonescaping-as-Any`

  ```swifttest
  -> func f(g: ()->Void) { let x: Any = g }
  !$ error: converting non-escaping value to 'Any' may allow it to escape
  !! func f(g: ()->Void) { let x: Any = g }
  !!                                    ^
  ```
-->

논에스케이핑 함수 타입의 파라미터는 다른 논에스케이핑 함수 파라미터에 인자로 전달할 수 없다. 이 제약은 Swift가 런타임이 아닌 컴파일 타임에 메모리 접근 충돌을 더 많이 검사할 수 있도록 돕는다. 예를 들어:

```swift
let external: (() -> Void) -> Void = { _ in () }
func takesTwoFunctions(first: (() -> Void) -> Void, second: (() -> Void) -> Void) {
    first { first {} }       // 오류
    second { second {}  }    // 오류

    first { second {} }      // 오류
    second { first {} }      // 오류

    first { external {} }    // 정상
    external { first {} }    // 정상
}
```

<!--
  - test: `memory-nonescaping-functions`

  ```swifttest
  -> let external: (() -> Void) -> Void = { _ in () }
  -> func takesTwoFunctions(first: (() -> Void) -> Void, second: (() -> Void) -> Void) {
         first { first {} }       // 오류
         second { second {}  }    // 오류

         first { second {} }      // 오류
         second { first {} }      // 오류

         first { external {} }    // 정상
         external { first {} }    // 정상
     }
  !$ error: passing a closure which captures a non-escaping function parameter 'first' to a call to a non-escaping function parameter can allow re-entrant modification of a variable
  !! first { first {} }       // 오류
  !! ^
  !$ error: passing a closure which captures a non-escaping function parameter 'second' to a call to a non-escaping function parameter can allow re-entrant modification of a variable
  !! second { second {}  }    // 오류
  !! ^
  !$ error: passing a closure which captures a non-escaping function parameter 'second' to a call to a non-escaping function parameter can allow re-entrant modification of a variable
  !! first { second {} }      // 오류
  !! ^
  !$ error: passing a closure which captures a non-escaping function parameter 'first' to a call to a non-escaping function parameter can allow re-entrant modification of a variable
  !! second { first {} }      // 오류
  !! ^
  ```
-->

위 코드에서 `takesTwoFunctions(first:second:)`의 두 파라미터는 모두 함수 타입이다. 두 파라미터 모두 `@escaping`으로 표시되지 않았기 때문에 논에스케이핑 함수로 간주된다.

예제에서 "오류"로 표시된 네 개의 함수 호출은 컴파일 오류를 발생시킨다. `first`와 `second` 파라미터가 논에스케이핑 함수이기 때문에, 이들을 다른 논에스케이핑 함수 파라미터에 인자로 전달할 수 없다. 반면, "정상"으로 표시된 두 함수 호출은 컴파일 오류를 발생시키지 않는다. 이 함수 호출들은 `external`이 `takesTwoFunctions(first:second:)`의 파라미터가 아니기 때문에 제약을 위반하지 않는다.

이 제약을 피하려면 파라미터 중 하나를 에스케이핑으로 표시하거나, `withoutActuallyEscaping(_:do:)` 함수를 사용해 논에스케이핑 함수 파라미터를 일시적으로 에스케이핑 함수로 변환하면 된다. 메모리 접근 충돌을 피하는 방법에 대한 자세한 내용은 <doc:MemorySafety>를 참고한다.

> 함수 타입의 문법:
>
> *function-type* → *attributes*_?_ *function-type-argument-clause* **`async`**_?_ *throws-clause*_?_ **`->`** *type*
>
> *function-type-argument-clause* → **`(`** **`)`** \
> *function-type-argument-clause* → **`(`** *function-type-argument-list* **`...`**_?_ **`)`**
>
> *function-type-argument-list* → *function-type-argument* | *function-type-argument**`,`** *function-type-argument-list* \
> *function-type-argument* → *attributes*_?_ *parameter-modifier*_?_ *type* | *argument-label* *type-annotation* \
> *argument-label* → *identifier*
>
> *throws-clause* → **`throws`** | **`throws`** **`(`** *type* **`)`**

<!--
  NOTE: Functions are first-class citizens in Swift,
  except for generic functions, i.e., parametric polymorphic functions.
  This means that monomorphic functions can be assigned to variables
  and can be passed as arguments to other functions.
  As an example, the following three lines of code are OK::

      func polymorphicF<T>(a: Int) -> T { return a }
      func monomorphicF(a: Int) -> Int { return a }
      var myMonomorphicF = monomorphicF

  But, the following is NOT allowed::

      var myPolymorphicF = polymorphicF
-->


## 배열 타입

Swift 언어는 Swift 표준 라이브러리의 `Array<Element>` 타입에 대해 다음과 같은 문법적 편의를 제공한다:

```swift
[<#타입#>]
```

즉, 다음 두 선언은 동일하다:

```swift
let someArray: Array<String> = ["Alex", "Brian", "Dave"]
let someArray: [String] = ["Alex", "Brian", "Dave"]
```

<!--
  - test: `array-literal`

  ```swifttest
  >> let someArray1: Array<String> = ["Alex", "Brian", "Dave"]
  >> let someArray2: [String] = ["Alex", "Brian", "Dave"]
  >> assert(someArray1 == someArray2)
  ```
-->

두 경우 모두 상수 `someArray`는 문자열 배열로 선언된다. 배열의 엘리먼트는 대괄호 안에 유효한 인덱스 값을 지정하여 접근할 수 있다. 예를 들어 `someArray[0]`은 인덱스 0에 위치한 `"Alex"`를 참조한다.

다차원 배열을 만들려면 대괄호 쌍을 중첩하면 된다. 이때 엘리먼트의 기본 타입 이름은 가장 안쪽의 대괄호 쌍에 위치한다. 예를 들어, 세 개의 대괄호 쌍을 사용해 3차원 정수 배열을 만들 수 있다:

```swift
var array3D: [[[Int]]] = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
```

<!--
  - test: `array-3d`

  ```swifttest
  -> var array3D: [[[Int]]] = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
  ```
-->

다차원 배열의 엘리먼트에 접근할 때, 가장 왼쪽의 인덱스는 가장 바깥쪽 배열의 해당 인덱스에 위치한 엘리먼트를 참조한다. 그 다음 오른쪽의 인덱스는 한 단계 안쪽에 중첩된 배열의 해당 인덱스 엘리먼트를 참조한다. 이와 같은 방식으로 계속 진행된다. 위 예제에서 `array3D[0]`은 `[[1, 2], [3, 4]]`를, `array3D[0][1]`은 `[3, 4]`를, `array3D[0][1][1]`은 값 4를 참조한다.

Swift 표준 라이브러리 `Array` 타입에 대한 자세한 내용은 <doc:CollectionTypes#Arrays>를 참고한다.

> 배열 타입 문법:
>
> *array-type* → **`[`** *타입* **`]`**


## 딕셔너리 타입

Swift 언어는 Swift 표준 라이브러리의 `Dictionary<Key, Value>` 타입에 대해 다음과 같은 문법적 설탕을 제공한다:

```swift
[<#키 타입#>: <#값 타입#>]
```

즉, 다음 두 선언은 동일하다:

```swift
let someDictionary: [String: Int] = ["Alex": 31, "Paul": 39]
let someDictionary: Dictionary<String, Int> = ["Alex": 31, "Paul": 39]
```

<!--
  - test: `dictionary-literal`

  ```swifttest
  >> let someDictionary1: [String: Int] = ["Alex": 31, "Paul": 39]
  >> let someDictionary2: Dictionary<String, Int> = ["Alex": 31, "Paul": 39]
  >> assert(someDictionary1 == someDictionary2)
  ```
-->

두 경우 모두, 상수 `someDictionary`는 문자열을 키로, 정수를 값으로 가지는 딕셔너리로 선언된다.

딕셔너리의 값은 대괄호 안에 해당 키를 지정해 접근할 수 있다. 예를 들어 `someDictionary["Alex"]`는 키 `"Alex"`와 연결된 값을 가리킨다. 서브스크립트는 딕셔너리의 값 타입의 옵셔널 값을 반환한다. 지정된 키가 딕셔너리에 없으면 서브스크립트는 `nil`을 반환한다.

딕셔너리의 키 타입은 Swift 표준 라이브러리의 `Hashable` 프로토콜을 준수해야 한다.

<!--
  Used to have an xref to :ref:`CollectionTypes_HashValuesForSetTypes` here.
  But it doesn't really work now that the Hashable content moved from Dictionary to Set.
-->

Swift 표준 라이브러리의 `Dictionary` 타입에 대한 자세한 설명은 <doc:CollectionTypes#Dictionaries>를 참조한다.

> 딕셔너리 타입 문법:
>
> *dictionary-type* → **`[`** *type* **`:`** *type* **`]`**


## 옵셔널 타입

Swift 언어에서는 `?` 접미사를 `Optional<Wrapped>` 타입에 대한 문법적 설탕(syntactic sugar)으로 정의한다. 이 타입은 Swift 표준 라이브러리에 정의되어 있다. 즉, 아래 두 선언은 동일한 의미를 가진다:

```swift
var optionalInteger: Int?
var optionalInteger: Optional<Int>
```

<!--
  - test: `optional-literal`

  ```swifttest
  >> var optionalInteger1: Int?
  >> var optionalInteger2: Optional<Int>
  ```
-->

<!--
  위 코드 목록은 optionalInteger의 재선언으로 인해 테스트할 수 없으므로,
  적어도 표시된 문법이 컴파일되는지 확인한다.
-->

두 경우 모두, `optionalInteger` 변수는 옵셔널 정수 타입으로 선언된다. 타입과 `?` 사이에 공백이 없어야 한다는 점에 유의한다.

`Optional<Wrapped>` 타입은 두 가지 케이스(`none`과 `some(Wrapped)`)를 가진 열거형이다. 이 타입은 값이 존재할 수도 있고 없을 수도 있는 상황을 표현한다. 모든 타입은 명시적으로 옵셔널 타입으로 선언하거나 암시적으로 변환할 수 있다. 옵셔널 변수나 프로퍼티를 선언할 때 초기값을 제공하지 않으면, 자동으로 `nil`로 초기화된다.

<!--
  TODO Optional Enum Reference 페이지로 링크 추가.
  옵셔널 타입에 대한 더 많은 정보는 ...을 참조한다.
-->

옵셔널 타입의 인스턴스가 값을 포함하고 있다면, 아래와 같이 `!` 접미사 연산자를 사용해 그 값에 접근할 수 있다:

```swift
optionalInteger = 42
optionalInteger! // 42
```

<!--
  - test: `optional-type`

  ```swifttest
  >> var optionalInteger: Int?
  -> optionalInteger = 42
  >> let r0 =
  -> optionalInteger! // 42
  >> assert(r0 == 42)
  ```
-->

<!--
  가능하다면 위 코드를 리팩토링해 bare expression 사용을 피한다.
  추적 중인 버그는 <rdar://problem/35301593>
-->

값이 `nil`인 옵셔널에 `!` 연산자를 사용하면 런타임 오류가 발생한다.

옵셔널 체이닝과 옵셔널 바인딩을 사용해 옵셔널 표현식에 조건부로 연산을 수행할 수도 있다. 값이 `nil`인 경우, 연산이 수행되지 않으므로 런타임 오류가 발생하지 않는다.

옵셔널 타입 사용법에 대한 더 많은 정보와 예제는 <doc:TheBasics#Optionals>를 참조한다.

> 옵셔널 타입의 문법:
>
> *optional-type* → *type* **`?`**


## 암시적 옵셔널 언래핑 타입

Swift 언어에서 `!` 접미사는 Swift 표준 라이브러리에 정의된 `Optional<Wrapped>` 타입에 대한 문법적 편의 기능이다. 이 타입은 접근 시 자동으로 언래핑되는 추가 동작을 가진다. 만약 값이 `nil`인 암시적 옵셔널을 사용하려고 하면 런타임 오류가 발생한다. 암시적 언래핑 동작을 제외하면, 아래 두 선언은 동일하다:

```swift
var implicitlyUnwrappedString: String!
var explicitlyUnwrappedString: Optional<String>
```

타입과 `!` 사이에 공백이 없어야 한다는 점에 유의한다.

암시적 언래핑은 해당 타입을 포함하는 선언의 의미를 변경한다. 따라서 튜플 타입이나 제네릭 타입 내부에 중첩된 옵셔널 타입(예: 딕셔너리나 배열의 요소 타입)은 암시적 언래핑으로 표시할 수 없다. 예를 들어:

```swift
let tupleOfImplicitlyUnwrappedElements: (Int!, Int!)  // 오류
let implicitlyUnwrappedTuple: (Int, Int)!             // 정상

let arrayOfImplicitlyUnwrappedElements: [Int!]        // 오류
let implicitlyUnwrappedArray: [Int]!                  // 정상
```

암시적 옵셔널은 일반 옵셔널 값과 동일한 `Optional<Wrapped>` 타입을 가지기 때문에, 코드 내에서 옵셔널을 사용할 수 있는 모든 곳에서 암시적 옵셔널을 사용할 수 있다. 예를 들어, 암시적 옵셔널 값을 옵셔널 변수, 상수, 프로퍼티에 할당할 수 있고, 그 반대도 가능하다.

옵셔널과 마찬가지로, 암시적 옵셔널 변수나 프로퍼티를 선언할 때 초기값을 제공하지 않으면 자동으로 `nil`로 초기화된다.

옵셔널 체이닝을 사용해 암시적 옵셔널 표현식에 대한 작업을 조건적으로 수행할 수 있다. 값이 `nil`인 경우, 작업이 수행되지 않으므로 런타임 오류가 발생하지 않는다.

암시적 옵셔널 타입에 대한 더 자세한 정보는 <doc:TheBasics#Implicitly-Unwrapped-Optionals>를 참고한다.

> 암시적 옵셔널 타입 문법:
>
> *implicitly-unwrapped-optional-type* → *type* **`!`**


## 프로토콜 합성 타입

*프로토콜 합성 타입*은 지정된 프로토콜 목록의 각 프로토콜을 준수하는 타입을 정의한다. 또는 주어진 클래스의 서브클래스이면서 지정된 프로토콜 목록의 각 프로토콜을 준수하는 타입을 정의한다. 프로토콜 합성 타입은 타입 어노테이션, 제네릭 매개변수 절, 그리고 제네릭 `where` 절에서 타입을 지정할 때만 사용할 수 있다.

<!--
  타입을 쉼표로 구분하여 나열할 수 있는 곳에서는 P&Q 구문을 사용할 수 없다.
-->

프로토콜 합성 타입은 다음과 같은 형태를 가진다:

```swift
<#Protocol 1#> & <#Protocol 2#>
```

프로토콜 합성 타입을 사용하면 여러 프로토콜의 요구 사항을 준수하는 타입의 값을 지정할 수 있다. 이때 새로운 이름을 가진 프로토콜을 명시적으로 정의할 필요가 없다. 예를 들어, `ProtocolA`, `ProtocolB`, `ProtocolC`를 상속받는 새로운 프로토콜을 선언하는 대신 `ProtocolA & ProtocolB & ProtocolC`와 같은 프로토콜 합성 타입을 사용할 수 있다. 마찬가지로, `SuperClass`의 서브클래스이면서 `ProtocolA`를 준수하는 새로운 프로토콜을 선언하는 대신 `SuperClass & ProtocolA`를 사용할 수 있다.

프로토콜 합성 목록의 각 항목은 다음 중 하나이며, 목록에는 최대 하나의 클래스만 포함될 수 있다:

- 클래스의 이름
- 프로토콜의 이름
- 프로토콜 합성 타입, 프로토콜, 또는 클래스를 기본 타입으로 하는 타입 별칭

프로토콜 합성 타입에 타입 별칭이 포함된 경우, 동일한 프로토콜이 정의에서 여러 번 나타날 수 있다. 이때 중복된 항목은 무시된다. 예를 들어, 아래 코드에서 `PQR`의 정의는 `P & Q & R`과 동일하다.

```swift
typealias PQ = P & Q
typealias PQR = PQ & Q & R
```

<!--
  - test: `protocol-composition-can-have-repeats`

  ```swifttest
  >> protocol P {}
  >> protocol Q {}
  >> protocol R {}
  -> typealias PQ = P & Q
  -> typealias PQR = PQ & Q & R
  ```
-->

> 프로토콜 합성 타입의 문법:
>
> *protocol-composition-type* → *type-identifier* **`&`** *protocol-composition-continuation* \
> *protocol-composition-continuation* → *type-identifier* | *protocol-composition-type*


## 불투명 타입

*불투명 타입*은 구체적인 타입을 명시하지 않고, 프로토콜 또는 프로토콜 합성을 준수하는 타입을 정의한다.

불투명 타입은 함수나 서브스크립트의 반환 타입, 함수, 서브스크립트, 또는 이니셜라이저의 파라미터 타입, 또는 프로퍼티의 타입으로 사용된다. 불투명 타입은 튜플 타입이나 제네릭 타입의 일부로는 사용할 수 없다. 예를 들어, 배열의 요소 타입이나 옵셔널의 래핑 타입으로는 사용할 수 없다.

불투명 타입은 다음과 같은 형태를 가진다:

```swift
some <#constraint#>
```

여기서 *constraint*는 클래스 타입, 프로토콜 타입, 프로토콜 합성 타입, 또는 `Any`가 될 수 있다. 값은 불투명 타입의 인스턴스로 사용될 수 있는데, 이 값은 나열된 프로토콜 또는 프로토콜 합성을 준수하거나, 나열된 클래스를 상속받는 타입의 인스턴스여야 한다. 불투명 값과 상호작용하는 코드는 *constraint*에 의해 정의된 인터페이스의 일부인 방식으로만 값을 사용할 수 있다.

컴파일 시점에 불투명 타입의 값은 특정한 구체적인 타입을 가지며, Swift는 이 타입을 최적화에 사용할 수 있다. 그러나 불투명 타입은 구체적인 타입에 대한 정보가 넘어갈 수 없는 경계를 형성한다.

프로토콜 선언에는 불투명 타입을 포함할 수 없다. 클래스는 nonfinal 메서드의 반환 타입으로 불투명 타입을 사용할 수 없다.

불투명 타입을 반환 타입으로 사용하는 함수는 동일한 구체적인 타입을 공유하는 값을 반환해야 한다. 반환 타입은 함수의 제네릭 타입 파라미터의 일부인 타입을 포함할 수 있다. 예를 들어, `someFunction<T>()`라는 함수는 `T` 타입이나 `Dictionary<String, T>` 타입의 값을 반환할 수 있다.

파라미터에 대한 불투명 타입을 작성하는 것은 제네릭 타입을 사용하는 것과 동일하지만, 제네릭 타입 파라미터의 이름을 지정하지 않는다. 암시적인 제네릭 타입 파라미터는 불투명 타입에 명시된 프로토콜을 준수해야 한다는 제약을 가진다. 여러 불투명 타입을 작성하면, 각각은 자체적인 제네릭 타입 파라미터를 만든다. 예를 들어, 다음 두 선언은 동일하다:

```swift
func someFunction(x: some MyProtocol, y: some MyProtocol) { }
func someFunction<T1: MyProtocol, T2: MyProtocol>(x: T1, y: T2) { }
```

두 번째 선언에서 제네릭 타입 파라미터 `T1`과 `T2`는 이름을 가지므로, 코드의 다른 부분에서 이 타입들을 참조할 수 있다. 반면, 첫 번째 선언의 제네릭 타입 파라미터는 이름이 없으며 다른 코드에서 참조할 수 없다.

가변 인자 파라미터의 타입으로는 불투명 타입을 사용할 수 없다.

반환되는 함수 타입의 파라미터로, 또는 파라미터 타입이 함수 타입인 경우의 파라미터로 불투명 타입을 사용할 수 없다. 이러한 위치에서는 함수의 호출자가 알 수 없는 타입의 값을 생성해야 하기 때문이다.

```swift
protocol MyProtocol { }
func badFunction() -> (some MyProtocol) -> Void { }  // 에러
func anotherBadFunction(callback: (some MyProtocol) -> Void) { }  // 에러
```

> 불투명 타입의 문법:
>
> *opaque-type* → **`some`** *type*


## 박싱된 프로토콜 타입

*박싱된 프로토콜 타입*은 프로토콜 또는 프로토콜 합성을 준수하는 타입을 정의한다. 이 타입은 프로그램이 실행되는 동안 준수하는 타입이 변할 수 있는 특징을 가진다.

박싱된 프로토콜 타입은 다음과 같은 형태를 가진다:

```swift
any <#constraint#>
```

여기서 *constraint*는 프로토콜 타입, 프로토콜 합성 타입, 프로토콜 타입의 메타타입, 또는 프로토콜 합성 타입의 메타타입이다.

런타임에 박싱된 프로토콜 타입의 인스턴스는 *constraint*를 만족하는 어떤 타입의 값이라도 포함할 수 있다. 이 동작은 컴파일 타임에 특정 준수 타입이 알려지는 불투명 타입과는 대조적이다. 박싱된 프로토콜 타입을 다룰 때 사용되는 추가적인 간접 참조를 *박싱*이라고 한다. 박싱은 일반적으로 별도의 메모리 할당과 접근을 위한 추가적인 간접 참조를 필요로 하며, 이는 런타임에 성능 비용을 발생시킨다.

`Any` 또는 `AnyObject` 타입에 `any`를 적용해도 아무런 효과가 없다. 이 타입들은 이미 박싱된 프로토콜 타입이기 때문이다.

<!--
  - test: `any-any-does-nothing`

   >> var x: any Any = 12
   >> var y: Any = 12
   >> print(type(of: x))
   << Int
   >> print(type(of: y))
   << Int
   >> print(type(of: x) == type(of: y))
   << true
-->

<!--
  - test: `any-anyobject-does-nothing`

   >> import Foundation
   >> var x: any AnyObject = NSNumber(value: 12)
   >> var y: AnyObject = NSNumber(value: 12)
   >> print(type(of: x))
   << __NSCFNumber
   >> print(type(of: y))
   << __NSCFNumber
   >> print(type(of: x) == type(of: y))
   << true
-->

<!--
Contrast P.Type with (any P.Type) and (any P).Type
https://github.com/swiftlang/swift-evolution/blob/main/proposals/0335-existential-any.md#metatypes
-->

> 박싱된 프로토콜 타입의 문법:
>
> *boxed-protocol-type* → **`any`** *type*


## 메타타입 타입

*메타타입 타입*은 클래스 타입, 구조체 타입, 열거형 타입, 프로토콜 타입을 포함한 모든 타입의 타입을 말한다.

클래스, 구조체, 또는 열거형 타입의 메타타입은 해당 타입 이름 뒤에 `.Type`을 붙인다. 프로토콜 타입의 메타타입은 해당 프로토콜 이름 뒤에 `.Protocol`을 붙인다. 이때 프로토콜을 준수하는 런타임의 구체적인 타입이 아니라 프로토콜 자체를 의미한다. 예를 들어, 클래스 타입 `SomeClass`의 메타타입은 `SomeClass.Type`이고, 프로토콜 `SomeProtocol`의 메타타입은 `SomeProtocol.Protocol`이다.

`self` 접미사 표현을 사용하면 타입을 값으로 접근할 수 있다. 예를 들어, `SomeClass.self`는 `SomeClass` 자체를 반환하며, `SomeClass`의 인스턴스가 아니다. 마찬가지로 `SomeProtocol.self`는 `SomeProtocol` 자체를 반환하며, 런타임에 해당 프로토콜을 준수하는 타입의 인스턴스가 아니다. `type(of:)` 함수를 사용하면 특정 인스턴스의 동적 런타임 타입을 값으로 접근할 수 있다. 다음 예제를 참고하자:

```swift
class SomeBaseClass {
    class func printClassName() {
        print("SomeBaseClass")
    }
}
class SomeSubClass: SomeBaseClass {
    override class func printClassName() {
        print("SomeSubClass")
    }
}
let someInstance: SomeBaseClass = SomeSubClass()
// someInstance의 컴파일 타임 타입은 SomeBaseClass,
// 런타임 타입은 SomeSubClass
type(of: someInstance).printClassName()
// "SomeSubClass" 출력
```

<!--
  - test: `metatype-type`

  ```swifttest
  -> class SomeBaseClass {
         class func printClassName() {
             print("SomeBaseClass")
         }
     }
  -> class SomeSubClass: SomeBaseClass {
         override class func printClassName() {
             print("SomeSubClass")
         }
     }
  -> let someInstance: SomeBaseClass = SomeSubClass()
  -> // The compile-time type of someInstance is SomeBaseClass,
  -> // and the runtime type of someInstance is SomeSubClass
  -> type(of: someInstance).printClassName()
  <- SomeSubClass
  ```
-->

자세한 내용은 Swift 표준 라이브러리의 [`type(of:)`](https://developer.apple.com/documentation/swift/2885064-type)를 참고하자.

타입의 메타타입 값을 사용해 해당 타입의 인스턴스를 생성하려면 초기화 표현식을 사용한다. 클래스 인스턴스의 경우, 호출되는 초기화 메서드는 `required` 키워드로 표시되어야 하거나, 전체 클래스가 `final` 키워드로 표시되어야 한다.

```swift
class AnotherSubClass: SomeBaseClass {
    let string: String
    required init(string: String) {
        self.string = string
    }
    override class func printClassName() {
        print("AnotherSubClass")
    }
}
let metatype: AnotherSubClass.Type = AnotherSubClass.self
let anotherInstance = metatype.init(string: "some string")
```

<!--
  - test: `metatype-type`

  ```swifttest
  -> class AnotherSubClass: SomeBaseClass {
        let string: String
        required init(string: String) {
           self.string = string
        }
        override class func printClassName() {
           print("AnotherSubClass")
        }
     }
  -> let metatype: AnotherSubClass.Type = AnotherSubClass.self
  -> let anotherInstance = metatype.init(string: "some string")
  ```
-->

> 메타타입 타입의 문법:
>
> *metatype-type* → *type* **`.`** **`Type`** | *type* **`.`** **`Protocol`**


## Any 타입

`Any` 타입은 다른 모든 타입의 값을 포함할 수 있다. `Any`는 다음과 같은 타입의 인스턴스에 대한 구체적인 타입으로 사용할 수 있다:

- 클래스, 구조체, 열거형
- `Int.self`와 같은 메타타입
- 다양한 타입의 구성 요소를 가진 튜플
- 클로저 또는 함수 타입

```swift
let mixed: [Any] = ["one", 2, true, (4, 5.3), { () -> Int in return 6 }]
```

<!--
  - test: `any-type`

  ```swifttest
  -> let mixed: [Any] = ["one", 2, true, (4, 5.3), { () -> Int in return 6 }]
  ```
-->

`Any`를 인스턴스의 구체적인 타입으로 사용할 때는, 해당 인스턴스의 프로퍼티나 메서드에 접근하기 전에 알려진 타입으로 캐스팅해야 한다. `Any` 타입으로 선언된 인스턴스는 원래의 동적 타입을 유지하며, 타입 캐스팅 연산자(`as`, `as?`, `as!`)를 사용해 해당 타입으로 캐스팅할 수 있다. 예를 들어, 이종 타입의 배열에서 첫 번째 객체를 `String`으로 조건부 다운캐스팅하려면 다음과 같이 `as?`를 사용한다:

```swift
if let first = mixed.first as? String {
    print("The first item, '\(first)', is a string.")
}
// Prints "The first item, 'one', is a string."
```

<!--
  - test: `any-type`

  ```swifttest
  -> if let first = mixed.first as? String {
         print("The first item, '\(first)', is a string.")
     }
  <- The first item, 'one', is a string.
  ```
-->

캐스팅에 대한 더 자세한 정보는 <doc:TypeCasting>을 참고한다.

`AnyObject` 프로토콜은 `Any` 타입과 유사하다. 모든 클래스는 암시적으로 `AnyObject`를 준수한다. `Any`가 언어 자체에 의해 정의되는 것과 달리, `AnyObject`는 Swift 표준 라이브러리에 의해 정의된다. 더 자세한 정보는 <doc:Protocols#Class-Only-Protocols>와 [`AnyObject`](https://developer.apple.com/documentation/swift/anyobject)를 참고한다.

> Any 타입의 문법:
>
> *any-type* → **`Any`**


## Self 타입

`Self` 타입은 특정 타입을 가리키는 것이 아니라, 현재 타입을 반복하거나 그 이름을 알지 않고도 편리하게 참조할 수 있게 해준다.

프로토콜 선언이나 프로토콜 멤버 선언에서 `Self` 타입은 해당 프로토콜을 준수하는 최종 타입을 가리킨다.

구조체, 클래스, 열거형 선언에서 `Self` 타입은 해당 선언에 의해 도입된 타입을 가리킨다. 타입의 멤버 선언 내부에서 `Self` 타입은 해당 타입을 가리킨다. 클래스 선언의 멤버에서 `Self`는 다음과 같은 경우에만 사용할 수 있다:

- 메서드의 반환 타입으로
- 읽기 전용 서브스크립트의 반환 타입으로
- 읽기 전용 계산 프로퍼티의 타입으로
- 메서드의 본문 내에서

예를 들어, 아래 코드는 반환 타입이 `Self`인 인스턴스 메서드 `f`를 보여준다.

```swift
class Superclass {
    func f() -> Self { return self }
}
let x = Superclass()
print(type(of: x.f()))
// "Superclass" 출력

class Subclass: Superclass { }
let y = Subclass()
print(type(of: y.f()))
// "Subclass" 출력

let z: Superclass = Subclass()
print(type(of: z.f()))
// "Subclass" 출력
```

위 예제의 마지막 부분은 `Self`가 변수 자체의 컴파일 타입인 `Superclass`가 아니라, `z` 값의 런타임 타입인 `Subclass`를 가리킨다는 것을 보여준다.

중첩된 타입 선언 내부에서 `Self` 타입은 가장 안쪽의 타입 선언에 의해 도입된 타입을 가리킨다.

`Self` 타입은 Swift 표준 라이브러리의 [`type(of:)`](https://developer.apple.com/documentation/swift/2885064-type) 함수와 동일한 타입을 가리킨다. 현재 타입의 멤버에 접근하기 위해 `Self.someStaticMember`를 작성하는 것은 `type(of: self).someStaticMember`를 작성하는 것과 동일하다.

> Self 타입의 문법:
>
> *self-type* → **`Self`**


## 타입 상속 절

*타입 상속 절*은 특정 타입이 어떤 클래스를 상속받는지, 그리고 어떤 프로토콜을 준수하는지 명시할 때 사용한다. 타입 상속 절은 콜론(`:`)으로 시작하며, 그 뒤에 타입 식별자 목록이 이어진다.

클래스 타입은 하나의 슈퍼클래스로부터 상속받을 수 있고, 여러 프로토콜을 준수할 수 있다. 클래스를 정의할 때, 슈퍼클래스의 이름은 타입 식별자 목록의 맨 앞에 위치해야 하며, 그 뒤에 준수해야 할 프로토콜 목록이 이어진다. 만약 클래스가 다른 클래스를 상속받지 않는다면, 목록은 프로토콜로 시작할 수 있다. 클래스 상속에 대한 자세한 설명과 여러 예제는 <doc:Inheritance>를 참고한다.

다른 명명된 타입은 오직 프로토콜 목록만 상속받거나 준수할 수 있다. 프로토콜 타입은 여러 다른 프로토콜을 상속받을 수 있다. 프로토콜 타입이 다른 프로토콜을 상속받을 때, 해당 프로토콜들의 요구사항이 모두 집합되며, 현재 프로토콜을 상속받는 타입은 모든 요구사항을 준수해야 한다.

열거형 정의에서 타입 상속 절은 프로토콜 목록이 될 수 있다. 또는, 열거형이 각 케이스에 원시 값을 할당하는 경우, 해당 원시 값의 타입을 지정하는 단일 명명된 타입이 될 수도 있다. 원시 값 타입을 지정하기 위해 타입 상속 절을 사용하는 열거형 정의 예제는 <doc:Enumerations#Raw-Values>를 참고한다.

> 타입 상속 절의 문법:
>
> *type-inheritance-clause* → **`:`** *type-inheritance-list* \
> *type-inheritance-list* → *attributes*_?_ *type-identifier* | *attributes*_?_ *type-identifier* **`,`** *type-inheritance-list*


## 타입 추론

Swift는 *타입 추론*을 광범위하게 사용한다. 이를 통해 코드에서 많은 변수와 표현식의 타입 또는 타입의 일부를 생략할 수 있다. 예를 들어, `var x: Int = 0` 대신 `var x = 0`으로 작성하면 타입을 완전히 생략할 수 있다. 이 경우 컴파일러는 `x`가 `Int` 타입의 값을 가진다는 것을 올바르게 추론한다. 마찬가지로, 전체 타입이 문맥에서 추론될 수 있다면 타입의 일부를 생략할 수도 있다. 예를 들어, `let dict: Dictionary = ["A": 1]`이라고 작성하면 컴파일러는 `dict`의 타입이 `Dictionary<String, Int>`라는 것을 추론한다.

위의 두 예제에서 타입 정보는 표현식 트리의 리프에서 루트로 전달된다. 즉, `var x: Int = 0`에서 `x`의 타입은 먼저 `0`의 타입을 확인한 다음 이 타입 정보를 루트(변수 `x`)로 전달하여 추론된다.

Swift에서는 타입 정보가 반대 방향으로도 흐를 수 있다. 즉, 루트에서 리프로 전달될 수도 있다. 예를 들어, 아래 예제에서 상수 `eFloat`에 명시적으로 타입 어노테이션(`: Float`)을 추가하면 숫자 리터럴 `2.71828`이 `Double` 대신 `Float` 타입으로 추론된다.

```swift
let e = 2.71828 // e의 타입은 Double로 추론된다.
let eFloat: Float = 2.71828 // eFloat의 타입은 Float이다.
```

<!--
  - test: `type-inference`

  ```swifttest
  -> let e = 2.71828 // The type of e is inferred to be Double.
  -> let eFloat: Float = 2.71828 // The type of eFloat is Float.
  ```
-->

Swift의 타입 추론은 단일 표현식 또는 문장 수준에서 동작한다. 이는 표현식에서 생략된 타입 또는 타입의 일부를 추론하는 데 필요한 모든 정보가 해당 표현식 또는 하위 표현식의 타입 체크를 통해 접근 가능해야 함을 의미한다.

<!--
  TODO: Email Doug for a list of rules or situations describing when type-inference
  is allowed and when types must be fully typed.
-->

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


