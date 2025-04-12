# 문서 개정 내역

이 책의 최근 변경 사항을 확인한다.

**2025-03-31**

- Swift 6.1 업데이트.
- 제네릭을 위한 경량 구문으로 `some`을 사용하는 방법에 대한 정보를 <doc:OpaqueTypes#Opaque-Parameter-Types> 섹션에 추가.
- <doc:Attributes#available> 섹션에 `noasync` 인자에 대한 정보 추가.

**2024-09-23**

- Swift 6 업데이트.
- 엄격한 동시성 검사로의 마이그레이션에 대한 정보를 <doc:Attributes#preconcurrency> 섹션에 추가.
- 특정 타입의 오류를 던지는 방법에 대한 정보를 <doc:ErrorHandling#Specifying-the-Error-Type> 섹션에 추가.
- 매크로를 파라미터의 기본값으로 사용할 수 있게 되면서 <doc:Expressions#Macro-Expansion-Expression> 섹션 업데이트.
- 패키지 수준 접근 제어에 대한 정보를 <doc:AccessControl> 장에 추가.

**2024-03-05**

- Swift 5.10 업데이트.
- 중첩 프로토콜에 대한 정보를 <doc:Protocols#Delegation> 섹션에 추가.
- <doc:Attributes#UIApplicationMain> 및 <doc:Attributes#NSApplicationMain> 섹션에 사용 중단 정보 추가.

**2023-12-11**

- Swift 5.9.2 업데이트.
- `borrowing` 및 `consuming` 수정자에 대한 정보를 <doc:Declarations#Parameter-Modifiers> 섹션에 추가.
- 상수 선언 후 값을 설정하는 방법에 대한 정보를 <doc:TheBasics#Declaring-Constants-and-Variables> 섹션에 추가.
- 작업, 작업 그룹, 작업 취소에 대한 추가 정보를 <doc:Concurrency> 장에 추가.
- 기존 Swift 패키지에서 매크로를 구현하는 방법에 대한 정보를 <doc:Macros> 장에 추가.
- 확장 매크로가 준수 매크로를 대체하면서 <doc:Attributes#attached> 섹션 업데이트.
- 백디플로이먼트에 대한 정보를 <doc:Attributes#backDeployed> 섹션에 추가.

**2023-09-18**

- Swift 5.9 업데이트.
- `if` 및 `switch` 표현식에 대한 정보를 <doc:ControlFlow> 장 및 <doc:Expressions#Conditional-Expression> 섹션에 추가.
- 컴파일 타임에 코드를 생성하는 방법에 대한 정보를 담은 <doc:Macros> 장 추가.
- <doc:TheBasics>에서 옵셔널에 대한 논의 확장.
- <doc:GuidedTour>에 동시성 예제 추가.
- 박스형 프로토콜 타입에 대한 정보를 <doc:OpaqueTypes> 장에 추가.
- `buildPartialBlock(first:)` 및 `buildPartialBlock(accumulated:next:)` 메서드에 대한 정보를 <doc:Attributes#Result-Transformations> 섹션에 추가.
- visionOS를 <doc:Attributes#available> 및 <doc:Statements#Conditional-Compilation-Block>의 플랫폼 목록에 추가.
- 공식 문법을 그룹화하기 위해 빈 줄을 사용하도록 형식화.

**2023-03-30**

- Swift 5.8 업데이트.
- 오류 처리 외부에서 `defer`를 사용하는 방법을 보여주는 <doc:ControlFlow#Deferred-Actions> 섹션 추가.
- Swift-DocC를 출판에 채택.
- 전체적으로 사소한 수정 및 추가.

**2022-09-12**

- Swift 5.7 업데이트.
- 액터와 작업 간 데이터 전송에 대한 정보를 담은 <doc:Concurrency#Sendable-Types> 섹션 추가, `@Sendable` 및 `@unchecked` 속성에 대한 정보를 <doc:Attributes#Sendable> 및 <doc:Attributes#unchecked> 섹션에 추가.
- 정규 표현식을 생성하는 방법에 대한 정보를 담은 <doc:LexicalStructure#Regular-Expression-Literals> 섹션 추가.
- `if`-`let`의 짧은 형식에 대한 정보를 <doc:TheBasics#Optional-Binding> 섹션에 추가.
- `#unavailable`에 대한 정보를 <doc:ControlFlow#Checking-API-Availability> 섹션에 추가.

**2022-03-14**

- Swift 5.6 업데이트.
- 체인 메서드 호출 및 기타 후위 표현식 주위에서 `#if`를 사용하는 방법에 대한 정보로 <doc:Expressions#Explicit-Member-Expression> 섹션 업데이트.
- 전체적으로 그림의 시각적 스타일 업데이트.

**2021-09-20**

- Swift 5.5 업데이트.
- 비동기 함수, 작업, 액터에 대한 정보를 <doc:Concurrency> 장 및 <doc:Declarations#Actor-Declaration>, <doc:Declarations#Asynchronous-Functions-and-Methods>, <doc:Expressions#Await-Operator> 섹션에 추가.
- 밑줄로 시작하는 식별자에 대한 정보로 <doc:LexicalStructure#Identifiers> 섹션 업데이트.

**2021-04-26**

- Swift 5.4 업데이트.
- 결과 빌더에 대한 정보를 담은 <doc:AdvancedOperators#Result-Builders> 및 <doc:Attributes#resultBuilder> 섹션 추가.
- 함수 호출에서 in-out 파라미터가 안전하지 않은 포인터로 암시적으로 변환되는 방법에 대한 정보를 담은 <doc:Expressions#Implicit-Conversion-to-a-Pointer-Type> 섹션 추가.
- 함수가 여러 가변 파라미터를 가질 수 있게 되면서 <doc:Functions#Variadic-Parameters> 및 <doc:Declarations#Function-Declaration> 섹션 업데이트.
- 암시적 멤버 표현식을 함께 연결할 수 있게 되면서 <doc:Expressions#Implicit-Member-Expression> 섹션 업데이트.

**2020-09-16**

- Swift 5.3 업데이트.
- 여러 후행 클로저에 대한 정보를 <doc:Closures#Trailing-Closures> 섹션에 추가, 후행 클로저가 파라미터와 어떻게 매칭되는지에 대한 정보를 <doc:Expressions#Function-Call-Expression> 섹션에 추가.
- 열거형에 대한 `Comparable`의 합성 구현에 대한 정보를 <doc:Protocols#Adopting-a-Protocol-Using-a-Synthesized-Implementation> 섹션에 추가.
- 더 많은 곳에서 일반 `where` 절을 작성할 수 있게 되면서 <doc:Generics#Contextual-Where-Clauses> 섹션 추가.
- 옵셔널 값과 함께 사용할 수 있는 소유하지 않은 참조에 대한 정보를 담은 <doc:AutomaticReferenceCounting#Unowned-Optional-References> 섹션 추가.
- `@main` 속성에 대한 정보를 <doc:Attributes#main> 섹션에 추가.
- `#filePath`를 <doc:Expressions#Literal-Expression> 섹션에 추가, `#file`에 대한 논의 업데이트.
- 더 많은 시나리오에서 클로저가 `self`를 암시적으로 참조할 수 있게 되면서 <doc:Closures#Escaping-Closures> 섹션 업데이트.
- `catch` 절이 여러 오류와 매칭될 수 있게 되면서 <doc:ErrorHandling#Handling-Errors-Using-Do-Catch> 및 <doc:Statements#Do-Statement> 섹션 업데이트.
- `Any`에 대한 추가 정보를 제공하고 새로운 <doc:Types#Any-Type> 섹션으로 이동.
- 지연 속성이 관찰자를 가질 수 있게 되면서 <doc:Properties#Property-Observers> 섹션 업데이트.
- 열거형의 멤버가 프로토콜 요구사항을 충족할 수 있게 되면서 <doc:Declarations#Protocol-Declaration> 섹션 업데이트.
- 관찰자가 호출되기 전에 게터가 호출되는 시점을 설명하기 위해 <doc:Declarations#Stored-Variable-Observers-and-Property-Observers> 섹션 업데이트.
- 원자적 연산에 대해 언급하기 위해 <doc:MemorySafety> 장 업데이트.

**2020-03-24**

- Swift 5.2 업데이트.
- 클로저 대신 키 경로를 전달하는 방법에 대한 정보를 <doc:Expressions#Key-Path-Expression> 섹션에 추가.
- 클래스, 구조체, 열거형의 인스턴스를 함수 호출 구문과 함께 사용할 수 있게 해주는 구문적 설탕에 대한 정보를 담은 <doc:Declarations#Methods-with-Special-Names> 섹션 추가.
- 서브스크립트가 기본값을 가진 파라미터를 지원하게 되면서 <doc:Subscripts#Subscript-Options> 섹션 업데이트.
- `Self`가 더 많은 컨텍스트에서 사용될 수 있게 되면서 <doc:Types#Self-Type> 섹션 업데이트.
- 암시적으로 언래핑된 옵셔널 값이 옵셔널 또는 비옵셔널 값으로 사용될 수 있음을 명확히 하기 위해 <doc:TheBasics#Implicitly-Unwrapped-Optionals> 섹션 업데이트.

**2019-09-10**

- Swift 5.1 업데이트.
- 특정 명명된 반환 타입을 제공하는 대신 반환 값이 준수하는 프로토콜을 지정하는 함수에 대한 정보를 <doc:OpaqueTypes> 장에 추가.
- 속성 래퍼에 대한 정보를 <doc:Properties#Property-Wrappers> 섹션에 추가.
- 라이브러리 진화를 위해 고정된 열거형과 구조체에 대한 정보를 <doc:Attributes#frozen> 섹션에 추가.
- `return`을 생략하는 함수에 대한 정보를 담은 <doc:Functions#Functions-With-an-Implicit-Return> 및 <doc:Properties#Shorthand-Getter-Declaration> 섹션 추가.
- 타입에서 서브스크립트를 사용하는 방법에 대한 정보를 <doc:Subscripts#Type-Subscripts> 섹션에 추가.
- 열거형 케이스 패턴이 옵셔널 값과 매칭될 수 있게 되면서 <doc:Patterns#Enumeration-Case-Pattern> 섹션 업데이트.
- 멤버별 이니셜라이저가 기본값을 가진 속성에 대한 파라미터를 생략할 수 있게 되면서 <doc:Initialization#Memberwise-Initializers-for-Structure-Types> 섹션 업데이트.
- 런타임에 키 경로로 조회되는 동적 멤버에 대한 정보를 <doc:Attributes#dynamicMemberLookup> 섹션에 추가.
- `macCatalyst`를 <doc:Statements#Conditional-Compilation-Block>의 대상 환경 목록에 추가.
- `Self`가 현재 클래스, 구조체, 열거형 선언에 의해 도입된 타입을 참조할 수 있게 되면서 <doc:Types#Self-Type> 섹션 업데이트.

**2019-03-25**

- Swift 5.0 업데이트.
- 확장 문자열 구분자에 대한 정보를 담은 <doc:StringsAndCharacters#Extended-String-Delimiters> 섹션 추가 및 <doc:LexicalStructure#String-Literals> 섹션 업데이트.
- `dynamicCallable` 속성을 사용하여 인스턴스를 동적으로 함수로 호출하는 방법에 대한 정보를 담은 <doc:Attributes#dynamicCallable> 섹션 추가.
- 스위치 문에서 미래의 열거형 케이스를 처리하는 방법에 대한 정보를 담은 <doc:Attributes#unknown> 및 <doc:Statements#Switching-Over-Future-Enumeration-Cases> 섹션 추가.
- 아이덴티티 키 경로(`\.self`)에 대한 정보를 <doc:Expressions#Key-Path-Expression> 섹션에 추가.
- 플랫폼 조건에서 `<` 연산자를 사용하는 방법에 대한 정보를 <doc:Statements#Conditional-Compilation-Block> 섹션에 추가.

**2018-09-17**

- Swift 4.2 업데이트.
- 열거형의 모든 케이스에 접근하는 방법에 대한 정보를 <doc:Enumerations#Iterating-over-Enumeration-Cases> 섹션에 추가.
- `#error` 및 `#warning`에 대한 정보를 <doc:Statements#Compile-Time-Diagnostic-Statement> 섹션에 추가.
- `inlinable` 및 `usableFromInline` 속성 아래 <doc:Attributes#Declaration-Attributes> 섹션에 인라이닝에 대한 정보 추가.
- 런타임에 이름으로 조회되는 멤버에 대한 정보를 <doc:Attributes#Declaration-Attributes> 섹션에 추가.
- `requires_stored_property_inits` 및 `warn_unqualified_access` 속성에 대한 정보를 <doc:Attributes#Declaration-Attributes> 섹션에 추가.
- 사용 중인 Swift 컴파일러 버전에 따라 코드를 조건부로 컴파일하는 방법에 대한 정보를 <doc:Statements#Conditional-Compilation-Block> 섹션에 추가.
- `#dsohandle`에 대한 정보를 <doc:Expressions#Literal-Expression> 섹션에 추가.

**2018-03-29**

- Swift 4.1 업데이트.
- 동등 연산자의 합성 구현에 대한 정보를 <doc:AdvancedOperators#Equivalence-Operators> 섹션에 추가.
- 조건부 프로토콜 준수에 대한 정보를 <doc:Declarations#Extension-Declaration> 섹션 및 <doc:Protocols#Conditionally-Conforming-to-a-Protocol> 섹션에 추가.
- 재귀적 프로토콜 제약에 대한 정보를 <doc:Generics#Using-a-Protocol-in-Its-Associated-Types-Constraints> 섹션에 추가.
- `canImport()` 및 `targetEnvironment()` 플랫폼 조건에 대한 정보를 <doc:Statements#Conditional-Compilation-Block>에 추가.

**2017-12-04**

- Swift 4.0.3 업데이트.
- 키 경로가 서브스크립트 컴포넌트를 지원하게 되면서 <doc:Expressions#Key-Path-Expression> 섹션 업데이트.

**2017-09-19**

- Swift 4.0 업데이트.
- 메모리에 대한 배타적 접근에 대한 정보를 <doc:MemorySafety> 장에 추가.
- 일반 `where` 절을 사용하여 연관 타입을 제한할 수 있게 되면서 <doc:Generics#Associated-Types-with-a-Generic-Where-Clause> 섹션 추가.
- 여러 줄 문자열 리터럴에 대한 정보를 <doc:StringsAndCharacters#String-Literals> 섹션 및 <doc:LexicalStructure#String-Literals> 섹션에 추가.
- `objc` 속성이 더 적은 곳에서 추론되게 되면서 <doc:Attributes#Declaration-Attributes>에서 `objc` 속성에 대한 논의 업데이트.
- 서브스크립트가 일반화될 수 있게 되면서 <doc:Generics#Generic-Subscripts> 섹션 추가.
- 프로토콜 합성 타입이 슈퍼클래스 요구사항을 포함할 수 있게 되면서 <doc:Protocols#Protocol-Composition> 섹션 및 <doc:Types#Protocol-Composition-Type> 섹션 업데이트.
- 프로토콜 확장에서 `final`이 허용되지 않게 되면서 <doc:Declarations#Extension-Declaration>에서 프로토콜 확장에 대한 논의 업데이트.
- 전제 조건 및 치명적 오류에 대한 정보를 <doc:TheBasics#Assertions-and-Preconditions> 섹션에 추가.

**2017-03-27**

- Swift 3.1 업데이트.
- 요구사항을 포함하는 확장에 대한 정보를 담은 <doc:Generics#Extensions-with-a-Generic-Where-Clause> 섹션 추가.
- 범위를 반복하는 예제를 <doc:ControlFlow#For-In-Loops> 섹션에 추가.
- 실패 가능한 숫자 변환 예제를 <doc:Initialization#Failable-Initializers> 섹션에 추가.
- Swift 언어 버전과 함께 `available` 속성을 사용하는 방법에 대한 정보를 <doc:Attributes#Declaration-Attributes> 섹션에 추가.
- 함수 타입을 작성할 때 인수 레이블이 허용되지 않음을 언급하기 위해 <doc:Types#Function-Type> 섹션 업데이트.
- Swift 언어 버전 번호에 대한 논의 업데이트, 이제 선택적 패치 번호가 허용됨.
- 여러 파라미터를 취하는 함수와 튜플 타입의 단일 파라미터를 취하는 함수를 구분할 수 있게 되면서 <doc:Types#Function-Type> 섹션 업데이트.
- `type(of:)`가 Swift 표준 라이브러리 함수가 되면서 <doc:Expressions> 장에서 동적 타입 표현 섹션 제거.

**2016-10-27**

- Swift 3.0.1 업데이트.
- <doc:AutomaticReferenceCounting> 장에서 약한 및 소유하지 않은 참조에 대한 논의 업데이트.
- `unowned`, `unowned(safe)`, `unowned(unsafe)` 선언 수정자에 대한 정보를 <doc:Declarations#Declaration-Modifiers> 섹션에 추가.
- `Any` 타입의 값이 예상될 때 옵셔널 값을 사용하는 방법에 대한 정보를 <doc:TypeCasting#Type-Casting-for-Any-and-AnyObject> 섹션에 추가.
- 괄호 표현식과 튜플 표현식에 대한 논의를 분리하기 위해 <doc:Expressions> 장 업데이트.

**2016-09-13**

- Swift 3.0 업데이트.
- 모든 파라미터가 기본적으로 인수 레이블을 가질 수 있게 되면서 <doc:Functions> 장 및 <doc:Declarations#Function-Declaration> 섹션에서 함수에 대한 논의 업데이트.
- 연산자를 전역 함수 대신 타입 메서드로 구현할 수 있게 되면서 <doc:AdvancedOperators> 장에서 연산자에 대한 논의 업데이트.
- `open` 및 `fileprivate` 접근 레벨 수정자에 대한 정보를 <doc:AccessControl> 장에 추가.
- `inout`이 파라미터 이름 앞이 아니라 파라미터 타입 앞에 나타나게 되면서 <doc:Declarations#Function-Declaration> 섹션에서 `inout`에 대한 논의 업데이트.
- `@noescape` 및 `@autoclosure` 속성이 선언 속성 대신 타입 속성이 되면서 <doc:Closures#Escaping-Closures> 및 <doc:Closures#Autoclosures> 섹션과 <doc:Attributes> 장에서 논의 업데이트.
- 연산자 우선순위 그룹에 대한 정보를 <doc:AdvancedOperators#Precedence-for-Custom-Infix-Operators> 섹션 및 <doc:Declarations#Precedence-Group-Declaration> 섹션에 추가.
- macOS 대신 OS X, `Error` 대신 `ErrorProtocol`, `ExpressibleByStringLiteral`과 같은 프로토콜 이름 사용 등 전체적으로 논의 업데이트.
- 일반 `where` 절이 선언 끝에 작성될 수 있게 되면서 <doc:Generics#Generic-Where-Clauses> 섹션 및 <doc:GenericParametersAndArguments> 장에서 논의 업데이트.
- 클로저가 기본적으로 비탈출 가능하게 되면서 <doc:Closures#Escaping-Closures> 섹션에서 논의 업데이트.
- `if`, `while`, `guard` 문이 `where` 절 없이 쉼표로 구분된 조건 목록을 사용할 수 있게 되면서 <doc:TheBasics#Optional-Binding> 섹션 및 <doc:Statements#While-Statement> 섹션에서 논의 업데이트.
- 스위치 케이스가 여러 패턴을 가질 수 있게 되면서 <doc:ControlFlow#Switch> 섹션 및 <doc:Statements#Switch-Statement> 섹션에서 논의 업데이트.
- 함수 인수 레이블이 더 이상 함수 타입의 일부가 아니게 되면서 <doc:Types#Function-Type> 섹션에서 함수 타입에 대한 논의 업데이트.
- 프로토콜 합성 타입이 새로운 `Protocol1 & Protocol2` 구문을 사용하게 되면서 <doc:Protocols#Protocol-Composition> 섹션 및 <doc:Types#Protocol-Composition-Type> 섹션에서 논의 업데이트.
- 동적 타입 표현이 새로운 `type(of:)` 구문을 사용하게 되면서 동적 타입 표현 섹션에서 논의 업데이트.
- 라인 제어 문이 새로운 `#sourceLocation(file:line:)` 구문을 사용하게 되면서 <doc:Statements#Line-Control-Statement> 섹션에서 논의 업데이트.
- `Never` 타입을 사용하게 되면서 <doc:Declarations#Functions-that-Never-Return>에서 논의 업데이트.
- 플레이그라운드 리터럴에 대한 정보를 <doc:Expressions#Literal-Expression> 섹션에 추가.
- 비탈출 클로저만 in-out 파라미터를 캡처할 수 있게 되면서 <doc:Declarations#In-Out-Parameters> 섹션에서 논의 업데이트.
- 함수 호출에서 기본 파라미터를 재정렬할 수 없게 되면서 <doc:Functions#Default-Parameter-Values> 섹션에서 논의 업데이트.
- 속성 인수가 콜론을 사용하게 되면서 <doc:Attributes> 장 업데이트.
- 재던지는 함수의 `catch` 블록 내에서 오류를 던지는 방법에 대한 정보를 <doc:Declarations#Rethrowing-Functions-and-Methods> 섹션에 추가.
- Objective-C 속성의 게터 또는 세터의 선택자에 접근하는 방법에 대한 정보를 <doc:Expressions#Selector-Expression> 섹션에 추가.
- 일반 타입 별칭 및 프로토콜 내에서 타입 별칭을 사용하는 방법에 대한 정보를 <doc:Declarations#Type-Alias-Declaration> 섹션에 추가.
- 함수 타입에서 파라미터 타입 주위에 괄호가 필요하게 되면서 <doc:Types#Function-Type> 섹션에서 논의 업데이트.
- `@IBAction`, `@IBOutlet`, `@NSManaged` 속성이 `@objc` 속성을 암시하게 되면서 <doc:Attributes> 장 업데이트.
- `@GKInspectable` 속성에 대한 정보를 <doc:Attributes#Declaration-Attributes> 섹션에 추가.
- 옵셔널 프로토콜 요구사항이 Objective-C와 상호 운용되는 코드에서만 사용됨을 명확히 하기 위해 <doc:Protocols#Optional-Protocol-Requirements> 섹션에서 논의 업데이트.
- 함수 파라미터에서 명시적으로 `let`을 사용하는 논의를 <doc:Declarations#Function-Declaration> 섹션에서 제거.
- `Boolean` 프로토콜이 Swift 표준 라이브러리에서 제거되면서 <doc:Statements> 장에서 논의 제거.
- `@NSApplicationMain` 속성에 대한 논의를 <doc:Attributes#Declaration-Attributes> 섹션에서 수정.

**2016-03-21**

- Swift 2.2 업데이트.
- 사용 중인 Swift 버전에 따라 코드를 조건부로 컴파일하는 방법에 대한 정보를 <doc:Statements#Conditional-Compilation-Block> 섹션에 추가.
- 인수 이름만 다른 메서드 또는 이니셜라이저를 구별하는 방법에 대한 정보를 <doc:Expressions#Explicit-Member-Expression> 섹션에 추가.
- Objective-C 선택자에 대한 `#selector` 구문에 대한 정보를 <doc:Expressions#Selector-Expression> 섹션에 추가.
- 연관 타입에 `associatedtype` 키워드를 사용하게 되면서 <doc:Generics#Associated-Types> 및 <doc:Declarations#Protocol-Associated-Type-Declaration> 섹션 업데이트.
- 인스턴스가 완전히 초기화되기 전에 `nil`을 반환하는 이니셜라이저에 대한 정보를 <doc:Initialization#Failable-Initializers> 섹션에 업데이트.
- 튜플 비교에 대한 정보를 <doc:BasicOperators#Comparison-Operators> 섹션에 추가.
- 키워드를 외부 파라미터 이름으로 사용하는 방법에 대한 정보를 <doc:LexicalStructure#Keywords-and-Punctuation> 섹션에 추가.
- 열거형 및 열거형 케이스가 `@objc` 속성을 사용할 수 있게 되면서 <doc:Attributes#Declaration-Attributes> 섹션에서 논의 업데이트.
- 점을 포함하는 커스텀 연산자에 대한 논의를 <doc:LexicalStructure#Operators> 섹션에 추가.
- 재던지는 함수가 직접 오류를 던질 수 없음을 언급하기 위해 <doc:Declarations#Rethrowing-Functions-and-Methods> 섹션에 추가.
- 속성을 in-out 파라미터로 전달할 때 속성 관찰자가 호출됨을 언급하기 위해 <doc:Properties#Property-Observers> 섹션에 추가.
- 오류 처리에 대한 섹션을 <doc:GuidedTour> 장에 추가.
- <doc:AutomaticReferenceCounting#Weak-References> 섹션의 그림을 더 명확하게 업데이트.
- C 스타일 `for` 루프, `++` 전위 및 후위 연산자, `--` 전위 및 후위 연산자에 대한 논의 제거.
- 가변 함수 인수 및 커리 함수에 대한 특수 구문에 대한 논의 제거.

**2015-10-20**

- Swift 2.1 업데이트.
- 문자열 보간이 문자열 리터럴을 포함할 수 있게 되면서 <doc:StringsAndCharacters#String-Interpolation> 및 <doc:LexicalStructure#String-Literals> 섹션 업데이트.
- `@noescape` 속성에 대한 정보를 담은 <doc:Closures#Escaping-Closures> 섹션 추가.
- tvOS에 대한 정보를 <doc:Attributes#Declaration-Attributes> 및 <doc:Statements#Conditional-Compilation-Block> 섹션에 추가.
- in-out 파라미터의 동작에 대한 정보를 <doc:Declarations#In-Out-Parameters> 섹션에 추가.
- 클로저 캡처 목록에 지정된 값이 어떻게 캡처되는지에 대한 정보를 <doc:Expressions#Capture-Lists> 섹션에 추가.
- 옵셔널 체인을 통해 할당이 어떻게 동작하는지 명확히 하기 위해 <doc:OptionalChaining#Accessing-Properties-Through-Optional-Chaining> 섹션 업데이트.
- <doc:Closures#Autoclosures> 섹션에서 자동 클로저에 대한 논의 개선.
- `??` 연산자를 사용하는 예제를 <doc:GuidedTour> 장에 추가.

**2015-09-16**

- Swift 2.0 업데이트.
- 오류 처리에 대한 정보를 <doc:ErrorHandling> 장, <doc:Statements#Do-Statement> 섹션, <doc:Statements#Throw-Statement> 섹션, <doc:Statements#Defer-Statement> 섹션, <doc:Expressions#Try-Operator> 섹션에 추가.
- 모든 타입이 `ErrorType` 프로토콜을 준수할 수 있게 되면서 <doc:ErrorHandling#Representing-and-Throwing-Errors> 섹션 업데이트.
- 새로운 `try?` 키워드에 대한 정보를 <doc:ErrorHandling#Converting-Errors-to-Optional-Values> 섹션에 추가.
- 재귀적 열거형에 대한 정보를 <doc:Enumerations#Recursive-Enumerations> 섹션 및 <doc:Declarations#Enumerations-with-Cases-of-Any-Type> 섹션에 추가.
- API 가용성 확인에 대한 정보를 <doc:ControlFlow#Checking-API-Availability> 섹션 및 <doc:Statements#Availability-Condition> 섹션에 추가.
- 새로운 `guard` 문에 대한 정보를 <doc:ControlFlow#Early-Exit> 섹션 및 <doc:Statements#Guard-Statement> 섹션에 추가.
- 프로토콜 확장에 대한 정보를 <doc:Protocols#Protocol-Extensions> 섹션에 추가.
- 단위 테스트를 위한 접근 제어에 대한 정보를 <doc:AccessControl#Access-Levels-for-Unit-Test-Targets> 섹션에 추가.
- 새로운 옵셔널 패턴에 대한 정보를 <doc:Patterns#Optional-Pattern> 섹션에 추가.
- `repeat`-`while` 루프에 대한 정보로 <doc:ControlFlow#Repeat-While> 섹션 업데이트.
- `String`이 더 이상 Swift 표준 라이브러리의 `CollectionType` 프로토콜을 준수하지 않게 되면서 <doc:StringsAndCharacters> 장 업데이트.
- Swift 표준 라이브러리의 새로운 `print(_:separator:terminator)` 함수에 대한 정보를 <doc:TheBasics#Printing-Constants-and-Variables> 섹션에 추가.
- `String` 원시 값을 가진 열거형 케이스의 동작에 대한 정보를 <doc:Enumerations#Implicitly-Assigned-Raw-Values> 섹션 및 <doc:Declarations#Enumerations-with-Cases-of-a-Raw-Value-Type> 섹션에 추가.
- `@autoclosure` 속성의 `@autoclosure(escaping)` 형식에 대한 정보를 <doc:Closures#Autoclosures> 섹션에 추가.
- `@available` 및 `@warn_unused_result` 속성에 대한 정보를 <doc:Attributes#Declaration-Attributes> 섹션에 추가.
- `@convention` 속성에 대한 정보를 <doc:Attributes#Type-Attributes> 섹션에 추가.
- `where` 절과 함께 여러 옵셔널 바인딩을 사용하는 예제를 <doc:TheBasics#Optional-Binding> 섹션에 추가.
- `+` 연산자를 사용하여 문자열 리터럴을 컴파일 타임에 연결하는 방법에 대한 정보를 <doc:LexicalStructure#String-Literals> 섹션에 추가.
- 메타타입 값을 비교하고 이를 사용하여 이니셜라이저 표현식으로 인스턴스를 생성하는 방법에 대한 정보를 <doc:Types#Metatype-Type> 섹션에 추가.
- 사용자 정의 어설션이 비활성화되는 시점에 대한 정보를 <doc:TheBasics#Debugging-with-Assertions> 섹션에 추가.
- `@NSManaged` 속성이 특정 인스턴스 메서드에 적용될 수 있게 되면서 <doc:Attributes#Declaration-Attributes> 섹션에서 논의 업데이트.
- 가변 파라미터가 함수 파라미터 목록의 어느 위치에든 선언될 수 있게 되면서 <doc:Functions#Variadic-Parameters> 섹션 업데이트.
- 비실패 가능 이니셜라이저가 슈퍼클래스의 이니셜라이저 결과를 강제 언래핑하여 실패 가능 이니셜라이저에 위임할 수 있게 되면서 <doc:Initialization#Overriding-a-Failable-Initializer> 섹션 업데이트.
- 열거형 케이스를 함수로 사용하는 방법에 대한 정보를 <doc:Declarations#Enumerations-with-Cases-of-Any-Type> 섹션에 추가.
- 이니셜라이저를 명시적으로 참조하는 방법에 대한 정보를 <doc:Expressions#Initializer-Expression> 섹션에 추가.
- 빌드 구성 및 라인 제어 문에 대한 정보를 <doc:Statements#Compiler-Control-Statements> 섹션에 추가.
- 메타타입 값에서 클래스 인스턴스를 생성하는 방법에 대한 정보를 <doc:Types#Metatype-Type> 섹션에 추가.
- 약한 참조가 캐싱에 적합하지 않음을 언급하기 위해 <doc:AutomaticReferenceCounting#Weak-References> 섹션에 추가.
- 저장된 타입 속성이 지연 초기화됨을 언급하기 위해 <doc:Properties#Type-Properties> 섹션 업데이트.
- 클로저에서 변수와 상수가 어떻게 캡처되는지 명확히 하기 위해 <doc:Closures#Capturing-Values> 섹션 업데이트.
- 클래스에 `@objc` 속성을 적용할 수 있는 시점을 설명하기 위해 <doc:Attributes#Declaration-Attributes> 섹션 업데이트.
- `throw` 문을 실행하는 성능에 대한 정보를 <doc:ErrorHandling#Handling-Errors> 섹션에 추가. `do` 문에 대한 유사한 정보를 <doc:Statements#Do-Statement> 섹션에 추가.
- 클래스, 구조체, 열거형에 대한 저장 및 계산 타입 속성에 대한 정보로 <doc:Properties#Type-Properties> 섹션 업데이트.
- 레이블이 지정된 `break` 문에 대한 정보를 <doc:Statements#Break-Statement> 섹션에 추가.
- `willSet` 및 `didSet` 관찰자의 동작을 명확히 하기 위해 <doc:Properties#Property-Observers> 섹션 업데이트.
- `private` 접근의 범위에 대한 정보를 <doc:AccessControl#Access-Levels> 섹션에 추가.
- 약한 참조가 가비지 수집 시스템과 ARC 간에 어떻게 다른지에 대한 정보를 <doc:AutomaticReferenceCounting#Weak-References> 섹션에 추가.
- 유니코드 스칼라에 대한 더 정확한 정의로 <doc:StringsAndCharacters#Special-Characters-in-String-Literals> 섹션 업데이트.

**2015-04-08**

- Swift 1.2 업데이트.
- Swift에 기본 `Set` 컬렉션 타입이 추가됨. 자세한 정보는 <doc:CollectionTypes#Sets> 참조.
- `@autoclosure`이 이제 파라미터 선언의 속성이 됨. 또한 새로운 `@noescape`


