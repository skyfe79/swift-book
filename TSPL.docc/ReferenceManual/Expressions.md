# 표현식

값에 접근하고, 수정하고, 할당하는 방법을 다룬다.

Swift에서는 네 가지 종류의 표현식이 있다:  
접두사 표현식, 중위 표현식, 기본 표현식, 그리고 접미사 표현식이다.  
표현식을 평가하면 값을 반환하거나, 부수 효과를 일으키거나, 두 가지 모두를 수행한다.

접두사 표현식과 중위 표현식은  
더 작은 표현식에 연산자를 적용할 수 있게 해준다.  
기본 표현식은 개념적으로 가장 단순한 형태의 표현식이며,  
값에 접근하는 방법을 제공한다.  
접미사 표현식은 접두사와 중위 표현식과 마찬가지로,  
함수 호출이나 멤버 접근과 같은 접미사를 사용해  
더 복잡한 표현식을 구성할 수 있게 한다.  
각 표현식의 종류는 아래 섹션에서 자세히 설명한다.

> 표현식의 문법:
>
> *expression* → *try-operator*_?_ *await-operator*_?_ *prefix-expression* *infix-expressions*_?_


## 접두사 표현식

*접두사 표현식*은 선택적인 접두사 연산자와 표현식을 조합한다. 접두사 연산자는 하나의 인자를 받으며, 바로 뒤에 오는 표현식이 그 인자가 된다.

이러한 연산자의 동작에 대한 자세한 내용은 <doc:BasicOperators>와 <doc:AdvancedOperators>를 참고한다.

Swift 표준 라이브러리에서 제공하는 연산자에 대한 정보는 [Operator Declarations](https://developer.apple.com/documentation/swift/operator_declarations)에서 확인할 수 있다.

> 접두사 표현식 문법:
>
> *prefix-expression* → *prefix-operator*_?_ *postfix-expression* \
> *prefix-expression* → *in-out-expression*


### In-Out 표현식

*in-out 표현식*은 함수 호출 표현식에 in-out 인자로 전달되는 변수를 표시한다.

```swift
&<#expression#>
```

in-out 매개변수에 대한 자세한 정보와 예제는 <doc:Functions#In-Out-Parameters>를 참고한다.

in-out 표현식은 포인터가 필요한 상황에서 포인터가 아닌 인자를 제공할 때도 사용한다. 이에 대한 내용은 <doc:Expressions#Implicit-Conversion-to-a-Pointer-Type>에서 확인할 수 있다.

> in-out 표현식의 문법:
>
> *in-out-expression* → **`&`** *primary-expression*


### Try 연산자

*try 표현식*은 `try` 연산자 뒤에 오류를 던질 수 있는 표현식이 오는 형태다. 다음과 같은 구조를 가진다:

```swift
try <#표현식#>
```

`try` 표현식의 값은 *표현식*의 값과 동일하다.

*옵셔널-try 표현식*은 `try?` 연산자 뒤에 오류를 던질 수 있는 표현식이 오는 형태다. 다음과 같은 구조를 가진다:

```swift
try? <#표현식#>
```

*표현식*이 오류를 던지지 않으면 옵셔널-try 표현식의 값은 *표현식*의 값을 포함한 옵셔널이다. 오류를 던지면 옵셔널-try 표현식의 값은 `nil`이 된다.

*강제-try 표현식*은 `try!` 연산자 뒤에 오류를 던질 수 있는 표현식이 오는 형태다. 다음과 같은 구조를 가진다:

```swift
try! <#표현식#>
```

강제-try 표현식의 값은 *표현식*의 값이다. *표현식*이 오류를 던지면 런타임 오류가 발생한다.

중위 연산자의 왼쪽에 `try`, `try?`, 또는 `try!`가 표시되면 해당 연산자는 전체 중위 표현식에 적용된다. 하지만 괄호를 사용해 연산자의 적용 범위를 명확히 할 수 있다.

```swift
// try가 두 함수 호출 모두에 적용됨
sum = try someThrowingFunction() + anotherThrowingFunction()

// try가 두 함수 호출 모두에 적용됨
sum = try (someThrowingFunction() + anotherThrowingFunction())

// 오류: try가 첫 번째 함수 호출에만 적용됨
sum = (try someThrowingFunction()) + anotherThrowingFunction()
```

<!--
  - test: `placement-of-try`

  ```swifttest
  >> func someThrowingFunction() throws -> Int { return 10 }
  >> func anotherThrowingFunction() throws -> Int { return 5 }
  >> var sum = 0
  // try가 두 함수 호출 모두에 적용됨
  -> sum = try someThrowingFunction() + anotherThrowingFunction()

  // try가 두 함수 호출 모두에 적용됨
  -> sum = try (someThrowingFunction() + anotherThrowingFunction())

  // 오류: try가 첫 번째 함수 호출에만 적용됨
  -> sum = (try someThrowingFunction()) + anotherThrowingFunction()
  !$ error: 호출이 오류를 던질 수 있지만 'try'로 표시되지 않음
  !! sum = (try someThrowingFunction()) + anotherThrowingFunction()
  !!                                      ^~~~~~~~~~~~~~~~~~~~~~~~~
  !$ note: 'try'를 사용하려 했나요?
  !! sum = (try someThrowingFunction()) + anotherThrowingFunction()
  !!                                      ^
  !!                                      try
  !$ note: 오류를 옵셔널 값으로 처리하려 했나요?
  !! sum = (try someThrowingFunction()) + anotherThrowingFunction()
  !!                                      ^
  !!                                      try?
  !$ note: 오류 전파를 비활성화하려 했나요?
  !! sum = (try someThrowingFunction()) + anotherThrowingFunction()
  !!                                      ^
  !!                                      try!
  ```
-->

`try` 표현식은 할당 연산자가 아닌 중위 연산자의 오른쪽에 올 수 없다. 단, 괄호로 감싸면 가능하다.

<!--
  - test: `try-on-right`

  ```swifttest
  >> func someThrowingFunction() throws -> Int { return 10 }
  >> var sum = 0
  -> sum = 7 + try someThrowingFunction() // 오류
  !$ error: 'try'는 할당 연산자가 아닌 연산자의 오른쪽에 올 수 없음
  !! sum = 7 + try someThrowingFunction() // 오류
  !!           ^
  -> sum = 7 + (try someThrowingFunction()) // OK
  ```
-->

표현식에 `try`와 `await` 연산자가 모두 포함되면 `try` 연산자가 먼저 와야 한다.

<!--
  "try await" 순서는 'expression' 문법의 일부이지만, 설명할 만큼 중요한 내용이다.
-->

`try`, `try?`, `try!` 사용 예제와 자세한 정보는 <doc:ErrorHandling>을 참고한다.

> try 표현식 문법:
>
> *try-operator* → **`try`** | **`try`** **`?`** | **`try`** **`!`**


### Await 연산자

*await 표현식*은 `await` 연산자와 비동기 작업의 결과를 사용하는 표현식으로 구성된다. 이 표현식은 다음과 같은 형태를 가진다:

```swift
await <#expression#>
```

`await` 표현식의 값은 *expression*의 값이다.

`await`로 표시된 표현식을 *잠재적 중단 지점*이라고 부른다. 비동기 함수의 실행은 `await`로 표시된 각 표현식에서 중단될 수 있다. 또한, 동시성 코드의 실행은 다른 어떤 지점에서도 중단되지 않는다. 이는 잠재적 중단 지점 사이의 코드가 임시로 불변성을 깨뜨리는 상태를 안전하게 업데이트할 수 있음을 의미한다. 단, 다음 잠재적 중단 지점이 오기 전에 업데이트를 완료해야 한다.

`await` 표현식은 비동기 컨텍스트 내에서만 나타날 수 있다. 예를 들어, `async(priority:operation:)` 함수에 전달된 후행 클로저 내에서 사용할 수 있다. `defer` 문의 본문이나 동기 함수 타입의 자동 클로저 내에서는 사용할 수 없다.

중위 연산자의 왼쪽 피연산자에 `await` 연산자가 표시되면, 해당 연산자는 전체 중위 표현식에 적용된다. 하지만 괄호를 사용해 연산자의 적용 범위를 명확히 할 수 있다.

```swift
// await는 두 함수 호출 모두에 적용된다
sum = await someAsyncFunction() + anotherAsyncFunction()

// await는 두 함수 호출 모두에 적용된다
sum = await (someAsyncFunction() + anotherAsyncFunction())

// 오류: await는 첫 번째 함수 호출에만 적용된다
sum = (await someAsyncFunction()) + anotherAsyncFunction()
```

`await` 표현식은 중위 연산자의 오른쪽 피연산자로 나타날 수 없다. 단, 중위 연산자가 할당 연산자이거나 `await` 표현식이 괄호로 둘러싸인 경우는 예외이다.

표현식에 `await`와 `try` 연산자가 모두 포함된 경우, `try` 연산자가 먼저 나타나야 한다.

> await 표현식의 문법:
>
> *await-operator* → **`await`**


## 중위 표현식

*중위 표현식*은 중위 이항 연산자를 사용해 왼쪽과 오른쪽 인자를 결합한다. 다음과 같은 형태를 가진다.

```swift
<#왼쪽 인자#> <#연산자#> <#오른쪽 인자#>
```

이 연산자들의 동작에 대한 자세한 내용은 <doc:BasicOperators>와 <doc:AdvancedOperators>를 참고한다.

Swift 표준 라이브러리에서 제공하는 연산자에 대한 정보는 [Operator Declarations](https://developer.apple.com/documentation/swift/operator_declarations)에서 확인할 수 있다.

<!--
  여기서는 본질적으로 표현식 시퀀스가 있으며, 그 안에 표현식의 일부가 포함된다. 
  우리는 이를 "표현식"이라고 부르지만, 일반적으로 생각하는 표현식과는 다르다. 
  두 단계로 나뉘는 과정이 있는데, 먼저 표현식 시퀀스 파싱을 통해 대략적인 파스 트리를 만든다. 
  그 다음 이름 바인딩을 통해 연산자 우선순위를 알게 되면, 두 번째 파싱 단계에서 더 전통적인 트리를 만든다.
-->

> 참고: 파싱 시점에 중위 연산자로 이루어진 표현식은 평평한 리스트로 표현된다. 
> 이 리스트는 연산자 우선순위를 적용해 트리로 변환된다. 
> 예를 들어, `2 + 3 * 5`라는 표현식은 처음에 다섯 개의 항목으로 이루어진 평평한 리스트로 이해된다. 
> 이 항목들은 `2`, `+`, `3`, `*`, `5`이다. 
> 이 과정을 통해 이 표현식은 (2 + (3 * 5))와 같은 트리로 변환된다.

> 중위 표현식 문법:
>
> *중위-표현식* → *중위-연산자* *접두사-표현식* \
> *중위-표현식* → *할당-연산자* *시도-연산자*_?_ *대기-연산자*_?_ *접두사-표현식* \
> *중위-표현식* → *조건-연산자* *시도-연산자*_?_ *대기-연산자*_?_ *접두사-표현식* \
> *중위-표현식* → *타입-캐스팅-연산자* \
> *중위-표현식들* → *중위-표현식* *중위-표현식들*_?_


### 할당 연산자

*할당 연산자*는 주어진 표현식에 새로운 값을 설정한다. 
이 연산자는 다음과 같은 형태를 가진다:

```swift
<#expression#> = <#value#>
```

*expression*의 값은 *value*를 평가하여 얻은 값으로 설정된다. 
만약 *expression*이 튜플이라면, *value*도 동일한 개수의 요소를 가진 튜플이어야 한다. 
(중첩된 튜플도 허용된다.) 
할당은 *value*의 각 부분에서 *expression*의 해당 부분으로 수행된다. 
예를 들어:

```swift
(a, _, (b, c)) = ("test", 9.45, (12, 3))
// a는 "test", b는 12, c는 3, 그리고 9.45는 무시됨
```

<!--
  - test: `assignmentOperator`

  ```swifttest
  >> var (a, _, (b, c)) = ("test", 9.45, (12, 3))
  -> (a, _, (b, c)) = ("test", 9.45, (12, 3))
  /> a is \"\(a)\", b is \(b), c is \(c), and 9.45 is ignored
  </ a is "test", b is 12, c is 3, and 9.45 is ignored
  ```
-->

할당 연산자는 어떤 값도 반환하지 않는다.

> 할당 연산자의 문법:
>
> *assignment-operator* → **`=`**


### 삼항 조건 연산자

*삼항 조건 연산자*는 주어진 조건의 값에 따라 두 가지 값 중 하나를 반환한다. 이 연산자는 다음과 같은 형태를 가진다:

```swift
<#조건#> ? <#참일 때 사용할 표현식#> : <#거짓일 때 사용할 표현식#>
```

*조건*이 `true`로 평가되면, 삼항 조건 연산자는 첫 번째 표현식을 평가하고 그 값을 반환한다. 반대로, 조건이 `false`로 평가되면 두 번째 표현식을 평가하고 그 값을 반환한다. 사용되지 않은 표현식은 평가되지 않는다.

삼항 조건 연산자를 사용한 예제는 <doc:BasicOperators#Ternary-Conditional-Operator>를 참고한다.

> 삼항 조건 연산자의 문법:
>
> *삼항 조건 연산자* → **`?`** *표현식* **`:`**


### 타입 캐스팅 연산자

타입 캐스팅 연산자는 총 네 가지가 있다:
`is` 연산자,
`as` 연산자,
`as?` 연산자,
그리고 `as!` 연산자.

이 연산자들은 다음과 같은 형태를 가진다:

```swift
<#expression#> is <#type#>
<#expression#> as <#type#>
<#expression#> as? <#type#>
<#expression#> as! <#type#>
```

`is` 연산자는 런타임에 *expression*이 지정된 *type*으로 캐스팅될 수 있는지 확인한다. *expression*이 지정된 *type*으로 캐스팅될 수 있으면 `true`를 반환하고, 그렇지 않으면 `false`를 반환한다.

<!--
  - test: `triviallyTrueIsAndAs`

  ```swifttest
  -> assert("hello" is String)
  -> assert(!("hello" is Int))
  !$ warning: 'is' test is always true
  !! assert("hello" is String)
  !!                ^
  !$ warning: cast from 'String' to unrelated type 'Int' always fails
  !! assert(!("hello" is Int))
  !!          ~~~~~~~ ^  ~~~
  ```
-->

<!--
  - test: `is-operator-tautology`

  ```swifttest
  -> class Base {}
  -> class Subclass: Base {}
  -> var s = Subclass()
  -> var b = Base()

  -> assert(s is Base)
  !$ warning: 'is' test is always true
  !! assert(s is Base)
  !!          ^
  ```
-->

`as` 연산자는 컴파일 타임에 캐스팅이 항상 성공할 것으로 알려진 경우, 예를 들어 업캐스팅이나 브리징에서 사용된다. 업캐스팅은 중간 변수를 사용하지 않고도 표현식을 해당 타입의 상위 타입 인스턴스로 사용할 수 있게 한다. 다음 두 접근 방식은 동일하다:

```swift
func f(_ any: Any) { print("Function for Any") }
func f(_ int: Int) { print("Function for Int") }
let x = 10
f(x)
// "Function for Int" 출력

let y: Any = x
f(y)
// "Function for Any" 출력

f(x as Any)
// "Function for Any" 출력
```

<!--
  - test: `explicit-type-with-as-operator`

  ```swifttest
  -> func f(_ any: Any) { print("Function for Any") }
  -> func f(_ int: Int) { print("Function for Int") }
  -> let x = 10
  -> f(x)
  <- Function for Int

  -> let y: Any = x
  -> f(y)
  <- Function for Any

  -> f(x as Any)
  <- Function for Any
  ```
-->

브리징은 Swift 표준 라이브러리 타입인 `String`과 같은 표현식을 해당 Foundation 타입인 `NSString`으로 사용할 수 있게 한다. 이때 새로운 인스턴스를 생성할 필요가 없다. 브리징에 대한 자세한 내용은 [Working with Foundation Types](https://developer.apple.com/documentation/swift/imported_c_and_objective_c_apis/working_with_foundation_types)를 참고한다.

`as?` 연산자는 *expression*을 지정된 *type*으로 조건부 캐스팅한다. `as?` 연산자는 지정된 *type*의 옵셔널을 반환한다. 런타임에 캐스팅이 성공하면 *expression*의 값이 옵셔널로 감싸져 반환되고, 그렇지 않으면 `nil`이 반환된다. 지정된 *type*으로의 캐스팅이 항상 실패하거나 항상 성공할 경우, 컴파일 타임 에러가 발생한다.

`as!` 연산자는 *expression*을 지정된 *type*으로 강제 캐스팅한다. `as!` 연산자는 지정된 *type*의 값을 반환하며, 옵셔널 타입이 아니다. 캐스팅이 실패하면 런타임 에러가 발생한다. `x as! T`의 동작은 `(x as? T)!`와 동일하다.

타입 캐스팅에 대한 자세한 내용과 타입 캐스팅 연산자를 사용한 예제는 <doc:TypeCasting>을 참고한다.

> 타입 캐스팅 연산자의 문법:
>
> *type-casting-operator* → **`is`** *type* \
> *type-casting-operator* → **`as`** *type* \
> *type-casting-operator* → **`as`** **`?`** *type* \
> *type-casting-operator* → **`as`** **`!`** *type*


## 기본 표현식

*기본 표현식*은 가장 기본적인 형태의 표현식이다. 독립적으로 사용할 수 있으며, 다른 토큰과 결합해 접두사 표현식, 중위 표현식, 후위 표현식을 만들 수 있다.

> 기본 표현식 문법:
>
> *primary-expression* → *identifier* *generic-argument-clause*_?_ \
> *primary-expression* → *literal-expression* \
> *primary-expression* → *self-expression* \
> *primary-expression* → *superclass-expression* \
> *primary-expression* → *conditional-expression* \
> *primary-expression* → *closure-expression* \
> *primary-expression* → *parenthesized-expression* \
> *primary-expression* → *tuple-expression* \
> *primary-expression* → *implicit-member-expression* \
> *primary-expression* → *wildcard-expression* \
> *primary-expression* → *macro-expansion-expression* \
> *primary-expression* → *key-path-expression* \
> *primary-expression* → *selector-expression* \
> *primary-expression* → *key-path-string-expression*

<!--
  NOTE: 기본 표현식을 후위 표현식과 구분한 이유는 설명을 더 체계적으로 정리하기 위함이다.
-->

<!--
  TR: 식 문맥에서 식별자 뒤에 일반 인자 절이 허용되는가?
  이는 식별자가 *타입* 식별자인 경우에만 발생하는 것 같다.
-->


### 리터럴 표현식

리터럴 표현식은 일반 리터럴(문자열이나 숫자 등), 배열 리터럴, 딕셔너리 리터럴, 또는 플레이그라운드 리터럴로 구성된다.

> 참고:
> Swift 5.9 이전에는 다음과 같은 특수 리터럴이 인식되었다:
> `#column`, `#dsohandle`, `#fileID`, `#filePath`, `#file`, `#function`, `#line`.
> 이제 이들은 Swift 표준 라이브러리의 매크로로 구현되었다:
> [`column()`](https://developer.apple.com/documentation/swift/column()),
> [`dsohandle()`](https://developer.apple.com/documentation/swift/dsohandle()),
> [`fileID()`](https://developer.apple.com/documentation/swift/fileID()),
> [`filePath()`](https://developer.apple.com/documentation/swift/filePath()),
> [`file()`](https://developer.apple.com/documentation/swift/file()),
> [`function()`](https://developer.apple.com/documentation/swift/function()),
> [`line()`](https://developer.apple.com/documentation/swift/line()).

<!--
  - test: `pound-file-flavors`

  ```swifttest
  >> print(#file == #filePath)
  << true
  >> print(#file == #fileID)
  << false
  ```
-->

*배열 리터럴*은 값들의 순서 있는 컬렉션이다. 다음과 같은 형태를 가진다:

```swift
[<#value 1#>, <#value 2#>, <#...#>]
```

배열의 마지막 표현식 뒤에는 선택적으로 쉼표를 추가할 수 있다. 배열 리터럴의 값은 `[T]` 타입을 가지며, 여기서 `T`는 배열 내부 표현식의 타입이다. 만약 여러 타입의 표현식이 있다면, `T`는 이들의 가장 가까운 공통 상위 타입이 된다. 빈 배열 리터럴은 빈 대괄호 쌍을 사용해 작성하며, 특정 타입의 빈 배열을 생성할 때 사용할 수 있다.

```swift
var emptyArray: [Double] = []
```

<!--
  - test: `array-literal-brackets`

  ```swifttest
  -> var emptyArray: [Double] = []
  ```
-->

*딕셔너리 리터럴*은 키-값 쌍의 순서 없는 컬렉션이다. 다음과 같은 형태를 가진다:

```swift
[<#key 1#>: <#value 1#>, <#key 2#>: <#value 2#>, <#...#>]
```

딕셔너리의 마지막 표현식 뒤에는 선택적으로 쉼표를 추가할 수 있다. 딕셔너리 리터럴의 값은 `[Key: Value]` 타입을 가지며, 여기서 `Key`는 키 표현식의 타입이고 `Value`는 값 표현식의 타입이다. 만약 여러 타입의 표현식이 있다면, `Key`와 `Value`는 각각의 값들에 대한 가장 가까운 공통 상위 타입이 된다. 빈 딕셔너리 리터럴은 빈 배열 리터럴과 구분하기 위해 대괄호 안에 콜론을 넣어 작성한다(`[:]`). 빈 딕셔너리 리터럴을 사용해 특정 키와 값 타입의 빈 딕셔너리를 생성할 수 있다.

```swift
var emptyDictionary: [String: Double] = [:]
```

<!--
  - test: `dictionary-literal-brackets`

  ```swifttest
  -> var emptyDictionary: [String: Double] = [:]
  ```
-->

*플레이그라운드 리터럴*은 Xcode에서 프로그램 편집기 내에서 색상, 파일, 이미지의 인터랙티브 표현을 생성하는 데 사용된다. Xcode 외부의 일반 텍스트에서 플레이그라운드 리터럴은 특수한 리터럴 구문으로 표현된다.

Xcode에서 플레이그라운드 리터럴을 사용하는 방법에 대한 자세한 내용은 Xcode 도움말의 [색상, 파일, 이미지 리터럴 추가](https://help.apple.com/xcode/mac/current/#/dev4c60242fc)를 참고한다.

> 리터럴 표현식 문법:
>
> *literal-expression* → *literal* \
> *literal-expression* → *array-literal* | *dictionary-literal* | *playground-literal*
>
> *array-literal* → **`[`** *array-literal-items*_?_ **`]`** \
> *array-literal-items* → *array-literal-item* **`,`**_?_ | *array-literal-item* **`,`** *array-literal-items* \
> *array-literal-item* → *expression*
>
> *dictionary-literal* → **`[`** *dictionary-literal-items* **`]`** | **`[`** **`:`** **`]`** \
> *dictionary-literal-items* → *dictionary-literal-item* **`,`**_?_ | *dictionary-literal-item* **`,`** *dictionary-literal-items* \
> *dictionary-literal-item* → *expression* **`:`** *expression*
>
> *playground-literal* → **`#colorLiteral`** **`(`** **`red`** **`:`** *expression* **`,`** **`green`** **`:`** *expression* **`,`** **`blue`** **`:`** *expression* **`,`** **`alpha`** **`:`** *expression* **`)`** \
> *playground-literal* → **`#fileLiteral`** **`(`** **`resourceName`** **`:`** *expression* **`)`** \
> *playground-literal* → **`#imageLiteral`** **`(`** **`resourceName`** **`:`** *expression* **`)`**


### `self` 표현식

`self` 표현식은 현재 타입 또는 해당 타입의 인스턴스를 명시적으로 참조한다. 다음과 같은 형태로 사용할 수 있다:

```swift
self
self.<#멤버 이름#>
self[<#서브스크립트 인덱스#>]
self(<#초기화 인자#>)
self.init(<#초기화 인자#>)
```

<!--
  TODO: 두 번째 마지막 형태(예: self(arg: value))에 대해 나중에 설명 추가.
-->

초기화 메서드, 서브스크립트, 인스턴스 메서드에서 `self`는 해당 타입의 현재 인스턴스를 가리킨다. 타입 메서드에서는 `self`가 현재 타입을 참조한다.

`self` 표현식은 멤버에 접근할 때 스코프를 명확히 지정하기 위해 사용된다. 예를 들어, 함수 매개변수와 같은 이름의 변수가 스코프 내에 있을 때 혼란을 방지하기 위해 `self`를 사용할 수 있다. 예를 들면:

```swift
class SomeClass {
    var greeting: String
    init(greeting: String) {
        self.greeting = greeting
    }
}
```

<!--
  - test: `self-expression`

  ```swifttest
  -> class SomeClass {
         var greeting: String
         init(greeting: String) {
             self.greeting = greeting
         }
     }
  ```
-->

값 타입의 뮤테이팅 메서드에서는 `self`에 해당 값 타입의 새 인스턴스를 할당할 수 있다. 예를 들어:

```swift
struct Point {
    var x = 0.0, y = 0.0
    mutating func moveBy(x deltaX: Double, y deltaY: Double) {
        self = Point(x: x + deltaX, y: y + deltaY)
    }
}
```

<!--
  - test: `self-expression`

  ```swifttest
  -> struct Point {
        var x = 0.0, y = 0.0
        mutating func moveBy(x deltaX: Double, y deltaY: Double) {
           self = Point(x: x + deltaX, y: y + deltaY)
        }
     }
  >> var somePoint = Point(x: 1.0, y: 1.0)
  >> somePoint.moveBy(x: 2.0, y: 3.0)
  >> print("The point is now at (\(somePoint.x), \(somePoint.y))")
  << The point is now at (3.0, 4.0)
  ```
-->

<!-- Apple Books screenshot begins here. -->

> `self` 표현식 문법:
>
> *self-expression* → **`self`** | *self-method-expression* | *self-subscript-expression* | *self-initializer-expression*
>
> *self-method-expression* → **`self`** **`.`** *identifier* \
> *self-subscript-expression* → **`self`** **`[`** *function-call-argument-list* **`]`** \
> *self-initializer-expression* → **`self`** **`.`** **`init`**


### 슈퍼클래스 표현식

*슈퍼클래스 표현식*은 클래스가 자신의 슈퍼클래스와 상호작용할 수 있게 한다. 이 표현식은 다음 중 하나의 형태를 가진다:

```swift
super.<#멤버 이름#>
super[<#서브스크립트 인덱스#>]
super.init(<#초기화 인자#>)
```

첫 번째 형태는 슈퍼클래스의 멤버에 접근할 때 사용한다.  
두 번째 형태는 슈퍼클래스의 서브스크립트 구현에 접근할 때 사용한다.  
세 번째 형태는 슈퍼클래스의 초기화 메서드에 접근할 때 사용한다.

서브클래스는 멤버, 서브스크립트, 초기화 메서드를 구현할 때 슈퍼클래스 표현식을 사용하여 슈퍼클래스의 구현을 활용할 수 있다.

> 슈퍼클래스 표현식 문법:
>
> *슈퍼클래스-표현식* → *슈퍼클래스-메서드-표현식* | *슈퍼클래스-서브스크립트-표현식* | *슈퍼클래스-초기화-표현식*
>
> *슈퍼클래스-메서드-표현식* → **`super`** **`.`** *식별자* \
> *슈퍼클래스-서브스크립트-표현식* → **`super`** **`[`** *함수-호출-인자-목록* **`]`** \
> *슈퍼클래스-초기화-표현식* → **`super`** **`.`** **`init`**


### 조건식

조건식은 특정 조건의 값에 따라 여러 주어진 값 중 하나를 평가한다. 조건식은 다음 두 가지 형태 중 하나를 가진다:

```swift
if <#조건 1#> {
   <#조건 1이 참일 때 사용되는 표현식#>
} else if <#조건 2#> {
   <#조건 2가 참일 때 사용되는 표현식#>
} else {
   <#두 조건 모두 거짓일 때 사용되는 표현식#>
}

switch <#표현식#> {
case <#패턴 1#>:
    <#표현식 1#>
case <#패턴 2#> where <#조건#>:
    <#표현식 2#>
default:
    <#표현식 3#>
}
```

조건식은 `if` 문이나 `switch` 문과 동일한 동작과 문법을 가지지만, 아래에서 설명할 몇 가지 차이점이 있다.

조건식은 다음과 같은 상황에서만 사용할 수 있다:

  - 변수에 할당되는 값으로 사용.
  - 변수나 상수 선언 시 초기값으로 사용.
  - `throw` 표현식에서 던져지는 오류로 사용.
  - 함수, 클로저, 프로퍼티 getter에서 반환되는 값으로 사용.
  - 조건식의 한 가지 분기 내부의 값으로 사용.

조건식의 분기는 완전해야 하며, 조건에 상관없이 항상 값을 생성한다. 이는 각 `if` 분기에 해당하는 `else` 분기가 필요함을 의미한다.

각 분기는 단일 표현식, `throw` 문, 또는 값을 반환하지 않는 함수 호출 중 하나를 포함한다.

각 분기는 동일한 타입의 값을 생성해야 한다. 각 분기의 타입 검사는 독립적으로 이루어지기 때문에, 분기가 서로 다른 종류의 리터럴을 포함하거나 분기의 값이 `nil`인 경우에는 명시적으로 타입을 지정해야 할 때가 있다. 이 경우, 결과가 할당되는 변수에 타입 주석을 추가하거나 분기의 값에 `as` 캐스트를 추가한다.

```swift
let number: Double = if someCondition { 10 } else { 12.34 }
let number = if someCondition { 10 as Double } else { 12.34 }
```

결과 빌더 내부에서는 조건식을 변수나 상수의 초기값으로만 사용할 수 있다. 이는 결과 빌더 내에서 `if`나 `switch`를 작성할 때, 변수나 상수 선언 외부에서 사용하면 해당 코드가 분기 문으로 이해되고, 결과 빌더의 메서드 중 하나가 해당 코드를 변환한다는 것을 의미한다.

조건식의 한 분기가 오류를 던지더라도 `try` 표현식 안에 조건식을 넣지 않도록 주의한다.

> 조건식 문법:
>
> *conditional-expression* → *if-expression* | *switch-expression*
>
> *if-expression* → **`if`** *condition-list* **`{`** *statement* **`}`** *if-expression-tail* \
> *if-expression-tail* → **`else`** *if-expression* \
> *if-expression-tail* → **`else`** **`{`** *statement* **`}`**
>
> *switch-expression* → **`switch`** *expression* **`{`** *switch-expression-cases* **`}`** \
> *switch-expression-cases* → *switch-expression-case* *switch-expression-cases*_?_ \
> *switch-expression-case* → *case-label* *statement* \
> *switch-expression-case* → *default-label* *statement*


### 클로저 표현식

*클로저 표현식*은 클로저를 생성한다. 다른 프로그래밍 언어에서는 *람다* 또는 *익명 함수*라고도 한다. 함수 선언과 마찬가지로 클로저는 문장을 포함하며, 자신을 둘러싼 스코프에서 상수와 변수를 캡처한다. 클로저 표현식은 다음과 같은 형태를 가진다:

```swift
{ (<#매개변수#>) -> <#반환 타입#> in
   <#문장#>
}
```

*매개변수*는 함수 선언에서 사용하는 매개변수와 동일한 형태를 가진다. 이는 <doc:Declarations#Function-Declaration>에서 설명한 것과 같다.

클로저 표현식에서 `throws` 또는 `async`를 명시적으로 작성하면, 클로저가 에러를 던지거나 비동기적으로 동작한다는 것을 나타낸다.

```swift
{ (<#매개변수#>) async throws -> <#반환 타입#> in
   <#문장#>
}
```

클로저 본문에 `throws` 문장이 포함되어 있거나, `do` 문장 내에서 완벽한 오류 처리가 없는 `try` 표현식이 포함되어 있다면, 해당 클로저는 에러를 던지는 것으로 간주된다. 만약 에러를 던지는 클로저가 단일 타입의 에러만 던진다면, 해당 클로저는 그 타입의 에러를 던지는 것으로 이해된다. 그렇지 않으면 `any Error`를 던지는 것으로 간주된다. 마찬가지로, 본문에 `await` 표현식이 포함되어 있다면, 해당 클로저는 비동기적으로 동작하는 것으로 이해된다.

클로저를 더 간결하게 작성할 수 있는 몇 가지 특별한 형태가 있다:

<!-- Apple Books screenshot ends here. -->

- 클로저는 매개변수의 타입, 반환 타입, 또는 둘 다 생략할 수 있다. 매개변수 이름과 타입을 모두 생략하면, `in` 키워드를 문장 앞에서 생략할 수 있다. 생략된 타입을 추론할 수 없는 경우, 컴파일 타임 오류가 발생한다.
- 클로저는 매개변수의 이름을 생략할 수 있다. 이 경우 매개변수는 암시적으로 `$` 뒤에 위치 번호가 붙은 이름으로 간주된다: `$0`, `$1`, `$2` 등.
- 단일 표현식으로만 구성된 클로저는 그 표현식의 값을 반환하는 것으로 간주된다. 이 표현식의 내용은 주변 표현식의 타입 추론 시에도 고려된다.

다음 클로저 표현식은 모두 동일하다:

```swift
myFunction { (x: Int, y: Int) -> Int in
    return x + y
}

myFunction { x, y in
    return x + y
}

myFunction { return $0 + $1 }

myFunction { $0 + $1 }
```

<!--
  - test: `closure-expression-forms`

  ```swifttest
  >> func myFunction(f: (Int, Int) -> Int) {}
  -> myFunction { (x: Int, y: Int) -> Int in
         return x + y
     }

  -> myFunction { x, y in
         return x + y
     }

  -> myFunction { return $0 + $1 }

  -> myFunction { $0 + $1 }
  ```
-->

클로저를 함수의 인자로 전달하는 방법에 대한 자세한 내용은 <doc:Expressions#Function-Call-Expression>을 참조한다.

클로저 표현식은 변수나 상수에 저장하지 않고도 사용할 수 있다. 예를 들어, 함수 호출의 일부로 클로저를 즉시 사용하는 경우가 있다. 위 코드에서 `myFunction`에 전달된 클로저 표현식은 이러한 즉시 사용의 예시이다. 결과적으로, 클로저 표현식이 탈출 가능한지 여부는 표현식의 주변 컨텍스트에 따라 결정된다. 클로저 표현식이 즉시 호출되거나 탈출하지 않는 함수 인자로 전달되면, 해당 클로저는 탈출하지 않는 것으로 간주된다. 그렇지 않으면 클로저는 탈출 가능한 것으로 간주된다.

탈출 클로저에 대한 자세한 내용은 <doc:Closures#Escaping-Closures>를 참조한다.


#### 캡처 리스트

기본적으로 클로저 표현식은 주변 스코프의 상수와 변수를 강한 참조로 캡처한다. **캡처 리스트**를 사용하면 클로저가 값을 캡처하는 방식을 명시적으로 제어할 수 있다.

캡처 리스트는 대괄호로 둘러싸인 쉼표로 구분된 표현식 목록으로 작성하며, 매개변수 목록 앞에 위치한다. 캡처 리스트를 사용할 때는 매개변수 이름, 타입, 반환 타입을 생략하더라도 `in` 키워드를 반드시 사용해야 한다.

캡처 리스트의 항목은 클로저가 생성될 때 초기화된다. 캡처 리스트의 각 항목은 주변 스코프에서 같은 이름을 가진 상수나 변수의 값으로 초기화된 상수이다. 예를 들어 아래 코드에서 `a`는 캡처 리스트에 포함되었지만 `b`는 포함되지 않아 서로 다른 동작을 보인다.

```swift
var a = 0
var b = 0
let closure = { [a] in
 print(a, b)
}

a = 10
b = 10
closure()
// Prints "0 10"
```

<!--
  - test: `capture-list-value-semantics`

  ```swifttest
  -> var a = 0
  -> var b = 0
  -> let closure = { [a] in
      print(a, b)
  }

  -> a = 10
  -> b = 10
  -> closure()
  <- 0 10
  ```
-->

여기서 `a`라는 이름이 두 개 존재한다. 하나는 외부 스코프의 변수이고, 다른 하나는 클로저 스코프의 상수이다. 반면 `b`는 하나의 변수만 존재한다. 내부 스코프의 `a`는 클로저가 생성될 때 외부 스코프의 `a` 값으로 초기화되지만, 두 값은 특별한 연결이 없다. 따라서 외부 스코프에서 `a` 값을 변경해도 내부 스코프의 `a` 값에는 영향을 미치지 않는다. 마찬가지로 클로저 내부에서 `a` 값을 변경해도 외부 스코프의 `a` 값은 변하지 않는다. 반면 `b`는 하나의 변수이므로 클로저 내부나 외부에서 값을 변경하면 두 곳 모두에 반영된다.

<!--
  [Contributor 6004] also describes the distinction as
  "capturing the variable, not the value"
  but he notes that we don't have a rigorous definition of
  capturing a variable in Swift
  (unlike some other languages)
  so that description's not likely to be very helpful for developers.
-->

이러한 차이는 캡처된 변수의 타입이 참조 의미론을 가질 때는 보이지 않는다. 예를 들어 아래 코드에서 `x`라는 이름이 두 개 존재하지만, 참조 의미론 때문에 두 상수 모두 같은 객체를 가리킨다.

```swift
class SimpleClass {
    var value: Int = 0
}
var x = SimpleClass()
var y = SimpleClass()
let closure = { [x] in
    print(x.value, y.value)
}

x.value = 10
y.value = 10
closure()
// Prints "10 10"
```

<!--
  - test: `capture-list-reference-semantics`

  ```swifttest
  -> class SimpleClass {
         var value: Int = 0
     }
  -> var x = SimpleClass()
  -> var y = SimpleClass()
  -> let closure = { [x] in
         print(x.value, y.value)
     }

  -> x.value = 10
  -> y.value = 10
  -> closure()
  <- 10 10
  ```
-->

<!--
  - test: `capture-list-with-commas`

  ```swifttest
  -> var x = 100
  -> var y = 7
  -> var f: () -> Int = { [x, y] in x+y }
  >> let r0 = f()
  >> assert(r0 == 107)
  ```
-->

<!--
  It's not an error to capture things that aren't included in the capture list,
  although maybe it should be.  See also rdar://17024367.
-->

<!--
  - test: `capture-list-is-not-exhaustive`

  ```swifttest
  -> var x = 100
     var y = 7
     var f: () -> Int = { [x] in x }
     var g: () -> Int = { [x] in x+y }

  -> let r0 = f()
  -> assert(r0 == 100)
  -> let r1 = g()
  -> assert(r1 == 107)
  ```
-->

표현식의 값 타입이 클래스인 경우, 캡처 리스트에서 `weak` 또는 `unowned`를 사용해 약한 참조 또는 미소유 참조로 값을 캡처할 수 있다.

```swift
myFunction { print(self.title) }                    // 암시적 강한 캡처
myFunction { [self] in print(self.title) }          // 명시적 강한 캡처
myFunction { [weak self] in print(self!.title) }    // 약한 캡처
myFunction { [unowned self] in print(self.title) }  // 미소유 캡처
```

<!--
  - test: `closure-expression-weak`

  ```swifttest
  >> func myFunction(f: () -> Void) { f() }
  >> class C {
  >> let title = "Title"
  >> func method() {
  -> myFunction { print(self.title) }                    // implicit strong capture
  -> myFunction { [self] in print(self.title) }          // explicit strong capture
  -> myFunction { [weak self] in print(self!.title) }    // weak capture
  -> myFunction { [unowned self] in print(self.title) }  // unowned capture
  >> } }
  >> C().method()
  << Title
  << Title
  << Title
  << Title
  ```
-->

캡처 리스트에서 임의의 표현식을 이름 있는 값에 바인딩할 수도 있다. 표현식은 클로저가 생성될 때 평가되며, 지정된 강도로 값이 캡처된다. 예를 들면 다음과 같다:

```swift
// "self.parent"를 "parent"로 약한 캡처
myFunction { [weak parent = self.parent] in print(parent!.title) }
```

<!--
  - test: `closure-expression-capture`

  ```swifttest
  >> func myFunction(f: () -> Void) { f() }
  >> class P { let title = "Title" }
  >> class C {
  >> let parent = P()
  >> func method() {
  // Weak capture of "self.parent" as "parent"
  -> myFunction { [weak parent = self.parent] in print(parent!.title) }
  >> } }
  >> C().method()
  << Title
  ```
-->

클로저 표현식에 대한 더 많은 정보와 예제는 <doc:Closures#Closure-Expressions>를 참고하라. 캡처 리스트에 대한 더 많은 정보와 예제는 <doc:AutomaticReferenceCounting#Resolving-Strong-Reference-Cycles-for-Closures>를 참고하라.

<!--
  - test: `async-throwing-closure-syntax`

  ```swifttest
  >> var a = 12
  >> let c1 = { [a] in return a }                  // OK -- no async or throws
  >> let c2 = { [a] async in return a }            // ERROR
  >> let c3 = { [a] async -> in return a }         // ERROR
  >> let c4 = { [a] () async -> Int in return a }  // OK -- has () and ->
  !$ error: expected expression
  !! let c3 = { [a] async -> in return a }         // ERROR
  !! ^
  !$ error: unable to infer type of a closure parameter 'async' in the current context
  !! let c2 = { [a] async in return a }            // ERROR
  !! ^
  // NOTE: The error message for c3 gets printed by the REPL before the c2 error.
  ```
-->

> 클로저 표현식 문법:
>
> *closure-expression* → **`{`** *attributes*_?_ *closure-signature*_?_ *statements*_?_ **`}`**
>
> *closure-signature* → *capture-list*_?_ *closure-parameter-clause* **`async`**_?_ *throws-clause*_?_ *function-result*_?_ **`in`** \
> *closure-signature* → *capture-list* **`in`**
>
> *closure-parameter-clause* → **`(`** **`)`** | **`(`** *closure-parameter-list* **`)`** | *identifier-list* \
> *closure-parameter-list* → *closure-parameter* | *closure-parameter* **`,`** *closure-parameter-list* \
> *closure-parameter* → *closure-parameter-name* *type-annotation*_?_ \
> *closure-parameter* → *closure-parameter-name* *type-annotation* **`...`** \
> *closure-parameter-name* → *identifier*
>
> *capture-list* → **`[`** *capture-list-items* **`]`** \
> *capture-list-items* → *capture-list-item* | *capture-list-item* **`,`** *capture-list-items* \
> *capture-list-item* → *capture-specifier*_?_ *identifier* \
> *capture-list-item* → *capture-specifier*_?_ *identifier* **`=`** *expression* \
> *capture-list-item* → *capture-specifier*_?_ *self-expression* \
> *capture-specifier* → **`weak`** | **`unowned`** | **`unowned(safe)`** | **`unowned(unsafe)`**


### 암시적 멤버 표현식

암시적 멤버 표현식(Implicit Member Expression)은 타입의 멤버에 접근하는 축약된 방식이다. 예를 들어 열거형 케이스나 타입 메서드에 접근할 때, 타입 추론을 통해 타입을 명시적으로 지정하지 않고도 멤버를 사용할 수 있다. 이 표현식은 다음과 같은 형태를 가진다:

```swift
.<#멤버 이름#>
```

예를 들어:

```swift
var x = MyEnumeration.someValue
x = .anotherValue
```

<!--
  - test: `implicitMemberEnum`

  ```swifttest
  >> enum MyEnumeration { case someValue, anotherValue }
  -> var x = MyEnumeration.someValue
  -> x = .anotherValue
  ```
-->

추론된 타입이 옵셔널인 경우, 암시적 멤버 표현식에서 옵셔널이 아닌 타입의 멤버를 사용할 수도 있다.

```swift
var someOptional: MyEnumeration? = .someValue
```

<!--
  - test: `implicitMemberEnum`

  ```swifttest
  -> var someOptional: MyEnumeration? = .someValue
  ```
-->

암시적 멤버 표현식은 <doc:Expressions#Postfix-Expressions>에 나열된 후위 연산자나 다른 후위 문법과 함께 사용할 수 있다. 이를 *체인된 암시적 멤버 표현식(Chained Implicit Member Expression)* 이라고 부른다. 체인된 후위 표현식들이 모두 동일한 타입을 가지는 경우가 일반적이지만, 유일한 요구사항은 전체 체인된 암시적 멤버 표현식이 컨텍스트에서 추론된 타입으로 변환 가능해야 한다는 것이다. 특히, 추론된 타입이 옵셔널인 경우 옵셔널이 아닌 타입의 값을 사용할 수 있으며, 추론된 타입이 클래스 타입인 경우 해당 클래스의 서브클래스 값을 사용할 수 있다. 예를 들어:

```swift
class SomeClass {
    static var shared = SomeClass()
    static var sharedSubclass = SomeSubclass()
    var a = AnotherClass()
}
class SomeSubclass: SomeClass { }
class AnotherClass {
    static var s = SomeClass()
    func f() -> SomeClass { return AnotherClass.s }
}
let x: SomeClass = .shared.a.f()
let y: SomeClass? = .shared
let z: SomeClass = .sharedSubclass
```

<!--
  - test: `implicit-member-chain`

  ```swifttest
  -> class SomeClass {
         static var shared = SomeClass()
         static var sharedSubclass = SomeSubclass()
         var a = AnotherClass()
     }
  -> class SomeSubclass: SomeClass { }
  -> class AnotherClass {
         static var s = SomeClass()
         func f() -> SomeClass { return AnotherClass.s }
     }
  -> let x: SomeClass = .shared.a.f()
  -> let y: SomeClass? = .shared
  -> let z: SomeClass = .sharedSubclass
  ```
-->

위 코드에서 `x`의 타입은 컨텍스트에서 추론된 타입과 정확히 일치하며, `y`의 타입은 `SomeClass`에서 `SomeClass?`로 변환 가능하다. 또한 `z`의 타입은 `SomeSubclass`에서 `SomeClass`로 변환 가능하다.

> 암시적 멤버 표현식 문법:
>
> *암시적-멤버-표현식* → **`.`** *식별자* \
> *암시적-멤버-표현식* → **`.`** *식별자* **`.`** *후위-표현식*

<!--
  위 문법은 아래 테스트에서 추가된 부분을 허용하며,
  이는 SE-0287 목록에서 생략되었지만 여전히 동작한다.
  또한 문법은 후위-표현식의 정의로 인해 모든 기본 표현식을 허용하므로
  과도하게 생성될 수 있다.
-->

<!--
  - test: `implicit-member-grammar`

  ```swifttest
  // self 표현식
  >> enum E { case left, right }
  >> let e: E = .left
  >> let e2: E = .left.self
  >> assert(e == e2)

  // 후위 연산자
  >> postfix operator ~
  >> extension E {
  >>     static postfix func ~ (e: E) -> E {
  >>         switch e {
  >>         case .left: return .right
  >>         case .right: return .left
  >>         }
  >>     }
  >> }
  >> let e3: E = .left~
  >> assert(e3 == .right)

  // 초기화 표현식
  >> class S {
  >>     var num: Int
  >>     init(bestNumber: Int) { self.num = bestNumber }
  >> }
  >> let s: S = .init(bestNumber: 42)
  ```
-->


### 괄호로 둘러싼 표현식

*괄호로 둘러싼 표현식*은 표현식을 괄호로 감싼 형태를 말한다. 괄호를 사용해 연산의 우선순위를 명시적으로 지정하거나 표현식을 그룹화할 수 있다. 괄호로 그룹화해도 표현식의 타입은 변하지 않는다. 예를 들어, `(1)`의 타입은 그대로 `Int`이다.

<!--
  "Tuple Expression" 아래의 langref 문법을 참조하세요.
-->

> 괄호로 둘러싼 표현식의 문법:
>
> *parenthesized-expression* → **`(`** *expression* **`)`**


### 튜플 표현식

*튜플 표현식*은 괄호로 둘러싸인 쉼표로 구분된 표현식 목록으로 구성된다. 각 표현식 앞에는 선택적으로 식별자를 추가할 수 있으며, 콜론(`:`)으로 구분한다. 튜플 표현식은 다음과 같은 형태를 가진다:

```swift
(<#식별자 1#>: <#표현식 1#>, <#식별자 2#>: <#표현식 2#>, <#...#>)
```

튜플 표현식 내의 각 식별자는 해당 튜플 표현식의 범위 내에서 고유해야 한다. 중첩된 튜플 표현식에서 동일한 중첩 수준의 식별자는 고유해야 한다. 예를 들어, `(a: 10, a: 20)`은 동일한 수준에서 `a`라는 라벨이 두 번 나타나기 때문에 유효하지 않다. 그러나 `(a: 10, b: (a: 1, x: 2))`는 외부 튜플과 내부 튜플에서 각각 `a`가 한 번씩 나타나므로 유효하다.

<!--
  - test: `tuple-labels-must-be-unique`

  ```swifttest
  >> let bad = (a: 10, a: 20)
  >> let good = (a: 10, b: (a: 1, x: 2))
  !$ error: cannot create a tuple with a duplicate element label
  !! let bad = (a: 10, a: 20)
  !! ^
  ```
-->

튜플 표현식은 표현식이 없거나, 두 개 이상의 표현식을 포함할 수 있다. 괄호 안에 단일 표현식이 있는 경우, 이는 괄호로 둘러싸인 표현식으로 간주된다.

> 참고: Swift에서 빈 튜플 표현식과 빈 튜플 타입은 모두 `()`로 표기한다. `Void`는 `()`의 타입 별칭이므로, 이를 사용해 빈 튜플 타입을 작성할 수 있다. 그러나 모든 타입 별칭과 마찬가지로 `Void`는 항상 타입이므로, 빈 튜플 표현식을 작성하는 데 사용할 수는 없다.

> 튜플 표현식 문법:
>
> *tuple-expression* → **`(`** **`)`** | **`(`** *tuple-element* **`,`** *tuple-element-list* **`)`** \
> *tuple-element-list* → *tuple-element* | *tuple-element* **`,`** *tuple-element-list* \
> *tuple-element* → *expression* | *identifier* **`:`** *expression*


### 와일드카드 표현식

와일드카드 표현식은 할당 과정에서 특정 값을 명시적으로 무시할 때 사용한다. 예를 들어, 다음 할당에서 10은 `x`에 할당되고 20은 무시된다:

```swift
(x, _) = (10, 20)
// x는 10이고, 20은 무시됨
```

<!--
  - test: `wildcardTuple`

  ```swifttest
  >> var (x, _) = (10, 20)
  -> (x, _) = (10, 20)
  -> // x는 10이고, 20은 무시됨
  ```
-->

> 와일드카드 표현식 문법:
>
> *wildcard-expression* → **`_`**


### 매크로 확장 표현식

매크로 확장 표현식은 매크로 이름과 그 뒤에 쉼표로 구분된 매크로 인자 목록을 괄호로 감싸서 구성한다. 이 매크로는 컴파일 시점에 확장된다. 매크로 확장 표현식은 다음과 같은 형태를 가진다:

```swift
<#macro name#>(<#macro argument 1#>, <#macro argument 2#>)
```

매크로가 인자를 받지 않는 경우, 매크로 이름 뒤의 괄호를 생략할 수 있다.

매크로 확장 표현식은 매개변수의 기본값으로 사용할 수 있다. 함수나 메서드 매개변수의 기본값으로 사용될 때, 매크로는 함수 정의 내부가 아닌 호출 지점의 소스 코드 위치를 기준으로 평가된다. 그러나 기본값이 더 큰 표현식이고, 그 안에 다른 코드와 함께 매크로가 포함된 경우, 해당 매크로는 함수 정의 내부에서 평가된다.

```swift
func f(a: Int = #line, b: Int = (#line), c: Int = 100 + #line) {
    print(a, b, c)
}
f()  // "4 1 101" 출력
```

위 함수에서 `a`의 기본값은 단일 매크로 표현식이므로, 이 매크로는 `f(a:b:c:)`가 호출된 소스 코드 위치를 기준으로 평가된다. 반면, `b`와 `c`의 값은 매크로를 포함한 표현식이므로, 이 매크로들은 `f(a:b:c:)`가 정의된 위치를 기준으로 평가된다.

매크로를 기본값으로 사용할 때, 매크로를 확장하지 않고 타입 검사를 수행하여 다음 요구사항을 확인한다:

- 매크로의 접근 레벨은 이를 사용하는 함수와 동일하거나 더 제한적이어야 한다.
- 매크로는 인자를 받지 않거나, 인자가 문자열 보간 없이 리터럴이어야 한다.
- 매크로의 반환 타입은 매개변수의 타입과 일치해야 한다.

매크로 표현식은 독립형 매크로를 호출할 때 사용한다. 부착형 매크로를 호출하려면 <doc:Attributes>에서 설명한 커스텀 속성 문법을 사용한다. 독립형과 부착형 매크로는 다음과 같이 확장된다:

1. Swift는 소스 코드를 파싱하여 추상 구문 트리(AST)를 생성한다.
2. 매크로 구현은 AST 노드를 입력으로 받아 해당 매크로가 필요한 변환을 수행한다.
3. 매크로 구현이 생성한 변환된 AST 노드가 원본 AST에 추가된다.

각 매크로의 확장은 독립적이고 자체적으로 이루어진다. 그러나 성능 최적화를 위해 Swift는 매크로를 구현하는 외부 프로세스를 시작하고 동일한 프로세스를 재사용하여 여러 매크로를 확장할 수 있다. 매크로를 구현할 때, 이전에 확장한 매크로나 현재 시간과 같은 외부 상태에 의존해서는 안 된다.

중첩된 매크로와 여러 역할을 가진 부착형 매크로의 경우, 확장 프로세스가 반복된다. 중첩된 매크로 확장 표현식은 외부에서 내부로 확장된다. 예를 들어, 아래 코드에서 `outerMacro(_:)`가 먼저 확장되고, `innerMacro(_:)`에 대한 확장되지 않은 호출은 `outerMacro(_:)`가 입력으로 받는 추상 구문 트리에 나타난다.

```swift
#outerMacro(12, #innerMacro(34), "some text")
```

여러 역할을 가진 부착형 매크로는 각 역할에 대해 한 번씩 확장된다. 각 확장은 동일한 원본 AST를 입력으로 받는다. Swift는 생성된 모든 AST 노드를 수집하고 AST의 해당 위치에 배치하여 전체 확장을 구성한다.

Swift에서 매크로에 대한 개요는 <doc:Macros>를 참조한다.

> 매크로 확장 표현식 문법:
>
> *macro-expansion-expression* → **`#`** *identifier* *generic-argument-clause*_?_ *function-call-argument-clause*_?_ *trailing-closures*_?_


### 키 경로 표현식

*키 경로 표현식*은 타입의 프로퍼티나 서브스크립트를 참조한다. 키-값 관찰과 같은 동적 프로그래밍 작업에서 키 경로 표현식을 사용한다. 키 경로 표현식은 다음과 같은 형태를 가진다:

```swift
\<#타입 이름#>.<#경로#>
```

*타입 이름*은 `String`, `[Int]`, `Set<Int>`와 같은 구체적인 타입의 이름을 나타낸다. 이 타입 이름은 제네릭 매개변수를 포함할 수 있다.

*경로*는 프로퍼티 이름, 서브스크립트, 옵셔널 체이닝 표현식, 강제 언래핑 표현식으로 구성된다. 이 키 경로 구성 요소들은 필요한 만큼 반복해서 사용할 수 있으며, 순서도 자유롭게 조합할 수 있다.

컴파일 시점에 키 경로 표현식은 [`KeyPath`](https://developer.apple.com/documentation/swift/keypath) 클래스의 인스턴스로 대체된다.

키 경로를 사용해 값을 접근하려면, 모든 타입에서 사용 가능한 `subscript(keyPath:)` 서브스크립트에 키 경로를 전달한다. 예를 들어:

```swift
struct SomeStructure {
    var someValue: Int
}

let s = SomeStructure(someValue: 12)
let pathToProperty = \SomeStructure.someValue

let value = s[keyPath: pathToProperty]
// value는 12
```

타입 추론이 가능한 경우 *타입 이름*을 생략할 수 있다. 다음 코드는 `\SomeClass.someProperty` 대신 `\.someProperty`를 사용한다:

```swift
class SomeClass: NSObject {
    @objc dynamic var someProperty: Int
    init(someProperty: Int) {
        self.someProperty = someProperty
    }
}

let c = SomeClass(someProperty: 10)
c.observe(\.someProperty) { object, change in
    // ...
}
```

*경로*는 `self`를 참조해 아이덴티티 키 경로(`\.self`)를 생성할 수 있다. 아이덴티티 키 경로는 인스턴스 전체를 참조하므로, 변수에 저장된 모든 데이터를 한 번에 접근하거나 변경할 때 사용할 수 있다. 예를 들어:

```swift
var compoundValue = (a: 1, b: 2)
// compoundValue = (a: 10, b: 20)과 동일
compoundValue[keyPath: \.self] = (a: 10, b: 20)
```

*경로*는 프로퍼티의 프로퍼티 값을 참조하기 위해 여러 프로퍼티 이름을 점으로 구분해 포함할 수 있다. 다음 코드는 `\OuterStructure.outer.someValue` 키 경로 표현식을 사용해 `OuterStructure` 타입의 `outer` 프로퍼티의 `someValue` 프로퍼티에 접근한다:

```swift
struct OuterStructure {
    var outer: SomeStructure
    init(someValue: Int) {
        self.outer = SomeStructure(someValue: someValue)
    }
}

let nested = OuterStructure(someValue: 24)
let nestedKeyPath = \OuterStructure.outer.someValue

let nestedValue = nested[keyPath: nestedKeyPath]
// nestedValue는 24
```

*경로*는 서브스크립트의 매개변수 타입이 `Hashable` 프로토콜을 준수하는 경우, 대괄호를 사용해 서브스크립트를 포함할 수 있다. 다음 예제는 키 경로에서 서브스크립트를 사용해 배열의 두 번째 요소에 접근한다:

```swift
let greetings = ["hello", "hola", "bonjour", "안녕"]
let myGreeting = greetings[keyPath: \[String].[1]]
// myGreeting은 'hola'
```

서브스크립트에서 사용하는 값은 명명된 값이거나 리터럴일 수 있다. 값은 값 의미론을 사용해 키 경로에 캡처된다. 다음 코드는 `index` 변수를 키 경로 표현식과 클로저에서 모두 사용해 `greetings` 배열의 세 번째 요소에 접근한다. `index`가 수정되면, 키 경로 표현식은 여전히 세 번째 요소를 참조하지만, 클로저는 새로운 인덱스를 사용한다.

```swift
var index = 2
let path = \[String].[index]
let fn: ([String]) -> String = { strings in strings[index] }

print(greetings[keyPath: path])
// "bonjour" 출력
print(fn(greetings))
// "bonjour" 출력

// 'index'를 새로운 값으로 설정해도 'path'에는 영향을 미치지 않음
index += 1
print(greetings[keyPath: path])
// "bonjour" 출력

// 'fn'은 'index'를 캡처하므로 새로운 값을 사용
print(fn(greetings))
// "안녕" 출력
```

*경로*는 옵셔널 체이닝과 강제 언래핑을 사용할 수 있다. 다음 코드는 키 경로에서 옵셔널 체이닝을 사용해 옵셔널 문자열의 프로퍼티에 접근한다:

```swift
let firstGreeting: String? = greetings.first
print(firstGreeting?.count as Any)
// "Optional(5)" 출력

// 키 경로를 사용해 같은 작업 수행
let count = greetings[keyPath: \[String].first?.count]
print(count as Any)
// "Optional(5)" 출력
```

키 경로의 구성 요소를 혼합해 타입 내부에 깊이 중첩된 값에 접근할 수 있다. 다음 코드는 이러한 구성 요소를 조합한 키 경로 표현식을 사용해 배열 딕셔너리의 다양한 값과 프로퍼티에 접근한다.

```swift
let interestingNumbers = ["prime": [2, 3, 5, 7, 11, 13, 17],
                          "triangular": [1, 3, 6, 10, 15, 21, 28],
                          "hexagonal": [1, 6, 15, 28, 45, 66, 91]]
print(interestingNumbers[keyPath: \[String: [Int]].["prime"]] as Any)
// "Optional([2, 3, 5, 7, 11, 13, 17])" 출력
print(interestingNumbers[keyPath: \[String: [Int]].["prime"]![0]])
// "2" 출력
print(interestingNumbers[keyPath: \[String: [Int]].["hexagonal"]!.count])
// "7" 출력
print(interestingNumbers[keyPath: \[String: [Int]].["hexagonal"]!.count.bitWidth])
// "64" 출력
```

일반적으로 함수나 클로저를 제공하는 컨텍스트에서 키 경로 표현식을 사용할 수 있다. 특히, 루트 타입이 `SomeType`이고 경로가 `Value` 타입의 값을 생성하는 키 경로 표현식을 `(SomeType) -> Value` 타입의 함수나 클로저 대신 사용할 수 있다.

```swift
struct Task {
    var description: String
    var completed: Bool
}
var toDoList = [
    Task(description: "Practice ping-pong.", completed: false),
    Task(description: "Buy a pirate costume.", completed: true),
    Task(description: "Visit Boston in the Fall.", completed: false),
]

// 아래 두 접근 방식은 동일함
let descriptions = toDoList.filter(\.completed).map(\.description)
let descriptions2 = toDoList.filter { $0.completed }.map { $0.description }
```

키 경로 표현식의 부수 효과는 표현식이 평가되는 시점에만 평가된다. 예를 들어, 키 경로 표현식 내부의 서브스크립트에서 함수를 호출하면, 표현식 평가 시점에 한 번만 호출되며, 키 경로를 사용할 때마다 호출되지 않는다.

```swift
func makeIndex() -> Int {
    print("Made an index")
    return 0
}
// 아래 줄에서 makeIndex() 호출
let taskKeyPath = \[Task][makeIndex()]
// "Made an index" 출력

// taskKeyPath를 사용해도 makeIndex()는 다시 호출되지 않음
let someTask = toDoList[keyPath: taskKeyPath]
```

Objective-C API와 상호작용하는 코드에서 키 경로를 사용하는 방법에 대한 자세한 내용은 [Using Objective-C Runtime Features in Swift](https://developer.apple.com/documentation/swift/using_objective_c_runtime_features_in_swift)를 참고한다. 키-값 코딩과 키-값 관찰에 대한 정보는 [Key-Value Coding Programming Guide](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)와 [Key-Value Observing Programming Guide](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i)를 참고한다.

> 키 경로 표현식 문법:
>
> *key-path-expression* → **`\`** *type*_?_ **`.`** *key-path-components* \
> *key-path-components* → *key-path-component* | *key-path-component* **`.`** *key-path-components* \
> *key-path-component* → *identifier* *key-path-postfixes*_?_ | *key-path-postfixes*
>
> *key-path-postfixes* → *key-path-postfix* *key-path-postfixes*_?_ \
> *key-path-postfix* → **`?`** | **`!`** | **`self`** | **`[`** *function-call-argument-list* **`]`**


### 셀렉터 표현식

셀렉터 표현식은 Objective-C에서 메서드나 프로퍼티의 getter 또는 setter를 참조할 때 사용한다. 이 표현식은 다음과 같은 형태를 가진다:

```swift
#selector(<#method name#>)
#selector(getter: <#property name#>)
#selector(setter: <#property name#>)
```

여기서 *method name*과 *property name*은 Objective-C 런타임에서 사용 가능한 메서드나 프로퍼티를 참조해야 한다. 셀렉터 표현식의 값은 `Selector` 타입의 인스턴스다. 예를 들어:

```swift
class SomeClass: NSObject {
    @objc let property: String

    @objc(doSomethingWithInt:)
    func doSomething(_ x: Int) { }

    init(property: String) {
        self.property = property
    }
}
let selectorForMethod = #selector(SomeClass.doSomething(_:))
let selectorForPropertyGetter = #selector(getter: SomeClass.property)
```

<!--
  - test: `selector-expression`

  ```swifttest
  >> import Foundation
  -> class SomeClass: NSObject {
  ->     @objc let property: String

  ->     @objc(doSomethingWithInt:)
         func doSomething(_ x: Int) { }

         init(property: String) {
             self.property = property
         }
     }
  -> let selectorForMethod = #selector(SomeClass.doSomething(_:))
  -> let selectorForPropertyGetter = #selector(getter: SomeClass.property)
  ```
-->

프로퍼티의 getter에 대한 셀렉터를 생성할 때, *property name*은 변수나 상수 프로퍼티를 참조할 수 있다. 반면, setter에 대한 셀렉터를 생성할 때는 *property name*이 반드시 변수 프로퍼티를 참조해야 한다.

*method name*은 그룹화를 위해 괄호를 포함할 수 있으며, `as` 연산자를 사용해 이름은 같지만 타입 시그니처가 다른 메서드를 명확히 구분할 수 있다. 예를 들어:

```swift
extension SomeClass {
    @objc(doSomethingWithString:)
    func doSomething(_ x: String) { }
}
let anotherSelector = #selector(SomeClass.doSomething(_:) as (SomeClass) -> (String) -> Void)
```

<!--
  - test: `selector-expression-with-as`

  ```swifttest
  >> import Foundation
  >> class SomeClass: NSObject {
  >>     @objc let property: String
  >>     @objc(doSomethingWithInt:)
  >>     func doSomething(_ x: Int) {}
  >>     init(property: String) {
  >>         self.property = property
  >>     }
  >> }
  -> extension SomeClass {
  ->     @objc(doSomethingWithString:)
         func doSomething(_ x: String) { }
     }
  -> let anotherSelector = #selector(SomeClass.doSomething(_:) as (SomeClass) -> (String) -> Void)
  ```
-->

셀렉터는 런타임이 아닌 컴파일 타임에 생성되기 때문에, 컴파일러는 메서드나 프로퍼티가 존재하는지, 그리고 Objective-C 런타임에 노출되어 있는지 확인할 수 있다.

> 참고: *method name*과 *property name*은 표현식이지만, 실제로 평가되지는 않는다.

Swift 코드에서 Objective-C API와 상호작용할 때 셀렉터를 사용하는 방법에 대한 자세한 내용은 [Using Objective-C Runtime Features in Swift](https://developer.apple.com/documentation/swift/using_objective_c_runtime_features_in_swift)를 참고하라.

> 셀렉터 표현식 문법:
>
> *selector-expression* → **`#selector`** **`(`** *expression* **`)`** \
> *selector-expression* → **`#selector`** **`(`** **`getter:`** *expression* **`)`** \
> *selector-expression* → **`#selector`** **`(`** **`setter:`** *expression* **`)`**

<!--
  Note: The parser does allow an arbitrary expression inside #selector(), not
  just a member name.  For example, see changes in Swift commit ef60d7289d in
  lib/Sema/CSApply.cpp -- there's explicit code to look through parens and
  optional binding.
-->


### 키 경로 문자열 표현식

키 경로 문자열 표현식은 Objective-C에서 프로퍼티를 참조하기 위해 사용되는 문자열에 접근할 수 있게 해준다. 이 표현식은 키-값 코딩과 키-값 관찰 API에서 사용된다. 표현식의 형태는 다음과 같다:

```swift
#keyPath(<#property name#>)
```

여기서 *property name*은 Objective-C 런타임에서 사용 가능한 프로퍼티를 참조해야 한다. 컴파일 시점에 키 경로 문자열 표현식은 문자열 리터럴로 대체된다. 예를 들어:

```swift
class SomeClass: NSObject {
    @objc var someProperty: Int
    init(someProperty: Int) {
       self.someProperty = someProperty
    }
}

let c = SomeClass(someProperty: 12)
let keyPath = #keyPath(SomeClass.someProperty)

if let value = c.value(forKey: keyPath) {
    print(value)
}
// Prints "12"
```

<!--
  - test: `keypath-string-expression`

  ```swifttest
  >> import Foundation
  -> class SomeClass: NSObject {
  ->    @objc var someProperty: Int
        init(someProperty: Int) {
            self.someProperty = someProperty
        }
     }

  -> let c = SomeClass(someProperty: 12)
  -> let keyPath = #keyPath(SomeClass.someProperty)

  -> if let value = c.value(forKey: keyPath) {
  ->     print(value)
  -> }
  <- 12
  ```
-->

클래스 내부에서 키 경로 문자열 표현식을 사용할 때는 클래스 이름 없이 프로퍼티 이름만으로 참조할 수 있다.

```swift
extension SomeClass {
    func getSomeKeyPath() -> String {
        return #keyPath(someProperty)
    }
}
print(keyPath == c.getSomeKeyPath())
// Prints "true"
```

<!--
  - test: `keypath-string-expression`

  ```swifttest
  -> extension SomeClass {
        func getSomeKeyPath() -> String {
           return #keyPath(someProperty)
        }
     }
  -> print(keyPath == c.getSomeKeyPath())
  <- true
  ```
-->

키 경로 문자열은 런타임이 아닌 컴파일 시점에 생성되므로, 컴파일러는 프로퍼티가 존재하는지와 Objective-C 런타임에 노출되어 있는지 확인할 수 있다.

Swift 코드에서 Objective-C API와 상호작용할 때 키 경로를 사용하는 방법에 대한 더 자세한 정보는 [Using Objective-C Runtime Features in Swift](https://developer.apple.com/documentation/swift/using_objective_c_runtime_features_in_swift)를 참고하라. 키-값 코딩과 키-값 관찰에 대한 정보는 [Key-Value Coding Programming Guide](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)와 [Key-Value Observing Programming Guide](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i)를 참고하라.

> 참고: *property name*은 표현식이지만, 실제로 평가되지는 않는다.

> 키 경로 문자열 표현식 문법:
>
> *key-path-string-expression* → **`#keyPath`** **`(`** *expression* **`)`**


## 후위 표현식

*후위 표현식*은 후위 연산자나 다른 후위 문법을 표현식에 적용하여 형성된다. 문법적으로 모든 기본 표현식은 후위 표현식이기도 하다.

이 연산자들의 동작에 대한 자세한 내용은 <doc:BasicOperators>와 <doc:AdvancedOperators>를 참고한다. Swift 표준 라이브러리에서 제공하는 연산자에 대한 정보는 [Operator Declarations](https://developer.apple.com/documentation/swift/operator_declarations)에서 확인할 수 있다.

> 후위 표현식 문법:
>
> *postfix-expression* → *primary-expression* \
> *postfix-expression* → *postfix-expression* *postfix-operator* \
> *postfix-expression* → *function-call-expression* \
> *postfix-expression* → *initializer-expression* \
> *postfix-expression* → *explicit-member-expression* \
> *postfix-expression* → *postfix-self-expression* \
> *postfix-expression* → *subscript-expression* \
> *postfix-expression* → *forced-value-expression* \
> *postfix-expression* → *optional-chaining-expression*


### 함수 호출 표현식

<!--
  TODO: 함수 선언 부분을 다시 작성한 후,
  이 섹션을 다시 검토해서 용어가 일치하는지 확인하자.
-->

*함수 호출 표현식*은 함수 이름과 괄호 안에 쉼표로 구분된 인자 목록으로 구성된다. 함수 호출 표현식은 다음과 같은 형태를 가진다.

```swift
<#함수 이름#>(<#인자 값 1#>, <#인자 값 2#>)
```

*함수 이름*은 함수 타입의 값을 가진 어떤 표현식이라도 가능하다.

함수 정의에서 매개변수 이름을 포함한 경우, 함수 호출 시 인자 값 앞에 콜론(`:`)으로 구분된 이름을 포함해야 한다. 이 경우 함수 호출 표현식은 다음과 같은 형태를 가진다.

```swift
<#함수 이름#>(<#인자 이름 1#>: <#인자 값 1#>, <#인자 이름 2#>: <#인자 값 2#>)
```

함수 호출 표현식은 닫는 괄호 바로 뒤에 클로저 표현식을 추가하는 방식으로 트레일링 클로저를 포함할 수 있다. 트레일링 클로저는 함수의 인자로 간주되며, 마지막 괄호 안의 인자 뒤에 추가된다. 첫 번째 클로저 표현식은 레이블이 없으며, 추가 클로저 표현식은 해당 인자 레이블이 앞에 붙는다. 아래 예제는 트레일링 클로저 구문을 사용한 경우와 사용하지 않은 경우의 동등한 함수 호출을 보여준다.

```swift
// someFunction은 정수와 클로저를 인자로 받음
someFunction(x: x, f: { $0 == 13 })
someFunction(x: x) { $0 == 13 }

// anotherFunction은 정수와 두 개의 클로저를 인자로 받음
anotherFunction(x: x, f: { $0 == 13 }, g: { print(99) })
anotherFunction(x: x) { $0 == 13 } g: { print(99) }
```

<!--
  - test: `trailing-closure`

  ```swifttest
  >> func someFunction (x: Int, f: (Int) -> Bool) -> Bool {
  >>    return f(x)
  >> }
  >> let x = 10
  // someFunction은 정수와 클로저를 인자로 받음
  >> let r0 =
  -> someFunction(x: x, f: { $0 == 13 })
  >> assert(r0 == false)
  >> let r1 =
  -> someFunction(x: x) { $0 == 13 }
  >> assert(r1 == false)

  >> func anotherFunction(x: Int, f: (Int) -> Bool, g: () -> Void) -> Bool {
  >>    g(); return f(x)
  >> }
  // anotherFunction은 정수와 두 개의 클로저를 인자로 받음
  >> let r2 =
  -> anotherFunction(x: x, f: { $0 == 13 }, g: { print(99) })
  << 99
  >> assert(r2 == false)
  >> let r3 =
  -> anotherFunction(x: x) { $0 == 13 } g: { print(99) }
  << 99
  >> assert(r3 == false)
  ```
-->

<!--
  위 내용을 다시 작성해서 표현식이 노출되지 않도록 하자.
  추적 버그는 <rdar://problem/35301593>
-->

트레일링 클로저가 함수의 유일한 인자인 경우, 괄호를 생략할 수 있다.

```swift
// someMethod는 클로저를 유일한 인자로 받음
myData.someMethod() { $0 == 13 }
myData.someMethod { $0 == 13 }
```

<!--
  - test: `no-paren-trailing-closure`

  ```swifttest
  >> class Data {
  >>    let data = 10
  >>    func someMethod(f: (Int) -> Bool) -> Bool {
  >>       return f(self.data)
  >>    }
  >> }
  >> let myData = Data()
  // someMethod는 클로저를 유일한 인자로 받음
  >> let r0 =
  -> myData.someMethod() { $0 == 13 }
  >> assert(r0 == false)
  >> let r1 =
  -> myData.someMethod { $0 == 13 }
  >> assert(r1 == false)
  ```
-->

<!--
  위 내용을 다시 작성해서 표현식이 노출되지 않도록 하자.
  추적 버그는 <rdar://problem/35301593>
-->

트레일링 클로저를 인자에 포함시키기 위해, 컴파일러는 함수의 매개변수를 왼쪽에서 오른쪽으로 다음과 같이 검사한다.

| 트레일링 클로저 | 매개변수 | 동작 |
| ---------------- | --------- | ------ |
| 레이블 있음 | 레이블 있음 | 레이블이 동일하면 클로저가 매개변수와 매치된다. 그렇지 않으면 매개변수를 건너뛴다. |
| 레이블 있음 | 레이블 없음 | 매개변수를 건너뛴다. |
| 레이블 없음 | 레이블 있거나 없음 | 매개변수가 아래 정의된 함수 타입과 구조적으로 유사하면 클로저가 매개변수와 매치된다. 그렇지 않으면 매개변수를 건너뛴다. |

트레일링 클로저는 매치된 매개변수에 대한 인자로 전달된다. 검사 과정에서 건너뛴 매개변수는 인자가 전달되지 않는다. 예를 들어 기본 매개변수 값을 사용할 수 있다. 매치를 찾은 후, 다음 트레일링 클로저와 다음 매개변수로 검사를 계속한다. 매칭 과정이 끝나면 모든 트레일링 클로저가 매치되어야 한다.

매개변수가 *구조적으로 함수 타입과 유사*하다는 것은 매개변수가 in-out 매개변수가 아니고, 다음 중 하나인 경우를 말한다.

- 함수 타입인 매개변수, 예: `(Bool) -> Int`
- 래핑된 표현식의 타입이 함수 타입인 autoclosure 매개변수, 예: `@autoclosure () -> ((Bool) -> Int)`
- 배열 요소 타입이 함수 타입인 가변 인자 매개변수, 예: `((Bool) -> Int)...`
- 옵셔널로 래핑된 타입인 매개변수, 예: `Optional<(Bool) -> Int>`
- 허용된 타입을 조합한 타입인 매개변수, 예: `(Optional<(Bool) -> Int>)...`

트레일링 클로저가 함수 타입과 구조적으로 유사하지만 함수가 아닌 매개변수와 매치될 때, 클로저는 필요에 따라 래핑된다. 예를 들어 매개변수의 타입이 옵셔널 타입인 경우, 클로저는 자동으로 `Optional`로 래핑된다.

<!--
  - test: `when-can-you-use-trailing-closure`

  ```swifttest
  // 위에서 "구조적으로 유사"를 설명할 때 사용한 예제 타입과 일치하는 테스트

  >> func f1(x: Int, y: (Bool)->Int) { print(x + y(true)) }
  >> f1(x: 10) { $0 ? 1 : 100 }
  << 11
  >> func f2(x: Int, y: @autoclosure ()->((Bool)->Int)) { print(x + y()(false)) }
  >> f2(x: 20) { $0 ? 2 : 200 }
  << 220
  >> func f3(x: Int, y: ((Bool)->Int)...) { print(x + y[0](true)) }
  >> f3(x: 30) { $0 ? 3 : 300}
  << 33
  >> func f4(x: Int, y: Optional<(Bool)->Int>) { print(x + y!(false)) }
  >> f4(x: 40) { $0 ? 4 : 400 }
  << 440
  >> func f5(x: Int, y: (Optional<(Bool) -> Int>)...) { print(x + y[0]!(true)) }
  >> f5(x: 50) { $0 ? 5 : 500 }
  << 55
  ```
-->

Swift 5.3 이전 버전에서 오른쪽에서 왼쪽으로 매칭을 수행했던 코드의 마이그레이션을 쉽게 하기 위해, 컴파일러는 왼쪽에서 오른쪽과 오른쪽에서 왼쪽 두 가지 순서로 검사한다. 두 방향의 검사 결과가 다르면 이전의 오른쪽에서 왼쪽 순서를 사용하고 컴파일러는 경고를 생성한다. 향후 Swift 버전에서는 항상 왼쪽에서 오른쪽 순서를 사용할 것이다.

```swift
typealias Callback = (Int) -> Int
func someFunction(firstClosure: Callback? = nil,
                secondClosure: Callback? = nil) {
    let first = firstClosure?(10)
    let second = secondClosure?(20)
    print(first ?? "-", second ?? "-")
}

someFunction()  // "- -" 출력
someFunction { return $0 + 100 }  // 모호함
someFunction { return $0 } secondClosure: { return $0 }  // "10 20" 출력
```

<!--
  - test: `trailing-closure-scanning-direction`

  ```swifttest
  -> typealias Callback = (Int) -> Int
  -> func someFunction(firstClosure: Callback? = nil,
                     secondClosure: Callback? = nil) {
         let first = firstClosure?(10)
         let second = secondClosure?(20)
         print(first ?? "-", second ?? "-")
     }

  -> someFunction()  // "- -" 출력
  << - -
  -> someFunction { return $0 + 100 }  // 모호함
  << - 120
  !$ warning: 레이블 없는 트레일링 클로저를 역순으로 매칭하는 것은 더 이상 사용되지 않음; 'secondClosure' 레이블로 인자를 명시하세요
  !! someFunction { return $0 + 100 }  // 모호함
  !!              ^
  !!              (secondClosure:     )
  !$ note: 'someFunction(firstClosure:secondClosure:)' 선언 위치
  !! func someFunction(firstClosure: Callback? = nil,
  !!      ^
  -> someFunction { return $0 } secondClosure: { return $0 }  // "10 20" 출력
  << 10 20
  ```
-->

위 예제에서 "모호함"으로 표시된 함수 호출은 Swift 5.3에서 "- 120"을 출력하고 컴파일러 경고를 생성한다. 향후 Swift 버전에서는 “110 -”를 출력할 것이다.

<!--
  위 줄에서 스마트 따옴표가 필요함
  왜냐하면 정규식 휴리스틱이 닫는 따옴표를 잘못 처리하기 때문.
-->

클래스, 구조체, 또는 열거형 타입은 <doc:Declarations#Methods-with-Special-Names>에서 설명한 여러 메서드를 선언함으로써 함수 호출 구문에 대한 문법적 편의를 제공할 수 있다.


#### 포인터 타입으로의 암시적 변환

함수 호출 표현식에서 인자와 매개변수의 타입이 다를 경우, 컴파일러는 아래 목록에 있는 암시적 변환 중 하나를 적용해 타입을 맞추려고 한다:

- `inout SomeType`은 `UnsafePointer<SomeType>` 또는 `UnsafeMutablePointer<SomeType>`으로 변환될 수 있다.
- `inout Array<SomeType>`은 `UnsafePointer<SomeType>` 또는 `UnsafeMutablePointer<SomeType>`으로 변환될 수 있다.
- `Array<SomeType>`은 `UnsafePointer<SomeType>`으로 변환될 수 있다.
- `String`은 `UnsafePointer<CChar>`으로 변환될 수 있다.

다음 두 함수 호출은 동일한 결과를 낸다:

```swift
func unsafeFunction(pointer: UnsafePointer<Int>) {
    // ...
}
var myNumber = 1234

unsafeFunction(pointer: &myNumber)
withUnsafePointer(to: myNumber) { unsafeFunction(pointer: $0) }
```

<!--
  - test: `inout-unsafe-pointer`

  ```swifttest
  -> func unsafeFunction(pointer: UnsafePointer<Int>) {
  ->     // ...
  >>     print(pointer.pointee)
  -> }
  -> var myNumber = 1234

  -> unsafeFunction(pointer: &myNumber)
  -> withUnsafePointer(to: myNumber) { unsafeFunction(pointer: $0) }
  << 1234
  << 1234
  ```
-->

이러한 암시적 변환으로 생성된 포인터는 함수 호출이 진행되는 동안에만 유효하다. 정의되지 않은 동작을 방지하려면, 함수 호출이 끝난 후에는 절대 포인터를 유지하지 않도록 주의해야 한다.

> 참고: 배열을 암시적으로 안전하지 않은 포인터로 변환할 때, Swift는 배열의 저장 공간이 연속적이도록 필요한 경우 배열을 변환하거나 복사한다. 예를 들어, 저장 공간에 대한 API 계약이 없는 `NSArray` 서브클래스에서 `Array`로 브리징된 배열에 이 문법을 사용할 수 있다. 배열의 저장 공간이 이미 연속적임을 보장해야 한다면, 암시적 변환이 이러한 작업을 수행하지 않도록 `Array` 대신 `ContiguousArray`를 사용한다.

`withUnsafePointer(to:)`와 같은 명시적 함수 대신 `&`를 사용하면, 특히 함수가 여러 포인터 인자를 받을 때, 저수준 C 함수 호출을 더 읽기 쉽게 만들 수 있다. 하지만 다른 Swift 코드에서 함수를 호출할 때는, 안전하지 않은 API를 명시적으로 사용하는 대신 `&`를 사용하지 않는 것이 좋다.

<!--
  - test: `implicit-conversion-to-pointer`

  ```swifttest
  >> import Foundation
  >> func takesUnsafePointer(p: UnsafePointer<Int>) { }
  >> func takesUnsafeMutablePointer(p: UnsafeMutablePointer<Int>) { }
  >> func takesUnsafePointerCChar(p: UnsafePointer<CChar>) { }
  >> func takesUnsafeMutablePointerCChar(p: UnsafeMutablePointer<CChar>) { }
  >> var n = 12
  >> var array = [1, 2, 3]
  >> var nsarray: NSArray = [10, 20, 30]
  >> var bridgedNSArray = nsarray as! Array<Int>
  >> var string = "Hello"

  // bullet 1
  >> takesUnsafePointer(p: &n)
  >> takesUnsafeMutablePointer(p: &n)

  // bullet 2
  >> takesUnsafePointer(p: &array)
  >> takesUnsafeMutablePointer(p: &array)
  >> takesUnsafePointer(p: &bridgedNSArray)
  >> takesUnsafeMutablePointer(p: &bridgedNSArray)

  // bullet 3
  >> takesUnsafePointer(p: array)
  >> takesUnsafePointer(p: bridgedNSArray)

  // bullet 4
  >> takesUnsafePointerCChar(p: string)

  // invalid conversions
  >> takesUnsafeMutablePointer(p: array)
  !$ error: cannot convert value of type '[Int]' to expected argument type 'UnsafeMutablePointer<Int>'
  !! takesUnsafeMutablePointer(p: array)
  !!                              ^
  >> takesUnsafeMutablePointerCChar(p: string)
  !$ error: cannot convert value of type 'String' to expected argument type 'UnsafeMutablePointer<CChar>' (aka 'UnsafeMutablePointer<Int8>')
  !! takesUnsafeMutablePointerCChar(p: string)
  !!                                   ^
  ```
-->

> 함수 호출 표현식의 문법:
>
> *function-call-expression* → *postfix-expression* *function-call-argument-clause* \
> *function-call-expression* → *postfix-expression* *function-call-argument-clause*_?_ *trailing-closures*
>
> *function-call-argument-clause* → **`(`** **`)`** | **`(`** *function-call-argument-list* **`)`** \
> *function-call-argument-list* → *function-call-argument* | *function-call-argument* **`,`** *function-call-argument-list* \
> *function-call-argument* → *expression* | *identifier* **`:`** *expression* \
> *function-call-argument* → *operator* | *identifier* **`:`** *operator*
>
> *trailing-closures* → *closure-expression* *labeled-trailing-closures*_?_ \
> *labeled-trailing-closures* → *labeled-trailing-closure* *labeled-trailing-closures*_?_ \
> *labeled-trailing-closure* → *identifier* **`:`** *closure-expression*


### 초기화 표현식

초기화 표현식(*initializer expression*)은 타입의 초기화 메서드에 접근할 수 있게 해준다. 이 표현식은 다음과 같은 형태를 가진다:

```swift
<#expression#>.init(<#initializer arguments#>)
```

초기화 표현식은 함수 호출 표현식에서 새로운 타입의 인스턴스를 초기화할 때 사용한다. 또한, 슈퍼클래스의 초기화 메서드를 호출할 때도 사용한다.

```swift
class SomeSubClass: SomeSuperClass {
    override init() {
        // 서브클래스 초기화 로직
        super.init()
    }
}
```

<!--
  - test: `init-call-superclass`

  ```swifttest
  >> class SomeSuperClass { }
  -> class SomeSubClass: SomeSuperClass {
  ->     override init() {
  ->         // subclass initialization goes here
  ->         super.init()
  ->     }
  -> }
  ```
-->

함수와 마찬가지로, 초기화 메서드도 값으로 사용할 수 있다. 예를 들어:

```swift
// String 타입에는 여러 초기화 메서드가 있으므로 타입 어노테이션이 필요하다.
let initializer: (Int) -> String = String.init
let oneTwoThree = [1, 2, 3].map(initializer).reduce("", +)
print(oneTwoThree)
// "123" 출력
```

<!--
  - test: `init-as-value`

  ```swifttest
  // Type annotation is required because String has multiple initializers.
  -> let initializer: (Int) -> String = String.init
  -> let oneTwoThree = [1, 2, 3].map(initializer).reduce("", +)
  -> print(oneTwoThree)
  <- 123
  ```
-->

타입 이름을 직접 지정하면 초기화 표현식 없이도 해당 타입의 초기화 메서드에 접근할 수 있다. 하지만 그 외의 경우에는 반드시 초기화 표현식을 사용해야 한다.

```swift
let s1 = SomeType.init(data: 3)  // 유효
let s2 = SomeType(data: 1)       // 또한 유효

let s3 = type(of: someValue).init(data: 7)  // 유효
let s4 = type(of: someValue)(data: 5)       // 오류
```

<!--
  - test: `explicit-implicit-init`

  ```swifttest
  >> struct SomeType {
  >>     let data: Int
  >> }
  -> let s1 = SomeType.init(data: 3)  // Valid
  -> let s2 = SomeType(data: 1)       // Also valid

  >> let someValue = s1
  -> let s3 = type(of: someValue).init(data: 7)  // Valid
  -> let s4 = type(of: someValue)(data: 5)       // Error
  !$ error: initializing from a metatype value must reference 'init' explicitly
  !! let s4 = type(of: someValue)(data: 5)       // Error
  !!                              ^
  !!                              .init
  ```
-->

> 초기화 표현식의 문법:
>
> *initializer-expression* → *postfix-expression* **`.`** **`init`** \
> *initializer-expression* → *postfix-expression* **`.`** **`init`** **`(`** *argument-names* **`)`**


### 명시적 멤버 표현식

*명시적 멤버 표현식*은 이름이 있는 타입, 튜플, 모듈의 멤버에 접근할 수 있게 한다. 이 표현식은 항목과 그 멤버의 식별자 사이에 마침표(`.`)를 사용한다.

```swift
<#expression#>.<#member name#>
```

이름이 있는 타입의 멤버는 타입 선언이나 확장에서 정의한다. 예를 들어:

```swift
class SomeClass {
    var someProperty = 42
}
let c = SomeClass()
let y = c.someProperty  // 멤버 접근
```

<!--
  - test: `explicitMemberExpression`

  ```swifttest
  -> class SomeClass {
         var someProperty = 42
     }
  -> let c = SomeClass()
  -> let y = c.someProperty  // Member access
  ```
-->

튜플의 멤버는 순서대로 0부터 시작하는 정수로 암시적으로 이름이 붙는다. 예를 들어:

```swift
var t = (10, 20, 30)
t.0 = t.1
// 이제 t는 (20, 20, 30)
```

<!--
  - test: `explicit-member-expression`

  ```swifttest
  -> var t = (10, 20, 30)
  -> t.0 = t.1
  -> // Now t is (20, 20, 30)
  ```
-->

모듈의 멤버는 해당 모듈의 최상위 선언에 접근한다.

`dynamicMemberLookup` 속성으로 선언된 타입은 런타임에 조회되는 멤버를 포함한다. 이는 <doc:Attributes>에서 자세히 설명한다.

메서드나 이니셜라이저의 이름이 인자 이름만 다른 경우, 인자 이름을 괄호 안에 포함해 구분할 수 있다. 각 인자 이름 뒤에 콜론(`:`)을 붙인다. 이름이 없는 인자에는 언더스코어(`_`)를 사용한다. 오버로드된 메서드를 구분하려면 타입 어노테이션을 사용한다. 예를 들어:

```swift
class SomeClass {
    func someMethod(x: Int, y: Int) {}
    func someMethod(x: Int, z: Int) {}
    func overloadedMethod(x: Int, y: Int) {}
    func overloadedMethod(x: Int, y: Bool) {}
}
let instance = SomeClass()

let a = instance.someMethod              // 모호함
let b = instance.someMethod(x:y:)        // 명확함

let d = instance.overloadedMethod        // 모호함
let d = instance.overloadedMethod(x:y:)  // 여전히 모호함
let d: (Int, Bool) -> Void  = instance.overloadedMethod(x:y:)  // 명확함
```

<!--
  - test: `function-with-argument-names`

  ```swifttest
  -> class SomeClass {
         func someMethod(x: Int, y: Int) {}
         func someMethod(x: Int, z: Int) {}
         func overloadedMethod(x: Int, y: Int) {}
         func overloadedMethod(x: Int, y: Bool) {}
     }
  -> let instance = SomeClass()

  -> let a = instance.someMethod              // Ambiguous
  !$ error: ambiguous use of 'someMethod'
  !! let a = instance.someMethod              // Ambiguous
  !!         ^
  !$ note: found this candidate
  !!              func someMethod(x: Int, y: Int) {}
  !!                   ^
  !$ note: found this candidate
  !!              func someMethod(x: Int, z: Int) {}
  !!                   ^
  -> let b = instance.someMethod(x:y:)        // Unambiguous

  -> let d = instance.overloadedMethod        // Ambiguous
  !$ error: ambiguous use of 'overloadedMethod(x:y:)'
  !! let d = instance.overloadedMethod        // Ambiguous
  !!         ^
  !$ note: found this candidate
  !!              func overloadedMethod(x: Int, y: Int) {}
  !!                   ^
  !$ note: found this candidate
  !!              func overloadedMethod(x: Int, y: Bool) {}
  !!                   ^
  -> let d = instance.overloadedMethod(x:y:)  // Still ambiguous
  !$ error: ambiguous use of 'overloadedMethod(x:y:)'
  !!     let d = instance.overloadedMethod(x:y:)  // Still ambiguous
  !!             ^
  !$ note: found this candidate
  !!              func overloadedMethod(x: Int, y: Int) {}
  !!                   ^
  !$ note: found this candidate
  !!              func overloadedMethod(x: Int, y: Bool) {}
  !!                   ^
  -> let d: (Int, Bool) -> Void  = instance.overloadedMethod(x:y:)  // Unambiguous
  ```
-->

마침표가 줄의 시작 부분에 있으면, 암시적 멤버 표현식이 아니라 명시적 멤버 표현식의 일부로 이해된다. 예를 들어, 다음 코드는 여러 줄에 걸쳐 체인된 메서드 호출을 보여준다:

```swift
let x = [10, 3, 20, 15, 4]
    .sorted()
    .filter { $0 > 5 }
    .map { $0 * 100 }
```

<!--
  - test: `period-at-start-of-line`

  ```swifttest
  -> let x = [10, 3, 20, 15, 4]
  ->     .sorted()
  ->     .filter { $0 > 5 }
  ->     .map { $0 * 100 }
  >> print(x)
  << [1000, 1500, 2000]
  ```
-->

이 다중 줄 체인 구문을 컴파일러 제어문과 결합해 각 메서드 호출 시점을 제어할 수 있다. 예를 들어, 다음 코드는 iOS에서 다른 필터링 규칙을 사용한다:

```swift
let numbers = [10, 20, 33, 43, 50]
#if os(iOS)
    .filter { $0 < 40 }
#else
    .filter { $0 > 25 }
#endif
```

<!--
  - test: `pound-if-inside-postfix-expression`

  ```swifttest
  -> let numbers = [10, 20, 33, 43, 50]
     #if os(iOS)
         .filter { $0 < 40 }
     #else
         .filter { $0 > 25 }
     #endif
  >> print(numbers)
  << [33, 43, 50]
  ```
-->

`#if`, `#endif`, 그리고 다른 컴파일 지시문 사이에서, 조건부 컴파일 블록은 암시적 멤버 표현식과 하나 이상의 접미사를 포함해 접미사 표현식을 형성할 수 있다. 또한 다른 조건부 컴파일 블록이나 이러한 표현식과 블록의 조합을 포함할 수 있다.

이 구문은 명시적 멤버 표현식을 쓸 수 있는 모든 곳에서 사용할 수 있으며, 최상위 코드에서만 사용하는 것은 아니다.

조건부 컴파일 블록에서 `#if` 컴파일 지시문의 분기는 최소한 하나의 표현식을 포함해야 한다. 다른 분기는 비어 있을 수 있다.

<!--
  - test: `pound-if-empty-if-not-allowed`

  ```swifttest
  >> let numbers = [10, 20, 33, 43, 50]
  >> #if os(iOS)
  >> #else
  >>     .filter { $0 > 25 }
  >> #endif
  !$ error: reference to member 'filter' cannot be resolved without a contextual type
  !! .filter { $0 > 25 }
  !! ~^~~~~~
  ```
-->

<!--
  - test: `pound-if-else-can-be-empty`

  ```swifttest
  >> let numbers = [10, 20, 33, 43, 50]
  >> #if os(iOS)
  >>     .filter { $0 > 25 }
  >> #else
  >> #endif
  >> print(numbers)
  << [10, 20, 33, 43, 50]
  ```
-->

<!--
  - test: `pound-if-cant-use-binary-operators`

  ```swifttest
  >> let s = "some string"
  >> #if os(iOS)
  >>     + " on iOS"
  >> #endif
  !$ error: unary operator cannot be separated from its operand
  !! + " on iOS"
  !! ^~
  !!-
  ```
-->

> 명시적 멤버 표현식 문법:
>
> *explicit-member-expression* → *postfix-expression* **`.`** *decimal-digits* \
> *explicit-member-expression* → *postfix-expression* **`.`** *identifier* *generic-argument-clause*_?_ \
> *explicit-member-expression* → *postfix-expression* **`.`** *identifier**`(`** *argument-names* **`)`** \
> *explicit-member-expression* → *postfix-expression* *conditional-compilation-block*
>
> *argument-names* → *argument-name* *argument-names*_?_ \
> *argument-name* → *identifier* **`:`**

<!--
  The grammar for method-name doesn't include the following:
      method-name -> identifier argument-names-OPT
  because the "postfix-expression . identifier" line above already covers that case.
-->

<!--
  See grammar for initializer-expression for the related "argument name" production there.
-->


### 포스트픽스 Self 표현식

포스트픽스 `self` 표현식은 표현식이나 타입 이름 뒤에 `.self`를 붙여 구성한다. 다음과 같은 두 가지 형태가 있다:

```swift
<#expression#>.self
<#type#>.self
```

첫 번째 형태는 *표현식*의 값을 평가한다. 예를 들어, `x.self`는 `x`를 반환한다.

두 번째 형태는 *타입*의 값을 평가한다. 타입을 값으로 접근할 때 이 형태를 사용한다. 예를 들어, `SomeClass.self`는 `SomeClass` 타입 자체를 반환하므로, 타입 레벨 인자를 받는 함수나 메서드에 전달할 수 있다.

> 포스트픽스 self 표현식 문법:
>
> *postfix-self-expression* → *postfix-expression* **`.`** **`self`**


### 서브스크립트 표현식

서브스크립트 표현식은 해당 서브스크립트 선언의 getter와 setter를 사용해 서브스크립트 접근을 제공한다. 이 표현식은 다음과 같은 형태를 가진다:

```swift
<#expression#>[<#index expressions#>]
```

서브스크립트 표현식의 값을 평가하려면, *expression*의 타입에 대한 서브스크립트 getter를 호출하고, *index expressions*를 서브스크립트 매개변수로 전달한다. 값을 설정하려면 동일한 방식으로 서브스크립트 setter를 호출한다.

<!--
  TR: 콤마로 구분된 표현식 목록에 대한 인덱싱이 의도적인지, 단순한 부작용이 아닌지 확인한다.
  예를 들어, 다음과 같이 동작하는 것을 확인했다:
  (swift) class Test {
            subscript(a: Int, b: Int) -> Int { return 12 }
          }
  (swift) var t = Test()
  // t : Test = <Test instance>
  (swift) t[1, 2]
  // r0 : Int = 12
-->

서브스크립트 선언에 대한 자세한 내용은 <doc:Declarations#Protocol-Subscript-Declaration>을 참고한다.

> 서브스크립트 표현식 문법:
>
> *subscript-expression* → *postfix-expression* **`[`** *function-call-argument-list* **`]`**

<!--
  - test: `subscripts-can-take-operators`

  ```swifttest
  >> struct S {
         let x: Int
         let y: Int
         subscript(operation: (Int, Int) -> Int) -> Int {
             return operation(x, y)
         }
     }
  >> let s = S(x: 10, y: 20)
  >> assert(s[+] == 30)
  ```
-->


### 강제 언래핑 표현식

*강제 언래핑 표현식*은 `nil`이 아니라고 확신하는 옵셔널 값을 언래핑한다. 이 표현식은 다음과 같은 형태를 가진다:

```swift
<#expression#>!
```

만약 *표현식*의 값이 `nil`이 아니라면, 옵셔널 값이 언래핑되고 해당하는 비옵셔널 타입으로 반환된다. 그렇지 않으면 런타임 오류가 발생한다.

강제 언래핑 표현식으로 언래핑된 값은 수정할 수 있다. 값 자체를 변경하거나 값의 멤버에 할당하는 방식으로 수정이 가능하다. 예를 들어:

```swift
var x: Int? = 0
x! += 1
// x는 이제 1

var someDictionary = ["a": [1, 2, 3], "b": [10, 20]]
someDictionary["a"]![0] = 100
// someDictionary는 이제 ["a": [100, 2, 3], "b": [10, 20]]
```

<!--
  - test: `optional-as-lvalue`

  ```swifttest
  -> var x: Int? = 0
  -> x! += 1
  /> x is now \(x!)
  </ x is now 1

  -> var someDictionary = ["a": [1, 2, 3], "b": [10, 20]]
  -> someDictionary["a"]![0] = 100
  /> someDictionary is now \(someDictionary)
  </ someDictionary is now ["a": [100, 2, 3], "b": [10, 20]]
  ```
-->

> 강제 언래핑 표현식의 문법:
>
> *forced-value-expression* → *postfix-expression* **`!`**


### 옵셔널 체이닝 표현식

*옵셔널 체이닝 표현식*은 후위 표현식에서 옵셔널 값을 사용하기 위한 간결한 문법을 제공한다. 이 표현식은 다음과 같은 형태를 가진다:

```swift
<#expression#>?
```

후위 `?` 연산자는 표현식의 값을 변경하지 않고 옵셔널 체이닝 표현식을 만든다.

옵셔널 체이닝 표현식은 반드시 후위 표현식 내에 나타나야 하며, 후위 표현식이 특별한 방식으로 평가되도록 한다. 만약 옵셔널 체이닝 표현식의 값이 `nil`이라면, 후위 표현식의 나머지 연산들은 무시되고 전체 후위 표현식은 `nil`로 평가된다. 만약 옵셔널 체이닝 표현식의 값이 `nil`이 아니라면, 해당 값은 언래핑되어 후위 표현식의 나머지 부분을 평가하는 데 사용된다. 두 경우 모두, 후위 표현식의 값은 여전히 옵셔널 타입이다.

만약 옵셔널 체이닝 표현식을 포함한 후위 표현식이 다른 후위 표현식 내에 중첩되어 있다면, 가장 바깥쪽 표현식만 옵셔널 타입을 반환한다. 아래 예제에서 `c`가 `nil`이 아닐 때, 그 값은 언래핑되어 `.property`를 평가하는 데 사용되고, 이 값은 다시 `.performAction()`을 평가하는 데 사용된다. 전체 표현식 `c?.property.performAction()`의 값은 옵셔널 타입이다.

```swift
var c: SomeClass?
var result: Bool? = c?.property.performAction()
```

<!--
  - test: `optional-chaining`

  ```swifttest
  >> class OtherClass { func performAction() -> Bool {return true} }
  >> class SomeClass { var property: OtherClass = OtherClass() }
  -> var c: SomeClass?
  -> var result: Bool? = c?.property.performAction()
  >> assert(result == nil)
  ```
-->

다음 예제는 위의 예제를 옵셔널 체이닝 없이 구현한 경우의 동작을 보여준다.

```swift
var result: Bool?
if let unwrappedC = c {
    result = unwrappedC.property.performAction()
}
```

<!--
  - test: `optional-chaining-alt`

  ```swifttest
  >> class OtherClass { func performAction() -> Bool {return true} }
  >> class SomeClass { var property: OtherClass = OtherClass() }
  >> var c: SomeClass?
  -> var result: Bool?
  -> if let unwrappedC = c {
        result = unwrappedC.property.performAction()
     }
  ```
-->

옵셔널 체이닝 표현식의 언래핑된 값은 변경할 수 있다. 이는 값 자체를 변경하거나 값의 멤버에 할당하는 방식으로 이루어진다. 만약 옵셔널 체이닝 표현식의 값이 `nil`이라면, 할당 연산자의 오른쪽에 있는 표현식은 평가되지 않는다. 예를 들어:

```swift
func someFunctionWithSideEffects() -> Int {
    return 42  // 실제로는 부작용이 없음.
}
var someDictionary = ["a": [1, 2, 3], "b": [10, 20]]

someDictionary["not here"]?[0] = someFunctionWithSideEffects()
// someFunctionWithSideEffects는 평가되지 않음
// someDictionary는 여전히 ["a": [1, 2, 3], "b": [10, 20]]

someDictionary["a"]?[0] = someFunctionWithSideEffects()
// someFunctionWithSideEffects는 평가되고 42를 반환함
// someDictionary는 이제 ["a": [42, 2, 3], "b": [10, 20]]
```

<!--
  - test: `optional-chaining-as-lvalue`

  ```swifttest
  -> func someFunctionWithSideEffects() -> Int {
        return 42  // No actual side effects.
     }
  -> var someDictionary = ["a": [1, 2, 3], "b": [10, 20]]

  -> someDictionary["not here"]?[0] = someFunctionWithSideEffects()
  // someFunctionWithSideEffects isn't evaluated
  /> someDictionary is still \(someDictionary)
  </ someDictionary is still ["a": [1, 2, 3], "b": [10, 20]]

  -> someDictionary["a"]?[0] = someFunctionWithSideEffects()
  /> someFunctionWithSideEffects is evaluated and returns \(someFunctionWithSideEffects())
  </ someFunctionWithSideEffects is evaluated and returns 42
  /> someDictionary is now \(someDictionary)
  </ someDictionary is now ["a": [42, 2, 3], "b": [10, 20]]
  ```
-->

> 옵셔널 체이닝 표현식의 문법:
>
> *optional-chaining-expression* → *postfix-expression* **`?`**

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


