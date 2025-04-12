# 고급 연산자

커스텀 연산자를 정의하고, 비트 연산을 수행하며, 빌더 구문을 사용하는 방법을 알아본다.

<doc:BasicOperators>에서 설명한 기본 연산자 외에도, Swift는 더 복잡한 값 조작을 수행하는 여러 고급 연산자를 제공한다. 이 연산자들은 C와 Objective-C에서 익숙할 만한 모든 비트 연산자와 비트 시프트 연산자를 포함한다.

C 언어의 산술 연산자와 달리, Swift의 산술 연산자는 기본적으로 오버플로우를 허용하지 않는다. 오버플로우가 발생하면 이를 감지하고 오류로 보고한다. 오버플로우 동작을 허용하려면, Swift에서 기본적으로 오버플로우를 허용하는 두 번째 산술 연산자 집합을 사용하면 된다. 예를 들어, 오버플로우 덧셈 연산자(`&+`)가 있다. 이러한 모든 오버플로우 연산자는 앰퍼샌드(`&`)로 시작한다.

커스텀 구조체, 클래스, 열거형을 정의할 때, 이러한 타입에 대해 표준 Swift 연산자의 커스텀 구현을 제공하는 것이 유용할 수 있다. Swift는 이러한 연산자의 맞춤형 구현을 쉽게 제공할 수 있도록 하며, 생성한 각 타입에 대해 연산자의 동작을 정확히 결정할 수 있게 해준다.

미리 정의된 연산자에만 제한되지 않는다. Swift는 커스텀 중위(infix), 전위(prefix), 후위(postfix), 할당(assignment) 연산자를 정의할 수 있는 자유를 제공한다. 이때 커스텀 우선순위와 결합성 값을 지정할 수 있다. 이러한 연산자는 미리 정의된 연산자와 마찬가지로 코드에서 사용하고 채택할 수 있으며, 기존 타입을 확장하여 정의한 커스텀 연산자를 지원하도록 할 수도 있다.


## 비트 연산자

**비트 연산자**는 데이터 구조 내의 개별 비트를 직접 조작할 수 있게 해준다. 이 연산자는 그래픽 프로그래밍이나 디바이스 드라이버 개발과 같은 저수준 프로그래밍에서 자주 사용된다. 또한 커스텀 프로토콜을 통한 통신을 위해 데이터를 인코딩하거나 디코딩할 때와 같이 외부 소스로부터의 원시 데이터를 다룰 때도 유용하게 활용할 수 있다.

Swift는 C 언어에서 사용되는 모든 비트 연산자를 지원한다. 아래에서 이들 연산자에 대해 자세히 알아보자.


### 비트 NOT 연산자

*비트 NOT 연산자*(`~`)는 숫자의 모든 비트를 반전시킨다:

![](bitwiseNOT)

비트 NOT 연산자는 접두사 연산자로, 연산 대상 값 바로 앞에 공백 없이 위치한다:

```swift
let initialBits: UInt8 = 0b00001111
let invertedBits = ~initialBits  // 11110000과 동일
```

<!--
  - test: `bitwiseOperators`

  ```swifttest
  -> let initialBits: UInt8 = 0b00001111
  >> assert(initialBits == 15)
  -> let invertedBits = ~initialBits  // equals 11110000
  >> assert(invertedBits == 240)
  ```
-->

`UInt8` 정수는 8비트를 가지며 `0`부터 `255`까지의 값을 저장할 수 있다. 이 예제에서는 이진 값 `00001111`로 `UInt8` 정수를 초기화한다. 이 값은 처음 4비트가 `0`이고, 나머지 4비트가 `1`로 설정되어 있다. 이는 십진수 `15`와 동일하다.

<!-- Apple Books screenshot begins here. -->

비트 NOT 연산자는 `initialBits`와 동일하지만 모든 비트가 반전된 `invertedBits`라는 새로운 상수를 생성하는 데 사용된다. `0`은 `1`이 되고, `1`은 `0`이 된다. `invertedBits`의 값은 `11110000`이며, 이는 부호 없는 십진수 `240`과 동일하다.


### 비트 AND 연산자

*비트 AND 연산자*(`&`)는 두 숫자의 비트를 결합한다. 이 연산자는 두 입력 숫자의 비트가 모두 `1`인 경우에만 새로운 숫자의 비트를 `1`로 설정한다:

![](bitwiseAND)

아래 예제에서 `firstSixBits`와 `lastSixBits`의 값은 모두 가운데 네 비트가 `1`이다. 비트 AND 연산자는 이 두 값을 결합해 `00111100`이라는 숫자를 만든다. 이 값은 부호 없는 10진수 `60`과 같다:

```swift
let firstSixBits: UInt8 = 0b11111100
let lastSixBits: UInt8  = 0b00111111
let middleFourBits = firstSixBits & lastSixBits  // equals 00111100
```

<!--
  - test: `bitwiseOperators`

  ```swifttest
  -> let firstSixBits: UInt8 = 0b11111100
  -> let lastSixBits: UInt8  = 0b00111111
  -> let middleFourBits = firstSixBits & lastSixBits  // equals 00111100
  >> assert(middleFourBits == 0b00111100)
  ```
-->


### 비트 OR 연산자

*비트 OR 연산자*(`|`)는 두 숫자의 비트를 비교한다. 이 연산자는 두 입력 숫자 중 하나라도 비트가 `1`인 경우, 새로운 숫자의 해당 비트를 `1`로 설정한다.

![](bitwiseOR)

<!-- Apple Books screenshot ends here. -->

아래 예제에서 `someBits`와 `moreBits`는 서로 다른 비트가 `1`로 설정되어 있다. 비트 OR 연산자는 이 두 값을 결합해 `11111110`이라는 숫자를 만드는데, 이는 부호 없는 10진수로 `254`에 해당한다.

```swift
let someBits: UInt8 = 0b10110010
let moreBits: UInt8 = 0b01011110
let combinedbits = someBits | moreBits  // equals 11111110
```

<!--
  - test: `bitwiseOperators`

  ```swifttest
  -> let someBits: UInt8 = 0b10110010
  -> let moreBits: UInt8 = 0b01011110
  -> let combinedbits = someBits | moreBits  // equals 11111110
  >> assert(combinedbits == 0b11111110)
  ```
-->


### 비트 XOR 연산자

*비트 XOR 연산자* 또는 "배타적 OR 연산자"(`^`)는 두 숫자의 비트를 비교한다. 이 연산자는 입력 비트가 서로 다른 위치에 `1`을, 같은 위치에 `0`을 설정한 새로운 숫자를 반환한다.

![](bitwiseXOR)

아래 예제에서 `firstBits`와 `otherBits`는 각각 다른 위치에 `1`을 가지고 있다. 비트 XOR 연산자는 이 두 비트를 모두 `1`로 설정한다. `firstBits`와 `otherBits`의 나머지 비트는 일치하므로 출력 값에서 `0`으로 설정된다.

```swift
let firstBits: UInt8 = 0b00010100
let otherBits: UInt8 = 0b00000101
let outputBits = firstBits ^ otherBits  // equals 00010001
```

<!--
  - test: `bitwiseOperators`

  ```swifttest
  -> let firstBits: UInt8 = 0b00010100
  -> let otherBits: UInt8 = 0b00000101
  -> let outputBits = firstBits ^ otherBits  // equals 00010001
  >> assert(outputBits == 0b00010001)
  ```
-->


### 비트 단위 왼쪽 및 오른쪽 시프트 연산자

*비트 단위 왼쪽 시프트 연산자* (`<<`)와 *비트 단위 오른쪽 시프트 연산자* (`>>`)는 숫자의 모든 비트를 특정 위치 수만큼 왼쪽 또는 오른쪽으로 이동한다. 이 동작은 아래 정의된 규칙에 따라 수행된다.

비트 단위 왼쪽 및 오른쪽 시프트는 정수를 2의 배수로 곱하거나 나누는 효과를 가진다. 정수의 비트를 왼쪽으로 한 칸 이동하면 값이 두 배가 되고, 오른쪽으로 한 칸 이동하면 값이 절반이 된다.

<!--
  TODO: 이 주장에 대한 주의사항을 언급한다.
-->


#### 부호 없는 정수의 비트 시프트 동작

부호 없는 정수(unsigned integers)의 비트 시프트 동작은 다음과 같다:

1. 기존 비트를 지정된 횟수만큼 왼쪽 또는 오른쪽으로 이동한다.
2. 정수의 저장 공간을 벗어난 비트는 버린다.
3. 원래 비트가 이동한 후 남은 자리에는 0을 채운다.

이 방식을 *논리적 시프트(logical shift)*라고 부른다.

아래 그림은 `11111111 << 1`(왼쪽으로 1칸 이동)과 `11111111 >> 1`(오른쪽으로 1칸 이동)의 결과를 보여준다. 초록색 숫자는 이동한 비트, 회색 숫자는 버려진 비트, 분홍색 0은 삽입된 비트를 나타낸다:

![](bitshiftUnsigned)

Swift 코드에서 비트 시프트는 다음과 같이 동작한다:

```swift
let shiftBits: UInt8 = 4   // 00000100 in binary
shiftBits << 1             // 00001000
shiftBits << 2             // 00010000
shiftBits << 5             // 10000000
shiftBits << 6             // 00000000
shiftBits >> 2             // 00000001
```

<!--
  - test: `bitwiseShiftOperators`

  ```swifttest
  -> let shiftBits: UInt8 = 4   // 00000100 in binary
  >> let r0 =
  -> shiftBits << 1             // 00001000
  >> assert(r0 == 8)
  >> let r1 =
  -> shiftBits << 2             // 00010000
  >> assert(r1 == 16)
  >> let r2 =
  -> shiftBits << 5             // 10000000
  >> assert(r2 == 128)
  >> let r3 =
  -> shiftBits << 6             // 00000000
  >> assert(r3 == 0)
  >> let r4 =
  -> shiftBits >> 2             // 00000001
  >> assert(r4 == 1)
  ```
-->

<!--
  Rewrite the above to avoid bare expressions.
  Tracking bug is <rdar://problem/35301593>
-->

비트 시프트를 사용하면 다른 데이터 타입 내부의 값을 인코딩하거나 디코딩할 수 있다:

```swift
let pink: UInt32 = 0xCC6699
let redComponent = (pink & 0xFF0000) >> 16    // redComponent is 0xCC, or 204
let greenComponent = (pink & 0x00FF00) >> 8   // greenComponent is 0x66, or 102
let blueComponent = pink & 0x0000FF           // blueComponent is 0x99, or 153
```

<!--
  - test: `bitwiseShiftOperators`

  ```swifttest
  -> let pink: UInt32 = 0xCC6699
  -> let redComponent = (pink & 0xFF0000) >> 16    // redComponent is 0xCC, or 204
  -> let greenComponent = (pink & 0x00FF00) >> 8   // greenComponent is 0x66, or 102
  -> let blueComponent = pink & 0x0000FF           // blueComponent is 0x99, or 153
  >> assert(redComponent == 204)
  >> assert(greenComponent == 102)
  >> assert(blueComponent == 153)
  ```
-->

이 예제에서는 `UInt32` 타입의 상수 `pink`를 사용해 CSS 색상 값인 분홍색(`#CC6699`)을 저장한다. Swift에서 이 색상 값은 `0xCC6699`로 표현된다. 이 색상은 비트 AND 연산자(`&`)와 비트 오른쪽 시프트 연산자(`>>`)를 사용해 빨간색(`CC`), 초록색(`66`), 파란색(`99`) 성분으로 분해한다.

빨간색 성분은 `0xCC6699`와 `0xFF0000` 사이의 비트 AND 연산을 통해 얻는다. `0xFF0000`의 0은 `0xCC6699`의 두 번째와 세 번째 바이트를 "마스킹"하여 `6699`를 무시하고 `0xCC0000`을 결과로 남긴다. 이 숫자는 16칸 오른쪽으로 시프트(`>> 16`)된다. 16진수에서 각 문자 쌍은 8비트를 사용하므로, 16칸 오른쪽으로 이동하면 `0xCC0000`이 `0x0000CC`로 변환된다. 이는 `0xCC`와 같으며, 10진수 값으로 `204`이다.

마찬가지로, 초록색 성분은 `0xCC6699`와 `0x00FF00` 사이의 비트 AND 연산을 통해 얻는다. 이 연산은 `0x006600`을 결과로 반환한다. 이 값은 8칸 오른쪽으로 시프트되어 `0x66`이 되며, 10진수 값으로 `102`이다.

마지막으로, 파란색 성분은 `0xCC6699`와 `0x0000FF` 사이의 비트 AND 연산을 통해 얻는다. 이 연산은 `0x000099`를 결과로 반환한다. `0x000099`는 이미 `0x99`와 같으며, 10진수 값으로 `153`이므로 오른쪽 시프트 없이 그대로 사용한다.


#### 부호 있는 정수의 시프트 동작

부호 있는 정수의 시프트 동작은 부호 없는 정수보다 복잡하다. 이는 부호 있는 정수가 바이너리로 표현되는 방식 때문이다. (아래 예제는 간단히 8비트 부호 있는 정수를 기준으로 설명하지만, 동일한 원칙이 모든 크기의 부호 있는 정수에 적용된다.)

부호 있는 정수는 첫 번째 비트(*부호 비트*)를 사용해 정수가 양수인지 음수인지 나타낸다. 부호 비트가 `0`이면 양수, `1`이면 음수를 의미한다.

나머지 비트(*값 비트*)는 실제 값을 저장한다. 양수는 부호 없는 정수와 동일한 방식으로 저장되며, `0`부터 시작해 증가한다. 다음은 `Int8`에서 숫자 `4`의 비트 표현이다:

![](bitshiftSignedFour)

부호 비트는 `0`(양수)이고, 값 비트는 `4`를 바이너리로 표현한 것이다.

음수는 다르게 저장된다. 음수는 절댓값을 `2`의 `n`제곱에서 빼는 방식으로 저장되며, 여기서 `n`은 값 비트의 수다. 8비트 숫자는 7개의 값 비트를 가지므로, `2`의 `7`제곱인 `128`에서 절댓값을 뺀다.

다음은 `Int8`에서 숫자 `-4`의 비트 표현이다:

![](bitshiftSignedMinusFour)

이번에는 부호 비트가 `1`(음수)이고, 값 비트는 `124`(즉, `128 - 4`)를 바이너리로 표현한 것이다:

![](bitshiftSignedMinusFourValue)

음수를 표현하는 이 방식을 *2의 보수 표현법*이라고 한다. 처음 보기에는 음수를 표현하는 이상한 방식처럼 보일 수 있지만, 몇 가지 장점이 있다.

첫째, `-1`과 `-4`를 더할 때, 모든 8비트(부호 비트 포함)에 대해 표준 바이너리 덧셈을 수행하고, 8비트를 초과하는 부분을 버리면 된다:

![](bitshiftSignedAddition)

둘째, 2의 보수 표현법은 음수의 비트를 양수처럼 왼쪽이나 오른쪽으로 시프트할 수 있게 한다. 왼쪽으로 시프트할 때마다 값을 두 배로, 오른쪽으로 시프트할 때마다 값을 절반으로 줄일 수 있다. 이를 위해 부호 있는 정수를 오른쪽으로 시프트할 때는 추가 규칙을 적용한다: 부호 있는 정수를 오른쪽으로 시프트할 때, 부호 없는 정수와 동일한 규칙을 적용하되, 왼쪽의 빈 비트를 `0` 대신 *부호 비트*로 채운다.

![](bitshiftSigned)

이 동작은 부호 있는 정수가 오른쪽으로 시프트된 후에도 동일한 부호를 유지하게 하며, 이를 *산술 시프트*라고 한다.

양수와 음수가 특별한 방식으로 저장되기 때문에, 오른쪽으로 시프트하면 두 값 모두 0에 가까워진다. 시프트 동안 부호 비트를 유지하면, 음수는 값이 0에 가까워져도 여전히 음수로 남는다.


## 오버플로우 연산자

정수 상수나 변수에 저장할 수 없는 값을 넣으려고 하면, Swift는 기본적으로 유효하지 않은 값이 생성되는 것을 허용하는 대신 오류를 발생시킨다. 이 동작은 너무 크거나 작은 숫자를 다룰 때 추가적인 안전성을 제공한다.

예를 들어, `Int16` 정수 타입은 `-32768`부터 `32767`까지의 부호 있는 정수를 저장할 수 있다. 이 범위를 벗어나는 숫자를 `Int16` 상수나 변수에 할당하려고 하면 오류가 발생한다:

```swift
var potentialOverflow = Int16.max
// potentialOverflow는 32767로, Int16이 저장할 수 있는 최대값이다
potentialOverflow += 1
// 이 코드는 오류를 발생시킨다
```

<!--
  - test: `overflowOperatorsWillFailToOverflow`

  ```swifttest
  -> var potentialOverflow = Int16.max
  /> potentialOverflow equals \(potentialOverflow), which is the maximum value an Int16 can hold
  </ potentialOverflow equals 32767, which is the maximum value an Int16 can hold
  -> potentialOverflow += 1
  xx overflow
  // this causes an error
  ```
-->

값이 너무 크거나 작을 때 오류 처리를 제공하면 경계값 조건을 다룰 때 더 많은 유연성을 얻을 수 있다.

그러나 특정 상황에서 오버플로우 조건을 통해 사용 가능한 비트 수를 줄이는 동작을 원한다면, 오류를 발생시키는 대신 이 동작을 선택할 수 있다. Swift는 정수 계산에서 오버플로우 동작을 선택할 수 있는 세 가지 산술 *오버플로우 연산자*를 제공한다. 이 연산자들은 모두 앰퍼샌드(`&`)로 시작한다:

- 오버플로우 덧셈 (`&+`)
- 오버플로우 뺄셈 (`&-`)
- 오버플로우 곱셈 (`&*`)


### 값의 오버플로우

숫자는 양수와 음수 방향 모두에서 오버플로우가 발생할 수 있다.

다음은 부호 없는 정수(unsigned integer)가 양수 방향으로 오버플로우될 때의 예시로, 오버플로우 덧셈 연산자(`&+`)를 사용한다:

```swift
var unsignedOverflow = UInt8.max
// unsignedOverflow는 255로, UInt8이 가질 수 있는 최댓값이다.
unsignedOverflow = unsignedOverflow &+ 1
// unsignedOverflow는 이제 0이 된다.
```

<!--
  - test: `overflowOperatorsWillOverflowInPositiveDirection`

  ```swifttest
  -> var unsignedOverflow = UInt8.max
  /> unsignedOverflow equals \(unsignedOverflow), which is the maximum value a UInt8 can hold
  </ unsignedOverflow equals 255, which is the maximum value a UInt8 can hold
  -> unsignedOverflow = unsignedOverflow &+ 1
  /> unsignedOverflow is now equal to \(unsignedOverflow)
  </ unsignedOverflow is now equal to 0
  ```
-->

변수 `unsignedOverflow`는 `UInt8`이 가질 수 있는 최댓값(`255`, 또는 바이너리로 `11111111`)으로 초기화된다. 이후 오버플로우 덧셈 연산자(`&+`)를 사용해 `1`을 더한다. 이 연산은 `UInt8`이 담을 수 있는 크기를 넘어서게 되고, 오버플로우가 발생한다. 오버플로우 이후 `UInt8`의 범위 내에 남은 값은 `00000000`, 즉 0이 된다.

![](overflowAddition)

부호 없는 정수가 음수 방향으로 오버플로우될 때도 비슷한 현상이 발생한다. 다음은 오버플로우 뺄셈 연산자(`&-`)를 사용한 예시다:

```swift
var unsignedOverflow = UInt8.min
// unsignedOverflow는 0으로, UInt8이 가질 수 있는 최솟값이다.
unsignedOverflow = unsignedOverflow &- 1
// unsignedOverflow는 이제 255가 된다.
```

<!--
  - test: `overflowOperatorsWillOverflowInNegativeDirection`

  ```swifttest
  -> var unsignedOverflow = UInt8.min
  /> unsignedOverflow equals \(unsignedOverflow), which is the minimum value a UInt8 can hold
  </ unsignedOverflow equals 0, which is the minimum value a UInt8 can hold
  -> unsignedOverflow = unsignedOverflow &- 1
  /> unsignedOverflow is now equal to \(unsignedOverflow)
  </ unsignedOverflow is now equal to 255
  ```
-->

`UInt8`이 가질 수 있는 최솟값은 0, 즉 바이너리로 `00000000`이다. 오버플로우 뺄셈 연산자(`&-`)를 사용해 `00000000`에서 `1`을 빼면, 숫자가 오버플로우되어 `11111111`, 즉 10진수로 `255`가 된다.

![](overflowUnsignedSubtraction)

부호 있는 정수(signed integer)에서도 오버플로우가 발생한다. 부호 있는 정수의 모든 덧셈과 뺄셈은 비트 단위로 수행되며, 숫자의 부호 비트도 연산에 포함된다. 이는 <doc:AdvancedOperators#Bitwise-Left-and-Right-Shift-Operators>에서 설명한 바와 같다.

```swift
var signedOverflow = Int8.min
// signedOverflow는 -128로, Int8이 가질 수 있는 최솟값이다.
signedOverflow = signedOverflow &- 1
// signedOverflow는 이제 127이 된다.
```

<!--
  - test: `overflowOperatorsWillOverflowSigned`

  ```swifttest
  -> var signedOverflow = Int8.min
  /> signedOverflow equals \(signedOverflow), which is the minimum value an Int8 can hold
  </ signedOverflow equals -128, which is the minimum value an Int8 can hold
  -> signedOverflow = signedOverflow &- 1
  /> signedOverflow is now equal to \(signedOverflow)
  </ signedOverflow is now equal to 127
  ```
-->

`Int8`이 가질 수 있는 최솟값은 `-128`, 즉 바이너리로 `10000000`이다. 오버플로우 연산자를 사용해 이 바이너리 값에서 `1`을 빼면 `01111111`이 되며, 부호 비트가 바뀌어 `Int8`이 가질 수 있는 최댓값인 `127`이 된다.

![](overflowSignedSubtraction)

부호 있는 정수와 부호 없는 정수 모두에서, 양수 방향의 오버플로우는 최댓값에서 최솟값으로 순환하고, 음수 방향의 오버플로우는 최솟값에서 최댓값으로 순환한다.


## 연산자 우선순위와 결합 방향

연산자 *우선순위*는 어떤 연산자가 다른 연산자보다 더 높은 우선권을 가지는지를 결정한다. 즉, 우선순위가 높은 연산자가 먼저 계산된다.

연산자 *결합 방향*은 동일한 우선순위를 가진 연산자들이 어떻게 묶이는지를 정의한다. 이는 연산자가 왼쪽에 있는 표현식과 결합하는지, 아니면 오른쪽에 있는 표현식과 결합하는지를 나타낸다. 쉽게 말해, "왼쪽에 있는 표현식과 결합한다" 또는 "오른쪽에 있는 표현식과 결합한다"는 의미로 이해할 수 있다.

복합 표현식이 어떤 순서로 계산될지 파악할 때는 각 연산자의 우선순위와 결합 방향을 고려하는 것이 중요하다. 예를 들어, 아래 표현식이 왜 `17`이라는 결과를 내는지는 연산자 우선순위로 설명할 수 있다.

```swift
2 + 3 % 4 * 5
// 이 결과는 17이다
```

<!--
  - test: `evaluationOrder`

  ```swifttest
  >> let r0 =
  -> 2 + 3 % 4 * 5
  >> assert(r0 == 17)
  /> this equals \(2 + 3 % 4 * 5)
  </ this equals 17
  ```
-->

<!--
  Rewrite the above to avoid bare expressions.
  Tracking bug is <rdar://problem/35301593>
-->

만약 이 표현식을 왼쪽에서 오른쪽으로 순서대로 읽는다면, 다음과 같이 계산될 것으로 예상할 수 있다:

- `2` 더하기 `3`은 `5`
- `5` 나누기 `4`의 나머지는 `1`
- `1` 곱하기 `5`는 `5`

하지만 실제 결과는 `5`가 아니라 `17`이다. 이는 우선순위가 높은 연산자가 낮은 연산자보다 먼저 계산되기 때문이다. Swift에서는 C 언어와 마찬가지로 나머지 연산자(`%`)와 곱셈 연산자(`*`)가 덧셈 연산자(`+`)보다 우선순위가 높다. 따라서 이 두 연산자가 덧셈보다 먼저 계산된다.

그런데 나머지 연산자와 곱셈 연산자는 서로 *동일한* 우선순위를 가진다. 이때 정확한 계산 순서를 파악하려면 결합 방향도 고려해야 한다. 나머지 연산자와 곱셈 연산자는 모두 왼쪽에 있는 표현식과 결합한다. 이는 표현식의 해당 부분에 왼쪽부터 묵시적 괄호를 추가하는 것과 같다:

```swift
2 + ((3 % 4) * 5)
```

<!--
  - test: `evaluationOrder`

  ```swifttest
  >> let r1 =
  -> 2 + ((3 % 4) * 5)
  >> assert(r1 == 17)
  ```
-->

<!--
  Rewrite the above to avoid bare expressions.
  Tracking bug is <rdar://problem/35301593>
-->

`(3 % 4)`는 `3`이므로, 이 표현식은 다음과 동일하다:

```swift
2 + (3 * 5)
```

<!--
  - test: `evaluationOrder`

  ```swifttest
  >> let r2 =
  -> 2 + (3 * 5)
  >> assert(r2 == 17)
  ```
-->

<!--
  Rewrite the above to avoid bare expressions.
  Tracking bug is <rdar://problem/35301593>
-->

`(3 * 5)`는 `15`이므로, 이 표현식은 다음과 동일하다:

```swift
2 + 15
```

<!--
  - test: `evaluationOrder`

  ```swifttest
  >> let r3 =
  -> 2 + 15
  >> assert(r3 == 17)
  ```
-->

<!--
  Rewrite the above to avoid bare expressions.
  Tracking bug is <rdar://problem/35301593>
-->

이 계산의 최종 결과는 `17`이다.

Swift 표준 라이브러리에서 제공하는 연산자에 대한 정보, 그리고 연산자 우선순위 그룹과 결합 방향 설정의 전체 목록은 [Operator Declarations](https://developer.apple.com/documentation/swift/operator_declarations)에서 확인할 수 있다.

> 주의: Swift의 연산자 우선순위와 결합 방향 규칙은 C나 Objective-C보다 더 단순하고 예측 가능하다. 하지만 이는 Swift가 C 기반 언어와 완전히 동일하지 않다는 것을 의미한다. 기존 코드를 Swift로 포팅할 때는 연산자의 상호작용이 의도한 대로 동작하는지 주의 깊게 확인해야 한다.


## 연산자 메서드

클래스와 구조체는 기존 연산자를 직접 구현할 수 있다. 이를 *연산자 오버로딩*이라고 한다.

아래 예제는 커스텀 구조체에 대해 산술 덧셈 연산자(`+`)를 구현하는 방법을 보여준다. 산술 덧셈 연산자는 두 개의 대상에 대해 동작하므로 바이너리 연산자이며, 두 대상 사이에 위치하므로 중위 연산자이다.

예제에서는 2차원 위치 벡터 `(x, y)`를 나타내는 `Vector2D` 구조체를 정의하고, 이 구조체의 인스턴스를 더하는 *연산자 메서드*를 정의한다:

```swift
struct Vector2D {
    var x = 0.0, y = 0.0
}

extension Vector2D {
    static func + (left: Vector2D, right: Vector2D) -> Vector2D {
       return Vector2D(x: left.x + right.x, y: left.y + right.y)
    }
}
```

<!--
  - test: `customOperators`

  ```swifttest
  -> struct Vector2D {
        var x = 0.0, y = 0.0
     }

  -> extension Vector2D {
         static func + (left: Vector2D, right: Vector2D) -> Vector2D {
            return Vector2D(x: left.x + right.x, y: left.y + right.y)
         }
     }
  ```
-->

연산자 메서드는 `Vector2D`에 대한 타입 메서드로 정의되며, 메서드 이름은 오버로딩할 연산자(`+`)와 일치한다. 덧셈은 벡터의 필수 동작이 아니므로, 이 타입 메서드는 `Vector2D`의 기본 구조체 선언이 아닌 확장에서 정의된다. 산술 덧셈 연산자는 바이너리 연산자이므로, 이 연산자 메서드는 `Vector2D` 타입의 두 입력 매개변수를 받고, `Vector2D` 타입의 단일 출력 값을 반환한다.

이 구현에서 입력 매개변수는 `+` 연산자의 왼쪽과 오른쪽에 위치할 `Vector2D` 인스턴스를 나타내기 위해 `left`와 `right`로 명명된다. 메서드는 새로운 `Vector2D` 인스턴스를 반환하며, 이 인스턴스의 `x`와 `y` 속성은 더해진 두 `Vector2D` 인스턴스의 `x`와 `y` 속성의 합으로 초기화된다.

이 타입 메서드는 기존 `Vector2D` 인스턴스 사이에서 중위 연산자로 사용할 수 있다:

```swift
let vector = Vector2D(x: 3.0, y: 1.0)
let anotherVector = Vector2D(x: 2.0, y: 4.0)
let combinedVector = vector + anotherVector
// combinedVector는 (5.0, 5.0) 값을 가진 Vector2D 인스턴스이다.
```

<!--
  - test: `customOperators`

  ```swifttest
  -> let vector = Vector2D(x: 3.0, y: 1.0)
  -> let anotherVector = Vector2D(x: 2.0, y: 4.0)
  -> let combinedVector = vector + anotherVector
  /> combinedVector는 (\(combinedVector.x), \(combinedVector.y)) 값을 가진 Vector2D 인스턴스이다.
  </ combinedVector는 (5.0, 5.0) 값을 가진 Vector2D 인스턴스이다.
  ```
-->

이 예제는 벡터 `(3.0, 1.0)`와 `(2.0, 4.0)`를 더해 벡터 `(5.0, 5.0)`를 만든다. 아래 그림에서 이를 확인할 수 있다.

![](vectorAddition)


### 접두사와 접미사 연산자

위 예제는 커스텀 이항 중위 연산자를 구현한 것을 보여준다. 클래스와 구조체는 또한 표준 *단항 연산자*를 구현할 수 있다. 단항 연산자는 하나의 대상에 대해 동작한다. 이 연산자는 대상 앞에 위치하면 *접두사* 연산자(예: `-a`)이고, 대상 뒤에 위치하면 *접미사* 연산자(예: `b!`)이다.

접두사 또는 접미사 단항 연산자를 구현하려면, 연산자 메서드를 선언할 때 `func` 키워드 앞에 `prefix` 또는 `postfix` 수식어를 붙인다:

```swift
extension Vector2D {
    static prefix func - (vector: Vector2D) -> Vector2D {
        return Vector2D(x: -vector.x, y: -vector.y)
    }
}
```

<!--
  - test: `customOperators`

  ```swifttest
  -> extension Vector2D {
         static prefix func - (vector: Vector2D) -> Vector2D {
             return Vector2D(x: -vector.x, y: -vector.y)
         }
     }
  ```
-->

위 예제는 `Vector2D` 인스턴스에 대한 단항 마이너스 연산자(`-a`)를 구현한다. 단항 마이너스 연산자는 접두사 연산자이므로, 이 메서드는 `prefix` 수식어로 한정해야 한다.

단순한 숫자 값의 경우, 단항 마이너스 연산자는 양수를 음수로, 음수를 양수로 변환한다. `Vector2D` 인스턴스에 대한 해당 구현은 `x`와 `y` 프로퍼티 모두에 이 연산을 수행한다:

```swift
let positive = Vector2D(x: 3.0, y: 4.0)
let negative = -positive
// negative는 (-3.0, -4.0) 값을 가진 Vector2D 인스턴스이다.
let alsoPositive = -negative
// alsoPositive는 (3.0, 4.0) 값을 가진 Vector2D 인스턴스이다.
```

<!--
  - test: `customOperators`

  ```swifttest
  -> let positive = Vector2D(x: 3.0, y: 4.0)
  -> let negative = -positive
  /> negative is a Vector2D instance with values of (\(negative.x), \(negative.y))
  </ negative is a Vector2D instance with values of (-3.0, -4.0)
  -> let alsoPositive = -negative
  /> alsoPositive is a Vector2D instance with values of (\(alsoPositive.x), \(alsoPositive.y))
  </ alsoPositive is a Vector2D instance with values of (3.0, 4.0)
  ```
-->


### 복합 할당 연산자

*복합 할당 연산자*는 할당(`=`)을 다른 연산과 결합한다. 예를 들어, 덧셈 할당 연산자(`+=`)는 덧셈과 할당을 하나의 연산으로 합친다. 복합 할당 연산자의 왼쪽 입력 매개변수 타입은 `inout`으로 표시한다. 매개변수의 값이 연산자 메서드 내부에서 직접 수정되기 때문이다.

아래 예제는 `Vector2D` 인스턴스에 대한 덧셈 할당 연산자 메서드를 구현한다:

```swift
extension Vector2D {
    static func += (left: inout Vector2D, right: Vector2D) {
        left = left + right
    }
}
```

<!--
  - test: `customOperators`

  ```swifttest
  -> extension Vector2D {
         static func += (left: inout Vector2D, right: Vector2D) {
             left = left + right
         }
     }
  ```
-->

이전에 덧셈 연산자를 정의했기 때문에, 여기서 덧셈 과정을 다시 구현할 필요가 없다. 대신, 덧셈 할당 연산자 메서드는 기존의 덧셈 연산자 메서드를 활용하고, 이를 사용해 왼쪽 값을 왼쪽 값 더하기 오른쪽 값으로 설정한다:

```swift
var original = Vector2D(x: 1.0, y: 2.0)
let vectorToAdd = Vector2D(x: 3.0, y: 4.0)
original += vectorToAdd
// original now has values of (4.0, 6.0)
```

<!--
  - test: `customOperators`

  ```swifttest
  -> var original = Vector2D(x: 1.0, y: 2.0)
  -> let vectorToAdd = Vector2D(x: 3.0, y: 4.0)
  -> original += vectorToAdd
  /> original now has values of (\(original.x), \(original.y))
  </ original now has values of (4.0, 6.0)
  ```
-->

> 주의: 기본 할당 연산자(`=`)를 오버로드할 수 없다. 오직 복합 할당 연산자만 오버로드할 수 있다. 마찬가지로 삼항 조건 연산자(`a ? b : c`)도 오버로드할 수 없다.

<!--
  - test: `cant-overload-assignment`

  ```swifttest
  >> struct Vector2D {
  >>    var x = 0.0, y = 0.0
  >> }
  >> extension Vector2D {
  >>     static func = (left: inout Vector2D, right: Vector2D) {
  >>         left = right
  >>     }
  >> }
  !$ error: expected identifier in function declaration
  !! static func = (left: inout Vector2D, right: Vector2D) {
  !!             ^
  ```
-->


### 동등 연산자

기본적으로 커스텀 클래스와 구조체는 *동등 연산자*를 구현하지 않는다. 여기서 동등 연산자는 *같음* 연산자(`==`)와 *같지 않음* 연산자(`!=`)를 의미한다. 일반적으로 `==` 연산자를 직접 구현하고, `!=` 연산자는 Swift 표준 라이브러리가 제공하는 기본 구현을 사용한다. 이때 `!=` 연산자는 `==` 연산자의 결과를 부정하는 방식으로 동작한다. `==` 연산자를 구현하는 방법은 두 가지다. 직접 구현하거나, 많은 타입의 경우 Swift가 자동으로 구현을 생성하도록 요청할 수 있다. 두 경우 모두 Swift 표준 라이브러리의 `Equatable` 프로토콜을 준수해야 한다.

다른 중위 연산자를 구현하는 것과 같은 방식으로 `==` 연산자를 구현할 수 있다:

```swift
extension Vector2D: Equatable {
    static func == (left: Vector2D, right: Vector2D) -> Bool {
       return (left.x == right.x) && (left.y == right.y)
    }
}
```

<!--
  - test: `customOperators`

  ```swifttest
  -> extension Vector2D: Equatable {
         static func == (left: Vector2D, right: Vector2D) -> Bool {
            return (left.x == right.x) && (left.y == right.y)
         }
     }
  ```
-->

위 예제는 두 `Vector2D` 인스턴스가 동일한 값을 가지는지 확인하기 위해 `==` 연산자를 구현한다. `Vector2D`의 경우 "두 인스턴스가 동일한 `x` 값과 `y` 값을 가진다"는 의미로 "같음"을 정의하는 것이 합리적이며, 이 로직이 연산자 구현에 사용된다.

이제 이 연산자를 사용해 두 `Vector2D` 인스턴스가 동등한지 확인할 수 있다:

```swift
let twoThree = Vector2D(x: 2.0, y: 3.0)
let anotherTwoThree = Vector2D(x: 2.0, y: 3.0)
if twoThree == anotherTwoThree {
    print("These two vectors are equivalent.")
}
// Prints "These two vectors are equivalent."
```

<!--
  - test: `customOperators`

  ```swifttest
  -> let twoThree = Vector2D(x: 2.0, y: 3.0)
  -> let anotherTwoThree = Vector2D(x: 2.0, y: 3.0)
  -> if twoThree == anotherTwoThree {
        print("These two vectors are equivalent.")
     }
  <- These two vectors are equivalent.
  ```
-->

많은 간단한 경우, Swift가 동등 연산자의 구현을 자동으로 생성하도록 요청할 수 있다. 이는 <doc:Protocols#Adopting-a-Protocol-Using-a-Synthesized-Implementation>에서 설명한 바와 같다.


## 커스텀 연산자

Swift에서 제공하는 표준 연산자 외에도 여러분은 직접 *커스텀 연산자*를 선언하고 구현할 수 있다. 커스텀 연산자를 정의할 때 사용할 수 있는 문자 목록은 <doc:LexicalStructure#Operators>를 참고한다.

새로운 연산자는 `operator` 키워드를 사용해 전역 수준에서 선언하며, `prefix`, `infix`, `postfix` 수식어로 표시한다:

```swift
prefix operator +++
```

<!--
  - test: `customOperators`

  ```swifttest
  -> prefix operator +++
  ```
-->

위 예제는 `+++`라는 새로운 전위 연산자를 정의한다. 이 연산자는 Swift에서 아직 정의된 의미가 없으므로, 아래에서 `Vector2D` 인스턴스를 다루는 특정 맥락에서 새로운 의미를 부여한다. 이 예제에서는 `+++`를 새로운 "전위 두 배 연산자"로 간주한다. 이 연산자는 앞서 정의한 덧셈 할당 연산자를 사용해 `Vector2D` 인스턴스의 `x`와 `y` 값을 두 배로 만든다. `+++` 연산자를 구현하려면 `Vector2D`에 `+++`라는 타입 메서드를 다음과 같이 추가한다:

```swift
extension Vector2D {
    static prefix func +++ (vector: inout Vector2D) -> Vector2D {
        vector += vector
        return vector
    }
}

var toBeDoubled = Vector2D(x: 1.0, y: 4.0)
let afterDoubling = +++toBeDoubled
// toBeDoubled now has values of (2.0, 8.0)
// afterDoubling also has values of (2.0, 8.0)
```

<!--
  - test: `customOperators`

  ```swifttest
  -> extension Vector2D {
        static prefix func +++ (vector: inout Vector2D) -> Vector2D {
           vector += vector
           return vector
        }
     }

  -> var toBeDoubled = Vector2D(x: 1.0, y: 4.0)
  -> let afterDoubling = +++toBeDoubled
  /> toBeDoubled now has values of (\(toBeDoubled.x), \(toBeDoubled.y))
  </ toBeDoubled now has values of (2.0, 8.0)
  /> afterDoubling also has values of (\(afterDoubling.x), \(afterDoubling.y))
  </ afterDoubling also has values of (2.0, 8.0)
  ```
-->


### 커스텀 중위 연산자의 우선순위

커스텀 중위 연산자는 각각 특정 우선순위 그룹에 속한다. 우선순위 그룹은 연산자의 우선순위와 결합 방향을 정의한다. 이 특성들이 다른 중위 연산자와 어떻게 상호작용하는지에 대한 자세한 설명은 <doc:AdvancedOperators#Precedence-and-Associativity>를 참고한다.

명시적으로 우선순위 그룹을 지정하지 않은 커스텀 중위 연산자는 기본 우선순위 그룹에 할당된다. 이 기본 그룹은 삼항 조건 연산자보다 한 단계 높은 우선순위를 가진다.

다음 예제는 `+-`이라는 새로운 커스텀 중위 연산자를 정의한다. 이 연산자는 `AdditionPrecedence` 우선순위 그룹에 속한다:

```swift
infix operator +-: AdditionPrecedence
extension Vector2D {
    static func +- (left: Vector2D, right: Vector2D) -> Vector2D {
        return Vector2D(x: left.x + right.x, y: left.y - right.y)
    }
}
let firstVector = Vector2D(x: 1.0, y: 2.0)
let secondVector = Vector2D(x: 3.0, y: 4.0)
let plusMinusVector = firstVector +- secondVector
// plusMinusVector는 (4.0, -2.0) 값을 가진 Vector2D 인스턴스다.
```

<!--
  - test: `customOperators`

  ```swifttest
  -> infix operator +-: AdditionPrecedence
  -> extension Vector2D {
        static func +- (left: Vector2D, right: Vector2D) -> Vector2D {
           return Vector2D(x: left.x + right.x, y: left.y - right.y)
        }
     }
  -> let firstVector = Vector2D(x: 1.0, y: 2.0)
  -> let secondVector = Vector2D(x: 3.0, y: 4.0)
  -> let plusMinusVector = firstVector +- secondVector
  /> plusMinusVector is a Vector2D instance with values of (\(plusMinusVector.x), \(plusMinusVector.y))
  </ plusMinusVector is a Vector2D instance with values of (4.0, -2.0)
  ```
-->

이 연산자는 두 벡터의 `x` 값을 더하고, 첫 번째 벡터의 `y` 값에서 두 번째 벡터의 `y` 값을 뺀다. 기본적으로 "덧셈" 연산자이기 때문에, `+`와 `-`와 같은 덧셈 연산자와 동일한 우선순위 그룹을 가진다. Swift 표준 라이브러리에서 제공하는 연산자와 우선순위 그룹, 결합 방향에 대한 전체 목록은 [Operator Declarations](https://developer.apple.com/documentation/swift/operator_declarations)를 참고한다. 우선순위 그룹에 대한 자세한 정보와 커스텀 연산자 및 우선순위 그룹을 정의하는 문법은 <doc:Declarations#Operator-Declaration>을 확인한다.

> 참고: 전위 연산자나 후위 연산자를 정의할 때는 우선순위를 지정하지 않는다. 하지만 동일한 피연산자에 전위 연산자와 후위 연산자를 모두 적용할 경우, 후위 연산자가 먼저 적용된다.

<!--
  - test: `postfixOperatorsAreAppliedBeforePrefixOperators`

  ```swifttest
  -> prefix operator +++
  -> postfix operator ---
  -> extension Int {
         static prefix func +++ (x: Int) -> Int {
             return x * 2
         }
     }
  -> extension Int {
         static postfix func --- (x: Int) -> Int {
             return x - 1
         }
     }
  -> let x = +++1---
  -> let y = +++(1---)
  -> let z = (+++1)---
  -> print(x, y, z)
  <- 0 0 1
  // Note that x==y
  ```
-->


## Result Builders

*Result Builder*는 리스트나 트리 같은 중첩된 데이터를 자연스럽고 선언적인 방식으로 생성하기 위한 구문을 추가하는 타입이다. Result Builder를 사용하는 코드는 조건문이나 반복문과 같은 일반적인 Swift 구문을 포함할 수 있다.

아래 코드는 별과 텍스트를 사용해 한 줄에 그림을 그리는 몇 가지 타입을 정의한다.

```swift
protocol Drawable {
    func draw() -> String
}
struct Line: Drawable {
    var elements: [Drawable]
    func draw() -> String {
        return elements.map { $0.draw() }.joined(separator: "")
    }
}
struct Text: Drawable {
    var content: String
    init(_ content: String) { self.content = content }
    func draw() -> String { return content }
}
struct Space: Drawable {
    func draw() -> String { return " " }
}
struct Stars: Drawable {
    var length: Int
    func draw() -> String { return String(repeating: "*", count: length) }
}
struct AllCaps: Drawable {
    var content: Drawable
    func draw() -> String { return content.draw().uppercased() }
}
```

<!--
  - test: `result-builder`

  ```swifttest
  -> protocol Drawable {
         func draw() -> String
     }
  -> struct Line: Drawable {
         var elements: [Drawable]
         func draw() -> String {
             return elements.map { $0.draw() }.joined(separator: "")
         }
     }
  -> struct Text: Drawable {
         var content: String
         init(_ content: String) { self.content = content }
         func draw() -> String { return content }
     }
  -> struct Space: Drawable {
         func draw() -> String { return " " }
     }
  -> struct Stars: Drawable {
         var length: Int
         func draw() -> String { return String(repeating: "*", count: length) }
     }
  -> struct AllCaps: Drawable {
         var content: Drawable
         func draw() -> String { return content.draw().uppercased() }
     }
  ```
-->

`Drawable` 프로토콜은 선이나 도형처럼 그릴 수 있는 것에 대한 요구사항을 정의한다. 해당 타입은 `draw()` 메서드를 구현해야 한다. `Line` 구조체는 한 줄로 된 그림을 나타내며, 대부분의 그림에서 최상위 컨테이너 역할을 한다. `Line`을 그리기 위해 구조체는 각 구성 요소의 `draw()`를 호출하고, 결과 문자열을 하나로 합친다. `Text` 구조체는 문자열을 감싸서 그림의 일부로 만든다. `AllCaps` 구조체는 다른 그림을 감싸고 수정하며, 그림 안의 모든 텍스트를 대문자로 변환한다.

이 타입들을 사용해 그림을 만들려면 초기화 메서드를 호출하면 된다.

```swift
let name: String? = "Ravi Patel"
let manualDrawing = Line(elements: [
     Stars(length: 3),
     Text("Hello"),
     Space(),
     AllCaps(content: Text((name ?? "World") + "!")),
     Stars(length: 2),
])
print(manualDrawing.draw())
// Prints "***Hello RAVI PATEL!**"
```

<!--
  - test: `result-builder`

  ```swifttest
  -> let name: String? = "Ravi Patel"
  -> let manualDrawing = Line(elements: [
          Stars(length: 3),
          Text("Hello"),
          Space(),
          AllCaps(content: Text((name ?? "World") + "!")),
          Stars(length: 2),
     ])
  -> print(manualDrawing.draw())
  <- ***Hello RAVI PATEL!**
  ```
-->

이 코드는 동작하지만 약간 불편하다. `AllCaps` 뒤의 깊게 중첩된 괄호는 읽기 어렵다. `name`이 `nil`일 때 "World"를 사용하는 폴백 로직은 `??` 연산자를 사용해 인라인으로 처리해야 하며, 더 복잡한 경우에는 어려울 수 있다. 그림의 일부를 구성하기 위해 `switch`나 `for` 루프를 포함해야 한다면, 이를 구현할 방법이 없다. Result Builder를 사용하면 이 코드를 일반 Swift 코드처럼 보이게 다시 작성할 수 있다.

Result Builder를 정의하려면 타입 선언에 `@resultBuilder` 속성을 작성한다. 예를 들어, 이 코드는 `DrawingBuilder`라는 Result Builder를 정의하며, 선언적 구문을 사용해 그림을 설명할 수 있게 한다.

```swift
@resultBuilder
struct DrawingBuilder {
    static func buildBlock(_ components: Drawable...) -> Drawable {
        return Line(elements: components)
    }
    static func buildEither(first: Drawable) -> Drawable {
        return first
    }
    static func buildEither(second: Drawable) -> Drawable {
        return second
    }
}
```

<!--
  - test: `result-builder`

  ```swifttest
  -> @resultBuilder
  -> struct DrawingBuilder {
         static func buildBlock(_ components: Drawable...) -> Drawable {
             return Line(elements: components)
         }
         static func buildEither(first: Drawable) -> Drawable {
             return first
         }
         static func buildEither(second: Drawable) -> Drawable {
             return second
         }
     }
  ```
-->

`DrawingBuilder` 구조체는 Result Builder 구문의 일부를 구현하는 세 가지 메서드를 정의한다. `buildBlock(_:)` 메서드는 코드 블록 안에 일련의 줄을 작성하는 기능을 추가한다. 이 메서드는 블록 안의 구성 요소를 `Line`으로 결합한다. `buildEither(first:)`와 `buildEither(second:)` 메서드는 `if`-`else` 구문을 지원한다.

`@DrawingBuilder` 속성을 함수의 매개변수에 적용하면, 함수에 전달된 클로저를 Result Builder가 생성한 값으로 변환한다. 예를 들어:

```swift
func draw(@DrawingBuilder content: () -> Drawable) -> Drawable {
    return content()
}
func caps(@DrawingBuilder content: () -> Drawable) -> Drawable {
    return AllCaps(content: content())
}

func makeGreeting(for name: String? = nil) -> Drawable {
    let greeting = draw {
        Stars(length: 3)
        Text("Hello")
        Space()
        caps {
            if let name = name {
                Text(name + "!")
            } else {
                Text("World!")
            }
        }
        Stars(length: 2)
    }
    return greeting
}
let genericGreeting = makeGreeting()
print(genericGreeting.draw())
// Prints "***Hello WORLD!**"

let personalGreeting = makeGreeting(for: "Ravi Patel")
print(personalGreeting.draw())
// Prints "***Hello RAVI PATEL!**"
```

<!--
  - test: `result-builder`

  ```swifttest
  -> func draw(@DrawingBuilder content: () -> Drawable) -> Drawable {
         return content()
     }
  -> func caps(@DrawingBuilder content: () -> Drawable) -> Drawable {
         return AllCaps(content: content())
     }

  -> func makeGreeting(for name: String? = nil) -> Drawable {
         let greeting = draw {
             Stars(length: 3)
             Text("Hello")
             Space()
             caps {
                 if let name = name {
                     Text(name + "!")
                 } else {
                     Text("World!")
                 }
             }
             Stars(length: 2)
         }
         return greeting
     }
  -> let genericGreeting = makeGreeting()
  -> print(genericGreeting.draw())
  <- ***Hello WORLD!**

  -> let personalGreeting = makeGreeting(for: "Ravi Patel")
  -> print(personalGreeting.draw())
  <- ***Hello RAVI PATEL!**
  ```
-->

`makeGreeting(for:)` 함수는 `name` 매개변수를 받아 개인화된 인사말을 그린다. `draw(_:)`와 `caps(_:)` 함수는 모두 단일 클로저를 인자로 받으며, 이 클로저는 `@DrawingBuilder` 속성으로 표시된다. 이 함수들을 호출할 때 `DrawingBuilder`가 정의한 특별한 구문을 사용한다. Swift는 그림에 대한 선언적 설명을 `DrawingBuilder`의 메서드 호출로 변환해 함수 인자로 전달된 값을 구성한다. 예를 들어, Swift는 `caps(_:)` 호출을 다음과 같은 코드로 변환한다.

```swift
let capsDrawing = caps {
    let partialDrawing: Drawable
    if let name = name {
        let text = Text(name + "!")
        partialDrawing = DrawingBuilder.buildEither(first: text)
    } else {
        let text = Text("World!")
        partialDrawing = DrawingBuilder.buildEither(second: text)
    }
    return partialDrawing
}
```

<!--
  - test: `result-builder`

  ```swifttest
  -> let capsDrawing = caps {
         let partialDrawing: Drawable
         if let name = name {
             let text = Text(name + "!")
             partialDrawing = DrawingBuilder.buildEither(first: text)
         } else {
             let text = Text("World!")
             partialDrawing = DrawingBuilder.buildEither(second: text)
         }
         return partialDrawing
  -> }
  >> print(capsDrawing.draw())
  << RAVI PATEL!
  ```
-->

Swift는 `if`-`else` 블록을 `buildEither(first:)`와 `buildEither(second:)` 메서드 호출로 변환한다. 이 메서드들을 직접 호출하지는 않지만, 변환 결과를 보면 Swift가 `DrawingBuilder` 구문을 사용할 때 코드를 어떻게 변환하는지 쉽게 이해할 수 있다.

특별한 그림 구문에서 `for` 루프를 작성할 수 있도록 지원하려면 `buildArray(_:)` 메서드를 추가한다.

```swift
extension DrawingBuilder {
    static func buildArray(_ components: [Drawable]) -> Drawable {
        return Line(elements: components)
    }
}
let manyStars = draw {
    Text("Stars:")
    for length in 1...3 {
        Space()
        Stars(length: length)
    }
}
```

<!--
  - test: `result-builder`

  ```swifttest
  -> extension DrawingBuilder {
         static func buildArray(_ components: [Drawable]) -> Drawable {
             return Line(elements: components)
         }
     }
  -> let manyStars = draw {
         Text("Stars:")
         for length in 1...3 {
             Space()
             Stars(length: length)
         }
  -> }
  >> print(manyStars.draw())
  << Stars: * ** ***
  ```
-->

위 코드에서 `for` 루프는 그림 배열을 생성하고, `buildArray(_:)` 메서드는 이 배열을 `Line`으로 변환한다.

Swift가 Builder 구문을 Builder 타입의 메서드 호출로 변환하는 전체 목록은 <doc:Attributes#resultBuilder>를 참조한다.

<!--
  The following needs more work...

   Protocol Operator Requirements
   ------------------------------

   You can include operators in the requirements of a protocol.
   A type conforms to the protocol
   only if there's an implementation of the operator for that type.
   You use ``Self`` to refer to the type that will conform to the protocol,
   just like you do in other protocol requirements.
   For example, the Swift standard library defines the ``Equatable`` protocol
   which requires the ``==`` operator:

   .. testcode:: protocolOperator

      -> protocol Equatable {
             static func == (lhs: Self, rhs: Self) -> Bool
         }

   To make a type conform to the protocol,
   you need to implement the ``==`` operator for that type.
   For example:

   .. testcode:: protocolOperator

  -> struct Vector3D {
        var x = 0.0, y = 0.0, z = 0.0
     }
  -> extension Vector3D: Equatable {
         static func == (left: Vector3D, right: Vector3D) -> Bool {
             return (left.x == right.x) && (left.y == right.y) && (left.z == right.z)
         }
     }
  >> let r0 =
  >> Vector3D(x: 1.1, y: 2.3, z: 12) == Vector3D(x: 1.1, y: 2.3, z: 12)
  >> assert(r0)
-->

<!--
  FIXME: This doesn't work
  <rdar://problem/27536066> SE-0091 -- can't have protocol conformance & operator implementation in different types

   For operators that take values of two different types,
   the operator's implementation doesn't have to be
   a member of the type that conforms to the protocol ---
   the implementation can also be a member of the other type.
   For example,
   the code below defines the ``*`` operator
   to scale a vector by a given amount.
   The ``Vector2D`` structure conforms to this protocol
   because there's an implementation of the operator
   that takes a ``Vector2D`` as its second argument,
   even though that implementation is a member of ``Double``.

   .. testcode:: customOperators

  -> infix operator *** {}
  -> protocol AnotherProtocol {
         // static func * (scale: Double, vector: Self) -> Self
         static func *** (scale: Double, vector: Vector2D) -> Vector2D
     }

  -> extension Double {
         static func *** (scale: Double, vector: Vector2D) -> Vector2D {
             return Vector2D(x: scale * vector.x, y: scale * vector.y)
         }
     }
  -> extension Vector2D: AnotherProtocol {}
  -> let unitVector = Vector2D(x: 1.0, y: 1.0)
  -> print(2.5 *** unitVector)
  <- Vector2D(x: 2.5, y: 2.5)
-->

<!--
  TODO: However, Doug thought that this might be better covered by Generics,
  where you know that two things are definitely of the same type.
  Perhaps mention it here, but don't actually show an example?
-->

<!--
  TODO: generic operators
-->

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->
