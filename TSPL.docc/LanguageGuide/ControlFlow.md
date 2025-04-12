# 제어 흐름

Swift는 다양한 제어 흐름 문법을 제공한다. 이를 통해 코드를 분기, 반복, 조기 종료 등의 방식으로 구조화할 수 있다.

Swift에서 제공하는 주요 제어 흐름 문법은 다음과 같다:

- `while` 반복문: 특정 작업을 여러 번 수행한다.
- `if`, `guard`, `switch` 문: 특정 조건에 따라 다른 코드 분기를 실행한다.
- `break`와 `continue`: 코드 실행 흐름을 다른 지점으로 이동시킨다.
- `for`-`in` 반복문: 배열, 딕셔너리, 범위, 문자열 등의 시퀀스를 쉽게 순회할 수 있다.
- `defer` 문: 현재 스코프를 벗어날 때 실행될 코드를 정의한다.

Swift의 `switch` 문은 C 계열 언어의 `switch` 문보다 훨씬 강력하다. 각 `case`는 다양한 패턴과 매칭될 수 있으며, 구간 매칭, 튜플, 특정 타입으로의 캐스팅 등을 지원한다. `switch` 문의 `case`에서 매칭된 값은 임시 상수나 변수로 바인딩되어 해당 `case` 내에서 사용할 수 있다. 또한, 각 `case`에 `where` 절을 추가해 복잡한 매칭 조건을 표현할 수 있다.

이러한 제어 흐름 문법을 활용하면 코드를 더 명확하고 효율적으로 작성할 수 있다. Swift는 특히 `switch` 문을 통해 다양한 상황에 유연하게 대응할 수 있는 강력한 도구를 제공한다.


## For-In 루프

`for`-`in` 루프는 배열의 항목, 숫자 범위, 문자열의 문자와 같은 시퀀스를 순회할 때 사용한다.

다음은 배열의 항목을 순회하는 `for`-`in` 루프 예제이다:

```swift
let names = ["Anna", "Alex", "Brian", "Jack"]
for name in names {
    print("Hello, \(name)!")
}
// Hello, Anna!
// Hello, Alex!
// Hello, Brian!
// Hello, Jack!
```

<!--
  - test: `forLoops`

  ```swifttest
  -> let names = ["Anna", "Alex", "Brian", "Jack"]
  -> for name in names {
        print("Hello, \(name)!")
     }
  </ Hello, Anna!
  </ Hello, Alex!
  </ Hello, Brian!
  </ Hello, Jack!
  ```
-->

딕셔너리를 순회하며 키-값 쌍에 접근할 수도 있다. 딕셔너리를 순회할 때 각 항목은 `(key, value)` 튜플로 반환되며, 이 튜플의 멤버를 명시적으로 이름을 붙인 상수로 분해하여 `for`-`in` 루프 내부에서 사용할 수 있다. 아래 코드 예제에서 딕셔너리의 키는 `animalName` 상수로, 값은 `legCount` 상수로 분해된다.

```swift
let numberOfLegs = ["spider": 8, "ant": 6, "cat": 4]
for (animalName, legCount) in numberOfLegs {
    print("\(animalName)s have \(legCount) legs")
}
// cats have 4 legs
// ants have 6 legs
// spiders have 8 legs
```

<!--
  - test: `forLoops`

  ```swifttest
  -> let numberOfLegs = ["spider": 8, "ant": 6, "cat": 4]
  -> for (animalName, legCount) in numberOfLegs {
        print("\(animalName)s have \(legCount) legs")
     }
  </ cats have 4 legs
  </ ants have 6 legs
  </ spiders have 8 legs
  ```
-->

딕셔너리의 내용은 본질적으로 순서가 없으며, 순회할 때 항목이 어떤 순서로 반환될지 보장되지 않는다. 특히, 딕셔너리에 항목을 추가한 순서가 순회 순서를 정의하지 않는다. 배열과 딕셔너리에 대한 자세한 내용은 <doc:CollectionTypes>를 참고한다.

숫자 범위와 함께 `for`-`in` 루프를 사용할 수도 있다. 다음은 5의 배수표의 처음 몇 항목을 출력하는 예제이다:

```swift
for index in 1...5 {
    print("\(index) times 5 is \(index * 5)")
}
// 1 times 5 is 5
// 2 times 5 is 10
// 3 times 5 is 15
// 4 times 5 is 20
// 5 times 5 is 25
```

<!--
  - test: `forLoops`

  ```swifttest
  -> for index in 1...5 {
        print("\(index) times 5 is \(index * 5)")
     }
  </ 1 times 5 is 5
  </ 2 times 5 is 10
  </ 3 times 5 is 15
  </ 4 times 5 is 20
  </ 5 times 5 is 25
  ```
-->

순회되는 시퀀스는 닫힌 범위 연산자(`...`)를 사용해 `1`부터 `5`까지의 숫자 범위이다. `index`의 값은 범위의 첫 번째 숫자(`1`)로 설정되고, 루프 내부의 문장이 실행된다. 이 경우 루프는 단 하나의 문장만 포함하며, 현재 `index` 값에 대한 5의 배수표 항목을 출력한다. 문장이 실행된 후, `index`의 값은 범위의 두 번째 값(`2`)으로 업데이트되고, `print(_:separator:terminator:)` 함수가 다시 호출된다. 이 과정은 범위의 끝에 도달할 때까지 계속된다.

위 예제에서 `index`는 루프의 각 반복이 시작될 때 자동으로 설정되는 상수이다. 따라서 `index`는 사용 전에 선언할 필요가 없다. 루프 선언에 포함되는 것만으로 암시적으로 선언되며, `let` 선언 키워드가 필요하지 않다.

시퀀스의 각 값이 필요하지 않다면, 변수 이름 대신 언더스코어(`_`)를 사용해 값을 무시할 수 있다.

```swift
let base = 3
let power = 10
var answer = 1
for _ in 1...power {
    answer *= base
}
print("\(base) to the power of \(power) is \(answer)")
// Prints "3 to the power of 10 is 59049"
```

<!--
  - test: `forLoops`

  ```swifttest
  -> let base = 3
  -> let power = 10
  -> var answer = 1
  -> for _ in 1...power {
        answer *= base
     }
  -> print("\(base) to the power of \(power) is \(answer)")
  <- 3 to the power of 10 is 59049
  ```
-->

위 예제는 한 숫자를 다른 숫자의 거듭제곱으로 계산한다(이 경우 `3`의 `10`제곱). 시작 값 `1`(즉, `3`의 `0`제곱)에 `3`을 10번 곱하며, `1`부터 `10`까지의 닫힌 범위를 사용한다. 이 계산에서는 루프를 돌 때마다 개별 카운터 값이 필요하지 않다. 코드는 단순히 루프를 정확한 횟수만큼 실행한다. 루프 변수 대신 사용된 언더스코어(`_`)는 개별 값을 무시하며, 루프의 각 반복에서 현재 값에 접근하지 않는다.

경우에 따라 양쪽 끝점을 모두 포함하는 닫힌 범위를 사용하고 싶지 않을 수 있다. 시계의 분침 눈금을 그리는 경우를 생각해보자. `0`분부터 시작해 `60`개의 눈금을 그려야 한다. 하한은 포함하지만 상한은 포함하지 않는 반열린 범위 연산자(`..<`)를 사용한다. 범위에 대한 자세한 내용은 <doc:BasicOperators#Range-Operators>를 참고한다.

```swift
let minutes = 60
for tickMark in 0..<minutes {
    // 분마다 눈금을 그린다 (60번)
}
```

<!--
  - test: `forLoops`

  ```swifttest
  -> let minutes = 60
  >> var result: [Int] = []
  -> for tickMark in 0..<minutes {
        // 분마다 눈금을 그린다 (60번)
  >>    result.append(tickMark)
     }
  >> print(result.first!, result.last!, result.count)
  << 0 59 60
  ```
-->

일부 사용자는 UI에 더 적은 눈금을 원할 수 있다. 예를 들어, 매 `5`분마다 하나의 눈금을 그리는 것을 선호할 수 있다. 원하지 않는 눈금을 건너뛰기 위해 `stride(from:to:by:)` 함수를 사용한다.

```swift
let minuteInterval = 5
for tickMark in stride(from: 0, to: minutes, by: minuteInterval) {
    // 5분마다 눈금을 그린다 (0, 5, 10, 15 ... 45, 50, 55)
}
```

<!--
  - test: `forLoops`

  ```swifttest
  -> let minuteInterval = 5
  >> result = []
  -> for tickMark in stride(from: 0, to: minutes, by: minuteInterval) {
        // 5분마다 눈금을 그린다 (0, 5, 10, 15 ... 45, 50, 55)
  >>      result.append(tickMark)
     }
  >> print(result.first!, result.last!, result.count)
  << 0 55 12
  ```
-->

닫힌 범위도 사용할 수 있으며, `stride(from:through:by:)`를 대신 사용한다:

```swift
let hours = 12
let hourInterval = 3
for tickMark in stride(from: 3, through: hours, by: hourInterval) {
    // 3시간마다 눈금을 그린다 (3, 6, 9, 12)
}
```

<!--
  - test: `forLoops`

  ```swifttest
  -> let hours = 12
  -> let hourInterval = 3
  -> for tickMark in stride(from: 3, through: hours, by: hourInterval) {
        // 3시간마다 눈금을 그린다 (3, 6, 9, 12)
  >>    print(tickMark)
     }
  << 3
  << 6
  << 9
  << 12
  ```
-->

위 예제들은 `for`-`in` 루프를 사용해 범위, 배열, 딕셔너리, 문자열을 순회하는 방법을 보여준다. 그러나 이 문법은 [`Sequence`](https://developer.apple.com/documentation/swift/sequence) 프로토콜을 준수하는 모든 컬렉션을 순회할 수 있으며, 사용자 정의 클래스와 컬렉션 타입도 포함된다.


## While 루프

`while` 루프는 특정 조건이 `false`가 될 때까지 일련의 명령문을 반복한다. 
이러한 루프는 반복 횟수를 처음 시작하기 전에 알 수 없는 경우에 가장 적합하다. 
Swift는 두 가지 종류의 `while` 루프를 제공한다:

- `while`은 각 루프를 시작할 때 조건을 평가한다.
- `repeat`-`while`은 각 루프를 끝낼 때 조건을 평가한다.


### While 반복문

`while` 반복문은 단일 조건을 평가하는 것으로 시작한다. 조건이 `true`일 경우, 조건이 `false`가 될 때까지 일련의 문장을 반복 실행한다.

`while` 반복문의 일반적인 형태는 다음과 같다:

```swift
while <#조건#> {
   <#문장#>
}
```

다음 예제는 *뱀과 사다리* 게임(또는 *미끄럼틀과 사다리*로도 알려진)을 간단히 구현한 것이다:

<!-- Apple Books 스크린샷 시작 -->

![](snakesAndLadders)

게임의 규칙은 다음과 같다:

- 게임판은 25개의 칸으로 이루어져 있으며, 목표는 25번 칸에 도달하거나 이를 넘어서는 것이다.
- 플레이어의 시작 칸은 "0번 칸"으로, 게임판의 왼쪽 아래 모서리 바로 바깥에 위치한다.
- 각 턴마다 6면체 주사위를 굴려 나온 숫자만큼 칸을 이동한다. 이동 경로는 위의 점선 화살표로 표시된 수평 경로를 따른다.
- 턴이 끝난 위치가 사다리의 하단이면, 해당 사다리를 타고 올라간다.
- 턴이 끝난 위치가 뱀의 머리면, 해당 뱀을 타고 내려간다.

게임판은 `Int` 값의 배열로 표현된다. 배열의 크기는 `finalSquare`라는 상수를 기반으로 하며, 이 상수는 배열을 초기화하고 나중에 승리 조건을 확인하는 데 사용된다. 플레이어가 게임판 바깥의 "0번 칸"에서 시작하기 때문에, 배열은 25가 아닌 26개의 `0`으로 초기화된다.

```swift
let finalSquare = 25
var board = [Int](repeating: 0, count: finalSquare + 1)
```

<!--
  - test: `snakesAndLadders1`

  ```swifttest
  -> let finalSquare = 25
  -> var board = [Int](repeating: 0, count: finalSquare + 1)
  >> assert(board == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
  ```
-->

일부 칸은 뱀과 사다리에 대해 더 구체적인 값을 갖도록 설정된다. 사다리의 하단에 해당하는 칸은 양수 값을 가지며, 이를 통해 게임판 위로 이동한다. 반면, 뱀의 머리에 해당하는 칸은 음수 값을 가지며, 이를 통해 게임판 아래로 이동한다.

```swift
board[03] = +08; board[06] = +11; board[09] = +09; board[10] = +02
board[14] = -10; board[19] = -11; board[22] = -02; board[24] = -08
```

<!--
  - test: `snakesAndLadders1`

  ```swifttest
  -> board[03] = +08; board[06] = +11; board[09] = +09; board[10] = +02
  -> board[14] = -10; board[19] = -11; board[22] = -02; board[24] = -08
  ```
-->

<!-- Apple Books 스크린샷 끝 -->

3번 칸은 사다리의 하단으로, 이를 통해 11번 칸으로 이동한다. 이를 표현하기 위해 `board[03]`은 `+08`로 설정되며, 이는 `8`의 정수 값(`3`과 `11`의 차이)과 동일하다. 값과 문장을 정렬하기 위해, 단항 플러스 연산자(`+i`)가 명시적으로 단항 마이너스 연산자(`-i`)와 함께 사용되며, `10`보다 작은 숫자는 0으로 패딩된다. (이러한 스타일 기법은 엄격히 필요하지 않지만, 코드를 더 깔끔하게 만든다.)

```swift
var square = 0
var diceRoll = 0
while square < finalSquare {
    // 주사위를 굴린다
    diceRoll += 1
    if diceRoll == 7 { diceRoll = 1 }
    // 주사위 값만큼 이동한다
    square += diceRoll
    if square < board.count {
        // 아직 게임판 위에 있다면, 뱀이나 사다리를 통해 이동한다
        square += board[square]
    }
}
print("Game over!")
```

<!--
  - test: `snakesAndLadders1`

  ```swifttest
  -> var square = 0
  -> var diceRoll = 0
  -> while square < finalSquare {
        // roll the dice
        diceRoll += 1
        if diceRoll == 7 { diceRoll = 1 }
  >>    print("diceRoll is \(diceRoll)")
        // move by the rolled amount
        square += diceRoll
  >>    print("after diceRoll, square is \(square)")
        if square < board.count {
           // if we're still on the board, move up or down for a snake or a ladder
           square += board[square]
  >>       print("after snakes or ladders, square is \(square)")
        }
     }
  -> print("Game over!")
  << diceRoll is 1
  << after diceRoll, square is 1
  << after snakes or ladders, square is 1
  << diceRoll is 2
  << after diceRoll, square is 3
  << after snakes or ladders, square is 11
  << diceRoll is 3
  << after diceRoll, square is 14
  << after snakes or ladders, square is 4
  << diceRoll is 4
  << after diceRoll, square is 8
  << after snakes or ladders, square is 8
  << diceRoll is 5
  << after diceRoll, square is 13
  << after snakes or ladders, square is 13
  << diceRoll is 6
  << after diceRoll, square is 19
  << after snakes or ladders, square is 8
  << diceRoll is 1
  << after diceRoll, square is 9
  << after snakes or ladders, square is 18
  << diceRoll is 2
  << after diceRoll, square is 20
  << after snakes or ladders, square is 20
  << diceRoll is 3
  << after diceRoll, square is 23
  << after snakes or ladders, square is 23
  << diceRoll is 4
  << after diceRoll, square is 27
  << Game over!
  ```
-->

위 예제는 주사위 굴리기를 매우 간단한 방식으로 처리한다. 랜덤 숫자를 생성하는 대신, `diceRoll` 값을 `0`으로 시작한다. `while` 반복문이 실행될 때마다 `diceRoll`은 1씩 증가하며, 너무 큰 값이 되었는지 확인한다. 이 반환 값이 `7`이 될 때마다, 주사위 값이 너무 커졌으므로 `1`로 재설정된다. 결과적으로 `diceRoll` 값은 항상 `1`, `2`, `3`, `4`, `5`, `6`, `1`, `2`와 같은 순서로 반복된다.

주사위를 굴린 후, 플레이어는 `diceRoll` 값만큼 앞으로 이동한다. 주사위 값이 플레이어를 25번 칸을 넘어서 이동시킬 수도 있으며, 이 경우 게임이 종료된다. 이 시나리오를 처리하기 위해, 코드는 `square`가 `board` 배열의 `count` 속성보다 작은지 확인한다. `square`가 유효하다면, `board[square]`에 저장된 값이 현재 `square` 값에 더해져 플레이어가 사다리나 뱀을 통해 이동한다.

> 참고: 이 확인을 수행하지 않으면, `board[square]`가 `board` 배열의 범위를 벗어난 값을 접근하려 할 수 있으며, 이는 런타임 오류를 발생시킬 수 있다.

현재 `while` 반복문의 실행이 끝나면, 반복문의 조건이 다시 확인되어 반복문을 계속 실행할지 결정한다. 플레이어가 25번 칸에 도달하거나 이를 넘어서면, 반복문의 조건이 `false`로 평가되어 게임이 종료된다.

이 경우 `while` 반복문이 적합하다. 왜냐하면 게임의 길이가 `while` 반복문 시작 시점에 명확하지 않기 때문이다. 대신, 특정 조건이 충족될 때까지 반복문이 실행된다.


### Repeat-While

`while` 루프의 다른 형태인 `repeat`-`while` 루프는  
루프 블록을 먼저 한 번 실행한 후에  
조건을 평가한다.  
그런 다음 조건이 `false`가 될 때까지 루프를 반복한다.

> 참고: Swift의 `repeat`-`while` 루프는  
> 다른 언어의 `do`-`while` 루프와 유사하다.

`repeat`-`while` 루프의 일반적인 형태는 다음과 같다:

```swift
repeat {
   <#statements#>
} while <#condition#>
```

다음은 *Snakes and Ladders* 예제를 `while` 루프 대신  
`repeat`-`while` 루프로 작성한 것이다.  
`finalSquare`, `board`, `square`, `diceRoll`의 값은  
`while` 루프와 동일한 방식으로 초기화된다.

```swift
let finalSquare = 25
var board = [Int](repeating: 0, count: finalSquare + 1)
board[03] = +08; board[06] = +11; board[09] = +09; board[10] = +02
board[14] = -10; board[19] = -11; board[22] = -02; board[24] = -08
var square = 0
var diceRoll = 0
```

<!--
  - test: `snakesAndLadders2`

  ```swifttest
  -> let finalSquare = 25
  -> var board = [Int](repeating: 0, count: finalSquare + 1)
  >> assert(board == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
  -> board[03] = +08; board[06] = +11; board[09] = +09; board[10] = +02
  -> board[14] = -10; board[19] = -11; board[22] = -02; board[24] = -08
  -> var square = 0
  -> var diceRoll = 0
  ```
-->

이 버전의 게임에서는 루프의 첫 번째 동작으로  
사다리나 뱀을 확인한다.  
보드에서 사다리를 타고 바로 25칸으로 이동할 수 없기 때문에  
사다리를 타고 게임에서 이길 수 없다.  
따라서 루프의 첫 번째 동작으로 뱀이나 사다리를 확인해도 안전하다.

게임 시작 시 플레이어는 "0번 칸"에 위치한다.  
`board[0]`은 항상 `0`이며 아무런 영향을 미치지 않는다.

```swift
repeat {
    // 뱀이나 사다리를 확인해 이동
    square += board[square]
    // 주사위를 굴림
    diceRoll += 1
    if diceRoll == 7 { diceRoll = 1 }
    // 주사위 결과만큼 이동
    square += diceRoll
} while square < finalSquare
print("Game over!")
```

<!--
  - test: `snakesAndLadders2`

  ```swifttest
  -> repeat {
        // move up or down for a snake or ladder
        square += board[square]
  >>      print("after snakes or ladders, square is \(square)")
        // roll the dice
        diceRoll += 1
        if diceRoll == 7 { diceRoll = 1 }
  >>    print("diceRoll is \(diceRoll)")
        // move by the rolled amount
        square += diceRoll
  >>    print("after diceRoll, square is \(square)")
  -> } while square < finalSquare
  -> print("Game over!")
  << after snakes or ladders, square is 0
  << diceRoll is 1
  << after diceRoll, square is 1
  << after snakes or ladders, square is 1
  << diceRoll is 2
  << after diceRoll, square is 3
  << after snakes or ladders, square is 11
  << diceRoll is 3
  << after diceRoll, square is 14
  << after snakes or ladders, square is 4
  << diceRoll is 4
  << after diceRoll, square is 8
  << after snakes or ladders, square is 8
  << diceRoll is 5
  << after diceRoll, square is 13
  << after snakes or ladders, square is 13
  << diceRoll is 6
  << after diceRoll, square is 19
  << after snakes or ladders, square is 8
  << diceRoll is 1
  << after diceRoll, square is 9
  << after snakes or ladders, square is 18
  << diceRoll is 2
  << after diceRoll, square is 20
  << after snakes or ladders, square is 20
  << diceRoll is 3
  << after diceRoll, square is 23
  << after snakes or ladders, square is 23
  << diceRoll is 4
  << after diceRoll, square is 27
  << Game over!
  ```
-->

뱀과 사다리를 확인한 후,  
주사위를 굴리고 플레이어를 `diceRoll`만큼 이동시킨다.  
그런 다음 현재 루프 실행이 종료된다.

루프의 조건(`while square < finalSquare`)은 이전과 동일하지만,  
이번에는 첫 번째 루프 실행이 끝난 후에 평가된다.  
`repeat`-`while` 루프의 구조는 이 게임에 더 적합하다.  
위의 `repeat`-`while` 루프에서  
`square += board[square]`는 루프의 `while` 조건이  
`square`가 여전히 보드 위에 있음을 확인한 후에 항상 즉시 실행된다.  
이 동작은 이전에 설명한 `while` 루프 버전에서 필요한  
배열 경계 확인을 제거한다.


## 조건문

특정 조건에 따라 서로 다른 코드를 실행하는 기능은 매우 유용하다. 오류 발생 시 추가 코드를 실행하거나, 값이 너무 높거나 낮을 때 메시지를 표시하는 등의 작업이 필요할 수 있다. 이를 위해 코드의 일부를 *조건부*로 작성한다.

Swift는 조건 분기를 추가하기 위해 두 가지 방법을 제공한다: `if` 문과 `switch` 문이다. 일반적으로 `if` 문은 가능한 결과가 몇 가지뿐인 간단한 조건을 평가할 때 사용한다. `switch` 문은 여러 가능성과 복잡한 조건에 더 적합하며, 패턴 매칭을 통해 실행할 적절한 코드 분기를 선택할 때 유용하다.


### If

가장 간단한 형태의 `if` 문은 단일 조건을 가진다. 이 조건이 `true`일 때만 특정 문장을 실행한다.

```swift
var temperatureInFahrenheit = 30
if temperatureInFahrenheit <= 32 {
    print("It's very cold. Consider wearing a scarf.")
}
// Prints "It's very cold. Consider wearing a scarf."
```

<!--
  - test: `ifElse`

  ```swifttest
  -> var temperatureInFahrenheit = 30
  -> if temperatureInFahrenheit <= 32 {
        print("It's very cold. Consider wearing a scarf.")
     }
  <- It's very cold. Consider wearing a scarf.
  ```
-->

위 예제는 온도가 32도 화씨(물의 어는점) 이하인지 확인한다. 만약 그렇다면 메시지를 출력한다. 그렇지 않으면 메시지를 출력하지 않고 `if` 문의 닫는 중괄호 이후로 코드 실행이 계속된다.

`if` 문은 `if` 조건이 `false`일 때 실행할 대체 문장을 제공할 수 있다. 이를 *else 절*이라고 하며, `else` 키워드로 표시한다.

```swift
temperatureInFahrenheit = 40
if temperatureInFahrenheit <= 32 {
    print("It's very cold. Consider wearing a scarf.")
} else {
    print("It's not that cold. Wear a T-shirt.")
}
// Prints "It's not that cold. Wear a T-shirt."
```

<!--
  - test: `ifElse`

  ```swifttest
  -> temperatureInFahrenheit = 40
  -> if temperatureInFahrenheit <= 32 {
        print("It's very cold. Consider wearing a scarf.")
     } else {
        print("It's not that cold. Wear a T-shirt.")
     }
  <- It's not that cold. Wear a T-shirt.
  ```
-->

이 두 가지 중 하나는 항상 실행된다. 온도가 40도 화씨로 올라가면 스카프를 권장할 만큼 춥지 않으므로 `else` 절이 실행된다.

여러 `if` 문을 연결하여 추가 조건을 고려할 수 있다.

```swift
temperatureInFahrenheit = 90
if temperatureInFahrenheit <= 32 {
    print("It's very cold. Consider wearing a scarf.")
} else if temperatureInFahrenheit >= 86 {
    print("It's really warm. Don't forget to wear sunscreen.")
} else {
    print("It's not that cold. Wear a T-shirt.")
}
// Prints "It's really warm. Don't forget to wear sunscreen."
```

<!--
  - test: `ifElse`

  ```swifttest
  -> temperatureInFahrenheit = 90
  -> if temperatureInFahrenheit <= 32 {
        print("It's very cold. Consider wearing a scarf.")
     } else if temperatureInFahrenheit >= 86 {
        print("It's really warm. Don't forget to wear sunscreen.")
     } else {
        print("It's not that cold. Wear a T-shirt.")
     }
  <- It's really warm. Don't forget to wear sunscreen.
  ```
-->

여기서는 특히 따뜻한 온도에 대응하기 위해 추가 `if` 문을 넣었다. 마지막 `else` 절은 남아 있으며, 너무 춥거나 덥지 않은 온도에 대한 응답을 출력한다.

그러나 마지막 `else` 절은 선택 사항이며, 조건 집합이 완전할 필요가 없는 경우 생략할 수 있다.

```swift
temperatureInFahrenheit = 72
if temperatureInFahrenheit <= 32 {
    print("It's very cold. Consider wearing a scarf.")
} else if temperatureInFahrenheit >= 86 {
    print("It's really warm. Don't forget to wear sunscreen.")
}
```

<!--
  - test: `ifElse`

  ```swifttest
  -> temperatureInFahrenheit = 72
  -> if temperatureInFahrenheit <= 32 {
        print("It's very cold. Consider wearing a scarf.")
     } else if temperatureInFahrenheit >= 86 {
        print("It's really warm. Don't forget to wear sunscreen.")
     }
  ```
-->

온도가 `if` 조건을 트리거할 만큼 춥지도 않고 `else if` 조건을 트리거할 만큼 따뜻하지도 않으므로 메시지가 출력되지 않는다.

Swift는 값을 설정할 때 사용할 수 있는 `if`의 간단한 표현을 제공한다. 예를 들어, 다음 코드를 살펴보자:

```swift
let temperatureInCelsius = 25
let weatherAdvice: String

if temperatureInCelsius <= 0 {
    weatherAdvice = "It's very cold. Consider wearing a scarf."
} else if temperatureInCelsius >= 30 {
    weatherAdvice = "It's really warm. Don't forget to wear sunscreen."
} else {
    weatherAdvice = "It's not that cold. Wear a T-shirt."
}

print(weatherAdvice)
// Prints "It's not that cold. Wear a T-shirt."
```

여기서 각 분기는 `weatherAdvice` 상수에 값을 설정하며, `if` 문 이후에 이를 출력한다.

`if` 표현식이라고 하는 대체 구문을 사용하면 이 코드를 더 간결하게 작성할 수 있다:

```swift
let weatherAdvice = if temperatureInCelsius <= 0 {
    "It's very cold. Consider wearing a scarf."
} else if temperatureInCelsius >= 30 {
    "It's really warm. Don't forget to wear sunscreen."
} else {
    "It's not that cold. Wear a T-shirt."
}

print(weatherAdvice)
// Prints "It's not that cold. Wear a T-shirt."
```

이 `if` 표현식 버전에서 각 분기는 단일 값을 포함한다. 분기의 조건이 `true`이면 해당 분기의 값이 `weatherAdvice` 할당을 위한 전체 `if` 표현식의 값으로 사용된다. 모든 `if` 분기에는 해당하는 `else if` 분기나 `else` 분기가 있어, 항상 하나의 분기가 일치하도록 보장하며, `if` 표현식이 항상 값을 생성하도록 한다.

할당 구문이 `if` 표현식 외부에서 시작하기 때문에 각 분기 내부에서 `weatherAdvice =`를 반복할 필요가 없다. 대신, `if` 표현식의 각 분기가 `weatherAdvice`의 세 가지 가능한 값 중 하나를 생성하며, 할당은 그 값을 사용한다.

`if` 표현식의 모든 분기는 동일한 타입의 값을 포함해야 한다. Swift는 각 분기의 타입을 개별적으로 확인하므로, `nil`과 같이 여러 타입과 함께 사용할 수 있는 값은 Swift가 `if` 표현식의 타입을 자동으로 결정하는 것을 방해한다. 대신, 타입을 명시적으로 지정해야 한다. 예를 들면:

```swift
let freezeWarning: String? = if temperatureInCelsius <= 0 {
    "It's below freezing. Watch for ice!"
} else {
    nil
}
```

위 코드에서 `if` 표현식의 한 분기는 문자열 값을 가지고 다른 분기는 `nil` 값을 가진다. `nil` 값은 모든 옵셔널 타입의 값으로 사용할 수 있으므로, `freezeWarning`이 옵셔널 문자열임을 명시적으로 작성해야 한다. 이는 <doc:TheBasics#Type-Annotations>에서 설명한 바와 같다.

이 타입 정보를 제공하는 또 다른 방법은 `freezeWarning`에 명시적 타입을 제공하는 대신, `nil`에 명시적 타입을 제공하는 것이다:

```swift
let freezeWarning = if temperatureInCelsius <= 0 {
    "It's below freezing. Watch for ice!"
} else {
    nil as String?
}
```

`if` 표현식은 예기치 않은 실패에 대해 에러를 던지거나 `fatalError(_:file:line:)`과 같이 절대 반환하지 않는 함수를 호출함으로써 대응할 수 있다. 예를 들어:

```swift
let weatherAdvice = if temperatureInCelsius > 100 {
    throw TemperatureError.boiling
} else {
    "It's a reasonable temperature."
}
```

이 예제에서 `if` 표현식은 예측된 온도가 100°C(물의 끓는점)보다 높은지 확인한다. 이렇게 뜨거운 온도는 텍스트 요약을 반환하는 대신 `.boiling` 에러를 던지도록 한다. 이 `if` 표현식이 에러를 던질 수 있음에도 불구하고, 앞에 `try`를 작성할 필요는 없다. 에러 처리에 대한 자세한 내용은 <doc:ErrorHandling>을 참조하라.

위 예제에서 보여준 것처럼 할당의 오른쪽에서 `if` 표현식을 사용하는 것 외에도, 함수나 클로저가 반환하는 값으로도 사용할 수 있다.


### Switch

`switch` 문은 특정 값을 고려하여 여러 가능한 패턴과 비교한다. 그리고 첫 번째로 일치하는 패턴에 따라 적절한 코드 블록을 실행한다. `switch` 문은 여러 잠재적 상태에 대응하기 위해 `if` 문의 대안으로 사용할 수 있다.

가장 간단한 형태의 `switch` 문은 하나의 값을 동일한 타입의 하나 이상의 값과 비교한다.

```swift
switch <#고려할 값#> {
case <#값 1#>:
    <#값 1에 대응하는 코드#>
case <#값 2#>,
    <#값 3#>:
    <#값 2 또는 3에 대응하는 코드#>
default:
    <#그 외의 경우 실행할 코드#>
}
```

모든 `switch` 문은 여러 개의 가능한 *케이스*로 구성되며, 각 케이스는 `case` 키워드로 시작한다. Swift는 특정 값과 비교하는 것 외에도, 각 케이스에서 더 복잡한 매칭 패턴을 지정할 수 있는 여러 방법을 제공한다. 이러한 옵션은 이 장의 후반부에서 설명한다.

`if` 문의 본문과 마찬가지로, 각 `case`는 별도의 코드 실행 분기이다. `switch` 문은 어떤 분기를 선택할지 결정한다. 이 과정은 고려 중인 값에 대해 *스위칭*한다고 표현한다.

모든 `switch` 문은 *완전해야 한다*. 즉, 고려 중인 타입의 모든 가능한 값이 `switch`의 케이스 중 하나와 일치해야 한다. 모든 가능한 값에 대해 케이스를 제공하는 것이 적절하지 않은 경우, 명시적으로 처리되지 않은 모든 값을 다루기 위해 기본 케이스를 정의할 수 있다. 이 기본 케이스는 `default` 키워드로 표시되며, 항상 마지막에 위치해야 한다.

다음 예제는 `someCharacter`라는 단일 소문자 문자를 고려하기 위해 `switch` 문을 사용한다:

```swift
let someCharacter: Character = "z"
switch someCharacter {
case "a":
    print("라틴 알파벳의 첫 번째 문자")
case "z":
    print("라틴 알파벳의 마지막 문자")
default:
    print("다른 문자")
}
// "라틴 알파벳의 마지막 문자"를 출력
```

<!--
  - test: `switch`

  ```swifttest
  -> let someCharacter: Character = "z"
  -> switch someCharacter {
        case "a":
           print("라틴 알파벳의 첫 번째 문자")
        case "z":
           print("라틴 알파벳의 마지막 문자")
        default:
           print("다른 문자")
     }
  <- 라틴 알파벳의 마지막 문자
  ```
-->

`switch` 문의 첫 번째 케이스는 영어 알파벳의 첫 번째 문자인 `a`와 일치하고, 두 번째 케이스는 마지막 문자인 `z`와 일치한다. `switch`는 모든 알파벳 문자뿐만 아니라 모든 가능한 문자에 대해 케이스가 있어야 하므로, 이 `switch` 문은 `a`와 `z`를 제외한 모든 문자와 일치시키기 위해 `default` 케이스를 사용한다. 이 조치는 `switch` 문이 완전하도록 보장한다.

`if` 문과 마찬가지로, `switch` 문도 표현식 형태를 가질 수 있다:

```swift
let anotherCharacter: Character = "a"
let message = switch anotherCharacter {
case "a":
    "라틴 알파벳의 첫 번째 문자"
case "z":
    "라틴 알파벳의 마지막 문자"
default:
    "다른 문자"
}

print(message)
// "라틴 알파벳의 첫 번째 문자"를 출력
```

이 예제에서, `switch` 표현식의 각 케이스는 `anotherCharacter`와 일치할 때 사용할 `message`의 값을 포함한다. `switch`는 항상 완전해야 하므로, 항상 할당할 값이 존재한다.

`if` 표현식과 마찬가지로, 특정 케이스에 대한 값을 제공하는 대신 오류를 던지거나 `fatalError(_:file:line:)`와 같이 반환하지 않는 함수를 호출할 수 있다. `switch` 표현식은 위 예제와 같이 할당의 오른쪽에 사용할 수 있으며, 함수나 클로저가 반환하는 값으로도 사용할 수 있다.


#### 암시적 폴스루 없음

C와 Objective-C의 `switch` 문과 달리,  
Swift의 `switch` 문은 기본적으로 한 케이스에서 다음 케이스로 넘어가지 않는다.  
대신, 첫 번째로 일치하는 `switch` 케이스가 실행된 후 전체 `switch` 문이 종료된다.  
이때 명시적인 `break` 문이 필요하지 않다.  
이러한 방식은 C의 `switch` 문보다 더 안전하고 사용하기 쉬우며,  
실수로 여러 케이스가 실행되는 것을 방지한다.

> 참고: Swift에서는 `break` 문이 필수는 아니지만,  
> 특정 케이스를 일치시킨 후 무시하거나,  
> 케이스 실행이 완료되기 전에 빠져나오기 위해 `break` 문을 사용할 수 있다.  
> 자세한 내용은 <doc:ControlFlow#Break-in-a-Switch-Statement>를 참고하라.

각 케이스의 본문에는 반드시 최소 하나의 실행 가능한 문장이 포함되어야 한다.  
다음 코드는 첫 번째 케이스가 비어 있기 때문에 유효하지 않다:

```swift
let anotherCharacter: Character = "a"
switch anotherCharacter {
case "a": // 유효하지 않음, 케이스 본문이 비어 있음
case "A":
    print("The letter A")
default:
    print("Not the letter A")
}
// 이 코드는 컴파일 타임 오류를 발생시킨다.
```

C의 `switch` 문과 달리,  
이 `switch` 문은 `"a"`와 `"A"`를 동시에 일치시키지 않는다.  
대신, `case "a":`에 실행 가능한 문장이 없다는 컴파일 타임 오류를 발생시킨다.  
이러한 접근 방식은 한 케이스에서 다른 케이스로의 의도치 않은 폴스루를 방지하고,  
코드의 의도를 더 명확하게 만든다.

`"a"`와 `"A"`를 모두 일치시키는 단일 케이스를 만들려면,  
두 값을 콤마로 구분하여 복합 케이스로 결합하면 된다.

```swift
let anotherCharacter: Character = "a"
switch anotherCharacter {
case "a", "A":
    print("The letter A")
default:
    print("Not the letter A")
}
// "The letter A"를 출력한다.
```

가독성을 위해 복합 케이스를 여러 줄에 걸쳐 작성할 수도 있다.  
복합 케이스에 대한 자세한 내용은 <doc:ControlFlow#Compound-Cases>를 참고하라.

> 참고: 특정 `switch` 케이스의 끝에서 명시적으로 폴스루를 하려면,  
> `fallthrough` 키워드를 사용하면 된다.  
> 자세한 내용은 <doc:ControlFlow#Fallthrough>를 참고하라.


#### 구간 매칭

`switch` 문의 각 `case`에서 값이 특정 구간에 포함되는지 확인할 수 있다. 다음 예제는 숫자 구간을 사용해 크기에 상관없이 숫자를 자연어로 표현하는 방법을 보여준다:

<!--
  REFERENCE
  토성은 확인된 궤도를 가진 62개의 위성을 가지고 있다.
-->

```swift
let approximateCount = 62
let countedThings = "moons orbiting Saturn"
let naturalCount: String
switch approximateCount {
case 0:
    naturalCount = "no"
case 1..<5:
    naturalCount = "a few"
case 5..<12:
    naturalCount = "several"
case 12..<100:
    naturalCount = "dozens of"
case 100..<1000:
    naturalCount = "hundreds of"
default:
    naturalCount = "many"
}
print("There are \(naturalCount) \(countedThings).")
// Prints "There are dozens of moons orbiting Saturn."
```

<!--
  - test: `intervalMatching`

  ```swifttest
  -> let approximateCount = 62
  -> let countedThings = "moons orbiting Saturn"
  -> let naturalCount: String
  -> switch approximateCount {
     case 0:
         naturalCount = "no"
     case 1..<5:
         naturalCount = "a few"
     case 5..<12:
         naturalCount = "several"
     case 12..<100:
         naturalCount = "dozens of"
     case 100..<1000:
         naturalCount = "hundreds of"
     default:
         naturalCount = "many"
     }
  -> print("There are \(naturalCount) \(countedThings).")
  <- There are dozens of moons orbiting Saturn.
  ```
-->

위 예제에서 `approximateCount`는 `switch` 문에서 평가된다. 각 `case`는 이 값을 숫자나 구간과 비교한다. `approximateCount`의 값이 12에서 100 사이에 속하기 때문에 `naturalCount`에는 `"dozens of"`가 할당되고, `switch` 문의 실행이 종료된다.


#### 튜플

튜플을 사용하면 하나의 `switch` 문에서 여러 값을 테스트할 수 있다. 튜플의 각 요소는 서로 다른 값이나 값의 범위와 비교할 수 있다. 또는 와일드카드 패턴으로 알려진 언더스코어 문자(`_`)를 사용해 모든 가능한 값과 일치시킬 수도 있다.

아래 예제는 `(Int, Int)` 타입의 간단한 튜플로 표현된 (x, y) 좌표를 받아 그래프 상에서 해당 점을 분류한다.

```swift
let somePoint = (1, 1)
switch somePoint {
case (0, 0):
    print("\(somePoint) is at the origin")
case (_, 0):
    print("\(somePoint) is on the x-axis")
case (0, _):
    print("\(somePoint) is on the y-axis")
case (-2...2, -2...2):
    print("\(somePoint) is inside the box")
default:
    print("\(somePoint) is outside of the box")
}
// Prints "(1, 1) is inside the box"
```

<!--
  - test: `tuples`

  ```swifttest
  -> let somePoint = (1, 1)
  -> switch somePoint {
        case (0, 0):
           print("\(somePoint) is at the origin")
        case (_, 0):
           print("\(somePoint) is on the x-axis")
        case (0, _):
           print("\(somePoint) is on the y-axis")
        case (-2...2, -2...2):
           print("\(somePoint) is inside the box")
        default:
           print("\(somePoint) is outside of the box")
     }
  <- (1, 1) is inside the box
  ```
-->

![](coordinateGraphSimple)

이 `switch` 문은 해당 점이 원점 (0, 0)에 있는지, 빨간색 x축 위에 있는지, 초록색 y축 위에 있는지, 원점을 중심으로 한 파란색 4x4 박스 안에 있는지, 아니면 박스 밖에 있는지를 판단한다.

C 언어와 달리 Swift는 여러 `switch` 케이스가 동일한 값을 고려하도록 허용한다. 사실 이 예제에서 점 (0, 0)은 네 가지 케이스 모두와 일치할 수 있다. 그러나 여러 케이스가 일치할 가능성이 있으면 항상 첫 번째로 일치하는 케이스가 사용된다. 따라서 점 (0, 0)은 `case (0, 0)`와 먼저 일치하며, 나머지 일치하는 케이스는 무시된다.


#### 값 바인딩

`switch` 케이스는 매칭되는 값을 임시 상수나 변수에 할당할 수 있다. 이렇게 하면 케이스 본문에서 해당 값을 사용할 수 있다. 이 동작을 *값 바인딩*이라고 부르며, 케이스 본문 내에서 임시 상수나 변수에 값이 바인딩된다.

아래 예제는 `(Int, Int)` 타입의 튜플로 표현된 (x, y) 좌표를 받아 그래프 상에서 분류한다:

```swift
let anotherPoint = (2, 0)
switch anotherPoint {
case (let x, 0):
    print("x축 위에 있으며 x 값은 \(x)입니다.")
case (0, let y):
    print("y축 위에 있으며 y 값은 \(y)입니다.")
case let (x, y):
    print("다른 위치에 있으며 좌표는 (\(x), \(y))입니다.")
}
// "x축 위에 있으며 x 값은 2입니다." 출력
```

<!--
  - test: `valueBindings`

  ```swifttest
  -> let anotherPoint = (2, 0)
  -> switch anotherPoint {
        case (let x, 0):
           print("on the x-axis with an x value of \(x)")
        case (0, let y):
           print("on the y-axis with a y value of \(y)")
        case let (x, y):
           print("somewhere else at (\(x), \(y))")
     }
  <- on the x-axis with an x value of 2
  ```
-->

![](coordinateGraphMedium)

이 `switch` 문은 점이 빨간색 x축 위에 있는지, 초록색 y축 위에 있는지, 아니면 다른 위치에 있는지 판단한다.

세 `switch` 케이스는 플레이스홀더 상수 `x`와 `y`를 선언하며, 이 상수는 `anotherPoint`의 튜플 값을 임시로 받는다. 첫 번째 케이스인 `case (let x, 0)`는 `y` 값이 `0`인 모든 점에 매칭되며, 점의 `x` 값을 임시 상수 `x`에 할당한다. 마찬가지로 두 번째 케이스인 `case (0, let y)`는 `x` 값이 `0`인 모든 점에 매칭되며, 점의 `y` 값을 임시 상수 `y`에 할당한다.

임시 상수가 선언되면, 해당 케이스의 코드 블록 내에서 사용할 수 있다. 여기서는 점의 위치를 분류해 출력하는 데 사용된다.

이 `switch` 문에는 `default` 케이스가 없다. 마지막 케이스인 `case let (x, y)`는 모든 값에 매칭될 수 있는 두 개의 플레이스홀더 상수를 선언한다. `anotherPoint`는 항상 두 개의 값으로 이루어진 튜플이기 때문에, 이 케이스는 모든 가능한 나머지 값에 매칭된다. 따라서 `switch` 문이 모든 경우를 커버하기 위해 `default` 케이스가 필요하지 않다.


#### Where

`switch` 케이스는 추가 조건을 확인하기 위해 `where` 절을 사용할 수 있다.

아래 예제는 (x, y) 점을 그래프 상에서 다음과 같이 분류한다:

```swift
let yetAnotherPoint = (1, -1)
switch yetAnotherPoint {
case let (x, y) where x == y:
    print("(\(x), \(y)) is on the line x == y")
case let (x, y) where x == -y:
    print("(\(x), \(y)) is on the line x == -y")
case let (x, y):
    print("(\(x), \(y)) is just some arbitrary point")
}
// Prints "(1, -1) is on the line x == -y"
```

<!--
  - test: `where`

  ```swifttest
  -> let yetAnotherPoint = (1, -1)
  -> switch yetAnotherPoint {
        case let (x, y) where x == y:
           print("(\(x), \(y)) is on the line x == y")
        case let (x, y) where x == -y:
           print("(\(x), \(y)) is on the line x == -y")
        case let (x, y):
           print("(\(x), \(y)) is just some arbitrary point")
     }
  <- (1, -1) is on the line x == -y
  ```
-->

![](coordinateGraphComplex)

`switch` 문은 점이 `x == y`인 초록색 대각선 위에 있는지, `x == -y`인 보라색 대각선 위에 있는지, 아니면 둘 다 아닌지를 판단한다.

세 개의 `switch` 케이스는 `yetAnotherPoint`의 두 튜플 값을 임시로 받는 `x`와 `y`라는 상수를 선언한다. 이 상수들은 동적 필터를 생성하기 위해 `where` 절의 일부로 사용된다. `switch` 케이스는 `where` 절의 조건이 해당 값에 대해 `true`로 평가될 때만 현재 `point` 값과 일치한다.

이전 예제와 마찬가지로, 마지막 케이스는 가능한 모든 나머지 값과 일치하므로 `switch` 문을 완전히 만들기 위해 `default` 케이스가 필요하지 않다.


#### 복합 케이스

동일한 본문을 공유하는 여러 `switch` 케이스는 `case` 뒤에 여러 패턴을 쉼표로 구분하여 결합할 수 있다. 패턴 중 하나라도 일치하면 해당 케이스가 일치한 것으로 간주한다. 패턴 목록이 길 경우 여러 줄에 걸쳐 작성할 수도 있다. 예를 들어:

```swift
let someCharacter: Character = "e"
switch someCharacter {
case "a", "e", "i", "o", "u":
    print("\(someCharacter) is a vowel")
case "b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
    "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z":
    print("\(someCharacter) is a consonant")
default:
    print("\(someCharacter) isn't a vowel or a consonant")
}
// Prints "e is a vowel"
```

<!--
  - test: `compound-switch-case`

  ```swifttest
  -> let someCharacter: Character = "e"
  -> switch someCharacter {
         case "a", "e", "i", "o", "u":
             print("\(someCharacter) is a vowel")
         case "b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
             "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z":
             print("\(someCharacter) is a consonant")
         default:
             print("\(someCharacter) isn't a vowel or a consonant")
     }
  <- e is a vowel
  ```
-->

위 `switch` 문의 첫 번째 케이스는 영어의 다섯 개 소문자 모음을 모두 매칭한다. 마찬가지로 두 번째 케이스는 영어 소문자 자음을 모두 매칭한다. 마지막으로 `default` 케이스는 그 외의 문자를 매칭한다.

복합 케이스는 값 바인딩도 포함할 수 있다. 복합 케이스의 모든 패턴은 동일한 값 바인딩 집합을 포함해야 하며, 각 바인딩은 복합 케이스의 모든 패턴에서 동일한 타입의 값을 가져와야 한다. 이를 통해 복합 케이스의 어느 부분이 일치하든 상관없이 케이스 본문의 코드가 항상 바인딩된 값에 접근할 수 있고, 그 값의 타입도 항상 동일하게 유지된다.

```swift
let stillAnotherPoint = (9, 0)
switch stillAnotherPoint {
case (let distance, 0), (0, let distance):
    print("On an axis, \(distance) from the origin")
default:
    print("Not on an axis")
}
// Prints "On an axis, 9 from the origin"
```

<!--
  - test: `compound-switch-case`

  ```swifttest
  -> let stillAnotherPoint = (9, 0)
  -> switch stillAnotherPoint {
         case (let distance, 0), (0, let distance):
             print("On an axis, \(distance) from the origin")
         default:
             print("Not on an axis")
     }
  <- On an axis, 9 from the origin
  ```
-->

위 `case`는 두 가지 패턴을 가진다: `(let distance, 0)`는 x축 상의 점을 매칭하고, `(0, let distance)`는 y축 상의 점을 매칭한다. 두 패턴 모두 `distance`에 대한 바인딩을 포함하며, `distance`는 두 패턴 모두 정수 타입이다. 따라서 `case` 본문의 코드는 항상 `distance`의 값에 접근할 수 있다.


## 제어 흐름 변경문

*제어 흐름 변경문*은 코드의 실행 순서를 변경하며, 특정 코드에서 다른 코드로 제어를 넘기는 역할을 한다. Swift는 다섯 가지 제어 흐름 변경문을 제공한다:

- `continue`
- `break`
- `fallthrough`
- `return`
- `throw`

이 중 `continue`, `break`, `fallthrough`는 아래에서 설명한다. `return` 문은 <doc:Functions>에서, `throw` 문은 <doc:ErrorHandling#Propagating-Errors-Using-Throwing-Functions>에서 자세히 다룬다.


`continue` 문은 루프가 현재 작업을 멈추고 다음 반복의 시작 부분으로 바로 이동하도록 지시한다. 이는 "현재 루프 반복을 마쳤다"는 의미를 전달하면서도 루프를 완전히 빠져나가지 않는다.

다음 예제는 소문자 문자열에서 모든 모음과 공백을 제거하여 암호화된 퍼즐 문구를 만든다:

```swift
let puzzleInput = "great minds think alike"
var puzzleOutput = ""
let charactersToRemove: [Character] = ["a", "e", "i", "o", "u", " "]
for character in puzzleInput {
    if charactersToRemove.contains(character) {
        continue
    }
    puzzleOutput.append(character)
}
print(puzzleOutput)
// Prints "grtmndsthnklk"
```

<!--
  - test: `continue`

  ```swifttest
  -> let puzzleInput = "great minds think alike"
  -> var puzzleOutput = ""
  -> let charactersToRemove: [Character] = ["a", "e", "i", "o", "u", " "]
  -> for character in puzzleInput {
        if charactersToRemove.contains(character) {
           continue
        }
        puzzleOutput.append(character)
     }
  -> print(puzzleOutput)
  <- grtmndsthnklk
  ```
-->

위 코드는 모음이나 공백이 발견될 때마다 `continue` 키워드를 호출한다. 이를 통해 현재 루프 반복을 즉시 종료하고 다음 반복의 시작 부분으로 바로 이동한다.


### break 문

`break` 문은 현재 실행 중인 제어 흐름문의 실행을 즉시 종료한다.  
`switch` 문이나 반복문 안에서 `break` 문을 사용하면,  
해당 `switch` 문이나 반복문의 실행을 원래보다 더 일찍 중단할 수 있다.


#### 반복문에서의 break 사용

반복문 안에서 `break`를 사용하면, 반복문의 실행이 즉시 종료되고, 반복문을 닫는 중괄호(`}`) 이후의 코드로 제어권이 넘어간다. 현재 반복 중인 코드는 더 이상 실행되지 않으며, 반복문의 다음 반복도 시작되지 않는다.

<!--
  TODO: 여기에 예제를 추가해야 합니다.
-->


#### Switch 문에서의 Break 사용

`switch` 문 내부에서 `break`를 사용하면, `switch` 문의 실행이 즉시 종료되고, `switch` 문의 닫는 중괄호(`}`) 이후의 코드로 제어가 이동한다.

이 동작은 `switch` 문에서 하나 이상의 케이스를 일치시켜 무시할 때 유용하다. Swift의 `switch` 문은 모든 가능성을 커버해야 하며, 빈 케이스를 허용하지 않기 때문에, 의도를 명확히 하기 위해 특정 케이스를 일치시켜 무시해야 할 때가 있다. 이때 해당 케이스의 본문 전체를 `break` 문으로 작성하면 된다. `switch` 문에서 해당 케이스가 일치하면, 케이스 내부의 `break` 문이 `switch` 문의 실행을 즉시 종료한다.

> 참고: 주석만 포함된 `switch` 케이스는 컴파일 시간 오류로 처리된다. 주석은 문장이 아니므로 `switch` 케이스를 무시하게 하지 않는다. `switch` 케이스를 무시하려면 항상 `break` 문을 사용해야 한다.

다음 예제는 `Character` 값에 대해 `switch` 문을 사용하여, 해당 문자가 네 가지 언어 중 하나의 숫자 기호인지 판단한다. 간결성을 위해 여러 값을 하나의 `switch` 케이스에서 처리한다.

```swift
let numberSymbol: Character = "三"  // 숫자 3을 나타내는 중국어 기호
var possibleIntegerValue: Int?
switch numberSymbol {
case "1", "١", "一", "๑":
    possibleIntegerValue = 1
case "2", "٢", "二", "๒":
    possibleIntegerValue = 2
case "3", "٣", "三", "๓":
    possibleIntegerValue = 3
case "4", "٤", "四", "๔":
    possibleIntegerValue = 4
default:
    break
}
if let integerValue = possibleIntegerValue {
    print("The integer value of \(numberSymbol) is \(integerValue).")
} else {
    print("An integer value couldn't be found for \(numberSymbol).")
}
// Prints "The integer value of 三 is 3."
```

<!--
  - test: `breakInASwitchStatement`

  ```swifttest
  -> let numberSymbol: Character = "三"  // Chinese symbol for the number 3
  -> var possibleIntegerValue: Int?
  -> switch numberSymbol {
        case "1", "١", "一", "๑":
           possibleIntegerValue = 1
        case "2", "٢", "二", "๒":
           possibleIntegerValue = 2
        case "3", "٣", "三", "๓":
           possibleIntegerValue = 3
        case "4", "٤", "四", "๔":
           possibleIntegerValue = 4
        default:
           break
     }
  -> if let integerValue = possibleIntegerValue {
        print("The integer value of \(numberSymbol) is \(integerValue).")
     } else {
        print("An integer value couldn't be found for \(numberSymbol).")
     }
  <- The integer value of 三 is 3.
  ```
-->

이 예제는 `numberSymbol`이 라틴어, 아랍어, 중국어, 태국어 중 하나의 숫자 `1`부터 `4`를 나타내는 기호인지 확인한다. 일치하는 경우, `switch` 문의 케이스 중 하나가 `possibleIntegerValue`라는 옵셔널 `Int?` 변수에 적절한 정수 값을 할당한다.

`switch` 문의 실행이 완료된 후, 이 예제는 옵셔널 바인딩을 사용하여 값이 발견되었는지 확인한다. `possibleIntegerValue` 변수는 옵셔널 타입이기 때문에 암시적으로 `nil`로 초기화되며, 따라서 옵셔널 바인딩은 `possibleIntegerValue`가 `switch` 문의 처음 네 케이스 중 하나에 의해 실제 값으로 설정된 경우에만 성공한다.

위 예제에서 모든 가능한 `Character` 값을 나열하는 것은 실용적이지 않기 때문에, `default` 케이스는 일치하지 않는 모든 문자를 처리한다. 이 `default` 케이스는 어떤 동작도 수행할 필요가 없으므로, 본문을 `break` 문 하나로 작성한다. `default` 케이스가 일치하면, `break` 문이 `switch` 문의 실행을 즉시 종료하고, `if let` 문 이후의 코드 실행이 계속된다.


### Fallthrough

Swift에서 `switch` 문은 각 case의 끝에서 다음 case로 넘어가지 않는다. 즉, 첫 번째로 일치하는 case가 실행되면 전체 `switch` 문의 실행이 완료된다. 반면 C에서는 `switch` case의 끝에 명시적으로 `break` 문을 추가해야 fallthrough를 방지할 수 있다. Swift는 기본적으로 fallthrough를 허용하지 않기 때문에 `switch` 문이 더 간결하고 예측 가능하며, 실수로 여러 case가 실행되는 것을 방지할 수 있다.

C 스타일의 fallthrough 동작이 필요하다면, `fallthrough` 키워드를 사용해 case별로 이 동작을 선택할 수 있다. 아래 예제는 `fallthrough`를 사용해 숫자에 대한 설명을 생성한다.

```swift
let integerToDescribe = 5
var description = "The number \(integerToDescribe) is"
switch integerToDescribe {
case 2, 3, 5, 7, 11, 13, 17, 19:
    description += " a prime number, and also"
    fallthrough
default:
    description += " an integer."
}
print(description)
// Prints "The number 5 is a prime number, and also an integer."
```

<!--
  - test: `fallthrough`

  ```swifttest
  -> let integerToDescribe = 5
  -> var description = "The number \(integerToDescribe) is"
  -> switch integerToDescribe {
        case 2, 3, 5, 7, 11, 13, 17, 19:
           description += " a prime number, and also"
           fallthrough
        default:
           description += " an integer."
     }
  -> print(description)
  <- The number 5 is a prime number, and also an integer.
  ```
-->

이 예제는 `description`이라는 새로운 `String` 변수를 선언하고 초기값을 할당한다. 그런 다음 `switch` 문을 사용해 `integerToDescribe`의 값을 확인한다. `integerToDescribe`의 값이 리스트에 있는 소수 중 하나라면, `description`의 끝에 해당 숫자가 소수임을 나타내는 텍스트를 추가한다. 그리고 `fallthrough` 키워드를 사용해 `default` case로 넘어간다. `default` case는 설명의 끝에 추가 텍스트를 붙이고, `switch` 문의 실행을 완료한다.

`integerToDescribe`의 값이 알려진 소수 리스트에 없다면, 첫 번째 `switch` case와 일치하지 않는다. 다른 특정 case가 없기 때문에 `integerToDescribe`는 `default` case와 일치하게 된다.

`switch` 문의 실행이 끝나면, `print(_:separator:terminator:)` 함수를 사용해 숫자에 대한 설명을 출력한다. 이 예제에서는 숫자 `5`가 올바르게 소수로 식별된다.

> 참고: `fallthrough` 키워드는 실행이 넘어가는 `switch` case의 조건을 확인하지 않는다. `fallthrough` 키워드는 단순히 코드 실행을 다음 case(또는 `default` case) 블록 내부의 문장으로 이동시킨다. 이 동작은 C의 표준 `switch` 문과 동일하다.


### 레이블이 붙은 구문

Swift에서는 루프와 조건문을 다른 루프나 조건문 안에 중첩시켜 복잡한 제어 흐름 구조를 만들 수 있다. 하지만 루프와 조건문 모두 `break` 구문을 사용해 실행을 조기에 종료할 수 있다. 따라서 어떤 루프나 조건문을 `break` 구문으로 종료할지 명시적으로 지정하는 것이 유용할 때가 있다. 마찬가지로 여러 루프가 중첩된 경우, `continue` 구문이 어떤 루프에 영향을 미칠지 명확히 지정하는 것이 도움이 될 수 있다.

이러한 목적을 달성하기 위해 루프 구문이나 조건문에 *구문 레이블*을 붙일 수 있다. 조건문의 경우, 레이블과 함께 `break` 구문을 사용해 레이블이 붙은 구문의 실행을 종료할 수 있다. 루프 구문의 경우, 레이블과 함께 `break` 또는 `continue` 구문을 사용해 레이블이 붙은 구문의 실행을 종료하거나 다음 반복으로 넘어갈 수 있다.

레이블이 붙은 구문은 구문의 시작 키워드와 같은 줄에 레이블을 붙이고 콜론을 추가해 표시한다. 다음은 `while` 루프에 이 구문을 적용한 예시다. 이 원칙은 모든 루프와 `switch` 구문에 동일하게 적용된다:

```swift
<#label name#>: while <#condition#> {
   <#statements#>
}
```

다음 예제는 이 장 앞부분에서 본 *Snakes and Ladders* 게임을 변형한 버전에서 레이블이 붙은 `while` 루프와 함께 `break` 및 `continue` 구문을 사용한다. 이번 버전에서는 새로운 규칙이 추가되었다:

- 게임에서 이기려면 정확히 25번 칸에 도착해야 한다.

주사위를 굴려 25번 칸을 넘어가게 되면, 정확히 25번 칸에 도착할 수 있는 숫자가 나올 때까지 다시 주사위를 굴려야 한다.

게임 보드는 이전과 동일하다.

![](snakesAndLadders)

`finalSquare`, `board`, `square`, `diceRoll`의 값은 이전과 동일한 방식으로 초기화된다:

```swift
let finalSquare = 25
var board = [Int](repeating: 0, count: finalSquare + 1)
board[03] = +08; board[06] = +11; board[09] = +09; board[10] = +02
board[14] = -10; board[19] = -11; board[22] = -02; board[24] = -08
var square = 0
var diceRoll = 0
```

이 버전의 게임은 `while` 루프와 `switch` 구문을 사용해 게임 로직을 구현한다. `while` 루프에는 `gameLoop`라는 구문 레이블이 붙어 있으며, 이는 Snakes and Ladders 게임의 메인 루프임을 나타낸다.

`while` 루프의 조건은 `while square != finalSquare`로, 정확히 25번 칸에 도착해야 함을 반영한다.

```swift
gameLoop: while square != finalSquare {
    diceRoll += 1
    if diceRoll == 7 { diceRoll = 1 }
    switch square + diceRoll {
    case finalSquare:
        // 주사위를 굴려 정확히 25번 칸에 도착하면 게임 종료
        break gameLoop
    case let newSquare where newSquare > finalSquare:
        // 주사위를 굴려 25번 칸을 넘어가면 다시 굴림
        continue gameLoop
    default:
        // 유효한 이동이므로 이동 결과 확인
        square += diceRoll
        square += board[square]
    }
}
print("Game over!")
```

각 루프가 시작될 때 주사위를 굴린다. 플레이어를 즉시 이동시키는 대신, `switch` 구문을 사용해 이동 결과를 고려하고 이동이 허용되는지 결정한다:

- 주사위를 굴려 플레이어가 정확히 25번 칸에 도착하면 게임이 종료된다. `break gameLoop` 구문은 `while` 루프 외부의 첫 번째 코드 줄로 제어를 이동시켜 게임을 끝낸다.
- 주사위를 굴려 플레이어가 25번 칸을 넘어가면 이동이 무효화되고 플레이어는 다시 주사위를 굴려야 한다. `continue gameLoop` 구문은 현재 `while` 루프 반복을 종료하고 다음 반복을 시작한다.
- 다른 모든 경우에는 주사위 굴림이 유효한 이동이다. 플레이어는 `diceRoll` 만큼 앞으로 이동하고, 게임 로직은 뱀과 사다리를 확인한다. 그런 다음 루프가 종료되고, 제어는 `while` 조건으로 돌아가 다음 턴이 필요한지 결정한다.

> 참고: 위의 `break` 구문에서 `gameLoop` 레이블을 사용하지 않았다면, `switch` 구문을 종료하게 되고 `while` 구문을 종료하지 않는다. `gameLoop` 레이블을 사용하면 어떤 제어 구문을 종료할지 명확히 할 수 있다.
>
> `continue gameLoop`를 사용해 루프의 다음 반복으로 넘어갈 때 `gameLoop` 레이블을 사용하는 것은 꼭 필요하지 않다. 게임에는 하나의 루프만 있으므로 `continue` 구문이 어떤 루프에 영향을 미칠지 모호하지 않다. 하지만 `continue` 구문에 `gameLoop` 레이블을 사용해도 문제는 없다. 이렇게 하면 `break` 구문과의 일관성을 유지할 수 있고, 게임 로직을 더 명확히 이해하는 데 도움이 된다.


## 조기 종료

`guard` 문은 `if` 문과 마찬가지로 표현식의 불리언 값에 따라 코드를 실행한다. `guard` 문은 특정 조건이 참일 때만 `guard` 문 이후의 코드가 실행되도록 요구한다. `if` 문과 달리, `guard` 문은 항상 `else` 절을 포함한다. 조건이 참이 아닐 경우 `else` 절 내부의 코드가 실행된다.

```swift
func greet(person: [String: String]) {
    guard let name = person["name"] else {
        return
    }

    print("Hello \(name)!")

    guard let location = person["location"] else {
        print("I hope the weather is nice near you.")
        return
    }

    print("I hope the weather is nice in \(location).")
}

greet(person: ["name": "John"])
// Prints "Hello John!"
// Prints "I hope the weather is nice near you."
greet(person: ["name": "Jane", "location": "Cupertino"])
// Prints "Hello Jane!"
// Prints "I hope the weather is nice in Cupertino."
```

<!--
  - test: `guard`

  ```swifttest
  -> func greet(person: [String: String]) {
         guard let name = person["name"] else {
             return
         }

         print("Hello \(name)!")

         guard let location = person["location"] else {
             print("I hope the weather is nice near you.")
             return
         }

         print("I hope the weather is nice in \(location).")
     }

  -> greet(person: ["name": "John"])
  <- Hello John!
  <- I hope the weather is nice near you.
  -> greet(person: ["name": "Jane", "location": "Cupertino"])
  <- Hello Jane!
  <- I hope the weather is nice in Cupertino.
  ```
-->

`guard` 문의 조건이 충족되면, `guard` 문의 닫는 중괄호 이후부터 코드 실행이 계속된다. 조건의 일부로 옵셔널 바인딩을 통해 할당된 변수나 상수는 `guard` 문이 위치한 코드 블록의 나머지 부분에서 사용할 수 있다.

조건이 충족되지 않으면, `else` 분기 내부의 코드가 실행된다. 이 분기는 `guard` 문이 위치한 코드 블록을 종료하기 위해 제어를 전달해야 한다. 이를 위해 `return`, `break`, `continue`, `throw`와 같은 제어 전달 문을 사용하거나, `fatalError(_:file:line:)`과 같이 반환하지 않는 함수나 메서드를 호출할 수 있다.

`guard` 문을 사용해 요구사항을 확인하면, `if` 문을 사용하는 것보다 코드의 가독성이 향상된다. 일반적으로 실행되는 코드를 `else` 블록으로 감싸지 않아도 되며, 요구사항이 위반되었을 때 처리하는 코드를 요구사항 바로 옆에 배치할 수 있다.


## 지연된 동작

`if`나 `while` 같은 제어 흐름 구문은 코드의 일부가 실행될지 여부나 실행 횟수를 제어한다. 반면 `defer`는 코드가 *언제* 실행될지를 제어한다. `defer` 블록을 사용하면 현재 스코프가 끝나는 시점에 실행될 코드를 작성할 수 있다. 예를 들어:

```swift
var score = 1
if score < 10 {
    defer {
        print(score)
    }
    score += 5
}
// "6" 출력
```

<!--
  - test: `defer-with-if`

  ```swifttest
  -> var score = 1
  -> if score < 10 {
  ->     defer {
  ->         print(score)
  ->     }
  ->     score += 5
  -> }
  <- 6
  ```
-->

위 예제에서 `defer` 블록 안의 코드는 `if` 문의 본문을 벗어나기 직전에 실행된다. 먼저 `if` 문 안의 코드가 실행되어 `score`에 5를 더한다. 그런 다음 `if` 문의 스코프를 벗어나기 직전에 지연된 코드가 실행되어 `score` 값을 출력한다.

`defer` 블록 안의 코드는 프로그램이 해당 스코프를 어떻게 벗어나든 상관없이 항상 실행된다. 여기에는 함수에서 조기 반환하거나, `for` 루프를 중단하거나, 오류를 던지는 경우도 포함된다. 이러한 동작은 메모리 할당과 해제, 저수준 파일 디스크립터 열기와 닫기, 데이터베이스 트랜잭션 시작과 종료처럼 반드시 짝을 이루어야 하는 작업에 `defer`를 유용하게 만든다. 코드에서 두 작업을 나란히 작성할 수 있기 때문이다. 예를 들어, 다음 코드는 일시적으로 점수에 보너스를 주기 위해 100을 더하고 빼는 작업을 수행한다:

```swift
var score = 3
if score < 100 {
    score += 100
    defer {
        score -= 100
    }
    // 보너스가 적용된 점수를 사용하는 다른 코드가 여기에 위치한다.
    print(score)
}
// "103" 출력
```

<!--
  - test: `defer-paired-actions`

  ```swift
  -> var score = 3
  -> if score < 100 {
  ->     score += 100
  ->     defer {
  ->         score -= 100
  ->     }
  ->     // Other code that uses the score with its bonus goes here.
  ->     print(score)
  -> }
  <- 103
  ```
-->

같은 스코프 안에 여러 개의 `defer` 블록을 작성하면, 처음 지정한 블록이 가장 나중에 실행된다.

```swift
if score < 10 {
    defer {
        print(score)
    }
    defer {
        print("The score is:")
    }
    score += 5
}
// "The score is:" 출력
// "6" 출력
```

<!--
  - test: `defer-with-if`

  ```swifttest
  -> if score < 10 {
  ->     defer {
  ->         print(score)
  ->     }
  ->     defer {
  ->         print("The score is:")
  ->     }
  ->     score += 5
  -> }
  <- 6
  ```
-->

프로그램이 실행을 중단하는 경우 --- 예를 들어 런타임 오류나 충돌로 인해 --- 지연된 코드는 실행되지 않는다. 하지만 오류가 발생한 후에는 지연된 코드가 실행된다. 오류 처리와 함께 `defer`를 사용하는 방법에 대한 자세한 내용은 <doc:ErrorHandling#Specifying-Cleanup-Actions>를 참고한다.


## API 가용성 확인

Swift는 API 가용성을 확인하는 기능을 기본으로 제공한다. 이를 통해 특정 배포 대상에서 사용할 수 없는 API를 실수로 사용하는 것을 방지할 수 있다.

컴파일러는 SDK에 포함된 가용성 정보를 활용해 코드에서 사용하는 모든 API가 프로젝트에서 지정한 배포 대상에서 사용 가능한지 확인한다. 만약 사용할 수 없는 API를 사용하려고 하면 컴파일 시점에 오류를 보고한다.

`if`나 `guard` 문에서 *가용성 조건*을 사용하면, 런타임에 사용하려는 API가 사용 가능한지에 따라 코드 블록을 조건부로 실행할 수 있다. 컴파일러는 이 가용성 조건의 정보를 활용해 해당 코드 블록 내의 API가 사용 가능한지 검증한다.

```swift
if #available(iOS 10, macOS 10.12, *) {
    // iOS에서는 iOS 10 API를, macOS에서는 macOS 10.12 API를 사용
} else {
    // 이전 버전의 iOS와 macOS API로 대체
}
```

위의 가용성 조건은 iOS에서는 `if` 문의 본문이 iOS 10 이상에서만 실행되고, macOS에서는 macOS 10.12 이상에서만 실행되도록 지정한다. 마지막 인자인 `*`는 필수이며, 다른 플랫폼에서는 프로젝트에서 지정한 최소 배포 대상에서 `if` 문의 본문이 실행된다.

일반적으로 가용성 조건은 플랫폼 이름과 버전 목록을 받는다. `iOS`, `macOS`, `watchOS`, `tvOS`, `visionOS`와 같은 플랫폼 이름을 사용할 수 있다. 전체 목록은 <doc:Attributes#Declaration-Attributes>를 참고한다. iOS 8이나 macOS 10.10과 같은 주 버전뿐만 아니라 iOS 11.2.6이나 macOS 10.13.3과 같은 부 버전도 지정할 수 있다.

```swift
if #available(<#플랫폼 이름#> <#버전#>, <#...#>, *) {
    <#API가 사용 가능할 때 실행할 코드#>
} else {
    <#API가 사용 불가능할 때 실행할 대체 코드#>
}
```

`guard` 문에서 가용성 조건을 사용하면, 해당 코드 블록의 나머지 부분에 사용할 가용성 정보를 구체화할 수 있다.

```swift
@available(macOS 10.12, *)
struct ColorPreference {
    var bestColor = "blue"
}

func chooseBestColor() -> String {
    guard #available(macOS 10.12, *) else {
       return "gray"
    }
    let colors = ColorPreference()
    return colors.bestColor
}
```

위 예제에서 `ColorPreference` 구조체는 macOS 10.12 이상이 필요하다. `chooseBestColor()` 함수는 가용성 가드를 시작으로, 플랫폼 버전이 `ColorPreference`를 사용하기에 너무 오래된 경우 항상 사용 가능한 동작으로 대체한다. `guard` 문 이후에는 macOS 10.12 이상이 필요한 API를 사용할 수 있다.

`#available` 외에도 Swift는 `#unavailable` 조건을 사용해 반대의 검사를 지원한다. 예를 들어, 다음 두 검사는 동일한 작업을 수행한다.

```swift
if #available(iOS 10, *) {
} else {
    // 대체 코드
}

if #unavailable(iOS 10) {
    // 대체 코드
}
```

`#unavailable` 형식을 사용하면 대체 코드만 포함된 경우 코드의 가독성을 높일 수 있다.


