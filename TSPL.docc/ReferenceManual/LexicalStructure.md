# 어휘 구조

문법의 가장 기본적인 요소를 사용한다.

Swift의 *어휘 구조*는 어떤 문자 시퀀스가 유효한 토큰을 구성하는지 설명한다.  
이 유효한 토큰들은 언어의 가장 기본적인 구성 요소이며, 이후 장에서 언어의 나머지 부분을 설명하는 데 사용된다.  
토큰은 식별자, 키워드, 구두점, 리터럴 또는 연산자로 구성된다.

대부분의 경우, Swift 소스 파일의 문자로부터 토큰이 생성된다.  
이때 아래에 명시된 문법 제약 조건 내에서 입력 텍스트에서 가능한 가장 긴 부분 문자열을 고려한다.  
이러한 동작을 *최장 일치* 또는 *최대 길이 우선*이라고 부른다.


## 공백과 주석

공백은 두 가지 용도로 사용된다. 소스 파일에서 토큰을 구분하거나, 접두사, 접미사, 중위 연산자를 구별하는 데 쓰인다(자세한 내용은 <doc:LexicalStructure#Operators> 참조). 이 외의 경우에는 무시된다. 다음 문자들은 공백으로 간주된다:
- 스페이스 (U+0020)
- 줄 바꿈 (U+000A)
- 캐리지 리턴 (U+000D)
- 수평 탭 (U+0009)
- 수직 탭 (U+000B)
- 폼 피드 (U+000C)
- 널 (U+0000)

<!--
  공백 문자는 유니코드 스칼라 값 순서가 아니라,
  중요도와 사용 빈도를 기준으로 대략 나열했다.
-->

컴파일러는 주석을 공백으로 취급한다. 한 줄 주석은 `//`로 시작하며, 줄 바꿈(U+000A)이나 캐리지 리턴(U+000D)이 나올 때까지 계속된다. 여러 줄 주석은 `/*`로 시작하고 `*/`로 끝난다. 여러 줄 주석을 중첩할 수 있지만, 주석 표시자는 반드시 균형을 맞춰야 한다.

주석은 [Markup Formatting Reference](https://developer.apple.com/library/content/documentation/Xcode/Reference/xcode_markup_formatting_ref/index.html)에 설명된 대로 추가적인 서식과 마크업을 포함할 수 있다.

> 공백 문법:
>
> *whitespace* → *whitespace-item* *whitespace*_?_ \
> *whitespace-item* → *line-break* \
> *whitespace-item* → *inline-space* \
> *whitespace-item* → *comment* \
> *whitespace-item* → *multiline-comment* \
> *whitespace-item* → U+0000, U+000B, or U+000C
>
> *line-break* → U+000A \
> *line-break* → U+000D \
> *line-break* → U+000D followed by U+000A
>
> *inline-spaces* → *inline-space* *inline-spaces*_?_ \
> *inline-space* → U+0009 or U+0020
>
> *comment* → **`//`** *comment-text* *line-break* \
> *multiline-comment* → **`/*`** *multiline-comment-text* **`*/`**
>
> *comment-text* → *comment-text-item* *comment-text*_?_ \
> *comment-text-item* → Any Unicode scalar value except U+000A or U+000D
>
> *multiline-comment-text* → *multiline-comment-text-item* *multiline-comment-text*_?_ \
> *multiline-comment-text-item* → *multiline-comment* \
> *multiline-comment-text-item* → *comment-text-item* \
> *multiline-comment-text-item* → Any Unicode scalar value except  **`/*`** or  **`*/`**


## 식별자

**식별자**는 다음과 같은 문자로 시작한다:
- 대문자 또는 소문자 A부터 Z
- 언더스코어(`_`)
- 기본 다국어 평면(Basic Multilingual Plane)에 속한 비결합 알파벳 유니코드 문자
- 기본 다국어 평면 외부에 있지만 사적 사용 영역(Private Use Area)에 속하지 않은 문자

첫 번째 문자 이후에는 숫자와 결합 유니코드 문자도 사용할 수 있다.

언더스코어로 시작하는 식별자, 첫 번째 인자 레이블이 언더스코어로 시작하는 서브스크립트, 그리고 첫 번째 인자 레이블이 언더스코어로 시작하는 초기화 구문은 `public` 접근 레벨 제어자를 사용하더라도 내부용으로 간주한다. 이 규칙은 프레임워크 개발자가 클라이언트가 상호작용하거나 의존하지 말아야 하는 API 부분을 표시할 수 있게 한다. 또한, 두 개의 언더스코어로 시작하는 식별자는 Swift 컴파일러와 표준 라이브러리가 사용하도록 예약되어 있다.

예약어를 식별자로 사용하려면 앞뒤에 백틱(\`)을 추가한다. 예를 들어, `class`는 유효한 식별자가 아니지만 `` `class` ``는 유효하다. 백틱은 식별자의 일부로 간주되지 않는다. 따라서 `` `x` ``와 `x`는 같은 의미를 가진다.

<!--
위 단락은 코드 음성에서 ` 사용과 관련된 알려진 문제로 인해 링크 해결 경고를 발생시킨다.

https://github.com/swiftlang/swift-book/issues/71
https://github.com/swiftlang/swift-markdown/issues/93
-->

명시적인 매개변수 이름이 없는 클로저 내부에서는 매개변수가 암시적으로 `$0`, `$1`, `$2` 등으로 이름 지어진다. 이러한 이름은 클로저 범위 내에서 유효한 식별자이다.

컴파일러는 프로퍼티 래퍼 프로젝션을 가진 프로퍼티에 대해 달러 기호(`$`)로 시작하는 식별자를 생성한다. 코드에서 이러한 식별자와 상호작용할 수 있지만, 해당 접두사로 식별자를 직접 선언할 수는 없다. 자세한 내용은 <doc:Attributes> 장의 <doc:Attributes#propertyWrapper> 섹션을 참고한다.

<!--
위의 교차 참조는 섹션과 장을 모두 포함한다. "propertyWrapper"가 섹션의 제목이지만, 섹션 이름이 제목 대문자 표기법을 따르지 않아 제목처럼 보이지 않을 수 있기 때문이다.
-->

<!--
아래의 'identifier' 문법은 코드 음성에서 ` 사용과 관련된 알려진 문제로 인해 링크 해결 경고를 발생시킨다.

https://github.com/swiftlang/swift-book/issues/71
https://github.com/swiftlang/swift-markdown/issues/93
-->

> 식별자 문법:
>
> *identifier* → *identifier-head* *identifier-characters*_?_ \
> *identifier* → **`` ` ``** *identifier-head* *identifier-characters*_?_ **`` ` ``** \
> *identifier* → *implicit-parameter-name* \
> *identifier* → *property-wrapper-projection* \
> *identifier-list* → *identifier* | *identifier* **`,`** *identifier-list*
>
> *identifier-head* → 대문자 또는 소문자 A부터 Z \
> *identifier-head* → **`_`** \
> *identifier-head* → U+00A8, U+00AA, U+00AD, U+00AF, U+00B2–U+00B5, 또는 U+00B7–U+00BA \
> *identifier-head* → U+00BC–U+00BE, U+00C0–U+00D6, U+00D8–U+00F6, 또는 U+00F8–U+00FF \
> *identifier-head* → U+0100–U+02FF, U+0370–U+167F, U+1681–U+180D, 또는 U+180F–U+1DBF \
> *identifier-head* → U+1E00–U+1FFF \
> *identifier-head* → U+200B–U+200D, U+202A–U+202E, U+203F–U+2040, U+2054, 또는 U+2060–U+206F \
> *identifier-head* → U+2070–U+20CF, U+2100–U+218F, U+2460–U+24FF, 또는 U+2776–U+2793 \
> *identifier-head* → U+2C00–U+2DFF 또는 U+2E80–U+2FFF \
> *identifier-head* → U+3004–U+3007, U+3021–U+302F, U+3031–U+303F, 또는 U+3040–U+D7FF \
> *identifier-head* → U+F900–U+FD3D, U+FD40–U+FDCF, U+FDF0–U+FE1F, 또는 U+FE30–U+FE44 \
> *identifier-head* → U+FE47–U+FFFD \
> *identifier-head* → U+10000–U+1FFFD, U+20000–U+2FFFD, U+30000–U+3FFFD, 또는 U+40000–U+4FFFD \
> *identifier-head* → U+50000–U+5FFFD, U+60000–U+6FFFD, U+70000–U+7FFFD, 또는 U+80000–U+8FFFD \
> *identifier-head* → U+90000–U+9FFFD, U+A0000–U+AFFFD, U+B0000–U+BFFFD, 또는 U+C0000–U+CFFFD \
> *identifier-head* → U+D0000–U+DFFFD 또는 U+E0000–U+EFFFD
>
> *identifier-character* → 숫자 0부터 9 \
> *identifier-character* → U+0300–U+036F, U+1DC0–U+1DFF, U+20D0–U+20FF, 또는 U+FE20–U+FE2F \
> *identifier-character* → *identifier-head* \
> *identifier-characters* → *identifier-character* *identifier-characters*_?_
>
> *implicit-parameter-name* → **`$`** *decimal-digits* \
> *property-wrapper-projection* → **`$`** *identifier-characters*


## 키워드와 구두점

다음 키워드는 예약어로, 앞서 <doc:LexicalStructure#Identifiers>에서 설명한대로 백틱(`)으로 이스케이프하지 않으면 식별자로 사용할 수 없다. `inout`, `var`, `let`을 제외한 키워드는 함수 선언이나 호출에서 파라미터 이름으로 사용할 때 백틱 없이도 사용할 수 있다. 멤버 이름이 키워드와 동일한 경우, 해당 멤버를 참조할 때 백틱으로 이스케이프할 필요가 없다. 단, 멤버 참조와 키워드 사용 간에 모호성이 발생하는 경우는 예외다. 예를 들어, `self`, `Type`, `Protocol`은 명시적 멤버 표현에서 특별한 의미를 가지므로, 이러한 컨텍스트에서는 반드시 백틱으로 이스케이프해야 한다.

<!--
  - test: `keywords-without-backticks`

  ```swifttest
  -> func f(x: Int, in y: Int) {
        print(x+y)
     }
  ```
-->

<!--
  - test: `var-requires-backticks`

  ```swifttest
  -> func g(`var` x: Int) {}
  -> func f(var x: Int) {}
  !$ warning: 'var' in this position is interpreted as an argument label
  !! func f(var x: Int) {}
  !!        ^~~
  !!        `var`
  ```
-->

<!--
  - test: `let-requires-backticks`

  ```swifttest
  -> func g(`let` x: Int) {}
  -> func f(let x: Int) {}
  !$ warning: 'let' in this position is interpreted as an argument label
  !! func f(let x: Int) {}
  !!        ^~~
  !!        `let`
  ```
-->

<!--
  - test: `inout-requires-backticks`

  ```swifttest
  -> func g(`inout` x: Int) {}
  -> func f(inout x: Int) {}
  !$ error: 'inout' before a parameter name is not allowed, place it before the parameter type instead
  !! func f(inout x: Int) {}
  !!        ^~~~~
  !!                 inout
  ```
-->

<!--
  NOTE: 이 언어 키워드와 구두점 목록은
  "swift/include/swift/Parse/Tokens.def" 파일과
  "utils/gyb_syntax_support/Token.py" 파일에서 파생되었으며,
  후자는 TokenKinds.def 파일을 생성한다.

  Swift 5.4 기준, Swift 커밋 2f1987567f5에서 마지막으로 업데이트되었다.
-->

- 선언에 사용되는 키워드:
  `associatedtype`,
  `borrowing`,
  `class`,
  `consuming`,
  `deinit`,
  `enum`,
  `extension`,
  `fileprivate`,
  `func`,
  `import`,
  `init`,
  `inout`,
  `internal`,
  `let`,
  `nonisolated`,
  `open`,
  `operator`,
  `precedencegroup`,
  `private`,
  `protocol`,
  `public`,
  `rethrows`,
  `static`,
  `struct`,
  `subscript`,
  `typealias`,
  그리고 `var`.

<!--
  Token.py에는 'open'이 포함되어 있지 않지만, DeclNodes.py에는 포함되어 있다.
-->

- 구문에 사용되는 키워드:
  `break`,
  `case`,
  `catch`,
  `continue`,
  `default`,
  `defer`,
  `do`,
  `else`,
  `fallthrough`,
  `for`,
  `guard`,
  `if`,
  `in`,
  `repeat`,
  `return`,
  `switch`,
  `throw`,
  `where`,
  그리고 `while`.
- 표현식과 타입에 사용되는 키워드:
  `Any`,
  `as`,
  `await`,
  `catch`,
  `false`,
  `is`,
  `nil`,
  `rethrows`,
  `self`,
  `Self`,
  `super`,
  `throw`,
  `throws`,
  `true`,
  그리고 `try`.
- 패턴에 사용되는 키워드:
  `_`.
- 숫자 기호(`#`)로 시작하는 키워드:
  `#available`,
  `#colorLiteral`,
  `#else`,
  `#elseif`,
  `#endif`,
  `#fileLiteral`,
  `#if`,
  `#imageLiteral`,
  `#keyPath`,
  `#selector`,
  `#sourceLocation`,
  `#unavailable`.

> 참고:
> Swift 5.9 이전에는 다음 키워드가 예약어였다:
> `#column`,
> `#dsohandle`,
> `#error`,
> `#fileID`,
> `#filePath`,
> `#file`,
> `#function`,
> `#line`,
> 그리고 `#warning`.
> 이제 이들은 Swift 표준 라이브러리의 매크로로 구현되었다:
> [`column`](https://developer.apple.com/documentation/swift/column()),
> [`dsohandle`](https://developer.apple.com/documentation/swift/dsohandle()),
> [`error(_:)`](https://developer.apple.com/documentation/swift/error(_:)),
> [`fileID`](https://developer.apple.com/documentation/swift/fileID()),
> [`filePath`](https://developer.apple.com/documentation/swift/filePath()),
> [`file`](https://developer.apple.com/documentation/swift/file()),
> [`function`](https://developer.apple.com/documentation/swift/function()),
> [`line`](https://developer.apple.com/documentation/swift/line()),
> 그리고 [`warning(_:)`](https://developer.apple.com/documentation/swift/warning(_:)).

<!--
  Token.py에는 #assert가 포함되어 있으며,
  이는 실험적 기능의 일부로 보인다.
  pound_assert_disabled 진단의 오류 메시지를 기반으로 추정된다:
-->


#assert는 현재 비활성화된 실험적 기능이다

-->

<!--
  Token.py에 포함된 #fileID는
  향후 -enable-experimental-concise-pound-file와 관련된 기능의 일부로 보인다
  (Swift 커밋 0e569f5d9e66 참조).
-->

<!--
  Token.py에 포함된 'yield' 키워드는
  메모리 소유권과 관련된 향후 기능과 연관되어 있다.
-->

- 특정 문맥에서 예약된 키워드:
  `associativity`,
  `async`,
  `convenience`,
  `didSet`,
  `dynamic`,
  `final`,
  `get`,
  `indirect`,
  `infix`,
  `lazy`,
  `left`,
  `mutating`,
  `none`,
  `nonmutating`,
  `optional`,
  `override`,
  `package`,
  `postfix`,
  `precedence`,
  `prefix`,
  `Protocol`,
  `required`,
  `right`,
  `set`,
  `some`,
  `Type`,
  `unowned`,
  `weak`,
  그리고 `willSet`.
  이 키워드들은 문법에서 정의된 특정 문맥 외부에서는 식별자로 사용할 수 있다.

<!--
  참고: 위의 문맥 의존적 키워드 목록은
  "swift/include/swift/AST/Attr.def" 파일에서 가져왔다.
  이 파일에서 CONTEXTUAL_SIMPLE_DECL_ATTR로 표시된 키워드들이다.
  하지만 모든 문맥 의존적 키워드가 여기에 포함되지는 않는다.
-->

다음 토큰들은 구두점으로 예약되어 있으며
커스텀 연산자로 사용할 수 없다:
`(`, `)`, `{`, `}`, `[`, `]`,
`.`, `,`, `:`, `;`, `=`, `@`, `#`,
`&` (접두사 연산자로 사용할 때), `->`, `` ` ``,
`?`, 그리고 `!` (접미사 연산자로 사용할 때).


## 리터럴

*리터럴*은 숫자나 문자열과 같은 타입의 값을 소스 코드에서 직접 표현한 것이다.

다음은 리터럴의 예제이다:

```swift
42               // 정수 리터럴
3.14159          // 부동소수점 리터럴
"Hello, world!"  // 문자열 리터럴
/Hello, .*/      // 정규 표현식 리터럴
true             // 불리언 리터럴
```

<!--
  - test: `basic-literals`

  ```swifttest
  >> let r0 =
  -> 42               // Integer literal
  >> let r1 =
  -> 3.14159          // Floating-point literal
  >> let r2 =
  -> "Hello, world!"  // String literal
  >> let r4 =
  -> /Hello, .*/      // Regular expression literal
  >> let r3 =
  -> true             // Boolean literal
  >> for x in [r0, r1, r2, r3] as [Any] { print(type(of: x)) }
  << Int
  << Double
  << String
  << Bool
  ```
-->

<!--
  Refactor the above if possible to avoid using bare expressions.
  Tracking bug is <rdar://problem/35301593>
-->

리터럴 자체는 타입을 가지지 않는다. 대신, 리터럴은 무한한 정밀도로 파싱되며 Swift의 타입 추론이 리터럴에 적합한 타입을 추론한다. 예를 들어, `let x: Int8 = 42` 선언에서 Swift는 명시적 타입 어노테이션(`: Int8`)을 사용해 정수 리터럴 `42`의 타입이 `Int8`임을 추론한다. 적절한 타입 정보가 없을 경우, Swift는 리터럴의 타입을 Swift 표준 라이브러리에 정의된 기본 리터럴 타입 중 하나로 추론한다. 아래 표에서 기본 리터럴 타입을 확인할 수 있다. 리터럴 값에 타입 어노테이션을 지정할 때, 어노테이션의 타입은 해당 리터럴 값으로부터 인스턴스화할 수 있는 타입이어야 한다. 즉, 타입은 아래 표에 나열된 Swift 표준 라이브러리 프로토콜을 준수해야 한다.

| 리터럴 | 기본 타입 | 프로토콜 |
| ------- | ------------ | -------- |
| 정수 | `Int` | `ExpressibleByIntegerLiteral` |
| 부동소수점 | `Double` | `ExpressibleByFloatLiteral` |
| 문자열 | `String` | `ExpressibleByStringLiteral`, 단일 유니코드 스칼라만 포함된 문자열 리터럴의 경우 `ExpressibleByUnicodeScalarLiteral`, 단일 확장 그래핌 클러스터만 포함된 문자열 리터럴의 경우 `ExpressibleByExtendedGraphemeClusterLiteral` |
| 정규 표현식 | `Regex` | 없음 |
| 불리언 | `Bool` | `ExpressibleByBooleanLiteral` |

예를 들어, `let str = "Hello, world"` 선언에서 문자열 리터럴 `"Hello, world"`의 기본 추론 타입은 `String`이다. 또한, `Int8`은 `ExpressibleByIntegerLiteral` 프로토콜을 준수하므로, `let x: Int8 = 42` 선언에서 정수 리터럴 `42`의 타입 어노테이션으로 사용할 수 있다.

<!--
  The list of ExpressibleBy... protocols above also appears in Declarations_EnumerationsWithRawCaseValues.
  ExpressibleByNilLiteral is left out of the list because conformance to it isn't recommended.
  There is no protocol for regex literal in the list because the stdlib intentionally omits that.
-->

> 리터럴 문법:
>
> *literal* → *numeric-literal* | *string-literal* | *regular-expression-literal* | *boolean-literal* | *nil-literal*
>
> *numeric-literal* → **`-`**_?_ *integer-literal* | **`-`**_?_ *floating-point-literal* \
> *boolean-literal* → **`true`** | **`false`** \
> *nil-literal* → **`nil`**


### 정수 리터럴

*정수 리터럴*은 정밀도가 명시되지 않은 정수 값을 나타낸다. 기본적으로 정수 리터럴은 10진수로 표현되지만, 접두사를 사용해 다른 진법을 지정할 수 있다. 바이너리 리터럴은 `0b`로 시작하고, 8진수 리터럴은 `0o`로 시작하며, 16진수 리터럴은 `0x`로 시작한다.

10진수 리터럴은 `0`부터 `9`까지의 숫자를 포함한다. 바이너리 리터럴은 `0`과 `1`을 포함하고, 8진수 리터럴은 `0`부터 `7`까지의 숫자를 포함한다. 16진수 리터럴은 `0`부터 `9`까지의 숫자와 대소문자 `A`부터 `F`까지의 문자를 포함한다.

음의 정수 리터럴은 정수 리터럴 앞에 마이너스 기호(`-`)를 붙여 표현한다. 예를 들어 `-42`와 같다.

가독성을 위해 숫자 사이에 언더스코어(`_`)를 사용할 수 있지만, 이는 무시되므로 리터럴의 값에 영향을 미치지 않는다. 정수 리터럴은 앞에 0(`0`)으로 시작할 수 있지만, 이 역시 무시되며 진법이나 값에 영향을 주지 않는다.

별도로 지정하지 않으면 정수 리터럴의 기본 타입은 Swift 표준 라이브러리의 `Int` 타입으로 추론된다. Swift 표준 라이브러리는 다양한 크기의 부호 있는 정수와 부호 없는 정수 타입도 정의하고 있다. 이에 대한 자세한 내용은 <doc:TheBasics#Integers>에서 확인할 수 있다.

<!--
  TR: 언더스코어는 숫자 사이에만 허용된다고 가정한다.
  리터럴 끝에 언더스코어를 허용해야 하는 이유가 있는가?
  Java와 Ruby는 모두 언더스코어가 숫자 사이에 있어야 한다고 규정한다.
  또한, 5__000과 같이 연속된 언더스코어를 허용하는가?
  (REPL은 swift-1.21부터 이를 지원하지만, 이상해 보인다.)
-->

<!--
  NOTE: [Contributor 7746]의 댓글을 반영해 문법을 업데이트했다.
  <rdar://problem/15181997> 컴파일러에게 음의 정수 리터럴 개념을 가르치기.
  이는 문법적 관점에서 매우 이상하게 느껴진다.
  업데이트: 이는 파서 해킹이며, 렉서 해킹이 아니다. 따라서,
  [Contributor 2562]의 주장과 달리 정수 리터럴의 문법에 포함되지 않는다.
  (Doug가 2014년 4월 2일에 확인함.)
-->

> 정수 리터럴 문법:
>
> *integer-literal* → *binary-literal* \
> *integer-literal* → *octal-literal* \
> *integer-literal* → *decimal-literal* \
> *integer-literal* → *hexadecimal-literal*
>
> *binary-literal* → **`0b`** *binary-digit* *binary-literal-characters*_?_ \
> *binary-digit* → 0 또는 1 \
> *binary-literal-character* → *binary-digit* | **`_`** \
> *binary-literal-characters* → *binary-literal-character* *binary-literal-characters*_?_
>
> *octal-literal* → **`0o`** *octal-digit* *octal-literal-characters*_?_ \
> *octal-digit* → 0부터 7까지의 숫자 \
> *octal-literal-character* → *octal-digit* | **`_`** \
> *octal-literal-characters* → *octal-literal-character* *octal-literal-characters*_?_
>
> *decimal-literal* → *decimal-digit* *decimal-literal-characters*_?_ \
> *decimal-digit* → 0부터 9까지의 숫자 \
> *decimal-digits* → *decimal-digit* *decimal-digits*_?_ \
> *decimal-literal-character* → *decimal-digit* | **`_`** \
> *decimal-literal-characters* → *decimal-literal-character* *decimal-literal-characters*_?_
>
> *hexadecimal-literal* → **`0x`** *hexadecimal-digit* *hexadecimal-literal-characters*_?_ \
> *hexadecimal-digit* → 0부터 9까지의 숫자, a부터 f, 또는 A부터 F \
> *hexadecimal-literal-character* → *hexadecimal-digit* | **`_`** \
> *hexadecimal-literal-characters* → *hexadecimal-literal-character* *hexadecimal-literal-characters*_?_


### 부동소수점 리터럴

*부동소수점 리터럴*은 정밀도가 명시되지 않은 부동소수점 값을 나타낸다. 기본적으로 부동소수점 리터럴은 10진수로 표현되지만, `0x` 접두사를 사용해 16진수로도 표현할 수 있다.

10진수 부동소수점 리터럴은 일련의 10진수 숫자 뒤에 소수 부분, 지수 부분, 또는 둘 다가 올 수 있다. 소수 부분은 소수점(`.`) 뒤에 일련의 10진수 숫자로 구성된다. 지수 부분은 대소문자 `e` 접두사와 일련의 10진수 숫자로 구성되며, `e` 앞의 값에 10의 몇 제곱을 곱할지를 나타낸다. 예를 들어, `1.25e2`는 1.25 x 10²를 의미하며, 이는 `125.0`으로 계산된다. 마찬가지로, `1.25e-2`는 1.25 x 10⁻²를 의미하며, 이는 `0.0125`로 계산된다.

16진수 부동소수점 리터럴은 `0x` 접두사 뒤에 선택적인 16진수 소수 부분과 16진수 지수 부분으로 구성된다. 16진수 소수 부분은 소수점 뒤에 일련의 16진수 숫자로 구성된다. 지수 부분은 대소문자 `p` 접두사와 일련의 10진수 숫자로 구성되며, `p` 앞의 값에 2의 몇 제곱을 곱할지를 나타낸다. 예를 들어, `0xFp2`는 15 x 2²를 의미하며, 이는 `60`으로 계산된다. 마찬가지로, `0xFp-2`는 15 x 2⁻²를 의미하며, 이는 `3.75`로 계산된다.

음수 부동소수점 리터럴은 부동소수점 리터럴 앞에 마이너스 기호(`-`)를 붙여 표현한다. 예를 들어, `-42.5`와 같이 쓸 수 있다.

가독성을 위해 숫자 사이에 언더스코어(`_`)를 사용할 수 있지만, 이는 무시되므로 리터럴의 값에 영향을 미치지 않는다. 부동소수점 리터럴은 앞에 0(`0`)으로 시작할 수 있지만, 이 역시 무시되며 리터럴의 진수나 값에 영향을 주지 않는다.

별도로 명시하지 않는 한, 부동소수점 리터럴의 기본 타입은 Swift 표준 라이브러리의 `Double` 타입이다. 이는 64비트 부동소수점 숫자를 나타낸다. Swift 표준 라이브러리는 32비트 부동소수점 숫자를 나타내는 `Float` 타입도 정의한다.

> 부동소수점 리터럴 문법:
>
> *부동소수점 리터럴* → *10진수 리터럴* *10진수 소수 부분*_?_ *10진수 지수 부분*_?_ \
> *부동소수점 리터럴* → *16진수 리터럴* *16진수 소수 부분*_?_ *16진수 지수 부분*
>
> *10진수 소수 부분* → **`.`** *10진수 리터럴* \
> *10진수 지수 부분* → *부동소수점 e* *부호*_?_ *10진수 리터럴*
>
> *16진수 소수 부분* → **`.`** *16진수 숫자* *16진수 리터럴 문자*_?_ \
> *16진수 지수 부분* → *부동소수점 p* *부호*_?_ *10진수 리터럴*
>
> *부동소수점 e* → **`e`** | **`E`** \
> *부동소수점 p* → **`p`** | **`P`** \
> *부호* → **`+`** | **`-`**


### 문자열 리터럴

문자열 리터럴은 따옴표로 둘러싸인 문자 시퀀스다.  
한 줄 문자열 리터럴은 큰따옴표로 둘러싸이며 다음과 같은 형태를 가진다:

```swift
"<#characters#>"
```

문자열 리터럴은 이스케이프되지 않은 큰따옴표(`"`),  
이스케이프되지 않은 백슬래시(`\`),  
캐리지 리턴, 또는 라인 피드를 포함할 수 없다.

여러 줄 문자열 리터럴은 세 개의 큰따옴표로 둘러싸이며  
다음과 같은 형태를 가진다:

```swift
"""
<#characters#>
"""
```

한 줄 문자열 리터럴과 달리,  
여러 줄 문자열 리터럴은 이스케이프되지 않은 큰따옴표(`"`),  
캐리지 리턴, 라인 피드를 포함할 수 있다.  
단, 연속된 세 개의 큰따옴표는 포함할 수 없다.

여러 줄 문자열 리터럴을 시작하는 `"""` 뒤의 줄바꿈은  
문자열의 일부가 아니다.  
리터럴을 끝내는 `"""` 앞의 줄바꿈도 마찬가지다.  
줄바꿈으로 시작하거나 끝나는 여러 줄 문자열 리터럴을 만들려면,  
첫 번째 또는 마지막 줄을 비워두면 된다.

여러 줄 문자열 리터럴은 공백과 탭을 조합해 들여쓸 수 있다.  
이 들여쓰기는 문자열에 포함되지 않는다.  
리터럴을 끝내는 `"""`가 들여쓰기를 결정한다.  
리터럴 내의 모든 비어 있지 않은 줄은  
닫는 `"""` 앞에 있는 들여쓰기와 정확히 일치해야 한다.  
탭과 공백 간 변환은 없다.  
들여쓰기 뒤에 추가 공백이나 탭을 넣을 수 있으며,  
이 공백과 탭은 문자열에 포함된다.

여러 줄 문자열 리터럴의 줄바꿈은  
라인 피드 문자로 정규화된다.  
소스 파일에 캐리지 리턴과 라인 피드가 혼합되어 있어도,  
문자열 내 모든 줄바꿈은 동일하다.

여러 줄 문자열 리터럴에서  
줄 끝에 백슬래시(`\`)를 쓰면  
해당 줄바꿈이 문자열에서 제외된다.  
백슬래시와 줄바꿈 사이의 공백도 제외된다.  
이 구문을 사용해 소스 코드에서 여러 줄 문자열 리터럴을  
하드 래핑할 수 있으며,  
결과 문자열의 값은 변하지 않는다.

특수 문자는 이스케이프 시퀀스를 사용해  
한 줄 및 여러 줄 문자열 리터럴에 포함할 수 있다:

- 널 문자 (`\0`)
- 백슬래시 (`\\`)
- 수평 탭 (`\t`)
- 라인 피드 (`\n`)
- 캐리지 리턴 (`\r`)
- 큰따옴표 (`\"`)
- 작은따옴표 (`\'`)
- 유니코드 스칼라 (`\u{`*n*`}`),  
  여기서 *n*은 1에서 8자리의 16진수다.

<!--
  \n과 \r의 동작은 C와 다르다.  
  이 이스케이프 시퀀스의 의미를 정확히 명시한다.  
  C에서는 플랫폼에 따라 다르며,  
  텍스트 모드에서 \n은 플랫폼의 줄 구분자로 매핑된다.  
  이는 CR, LF, 또는 CRLF일 수 있다.
-->

표현식의 값을 문자열 리터럴에 삽입하려면  
백슬래시(`\`) 뒤에 괄호로 둘러싼 표현식을 넣는다.  
삽입된 표현식은 문자열 리터럴을 포함할 수 있지만,  
이스케이프되지 않은 백슬래시,  
캐리지 리턴, 또는 라인 피드는 포함할 수 없다.

예를 들어, 다음 문자열 리터럴은 모두 동일한 값을 가진다:

```swift
"1 2 3"
"1 2 \("3")"
"1 2 \(3)"
"1 2 \(1 + 2)"
let x = 3; "1 2 \(x)"
```

<!--
  - test: `string-literals`

  ```swifttest
  >> let r0 =
  -> "1 2 3"
  >> let r1 =
  -> "1 2 \("3")"
  >> assert(r0 == r1)
  >> let r2 =
  -> "1 2 \(3)"
  >> assert(r0 == r2)
  >> let r3 =
  -> "1 2 \(1 + 2)"
  >> assert(r0 == r3)
  -> let x = 3; "1 2 \(x)"
  >> assert(r0 == "1 2 \(x)")
  !$ warning: string literal is unused
  !! let x = 3; "1 2 \(x)"
  !!            ^~~~~~~~~~
  ```
-->

<!--
  위 예제를 가능한 한 표현식 없이 리팩토링한다.  
  추적 버그는 <rdar://problem/35301593>
-->

확장 구분자로 둘러싼 문자열은  
따옴표와 하나 이상의 숫자 기호(`#`)로 둘러싸인 문자 시퀀스다.  
확장 구분자로 둘러싼 문자열은 다음과 같은 형태를 가진다:

```swift
#"<#characters#>"#

#"""
<#characters#>
"""#
```

확장 구분자로 둘러싼 문자열의 특수 문자는  
일반 문자로 처리된다.  
확장 구분자를 사용해 문자열 보간을 생성하거나,  
이스케이프 시퀀스를 시작하거나,  
문자열을 종료하는 등의 특수 효과를 가진 문자를 포함할 수 있다.

다음 예제는 동일한 문자열 값을 생성하는  
문자열 리터럴과 확장 구분자로 둘러싼 문자열을 보여준다:

```swift
let string = #"\(x) \ " \u{2603}"#
let escaped = "\\(x) \\ \" \\u{2603}"
print(string)
// Prints "\(x) \ " \u{2603}"
print(string == escaped)
// Prints "true"
```

<!--
  - test: `extended-string-delimiters`

  ```swifttest
  -> let string = #"\(x) \ " \u{2603}"#
  -> let escaped = "\\(x) \\ \" \\u{2603}"
  -> print(string)
  <- \(x) \ " \u{2603}
  -> print(string == escaped)
  <- true
  ```
-->

확장 구분자를 형성하기 위해  
하나 이상의 숫자 기호를 사용할 때,  
숫자 기호 사이에 공백을 넣지 않는다:

<!--
  - test: `extended-string-delimiters`

  ```swifttest
  -> print(###"Line 1\###nLine 2"###) // OK
  << Line 1
  << Line 2
  ```
-->

```swift
print(###"Line 1\###nLine 2"###) // OK
print(# # #"Line 1\# # #nLine 2"# # #) // Error
```

<!--
  - test: `extended-string-delimiters-err`

  ```swifttest
  -> print(###"Line 1\###nLine 2"###) // OK
  -> print(# # #"Line 1\# # #nLine 2"# # #) // Error
  !$ error: expected expression in list of expressions
  !! print(# # #"Line 1\# # #nLine 2"# # #) // Error
  !! ^
  !$ error: invalid escape sequence in literal
  !! print(# # #"Line 1\# # #nLine 2"# # #) // Error
  !! ^
  ```
-->

확장 구분자를 사용해 만든 여러 줄 문자열 리터럴은  
일반 여러 줄 문자열 리터럴과 동일한 들여쓰기 요구사항을 가진다.

문자열 리터럴의 기본 추론 타입은 `String`이다.  
`String` 타입에 대한 자세한 내용은  
<doc:StringsAndCharacters>와  
[`String`](https://developer.apple.com/documentation/swift/string)을 참고한다.

`+` 연산자로 연결된 문자열 리터럴은  
컴파일 시점에 연결된다.  
예를 들어, 아래 예제의 `textA`와 `textB` 값은 동일하며,  
런타임에 연결 작업이 수행되지 않는다.

```swift
let textA = "Hello " + "world"
let textB = "Hello world"
```

<!--
  - test: `concatenated-strings`

  ```swifttest
  -> let textA = "Hello " + "world"
  -> let textB = "Hello world"
  ```
-->

> 문자열 리터럴 문법:
>
> *string-literal* → *static-string-literal* | *interpolated-string-literal*
>
> *string-literal-opening-delimiter* → *extended-string-literal-delimiter*_?_ **`"`** \
> *string-literal-closing-delimiter* → **`"`** *extended-string-literal-delimiter*_?_
>
> *static-string-literal* → *string-literal-opening-delimiter* *quoted-text*_?_ *string-literal-closing-delimiter* \
> *static-string-literal* → *multiline-string-literal-opening-delimiter* *multiline-quoted-text*_?_ *multiline-string-literal-closing-delimiter*
>
> *multiline-string-literal-opening-delimiter* → *extended-string-literal-delimiter*_?_ **`"""`** \
> *multiline-string-literal-closing-delimiter* → **`"""`** *extended-string-literal-delimiter*_?_ \
> *extended-string-literal-delimiter* → **`#`** *extended-string-literal-delimiter*_?_
>
> *quoted-text* → *quoted-text-item* *quoted-text*_?_ \
> *quoted-text-item* → *escaped-character* \
> *quoted-text-item* → Any Unicode scalar value except  **`"`**,  **`\`**, U+000A, or U+000D
>
> *multiline-quoted-text* → *multiline-quoted-text-item* *multiline-quoted-text*_?_ \
> *multiline-quoted-text-item* → *escaped-character* \
> *multiline-quoted-text-item* → Any Unicode scalar value except  **`\`** \
> *multiline-quoted-text-item* → *escaped-newline*
>
> *interpolated-string-literal* → *string-literal-opening-delimiter* *interpolated-text*_?_ *string-literal-closing-delimiter* \
> *interpolated-string-literal* → *multiline-string-literal-opening-delimiter* *multiline-interpolated-text*_?_ *multiline-string-literal-closing-delimiter*
>
> *interpolated-text* → *interpolated-text-item* *interpolated-text*_?_ \
> *interpolated-text-item* → **`\(`** *expression* **`)`** | *quoted-text-item*
>
> *multiline-interpolated-text* → *multiline-interpolated-text-item* *multiline-interpolated-text*_?_ \
> *multiline-interpolated-text-item* → **`\(`** *expression* **`)`** | *multiline-quoted-text-item*
>
> *escape-sequence* → **`\`** *extended-string-literal-delimiter* \
> *escaped-character* → *escape-sequence* **`0`** | *escape-sequence* **`\`** | *escape-sequence* **`t`** | *escape-sequence* **`n`** | *escape-sequence* **`r`** | *escape-sequence* **`"`** | *escape-sequence* **`'`** \
> *escaped-character* → *escape-sequence* **`u`** **`{`** *unicode-scalar-digits* **`}`** \
> *unicode-scalar-digits* → Between one and eight hexadecimal digits
>
> *escaped-newline* → *escape-sequence* *inline-spaces*_?_ *line-break*

<!--
  인용된 텍스트는 이스케이프된 문자 시퀀스로 해석되며,  
  quoted-text 규칙을 통해 반복이 허용된다.  
  quoted-text/escaped-character 규칙에서도 반복을 허용할 필요는 없다.
-->

<!--
  이제 작은따옴표가 사라졌으므로 문자 리터럴이 없다.  
  언젠가 다시 도입할 수 있으므로,  
  이전 문자 리터럴 문법은 다음과 같다:

  textual-literal -> character-literal | string-literal

  character-literal -> ``'`` quoted-character ``'``
  quoted-character -> escaped-character
  quoted-character -> Any Unicode scalar value except ``'``, ``\``, U+000A, or U+000D
-->


### 정규 표현식 리터럴

정규 표현식 리터럴은 슬래시(`/`)로 둘러싸인 일련의 문자로 다음과 같은 형태를 가진다:

```swift
/<#정규 표현식#>/
```

정규 표현식 리터럴은 탭이나 공백으로 시작할 수 없으며, 이스케이프 되지 않은 슬래시(`/`), 캐리지 리턴, 라인 피드를 포함할 수 없다.

정규 표현식 리터럴 내에서 백슬래시는 단순한 이스케이프 문자가 아니라 정규 표현식의 일부로 해석된다. 이는 뒤에 오는 특수 문자를 문자 그대로 해석하거나, 특수하지 않은 문자를 특수한 방식으로 해석하도록 지시한다. 예를 들어, `/\(/`는 단일 왼쪽 괄호와 일치하고, `/\d/`는 단일 숫자와 일치한다.

확장 구분자로 둘러싸인 정규 표현식 리터럴은 슬래시(`/`)와 하나 이상의 숫자 기호(`#`)로 구성된 균형 잡힌 집합으로 둘러싸인 일련의 문자다. 확장 구분자를 사용한 정규 표현식 리터럴은 다음과 같은 형태를 가진다:

```swift
#/<#정규 표현식#>/#

#/
<#정규 표현식#>
/#
```

확장 구분자를 사용한 정규 표현식 리터럴은 이스케이프 되지 않은 공백이나 탭으로 시작할 수 있으며, 이스케이프 되지 않은 슬래시(`/`)를 포함할 수 있고, 여러 줄에 걸쳐 작성할 수 있다. 여러 줄로 된 정규 표현식 리터럴의 경우, 시작 구분자는 줄 끝에 위치해야 하며, 종료 구분자는 별도의 줄에 위치해야 한다. 여러 줄 정규 표현식 리터럴 내에서는 확장 정규 표현식 구문이 기본적으로 활성화된다. 특히, 공백은 무시되고 주석이 허용된다.

확장 구분자를 사용해 정규 표현식 리터럴을 만들 때, 숫자 기호 사이에 공백을 넣지 않도록 주의한다:

```swift
let regex1 = ##/abc/##       // OK
let regex2 = # #/abc/# #     // Error
```

빈 정규 표현식 리터럴을 만들려면 반드시 확장 구분자 구문을 사용해야 한다.

> 정규 표현식 리터럴의 문법:
>
> *정규-표현식-리터럴* → *정규-표현식-리터럴-시작-구분자* *정규-표현식* *정규-표현식-리터럴-종료-구분자* \
> *정규-표현식* → 모든 정규 표현식
>
> *정규-표현식-리터럴-시작-구분자* → *확장-정규-표현식-리터럴-구분자*_?_ **`/`** \
> *정규-표현식-리터럴-종료-구분자* → **`/`** *확장-정규-표현식-리터럴-구분자*_?_
>
> *확장-정규-표현식-리터럴-구분자* → **`#`** *확장-정규-표현식-리터럴-구분자*_?_


## 연산자

Swift 표준 라이브러리는 다양한 연산자를 제공한다. 이 중 많은 연산자는 <doc:BasicOperators>와 <doc:AdvancedOperators>에서 다룬다. 이 섹션에서는 커스텀 연산자를 정의할 때 사용할 수 있는 문자에 대해 설명한다.

커스텀 연산자는 `/`, `=`, `-`, `+`, `!`, `*`, `%`, `<`, `>`, `&`, `|`, `^`, `?`, `~`와 같은 ASCII 문자로 시작할 수 있다. 또는 아래 문법에 정의된 유니코드 문자로 시작할 수도 있다. 이 유니코드 문자들은 *수학 연산자*, *기타 기호*, *딩벳* 등의 유니코드 블록에 포함된 문자들이다. 첫 번째 문자 이후에는 결합 유니코드 문자도 허용된다.

점(`.`)으로 시작하는 커스텀 연산자를 정의할 수도 있다. 이러한 연산자는 추가 점을 포함할 수 있다. 예를 들어, `.+.`은 단일 연산자로 처리된다. 만약 연산자가 점으로 시작하지 않는다면, 다른 곳에 점을 포함할 수 없다. 예를 들어, `+.+`는 `+` 연산자 뒤에 `.+` 연산자가 오는 것으로 처리된다.

물음표(`?`)를 포함하는 커스텀 연산자를 정의할 수 있지만, 단독 물음표 문자로만 구성된 연산자는 정의할 수 없다. 또한, 느낌표(`!`)를 포함할 수는 있지만, 후위 연산자는 물음표나 느낌표로 시작할 수 없다.

> 참고: `=`, `->`, `//`, `/*`, `*/`, `.`, 접두사 연산자 `<`, `&`, `?`, 중위 연산자 `?`, 후위 연산자 `>`, `!`, `?`와 같은 토큰은 예약어다. 이러한 토큰은 오버로드할 수 없으며, 커스텀 연산자로 사용할 수도 없다.

연산자 주변의 공백은 해당 연산자가 접두사 연산자, 후위 연산자, 중위 연산자 중 어떤 것으로 사용될지를 결정한다. 이 동작은 다음과 같은 규칙을 따른다:

- 연산자 양쪽에 공백이 있거나 양쪽 모두 공백이 없으면 중위 연산자로 처리된다. 예를 들어, `a+++b`와 `a +++ b`에서 `+++` 연산자는 중위 연산자로 처리된다.
- 연산자 왼쪽에만 공백이 있으면 접두사 단항 연산자로 처리된다. 예를 들어, `a +++b`에서 `+++` 연산자는 접두사 단항 연산자로 처리된다.
- 연산자 오른쪽에만 공백이 있으면 후위 단항 연산자로 처리된다. 예를 들어, `a+++ b`에서 `+++` 연산자는 후위 단항 연산자로 처리된다.
- 연산자 왼쪽에 공백이 없고 바로 뒤에 점(`.`)이 오면 후위 단항 연산자로 처리된다. 예를 들어, `a+++.b`에서 `+++` 연산자는 후위 단항 연산자로 처리된다(`a+++ .b`가 아니라 `a +++ .b`로 처리된다).

이 규칙을 적용할 때, 연산자 앞에 오는 `(`, `[`, `{` 문자와 연산자 뒤에 오는 `)`, `]`, `}` 문자, 그리고 `,`, `;`, `:` 문자도 공백으로 간주한다.

`!`나 `?`와 같은 미리 정의된 연산자 왼쪽에 공백이 없으면, 오른쪽에 공백이 있더라도 후위 연산자로 처리된다. 옵셔널 체이닝 연산자로 `?`를 사용하려면 왼쪽에 공백이 없어야 한다. 삼항 조건 연산자(`?` `:`)로 사용하려면 양쪽에 공백이 있어야 한다.

중위 연산자의 인수 중 하나가 정규 표현식 리터럴이면, 연산자 양쪽에 공백이 있어야 한다.

특정 구조에서 `<`나 `>`로 시작하는 연산자는 두 개 이상의 토큰으로 분리될 수 있다. 나머지 부분도 동일한 방식으로 처리되며 다시 분리될 수 있다. 결과적으로 `Dictionary<String, Array<Int>>`와 같은 구조에서 닫는 `>` 문자를 명확히 구분하기 위해 공백을 추가할 필요가 없다. 이 예제에서 닫는 `>` 문자는 단일 토큰으로 처리되지 않으며, 비트 시프트 `>>` 연산자로 오해되지 않는다.

새로운 커스텀 연산자를 정의하는 방법은 <doc:AdvancedOperators#Custom-Operators>와 <doc:Declarations#Operator-Declaration>을 참고한다. 기존 연산자를 오버로드하는 방법은 <doc:AdvancedOperators#Operator-Methods>를 참고한다.

> 연산자 문법:
>
> *operator* → *operator-head* *operator-characters*_?_ \
> *operator* → *dot-operator-head* *dot-operator-characters*
>
> *operator-head* → **`/`** | **`=`** | **`-`** | **`+`** | **`!`** | **`*`** | **`%`** | **`<`** | **`>`** | **`&`** | **`|`** | **`^`** | **`~`** | **`?`** \
> *operator-head* → U+00A1–U+00A7 \
> *operator-head* → U+00A9 or U+00AB \
> *operator-head* → U+00AC or U+00AE \
> *operator-head* → U+00B0–U+00B1 \
> *operator-head* → U+00B6, U+00BB, U+00BF, U+00D7, or U+00F7 \
> *operator-head* → U+2016–U+2017 \
> *operator-head* → U+2020–U+2027 \
> *operator-head* → U+2030–U+203E \
> *operator-head* → U+2041–U+2053 \
> *operator-head* → U+2055–U+205E \
> *operator-head* → U+2190–U+23FF \
> *operator-head* → U+2500–U+2775 \
> *operator-head* → U+2794–U+2BFF \
> *operator-head* → U+2E00–U+2E7F \
> *operator-head* → U+3001–U+3003 \
> *operator-head* → U+3008–U+3020 \
> *operator-head* → U+3030
>
> *operator-character* → *operator-head* \
> *operator-character* → U+0300–U+036F \
> *operator-character* → U+1DC0–U+1DFF \
> *operator-character* → U+20D0–U+20FF \
> *operator-character* → U+FE00–U+FE0F \
> *operator-character* → U+FE20–U+FE2F \
> *operator-character* → U+E0100–U+E01EF \
> *operator-characters* → *operator-character* *operator-characters*_?_
>
> *dot-operator-head* → **`.`** \
> *dot-operator-character* → **`.`** | *operator-character* \
> *dot-operator-characters* → *dot-operator-character* *dot-operator-characters*_?_
>
> *infix-operator* → *operator* \
> *prefix-operator* → *operator* \
> *postfix-operator* → *operator*


