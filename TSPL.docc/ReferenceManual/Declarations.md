# 선언문

타입, 연산자, 변수, 그리고 다른 이름과 구조를 소개한다.

*선언문*은 프로그램에 새로운 이름이나 구조를 도입한다. 예를 들어, 함수와 메서드를 소개하거나, 변수와 상수를 도입하고, 열거형, 구조체, 클래스, 프로토콜 타입을 정의할 때 선언문을 사용한다. 또한 기존에 존재하는 이름이 붙은 타입의 동작을 확장하거나, 다른 곳에서 선언된 심볼을 프로그램으로 임포트할 때도 선언문을 사용한다.

Swift에서는 대부분의 선언문이 동시에 구현되거나 초기화되기 때문에 정의의 역할도 한다. 그러나 프로토콜은 멤버를 구현하지 않기 때문에, 대부분의 프로토콜 멤버는 선언만 제공한다. 편의상 그리고 이 구분이 Swift에서 크게 중요하지 않기 때문에, *선언문*이라는 용어는 선언과 정의를 모두 포함한다.

> 선언문 문법:
>
> *선언문* → *임포트 선언문* \
> *선언문* → *상수 선언문* \
> *선언문* → *변수 선언문* \
> *선언문* → *타입 별칭 선언문* \
> *선언문* → *함수 선언문* \
> *선언문* → *열거형 선언문* \
> *선언문* → *구조체 선언문* \
> *선언문* → *클래스 선언문* \
> *선언문* → *액터 선언문* \
> *선언문* → *프로토콜 선언문* \
> *선언문* → *초기화자 선언문* \
> *선언문* → *디이니셜라이저 선언문* \
> *선언문* → *확장 선언문* \
> *선언문* → *서브스크립트 선언문* \
> *선언문* → *매크로 선언문* \
> *선언문* → *연산자 선언문* \
> *선언문* → *우선순위 그룹 선언문*


## 최상위 코드

Swift 소스 파일의 최상위 코드는 0개 이상의 구문, 선언, 그리고 표현식으로 구성된다. 기본적으로 소스 파일의 최상위 수준에서 선언된 변수, 상수, 그리고 기타 명명된 선언은 동일한 모듈에 속한 모든 소스 파일의 코드에서 접근할 수 있다. 이 기본 동작은 <doc:Declarations#Access-Control-Levels>에서 설명한 접근 레벨 수정자를 사용해 선언에 표시함으로써 재정의할 수 있다.

최상위 코드는 크게 두 가지 유형으로 나뉜다: 최상위 선언과 실행 가능한 최상위 코드. 최상위 선언은 선언만으로 이루어지며, 모든 Swift 소스 파일에서 허용된다. 실행 가능한 최상위 코드는 선언뿐만 아니라 구문과 표현식을 포함하며, 프로그램의 최상위 진입점으로만 허용된다.

실행 파일을 만들기 위해 컴파일하는 Swift 코드는 코드가 파일과 모듈로 어떻게 구성되어 있든 상관없이 다음 접근 방식 중 최대 하나만 사용해 최상위 진입점을 표시할 수 있다: `main` 속성, `NSApplicationMain` 속성, `UIApplicationMain` 속성, `main.swift` 파일, 또는 최상위 실행 가능한 코드를 포함하는 파일.

> 최상위 선언 문법:
>
> *top-level-declaration* → *statements*_?_


## 코드 블록

코드 블록은 다양한 선언과 제어 구조에서 여러 문장을 그룹화하는 데 사용된다. 코드 블록은 다음과 같은 형태를 가진다:

```swift
{
   <#statements#>
}
```

코드 블록 내부의 *statements*는 선언, 표현식, 그리고 다른 종류의 문장을 포함하며, 소스 코드에 나타난 순서대로 실행된다.

<!--
  TR: Swift의 스코프 규칙은 정확히 무엇인가?
-->

<!--
  TODO: 스코프에 대해 논의. 코드 블록이 새로운 스코프를 생성한다고 가정하는지?
-->

> 코드 블록의 문법:
>
> *code-block* → **`{`** *statements*_?_ **`}`**


## 임포트(Import) 선언

*임포트 선언*은 현재 파일 외부에서 선언된 심볼에 접근할 수 있게 한다. 기본 형태는 전체 모듈을 임포트하는 방식으로, `import` 키워드 뒤에 모듈 이름을 붙인다:

```swift
import <#module#>
```

더 세부적으로 지정하면 특정 심볼만 임포트할 수 있다. 예를 들어, 특정 하위 모듈이나 모듈 내의 특정 선언만 가져올 수 있다. 이렇게 세부적으로 지정하면, 현재 스코프에서 임포트된 심볼만 사용할 수 있고, 해당 심볼을 선언한 모듈은 사용할 수 없다.

```swift
import <#import kind#> <#module#>.<#symbol name#>
import <#module#>.<#submodule#>
```

<!--
  TODO: 이 섹션에 더 많은 내용을 추가해야 함.
-->

> 임포트 선언의 문법:
>
> *import-declaration* → *attributes*_?_ **`import`** *import-kind*_?_ *import-path*
>
> *import-kind* → **`typealias`** | **`struct`** | **`class`** | **`enum`** | **`protocol`** | **`let`** | **`var`** | **`func`** \
> *import-path* → *identifier* | *identifier* **`.`** *import-path*


## 상수 선언

*상수 선언*은 프로그램에 명명된 상수 값을 도입한다. 상수 선언은 `let` 키워드를 사용하며, 다음과 같은 형태를 가진다:

```swift
let <#상수 이름#>: <#타입#> = <#표현식#>
```

상수 선언은 *상수 이름*과 초기화 *표현식*의 값 사이에 불변의 바인딩을 정의한다. 상수의 값이 설정된 후에는 변경할 수 없다. 단, 상수가 클래스 객체로 초기화된 경우, 객체 자체는 변경될 수 있지만, 상수 이름과 객체 간의 바인딩은 변경할 수 없다.

상수가 전역 범위에서 선언되면 반드시 값으로 초기화해야 한다. 함수나 메서드의 컨텍스트에서 상수 선언이 발생하면, 상수의 값이 처음 읽히기 전에 값이 설정되도록 보장된다면 나중에 초기화할 수 있다. 컴파일러가 상수의 값이 절대 읽히지 않음을 증명할 수 있다면, 상수에 값을 설정할 필요가 없다. 이 분석을 *명확한 초기화*라고 한다. 컴파일러는 값이 읽히기 전에 반드시 설정됨을 증명한다.

> 참고:
> 명확한 초기화는 도메인 지식을 요구하는 증명을 구성할 수 없으며, 조건문을 통해 상태를 추적하는 능력에도 한계가 있다. 상수에 항상 값이 설정됨을 알 수 있지만, 컴파일러가 이를 증명할 수 없는 경우, 값을 설정하는 코드 경로를 단순화하거나 변수 선언을 사용해 보자.

클래스나 구조체 선언의 컨텍스트에서 상수 선언이 발생하면, 이를 *상수 프로퍼티*라고 한다. 상수 선언은 계산된 프로퍼티가 아니므로, getter나 setter를 가지지 않는다.

상수 선언의 *상수 이름*이 튜플 패턴인 경우, 튜플의 각 항목 이름은 초기화 *표현식*의 해당 값에 바인딩된다.

```swift
let (firstNumber, secondNumber) = (10, 42)
```

이 예제에서 `firstNumber`는 값 `10`에 대한 명명된 상수이고, `secondNumber`는 값 `42`에 대한 명명된 상수이다. 이제 두 상수를 독립적으로 사용할 수 있다:

```swift
print("첫 번째 숫자는 \(firstNumber)입니다.")
// "첫 번째 숫자는 10입니다." 출력
print("두 번째 숫자는 \(secondNumber)입니다.")
// "두 번째 숫자는 42입니다." 출력
```

타입 주석(`:` *타입*)은 *상수 이름*의 타입을 추론할 수 있는 경우 상수 선언에서 선택 사항이다. 이는 <doc:Types#Type-Inference>에서 설명한다.

상수 타입 프로퍼티를 선언하려면, 선언에 `static` 선언 수정자를 표시한다. 클래스의 상수 타입 프로퍼티는 항상 암묵적으로 final이다. 서브클래스에서의 재정의를 허용하거나 금지하기 위해 `class`나 `final` 선언 수정자를 표시할 수 없다. 타입 프로퍼티는 <doc:Properties#Type-Properties>에서 논의한다.

상수에 대한 더 많은 정보와 사용 시기를 위한 지침은 <doc:TheBasics#Constants-and-Variables>와 <doc:Properties#Stored-Properties>를 참고한다.

> 상수 선언의 문법:
>
> *constant-declaration* → *attributes*_?_ *declaration-modifiers*_?_ **`let`** *pattern-initializer-list*
>
> *pattern-initializer-list* → *pattern-initializer* | *pattern-initializer* **`,`** *pattern-initializer-list* \
> *pattern-initializer* → *pattern* *initializer*_?_ \
> *initializer* → **`=`** *expression*


## 변수 선언

*변수 선언*은 프로그램에 특정 이름의 값을 도입하는 과정이다. 이때 `var` 키워드를 사용해 변수를 선언한다.

변수 선언은 다양한 형태로 이루어질 수 있다. 저장된 변수와 계산된 변수, 프로퍼티, 저장 변수 및 프로퍼티 옵저버, 정적 변수 프로퍼티 등 여러 종류의 변경 가능한 값을 선언할 수 있다. 어떤 형태를 사용할지는 변수가 선언되는 범위와 선언하려는 변수의 종류에 따라 결정된다.

> 참고: 프로토콜 선언 컨텍스트에서도 프로퍼티를 선언할 수 있다. 자세한 내용은 <doc:Declarations#Protocol-Property-Declaration>에서 확인할 수 있다.

서브클래스에서 프로퍼티를 재정의하려면 `override` 선언 수정자를 사용하면 된다. 이에 대한 자세한 설명은 <doc:Inheritance#Overriding>에서 찾아볼 수 있다.


### 저장 변수와 저장 변수 프로퍼티

다음 형태는 저장 변수 또는 저장 변수 프로퍼티를 선언한다:

```swift
var <#변수 이름#>: <#타입#> = <#표현식#>
```

이 형태의 변수 선언은 전역 범위, 함수의 지역 범위, 또는 클래스나 구조체 선언 내에서 정의할 수 있다. 이 형태의 변수 선언이 전역 범위나 함수의 지역 범위에서 선언되면 *저장 변수*로 불린다. 클래스나 구조체 선언 내에서 선언되면 *저장 변수 프로퍼티*로 불린다.

초기화 *표현식*은 프로토콜 선언에서는 사용할 수 없지만, 다른 모든 상황에서는 선택 사항이다. 초기화 *표현식*이 없으면 변수 선언에 명시적 타입 주석(`:` *타입*)이 반드시 포함되어야 한다.

상수 선언과 마찬가지로, 변수 선언에서 초기화 *표현식*을 생략하면 변수는 처음 읽기 전에 값을 설정해야 한다. 또한 상수 선언과 유사하게, *변수 이름*이 튜플 패턴인 경우 튜플의 각 항목 이름은 초기화 *표현식*의 해당 값에 바인딩된다.

이름에서 알 수 있듯이, 저장 변수나 저장 변수 프로퍼티의 값은 메모리에 저장된다.


### 계산 변수와 계산 프로퍼티

다음은 계산 변수 또는 계산 프로퍼티를 선언하는 형식이다:

```swift
var <#variable name#>: <#type#> {
   get {
      <#statements#>
   }
   set(<#setter name#>) {
      <#statements#>
   }
}
```

이 형식의 변수 선언은 전역 범위, 함수의 지역 범위, 또는 클래스, 구조체, 열거형, 확장 선언의 컨텍스트에서 정의할 수 있다. 이 형식의 변수 선언이 전역 범위나 함수의 지역 범위에서 선언되면 *계산 변수*라고 부른다. 클래스, 구조체, 또는 확장 선언의 컨텍스트에서 선언되면 *계산 프로퍼티*라고 부른다.

getter는 값을 읽는 데 사용되고, setter는 값을 쓰는 데 사용된다. setter 절은 선택 사항이며, getter만 필요한 경우에는 두 절을 모두 생략하고 직접 요청된 값을 반환할 수 있다. 이는 <doc:Properties#Read-Only-Computed-Properties>에 설명되어 있다. 하지만 setter 절을 제공한다면, getter 절도 반드시 제공해야 한다.

*setter 이름*과 괄호는 선택 사항이다. setter 이름을 제공하면, setter의 매개변수 이름으로 사용된다. setter 이름을 제공하지 않으면, setter의 기본 매개변수 이름은 `newValue`가 된다. 이는 <doc:Properties#Shorthand-Setter-Declaration>에 설명되어 있다.

저장된 명명된 값과 저장된 변수 프로퍼티와 달리, 계산된 명명된 값이나 계산 프로퍼티의 값은 메모리에 저장되지 않는다.

계산 프로퍼티에 대한 더 많은 정보와 예제는 <doc:Properties#Computed-Properties>를 참고한다.


### 저장 변수 관찰자와 프로퍼티 관찰자

`willSet`과 `didSet` 관찰자를 사용해 저장 변수나 프로퍼티를 선언할 수 있다. 관찰자가 있는 저장 변수나 프로퍼티는 다음과 같은 형태를 가진다:

```swift
var <#변수 이름#>: <#타입#> = <#표현식#> {
   willSet(<#setter 이름#>) {
      <#구문#>
   }
   didSet(<#setter 이름#>) {
      <#구문#>
   }
}
```

이 형태의 변수 선언은 전역 범위, 함수의 지역 범위, 또는 클래스나 구조체 선언 내에서 정의할 수 있다. 전역 범위나 함수의 지역 범위에서 이 형태로 변수를 선언하면 관찰자를 *저장 변수 관찰자*라고 부른다. 클래스나 구조체 선언 내에서 선언하면 관찰자를 *프로퍼티 관찰자*라고 부른다.

프로퍼티 관찰자는 모든 저장 프로퍼티에 추가할 수 있다. 또한 상속된 프로퍼티(저장 프로퍼티든 계산 프로퍼티든)에 프로퍼티 관찰자를 추가하려면 하위 클래스에서 해당 프로퍼티를 재정의하면 된다. 이에 대한 자세한 내용은 <doc:Inheritance#Overriding-Property-Observers>를 참고한다.

클래스나 구조체 선언 내에서는 초기화 *표현식*이 선택 사항이지만, 다른 곳에서는 필수이다. 초기화 *표현식*에서 타입을 추론할 수 있는 경우 *타입* 주석은 선택 사항이다. 이 표현식은 프로퍼티 값을 처음 읽을 때 평가된다. 프로퍼티 값을 읽지 않고 초기 값을 덮어쓰면, 이 표현식은 프로퍼티에 처음 쓰기 전에 평가된다.

`willSet`과 `didSet` 관찰자는 변수나 프로퍼티의 값이 설정될 때 이를 관찰하고 적절히 대응할 수 있는 방법을 제공한다. 관찰자는 변수나 프로퍼티가 처음 초기화될 때 호출되지 않는다. 대신, 초기화가 아닌 상황에서 값이 설정될 때만 호출된다.

`willSet` 관찰자는 변수나 프로퍼티의 값이 설정되기 직전에 호출된다. 새로운 값은 상수로 `willSet` 관찰자에 전달되므로, `willSet` 절 내에서 이 값을 변경할 수 없다. `didSet` 관찰자는 새로운 값이 설정된 직후에 호출된다. `willSet` 관찰자와 달리, `didSet` 관찰자에는 변수나 프로퍼티의 이전 값이 전달된다. 따라서 이전 값에 접근해야 할 때 유용하다. 다만, `didSet` 관찰자 절 내에서 변수나 프로퍼티에 값을 할당하면, 방금 설정된 값을 대체한다.

`willSet`과 `didSet` 절의 *setter 이름*과 괄호는 선택 사항이다. setter 이름을 제공하면, 이 이름이 `willSet`과 `didSet` 관찰자의 매개변수 이름으로 사용된다. setter 이름을 제공하지 않으면, `willSet` 관찰자의 기본 매개변수 이름은 `newValue`이고, `didSet` 관찰자의 기본 매개변수 이름은 `oldValue`이다.

`willSet` 절을 제공할 때 `didSet` 절은 선택 사항이다. 마찬가지로, `didSet` 절을 제공할 때 `willSet` 절도 선택 사항이다.

`didSet` 관찰자 본문에서 이전 값을 참조하면, 관찰자가 호출되기 전에 getter가 호출되어 이전 값을 사용할 수 있게 한다. 그렇지 않으면, 새로운 값은 슈퍼클래스의 getter를 호출하지 않고 저장된다. 아래 예제는 슈퍼클래스에서 정의된 계산 프로퍼티를 하위 클래스에서 재정의해 관찰자를 추가하는 방법을 보여준다.

```swift
class Superclass {
    private var xValue = 12
    var x: Int {
        get { print("Getter was called"); return xValue }
        set { print("Setter was called"); xValue = newValue }
    }
}

// 이 하위 클래스는 관찰자에서 oldValue를 참조하지 않으므로,
// 슈퍼클래스의 getter는 값을 출력하기 위해 한 번만 호출된다.
class New: Superclass {
    override var x: Int {
        didSet { print("New value \(x)") }
    }
}
let new = New()
new.x = 100
// Prints "Setter was called"
// Prints "Getter was called"
// Prints "New value 100"

// 이 하위 클래스는 관찰자에서 oldValue를 참조하므로,
// 슈퍼클래스의 getter는 setter 전에 한 번, 그리고 값을 출력하기 위해 다시 한 번 호출된다.
class NewAndOld: Superclass {
    override var x: Int {
        didSet { print("Old value \(oldValue) - new value \(x)") }
    }
}
let newAndOld = NewAndOld()
newAndOld.x = 200
// Prints "Getter was called"
// Prints "Setter was called"
// Prints "Getter was called"
// Prints "Old value 12 - new value 200"
```

프로퍼티 관찰자를 사용하는 방법에 대한 더 많은 정보와 예제는 <doc:Properties#Property-Observers>를 참고한다.


### 타입 변수 프로퍼티

타입 변수 프로퍼티를 선언하려면 `static` 선언 수식어를 사용한다. 클래스는 타입 계산 프로퍼티에 `class` 선언 수식어를 사용해 서브클래스가 슈퍼클래스의 구현을 재정의할 수 있도록 허용한다. 타입 프로퍼티에 대한 자세한 내용은 <doc:Properties#Type-Properties>에서 다룬다.

> 변수 선언 문법:
>
> *variable-declaration* → *variable-declaration-head* *pattern-initializer-list* \
> *variable-declaration* → *variable-declaration-head* *variable-name* *type-annotation* *code-block* \
> *variable-declaration* → *variable-declaration-head* *variable-name* *type-annotation* *getter-setter-block* \
> *variable-declaration* → *variable-declaration-head* *variable-name* *type-annotation* *getter-setter-keyword-block* \
> *variable-declaration* → *variable-declaration-head* *variable-name* *initializer* *willSet-didSet-block* \
> *variable-declaration* → *variable-declaration-head* *variable-name* *type-annotation* *initializer*_?_ *willSet-didSet-block*
>
> *variable-declaration-head* → *attributes*_?_ *declaration-modifiers*_?_ **`var`** \
> *variable-name* → *identifier*
>
> *getter-setter-block* → *code-block* \
> *getter-setter-block* → **`{`** *getter-clause* *setter-clause*_?_ **`}`** \
> *getter-setter-block* → **`{`** *setter-clause* *getter-clause* **`}`** \
> *getter-clause* → *attributes*_?_ *mutation-modifier*_?_ **`get`** *code-block* \
> *setter-clause* → *attributes*_?_ *mutation-modifier*_?_ **`set`** *setter-name*_?_ *code-block* \
> *setter-name* → **`(`** *identifier* **`)`**
>
> *getter-setter-keyword-block* → **`{`** *getter-keyword-clause* *setter-keyword-clause*_?_ **`}`** \
> *getter-setter-keyword-block* → **`{`** *setter-keyword-clause* *getter-keyword-clause* **`}`** \
> *getter-keyword-clause* → *attributes*_?_ *mutation-modifier*_?_ **`get`** \
> *setter-keyword-clause* → *attributes*_?_ *mutation-modifier*_?_ **`set`**
>
> *willSet-didSet-block* → **`{`** *willSet-clause* *didSet-clause*_?_ **`}`** \
> *willSet-didSet-block* → **`{`** *didSet-clause* *willSet-clause*_?_ **`}`** \
> *willSet-clause* → *attributes*_?_ **`willSet`** *setter-name*_?_ *code-block* \
> *didSet-clause* → *attributes*_?_ **`didSet`** *setter-name*_?_ *code-block*

<!--
  NOTE: 계산 프로퍼티에는 타입 어노테이션이 필수적이다 -- 해당 프로퍼티의 타입은 계산되거나 추론되지 않는다.
-->


## 타입 별칭 선언

*타입 별칭 선언*은 프로그램 내에 기존 타입에 대한 이름을 부여한다. 타입 별칭 선언은 `typealias` 키워드를 사용하며, 다음과 같은 형태를 가진다:

```swift
typealias <#이름#> = <#기존 타입#>
```

타입 별칭을 선언한 후에는 프로그램 어디에서나 *기존 타입* 대신 *이름*을 사용할 수 있다. *기존 타입*은 이름이 있는 타입이거나 복합 타입일 수 있다. 타입 별칭은 새로운 타입을 생성하지 않으며, 단순히 기존 타입을 가리키는 이름을 제공한다.

타입 별칭 선언은 제네릭 매개변수를 사용해 기존 제네릭 타입에 이름을 부여할 수 있다. 타입 별칭은 기존 타입의 제네릭 매개변수 중 일부 또는 전체에 대해 구체적인 타입을 제공할 수 있다. 예를 들어:

```swift
typealias StringDictionary<Value> = Dictionary<String, Value>

// 다음 두 딕셔너리는 동일한 타입을 가진다.
var dictionary1: StringDictionary<Int> = [:]
var dictionary2: Dictionary<String, Int> = [:]
```

<!--
  - test: `typealias-with-generic`

  ```swifttest
  -> typealias StringDictionary<Value> = Dictionary<String, Value>

  // The following dictionaries have the same type.
  -> var dictionary1: StringDictionary<Int> = [:]
  -> var dictionary2: Dictionary<String, Int> = [:]
  ```
-->

타입 별칭이 제네릭 매개변수와 함께 선언될 때, 해당 매개변수의 제약 조건은 기존 타입의 제네릭 매개변수 제약 조건과 정확히 일치해야 한다. 예를 들어:

```swift
typealias DictionaryOfInts<Key: Hashable> = Dictionary<Key, Int>
```

<!--
  - test: `typealias-with-generic-constraint`

  ```swifttest
  -> typealias DictionaryOfInts<Key: Hashable> = Dictionary<Key, Int>
  ```
-->

타입 별칭과 기존 타입은 서로 교환 가능하게 사용할 수 있으므로, 타입 별칭은 추가적인 제네릭 제약 조건을 도입할 수 없다.

타입 별칭은 선언에서 모든 제네릭 매개변수를 생략함으로써 기존 타입의 제네릭 매개변수를 전달할 수 있다. 예를 들어, 여기서 선언된 `Diccionario` 타입 별칭은 `Dictionary`와 동일한 제네릭 매개변수와 제약 조건을 가진다.

```swift
typealias Diccionario = Dictionary
```

<!--
  - test: `typealias-using-shorthand`

  ```swifttest
  -> typealias Diccionario = Dictionary
  ```
-->

<!--
  Note that the compiler doesn't currently enforce this. For example, this works but shouldn't:
  typealias ProvidingMoreSpecificConstraints<T: Comparable & Hashable> = Dictionary<T, Int>
-->

<!--
  Things that shouldn't work:
  typealias NotRedeclaringSomeOfTheGenericParameters = Dictionary<T, String>
  typealias NotRedeclaringAnyOfTheGenericParameters = Dictionary
  typealias NotProvidingTheCorrectConstraints<T> = Dictionary<T, Int>
  typealias ProvidingMoreSpecificConstraints<T: Comparable & Hashable> = Dictionary<T, Int>
-->

프로토콜 선언 내부에서 타입 별칭은 자주 사용되는 타입에 대해 더 짧고 편리한 이름을 제공할 수 있다. 예를 들어:

```swift
protocol Sequence {
    associatedtype Iterator: IteratorProtocol
    typealias Element = Iterator.Element
}

func sum<T: Sequence>(_ sequence: T) -> Int where T.Element == Int {
    // ...
}
```

<!--
  - test: `typealias-in-protocol`

  ```swifttest
  -> protocol Sequence {
         associatedtype Iterator: IteratorProtocol
         typealias Element = Iterator.Element
     }

  -> func sum<T: Sequence>(_ sequence: T) -> Int where T.Element == Int {
         // ...
  >>     return 9000
     }
  ```
-->

이 타입 별칭이 없다면, `sum` 함수는 연관 타입을 `T.Iterator.Element` 대신 `T.Element`로 참조해야 한다.

자세한 내용은 <doc:Declarations#Protocol-Associated-Type-Declaration>을 참고한다.

> 타입 별칭 선언 문법:
>
> *typealias-declaration* → *attributes*_?_ *access-level-modifier*_?_ **`typealias`** *typealias-name* *generic-parameter-clause*_?_ *typealias-assignment* \
> *typealias-name* → *identifier* \
> *typealias-assignment* → **`=`** *type*

<!--
  Old grammar:
  typealias-declaration -> typealias-head typealias-assignment
  typealias-head -> ``typealias`` typealias-name type-inheritance-clause-OPT
  typealias-name -> identifier
  typealias-assignment -> ``=`` type
-->


## 함수 선언

*함수 선언*은 프로그램에 함수나 메서드를 도입한다. 클래스, 구조체, 열거형, 프로토콜 내부에서 선언된 함수는 *메서드*로 불린다. 함수 선언은 `func` 키워드를 사용하며, 다음과 같은 형태를 가진다:

```swift
func <#함수 이름#>(<#매개변수#>) -> <#반환 타입#> {
   <#구문#>
}
```

함수의 반환 타입이 `Void`인 경우, 반환 타입을 생략할 수 있다:

```swift
func <#함수 이름#>(<#매개변수#>) {
   <#구문#>
}
```

각 매개변수의 타입은 반드시 명시해야 한다. 타입 추론은 불가능하다. 매개변수 타입 앞에 `inout`을 작성하면, 함수 내부에서 해당 매개변수를 수정할 수 있다. in-out 매개변수에 대한 자세한 내용은 아래 <doc:Declarations#In-Out-Parameters>에서 다룬다.

함수 선언의 *구문*이 단일 표현식으로만 구성된 경우, 해당 표현식의 값을 반환하는 것으로 이해된다. 이 암시적 반환 구문은 표현식의 타입과 함수의 반환 타입이 `Void`가 아니고, `Never`와 같이 케이스가 없는 열거형이 아닐 때만 고려된다.

함수는 튜플 타입을 반환 타입으로 사용해 여러 값을 반환할 수 있다.

함수 정의는 다른 함수 선언 내부에 나타날 수 있다. 이런 종류의 함수는 *중첩 함수*로 알려져 있다.

중첩 함수는 값이 절대 벗어나지 않도록 보장된 경우(예: in-out 매개변수) 또는 논스케이핑 함수 인자로 전달된 경우 논스케이핑 함수로 간주된다. 그렇지 않으면 중첩 함수는 스케이핑 함수가 된다.

중첩 함수에 대한 자세한 내용은 <doc:Functions#Nested-Functions>에서 확인할 수 있다.


### 파라미터 이름

함수 파라미터는 쉼표로 구분된 목록으로, 각 파라미터는 여러 형태 중 하나를 가진다. 함수 호출 시 전달하는 인자의 순서는 함수 선언 시 파라미터 순서와 일치해야 한다. 파라미터 목록의 가장 간단한 형태는 다음과 같다:

```swift
<#파라미터 이름#>: <#파라미터 타입#>
```

파라미터는 함수 본문 내에서 사용되는 이름과, 함수나 메서드를 호출할 때 사용되는 인자 레이블을 가진다. 기본적으로 파라미터 이름은 인자 레이블로도 사용된다. 예를 들어:

```swift
func f(x: Int, y: Int) -> Int { return x + y }
f(x: 1, y: 2) // x와 y 모두 레이블이 지정됨
```

기본 인자 레이블 동작을 재정의하려면 다음 형태 중 하나를 사용한다:

```swift
<#인자 레이블#> <#파라미터 이름#>: <#파라미터 타입#>
_ <#파라미터 이름#>: <#파라미터 타입#>
```

파라미터 이름 앞에 오는 이름은 파라미터에 명시적인 인자 레이블을 부여하며, 이는 파라미터 이름과 다를 수 있다. 해당 인자는 함수나 메서드 호출 시 주어진 인자 레이블을 반드시 사용해야 한다.

파라미터 이름 앞에 언더스코어(`_`)를 사용하면 인자 레이블을 생략한다. 해당 인자는 함수나 메서드 호출 시 레이블 없이 전달해야 한다.

```swift
func repeatGreeting(_ greeting: String, count n: Int) { /* n번 인사 */ }
repeatGreeting("Hello, world!", count: 2) // count는 레이블이 지정되고, greeting은 지정되지 않음
```


### 매개변수 수정자

*매개변수 수정자*는 인자가 함수에 전달되는 방식을 변경한다.

```swift
<#argument label#> <#parameter name#>: <#parameter modifier#> <#parameter type#>
```

매개변수 수정자를 사용하려면,
인자의 타입 앞에 `inout`, `borrowing`, 또는 `consuming`을 작성한다.

```swift
func someFunction(a: inout A, b: consuming B, c: C) { ... }
```


#### 입출력 매개변수

기본적으로 Swift에서 함수 인자는 값에 의해 전달된다. 함수 내부에서 변경된 내용은 호출자에게 보이지 않는다. 입출력 매개변수를 사용하려면 `inout` 매개변수 수정자를 적용한다.

```swift
func someFunction(a: inout Int) {
    a += 1
}
```

입출력 매개변수가 포함된 함수를 호출할 때는, 인자 앞에 앰퍼샌드(`&`)를 붙여 함수 호출이 인자의 값을 변경할 수 있음을 표시한다.

```swift
var x = 7
someFunction(&x)
print(x)  // "8" 출력
```

입출력 매개변수는 다음과 같이 전달된다:

1. 함수가 호출되면 인자의 값이 복사된다.
2. 함수 본문에서 복사된 값이 수정된다.
3. 함수가 반환될 때 복사된 값이 원래 인자에 할당된다.

이 동작을 *복사-입력 복사-출력* 또는 *값 결과 호출*이라고 한다. 예를 들어, 계산 속성이나 관찰자를 가진 속성이 입출력 매개변수로 전달되면, 함수 호출 시 getter가 호출되고 함수 반환 시 setter가 호출된다.

최적화를 위해, 인자가 메모리의 물리적 주소에 저장된 값인 경우, 함수 내부와 외부에서 동일한 메모리 위치를 사용한다. 이 최적화된 동작을 *참조 호출*이라고 하며, 복사 오버헤드를 제거하면서 복사-입력 복사-출력 모델의 모든 요구 사항을 충족한다. 코드를 작성할 때는 최적화에 의존하지 않고 복사-입력 복사-출력 모델을 기준으로 작성해야 하며, 최적화 여부에 관계없이 올바르게 동작하도록 해야 한다.

함수 내부에서는 입출력 매개변수로 전달된 값에 접근하지 않아야 한다. 원래 값이 현재 범위에서 사용 가능하더라도 접근하면 동시 접근이 발생하여 메모리 독점성을 위반하게 된다.

```swift
var someValue: Int
func someFunction(a: inout Int) {
    a += someValue
}

// 오류: 런타임 독점성 위반 발생
someFunction(&someValue)
```

같은 이유로, 동일한 값을 여러 입출력 매개변수에 전달할 수 없다.

```swift
var someValue: Int
func someFunction(a: inout Int, b: inout Int) {
    a += b
    b += 1
}

// 오류: 동일한 값을 여러 입출력 매개변수에 전달할 수 없음
someFunction(&someValue, &someValue)
```

메모리 안전성과 메모리 독점성에 대한 자세한 내용은 <doc:MemorySafety>를 참조한다.

<!--
  참조 호출 최적화가 적용되면 원하는 대로 동작할 수 있다.
  하지만 여전히 그렇게 해서는 안 된다.
  위에서 언급한 것처럼, 참조 호출로 인한 동작 차이에 의존해서는 안 된다.
-->

입출력 매개변수를 캡처하는 클로저나 중첩 함수는 비탈출(nonescaping)이어야 한다. 입출력 매개변수를 변경하지 않고 캡처해야 한다면, 캡처 목록을 사용해 명시적으로 불변으로 캡처한다.

```swift
func someFunction(a: inout Int) -> () -> Int {
    return { [a] in return a + 1 }
}
```

<!--
  - test: `explicit-capture-for-inout`

  ```swifttest
  -> func someFunction(a: inout Int) -> () -> Int {
         return { [a] in return a + 1 }
     }
  >> class C { var x = 100 }
  >> let c = C()
  >> let f = someFunction(a: &c.x)
  >> c.x = 200
  >> let r = f()
  >> print(r, r == c.x)
  << 101 false
  ```
-->

입출력 매개변수를 캡처하고 변경해야 한다면, 명시적으로 로컬 복사본을 사용한다. 예를 들어, 함수가 반환되기 전에 모든 변경이 완료되도록 보장하는 멀티스레드 코드에서 다음과 같이 사용할 수 있다.

```swift
func multithreadedFunction(queue: DispatchQueue, x: inout Int) {
    // 로컬 복사본을 만들고 수동으로 복사본을 다시 복사한다.
    var localX = x
    defer { x = localX }

    // localX에 대해 비동기적으로 작업한 후 반환 전에 대기한다.
    queue.async { someMutatingOperation(&localX) }
    queue.sync {}
}
```

<!--
  - test: `cant-pass-inout-aliasing`

  ```swifttest
  >> import Dispatch
  >> func someMutatingOperation(_ a: inout Int) {}
  -> func multithreadedFunction(queue: DispatchQueue, x: inout Int) {
        // 로컬 복사본을 만들고 수동으로 복사본을 다시 복사한다.
        var localX = x
        defer { x = localX }

        // localX에 대해 비동기적으로 작업한 후 반환 전에 대기한다.
        queue.async { someMutatingOperation(&localX) }
        queue.sync {}
     }
  ```
-->

입출력 매개변수에 대한 더 많은 논의와 예제는 <doc:Functions#In-Out-Parameters>를 참조한다.

<!--
  - test: `escaping-cant-capture-inout`

  ```swifttest
  -> func outer(a: inout Int) -> () -> Void {
         func inner() {
             a += 1
         }
         return inner
     }
  !$ error: escaping local function captures 'inout' parameter 'a'
  !! return inner
  !! ^
  !$ note: parameter 'a' is declared 'inout'
  !! func outer(a: inout Int) -> () -> Void {
  !! ^
  !$ note: captured here
  !! a += 1
  !! ^
  -> func closure(a: inout Int) -> () -> Void {
         return { a += 1 }
     }
  !$ error: escaping closure captures 'inout' parameter 'a'
  !! return { a += 1 }
  !! ^
  !$ note: parameter 'a' is declared 'inout'
  !! func closure(a: inout Int) -> () -> Void {
  !! ^
  !$ note: captured here
  !! return { a += 1 }
  !! ^
  ```
-->


#### 파라미터의 차용과 소비

기본적으로 Swift는 함수 호출 간 객체 수명을 자동으로 관리하기 위해 일련의 규칙을 사용한다. 필요할 때 값을 복사하는 방식으로 동작한다. 기본 규칙은 대부분의 경우 오버헤드를 최소화하도록 설계되었다. 더 세밀한 제어가 필요하다면 `borrowing`이나 `consuming` 파라미터 수정자를 사용할 수 있다. 이 경우 `copy`를 사용해 명시적으로 복사 작업을 표시한다.

기본 규칙을 사용하든 아니든, Swift는 모든 경우에 객체 수명과 소유권이 올바르게 관리되도록 보장한다. 이 파라미터 수정자들은 특정 사용 패턴의 상대적 효율성에만 영향을 미치며, 정확성에는 영향을 주지 않는다.

<!--
TODO: 기본 규칙 설명.
기본적으로 초기화 함수와 프로퍼티 설정자는 consuming,
그 외는 borrowing으로 동작한다.
복사 작업은 어디에 암시적으로 삽입되는가?
-->

`borrowing` 수정자는 함수가 파라미터의 값을 유지하지 않음을 나타낸다. 이 경우 호출자가 객체의 소유권과 수명 관리 책임을 가진다. 함수가 객체를 일시적으로만 사용할 때 `borrowing`을 사용하면 오버헤드를 최소화할 수 있다.

```swift
// `isLessThan`은 두 인수 모두를 유지하지 않음
func isLessThan(lhs: borrowing A, rhs: borrowing A) -> Bool {
    ...
}
```

함수가 파라미터의 값을 유지해야 한다면, 예를 들어 전역 변수에 저장해야 한다면 `copy`를 사용해 명시적으로 그 값을 복사한다.

```swift
// 위와 같지만, 이 `isLessThan`은 가장 작은 값을 기록하려 함
func isLessThan(lhs: borrowing A, rhs: borrowing A) -> Bool {
    if lhs < storedValue {
        storedValue = copy lhs
    } else if rhs < storedValue {
        storedValue = copy rhs
    }
    return lhs < rhs
}
```

반대로, `consuming` 파라미터 수정자는 함수가 값의 소유권을 가짐을 나타낸다. 함수가 반환되기 전에 값을 저장하거나 파괴할 책임을 가진다.

```swift
// `store`는 인수를 유지하므로 `consuming`으로 표시
func store(a: consuming A) {
    someGlobalVariable = a
}
```

호출자가 함수 호출 후 객체를 더 이상 사용하지 않을 때 `consuming`을 사용하면 오버헤드를 최소화할 수 있다.

```swift
// 일반적으로 이는 값을 사용하는 마지막 작업
store(a: value)
```

함수 호출 후 복사 가능한 객체를 계속 사용한다면, 컴파일러는 함수 호출 전에 해당 객체의 복사본을 자동으로 만든다.

```swift
// 컴파일러는 여기에 암시적 복사를 삽입
store(a: someValue)  // 이 함수는 someValue를 소비
print(someValue)  // someValue의 복사본을 사용
```

`inout`과 달리, `borrowing`이나 `consuming` 파라미터는 함수를 호출할 때 특별한 표기법이 필요하지 않다.

```swift
func someFunction(a: borrowing A, b: consuming B) { ... }

someFunction(a: someA, b: someB)
```

`borrowing`이나 `consuming`을 명시적으로 사용하면 런타임 소유권 관리의 오버헤드를 더 엄격하게 제어하려는 의도를 나타낸다. 복사가 예상치 못한 런타임 소유권 작업을 유발할 수 있기 때문에, 이 수정자로 표시된 파라미터는 명시적으로 `copy` 키워드를 사용하지 않으면 복사할 수 없다.

```swift
func borrowingFunction1(a: borrowing A) {
    // 오류: a를 암시적으로 복사할 수 없음
    // 이 할당은 복사가 필요함
    // `a`는 호출자로부터 차용된 것임
    someGlobalVariable = a
}

func borrowingFunction2(a: borrowing A) {
    // OK: 명시적 복사는 동작함
    someGlobalVariable = copy a
}

func consumingFunction1(a: consuming A) {
    // 오류: a를 암시적으로 복사할 수 없음
    // 이 할당은 복사가 필요함
    // 아래 `print` 때문
    someGlobalVariable = a
    print(a)
}

func consumingFunction2(a: consuming A) {
    // OK: 명시적 복사는 문제없이 동작
    someGlobalVariable = copy a
    print(a)
}

func consumingFunction3(a: consuming A) {
    // OK: 여기서는 복사가 필요 없음. 이게 마지막 사용임
    someGlobalVariable = a
}
```

<!--
  TODO: `borrowing`과 `consuming` 키워드를 복사 불가능한 타입 인수와 함께 사용
-->
<!--
  TODO: 파라미터 수정자의 변경은 ABI 호환성을 깨뜨림
-->


### 특별한 종류의 파라미터

파라미터는 무시할 수도 있고, 다양한 개수의 값을 받을 수도 있으며, 기본값을 제공할 수도 있다. 이러한 기능은 다음과 같은 형태로 사용한다:

```swift
_ : <#파라미터 타입#>
<#파라미터 이름#>: <#파라미터 타입#>...
<#파라미터 이름#>: <#파라미터 타입#> = <#기본값#>
```

언더스코어(`_`)로 표시된 파라미터는 명시적으로 무시되며, 함수 본문 내에서 접근할 수 없다.

기본 타입 이름 뒤에 바로 점 세 개(`...`)가 오는 파라미터는 가변 인자(variadic parameter)로 이해된다. 가변 인자 바로 뒤에 오는 파라미터는 반드시 인자 레이블이 있어야 한다. 하나의 함수는 여러 개의 가변 인자를 가질 수 있다. 가변 인자는 기본 타입의 요소를 포함하는 배열로 처리된다. 예를 들어, `Int...`라는 가변 인자는 `[Int]`로 처리된다. 가변 인자를 사용하는 예제는 <doc:Functions#Variadic-Parameters>를 참고한다.

타입 뒤에 등호(`=`)와 표현식이 오는 파라미터는 해당 표현식을 기본값으로 가진다. 이 표현식은 함수가 호출될 때 평가된다. 함수를 호출할 때 파라미터를 생략하면 기본값이 대신 사용된다.

```swift
func f(x: Int = 42) -> Int { return x }
f()       // 유효함, 기본값 사용
f(x: 7)   // 유효함, 제공된 값 사용
f(7)      // 유효하지 않음, 인자 레이블 누락
```

<!--
  - test: `default-args-and-labels`

  ```swifttest
  -> func f(x: Int = 42) -> Int { return x }
  >> let _ =
  -> f()       // 유효함, 기본값 사용
  >> let _ =
  -> f(x: 7)   // 유효함, 제공된 값 사용
  >> let _ =
  -> f(7)      // 유효하지 않음, 인자 레이블 누락
  !$ error: missing argument label 'x:' in call
  !! f(7)      // 유효하지 않음, 인자 레이블 누락
  !!   ^
  !!   x:
  ```
-->

<!--
  위의 내용을 함수의 반환값을 버리지 않도록 다시 작성한다.
  추적 중인 버그는 <rdar://problem/35301593>
-->

<!--
  - test: `default-args-evaluated-at-call-site`

  ```swifttest
  -> func shout() -> Int {
        print("evaluated")
        return 10
     }
  -> func foo(x: Int = shout()) { print("x is \(x)") }
  -> foo(x: 100)
  << x is 100
  -> foo()
  << evaluated
  << x is 10
  -> foo()
  << evaluated
  << x is 10
  ```
-->


### 특별한 종류의 메서드

열거형이나 구조체에서 `self`를 수정하는 메서드는 `mutating` 선언 수식어를 반드시 붙여야 한다.

슈퍼클래스의 메서드를 오버라이드하는 메서드는 `override` 선언 수식어를 반드시 붙여야 한다. `override` 수식어 없이 메서드를 오버라이드하거나, 슈퍼클래스 메서드를 오버라이드하지 않는 메서드에 `override` 수식어를 사용하면 컴파일 타임 에러가 발생한다.

타입의 인스턴스가 아닌 타입 자체와 연관된 메서드는 열거형과 구조체의 경우 `static` 선언 수식어를 붙여야 하고, 클래스의 경우 `static` 또는 `class` 선언 수식어를 붙여야 한다. `class` 수식어로 표시된 클래스 타입 메서드는 서브클래스에서 오버라이드할 수 있지만, `class final` 또는 `static`으로 표시된 클래스 타입 메서드는 오버라이드할 수 없다.

<!--
  - test: `overriding-class-methods-err`

  ```swifttest
  -> class S { class final func f() -> Int { return 12 } }
  -> class SS: S { override class func f() -> Int { return 120 } }
  !$ error: class method overrides a 'final' class method
  !! class SS: S { override class func f() -> Int { return 120 } }
  !!                                  ^
  !$ note: overridden declaration is here
  !! class S { class final func f() -> Int { return 12 } }
  !!                           ^
  -> class S2 { static func f() -> Int { return 12 } }
  -> class SS2: S2 { override static func f() -> Int { return 120 } }
  !$ error: cannot override static method
  !! class SS2: S2 { override static func f() -> Int { return 120 } }
  !! ^
  !$ note: overridden declaration is here
  !! class S2 { static func f() -> Int { return 12 } }
  !! ^
  ```
-->

<!--
  - test: `overriding-class-methods`

  ```swifttest
  -> class S3 { class func f() -> Int { return 12 } }
  -> class SS3: S3 { override class func f() -> Int { return 120 } }
  -> print(SS3.f())
  <- 120
  ```
-->


### 특별한 이름을 가진 메서드

특별한 이름을 가진 몇 가지 메서드는 함수 호출 구문을 위한 문법적 편의를 제공한다. 타입이 이러한 메서드 중 하나를 정의하면, 해당 타입의 인스턴스를 함수 호출 구문에서 사용할 수 있다. 함수 호출은 해당 인스턴스의 특별한 이름을 가진 메서드 호출로 이해된다.

클래스, 구조체, 또는 열거형 타입은 `dynamicallyCall(withArguments:)` 메서드나 `dynamicallyCall(withKeywordArguments:)` 메서드를 정의하거나, 아래 설명된 call-as-function 메서드를 정의함으로써 함수 호출 구문을 지원할 수 있다. 타입이 call-as-function 메서드와 `dynamicCallable` 속성에 사용되는 메서드를 모두 정의한 경우, 컴파일러는 두 메서드 중 어느 것을 사용할 수 있는 상황에서도 call-as-function 메서드를 우선적으로 선택한다.

call-as-function 메서드의 이름은 `callAsFunction()`이거나, `callAsFunction(`으로 시작하고 레이블이 있거나 없는 인자를 추가한 이름일 수 있다. 예를 들어, `callAsFunction(_:_:)`와 `callAsFunction(something:)`도 유효한 call-as-function 메서드 이름이다.

<!--
  위에서 callAsFunction(은 코드 서체로 표시되었지만, 실제로 독자의 코드에 존재하는 심볼은 아니다.
  Chuck과의 논의에 따르면, 여기서 표현하려는 것에 가장 가까운 타이포그래피 규칙이다.
-->

다음 함수 호출은 동일하다:

```swift
struct CallableStruct {
    var value: Int
    func callAsFunction(_ number: Int, scale: Int) {
        print(scale * (number + value))
    }
}
let callable = CallableStruct(value: 100)
callable(4, scale: 2)
callable.callAsFunction(4, scale: 2)
// 두 함수 호출 모두 208을 출력한다.
```

<!--
  - test: `call-as-function`

  ```swifttest
  -> struct CallableStruct {
         var value: Int
         func callAsFunction(_ number: Int, scale: Int) {
             print(scale * (number + value))
         }
     }
  -> let callable = CallableStruct(value: 100)
  -> callable(4, scale: 2)
  -> callable.callAsFunction(4, scale: 2)
  // 두 함수 호출 모두 208을 출력한다.
  << 208
  << 208
  ```
-->

call-as-function 메서드와 `dynamicCallable` 속성의 메서드는 타입 시스템에 얼마나 많은 정보를 인코딩할지와 런타임에 얼마나 많은 동적 동작이 가능한지 사이에서 다른 트레이드오프를 제공한다. call-as-function 메서드를 선언할 때는 인자의 수와 각 인자의 타입 및 레이블을 지정한다. `dynamicCallable` 속성의 메서드는 인자 배열을 보유하는 데 사용되는 타입만 지정한다.

call-as-function 메서드나 `dynamicCallable` 속성의 메서드를 정의한다고 해서 해당 타입의 인스턴스를 함수 호출 표현식 이외의 다른 컨텍스트에서 함수처럼 사용할 수 있는 것은 아니다. 예를 들어:

```swift
let someFunction1: (Int, Int) -> Void = callable(_:scale:)  // 오류
let someFunction2: (Int, Int) -> Void = callable.callAsFunction(_:scale:)
```

<!--
  - test: `call-as-function-err`

  ```swifttest
  >> struct CallableStruct {
  >>     var value: Int
  >>     func callAsFunction(_ number: Int, scale: Int) { }
  >> }
  >> let callable = CallableStruct(value: 100)
  -> let someFunction1: (Int, Int) -> Void = callable(_:scale:)  // 오류
  -> let someFunction2: (Int, Int) -> Void = callable.callAsFunction(_:scale:)
  >> _ = someFunction1 // 사용되지 않은 상수 경고 억제
  >> _ = someFunction2 // 사용되지 않은 상수 경고 억제
  !$ error: 'callable(_:scale:)'를 찾을 수 없음
  !! let someFunction1: (Int, Int) -> Void = callable(_:scale:)  // 오류
  !! ^~~~~~~~~~~~~~~~~~
  ```
-->

`subscript(dynamicMember:)` 서브스크립트는 멤버 조회를 위한 문법적 편의를 제공하며, <doc:Attributes#dynamicMemberLookup>에서 설명된다.


### 에러를 던지는 함수와 메서드

에러를 던질 수 있는 함수와 메서드는 `throws` 키워드로 표시한다. 이러한 함수와 메서드를 *에러 던지는 함수(throwing function)*와 *에러 던지는 메서드(throwing method)*라고 부른다. 이들의 기본 형태는 다음과 같다:

```swift
func <#function name#>(<#parameters#>) throws -> <#return type#> {
   <#statements#>
}
```

특정 타입의 에러를 던지는 함수는 다음과 같은 형태를 가진다:

```swift
func <#function name#>(<#parameters#>) throws(<#error type#>) -> <#return type#> {
   <#statements#>
}
```

에러를 던지는 함수나 메서드를 호출할 때는 반드시 `try` 또는 `try!` 표현식으로 감싸야 한다. 즉, `try` 또는 `try!` 연산자의 범위 내에서 호출해야 한다.

함수의 타입은 에러를 던질 수 있는지 여부와 어떤 타입의 에러를 던지는지를 포함한다. 이 하위 타입 관계는 예를 들어, 에러를 던지는 함수가 예상되는 곳에서 에러를 던지지 않는 함수를 사용할 수 있음을 의미한다. 에러를 던지는 함수의 타입에 대한 자세한 내용은 <doc:Types#Function-Type>을 참고한다. 명시적 타입을 가진 에러를 다루는 예제는 <doc:ErrorHandling#Specifying-the-Error-Type>에서 확인할 수 있다.

함수가 에러를 던질 수 있는지 여부만으로 함수를 오버로드할 수는 없다. 그러나 함수의 *파라미터*가 에러를 던질 수 있는지 여부를 기준으로 함수를 오버로드할 수는 있다.

에러를 던지는 메서드는 에러를 던지지 않는 메서드를 오버라이드할 수 없으며, 에러를 던지지 않는 메서드에 대한 프로토콜 요구사항을 충족할 수도 없다. 반면, 에러를 던지지 않는 메서드는 에러를 던지는 메서드를 오버라이드할 수 있고, 에러를 던지는 메서드에 대한 프로토콜 요구사항을 충족할 수 있다.


### 에러 재전달 함수와 메서드

함수나 메서드는 `rethrows` 키워드를 사용해 선언할 수 있다. 이 키워드는 해당 함수의 인자 중 하나가 에러를 던질 때만 에러를 던진다는 것을 의미한다. 이러한 함수와 메서드를 *에러 재전달 함수*와 *에러 재전달 메서드*라고 부른다. 에러 재전달 함수와 메서드는 최소한 하나 이상의 에러를 던지는 함수 인자를 포함해야 한다.

```swift
func someFunction(callback: () throws -> Void) rethrows {
    try callback()
}
```

<!--
  - test: `rethrows`

  ```swifttest
  -> func someFunction(callback: () throws -> Void) rethrows {
         try callback()
     }
  ```
-->

에러 재전달 함수나 메서드는 `catch` 절 내부에서만 `throw` 문을 사용할 수 있다. 이렇게 하면 `do`-`catch` 문 내부에서 에러를 던지는 함수를 호출하고, `catch` 절에서 다른 에러를 던지며 에러를 처리할 수 있다. 또한 `catch` 절은 에러 재전달 함수의 에러를 던지는 인자로부터 발생한 에러만 처리해야 한다. 예를 들어, 다음 코드는 `catch` 절이 `alwaysThrows()`에서 던진 에러를 처리하기 때문에 유효하지 않다.

```swift
func alwaysThrows() throws {
    throw SomeError.error
}
func someFunction(callback: () throws -> Void) rethrows {
    do {
        try callback()
        try alwaysThrows()  // 유효하지 않음, alwaysThrows()는 에러를 던지는 인자가 아님
    } catch {
        throw AnotherError.error
    }
}
```

<!--
  - test: `double-negative-rethrows`

  ```swifttest
  >> enum SomeError: Error { case error }
  >> enum AnotherError: Error { case error }
  -> func alwaysThrows() throws {
         throw SomeError.error
     }
  -> func someFunction(callback: () throws -> Void) rethrows {
        do {
           try callback()
           try alwaysThrows()  // Invalid, alwaysThrows() isn't a throwing parameter
        } catch {
           throw AnotherError.error
        }
     }
  !$ error: a function declared 'rethrows' may only throw if its parameter does
  !!               throw AnotherError.error
  !!               ^
  ```
-->

<!--
  - test: `throwing-in-rethrowing-function`

  ```swifttest
  -> enum SomeError: Error { case c, d }
  -> func f1(callback: () throws -> Void) rethrows {
         do {
             try callback()
         } catch {
             throw SomeError.c  // OK
         }
     }
  -> func f2(callback: () throws -> Void) rethrows {
         throw SomeError.d  // Error
     }
  !$ error: a function declared 'rethrows' may only throw if its parameter does
  !! throw SomeError.d  // Error
  !! ^
  ```
-->

에러를 던지는 메서드는 에러 재전달 메서드를 오버라이드할 수 없으며, 에러 재전달 메서드를 위한 프로토콜 요구사항을 충족할 수도 없다. 반면에, 에러 재전달 메서드는 에러를 던지는 메서드를 오버라이드할 수 있고, 에러를 던지는 메서드를 위한 프로토콜 요구사항을 충족할 수 있다.

에러 재전달 대신 제네릭 코드에서 특정 에러 타입을 던지는 방법도 있다. 예를 들면:

```swift
func someFunction<E: Error>(callback: () throws(E) -> Void) throws(E) {
    try callback()
}
```

이 방법은 에러에 대한 타입 정보를 보존한다. 하지만 `rethrows`로 함수를 표시하는 것과 달리, 이 방법은 동일한 타입의 에러를 던지는 것을 막지 않는다.

<!--
TODO: Revisit the comparison between rethrows and throws(E) above,
since it seems likely that the latter will generally replace the former.

See also rdar://128972373
-->


### 비동기 함수와 메서드

비동기적으로 실행되는 함수와 메서드는 반드시 `async` 키워드를 사용해 표시해야 한다. 이러한 함수와 메서드를 각각 *비동기 함수*와 *비동기 메서드*라고 부른다. 이들은 다음과 같은 형태를 가진다:

```swift
func <#function name#>(<#parameters#>) async -> <#return type#> {
   <#statements#>
}
```

비동기 함수나 메서드를 호출할 때는 반드시 `await` 표현식으로 감싸야 한다. 즉, `await` 연산자의 범위 내에서 호출해야 한다.

`async` 키워드는 함수의 타입에 포함되며, 동기 함수는 비동기 함수의 하위 타입이다. 따라서 비동기 함수가 필요한 상황에서 동기 함수를 사용할 수 있다. 예를 들어, 비동기 메서드를 동기 메서드로 재정의할 수 있으며, 동기 메서드가 비동기 메서드를 요구하는 프로토콜 요구사항을 충족할 수 있다.

함수가 비동기인지 여부에 따라 함수를 오버로드할 수 있다. 호출 지점에서 컨텍스트에 따라 어떤 오버로드가 사용될지 결정된다: 비동기 컨텍스트에서는 비동기 함수가 사용되고, 동기 컨텍스트에서는 동기 함수가 사용된다.

비동기 메서드는 동기 메서드를 재정의할 수 없으며, 동기 메서드를 요구하는 프로토콜 요구사항을 충족할 수 없다. 반면, 동기 메서드는 비동기 메서드를 재정의할 수 있고, 비동기 메서드를 요구하는 프로토콜 요구사항을 충족할 수 있다.

<!--
  - test: `sync-satisfy-async-protocol-requirements`

  ```swifttest
  >> protocol P { func f() async -> Int }
  >> class Super: P {
  >>     func f() async -> Int { return 12 }
  >> }
  >> class Sub: Super {
  >>     func f() -> Int { return 120 }
  >> }
  ```
-->


### 반환하지 않는 함수

Swift는 [`Never`][] 타입을 정의한다. 이 타입은 함수나 메서드가 호출자에게 제어를 반환하지 않음을 나타낸다. `Never` 반환 타입을 가진 함수와 메서드를 *nonreturning*이라고 부른다. Nonreturning 함수와 메서드는 복구할 수 없는 오류를 발생시키거나 무한히 지속되는 작업을 시작한다. 이는 호출 이후에 실행될 코드가 절대 실행되지 않음을 의미한다. Throwing과 rethrowing 함수는 nonreturning이더라도 적절한 `catch` 블록으로 프로그램 제어를 전달할 수 있다.

[`Never`]: https://developer.apple.com/documentation/swift/never

Nonreturning 함수나 메서드는 guard 문의 `else` 절을 마무리하기 위해 호출할 수 있다. 이는 <doc:Statements#Guard-Statement>에서 논의한 바와 같다.

Nonreturning 메서드를 오버라이드할 수 있지만, 새로운 메서드는 반환 타입과 nonreturning 동작을 유지해야 한다.

> 함수 선언 문법:
>
> *function-declaration* → *function-head* *function-name* *generic-parameter-clause*_?_ *function-signature* *generic-where-clause*_?_ *function-body*_?_
>
> *function-head* → *attributes*_?_ *declaration-modifiers*_?_ **`func`** \
> *function-name* → *identifier* | *operator*
>
> *function-signature* → *parameter-clause* **`async`**_?_ *throws-clause*_?_ *function-result*_?_ \
> *function-signature* → *parameter-clause* **`async`**_?_ **`rethrows`** *function-result*_?_ \
> *function-result* → **`->`** *attributes*_?_ *type* \
> *function-body* → *code-block*
>
> *parameter-clause* → **`(`** **`)`** | **`(`** *parameter-list* **`)`** \
> *parameter-list* → *parameter* | *parameter* **`,`** *parameter-list* \
> *parameter* → *external-parameter-name*_?_ *local-parameter-name* *parameter-type-annotation* *default-argument-clause*_?_ \
> *parameter* → *external-parameter-name*_?_ *local-parameter-name* *parameter-type-annotation* \
> *parameter* → *external-parameter-name*_?_ *local-parameter-name* *parameter-type-annotation* **`...`**
>
> *external-parameter-name* → *identifier* \
> *local-parameter-name* → *identifier* \
> *parameter-type-annotation* → **`:`** *attributes*_?_ *parameter-modifier*_?_ *type* \
> *parameter-modifier* → **`inout`** | **`borrowing`** | **`consuming`**
> *default-argument-clause* → **`=`** *expression*

<!--
  NOTE: 프로토콜 컨텍스트에서 코드 블록은 선택 사항이다.
  다른 모든 경우에는 필수이다.
  함수 정의/선언을 구분하도록 리팩토링할 수 있다.
  또한 저수준 "asm name" FFI가 있는데,
  이는 정의와 선언의 특수한 경우이다.
  이 차이는 본문에서 다루도록 한다.
-->


## 열거형 선언

열거형 선언은 프로그램에 이름이 있는 열거형 타입을 도입한다.

열거형 선언은 `enum` 키워드를 사용하며, 두 가지 기본 형태가 있다. 두 가지 형태 모두 열거형 본문에는 *열거형 케이스*라고 불리는 값이 0개 이상 포함될 수 있다. 또한 계산 속성, 인스턴스 메서드, 타입 메서드, 초기화 구문, 타입 별칭, 심지어 다른 열거형, 구조체, 클래스, 액터 선언도 포함할 수 있다. 단, 열거형 선언에는 디이니셜라이저나 프로토콜 선언은 포함할 수 없다.

열거형 타입은 여러 프로토콜을 채택할 수 있지만, 클래스, 구조체, 다른 열거형으로부터 상속받을 수는 없다.

클래스와 구조체와 달리, 열거형 타입은 암시적으로 제공되는 기본 초기화 구문이 없다. 모든 초기화 구문은 명시적으로 선언해야 한다. 초기화 구문은 열거형 내의 다른 초기화 구문에 위임할 수 있지만, 초기화 과정은 초기화 구문이 `self`에 열거형 케이스 중 하나를 할당한 후에야 완료된다.

구조체와 마찬가지로 클래스와 달리, 열거형은 값 타입이다. 열거형 인스턴스는 변수나 상수에 할당되거나 함수 호출 시 인자로 전달될 때 복사된다. 값 타입에 대한 자세한 내용은 <doc:ClassesAndStructures#Structures-and-Enumerations-Are-Value-Types>를 참조한다.

<doc:Declarations#Extension-Declaration>에서 설명한 것처럼, 확장 선언을 통해 열거형 타입의 동작을 확장할 수 있다.


### 다양한 타입을 가진 열거형 케이스

다음은 다양한 타입의 열거형 케이스를 포함하는 열거형 타입을 선언하는 형식이다:

```swift
enum <#enumeration name#>: <#adopted protocols#> {
    case <#enumeration case 1#>
    case <#enumeration case 2#>(<#associated value types#>)
}
```

이 방식으로 선언된 열거형은 다른 프로그래밍 언어에서 *구분된 유니온(discriminated unions)* 이라고도 불린다.

이 형식에서 각 케이스 블록은 `case` 키워드 뒤에 하나 이상의 열거형 케이스를 쉼표로 구분하여 작성한다. 각 케이스의 이름은 고유해야 한다. 또한 각 케이스는 특정 타입의 값을 저장할 수 있다. 이 타입들은 케이스 이름 바로 뒤에 *연관 값 타입(associated value types)* 튜플로 지정된다.

연관 값을 저장하는 열거형 케이스는 해당 연관 값을 가진 열거형 인스턴스를 생성하는 함수처럼 사용할 수 있다. 그리고 함수와 마찬가지로, 열거형 케이스에 대한 참조를 얻어 나중에 코드에서 적용할 수 있다.

```swift
enum Number {
    case integer(Int)
    case real(Double)
}
let f = Number.integer
// f는 (Int) -> Number 타입의 함수이다

// f를 적용해 정수 값을 가진 Number 인스턴스 배열 생성
let evenInts: [Number] = [0, 2, 4, 6].map(f)
```

<!--
  - test: `enum-case-as-function`

  ```swifttest
  -> enum Number {
        case integer(Int)
        case real(Double)
     }
  -> let f = Number.integer
  -> // f는 (Int) -> Number 타입의 함수이다

  -> // f를 적용해 정수 값을 가진 Number 인스턴스 배열 생성
  -> let evenInts: [Number] = [0, 2, 4, 6].map(f)
  ```
-->

<!--
  evenInts에 대한 기대값은 없음. print()를 사용하면 Number 앞에 tmpabc와 같은 모듈 접두사가 붙어서
  기대값을 정규식으로 작성해야 하며(현재는 지원하지 않음), assert()를 사용하려면 Number가 Equatable을 준수해야 함.
-->

연관 값 타입을 가진 케이스에 대한 더 많은 정보와 예제는 <doc:Enumerations#Associated-Values>를 참고한다.


#### 간접 참조를 사용하는 열거형

열거형은 재귀적인 구조를 가질 수 있다. 즉, 열거형 타입 자체의 인스턴스를 연관 값으로 가지는 케이스를 정의할 수 있다. 하지만 열거형 타입의 인스턴스는 값 의미론(value semantics)을 가지기 때문에 메모리에 고정된 레이아웃을 가진다. 재귀를 지원하기 위해 컴파일러는 간접 참조(indirection) 계층을 추가해야 한다.

특정 열거형 케이스에 대해 간접 참조를 활성화하려면 `indirect` 선언 수식어를 사용한다. 간접 참조 케이스는 반드시 연관 값을 가져야 한다.

```swift
enum Tree<T> {
    case empty
    indirect case node(value: T, left: Tree, right: Tree)
}
```

연관 값을 가지는 모든 열거형 케이스에 대해 간접 참조를 활성화하려면 전체 열거형에 `indirect` 수식어를 붙인다. 이는 `indirect` 수식어를 각 케이스에 일일이 붙여야 하는 번거로움을 줄여준다.

`indirect` 수식어가 붙은 열거형은 연관 값을 가지는 케이스와 그렇지 않은 케이스를 혼합하여 포함할 수 있다. 하지만 이미 `indirect` 수식어가 붙은 케이스를 포함할 수는 없다.


### 원시 값 타입을 가진 열거형

다음 형식은 동일한 기본 타입의 원시 값을 가지는 열거형 케이스로 구성된 열거형을 선언한다:

```swift
enum <#열거형 이름#>: <#원시 값 타입#>, <#채택한 프로토콜#> {
    case <#열거형 케이스 1#> = <#원시 값 1#>
    case <#열거형 케이스 2#> = <#원시 값 2#>
}
```

이 형식에서 각 케이스 블록은 `case` 키워드로 시작하며, 쉼표로 구분된 하나 이상의 열거형 케이스로 구성된다. 첫 번째 형식과 달리, 각 케이스는 동일한 기본 타입의 *원시 값*이라는 내부 값을 가진다. 이 값의 타입은 *원시 값 타입*으로 지정되며, 정수, 부동소수점 숫자, 문자열 또는 단일 문자를 나타내야 한다. 특히, *원시 값 타입*은 `Equatable` 프로토콜과 다음 프로토콜 중 하나를 준수해야 한다: 정수 리터럴을 위한 `ExpressibleByIntegerLiteral`, 부동소수점 리터럴을 위한 `ExpressibleByFloatLiteral`, 여러 문자를 포함하는 문자열 리터럴을 위한 `ExpressibleByStringLiteral`, 단일 문자를 포함하는 문자열 리터럴을 위한 `ExpressibleByUnicodeScalarLiteral` 또는 `ExpressibleByExtendedGraphemeClusterLiteral`. 각 케이스는 고유한 이름을 가지고 고유한 원시 값이 할당되어야 한다.

<!--
  위의 ExpressibleBy... 프로토콜 목록은 LexicalStructure_Literals에도 등장한다.
  이 목록은 더 짧은데, 이 다섯 가지 프로토콜이 컴파일러에서 명시적으로 지원되기 때문이다.
-->

원시 값 타입이 `Int`로 지정되고 케이스에 명시적으로 값을 할당하지 않으면, 케이스는 암시적으로 `0`, `1`, `2` 등의 값을 할당받는다. `Int` 타입의 할당되지 않은 각 케이스는 이전 케이스의 원시 값에서 자동으로 증가한 값을 암시적으로 할당받는다.

```swift
enum ExampleEnum: Int {
    case a, b, c = 5, d
}
```

<!--
  - test: `raw-value-enum`

  ```swifttest
  -> enum ExampleEnum: Int {
        case a, b, c = 5, d
     }
  ```
-->

위 예제에서 `ExampleEnum.a`의 원시 값은 `0`이고, `ExampleEnum.b`의 값은 `1`이다. 그리고 `ExampleEnum.c`의 값이 명시적으로 `5`로 설정되었기 때문에, `ExampleEnum.d`의 값은 `5`에서 자동으로 증가하여 `6`이 된다.

원시 값 타입이 `String`으로 지정되고 케이스에 값을 명시적으로 할당하지 않으면, 할당되지 않은 각 케이스는 해당 케이스 이름과 동일한 텍스트를 가진 문자열을 암시적으로 할당받는다.

```swift
enum GamePlayMode: String {
    case cooperative, individual, competitive
}
```

<!--
  - test: `raw-value-enum-implicit-string-values`

  ```swifttest
  -> enum GamePlayMode: String {
        case cooperative, individual, competitive
     }
  ```
-->

위 예제에서 `GamePlayMode.cooperative`의 원시 값은 `"cooperative"`이고, `GamePlayMode.individual`의 원시 값은 `"individual"`, `GamePlayMode.competitive`의 원시 값은 `"competitive"`이다.

원시 값 타입을 가진 열거형 케이스는 Swift 표준 라이브러리에 정의된 `RawRepresentable` 프로토콜을 암시적으로 준수한다. 결과적으로, 이 열거형은 `rawValue` 프로퍼티와 `init?(rawValue: RawValue)` 시그니처를 가진 실패 가능한 초기화자를 제공한다. `rawValue` 프로퍼티를 사용해 열거형 케이스의 원시 값에 접근할 수 있다. 예를 들어, `ExampleEnum.b.rawValue`와 같이 사용한다. 또한 원시 값을 사용해 해당 케이스를 찾을 수도 있다. 예를 들어, `ExampleEnum(rawValue: 5)`와 같이 호출하면 옵셔널 케이스를 반환한다. 원시 값 타입을 가진 케이스에 대한 더 많은 정보와 예제는 <doc:Enumerations#Raw-Values>를 참고한다.


### 열거형 케이스 접근하기

열거형 타입의 케이스를 참조하려면 점(`.`) 문법을 사용한다. 예를 들어 `EnumerationType.enumerationCase`와 같이 쓸 수 있다. 문맥에서 열거형 타입을 유추할 수 있는 경우, 타입을 생략할 수 있다. (점은 여전히 필요하다.) 이 내용은 <doc:Enumerations#Enumeration-Syntax>와 <doc:Expressions#Implicit-Member-Expression>에서 자세히 설명한다.

열거형 케이스의 값을 확인하려면 `switch` 문을 사용한다. 이 내용은 <doc:Enumerations#Matching-Enumeration-Values-with-a-Switch-Statement>에서 예제와 함께 설명한다. 열거형 타입은 `switch` 문의 케이스 블록에서 열거형 케이스 패턴과 패턴 매칭을 수행한다. 이 내용은 <doc:Patterns#Enumeration-Case-Pattern>에서 다룬다.

<!--
  FIXME: 또는 if-case를 사용할 수 있다:
  enum E { case c(Int) }
  let e = E.c(100)
  if case E.c(let i) = e { print(i) }
  // 출력: 100
-->

<!--
  NOTE: 프로토콜 타입을 raw-value 타입으로 사용해 프로토콜 채택을 요구할 수 있다.
  하지만 raw 값을 지정하려면 =를 지원하는 타입 중 하나여야 한다.
  <#raw-value type, protocol conformance#>를 가질 수 있다.
  업데이트: 하나의 raw-value 타입만 지정할 수 있다.
  이에 따라 문법을 더 엄격하게 수정했다.
-->

<!--
  NOTE: Doug과 Ted에 따르면, "('->' type)?"는 문법의 일부가 아니다.
  아래 문법에서 이를 제거했다.
-->

> 열거형 선언의 문법:
>
> *enum-declaration* → *attributes*_?_ *access-level-modifier*_?_ *union-style-enum* \
> *enum-declaration* → *attributes*_?_ *access-level-modifier*_?_ *raw-value-style-enum*
>
> *union-style-enum* → **`indirect`**_?_ **`enum`** *enum-name* *generic-parameter-clause*_?_ *type-inheritance-clause*_?_ *generic-where-clause*_?_ **`{`** *union-style-enum-members*_?_ **`}`** \
> *union-style-enum-members* → *union-style-enum-member* *union-style-enum-members*_?_ \
> *union-style-enum-member* → *declaration* | *union-style-enum-case-clause* | *compiler-control-statement* \
> *union-style-enum-case-clause* → *attributes*_?_ **`indirect`**_?_ **`case`** *union-style-enum-case-list* \
> *union-style-enum-case-list* → *union-style-enum-case* | *union-style-enum-case* **`,`** *union-style-enum-case-list* \
> *union-style-enum-case* → *enum-case-name* *tuple-type*_?_ \
> *enum-name* → *identifier* \
> *enum-case-name* → *identifier*
>
> *raw-value-style-enum* → **`enum`** *enum-name* *generic-parameter-clause*_?_ *type-inheritance-clause* *generic-where-clause*_?_ **`{`** *raw-value-style-enum-members* **`}`** \
> *raw-value-style-enum-members* → *raw-value-style-enum-member* *raw-value-style-enum-members*_?_ \
> *raw-value-style-enum-member* → *declaration* | *raw-value-style-enum-case-clause* | *compiler-control-statement* \
> *raw-value-style-enum-case-clause* → *attributes*_?_ **`case`** *raw-value-style-enum-case-list* \
> *raw-value-style-enum-case-list* → *raw-value-style-enum-case* | *raw-value-style-enum-case* **`,`** *raw-value-style-enum-case-list* \
> *raw-value-style-enum-case* → *enum-case-name* *raw-value-assignment*_?_ \
> *raw-value-assignment* → **`=`** *raw-value-literal* \
> *raw-value-literal* → *numeric-literal* | *static-string-literal* | *boolean-literal*

<!--
  NOTE: 두 종류의 열거형은 충분히 다르기 때문에 문법을 분리할 필요가 있다.
  ([Contributor 6004]이 이메일에서 이 점을 지적했다.)
  두 종류의 열거형에 대해 선택한 이름이 마음에 들지는 않는다.
  더 나은 이름을 생각할 수 있다면 알려주길 바란다. (Tim과 Dave는 이 이름에 동의했다!)
  union-style-enum이라는 이름을 선택한 이유는 이 종류의 열거형이 일반적인 열거형 타입이 아니라
  구분된 합집합(discriminated union)처럼 동작하기 때문이다.
  이들은 ADT(Algebraic Data Types)의 용어로 "합" 타입의 일종이다.
  F#과 같은 함수형 언어는 실제로 두 종류의 타입(구분된 합집합과 열거형 타입)을 모두 가지고 있다.
  왜냐하면 이들은 서로 다르게 동작하기 때문이다.
  왜 우리가 이 두 종류를 하나로 합쳤는지 잘 모르겠다.
  특히 이들은 서로 다른 선언 요구 사항을 가지고 있고, 동작 방식도 다르다.
-->


## 구조체 선언

*구조체 선언*은 프로그램 내에 이름이 있는 구조체 타입을 도입한다. 구조체 선언은 `struct` 키워드를 사용하며 다음과 같은 형태를 가진다:

```swift
struct <#구조체 이름#>: <#채택한 프로토콜#> {
   <#선언문#>
}
```

구조체의 본문에는 0개 이상의 *선언문*이 포함될 수 있다. 이 *선언문*은 저장 프로퍼티와 계산 프로퍼티, 타입 프로퍼티, 인스턴스 메서드, 타입 메서드, 초기화 구문, 서브스크립트, 타입 별칭, 그리고 다른 구조체, 클래스, 액터, 열거형 선언까지 포함할 수 있다. 단, 구조체 선언은 디이니셜라이저나 프로토콜 선언을 포함할 수 없다. 다양한 종류의 선언문을 포함한 구조체에 대한 논의와 예제는 <doc:ClassesAndStructures>에서 확인할 수 있다.

구조체 타입은 여러 프로토콜을 채택할 수 있지만, 클래스, 열거형, 또는 다른 구조체로부터 상속받을 수는 없다.

이미 선언된 구조체의 인스턴스를 생성하는 방법은 세 가지가 있다:

- 구조체 내부에 선언된 초기화 구문 중 하나를 호출한다. 이는 <doc:Initialization#Initializers>에서 설명한다.
- 초기화 구문이 선언되지 않은 경우, 구조체의 멤버별 초기화 구문을 호출한다. 이는 <doc:Initialization#Memberwise-Initializers-for-Structure-Types>에서 설명한다.
- 초기화 구문이 선언되지 않고, 구조체 선언의 모든 프로퍼티에 초기값이 지정된 경우, 구조체의 기본 초기화 구문을 호출한다. 이는 <doc:Initialization#Default-Initializers>에서 설명한다.

구조체의 선언된 프로퍼티를 초기화하는 과정은 <doc:Initialization>에서 설명한다.

구조체 인스턴스의 프로퍼티는 점(`.`) 문법을 사용해 접근할 수 있다. 이는 <doc:ClassesAndStructures#Accessing-Properties>에서 설명한다.

구조체는 값 타입이다. 따라서 구조체의 인스턴스는 변수나 상수에 할당되거나 함수 호출의 인자로 전달될 때 복사된다. 값 타입에 대한 자세한 정보는 <doc:ClassesAndStructures#Structures-and-Enumerations-Are-Value-Types>에서 확인할 수 있다.

구조체 타입의 동작을 확장하려면 확장 선언을 사용할 수 있다. 이는 <doc:Declarations#Extension-Declaration>에서 논의한다.

> 구조체 선언의 문법:
>
> *struct-declaration* → *attributes*_?_ *access-level-modifier*_?_ **`struct`** *struct-name* *generic-parameter-clause*_?_ *type-inheritance-clause*_?_ *generic-where-clause*_?_ *struct-body* \
> *struct-name* → *identifier* \
> *struct-body* → **`{`** *struct-members*_?_ **`}`**
>
> *struct-members* → *struct-member* *struct-members*_?_ \
> *struct-member* → *declaration* | *compiler-control-statement*


## 클래스 선언

*클래스 선언*은 프로그램에 이름이 있는 클래스 타입을 도입한다. 클래스 선언은 `class` 키워드를 사용하며 다음과 같은 형태를 가진다:

```swift
class <#클래스 이름#>: <#슈퍼클래스#>, <#채택한 프로토콜#> {
   <#선언#>
}
```

클래스의 본문에는 0개 이상의 *선언*이 포함될 수 있다. 이러한 *선언*에는 저장 프로퍼티와 계산 프로퍼티, 인스턴스 메서드, 타입 메서드, 초기화 구문, 단일 소멸자, 서브스크립트, 타입 별칭, 그리고 심지어 다른 클래스, 구조체, 액터, 열거형 선언도 포함될 수 있다. 단, 클래스 선언에는 프로토콜 선언을 포함할 수 없다. 다양한 종류의 선언을 포함한 클래스에 대한 논의와 예제는 <doc:ClassesAndStructures>를 참고한다.

클래스 타입은 하나의 부모 클래스, 즉 *슈퍼클래스*로부터만 상속받을 수 있지만, 임의의 수의 프로토콜을 채택할 수 있다. *슈퍼클래스*는 *클래스 이름*과 콜론 뒤에 먼저 표시되며, 그 다음에 *채택한 프로토콜*이 이어진다. 제네릭 클래스는 다른 제네릭 및 비제네릭 클래스로부터 상속받을 수 있지만, 비제네릭 클래스는 다른 비제네릭 클래스로부터만 상속받을 수 있다. 콜론 뒤에 제네릭 슈퍼클래스의 이름을 작성할 때는 제네릭 매개변수 절을 포함한 전체 이름을 명시해야 한다.

<doc:Declarations#Initializer-Declaration>에서 설명한 것처럼, 클래스는 지정 초기화 구문과 편의 초기화 구문을 가질 수 있다. 클래스의 지정 초기화 구문은 클래스의 모든 선언된 프로퍼티를 초기화해야 하며, 슈퍼클래스의 지정 초기화 구문을 호출하기 전에 이를 완료해야 한다.

클래스는 슈퍼클래스의 프로퍼티, 메서드, 서브스크립트, 초기화 구문을 재정의할 수 있다. 재정의된 프로퍼티, 메서드, 서브스크립트, 지정 초기화 구문은 `override` 선언 수식어로 표시해야 한다.

<!--
  - test: `designatedInitializersRequireOverride`

  ```swifttest
  -> class C { init() {} }
  -> class D: C { override init() { super.init() } }
  ```
-->

서브클래스가 슈퍼클래스의 초기화 구문을 구현하도록 요구하려면, 슈퍼클래스의 초기화 구문에 `required` 선언 수식어를 표시한다. 서브클래스에서 해당 초기화 구문을 구현할 때도 `required` 선언 수식어를 표시해야 한다.

*슈퍼클래스*에 선언된 프로퍼티와 메서드는 현재 클래스에 상속되지만, *슈퍼클래스*에 선언된 지정 초기화 구문은 서브클래스가 <doc:Initialization#Automatic-Initializer-Inheritance>에 설명된 조건을 충족할 때만 상속된다. Swift 클래스는 범용 베이스 클래스로부터 상속받지 않는다.

이전에 선언된 클래스의 인스턴스를 생성하는 방법은 두 가지가 있다:

- 클래스 내부에 선언된 초기화 구문 중 하나를 호출한다. 이는 <doc:Initialization#Initializers>에 설명되어 있다.
- 초기화 구문이 선언되지 않고, 클래스 선언의 모든 프로퍼티에 초기값이 제공된 경우, 클래스의 기본 초기화 구문을 호출한다. 이는 <doc:Initialization#Default-Initializers>에 설명되어 있다.

클래스 인스턴스의 프로퍼티에 접근하려면 점(`.`) 구문을 사용한다. 이는 <doc:ClassesAndStructures#Accessing-Properties>에 설명되어 있다.

클래스는 참조 타입이다. 클래스의 인스턴스는 변수나 상수에 할당되거나 함수 호출의 인자로 전달될 때 복사되지 않고 참조된다. 참조 타입에 대한 자세한 내용은 <doc:ClassesAndStructures#Classes-Are-Reference-Types>를 참고한다.

클래스 타입의 동작을 확장하려면 확장 선언을 사용할 수 있다. 이는 <doc:Declarations#Extension-Declaration>에서 논의된다.

> 클래스 선언의 문법:
>
> *class-declaration* → *attributes*_?_ *access-level-modifier*_?_ **`final`**_?_ **`class`** *class-name* *generic-parameter-clause*_?_ *type-inheritance-clause*_?_ *generic-where-clause*_?_ *class-body* \
> *class-declaration* → *attributes*_?_ **`final`** *access-level-modifier*_?_ **`class`** *class-name* *generic-parameter-clause*_?_ *type-inheritance-clause*_?_ *generic-where-clause*_?_ *class-body* \
> *class-name* → *identifier* \
> *class-body* → **`{`** *class-members*_?_ **`}`**
>
> *class-members* → *class-member* *class-members*_?_ \
> *class-member* → *declaration* | *compiler-control-statement*


## 액터 선언

*액터 선언*은 프로그램에 이름이 있는 액터 타입을 도입한다. 액터 선언은 `actor` 키워드를 사용하며 다음과 같은 형태를 가진다:

```swift
actor <#액터 이름#>: <#채택한 프로토콜#> {
    <#선언#>
}
```

액터의 본문에는 0개 이상의 *선언*이 포함된다. 이러한 *선언*은 저장 프로퍼티와 계산 프로퍼티, 인스턴스 메서드, 타입 메서드, 이니셜라이저, 단일 디이니셜라이저, 서브스크립트, 타입 별칭, 그리고 다른 클래스, 구조체, 열거형 선언까지 포함할 수 있다. 다양한 종류의 선언을 포함하는 액터에 대한 설명과 예제는 <doc:Concurrency#Actors>를 참고한다.

액터 타입은 여러 프로토콜을 채택할 수 있지만, 클래스, 열거형, 구조체, 또는 다른 액터로부터 상속받을 수는 없다. 그러나 `@objc` 속성이 붙은 액터는 암시적으로 `NSObjectProtocol` 프로토콜을 준수하며, Objective-C 런타임에서 `NSObject`의 하위 타입으로 노출된다.

이미 선언된 액터의 인스턴스를 생성하는 방법은 두 가지이다:

- 액터 내부에 선언된 이니셜라이저 중 하나를 호출한다. 이에 대한 자세한 내용은 <doc:Initialization#Initializers>를 참고한다.
- 이니셜라이저가 선언되지 않고, 액터 선언의 모든 프로퍼티에 초기값이 지정된 경우, 액터의 기본 이니셜라이저를 호출한다. 이에 대한 자세한 내용은 <doc:Initialization#Default-Initializers>를 참고한다.

기본적으로 액터의 멤버는 해당 액터에 격리된다. 메서드의 본문이나 프로퍼티의 getter와 같은 코드는 해당 액터에서 실행된다. 액터 내부의 코드는 동일한 액터에서 실행되기 때문에 동기적으로 상호작용할 수 있지만, 액터 외부의 코드는 `await`를 사용해 다른 액터에서 비동기적으로 실행되는 코드임을 표시해야 한다. 키 경로는 액터의 격리된 멤버를 참조할 수 없다. 액터에 격리된 저장 프로퍼티는 동기 함수에 in-out 파라미터로 전달할 수 있지만, 비동기 함수에는 전달할 수 없다.

액터는 `nonisolated` 키워드로 표시된 비격리 멤버를 가질 수도 있다. 비격리 멤버는 액터 외부의 코드처럼 실행된다. 액터의 격리된 상태와 상호작용할 수 없으며, 호출자가 사용할 때 `await`를 표시할 필요가 없다.

액터의 멤버는 비격리 멤버이거나 비동기 멤버인 경우에만 `@objc` 속성을 표시할 수 있다.

액터의 선언된 프로퍼티를 초기화하는 과정은 <doc:Initialization>에 설명되어 있다.

액터 인스턴스의 프로퍼티는 점(`.`) 문법을 사용해 접근할 수 있다. 이에 대한 자세한 내용은 <doc:ClassesAndStructures#Accessing-Properties>를 참고한다.

액터는 참조 타입이다. 액터의 인스턴스는 변수나 상수에 할당되거나 함수 호출의 인자로 전달될 때 복사되지 않고 참조된다. 참조 타입에 대한 자세한 내용은 <doc:ClassesAndStructures#Classes-Are-Reference-Types>를 참고한다.

액터 타입의 동작을 확장 선언으로 확장할 수 있다. 이에 대한 자세한 내용은 <doc:Declarations#Extension-Declaration>을 참고한다.

<!--
  TODO SE-0306 액터 제안에서 추가된 내용:

  격리된 함수의 부분 적용은 표현식이 비탈출 및 비-Sendable 파라미터에 해당하는 직접적인 인자인 경우에만 허용된다.
-->

> 액터 선언의 문법:
>
> *actor-declaration* → *attributes*_?_ *access-level-modifier*_?_ **`actor`** *actor-name* *generic-parameter-clause*_?_ *type-inheritance-clause*_?_ *generic-where-clause*_?_ *actor-body* \
> *actor-name* → *identifier* \
> *actor-body* → **`{`** *actor-members*_?_ **`}`**
>
> *actor-members* → *actor-member* *actor-members*_?_ \
> *actor-member* → *declaration* | *compiler-control-statement*


## 프로토콜 선언

*프로토콜 선언*은 프로그램에 이름이 붙은 프로토콜 타입을 도입한다. 프로토콜 선언은 `protocol` 키워드를 사용하며, 다음과 같은 형태를 가진다:

```swift
protocol <#프로토콜 이름#>: <#상속받은 프로토콜#> {
   <#프로토콜 멤버 선언#>
}
```

프로토콜 선언은 전역 범위에 나타날 수도 있고, 제네릭이 아닌 타입이나 제네릭이 아닌 함수 내부에 중첩될 수도 있다.

프로토콜의 본문에는 0개 이상의 *프로토콜 멤버 선언*이 포함된다. 이는 프로토콜을 채택한 타입이 반드시 준수해야 하는 요구사항을 설명한다. 특히, 프로토콜은 채택한 타입이 특정 프로퍼티, 메서드, 이니셜라이저, 그리고 서브스크립트를 구현해야 한다고 선언할 수 있다. 프로토콜은 또한 *연관 타입*이라는 특별한 종류의 타입 별칭을 선언할 수 있으며, 이를 통해 프로토콜의 다양한 선언 간의 관계를 지정할 수 있다. 프로토콜 선언에는 클래스, 구조체, 열거형, 또는 다른 프로토콜 선언을 포함할 수 없다. *프로토콜 멤버 선언*에 대해서는 아래에서 자세히 설명한다.

프로토콜 타입은 여러 다른 프로토콜을 상속받을 수 있다. 프로토콜 타입이 다른 프로토콜을 상속받으면, 해당 프로토콜의 요구사항 집합이 통합된다. 그리고 현재 프로토콜을 상속받는 모든 타입은 이 모든 요구사항을 준수해야 한다. 프로토콜 상속을 사용하는 예제는 <doc:Protocols#Protocol-Inheritance>를 참조한다.

> 참고: 여러 프로토콜의 준수 요구사항을 통합하려면 프로토콜 합성 타입을 사용할 수도 있다. 이에 대한 자세한 내용은 <doc:Types#Protocol-Composition-Type>과 <doc:Protocols#Protocol-Composition>을 참조한다.

이미 선언된 타입에 프로토콜 준수를 추가하려면 해당 타입의 익스텐션 선언에서 프로토콜을 채택하면 된다. 익스텐션에서는 채택한 프로토콜의 모든 요구사항을 구현해야 한다. 타입이 이미 모든 요구사항을 구현했다면, 익스텐션 선언의 본문을 비워둘 수 있다.

기본적으로, 프로토콜을 준수하는 타입은 프로토콜에 선언된 모든 프로퍼티, 메서드, 그리고 서브스크립트를 구현해야 한다. 그러나 `optional` 선언 수식어를 사용해 프로토콜 멤버 선언을 표시하면, 준수 타입에서 이들의 구현을 선택적으로 할 수 있다. `optional` 수식어는 `objc` 속성이 표시된 멤버에만 적용할 수 있으며, `objc` 속성이 표시된 프로토콜의 멤버에만 적용할 수 있다. 결과적으로, 선택적 멤버 요구사항이 포함된 프로토콜을 채택하고 준수할 수 있는 것은 클래스 타입뿐이다. `optional` 선언 수식어를 사용하는 방법과 선택적 프로토콜 멤버에 접근하는 방법에 대한 자세한 내용은 <doc:Protocols#Optional-Protocol-Requirements>를 참조한다.

열거형의 케이스는 타입 멤버에 대한 프로토콜 요구사항을 충족할 수 있다. 특히, 연관 값이 없는 열거형 케이스는 `Self` 타입의 읽기 전용 타입 변수에 대한 프로토콜 요구사항을 충족하며, 연관 값이 있는 열거형 케이스는 `Self`를 반환하고 매개변수와 인자 레이블이 케이스의 연관 값과 일치하는 함수에 대한 프로토콜 요구사항을 충족한다. 예를 들어:

```swift
protocol SomeProtocol {
    static var someValue: Self { get }
    static func someFunction(x: Int) -> Self
}
enum MyEnum: SomeProtocol {
    case someValue
    case someFunction(x: Int)
}
```

프로토콜의 채택을 클래스 타입으로만 제한하려면, 콜론 뒤의 *상속받은 프로토콜* 목록에 `AnyObject` 프로토콜을 포함하면 된다. 예를 들어, 다음 프로토콜은 클래스 타입만 채택할 수 있다:

```swift
protocol SomeProtocol: AnyObject {
    /* 프로토콜 멤버는 여기에 작성 */
}
```

`AnyObject` 요구사항이 표시된 프로토콜을 상속받은 프로토콜 역시 클래스 타입만 채택할 수 있다.

> 참고: 프로토콜이 `objc` 속성으로 표시된 경우, `AnyObject` 요구사항이 암시적으로 적용된다. 따라서 프로토콜에 `AnyObject` 요구사항을 명시적으로 표시할 필요는 없다.

프로토콜은 이름이 붙은 타입이므로, 코드에서 다른 이름이 붙은 타입과 동일한 위치에 나타날 수 있다. 이에 대한 자세한 내용은 <doc:Protocols#Protocols-as-Types>에서 다룬다. 그러나 프로토콜의 인스턴스를 생성할 수는 없다. 프로토콜은 실제로 지정한 요구사항에 대한 구현을 제공하지 않기 때문이다.

프로토콜을 사용해 클래스나 구조체의 델리게이트가 구현해야 하는 메서드를 선언할 수 있다. 이에 대한 자세한 내용은 <doc:Protocols#Delegation>에서 설명한다.

> 프로토콜 선언의 문법:
>
> *protocol-declaration* → *attributes*_?_ *access-level-modifier*_?_ **`protocol`** *protocol-name* *type-inheritance-clause*_?_ *generic-where-clause*_?_ *protocol-body* \
> *protocol-name* → *identifier* \
> *protocol-body* → **`{`** *protocol-members*_?_ **`}`**
>
> *protocol-members* → *protocol-member* *protocol-members*_?_ \
> *protocol-member* → *protocol-member-declaration* | *compiler-control-statement*
>
> *protocol-member-declaration* → *protocol-property-declaration* \
> *protocol-member-declaration* → *protocol-method-declaration* \
> *protocol-member-declaration* → *protocol-initializer-declaration* \
> *protocol-member-declaration* → *protocol-subscript-declaration* \
> *protocol-member-declaration* → *protocol-associated-type-declaration* \
> *protocol-member-declaration* → *typealias-declaration*


### 프로토콜 프로퍼티 선언

프로토콜은 특정 타입이 프로퍼티를 구현해야 한다는 요구사항을 정의한다. 이를 위해 프로토콜 선언 내부에 *프로토콜 프로퍼티 선언*을 포함한다. 프로토콜 프로퍼티 선언은 변수 선언의 특수한 형태를 가진다.

```swift
var <#프로퍼티 이름#>: <#타입#> { get set }
```

다른 프로토콜 멤버 선언과 마찬가지로, 프로토콜 프로퍼티 선언은 해당 프로토콜을 준수하는 타입이 구현해야 하는 getter와 setter 요구사항만을 정의한다. 따라서 프로토콜 내부에서 직접 getter나 setter를 구현하지 않는다.

getter와 setter 요구사항은 준수 타입에서 다양한 방식으로 충족될 수 있다. 프로퍼티 선언에 `get`과 `set` 키워드가 모두 포함된 경우, 준수 타입은 저장 프로퍼티 또는 읽기와 쓰기가 모두 가능한 계산 프로퍼티(즉, getter와 setter를 모두 구현한 프로퍼티)로 이를 구현할 수 있다. 그러나 상수 프로퍼티나 읽기 전용 계산 프로퍼티로는 구현할 수 없다. 프로퍼티 선언에 `get` 키워드만 포함된 경우, 어떤 종류의 프로퍼티로도 구현할 수 있다. 프로토콜의 프로퍼티 요구사항을 준수하는 타입의 예시는 <doc:Protocols#Property-Requirements>를 참고한다.

프로토콜 선언에서 타입 프로퍼티 요구사항을 선언하려면, 프로퍼티 선언에 `static` 키워드를 추가한다. 프로토콜을 준수하는 구조체와 열거형은 `static` 키워드를 사용해 프로퍼티를 선언하고, 클래스는 `static` 또는 `class` 키워드를 사용해 프로퍼티를 선언한다. 구조체, 열거형, 클래스에 프로토콜 준수를 추가하는 익스텐션은 해당 타입이 사용하는 키워드와 동일한 키워드를 사용한다. 타입 프로퍼티 요구사항에 대한 기본 구현을 제공하는 익스텐션은 `static` 키워드를 사용한다.

<!--
  - test: `protocols-with-type-property-requirements`

  ```swifttest
  -> protocol P { static var x: Int { get } }
  -> protocol P2 { class var x: Int { get } }
  !$ error: class properties are only allowed within classes; use 'static' to declare a requirement fulfilled by either a static or class property
  !! protocol P2 { class var x: Int { get } }
  !!              ~~~~~ ^
  !!              static
  -> struct S: P { static var x = 10 }
  -> class C1: P { static var x = 20 }
  -> class C2: P { class var x = 30 }
  !$ error: class stored properties not supported in classes; did you mean 'static'?
  !! class C2: P { class var x = 30 }
  !!               ~~~~~     ^
  ```
-->

<!--
  - test: `protocol-type-property-default-implementation`

  ```swifttest
  -> protocol P { static var x: Int { get } }
  -> extension P { static var x: Int { return 100 } }
  -> struct S1: P { }
  -> print(S1.x)
  <- 100
  -> struct S2: P { static var x = 10 }
  -> print(S2.x)
  <- 10
  ```
-->

자세한 내용은 <doc:Declarations#Variable-Declaration>을 참고한다.

> 프로토콜 프로퍼티 선언 문법:
>
> *protocol-property-declaration* → *variable-declaration-head* *variable-name* *type-annotation* *getter-setter-keyword-block*


### 프로토콜 메서드 선언

프로토콜은 특정 타입이 해당 프로토콜을 준수하려면 반드시 구현해야 하는 메서드를 정의한다. 프로토콜 메서드 선언은 함수 선언과 비슷한 형태를 가지지만, 두 가지 중요한 차이점이 있다. 첫째, 메서드 본문을 포함하지 않는다. 둘째, 함수 선언에서 기본 매개변수 값을 제공할 수 없다. 프로토콜의 메서드 요구사항을 구현한 타입의 예제는 <doc:Protocols#Method-Requirements>를 참고한다.

프로토콜 선언에서 클래스 메서드나 정적 메서드 요구사항을 선언하려면, 메서드 선언에 `static` 선언 수정자를 추가한다. 이 프로토콜을 준수하는 구조체와 열거형은 `static` 키워드를 사용해 메서드를 선언하고, 클래스는 `static` 또는 `class` 키워드를 사용한다. 구조체, 열거형, 클래스에 프로토콜 준수를 추가하는 익스텐션은 해당 타입이 사용하는 키워드와 동일한 키워드를 사용한다. 타입 메서드 요구사항에 대한 기본 구현을 제공하는 익스텐션은 `static` 키워드를 사용한다.

자세한 내용은 <doc:Declarations#Function-Declaration>을 참고한다.

<!--
  TODO: 매개변수와 반환 타입에서 ``Self`` 사용에 대해 설명하기
-->

> 프로토콜 메서드 선언 문법:
>
> *protocol-method-declaration* → *function-head* *function-name* *generic-parameter-clause*_?_ *function-signature* *generic-where-clause*_?_


### 프로토콜 이니셜라이저 선언

프로토콜은 프로토콜 선언 본문에 이니셜라이저 선언을 포함함으로써, 해당 프로토콜을 준수하는 타입이 반드시 이니셜라이저를 구현해야 한다고 명시한다. 프로토콜 이니셜라이저 선언은 일반 이니셜라이저 선언과 동일한 형태를 가지지만, 이니셜라이저의 본문은 포함하지 않는다.

프로토콜을 준수하는 타입은 **nonfailable** 프로토콜 이니셜라이저 요구사항을 충족하기 위해 nonfailable 이니셜라이저 또는 `init!` failable 이니셜라이저를 구현할 수 있다. **failable** 프로토콜 이니셜라이저 요구사항은 어떤 종류의 이니셜라이저로도 충족할 수 있다.

클래스가 프로토콜의 이니셜라이저 요구사항을 충족하기 위해 이니셜라이저를 구현할 때, 해당 클래스가 `final` 선언 수식어로 표시되지 않은 경우 이니셜라이저는 `required` 선언 수식어로 표시되어야 한다.

자세한 내용은 <doc:Declarations#Initializer-Declaration>을 참고한다.

> 프로토콜 이니셜라이저 선언 문법:
>
> *protocol-initializer-declaration* → *initializer-head* *generic-parameter-clause*_?_ *parameter-clause* *throws-clause*_?_ *generic-where-clause*_?_ \
> *protocol-initializer-declaration* → *initializer-head* *generic-parameter-clause*_?_ *parameter-clause* **`rethrows`** *generic-where-clause*_?_


### 프로토콜 서브스크립트 선언

프로토콜은 해당 프로토콜을 준수하는 타입이 반드시 서브스크립트를 구현해야 한다고 선언한다. 이를 위해 프로토콜 본문에 프로토콜 서브스크립트 선언을 포함한다. 프로토콜 서브스크립트 선언은 특별한 형태의 서브스크립트 선언을 가진다.

```swift
subscript (<#parameters#>) -> <#return type#> { get set }
```

서브스크립트 선언은 프로토콜을 준수하는 타입이 최소한의 getter와 setter 구현 요구사항을 충족해야 함을 나타낸다. 서브스크립트 선언에 `get`과 `set` 키워드가 모두 포함된 경우, 준수하는 타입은 반드시 getter와 setter를 모두 구현해야 한다. 서브스크립트 선언에 `get` 키워드만 포함된 경우, 준수하는 타입은 최소한 getter를 구현해야 하며, 선택적으로 setter를 구현할 수 있다.

프로토콜 선언에서 정적(static) 서브스크립트 요구사항을 선언하려면, 서브스크립트 선언에 `static` 선언 수식어를 붙인다. 프로토콜을 준수하는 구조체와 열거형은 `static` 키워드를 사용해 서브스크립트를 선언하고, 클래스는 `static` 또는 `class` 키워드를 사용해 서브스크립트를 선언한다. 구조체, 열거형, 클래스에 프로토콜 준수를 추가하는 익스텐션은 해당 타입이 사용하는 키워드와 동일한 키워드를 사용한다. 정적 서브스크립트 요구사항에 대한 기본 구현을 제공하는 익스텐션은 `static` 키워드를 사용한다.

자세한 내용은 <doc:Declarations#Subscript-Declaration>을 참고한다.

> 프로토콜 서브스크립트 선언 문법:
>
> *protocol-subscript-declaration* → *subscript-head* *subscript-result* *generic-where-clause*_?_ *getter-setter-keyword-block*


### 프로토콜 연관 타입 선언

프로토콜은 `associatedtype` 키워드를 사용해 연관 타입을 선언한다. 연관 타입은 프로토콜 선언의 일부로 사용되는 타입에 대한 별칭을 제공한다. 연관 타입은 제네릭 매개변수 절의 타입 매개변수와 유사하지만, 선언된 프로토콜 내에서 `Self`와 연관된다. 이때 `Self`는 프로토콜을 준수하는 최종 타입을 의미한다. 더 자세한 정보와 예제는 <doc:Generics#Associated-Types>를 참고한다.

프로토콜 선언에서 제네릭 `where` 절을 사용하면, 다른 프로토콜에서 상속받은 연관 타입에 제약을 추가할 수 있다. 이때 연관 타입을 다시 선언할 필요가 없다. 예를 들어, 아래 `SubProtocol`의 선언은 동일하다:

```swift
protocol SomeProtocol {
    associatedtype SomeType
}

protocol SubProtocolA: SomeProtocol {
    // 이 구문은 경고를 발생시킨다.
    associatedtype SomeType: Equatable
}

// 이 구문이 더 권장된다.
protocol SubProtocolB: SomeProtocol where SomeType: Equatable { }
```

<!--
  - test: `protocol-associatedtype`

  ```swifttest
  -> protocol SomeProtocol {
         associatedtype SomeType
     }

  -> protocol SubProtocolA: SomeProtocol {
         // 이 구문은 경고를 발생시킨다.
         associatedtype SomeType: Equatable
     }
  !$ warning: redeclaration of associated type 'SomeType' from protocol 'SomeProtocol' is better expressed as a 'where' clause on the protocol
  !! associatedtype SomeType: Equatable
  !! ~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~
  !!-
  !$ note: 'SomeType' declared here
  !! associatedtype SomeType
  !! ^

  // 이 구문이 더 권장된다.
  -> protocol SubProtocolB: SomeProtocol where SomeType: Equatable { }
  ```
-->

<!--
  TODO: Finish writing this section after WWDC.
-->

<!--
  NOTE:
  What are associated types? What are they "associated" with? Is "Self"
  an implicit associated type of every protocol? [...]

  Here's an initial stab:
  An Associated Type is associated with an implementation of that protocol.
  The protocol declares it, and is defined as part of the protocol's implementation.

  "The ``Self`` type allows you to refer to the eventual type of ``self``
  (where ``self`` is the type that conforms to the protocol).
  In addition to ``Self``, a protocol's operations often need to refer to types
  that are related to the type of ``Self``, such as a type of data stored in a
  collection or the node and edge types of a graph." Is this still true?

    -> If we expand the discussion here,
    -> add a link from Types_SelfType
    -> to give more details about Self in protocols.

  NOTES from Doug:
  At one point, Self was an associated type, but that's the wrong modeling of
  the problem.  Self is the stand-in type for the thing that conforms to the
  protocol.  It's weird to think of it as an associated type because it's the
  primary thing.  It's certainly not an associated type.  In many ways, you
  can think of associated types as being parameters that get filled in by the
  conformance of a specific concrete type to that protocol.

  There's a substitution mapping here.  The parameters are associated with
  Self because they're derived from Self.  When you have a concrete type that
  conforms to a protocol, it supplies concrete types for Self and all the
  associated types.

  The associated types are like parameters, but they're associated with Self in
  the protocol.  Self is the eventual type of the thing that conforms to the
  protocol -- you have to have a name for it so you can do things with it.

  We use "associated" in contrast with generic parameters in interfaces in C#.
  The interesting thing there is that they don't have a name like Self for the
  actual type, but you can name any of these independent types.    In theory,
  they're often independent but in practice they're often not -- you have an
  interface parameterized on T, where all the uses of the thing are that T are
  the same as Self.  Instead of having these independent parameters to an
  interface, we have a named thing (Self) and all these other things that hand
  off of it.

  Here's a stupid simple way to see the distinction:

  C#:

  interface Sequence <Element> {}

  class String : Sequence <UnicodeScalar>
  class String : Sequence <GraphemeCluster>

  These are both fine in C#

  Swift:

  protocol Sequence { typealias Element }

  class String : Sequence { typealias Element = ... }

  Here you have to pick one or the other -- you can't have both.
-->

<doc:Declarations#Type-Alias-Declaration>도 참고한다.

> 프로토콜 연관 타입 선언의 문법:
>
> *protocol-associated-type-declaration* → *attributes*_?_ *access-level-modifier*_?_ **`associatedtype`** *typealias-name* *type-inheritance-clause*_?_ *typealias-assignment*_?_ *generic-where-clause*_?_


## 초기화자 선언

*초기화자 선언*은 클래스, 구조체, 또는 열거형을 초기화하는 메서드를 프로그램에 도입한다. 초기화자 선언은 `init` 키워드를 사용하며, 두 가지 기본 형태가 있다.

구조체, 열거형, 그리고 클래스 타입은 여러 개의 초기화자를 가질 수 있지만, 클래스 초기화자의 규칙과 관련 동작은 다르다. 구조체와 열거형과 달리 클래스에는 지정 초기화자와 편의 초기화자 두 가지 종류가 있다. 이는 <doc:Initialization>에서 자세히 설명한다.

다음은 구조체, 열거형, 그리고 클래스의 지정 초기화자를 선언하는 형태다:

```swift
init(<#parameters#>) {
   <#statements#>
}
```

클래스의 지정 초기화자는 해당 클래스의 모든 프로퍼티를 직접 초기화한다. 동일한 클래스의 다른 초기화자를 호출할 수 없으며, 클래스가 슈퍼클래스를 가진다면 슈퍼클래스의 지정 초기화자 중 하나를 반드시 호출해야 한다. 클래스가 슈퍼클래스로부터 프로퍼티를 상속받았다면, 현재 클래스에서 해당 프로퍼티를 설정하거나 수정하기 전에 슈퍼클래스의 지정 초기화자 중 하나를 호출해야 한다.

지정 초기화자는 클래스 선언의 컨텍스트에서만 선언할 수 있으며, 따라서 확장 선언을 사용해 클래스에 추가할 수 없다.

구조체와 열거형의 초기화자는 다른 선언된 초기화자를 호출해 초기화 과정의 일부 또는 전체를 위임할 수 있다.

클래스의 편의 초기화자를 선언하려면, 초기화자 선언에 `convenience` 선언 수식어를 붙인다.

```swift
convenience init(<#parameters#>) {
   <#statements#>
}
```

편의 초기화자는 초기화 과정을 다른 편의 초기화자나 클래스의 지정 초기화자에게 위임할 수 있다. 하지만 초기화 과정은 반드시 클래스의 프로퍼티를 최종적으로 초기화하는 지정 초기화자 호출로 끝나야 한다. 편의 초기화자는 슈퍼클래스의 초기화자를 호출할 수 없다.

지정 초기화자와 편의 초기화자에 `required` 선언 수식어를 붙여 모든 서브클래스가 해당 초기화자를 구현하도록 요구할 수 있다. 서브클래스에서 이 초기화자를 구현할 때도 `required` 선언 수식어를 붙여야 한다.

기본적으로 슈퍼클래스에 선언된 초기화자는 서브클래스에 상속되지 않는다. 하지만 서브클래스가 모든 저장 프로퍼티를 기본값으로 초기화하고 자체 초기화자를 정의하지 않았다면, 슈퍼클래스의 모든 초기화자를 상속받는다. 서브클래스가 슈퍼클래스의 모든 지정 초기화자를 재정의하면, 슈퍼클래스의 편의 초기화자를 상속받는다.

메서드, 프로퍼티, 그리고 서브스크립트와 마찬가지로, 재정의된 지정 초기화자에는 `override` 선언 수식어를 붙여야 한다.

> 참고: 초기화자에 `required` 선언 수식어를 붙였다면, 서브클래스에서 해당 초기화자를 재정의할 때 `override` 수식어를 함께 붙이지 않는다.

함수와 메서드처럼 초기화자도 에러를 던지거나 다시 던질 수 있다. 또한 함수와 메서드처럼 초기화자의 파라미터 뒤에 `throws` 또는 `rethrows` 키워드를 사용해 적절한 동작을 나타낸다. 마찬가지로 초기화자는 비동기적일 수 있으며, `async` 키워드를 사용해 이를 나타낸다.

다양한 타입 선언에서 초기화자의 예를 보려면 <doc:Initialization>을 참고한다.


### 실패 가능한 초기화 메서드

*실패 가능한 초기화 메서드*는 초기화 과정에서 옵셔널 인스턴스나 암시적 언래핑 옵셔널 인스턴스를 반환할 수 있는 초기화 메서드다. 따라서 초기화가 실패할 경우 `nil`을 반환할 수 있다.

옵셔널 인스턴스를 반환하는 실패 가능한 초기화 메서드를 선언하려면, 초기화 메서드 선언에서 `init` 키워드 뒤에 물음표를 붙인다(`init?`). 암시적 언래핑 옵셔널 인스턴스를 반환하는 실패 가능한 초기화 메서드를 선언하려면, 느낌표를 붙인다(`init!`). 아래 예제는 옵셔널 인스턴스를 반환하는 `init?` 실패 가능한 초기화 메서드를 보여준다.

```swift
struct SomeStruct {
    let property: String
    // 'SomeStruct'의 옵셔널 인스턴스를 반환
    init?(input: String) {
        if input.isEmpty {
            // 'self'를 버리고 'nil' 반환
            return nil
        }
        property = input
    }
}
```

<!--
  - test: `failable`

  ```swifttest
  -> struct SomeStruct {
         let property: String
         // produces an optional instance of 'SomeStruct'
         init?(input: String) {
             if input.isEmpty {
                 // discard 'self' and return 'nil'
                 return nil
             }
             property = input
         }
     }
  ```
-->

`init?` 실패 가능한 초기화 메서드를 호출할 때는 일반 초기화 메서드와 동일한 방식으로 호출하되, 결과의 옵셔널성을 처리해야 한다.

```swift
if let actualInstance = SomeStruct(input: "Hello") {
    // 'SomeStruct' 인스턴스를 사용
} else {
    // 'SomeStruct' 초기화 실패, 초기화 메서드가 'nil' 반환
}
```

<!--
  - test: `failable`

  ```swifttest
  -> if let actualInstance = SomeStruct(input: "Hello") {
         // do something with the instance of 'SomeStruct'
  >>     _ = actualInstance
     } else {
         // initialization of 'SomeStruct' failed and the initializer returned 'nil'
     }
  ```
-->

실패 가능한 초기화 메서드는 초기화 메서드 본문의 어느 지점에서든 `nil`을 반환할 수 있다.

실패 가능한 초기화 메서드는 어떤 종류의 초기화 메서드에도 위임할 수 있다. 실패하지 않는 초기화 메서드는 다른 실패하지 않는 초기화 메서드나 `init!` 실패 가능한 초기화 메서드에 위임할 수 있다. 실패하지 않는 초기화 메서드는 `init?` 실패 가능한 초기화 메서드에 위임할 수 있는데, 이때 슈퍼클래스의 초기화 메서드 결과를 강제 언래핑해야 한다. 예를 들어, `super.init()!`과 같이 작성한다.

초기화 실패는 초기화 위임을 통해 전파된다. 구체적으로, 실패 가능한 초기화 메서드가 초기화에 실패해 `nil`을 반환하는 초기화 메서드에 위임하면, 위임한 초기화 메서드도 실패하고 암시적으로 `nil`을 반환한다. 실패하지 않는 초기화 메서드가 `init!` 실패 가능한 초기화 메서드에 위임했는데, 해당 초기화 메서드가 실패해 `nil`을 반환하면 런타임 오류가 발생한다. 이는 `nil` 값을 가진 옵셔널을 강제 언래핑할 때와 동일한 상황이다.

실패 가능한 지정 초기화 메서드는 서브클래스에서 어떤 종류의 지정 초기화 메서드로도 재정의할 수 있다. 실패하지 않는 지정 초기화 메서드는 서브클래스에서 실패하지 않는 지정 초기화 메서드로만 재정의할 수 있다.

실패 가능한 초기화 메서드에 대한 더 자세한 정보와 예제는 <doc:Initialization#Failable-Initializers>를 참고한다.

> 초기화 메서드 선언 문법:
>
> *initializer-declaration* → *initializer-head* *generic-parameter-clause*_?_ *parameter-clause* **`async`**_?_ *throws-clause*_?_ *generic-where-clause*_?_ *initializer-body* \
> *initializer-declaration* → *initializer-head* *generic-parameter-clause*_?_ *parameter-clause* **`async`**_?_ **`rethrows`** *generic-where-clause*_?_ *initializer-body* \
> *initializer-head* → *attributes*_?_ *declaration-modifiers*_?_ **`init`** \
> *initializer-head* → *attributes*_?_ *declaration-modifiers*_?_ **`init`** **`?`** \
> *initializer-head* → *attributes*_?_ *declaration-modifiers*_?_ **`init`** **`!`** \
> *initializer-body* → *code-block*


## 디이니셜라이저 선언

*디이니셜라이저 선언*은 클래스 타입을 위한 디이니셜라이저를 정의한다. 디이니셜라이저는 매개변수를 받지 않으며, 다음과 같은 형태를 가진다:

```swift
deinit {
   <#statements#>
}
```

디이니셜라이저는 클래스 객체에 더 이상 참조가 없을 때, 객체가 메모리에서 해제되기 직전에 자동으로 호출된다. 디이니셜라이저는 클래스 선언 본문 안에서만 선언할 수 있으며, 클래스 확장에서는 선언할 수 없다. 또한, 각 클래스는 최대 하나의 디이니셜라이저를 가질 수 있다.

서브클래스는 슈퍼클래스의 디이니셜라이저를 상속받는다. 이 디이니셜라이저는 서브클래스 객체가 해제되기 직전에 암묵적으로 호출된다. 서브클래스 객체는 상속 체인에 있는 모든 디이니셜라이저가 실행을 마칠 때까지 해제되지 않는다.

디이니셜라이저는 직접 호출할 수 없다.

클래스 선언에서 디이니셜라이저를 사용하는 예제는 <doc:Deinitialization>을 참고한다.

> 디이니셜라이저 선언 문법:
>
> *deinitializer-declaration* → *attributes*_?_ **`deinit`** *code-block*


## 확장 선언

*확장 선언*을 사용하면 기존 타입의 동작을 확장할 수 있다. 확장 선언은 `extension` 키워드를 사용하며, 다음과 같은 형태를 가진다:

```swift
extension <#type name#> where <#requirements#> {
   <#declarations#>
}
```

확장 선언의 본문에는 0개 이상의 *선언*이 포함될 수 있다. 이러한 *선언*은 계산 프로퍼티, 계산 타입 프로퍼티, 인스턴스 메서드, 타입 메서드, 이니셜라이저, 서브스크립트 선언, 그리고 클래스, 구조체, 열거형 선언까지 포함할 수 있다. 확장 선언은 디이니셜라이저나 프로토콜 선언, 저장 프로퍼티, 프로퍼티 옵저버, 또는 다른 확장 선언을 포함할 수 없다. 프로토콜 확장 내의 선언은 `final`로 표시될 수 없다. 다양한 종류의 선언을 포함하는 확장에 대한 논의와 여러 예제는 <doc:Extensions>를 참고한다.

*타입 이름*이 클래스, 구조체, 또는 열거형 타입인 경우, 확장은 해당 타입을 확장한다. *타입 이름*이 프로토콜 타입인 경우, 확장은 해당 프로토콜을 준수하는 모든 타입을 확장한다.

제네릭 타입이나 연관 타입을 가진 프로토콜을 확장하는 확장 선언은 *요구사항*을 포함할 수 있다. 확장된 타입의 인스턴스나 확장된 프로토콜을 준수하는 타입의 인스턴스가 *요구사항*을 만족하면, 해당 인스턴스는 선언에 지정된 동작을 얻게 된다.

확장 선언은 이니셜라이저 선언을 포함할 수 있다. 그러나 확장하려는 타입이 다른 모듈에 정의된 경우, 이니셜라이저 선언은 해당 모듈에 이미 정의된 이니셜라이저에 위임해야 하며, 이를 통해 해당 타입의 멤버가 올바르게 초기화되도록 보장한다.

기존 타입의 프로퍼티, 메서드, 이니셜라이저는 해당 타입의 확장에서 재정의할 수 없다.

확장 선언은 기존 클래스, 구조체, 또는 열거형 타입에 프로토콜 준수를 추가할 수 있다. 이를 위해 *채택된 프로토콜*을 지정한다:

```swift
extension <#type name#>: <#adopted protocols#> where <#requirements#> {
   <#declarations#>
}
```

확장 선언은 기존 클래스에 클래스 상속을 추가할 수 없으므로, *타입 이름*과 콜론 뒤에는 프로토콜 목록만 지정할 수 있다.


### 조건부 프로토콜 준수

제네릭 타입을 확장해 특정 조건을 만족할 때만 프로토콜을 준수하도록 할 수 있다. 이를 조건부 프로토콜 준수라고 한다. 타입의 인스턴스가 특정 요구사항을 충족할 때만 프로토콜을 준수하게 된다. 조건부 프로토콜 준수를 추가하려면 익스텐션 선언에 *요구사항*을 포함하면 된다.


#### 특정 제네릭 컨텍스트에서는 재정의된 요구사항이 사용되지 않는다

일부 제네릭 컨텍스트에서는, 프로토콜에 대한 조건적 준수(conditional conformance)를 통해 동작을 얻는 타입이 해당 프로토콜의 요구사항에 대한 특수화된 구현을 항상 사용하지 않는다. 이 동작을 설명하기 위해, 다음 예제에서는 두 개의 프로토콜과 두 프로토콜에 조건적으로 준수하는 제네릭 타입을 정의한다.

```swift
protocol Loggable {
    func log()
}
extension Loggable {
    func log() {
        print(self)
    }
}

protocol TitledLoggable: Loggable {
    static var logTitle: String { get }
}
extension TitledLoggable {
    func log() {
        print("\(Self.logTitle): \(self)")
    }
}

struct Pair<T>: CustomStringConvertible {
    let first: T
    let second: T
    var description: String {
        return "(\(first), \(second))"
    }
}

extension Pair: Loggable where T: Loggable { }
extension Pair: TitledLoggable where T: TitledLoggable {
    static var logTitle: String {
        return "Pair of '\(T.logTitle)'"
    }
}

extension String: TitledLoggable {
    static var logTitle: String {
        return "String"
    }
}
```

`Pair` 구조체는 제네릭 타입이 `Loggable` 또는 `TitledLoggable`을 준수할 때 각각 `Loggable`과 `TitledLoggable`을 준수한다. 아래 예제에서 `oneAndTwo`는 `Pair<String>`의 인스턴스이며, `String`이 `TitledLoggable`을 준수하기 때문에 `TitledLoggable`을 준수한다. `oneAndTwo`에서 `log()` 메서드를 직접 호출하면, 제목 문자열을 포함한 특수화된 버전이 사용된다.

```swift
let oneAndTwo = Pair(first: "one", second: "two")
oneAndTwo.log()
// Prints "Pair of 'String': (one, two)"
```

그러나 `oneAndTwo`가 제네릭 컨텍스트에서 사용되거나 `Loggable` 프로토콜의 인스턴스로 사용될 때는 특수화된 버전이 사용되지 않는다. Swift는 `Pair`가 `Loggable`을 준수하는 데 필요한 최소 요구사항만을 참조하여 `log()`의 구현을 선택한다. 이 때문에 `Loggable` 프로토콜에서 제공하는 기본 구현이 대신 사용된다.

```swift
func doSomething<T: Loggable>(with x: T) {
    x.log()
}
doSomething(with: oneAndTwo)
// Prints "(one, two)"
```

`doSomething(_:)`에 전달된 인스턴스에서 `log()`가 호출되면, 로그된 문자열에서 커스텀 제목이 생략된다.


### 프로토콜 준수는 중복될 수 없다

구체적인 타입은 특정 프로토콜에 한 번만 준수할 수 있다. Swift는 중복된 프로토콜 준수를 에러로 표시한다. 이러한 에러는 주로 두 가지 상황에서 발생한다. 첫 번째는 동일한 프로토콜을 여러 번 명시적으로 준수하려고 할 때이며, 두 번째는 동일한 프로토콜을 여러 번 암묵적으로 상속받을 때다. 이 두 상황에 대해 아래에서 자세히 설명한다.


#### 명시적 중복 해결

동일한 타입에 대해 여러 확장을 추가할 때, 동일한 프로토콜을 준수하도록 할 수 없다. 이는 확장의 요구사항이 서로 배타적일지라도 마찬가지다. 아래 예제는 이러한 제약을 보여준다. 두 개의 확장 선언이 `Serializable` 프로토콜에 대한 조건부 준수를 추가하려고 한다. 하나는 `Int` 타입의 배열을 위한 것이고, 다른 하나는 `String` 타입의 배열을 위한 것이다.

```swift
protocol Serializable {
    func serialize() -> Any
}

extension Array: Serializable where Element == Int {
    func serialize() -> Any {
        // 구현
    }
}
extension Array: Serializable where Element == String {
    func serialize() -> Any {
        // 구현
    }
}
// 에러: 'Array<Element>'의 'Serializable' 프로토콜에 대한 중복 준수
```

<!--
  - test: `multiple-conformances`

  ```swifttest
  -> protocol Serializable {
        func serialize() -> Any
     }

     extension Array: Serializable where Element == Int {
         func serialize() -> Any {
             // 구현
  >>         return 0
  ->     }
     }
     extension Array: Serializable where Element == String {
         func serialize() -> Any {
             // 구현
  >>         return 0
  ->     }
     }
  // 에러: 'Array<Element>'의 'Serializable' 프로토콜에 대한 중복 준수
  !$ error: 'Array<Element>'의 'Serializable' 프로토콜에 대한 충돌하는 준수; 조건부 경계가 다르더라도 하나 이상의 준수를 추가할 수 없음
  !! extension Array: Serializable where Element == String {
  !! ^
  !$ note: 'Array<Element>'이 'Serializable' 프로토콜을 준수함을 선언한 위치
  !! extension Array: Serializable where Element == Int {
  !! ^
  ```
-->

여러 구체적인 타입에 대한 조건부 준수를 추가해야 한다면, 각 타입이 준수할 수 있는 새로운 프로토콜을 생성하고, 조건부 준수를 선언할 때 해당 프로토콜을 요구사항으로 사용하면 된다.

```swift
protocol SerializableInArray { }
extension Int: SerializableInArray { }
extension String: SerializableInArray { }

extension Array: Serializable where Element: SerializableInArray {
    func serialize() -> Any {
        // 구현
    }
}
```

<!--
  - test: `multiple-conformances-success`

  ```swifttest
  >> protocol Serializable { }
  -> protocol SerializableInArray { }
     extension Int: SerializableInArray { }
     extension String: SerializableInArray { }

  -> extension Array: Serializable where Element: SerializableInArray {
         func serialize() -> Any {
             // 구현
  >>         return 0
  ->     }
     }
  ```
-->


#### 암시적 중복 해결하기

구체 타입이 조건부로 프로토콜을 준수할 때, 해당 타입은 동일한 요구 사항을 가진 모든 부모 프로토콜에도 암시적으로 준수한다.

하나의 부모 프로토콜을 상속받는 두 프로토콜에 대해 조건부로 준수해야 한다면, 부모 프로토콜에 대한 준수를 명시적으로 선언한다. 이렇게 하면 서로 다른 요구 사항으로 부모 프로토콜에 두 번 암시적으로 준수하는 상황을 피할 수 있다.

다음 예제는 `Array`가 `TitledLoggable`과 새로운 `MarkedLoggable` 프로토콜에 조건부로 준수할 때 발생할 수 있는 충돌을 피하기 위해, `Loggable`에 대한 조건부 준수를 명시적으로 선언한다.

```swift
protocol MarkedLoggable: Loggable {
    func markAndLog()
}

extension MarkedLoggable {
    func markAndLog() {
        print("----------")
        log()
    }
}

extension Array: Loggable where Element: Loggable { }
extension Array: TitledLoggable where Element: TitledLoggable {
    static var logTitle: String {
        return "Array of '\(Element.logTitle)'"
    }
}
extension Array: MarkedLoggable where Element: MarkedLoggable { }
```

<!--
  - test: `conditional-conformance`

  ```swifttest
  -> protocol MarkedLoggable: Loggable {
        func markAndLog()
     }

     extension MarkedLoggable {
        func markAndLog() {
           print("----------")
           log()
        }
     }

     extension Array: Loggable where Element: Loggable { }
     extension Array: TitledLoggable where Element: TitledLoggable {
        static var logTitle: String {
           return "Array of '\(Element.logTitle)'"
        }
     }
     extension Array: MarkedLoggable where Element: MarkedLoggable { }
  ```
-->

`Loggable`에 대한 조건부 준수를 명시적으로 선언하지 않으면, 다른 `Array` 확장이 암시적으로 이 선언을 생성하게 되어 에러가 발생한다:

```swift
extension Array: Loggable where Element: TitledLoggable { }
extension Array: Loggable where Element: MarkedLoggable { }
// Error: redundant conformance of 'Array<Element>' to protocol 'Loggable'
```

<!--
  - test: `conditional-conformance-implicit-overlap`

  ```swifttest
  >> protocol Loggable { }
  >> protocol MarkedLoggable : Loggable { }
  >> protocol TitledLoggable : Loggable { }
  -> extension Array: Loggable where Element: TitledLoggable { }
     extension Array: Loggable where Element: MarkedLoggable { }
  // Error: redundant conformance of 'Array<Element>' to protocol 'Loggable'
  !$ error: conflicting conformance of 'Array<Element>' to protocol 'Loggable'; there cannot be more than one conformance, even with different conditional bounds
  !! extension Array: Loggable where Element: MarkedLoggable { }
  !! ^
  !$ note: 'Array<Element>' declares conformance to protocol 'Loggable' here
  !! extension Array: Loggable where Element: TitledLoggable { }
  !! ^
  ```
-->

<!--
  - test: `types-cant-have-multiple-implicit-conformances`

  ```swifttest
  >> protocol Loggable { }
     protocol TitledLoggable: Loggable { }
     protocol MarkedLoggable: Loggable { }
     extension Array: TitledLoggable where Element: TitledLoggable {
         // ...
     }
     extension Array: MarkedLoggable where Element: MarkedLoggable { }
  !$ error: conditional conformance of type 'Array<Element>' to protocol 'TitledLoggable' does not imply conformance to inherited protocol 'Loggable'
  !! extension Array: TitledLoggable where Element: TitledLoggable {
  !! ^
  !$ note: did you mean to explicitly state the conformance like 'extension Array: Loggable where ...'?
  !! extension Array: TitledLoggable where Element: TitledLoggable {
  !! ^
  !$ error: type 'Array<Element>' does not conform to protocol 'MarkedLoggable'
  !! extension Array: MarkedLoggable where Element: MarkedLoggable { }
  !! ^
  !$ error: type 'Element' does not conform to protocol 'TitledLoggable'
  !! extension Array: MarkedLoggable where Element: MarkedLoggable { }
  !! ^
  !$ error: 'MarkedLoggable' requires that 'Element' conform to 'TitledLoggable'
  !! extension Array: MarkedLoggable where Element: MarkedLoggable { }
  !! ^
  !$ note: requirement specified as 'Element' : 'TitledLoggable'
  !! extension Array: MarkedLoggable where Element: MarkedLoggable { }
  !! ^
  !$ note: requirement from conditional conformance of 'Array<Element>' to 'Loggable'
  !! extension Array: MarkedLoggable where Element: MarkedLoggable { }
  !! ^
  ```
-->

<!--
  - test: `extension-can-have-where-clause`

  ```swifttest
  >> extension Array where Element: Equatable {
         func f(x: Array) -> Int { return 7 }
     }
  >> let x = [1, 2, 3]
  >> let y = [10, 20, 30]
  >> let r0 = x.f(x: y)
  >> assert(r0 == 7)
  ```
-->

<!--
  - test: `extensions-can-have-where-clause-and-inheritance-together`

  ```swifttest
  >> protocol P { func foo() -> Int }
  >> extension Array: P where Element: Equatable {
  >>    func foo() -> Int { return 0 }
  >> }
  >> let r0 = [1, 2, 3].foo()
  >> assert(r0 == 0)
  ```
-->

> 확장 선언 문법:
>
> *extension-declaration* → *attributes*_?_ *access-level-modifier*_?_ **`extension`** *type-identifier* *type-inheritance-clause*_?_ *generic-where-clause*_?_ *extension-body* \
> *extension-body* → **`{`** *extension-members*_?_ **`}`**
>
> *extension-members* → *extension-member* *extension-members*_?_ \
> *extension-member* → *declaration* | *compiler-control-statement*


## 서브스크립트 선언

*서브스크립트* 선언은 특정 타입의 객체에 서브스크립트 기능을 추가할 수 있게 해준다. 주로 컬렉션, 리스트, 시퀀스 등의 요소에 접근하기 위한 편리한 문법을 제공하는 데 사용된다. 서브스크립트 선언은 `subscript` 키워드를 사용하며, 다음과 같은 형태를 가진다:

```swift
subscript (<#parameters#>) -> <#return type#> {
   get {
      <#statements#>
   }
   set(<#setter name#>) {
      <#statements#>
   }
}
```

서브스크립트 선언은 클래스, 구조체, 열거형, 확장, 프로토콜 선언 내에서만 사용할 수 있다.

*파라미터*는 서브스크립트 표현식에서 해당 타입의 요소에 접근하기 위해 사용되는 하나 이상의 인덱스를 지정한다(예: `object[i]` 표현식에서 `i`). 요소에 접근하는 데 사용되는 인덱스는 어떤 타입이든 가능하지만, 각 파라미터는 인덱스의 타입을 명시하기 위해 타입 어노테이션을 포함해야 한다. *반환 타입*은 접근되는 요소의 타입을 지정한다.

계산 프로퍼티와 마찬가지로, 서브스크립트 선언은 요소의 값을 읽고 쓰는 기능을 지원한다. getter는 값을 읽는 데 사용되며, setter는 값을 쓰는 데 사용된다. setter 절은 선택 사항이며, getter만 필요하다면 두 절을 모두 생략하고 요청된 값을 직접 반환할 수 있다. 하지만 setter 절을 제공한다면 반드시 getter 절도 함께 제공해야 한다.

*setter 이름*과 괄호는 선택 사항이다. setter 이름을 제공하면 setter의 파라미터 이름으로 사용된다. setter 이름을 제공하지 않으면 기본 파라미터 이름은 `value`가 된다. setter의 파라미터 타입은 *반환 타입*과 동일하다.

서브스크립트 선언은 *파라미터*나 *반환 타입*이 다르다면 동일한 타입 내에서 오버로드할 수 있다. 또한 슈퍼클래스에서 상속받은 서브스크립트 선언을 오버라이드할 수도 있다. 이 경우, 오버라이드된 서브스크립트 선언에 `override` 선언 수정자를 표시해야 한다.

서브스크립트 파라미터는 함수 파라미터와 동일한 규칙을 따르지만, 두 가지 예외가 있다. 기본적으로 서브스크립트에 사용되는 파라미터는 함수, 메서드, 이니셜라이저와 달리 인자 레이블을 가지지 않는다. 하지만 함수, 메서드, 이니셜라이저와 동일한 문법을 사용해 명시적으로 인자 레이블을 제공할 수 있다. 또한 서브스크립트는 in-out 파라미터를 가질 수 없다. 서브스크립트 파라미터는 기본값을 가질 수 있으며, 이는 <doc:Declarations#Special-Kinds-of-Parameters>에서 설명한 문법을 사용한다.

서브스크립트는 프로토콜 선언 내에서도 선언할 수 있으며, 이는 <doc:Declarations#Protocol-Subscript-Declaration>에서 자세히 설명한다.

서브스크립트에 대한 더 자세한 정보와 서브스크립트 선언 예제는 <doc:Subscripts>를 참고한다.


### 타입 서브스크립트 선언

타입 인스턴스가 아닌 타입 자체에 의해 노출되는 서브스크립트를 선언하려면, 서브스크립트 선언에 `static` 선언 수정자를 붙인다. 클래스에서는 타입 계산 프로퍼티에 `class` 선언 수정자를 사용해 서브클래스가 슈퍼클래스의 구현을 재정의할 수 있도록 허용할 수 있다. 클래스 선언에서 `static` 키워드는 `class`와 `final` 선언 수정자를 모두 붙인 것과 동일한 효과를 가진다.

<!--
  - test: `cant-override-static-subscript-in-subclass`

  ```swifttest
  -> class Super { static subscript(i: Int) -> Int { return 10 } }
  -> class Sub: Super { override static subscript(i: Int) -> Int { return 100 } }
  !$ error: cannot override static subscript
  !! class Sub: Super { override static subscript(i: Int) -> Int { return 100 } }
  !!                                    ^
  !$ note: overridden declaration is here
  !! class Super { static subscript(i: Int) -> Int { return 10 } }
  !!                      ^
  ```
-->

> 서브스크립트 선언 문법:
>
> *subscript-declaration* → *subscript-head* *subscript-result* *generic-where-clause*_?_ *code-block* \
> *subscript-declaration* → *subscript-head* *subscript-result* *generic-where-clause*_?_ *getter-setter-block* \
> *subscript-declaration* → *subscript-head* *subscript-result* *generic-where-clause*_?_ *getter-setter-keyword-block* \
> *subscript-head* → *attributes*_?_ *declaration-modifiers*_?_ **`subscript`** *generic-parameter-clause*_?_ *parameter-clause* \
> *subscript-result* → **`->`** *attributes*_?_ *type*


## 매크로 선언

*매크로 선언*은 새로운 매크로를 도입한다. `macro` 키워드로 시작하며, 다음과 같은 형태를 가진다:

```swift
macro <#name#> = <#macro implementation#>
```

*매크로 구현*은 또 다른 매크로를 의미하며, 이 매크로의 확장을 수행하는 코드의 위치를 나타낸다. 매크로 확장을 수행하는 코드는 별도의 Swift 프로그램으로, [SwiftSyntax][] 모듈을 사용해 Swift 코드와 상호작용한다. Swift 표준 라이브러리에서 제공하는 `externalMacro(module:type:)` 매크로를 호출하고, 매크로 구현을 포함하는 타입의 이름과 해당 타입이 포함된 모듈의 이름을 전달한다.

[SwiftSyntax]: https://github.com/swiftlang/swift-syntax

매크로는 함수와 동일한 모델을 따라 오버로드할 수 있다. 매크로 선언은 파일 범위에서만 나타난다.

Swift에서 매크로에 대한 개요는 <doc:Macros>를 참고한다.

> 매크로 선언 구문:
>
> *macro-declaration* → *macro-head* *identifier* *generic-parameter-clause*_?_ *macro-signature* *macro-definition*_?_ *generic-where-clause* \
> *macro-head* → *attributes*_?_ *declaration-modifiers*_?_ **`macro`** \
> *macro-signature* → *parameter-clause* *macro-function-signature-result*_?_ \
> *macro-function-signature-result* → **`->`** *type* \
> *macro-definition* → **`=`** *expression*


## 연산자 선언

*연산자 선언*은 프로그램에 새로운 중위, 전위, 후위 연산자를 도입한다. `operator` 키워드를 사용해 선언한다.

연산자는 세 가지 형태로 선언할 수 있다: 중위, 전위, 후위. 연산자의 *위치성*은 연산자가 피연산자에 대해 상대적으로 어디에 위치하는지를 결정한다.

연산자 선언에는 세 가지 기본 형태가 있으며, 각각 위치성에 따라 다르다. 연산자의 위치성은 `operator` 키워드 앞에 `infix`, `prefix`, `postfix` 선언 수식자를 붙여 지정한다. 각 형태에서 연산자의 이름은 <doc:LexicalStructure#Operators>에서 정의된 연산자 문자만 포함할 수 있다.

다음은 새로운 중위 연산자를 선언하는 형태이다:

```swift
infix operator <#operator name#>: <#precedence group#>
```

*중위 연산자*는 두 피연산자 사이에 위치하는 이항 연산자이다. 예를 들어, 표현식 `1 + 2`에서 익숙한 덧셈 연산자(`+`)가 있다.

중위 연산자는 선택적으로 우선순위 그룹을 지정할 수 있다. 연산자에 우선순위 그룹을 생략하면, Swift는 기본 우선순위 그룹인 `DefaultPrecedence`를 사용한다. 이 그룹은 `TernaryPrecedence`보다 약간 높은 우선순위를 지정한다. 자세한 내용은 <doc:Declarations#Precedence-Group-Declaration>을 참고한다.

다음은 새로운 전위 연산자를 선언하는 형태이다:

```swift
prefix operator <#operator name#>
```

*전위 연산자*는 피연산자 바로 앞에 위치하는 단항 연산자이다. 예를 들어, 표현식 `!a`에서 전위 논리 NOT 연산자(`!`)가 있다.

전위 연산자 선언은 우선순위 수준을 지정하지 않는다. 전위 연산자는 결합성이 없다.

다음은 새로운 후위 연산자를 선언하는 형태이다:

```swift
postfix operator <#operator name#>
```

*후위 연산자*는 피연산자 바로 뒤에 위치하는 단항 연산자이다. 예를 들어, 표현식 `a!`에서 후위 강제 언래핑 연산자(`!`)가 있다.

전위 연산자와 마찬가지로, 후위 연산자 선언도 우선순위 수준을 지정하지 않는다. 후위 연산자는 결합성이 없다.

새로운 연산자를 선언한 후, 해당 연산자와 동일한 이름을 가진 정적 메서드를 선언해 구현한다. 정적 메서드는 연산자가 인자로 받는 값의 타입 중 하나의 멤버이다. 예를 들어, `Double`과 `Int`를 곱하는 연산자는 `Double` 또는 `Int` 구조체에 정적 메서드로 구현된다. 전위 또는 후위 연산자를 구현할 때는 해당 메서드 선언에 `prefix` 또는 `postfix` 선언 수식자를 붙여야 한다. 새로운 연산자를 만들고 구현하는 예제는 <doc:AdvancedOperators#Custom-Operators>를 참고한다.

> 연산자 선언 문법:
>
> *operator-declaration* → *prefix-operator-declaration* | *postfix-operator-declaration* | *infix-operator-declaration*
>
> *prefix-operator-declaration* → **`prefix`** **`operator`** *operator* \
> *postfix-operator-declaration* → **`postfix`** **`operator`** *operator* \
> *infix-operator-declaration* → **`infix`** **`operator`** *operator* *infix-operator-group*_?_
>
> *infix-operator-group* → **`:`** *precedence-group-name*


## 우선순위 그룹 선언

*우선순위 그룹 선언*은 프로그램에 새로운 중위 연산자 우선순위 그룹을 추가한다. 연산자의 우선순위는 그룹화 괄호가 없을 때 연산자가 피연산자와 얼마나 강하게 결합하는지를 결정한다.

우선순위 그룹 선언은 다음과 같은 형태를 가진다:

```swift
precedencegroup <#우선순위 그룹 이름#> {
    higherThan: <#낮은 그룹 이름#>
    lowerThan: <#높은 그룹 이름#>
    associativity: <#결합성#>
    assignment: <#할당#>
}
```

*낮은 그룹 이름*과 *높은 그룹 이름* 목록은 새로운 우선순위 그룹이 기존 우선순위 그룹과 어떻게 관련되는지를 지정한다. `lowerThan` 우선순위 그룹 속성은 현재 모듈 외부에서 선언된 우선순위 그룹만 참조할 수 있다. 두 연산자가 피연산자를 놓고 경쟁할 때, 예를 들어 `2 + 3 * 5`와 같은 표현식에서, 상대적으로 더 높은 우선순위를 가진 연산자가 피연산자와 더 강하게 결합한다.

> 참고: *낮은 그룹 이름*과 *높은 그룹 이름*을 사용해 서로 관련된 우선순위 그룹은 단일 관계 계층에 맞아야 하지만, 반드시 선형 계층을 형성할 필요는 없다. 이는 상대적 우선순위가 정의되지 않은 우선순위 그룹이 존재할 수 있음을 의미한다. 이러한 우선순위 그룹의 연산자는 그룹화 괄호 없이 서로 나란히 사용할 수 없다.

Swift는 Swift 표준 라이브러리에서 제공하는 연산자와 함께 사용할 수 있는 다양한 우선순위 그룹을 정의한다. 예를 들어, 덧셈(`+`)과 뺄셈(`-`) 연산자는 `AdditionPrecedence` 그룹에 속하고, 곱셈(`*`)과 나눗셈(`/`) 연산자는 `MultiplicationPrecedence` 그룹에 속한다. Swift 표준 라이브러리에서 제공하는 우선순위 그룹의 전체 목록은 [Operator Declarations](https://developer.apple.com/documentation/swift/operator_declarations)를 참고한다.

연산자의 *결합성*은 동일한 우선순위 수준을 가진 연산자 시퀀스가 그룹화 괄호 없이 어떻게 함께 그룹화되는지를 지정한다. 연산자의 결합성을 지정하려면 `left`, `right`, `none` 중 하나의 컨텍스트 키워드를 작성한다. 결합성을 생략하면 기본값은 `none`이다. 왼쪽 결합성 연산자는 왼쪽에서 오른쪽으로 그룹화된다. 예를 들어, 뺄셈 연산자(`-`)는 왼쪽 결합성을 가지므로, `4 - 5 - 6` 표현식은 `(4 - 5) - 6`으로 그룹화되고 `-7`로 평가된다. 오른쪽 결합성 연산자는 오른쪽에서 왼쪽으로 그룹화되고, `none`으로 지정된 연산자는 전혀 결합하지 않는다. 동일한 우선순위 수준을 가진 비결합성 연산자는 서로 인접할 수 없다. 예를 들어, `<` 연산자는 `none` 결합성을 가지므로 `1 < 2 < 3`은 유효한 표현식이 아니다.

우선순위 그룹의 *할당*은 옵셔널 체이닝을 포함하는 연산에서 연산자의 우선순위를 지정한다. `true`로 설정하면, 해당 우선순위 그룹의 연산자는 Swift 표준 라이브러리의 할당 연산자와 동일한 그룹화 규칙을 사용한다. `false`로 설정하거나 생략하면, 우선순위 그룹의 연산자는 할당을 수행하지 않는 연산자와 동일한 옵셔널 체이닝 규칙을 따른다.

> 우선순위 그룹 선언 문법:
>
> *precedence-group-declaration* → **`precedencegroup`** *precedence-group-name* **`{`** *precedence-group-attributes*_?_ **`}`**
>
> *precedence-group-attributes* → *precedence-group-attribute* *precedence-group-attributes*_?_ \
> *precedence-group-attribute* → *precedence-group-relation* \
> *precedence-group-attribute* → *precedence-group-assignment* \
> *precedence-group-attribute* → *precedence-group-associativity*
>
> *precedence-group-relation* → **`higherThan`** **`:`** *precedence-group-names* \
> *precedence-group-relation* → **`lowerThan`** **`:`** *precedence-group-names*
>
> *precedence-group-assignment* → **`assignment`** **`:`** *boolean-literal*
>
> *precedence-group-associativity* → **`associativity`** **`:`** **`left`** \
> *precedence-group-associativity* → **`associativity`** **`:`** **`right`** \
> *precedence-group-associativity* → **`associativity`** **`:`** **`none`**
>
> *precedence-group-names* → *precedence-group-name* | *precedence-group-name* **`,`** *precedence-group-names* \
> *precedence-group-name* → *identifier*


## 선언 수정자

*선언 수정자*는 선언의 동작이나 의미를 변경하는 키워드 또는 문맥에 따라 달라지는 키워드다. 선언 수정자를 사용하려면 선언의 속성(있는 경우)과 선언을 시작하는 키워드 사이에 적절한 키워드나 문맥에 따라 달라지는 키워드를 작성한다.

- `class` 용어:
  클래스의 멤버에 이 수정자를 적용하면, 해당 멤버가 클래스의 인스턴스가 아닌 클래스 자체의 멤버임을 나타낸다. 이 수정자가 적용된 슈퍼클래스의 멤버는 `final` 수정자가 없을 경우 서브클래스에서 재정의할 수 있다.

- `dynamic` 용어:
  Objective-C로 표현할 수 있는 클래스의 모든 멤버에 이 수정자를 적용한다. `dynamic` 수정자로 멤버 선언을 표시하면, 해당 멤버에 대한 접근은 항상 Objective-C 런타임을 통해 동적으로 디스패치된다. 컴파일러는 이 멤버를 인라인 처리하거나 가상화하지 않는다.

  `dynamic` 수정자로 표시된 선언은 Objective-C 런타임을 통해 디스패치되므로, `objc` 속성으로 표시해야 한다.

- `final` 용어:
  클래스나 클래스의 프로퍼티, 메서드, 서브스크립트 멤버에 이 수정자를 적용한다. 클래스에 적용하면 해당 클래스는 서브클래싱할 수 없음을 나타낸다. 클래스의 프로퍼티, 메서드, 서브스크립트에 적용하면 해당 멤버는 어떤 서브클래스에서도 재정의할 수 없음을 나타낸다. `final` 속성을 사용하는 예제는 <doc:Inheritance#Preventing-Overrides>를 참고한다.

- `lazy` 용어:
  클래스나 구조체의 저장 변수 프로퍼티에 이 수정자를 적용하면, 프로퍼티의 초기값이 처음 접근될 때 최대 한 번 계산되어 저장됨을 나타낸다. `lazy` 수정자를 사용하는 예제는 <doc:Properties#Lazy-Stored-Properties>를 참고한다.

- `optional` 용어:
  프로토콜의 프로퍼티, 메서드, 서브스크립트 멤버에 이 수정자를 적용하면, 해당 프로토콜을 준수하는 타입이 이 멤버를 구현할 필요가 없음을 나타낸다.

  `optional` 수정자는 `objc` 속성으로 표시된 프로토콜에만 적용할 수 있다. 따라서 클래스 타입만이 선택적 멤버 요구사항을 포함하는 프로토콜을 채택하고 준수할 수 있다. `optional` 수정자를 사용하는 방법과 선택적 프로토콜 멤버에 접근하는 방법에 대한 자세한 내용은 <doc:Protocols#Optional-Protocol-Requirements>를 참고한다.

<!--
  TODO: 현재는 선택적 이니셜라이저를 확인할 수 없으므로, 이니셜라이저를 @optional 속성으로 표시할 수 있더라도 문서에서 제외하고 있다. 컴파일러 팀이 결정 중이다. 선택적 이니셜라이저 요구사항이 제대로 작동하도록 결정되면 이 섹션을 업데이트한다.
-->

- `required` 용어:
  클래스의 지정 이니셜라이저나 편의 이니셜라이저에 이 수정자를 적용하면, 모든 서브클래스가 해당 이니셜라이저를 구현해야 함을 나타낸다. 서브클래스의 이니셜라이저 구현도 `required` 수정자로 표시해야 한다.

- `static` 용어:
  구조체, 클래스, 열거형, 프로토콜의 멤버에 이 수정자를 적용하면, 해당 멤버가 타입의 인스턴스가 아닌 타입 자체의 멤버임을 나타낸다. 클래스 선언 범위에서 멤버 선언에 `static` 수정자를 작성하는 것은 `class`와 `final` 수정자를 작성하는 것과 동일한 효과를 가진다. 그러나 클래스의 상수 타입 프로퍼티는 예외다: 이 선언에는 `class`나 `final`을 작성할 수 없으므로 `static`은 일반적인, 비클래스 의미를 가진다.

- `unowned` 용어:
  저장 변수, 상수, 저장 프로퍼티에 이 수정자를 적용하면, 변수나 프로퍼티가 값으로 저장된 객체에 대한 소유하지 않은 참조를 가짐을 나타낸다. 객체가 해제된 후 변수나 프로퍼티에 접근하려고 하면 런타임 오류가 발생한다. 약한 참조와 마찬가지로 프로퍼티나 값의 타입은 클래스 타입이어야 한다. 약한 참조와 달리 타입은 옵셔널이 아니다. `unowned` 수정자에 대한 예제와 자세한 내용은 <doc:AutomaticReferenceCounting#Unowned-References>를 참고한다.

- `unowned(safe)` 용어:
  `unowned`의 명시적 표기법이다.

- `unowned(unsafe)` 용어:
  저장 변수, 상수, 저장 프로퍼티에 이 수정자를 적용하면, 변수나 프로퍼티가 값으로 저장된 객체에 대한 소유하지 않은 참조를 가짐을 나타낸다. 객체가 해제된 후 변수나 프로퍼티에 접근하려고 하면, 객체가 있던 메모리 위치에 접근하게 되는데, 이는 메모리 안전하지 않은 작업이다. 약한 참조와 마찬가지로 프로퍼티나 값의 타입은 클래스 타입이어야 한다. 약한 참조와 달리 타입은 옵셔널이 아니다. `unowned` 수정자에 대한 예제와 자세한 내용은 <doc:AutomaticReferenceCounting#Unowned-References>를 참고한다.

- `weak` 용어:
  저장 변수나 저장 변수 프로퍼티에 이 수정자를 적용하면, 변수나 프로퍼티가 값으로 저장된 객체에 대한 약한 참조를 가짐을 나타낸다. 변수나 프로퍼티의 타입은 옵셔널 클래스 타입이어야 한다. 객체가 해제된 후 변수나 프로퍼티에 접근하면 값은 `nil`이 된다. `weak` 수정자에 대한 예제와 자세한 내용은 <doc:AutomaticReferenceCounting#Weak-References>를 참고한다.


### 접근 제어 수준

Swift는 다섯 가지 접근 제어 수준을 제공한다: `open`, `public`, `internal`, `fileprivate`, `private`.  
선언에 접근 제어 수준을 지정하려면 아래 접근 제어 수준 지정자 중 하나를 사용한다.  
접근 제어에 대한 자세한 내용은 <doc:AccessControl>에서 다룬다.

- `open`:  
  이 지정자를 사용하면 선언이 속한 모듈 내 코드에서 해당 선언에 접근하고 서브클래싱할 수 있다.  
  또한 `open`으로 표시된 선언은 해당 모듈을 임포트한 모듈의 코드에서도 접근 및 서브클래싱이 가능하다.

- `public`:  
  이 지정자를 사용하면 선언이 속한 모듈 내 코드에서 해당 선언에 접근하고 서브클래싱할 수 있다.  
  `public`으로 표시된 선언은 해당 모듈을 임포트한 모듈의 코드에서도 접근할 수 있지만, 서브클래싱은 불가능하다.

- `package`:  
  이 지정자를 사용하면 선언이 속한 패키지 내 코드에서만 해당 선언에 접근할 수 있다.  
  패키지는 빌드 시스템에서 정의한 코드 배포 단위다.  
  빌드 시스템이 코드를 컴파일할 때 `-package-name` 플래그를 Swift 컴파일러에 전달해 패키지 이름을 지정한다.  
  두 모듈이 동일한 패키지 이름으로 빌드되면 같은 패키지로 간주된다.

- `internal`:  
  이 지정자를 사용하면 선언이 속한 모듈 내 코드에서만 해당 선언에 접근할 수 있다.  
  기본적으로 대부분의 선언은 암묵적으로 `internal` 접근 제어 수준을 가진다.

- `fileprivate`:  
  이 지정자를 사용하면 선언이 속한 소스 파일 내 코드에서만 해당 선언에 접근할 수 있다.

- `private`:  
  이 지정자를 사용하면 선언이 포함된 스코프 내 코드에서만 해당 선언에 접근할 수 있다.

접근 제어 관점에서 확장(extension)은 다음과 같이 동작한다:

- 같은 파일에 여러 확장이 있고, 모두 동일한 타입을 확장한다면,  
  해당 확장들은 동일한 접근 제어 스코프를 가진다.  
  확장과 확장 대상 타입은 서로 다른 파일에 있을 수 있다.

- 확장이 확장 대상 타입과 같은 파일에 있다면,  
  확장은 타입과 동일한 접근 제어 스코프를 가진다.

- 타입 선언에서 `private`으로 선언된 멤버는 해당 타입의 확장에서 접근할 수 있다.  
  한 확장에서 `private`으로 선언된 멤버는 다른 확장과 확장 대상 타입 선언에서 접근할 수 있다.

위 접근 제어 지정자는 선택적으로 괄호로 둘러싼 `set` 키워드를 인자로 받을 수 있다(예: `private(set)`).  
이 형식은 변수나 서브스크립트의 setter에 변수나 서브스크립트 자체의 접근 제어 수준보다 낮거나 같은 접근 제어 수준을 지정할 때 사용한다.  
자세한 내용은 <doc:AccessControl#Getters-and-Setters>에서 다룬다.

> 선언 지정자 문법:
>
> *declaration-modifier* → **`class`** | **`convenience`** | **`dynamic`** | **`final`** | **`infix`** | **`lazy`** | **`optional`** | **`override`** | **`postfix`** | **`prefix`** | **`required`** | **`static`** | **`unowned`** | **`unowned`** **`(`** **`safe`** **`)`** | **`unowned`** **`(`** **`unsafe`** **`)`** | **`weak`** \
> *declaration-modifier* → *access-level-modifier* \
> *declaration-modifier* → *mutation-modifier* \
> *declaration-modifier* → *actor-isolation-modifier* \
> *declaration-modifiers* → *declaration-modifier* *declaration-modifiers*_?_
>
> *access-level-modifier* → **`private`** | **`private`** **`(`** **`set`** **`)`** \
> *access-level-modifier* → **`fileprivate`** | **`fileprivate`** **`(`** **`set`** **`)`** \
> *access-level-modifier* → **`internal`** | **`internal`** **`(`** **`set`** **`)`** \
> *access-level-modifier* → **`package`** | **`package`** **`(`** **`set`** **`)`** \
> *access-level-modifier* → **`public`** | **`public`** **`(`** **`set`** **`)`** \
> *access-level-modifier* → **`open`** | **`open`** **`(`** **`set`** **`)`**
>
> *mutation-modifier* → **`mutating`** | **`nonmutating`**
>
> *actor-isolation-modifier* → **`nonisolated`**

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


