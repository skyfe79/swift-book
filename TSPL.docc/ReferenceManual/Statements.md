# 구문

표현식을 그룹화하고 실행 흐름을 제어한다.

Swift에는 세 가지 종류의 구문이 있다: 단순 구문, 컴파일러 제어 구문, 그리고 제어 흐름 구문.
단순 구문은 가장 일반적으로 사용되며 표현식이나 선언문으로 구성된다.
컴파일러 제어 구문은 프로그램이 컴파일러의 동작 방식을 변경할 수 있게 하며, 조건부 컴파일 블록과 라인 제어 구문이 포함된다.

제어 흐름 구문은 프로그램의 실행 흐름을 제어하는 데 사용된다.
Swift에는 여러 종류의 제어 흐름 구문이 있으며, 루프 구문, 분기 구문, 그리고 제어 전달 구문이 포함된다.
루프 구문은 코드 블록을 반복적으로 실행할 수 있게 한다.
분기 구문은 특정 조건이 충족될 때만 코드 블록을 실행한다.
제어 전달 구문은 코드 실행 순서를 변경하는 방법을 제공한다.
또한 Swift는 `do` 구문을 통해 스코프를 도입하고 오류를 잡아 처리할 수 있다.
`defer` 구문은 현재 스코프가 종료되기 직전에 정리 작업을 실행한다.

세미콜론(`;`)은 선택적으로 모든 구문 뒤에 올 수 있으며, 같은 줄에 여러 구문이 있을 때 구분자로 사용된다.

> 구문 문법:
>
> *구문* → *표현식* **`;`**_?_ \
> *구문* → *선언문* **`;`**_?_ \
> *구문* → *루프-구문* **`;`**_?_ \
> *구문* → *분기-구문* **`;`**_?_ \
> *구문* → *레이블-구문* **`;`**_?_ \
> *구문* → *제어-전달-구문* **`;`**_?_ \
> *구문* → *defer-구문* **`;`**_?_ \
> *구문* → *do-구문* **`;`**_?_ \
> *구문* → *컴파일러-제어-구문* \
> *구문들* → *구문* *구문들*_?_

<!--
  참고: 세미콜론 구문을 문법적 범주에서 제거했다.
  Doug에 따르면, 이들은 실제로 구문이 아니기 때문이다.
  예를 들어, 다음과 같은 코드는 불가능하다:
      if foo { ; }
  하지만 정말로 구문으로 간주된다면 가능해야 한다.
  세미콜론은 컴파일러에게 필수적이지 않다. 단지 가독성을 위해
  일부 위치에서 이를 요구하는 규칙을 추가했을 뿐이다.
-->


## 반복문

반복문은 특정 조건에 따라 코드 블록을 반복해서 실행할 수 있게 해준다. Swift는 세 가지 반복문을 제공한다: `for`-`in` 문, `while` 문, 그리고 `repeat`-`while` 문이다.

반복문의 제어 흐름은 `break` 문과 `continue` 문으로 변경할 수 있다. 이에 대한 자세한 내용은 아래 <doc:Statements#Break-Statement>와 <doc:Statements#Continue-Statement>에서 다룬다.

> 반복문 문법:
>
> *loop-statement* → *for-in-statement* \
> *loop-statement* → *while-statement* \
> *loop-statement* → *repeat-while-statement*


### For-In 문

`for`-`in` 문은 [`Sequence`](https://developer.apple.com/documentation/swift/sequence) 프로토콜을 준수하는 컬렉션(또는 모든 타입)의 각 항목에 대해 코드 블록을 한 번씩 실행할 수 있게 한다.

`for`-`in` 문은 다음과 같은 형태를 가진다:

```swift
for <#item#> in <#collection#> {
   <#statements#>
}
```

*컬렉션* 표현식에 대해 `makeIterator()` 메서드를 호출해 이터레이터 타입의 값을 얻는다. 이터레이터 타입은 [`IteratorProtocol`](https://developer.apple.com/documentation/swift/iteratorprotocol) 프로토콜을 준수하는 타입이다. 프로그램은 이터레이터의 `next()` 메서드를 호출해 루프를 시작한다. 반환된 값이 `nil`이 아니면, 그 값을 *item* 패턴에 할당하고 *statements*를 실행한 후 루프의 시작 부분으로 돌아가 실행을 계속한다. 반환된 값이 `nil`이면, 할당이나 *statements* 실행을 하지 않고 `for`-`in` 문의 실행을 종료한다.

> For-In 문의 문법:
>
> *for-in-statement* → **`for`** **`case`**_?_ *pattern* **`in`** *expression* *where-clause*_?_ *code-block*


### While 문

`while` 문은 특정 조건이 참일 동안 코드 블록을 반복적으로 실행한다.

`while` 문은 다음과 같은 형태를 가진다:

```swift
while <#조건#> {
   <#실행할 코드#>
}
```

`while` 문은 다음과 같은 순서로 실행된다:

1. **조건**을 평가한다.
   - 조건이 `true`이면 2단계로 진행한다.
   - 조건이 `false`이면 `while` 문 실행을 종료한다.
2. **실행할 코드**를 실행한 후, 다시 1단계로 돌아간다.

조건은 **실행할 코드**가 실행되기 전에 평가되므로, `while` 문 내부의 코드는 0번 이상 실행될 수 있다.

조건의 값은 `Bool` 타입이거나 `Bool`로 변환 가능한 타입이어야 한다. 또한 조건은 옵셔널 바인딩 선언일 수도 있으며, 이는 <doc:TheBasics#Optional-Binding>에서 다룬다.

> While 문의 문법:
>
> *while-statement* → **`while`** *조건-목록* *코드-블록*
>
> *조건-목록* → *조건* | *조건* **`,`** *조건-목록* \
> *조건* → *표현식* | *가용성-조건* | *케이스-조건* | *옵셔널-바인딩-조건*
>
> *케이스-조건* → **`case`** *패턴* *초기화자* \
> *옵셔널-바인딩-조건* → **`let`** *패턴* *초기화자*_?_ | **`var`** *패턴* *초기화자*_?_


### Repeat-While 문

`repeat`-`while` 문은 조건이 참인 동안 코드 블록을 한 번 이상 실행할 수 있게 해준다.

`repeat`-`while` 문은 다음과 같은 형태를 가진다:

```swift
repeat {
   <#statements#>
} while <#condition#>
```

`repeat`-`while` 문은 다음과 같은 순서로 실행된다:

1. 프로그램이 *statements*를 실행한 후, 2단계로 진행한다.
2. *condition*을 평가한다.

   - 조건이 `true`이면 1단계로 돌아간다.
   - 조건이 `false`이면 `repeat`-`while` 문 실행을 종료한다.

*condition*은 *statements*가 실행된 후에 평가되기 때문에, `repeat`-`while` 문 안의 *statements*는 최소 한 번은 실행된다.

*condition*의 값은 반드시 `Bool` 타입이거나 `Bool`로 변환 가능한 타입이어야 한다.

> repeat-while 문의 문법:
>
> *repeat-while-statement* → **`repeat`** *code-block* **`while`** *expression*


## 분기문

분기문은 프로그램이 하나 이상의 조건 값에 따라 특정 코드 부분을 실행할 수 있게 한다. 분기문에 지정된 조건 값은 프로그램이 어떻게 분기할지, 그리고 어떤 코드 블록을 실행할지를 결정한다. Swift는 세 가지 분기문을 제공한다: `if` 문, `guard` 문, 그리고 `switch` 문.

`if` 문이나 `switch` 문에서의 제어 흐름은 `break` 문에 의해 변경될 수 있으며, 이에 대한 내용은 아래 <doc:Statements#Break-Statement>에서 다룬다.

> 분기문 문법:
>
> *branch-statement* → *if-statement* \
> *branch-statement* → *guard-statement* \
> *branch-statement* → *switch-statement*


### If 문

`if` 문은 하나 이상의 조건을 평가한 결과에 따라 코드를 실행할 때 사용한다.

`if` 문에는 두 가지 기본 형태가 있다. 두 형태 모두 여는 중괄호와 닫는 중괄호가 필수적으로 필요하다.

첫 번째 형태는 조건이 참일 때만 코드를 실행한다. 형태는 다음과 같다:

```swift
if <#조건#> {
   <#실행할 코드#>
}
```

두 번째 형태는 추가적인 *else 절*을 제공한다. `else` 키워드로 시작하며, 조건이 참일 때와 거짓일 때 각각 다른 코드를 실행한다. 단일 else 절이 있는 경우, `if` 문의 형태는 다음과 같다:

```swift
if <#조건#> {
   <#조건이 참일 때 실행할 코드#>
} else {
   <#조건이 거짓일 때 실행할 코드#>
}
```

`if` 문의 else 절은 다른 `if` 문을 포함할 수 있다. 이를 통해 여러 조건을 테스트할 수 있다. 이런 방식으로 연결된 `if` 문의 형태는 다음과 같다:

```swift
if <#조건 1#> {
   <#조건 1이 참일 때 실행할 코드#>
} else if <#조건 2#> {
   <#조건 2이 참일 때 실행할 코드#>
} else {
   <#두 조건 모두 거짓일 때 실행할 코드#>
}
```

`if` 문에서 사용하는 모든 조건의 값은 `Bool` 타입이거나 `Bool`로 변환 가능한 타입이어야 한다. 조건은 또한 옵셔널 바인딩 선언일 수도 있다. 이 내용은 <doc:TheBasics#Optional-Binding>에서 다룬다.

> If 문의 문법:
>
> *if-statement* → **`if`** *condition-list* *code-block* *else-clause*_?_ \
> *else-clause* → **`else`** *code-block* | **`else`** *if-statement*


### 가드 문

`guard` 문은 하나 이상의 조건이 충족되지 않을 때 프로그램의 제어를 현재 스코프 밖으로 전달하는 데 사용한다.

`guard` 문은 다음과 같은 형태를 가진다:

```swift
guard <#조건#> else {
   <#실행문#>
}
```

`guard` 문의 조건은 `Bool` 타입이거나 `Bool`로 변환 가능한 타입이어야 한다. 조건은 옵셔널 바인딩 선언일 수도 있으며, 이는 <doc:TheBasics#Optional-Binding>에서 다룬다.

`guard` 문의 조건에서 옵셔널 바인딩 선언을 통해 할당된 상수나 변수는 가드 문이 포함된 스코프의 나머지 부분에서 사용할 수 있다.

`guard` 문의 `else` 절은 필수이며, `Never` 반환 타입을 가진 함수를 호출하거나 다음 중 하나를 사용해 가드 문의 스코프 밖으로 제어를 전달해야 한다:

- `return`
- `break`
- `continue`
- `throw`

제어 전달문에 대해서는 <doc:Statements#Control-Transfer-Statements>에서 다룬다. `Never` 반환 타입을 가진 함수에 대한 자세한 내용은 <doc:Declarations#Functions-that-Never-Return>을 참고한다.

> 가드 문 문법:
>
> *guard-statement* → **`guard`** *condition-list* **`else`** *code-block*


### Switch 문

`switch` 문은 제어 표현식의 값에 따라 특정 코드 블록을 실행할 수 있게 한다.

`switch` 문은 다음과 같은 형태를 가진다:

```swift
switch <#제어 표현식#> {
case <#패턴 1#>:
    <#구문#>
case <#패턴 2#> where <#조건#>:
    <#구문#>
case <#패턴 3#> where <#조건#>,
    <#패턴 4#> where <#조건#>:
    <#구문#>
default:
    <#구문#>
}
```

`switch` 문의 *제어 표현식*을 평가한 후, 각 `case`에 지정된 패턴과 비교한다. 일치하는 패턴이 있으면 해당 `case` 범위 내의 *구문*을 실행한다. 각 `case`의 범위는 비어 있을 수 없다. 따라서 각 `case` 레이블의 콜론(`:`) 뒤에 최소한 하나의 구문을 포함해야 한다. 만약 일치하는 `case`의 본문에서 어떤 코드도 실행하지 않으려면 단일 `break` 구문을 사용한다.

코드가 분기할 수 있는 표현식의 값은 매우 유연하다. 예를 들어, 정수나 문자와 같은 스칼라 타입의 값 외에도, 부동소수점 숫자, 문자열, 튜플, 커스텀 클래스의 인스턴스, 옵셔널 등 모든 타입의 값에 대해 분기할 수 있다. *제어 표현식*의 값은 열거형의 `case` 값과 일치하거나 특정 범위의 값에 포함되는지 확인할 수도 있다. `switch` 문에서 이러한 다양한 타입의 값을 사용하는 방법에 대한 예제는 <doc:ControlFlow#Switch>를 참조한다.

`switch` 문의 `case`는 각 패턴 뒤에 선택적으로 `where` 절을 포함할 수 있다. *where 절*은 `where` 키워드와 뒤따르는 표현식으로 구성되며, `case`의 패턴이 *제어 표현식*과 일치하는지 확인하기 전에 추가 조건을 제공한다. `where` 절이 있으면, *제어 표현식*의 값이 `case`의 패턴 중 하나와 일치하고 `where` 절의 표현식이 `true`로 평가될 때만 해당 `case` 내의 *구문*이 실행된다. 예를 들어, 아래 예제에서 *제어 표현식*은 `(1, 1)`과 같이 두 요소가 같은 값을 가진 튜플일 때만 해당 `case`와 일치한다.

```swift
case let (x, y) where x == y:
```

위 예제에서 볼 수 있듯이, `case`의 패턴은 `let` 키워드를 사용해 상수를 바인딩할 수도 있다(또한 `var` 키워드를 사용해 변수를 바인딩할 수도 있다). 이 상수(또는 변수)는 해당 `where` 절과 `case` 범위 내의 나머지 코드에서 참조할 수 있다. 만약 `case`가 제어 표현식과 일치하는 여러 패턴을 포함한다면, 모든 패턴은 동일한 상수 또는 변수 바인딩을 포함해야 하며, 각 바인딩된 변수 또는 상수는 모든 패턴에서 동일한 타입을 가져야 한다.

`switch` 문은 `default` 키워드로 시작하는 기본 `case`를 포함할 수도 있다. 기본 `case` 내의 코드는 다른 어떤 `case`도 제어 표현식과 일치하지 않을 때만 실행된다. `switch` 문은 기본 `case`를 하나만 포함할 수 있으며, 이는 `switch` 문의 끝에 위치해야 한다.

패턴 매칭 연산의 실제 실행 순서, 특히 `case` 내 패턴의 평가 순서는 지정되지 않았지만, `switch` 문의 패턴 매칭은 소스 코드에서 나타나는 순서대로 평가되는 것처럼 동작한다. 따라서 여러 `case`가 동일한 값으로 평가되는 패턴을 포함하고 있어 제어 표현식의 값과 일치할 수 있다면, 프로그램은 소스 코드 순서상 첫 번째로 일치하는 `case` 내의 코드만 실행한다.


#### Switch 문은 모든 경우를 처리해야 한다

Swift에서,  
제어 표현식의 타입이 가질 수 있는 모든 가능한 값은  
적어도 하나의 case 패턴과 일치해야 한다.  
이것이 실질적으로 불가능한 경우  
(예를 들어, 제어 표현식의 타입이 `Int`인 경우),  
요구 사항을 충족시키기 위해 default case를 추가할 수 있다.


#### 향후 열거형 케이스 전환

*비동결 열거형(nonfrozen enumeration)*은 미래에 새로운 열거형 케이스를 추가할 수 있는 특별한 종류의 열거형이다. 앱을 컴파일하고 배포한 후에도 새로운 케이스가 추가될 수 있다. 비동결 열거형을 전환할 때는 추가적인 고려가 필요하다. 라이브러리 작성자가 열거형을 비동결로 표시하면, 새로운 열거형 케이스를 추가할 권리를 보유하게 되며, 해당 열거형과 상호작용하는 모든 코드는 재컴파일 없이도 미래의 케이스를 처리할 수 있어야 한다. 라이브러리 진화 모드로 컴파일된 코드, Swift 표준 라이브러리, Apple 프레임워크의 Swift 오버레이, 그리고 C 및 Objective-C 코드는 비동결 열거형을 선언할 수 있다. 동결 및 비동결 열거형에 대한 자세한 정보는 <doc:Attributes#frozen>을 참고한다.

비동결 열거형 값을 전환할 때는, 모든 케이스에 해당하는 전환 케이스가 이미 존재하더라도 항상 기본 케이스를 포함해야 한다. 기본 케이스에 `@unknown` 속성을 적용할 수 있는데, 이는 기본 케이스가 미래에 추가될 열거형 케이스와만 매치되어야 함을 나타낸다. Swift는 기본 케이스가 컴파일 시점에 알려진 열거형 케이스와 매치될 경우 경고를 발생시킨다. 이 경고는 라이브러리 작성자가 새로운 케이스를 추가했지만, 해당 케이스에 대한 전환 케이스가 없음을 알려준다.

다음 예제는 Swift 표준 라이브러리의 [`Mirror.AncestorRepresentation`](https://developer.apple.com/documentation/swift/mirror/ancestorrepresentation) 열거형의 기존 세 가지 케이스를 전환한다. 만약 미래에 추가적인 케이스가 생기면, 컴파일러는 새로운 케이스를 고려하도록 전환문을 업데이트해야 한다는 경고를 생성한다.

```swift
let representation: Mirror.AncestorRepresentation = .generated
switch representation {
case .customized:
    print("가장 가까운 조상의 구현을 사용한다.")
case .generated:
    print("모든 조상 클래스에 대한 기본 미러를 생성한다.")
case .suppressed:
    print("모든 조상 클래스의 표현을 억제한다.")
@unknown default:
    print("이 코드가 컴파일될 때 알려지지 않은 표현을 사용한다.")
}
// "모든 조상 클래스에 대한 기본 미러를 생성한다." 출력
```

<!--
  - test: `unknown-case`

  ```swifttest
  -> let representation: Mirror.AncestorRepresentation = .generated
  -> switch representation {
     case .customized:
         print("가장 가까운 조상의 구현을 사용한다.")
     case .generated:
         print("모든 조상 클래스에 대한 기본 미러를 생성한다.")
     case .suppressed:
         print("모든 조상 클래스의 표현을 억제한다.")
  -> @unknown default:
         print("이 코드가 컴파일될 때 알려지지 않은 표현을 사용한다.")
     }
  <- 모든 조상 클래스에 대한 기본 미러를 생성한다.
  ```
-->


#### case 문 실행 후 자동으로 다음 case로 넘어가지 않음

일치하는 case 내부의 코드가 실행을 마치면, 프로그램은 `switch` 문을 빠져나간다. 프로그램 실행이 자동으로 다음 case나 default case로 넘어가지 않는다. 만약 하나의 case에서 다음 case로 실행을 이어가고 싶다면, `fallthrough` 문을 명시적으로 추가해야 한다. `fallthrough` 문은 단순히 `fallthrough` 키워드로 구성된다. `fallthrough` 문에 대한 자세한 내용은 아래 <doc:Statements#Fallthrough-Statement>를 참고한다.

> switch 문의 문법:
>
> *switch-statement* → **`switch`** *expression* **`{`** *switch-cases*_?_ **`}`** \
> *switch-cases* → *switch-case* *switch-cases*_?_ \
> *switch-case* → *case-label* *statements* \
> *switch-case* → *default-label* *statements* \
> *switch-case* → *conditional-switch-case*
>
> *case-label* → *attributes*_?_ **`case`** *case-item-list* **`:`** \
> *case-item-list* → *pattern* *where-clause*_?_ | *pattern* *where-clause*_?_ **`,`** *case-item-list* \
> *default-label* → *attributes*_?_ **`default`** **`:`**
>
> *where-clause* → **`where`** *where-expression* \
> *where-expression* → *expression*
>
> *conditional-switch-case* → *switch-if-directive-clause* *switch-elseif-directive-clauses*_?_ *switch-else-directive-clause*_?_ *endif-directive* \
> *switch-if-directive-clause* → *if-directive* *compilation-condition* *switch-cases*_?_ \
> *switch-elseif-directive-clauses* → *elseif-directive-clause* *switch-elseif-directive-clauses*_?_ \
> *switch-elseif-directive-clause* → *elseif-directive* *compilation-condition* *switch-cases*_?_ \
> *switch-else-directive-clause* → *else-directive* *switch-cases*_?_

<!--
  위 문법은 다른 모든 속성이 허용되는 곳에서 사용되는 attributes-OPT를 사용하지만,
  Swift 4.2 기준으로는 단일 속성(@unknown)만 허용된다.
-->


## 레이블 문법

루프 문, `if` 문, `switch` 문, `do` 문 앞에 *문장 레이블*을 붙일 수 있다. 문장 레이블은 레이블 이름과 바로 뒤에 오는 콜론(:)으로 구성된다. `break`와 `continue` 문과 함께 문장 레이블을 사용하면 루프 문이나 `switch` 문에서 제어 흐름을 어떻게 변경할지 명확히 지정할 수 있다. 이 내용은 아래 <doc:Statements#Break-Statement>와 <doc:Statements#Continue-Statement>에서 더 자세히 다룬다.

레이블 문의 범위는 레이블 뒤에 오는 전체 문장이다. 레이블 문을 중첩할 수 있지만, 각 레이블 이름은 고유해야 한다.

문장 레이블을 사용하는 방법에 대한 자세한 정보와 예제는 <doc:ControlFlow>의 <doc:ControlFlow#Labeled-Statements>를 참고한다.

<!--
  - test: `backtick-identifier-is-legal-label`

  ```swifttest
  -> var i = 0
  -> `return`: while i < 100 {
         i += 1
         if i == 10 {
             break `return`
         }
     }
  -> print(i)
  << 10
  ```
-->

> 레이블 문법:
>
> *labeled-statement* → *statement-label* *loop-statement* \
> *labeled-statement* → *statement-label* *if-statement* \
> *labeled-statement* → *statement-label* *switch-statement* \
> *labeled-statement* → *statement-label* *do-statement*
>
> *statement-label* → *label-name* **`:`** \
> *label-name* → *identifier*


## 제어 흐름 전환문

제어 흐름 전환문은 프로그램의 실행 순서를 변경할 수 있다. 이 문법은 특정 코드에서 다른 코드로 프로그램의 제어를 무조건적으로 전환한다. Swift는 다섯 가지 제어 흐름 전환문을 제공한다: `break` 문, `continue` 문, `fallthrough` 문, `return` 문, 그리고 `throw` 문.

> 제어 흐름 전환문 문법:
>
> *control-transfer-statement* → *break-statement* \
> *control-transfer-statement* → *continue-statement* \
> *control-transfer-statement* → *fallthrough-statement* \
> *control-transfer-statement* → *return-statement* \
> *control-transfer-statement* → *throw-statement*


### Break 문

`break` 문은 반복문, `if` 문, 또는 `switch` 문의 실행을 종료한다. `break` 문은 단독으로 `break` 키워드만 사용할 수도 있고, `break` 키워드 뒤에 문장 레이블 이름을 붙여 사용할 수도 있다. 아래 예제를 참고한다.

```swift
break
break <#label name#>
```

`break` 문 뒤에 문장 레이블 이름이 오면, 해당 레이블이 붙은 반복문, `if` 문, 또는 `switch` 문의 실행을 종료한다.

`break` 문 뒤에 문장 레이블 이름이 없으면, `switch` 문 또는 `break` 문이 포함된 가장 안쪽의 반복문 실행을 종료한다. 레이블이 없는 `break` 문은 `if` 문을 벗어나는 데 사용할 수 없다.

두 경우 모두, 프로그램의 제어는 반복문 또는 `switch` 문 다음에 오는 첫 번째 코드 라인으로 이동한다.

`break` 문 사용 예제는 <doc:ControlFlow#Break>와 <doc:ControlFlow#Labeled-Statements>를 참고한다.

> Break 문 문법:
>
> *break-statement* → **`break`** *label-name*_?_


### continue 문

`continue` 문은 현재 루프 반복의 실행을 종료하지만, 루프 자체의 실행을 멈추지는 않는다. `continue` 문은 단순히 `continue` 키워드만으로 구성될 수도 있고, `continue` 키워드 뒤에 문장 레이블 이름을 붙여 사용할 수도 있다. 아래 예제를 참고하라.

```swift
continue
continue <#label name#>
```

`continue` 문 뒤에 문장 레이블 이름이 붙으면, 해당 레이블이 지정한 루프 문의 현재 반복 실행이 종료된다. 레이블 이름이 없으면, `continue` 문이 포함된 가장 안쪽의 루프 문의 현재 반복 실행이 종료된다.

두 경우 모두 프로그램 제어는 해당 루프 문의 조건 평가 부분으로 이동한다.

`for` 문에서는 `continue` 문이 실행된 후에도 증가식이 평가된다. 이는 루프 본문 실행 후에 증가식이 평가되기 때문이다.

`continue` 문 사용 예제는 <doc:ControlFlow#Continue>와 <doc:ControlFlow#Labeled-Statements>를 참고하라.

> continue 문 문법:
>
> *continue-statement* → **`continue`** *label-name*_?_


### Fallthrough 문

`fallthrough` 문은 `fallthrough` 키워드로 구성되며, `switch` 문의 `case` 블록 내에서만 사용할 수 있다. 이 문은 `switch` 문에서 하나의 `case` 블록이 끝난 후, 다음 `case` 블록으로 실행을 이어가도록 한다. 다음 `case` 블록으로 실행이 이어지는 것은, 해당 `case` 라벨의 패턴이 `switch` 문의 제어 표현식 값과 일치하지 않더라도 마찬가지다.

`fallthrough` 문은 `switch` 문 내 어디에서나 사용할 수 있으며, 반드시 `case` 블록의 마지막 문장일 필요는 없다. 하지만, `fallthrough` 문은 마지막 `case` 블록에서는 사용할 수 없다. 또한, 값 바인딩 패턴을 포함하는 `case` 블록으로 제어를 전달할 수도 없다.

`switch` 문에서 `fallthrough` 문을 어떻게 사용하는지에 대한 예제는 <doc:ControlFlow#Control-Transfer-Statements>를 참고한다.

> Fallthrough 문의 문법:
>
> *fallthrough-statement* → **`fallthrough`**


### 반환문

반환문(`return` statement)은 함수나 메서드 정의 내부에 위치하며, 프로그램 실행을 호출한 함수나 메서드로 되돌린다. 프로그램 실행은 함수나 메서드 호출 바로 다음 지점에서 계속된다.

반환문은 `return` 키워드만으로 구성될 수도 있고, `return` 키워드 뒤에 표현식을 포함할 수도 있다. 아래 예제를 참고한다.

```swift
return
return <#expression#>
```

반환문 뒤에 표현식이 오는 경우, 해당 표현식의 값은 호출한 함수나 메서드로 반환된다. 만약 표현식의 값이 함수나 메서드 선언에서 지정한 반환 타입과 일치하지 않으면, 반환되기 전에 해당 값은 반환 타입으로 변환된다.

> 참고: <doc:Declarations#Failable-Initializers>에서 설명한 것처럼, 실패 가능한 초기화 메서드에서는 특수한 형태의 반환문(`return nil`)을 사용해 초기화 실패를 나타낼 수 있다.

<!--
  TODO: 변환이 어떻게 이루어지는지, 그리고 어떤 타입 변환이 허용되는지에 대해
  (아직 작성되지 않은) 하위 타입 및 타입 변환 장에서 다룰 예정이다.
-->

반환문 뒤에 표현식이 없는 경우, 이는 값을 반환하지 않는 함수나 메서드(즉, 반환 타입이 `Void` 또는 `()`인 경우)에서만 사용할 수 있다.

> 반환문 문법:
>
> *return-statement* → **`return`** *expression*_?_


### `throw` 구문

`throw` 구문은 에러를 던지는 함수나 메서드의 본문에서 발생한다. 또는 `throws` 키워드로 타입이 표시된 클로저 표현식의 본문에서도 사용할 수 있다.

`throw` 구문은 프로그램이 현재 스코프의 실행을 중단하고, 에러를 상위 스코프로 전파하도록 만든다. 던져진 에러는 `do` 구문의 `catch` 절에서 처리될 때까지 계속 전파된다.

`throw` 구문은 `throw` 키워드와 그 뒤에 오는 표현식으로 구성된다. 아래 예제를 참고하자.

```swift
throw <#expression#>
```

여기서 *표현식*의 값은 반드시 `Error` 프로토콜을 준수하는 타입이어야 한다. `throw` 구문을 포함하는 `do` 구문이나 함수가 던지는 에러의 타입을 명시했다면, *표현식*의 값은 해당 타입의 인스턴스여야 한다.

`throw` 구문을 사용하는 방법에 대한 예제는 <doc:ErrorHandling#Propagating-Errors-Using-Throwing-Functions>를 참고하자. 이 내용은 <doc:ErrorHandling> 문서에서 확인할 수 있다.

> `throw` 구문의 문법:
>
> *throw-statement* → **`throw`** *expression*


## defer 문

`defer` 문은 프로그램의 제어가 해당 `defer` 문이 포함된 스코프를 벗어나기 직전에 코드를 실행하기 위해 사용한다.

`defer` 문은 다음과 같은 형태를 가진다:

```swift
defer {
    <#statements#>
}
```

`defer` 문 내부의 코드는 프로그램의 제어가 어떻게 전달되든 상관없이 반드시 실행된다. 이를 통해 파일 디스크립터를 닫는 등 수동 리소스 관리를 수행하거나, 오류가 발생하더라도 반드시 실행되어야 하는 작업을 처리할 수 있다.

`defer` 문 내부의 *statements*는 해당 `defer` 문이 포함된 스코프가 끝나는 시점에 실행된다.

```swift
func f(x: Int) {
  defer { print("First defer") }

  if x < 10 {
    defer { print("Second defer") }
    print("End of if")
  }

  print("End of function")
}
f(x: 5)
// Prints "End of if"
// Prints "Second defer"
// Prints "End of function"
// Prints "First defer"
```

<!--
  ```swifttest
  -> func f(x: Int) {
    defer { print("First defer") }

    if x < 10 {
      defer { print("Second defer") }
      print("End of if")
    }

    print("End of function")
  }
  f(x: 5)
  <- End of if
  <- Second defer
  <- End of function
  <- First defer
  ```
-->

위 코드에서 `if` 문 내부의 `defer`는 함수 `f`에 선언된 `defer`보다 먼저 실행된다. 이는 `if` 문의 스코프가 함수의 스코프보다 먼저 종료되기 때문이다.

동일한 스코프 내에 여러 `defer` 문이 존재할 경우, 실행 순서는 선언된 순서의 반대가 된다. 즉, 마지막에 선언된 `defer` 문이 가장 먼저 실행된다. 이를 통해 마지막 `defer` 문 내부의 코드가 다른 `defer` 문에서 정리될 리소스를 참조할 수 있다.

```swift
func f() {
    defer { print("First defer") }
    defer { print("Second defer") }
    print("End of function")
}
f()
// Prints "End of function"
// Prints "Second defer"
// Prints "First defer"
```

<!--
  ```swifttest
  -> func f() {
         defer { print("First defer") }
         defer { print("Second defer") }
         print("End of function")
     }
     f()
  <- End of function
  <- Second defer
  <- First defer
  ```
-->

`defer` 문 내부의 코드는 프로그램의 제어를 `defer` 문 외부로 전달할 수 없다.

> defer 문의 문법:
>
> *defer-statement* → **`defer`** *code-block*


## Do 문

`do` 문은 새로운 스코프를 도입하며, 선택적으로 하나 이상의 `catch` 절을 포함할 수 있다. `catch` 절은 정의된 오류 조건과 일치하는 패턴을 포함한다. `do` 문의 스코프 내에서 선언된 변수와 상수는 해당 스코프 내에서만 접근할 수 있다.

Swift의 `do` 문은 C 언어에서 코드 블록을 구분하기 위해 사용하는 중괄호(`{}`)와 유사하며, 런타임에 성능 비용을 발생시키지 않는다.

`do` 문은 다음과 같은 형태를 가진다:

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

`do` 문은 선택적으로 발생할 수 있는 오류의 타입을 지정할 수 있으며, 이는 다음과 같은 형태를 가진다:

```swift
do throws(<#type#>) {
    try <#expression#>
} catch <#pattern> {
    <#statements#>
} catch {
    <#statements#>
}
```

`do` 문에 `throws` 절이 포함된 경우, `do` 블록은 지정된 *타입*의 오류만 발생시킬 수 있다. *타입*은 `Error` 프로토콜을 준수하는 구체적인 타입, `Error` 프로토콜을 준수하는 불투명 타입, 또는 박스화된 프로토콜 타입인 `any Error`여야 한다. `do` 문이 발생할 수 있는 오류 타입을 지정하지 않으면, Swift는 다음과 같이 오류 타입을 추론한다:

- `do` 코드 블록 내의 모든 `throws` 문과 `try` 표현식이 완전한 오류 처리 메커니즘 내에 중첩된 경우, Swift는 `do` 문이 오류를 발생시키지 않는다고 추론한다.

- `do` 코드 블록이 완전한 오류 처리 외부에서 단일 타입의 오류만 발생시키는 코드를 포함하고 있고, `Never`를 발생시키지 않는 경우, Swift는 `do` 문이 해당 구체적인 오류 타입을 발생시킨다고 추론한다.

- `do` 코드 블록이 완전한 오류 처리 외부에서 여러 타입의 오류를 발생시키는 코드를 포함하고 있는 경우, Swift는 `do` 문이 `any Error`를 발생시킨다고 추론한다.

명시적 타입의 오류를 다루는 방법에 대한 자세한 내용은 <doc:ErrorHandling#Specifying-the-Error-Type>을 참조한다.

`do` 코드 블록 내의 어떤 문장이 오류를 발생시키면, 프로그램 제어는 해당 오류와 일치하는 첫 번째 `catch` 절로 전달된다. 일치하는 절이 없으면, 오류는 주변 스코프로 전파된다. 최상위 수준에서 오류가 처리되지 않으면, 프로그램 실행은 런타임 오류와 함께 중단된다.

`switch` 문과 마찬가지로, 컴파일러는 `catch` 절이 완전한지 여부를 추론하려고 시도한다. 이러한 판단이 가능하면, 오류는 처리된 것으로 간주된다. 그렇지 않으면, 오류는 포함된 스코프 밖으로 전파될 수 있으며, 이는 오류가 포함된 `catch` 절에 의해 처리되거나 포함된 함수가 `throws`로 선언되어야 함을 의미한다.

여러 패턴을 가진 `catch` 절은 해당 패턴 중 하나라도 오류와 일치하면 오류를 처리한다. `catch` 절이 여러 패턴을 포함하는 경우, 모든 패턴은 동일한 상수 또는 변수 바인딩을 포함해야 하며, 각 바인딩된 변수 또는 상수는 `catch` 절의 모든 패턴에서 동일한 타입을 가져야 한다.

<!--
  위의 다중 패턴 catch에 대한 논의는
  Switch Statement에서의 다중 패턴 case에 대한 논의와 일치한다.
-->

오류가 처리되도록 보장하기 위해, 모든 오류와 일치하는 패턴(예: 와일드카드 패턴(`_`))을 가진 `catch` 절을 사용한다. `catch` 절이 패턴을 지정하지 않으면, `catch` 절은 모든 오류를 `error`라는 로컬 상수에 바인딩하여 처리한다. `catch` 절에서 사용할 수 있는 패턴에 대한 자세한 내용은 <doc:Patterns>를 참조한다.

여러 `catch` 절과 함께 `do` 문을 사용하는 예제를 보려면 <doc:ErrorHandling#Handling-Errors>를 참조한다.

> Do 문의 문법:
>
> *do-statement* → **`do`** *throws-clause*_?_ *code-block* *catch-clauses*_?_ \
> *catch-clauses* → *catch-clause* *catch-clauses*_?_ \
> *catch-clause* → **`catch`** *catch-pattern-list*_?_ *code-block* \
> *catch-pattern-list* → *catch-pattern* | *catch-pattern* **`,`** *catch-pattern-list* \
> *catch-pattern* → *pattern* *where-clause*_?_


## 컴파일러 제어 구문

컴파일러 제어 구문은 프로그램이 컴파일러의 동작 방식을 변경할 수 있게 한다. Swift는 세 가지 컴파일러 제어 구문을 제공한다:
조건부 컴파일 블록, 라인 제어 구문, 그리고 컴파일 타임 진단 구문이다.

> 컴파일러 제어 구문 문법:
>
> *compiler-control-statement* → *conditional-compilation-block* \
> *compiler-control-statement* → *line-control-statement* \
> *compiler-control-statement* → *diagnostic-statement*


### 조건부 컴파일 블록

조건부 컴파일 블록은 하나 이상의 컴파일 조건에 따라 코드를 조건적으로 컴파일할 수 있게 해준다.

모든 조건부 컴파일 블록은 `#if` 컴파일 지시문으로 시작하고 `#endif` 컴파일 지시문으로 끝난다. 간단한 조건부 컴파일 블록은 다음과 같은 형태를 가진다:

```swift
#if <#컴파일 조건#>
    <#구문#>
#endif
```

`if` 문의 조건과 달리, *컴파일 조건*은 컴파일 시점에 평가된다. 결과적으로, *구문*은 *컴파일 조건*이 컴파일 시점에 `true`로 평가될 때만 컴파일되고 실행된다.

*컴파일 조건*은 `true`와 `false` 불리언 리터럴, `-D` 커맨드라인 플래그와 함께 사용된 식별자, 또는 아래 표에 나열된 플랫폼 조건 중 하나를 포함할 수 있다.

| 플랫폼 조건 | 유효한 인자 |
| ----------- | ----------- |
| `os()` | `macOS`, `iOS`, `watchOS`, `tvOS`, `visionOS`, `Linux`, `Windows` |
| `arch()` | `i386`, `x86_64`, `arm`, `arm64` |
| `swift()` | `>=` 또는 `<` 뒤에 버전 번호 |
| `compiler()` | `>=` 또는 `<` 뒤에 버전 번호 |
| `canImport()` | 모듈 이름 |
| `targetEnvironment()` | `simulator`, `macCatalyst` |

<!--
  위 목록은 <https://www.swift.org/platform-support/>와 일치하며,
  *공식* 지원 플랫폼만 포함한다.
  비공식 또는 실험적 지원을 포함한 전체 운영 체제 및 아키텍처 목록은
  lib/Basic/LangOptions.cpp 파일의
  SupportedConditionalCompilationOSs와 SupportedConditionalCompilationArches 값을 참조하라.
  컴파일러는 거의 모든 문자열을 허용한다.
  예를 들어 "#if os(toaster)"는 컴파일되지만,
  Swift는 실제로 토스터 오븐에서 실행되도록 지원하지 않으므로,
  가능한 os/arch 값을 확인할 때 이에 의존하지 않도록 주의하라.
-->

<!--
  컴파일러는 "UIKitForMac"을 "macCatalyst"의 동의어로 이해하지만,
  이 철자는 몇 군데를 제외하고 "Must be removed"로 표시되어 있으므로,
  위 표에서 생략했다.
-->

`swift()`와 `compiler()` 플랫폼 조건의 버전 번호는 주 버전, 선택적 부 버전, 선택적 패치 버전 등으로 구성되며, 각 부분은 점(`.`)으로 구분된다. 비교 연산자와 버전 번호 사이에 공백이 없어야 한다. `compiler()`의 버전은 컴파일러 버전이며, 컴파일러에 전달된 Swift 버전 설정과 무관하다. `swift()`의 버전은 현재 컴파일 중인 언어 버전이다. 예를 들어, Swift 5 컴파일러를 사용하여 Swift 4.2 모드로 코드를 컴파일하면, 컴파일러 버전은 5이고 언어 버전은 4.2이다. 이 설정에서 다음 코드는 세 메시지를 모두 출력한다:

```swift
#if compiler(>=5)
print("Swift 5 컴파일러 이상으로 컴파일됨")
#endif
#if swift(>=4.2)
print("Swift 4.2 모드 이상으로 컴파일됨")
#endif
#if compiler(>=5) && swift(<5)
print("Swift 5 컴파일러 이상으로 컴파일되었지만, Swift 5 이전 모드로 컴파일됨")
#endif
// "Swift 5 컴파일러 이상으로 컴파일됨" 출력
// "Swift 4.2 모드 이상으로 컴파일됨" 출력
// "Swift 5 컴파일러 이상으로 컴파일되었지만, Swift 5 이전 모드로 컴파일됨" 출력
```

<!--
  ```swifttest
  -> #if compiler(>=5)
     print("Swift 5 컴파일러 이상으로 컴파일됨")
     #endif
     #if swift(>=4.2)
     print("Swift 4.2 모드 이상으로 컴파일됨")
     #endif
     #if compiler(>=5) && swift(<5)
     print("Swift 5 컴파일러 이상으로 컴파일되었지만, Swift 5 이전 모드로 컴파일됨")
     #endif
  <- Swift 5 컴파일러 이상으로 컴파일됨
  <- Swift 4.2 모드 이상으로 컴파일됨
  // "Swift 5 컴파일러 이상으로 컴파일되었지만, Swift 5 이전 모드로 컴파일됨" 출력
  ```
-->

<!--
  이 테스트 코드는 실제로 Swift 4.2 모드에서 실행되지 않으므로,
  명시적으로 세 번째 줄의 출력을 출력하는 방식으로 속임수를 쓴다.
-->

`canImport()` 플랫폼 조건의 인자는 모든 플랫폼에 존재하지 않을 수 있는 모듈의 이름이다. 모듈 이름에는 점(`.`)이 포함될 수 있다. 이 조건은 모듈을 임포트할 수 있는지 테스트하지만, 실제로 임포트하지는 않는다. 모듈이 존재하면 플랫폼 조건은 `true`를 반환하고, 그렇지 않으면 `false`를 반환한다.

<!--
  - test: `canImport_A, canImport`

  ```swifttest
  >> public struct SomeStruct {
  >>     public init() { }
  >> }
  ```
-->

<!--
  - test: `canImport_A.B, canImport`

  ```swifttest
  >> public struct AnotherStruct {
  >>     public init() { }
  >> }
  ```
-->

<!--
  - test: `canImport`

  ```swifttest
  >> import canImport_A
  >> let s = SomeStruct()
  >> #if canImport(canImport_A)
  >> #else
  >> #error("A를 임포트할 수 없음")
  >> #endif

  >> #if canImport(canImport_A.B)
  >> #else
  >> #error("A.B를 임포트할 수 없음")
  >> #endif
  ```
-->

`targetEnvironment()` 플랫폼 조건은 코드가 지정된 환경을 위해 컴파일될 때 `true`를 반환하고, 그렇지 않으면 `false`를 반환한다.

> 참고: `arch(arm)` 플랫폼 조건은 ARM 64 디바이스에 대해 `true`를 반환하지 않는다. `arch(i386)` 플랫폼 조건은 32비트 iOS 시뮬레이터를 위해 코드가 컴파일될 때 `true`를 반환한다.

<!--
  - test: `pound-if-swift-version`

  ```swifttest
  -> #if swift(>=2.1)
         print(1)
     #endif
  << 1
  -> #if swift(>=2.1) && true
         print(2)
     #endif
  << 2
  -> #if swift(>=2.1) && false
         print(3)
     #endif
  -> #if swift(>=2.1.9.9.9.9.9.9.9.9.9)
         print(5)
     #endif
  << 5
  ```
-->

<!--
  - test: `pound-if-swift-version-err`

  ```swifttest
  -> #if swift(>= 2.1)
         print(4)
     #endif
  !$ error: 단항 연산자는 피연산자와 분리될 수 없음
  !! #if swift(>= 2.1)
  !!           ^ ~
  !!-
  ```
-->

<!--
  - test: `pound-if-compiler-version`

  ```swifttest
  -> #if compiler(>=4.2)
         print(1)
     #endif
  << 1
  -> #if compiler(>=4.2) && true
         print(2)
     #endif
  << 2
  -> #if compiler(>=4.2) && false
         print(3)
     #endif
  ```
-->

논리 연산자 `&&`, `||`, `!`를 사용하여 컴파일 조건을 결합하거나 부정할 수 있으며, 그룹화를 위해 괄호를 사용할 수 있다. 이러한 연산자는 일반 불리언 표현식을 결합하는 데 사용되는 논리 연산자와 동일한 결합성과 우선순위를 가진다.

`if` 문과 유사하게, 여러 조건부 분기를 추가하여 서로 다른 컴파일 조건을 테스트할 수 있다. `#elseif` 절을 사용하여 원하는 만큼 추가 분기를 추가할 수 있다. 또한 `#else` 절을 사용하여 최종 추가 분기를 추가할 수 있다. 여러 분기를 포함하는 조건부 컴파일 블록은 다음과 같은 형태를 가진다:

```swift
#if <#컴파일 조건 1#>
    <#컴파일 조건 1이 true일 때 컴파일할 구문#>
#elseif <#컴파일 조건 2#>
    <#컴파일 조건 2이 true일 때 컴파일할 구문#>
#else
    <#두 컴파일 조건 모두 false일 때 컴파일할 구문#>
#endif
```

> 참고: 조건부 컴파일 블록의 각 구문은 컴파일되지 않더라도 파싱된다. 그러나 컴파일 조건에 `swift()` 또는 `compiler()` 플랫폼 조건이 포함된 경우 예외가 있다: 구문은 언어 또는 컴파일러 버전이 플랫폼 조건에 지정된 내용과 일치할 때만 파싱된다. 이 예외는 이전 버전의 컴파일러가 Swift의 새 버전에서 도입된 구문을 파싱하려고 시도하지 않도록 보장한다.

명시적 멤버 표현식을 조건부 컴파일 블록으로 감싸는 방법에 대한 자세한 내용은 <doc:Expressions#Explicit-Member-Expression>을 참조하라.

> 조건부 컴파일 블록의 문법:
>
> *conditional-compilation-block* → *if-directive-clause* *elseif-directive-clauses*_?_ *else-directive-clause*_?_ *endif-directive*
>
> *if-directive-clause* → *if-directive* *compilation-condition* *statements*_?_ \
> *elseif-directive-clauses* → *elseif-directive-clause* *elseif-directive-clauses*_?_ \
> *elseif-directive-clause* → *elseif-directive* *compilation-condition* *statements*_?_ \
> *else-directive-clause* → *else-directive* *statements*_?_ \
> *if-directive* → **`#if`** \
> *elseif-directive* → **`#elseif`** \
> *else-directive* → **`#else`** \
> *endif-directive* → **`#endif`**
>
> *compilation-condition* → *platform-condition* \
> *compilation-condition* → *identifier* \
> *compilation-condition* → *boolean-literal* \
> *compilation-condition* → **`(`** *compilation-condition* **`)`** \
> *compilation-condition* → **`!`** *compilation-condition* \
> *compilation-condition* → *compilation-condition* **`&&`** *compilation-condition* \
> *compilation-condition* → *compilation-condition* **`||`** *compilation-condition*
>
> *platform-condition* → **`os`** **`(`** *operating-system* **`)`** \
> *platform-condition* → **`arch`** **`(`** *architecture* **`)`** \
> *platform-condition* → **`swift`** **`(`** **`>=`** *swift-version* **`)`** | **`swift`** **`(`** **`<`** *swift-version* **`)`** \
> *platform-condition* → **`compiler`** **`(`** **`>=`** *swift-version* **`)`** | **`compiler`** **`(`** **`<`** *swift-version* **`)`** \
> *platform-condition* → **`canImport`** **`(`** *import-path* **`)`** \
> *platform-condition* → **`targetEnvironment`** **`(`** *environment* **`)`**
>
> *operating-system* → **`macOS`** | **`iOS`** | **`watchOS`** | **`tvOS`** | **`visionOS`** | **`Linux`** | **`Windows`** \
> *architecture* → **`i386`** | **`x86_64`** | **`arm`** | **`arm64`** \
> *swift-version* → *decimal-digits* *swift-version-continuation*_?_ \
> *swift-version-continuation* → **`.`** *decimal-digits* *swift-version-continuation*_?_ \
> *environment* → **`simulator`** | **`macCatalyst`**

<!--
  테스트 노트:

  !!true는 동작하지 않지만 !(!true)는 동작한다. 이는 일반 표현식과 일치한다.
-->


#if를 중첩해서 사용할 수 있다. 이는 일반적으로 예상되는 동작이다.

또한, 조건부 컴파일 블록의 본문에는 *0개 이상*의 문장이 포함될 수 있다. 따라서 다음과 같은 코드도 유효하다:


#if

#elseif

#else

#endif

-->


### 라인 컨트롤 구문

라인 컨트롤 구문은 컴파일 중인 소스 코드의 라인 번호와 파일명과 다른 값을 지정할 때 사용한다. 이 구문은 Swift가 진단 및 디버깅 목적으로 사용하는 소스 코드 위치를 변경한다.

라인 컨트롤 구문은 다음과 같은 형태를 가진다:

```swift
#sourceLocation(file: <#file path#>, line: <#line number#>)
#sourceLocation()
```

첫 번째 형태의 라인 컨트롤 구문은 `#line`, `#file`, `#fileID`, `#filePath` 리터럴 표현식의 값을 변경한다. 이 변경은 라인 컨트롤 구문 다음 줄부터 적용된다. *line number*는 `#line`의 값을 변경하며, 0보다 큰 정수 리터럴이어야 한다. *file path*는 `#file`, `#fileID`, `#filePath`의 값을 변경하며, 문자열 리터럴이어야 한다. 지정된 문자열은 `#filePath`의 값이 되고, 이 문자열의 마지막 경로 구성 요소는 `#fileID`의 값으로 사용된다. `#file`, `#fileID`, `#filePath`에 대한 자세한 내용은 <doc:Expressions#Literal-Expression>을 참고한다.

두 번째 형태의 라인 컨트롤 구문인 `#sourceLocation()`은 소스 코드 위치를 기본 라인 번호와 파일 경로로 재설정한다.

> 라인 컨트롤 구문 문법:
>
> *line-control-statement* → **`#sourceLocation`** **`(`** **`file:`** *file-path* **`,`** **`line:`** *line-number* **`)`** \
> *line-control-statement* → **`#sourceLocation`** **`(`** **`)`** \
> *line-number* → 0보다 큰 십진 정수 \
> *file-path* → *static-string-literal*


### 컴파일 타임 진단 문장

Swift 5.9 이전에는 `#warning`과 `#error` 문장이 컴파일 중에 진단 메시지를 출력했다. 이제는 Swift 표준 라이브러리의 [`warning(_:)`][]과 [`error(_:)`][] 매크로가 이러한 기능을 제공한다.

[`warning(_:)`]: https://developer.apple.com/documentation/swift/warning(_:)
[`error(_:)`]: https://developer.apple.com/documentation/swift/error(_:)


## 가용성 조건

*가용성 조건*은 `if`, `while`, `guard` 문에서 특정 플랫폼 인자를 기반으로 런타임에 API의 가용성을 확인하기 위해 사용한다.

가용성 조건은 다음과 같은 형태를 가진다:

```swift
if #available(<#플랫폼 이름#> <#버전#>, <#...#>, *) {
    <#API가 사용 가능할 때 실행할 코드#>
} else {
    <#API가 사용 불가능할 때 실행할 대체 코드#>
}
```

가용성 조건을 사용하면 런타임에 사용하려는 API가 사용 가능한지에 따라 코드 블록을 실행할 수 있다. 컴파일러는 가용성 조건에서 제공된 정보를 사용해 해당 코드 블록 내의 API가 사용 가능한지 확인한다.

가용성 조건은 쉼표로 구분된 플랫폼 이름과 버전 목록을 인자로 받는다. 플랫폼 이름으로 `iOS`, `macOS`, `watchOS`, `tvOS`, `visionOS`를 사용하고, 해당 버전 번호를 포함한다. `*` 인자는 필수이며, 다른 모든 플랫폼에서 가용성 조건으로 보호된 코드 블록이 타겟의 최소 배포 타겟에서 실행됨을 지정한다.

불리언 조건과 달리, 가용성 조건은 `&&`나 `||` 같은 논리 연산자로 결합할 수 없다. 또한 `!`를 사용해 가용성 조건을 부정하는 대신, 다음과 같은 형태의 *비가용성 조건*을 사용한다:

```swift
if #unavailable(<#플랫폼 이름#> <#버전#>, <#...#>) {
    <#API가 사용 불가능할 때 실행할 대체 코드#>
} else {
    <#API가 사용 가능할 때 실행할 코드#>
}
```

`#unavailable` 형태는 조건을 부정하는 문법적 설탕이다. 비가용성 조건에서는 `*` 인자가 암시적으로 포함되며, 명시적으로 포함해서는 안 된다. 이는 가용성 조건에서의 `*` 인자와 동일한 의미를 가진다.

> 가용성 조건 문법:
>
> *availability-condition* → **`#available`** **`(`** *availability-arguments* **`)`** \
> *availability-condition* → **`#unavailable`** **`(`** *availability-arguments* **`)`** \
> *availability-arguments* → *availability-argument* | *availability-argument* **`,`** *availability-arguments* \
> *availability-argument* → *platform-name* *platform-version* \
> *availability-argument* → **`*`**
>
>
>
> *platform-name* → **`iOS`** | **`iOSApplicationExtension`** \
> *platform-name* → **`macOS`** | **`macOSApplicationExtension`** \
> *platform-name* → **`macCatalyst`** | **`macCatalystApplicationExtension`** \
> *platform-name* → **`watchOS`** | **`watchOSApplicationExtension`** \
> *platform-name* → **`tvOS`** | **`tvOSApplicationExtension`** \
> *platform-name* → **`visionOS`** | **`visionOSApplicationExtension`** \
> *platform-version* → *decimal-digits* \
> *platform-version* → *decimal-digits* **`.`** *decimal-digits* \
> *platform-version* → *decimal-digits* **`.`** *decimal-digits* **`.`** *decimal-digits*

<!--
  새로운 플랫폼을 이 목록에 추가해야 한다면,
  @available 아래의 목록도 업데이트해야 할 가능성이 높다.
-->

<!--
  - test: `pound-available-platform-names`

  ```swifttest
  >> if #available(iOS 1, iOSApplicationExtension 1,
  >>               macOS 1, macOSApplicationExtension 1,
  >>               macCatalyst 1, macCatalystApplicationExtension 1,
  >>               watchOS 1, watchOSApplicationExtension 1,
  >>               tvOS 1, tvOSApplicationExtension 1,
  >>               visionOS 1, visionOSApplicationExtension 1, *) {
  >>     print("a")
  >> } else {
  >>     print("b")
  >> }
  >> if #available(madeUpPlatform 1, *) {
  >>     print("c")
  >> }
  >> if #unavailable(fakePlatform 1) {
  >>     print("d")
  >> } else {
  >>     print("dd")
  >> }
  !$ warning: unrecognized platform name 'madeUpPlatform'
  !$ if #available(madeUpPlatform 1, *) {
  !$               ^
  !$ warning: unrecognized platform name 'fakePlatform'
  !$ if #unavailable(fakePlatform 1) {
  !$                 ^
  << a
  << c
  << dd
  ```
-->

<!--
  - test: `empty-availability-condition`

  ```swifttest
  >> if #available(*) { print("1") }
  << 1
  ```
-->

<!--
  - test: `empty-unavailability-condition`

  ```swifttest
  >> if #unavailable() { print("2") }
  !$ error: expected platform name
  !$ if #unavailable() { print("2") }
  !$                ^
  ```
-->

<!--
이 소스 파일은 Swift.org 오픈 소스 프로젝트의 일부입니다.

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Apache License v2.0 및 Runtime Library Exception에 따라 라이선스가 부여됩니다.

라이선스 정보는 https://swift.org/LICENSE.txt에서 확인할 수 있습니다.
Swift 프로젝트 작성자 목록은 https://swift.org/CONTRIBUTORS.txt에서 확인할 수 있습니다.
-->


