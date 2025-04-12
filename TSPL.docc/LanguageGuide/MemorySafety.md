# 메모리 안전성

메모리 접근 시 충돌이 발생하지 않도록 코드를 구조화한다.

Swift는 기본적으로 코드에서 안전하지 않은 동작이 발생하지 않도록 방지한다. 예를 들어, Swift는 변수가 사용되기 전에 초기화되도록 보장하고, 메모리가 해제된 후에는 접근하지 않도록 하며, 배열 인덱스가 범위를 벗어나지 않도록 검사한다.

또한 Swift는 메모리의 동일한 영역에 대한 여러 접근이 충돌하지 않도록 한다. 이를 위해 메모리의 특정 위치를 수정하는 코드가 해당 메모리에 대한 독점적인 접근 권한을 갖도록 요구한다. Swift가 메모리를 자동으로 관리하기 때문에 대부분의 경우 메모리 접근에 대해 생각할 필요가 없다. 그러나 잠재적인 충돌이 발생할 수 있는 상황을 이해하는 것이 중요하다. 이를 통해 메모리에 대한 충돌 접근이 발생하는 코드를 작성하지 않도록 할 수 있다. 코드에 충돌이 포함되어 있다면 컴파일 타임 또는 런타임 오류가 발생한다.

<!--
  TODO: maybe re-introduce this text...

  메모리 안전성은...
  *안전성*이라는 용어는 일반적으로 :newTerm:`메모리 안전성`을 의미한다...
  명시적으로 요청하면 안전하지 않은 메모리 접근이 가능하다...
-->


## 메모리 접근 충돌 이해하기

메모리에 접근하는 일은 변수에 값을 설정하거나 함수에 인자를 전달할 때 발생한다. 예를 들어, 다음 코드는 메모리에 대한 쓰기 접근과 읽기 접근을 모두 포함한다:

```swift
// one이 저장된 메모리에 대한 쓰기 접근
var one = 1

// one이 저장된 메모리에서 읽기 접근
print("We're number \(one)!")
```

<!--
  - test: `memory-read-write`

  ```swifttest
  // A write access to the memory where one is stored.
  -> var one = 1

  // A read access from the memory where one is stored.
  -> print("We're number \(one)!")
  << We're number 1!
  ```
-->

메모리 접근 충돌은 코드의 다른 부분이 동시에 같은 메모리 위치에 접근하려 할 때 발생할 수 있다. 동시에 여러 번 메모리 위치에 접근하면 예측할 수 없거나 일관되지 않은 동작이 발생할 수 있다. Swift에서는 여러 줄에 걸쳐 값을 수정할 수 있기 때문에, 값이 수정되는 도중에 해당 값에 접근하려는 시도가 가능하다.

이와 유사한 문제를 예산을 업데이트하는 과정을 통해 생각해볼 수 있다. 예산 업데이트는 두 단계로 이루어진다: 먼저 항목의 이름과 가격을 추가한 다음, 현재 목록에 있는 항목을 반영해 총액을 변경한다. 업데이트 전후에는 예산에서 정보를 읽어 정확한 답을 얻을 수 있다.

![](memory_shopping)

항목을 예산에 추가하는 동안, 새로 추가된 항목을 반영해 총액이 업데이트되지 않았기 때문에 예산은 일시적으로 유효하지 않은 상태가 된다. 항목을 추가하는 과정에서 총액을 읽으면 잘못된 정보를 얻을 수 있다.

이 예제는 메모리 접근 충돌을 해결할 때 마주할 수 있는 어려움도 보여준다. 충돌을 해결하는 방법은 여러 가지가 있을 수 있으며, 어떤 답이 올바른지 항상 명확하지 않다. 이 예제에서는 원래 총액을 원하는지 업데이트된 총액을 원하는지에 따라 $5 또는 $320이 정답이 될 수 있다. 메모리 접근 충돌을 해결하기 전에 의도한 바가 무엇인지 먼저 파악해야 한다.

> 참고: 동시성 또는 멀티스레드 코드를 작성해본 적이 있다면 메모리 접근 충돌이 익숙한 문제일 수 있다. 그러나 여기서 논의하는 메모리 접근 충돌은 단일 스레드에서도 발생할 수 있으며, 동시성 또는 멀티스레드 코드와는 관련이 없다.
>
> 단일 스레드 내에서 메모리 접근 충돌이 발생하면 Swift는 컴파일 시간 또는 런타임에 오류를 발생시킨다. 멀티스레드 코드의 경우 [Thread Sanitizer](https://developer.apple.com/documentation/xcode/diagnosing_memory_thread_and_crash_issues_early)를 사용해 스레드 간의 메모리 접근 충돌을 감지할 수 있다.

<!--
  TODO: 위의 xref는 충분한 정보를 제공하지 않는 것 같다.
  링크된 페이지에 도달했을 때 무엇을 찾아야 하는가?
-->


### 메모리 접근의 특성

메모리 접근 충돌을 고려할 때는 세 가지 특성을 살펴봐야 한다. 접근이 읽기인지 쓰기인지, 접근 지속 시간이 얼마나 되는지, 그리고 메모리에서 어떤 위치를 접근하는지가 그것이다. 구체적으로, 두 접근이 다음 조건을 모두 만족하면 충돌이 발생한다:

- 두 접근이 모두 읽기가 아니며, 모두 아토믹(atomic)하지 않다.
- 같은 메모리 위치를 접근한다.
- 접근 지속 시간이 겹친다.

읽기와 쓰기 접근의 차이는 일반적으로 명확하다. 쓰기 접근은 메모리 위치를 변경하지만, 읽기 접근은 그렇지 않다. 메모리 위치는 접근 대상(예: 변수, 상수, 프로퍼티)을 의미한다. 메모리 접근 지속 시간은 순간적이거나 장기적일 수 있다.

접근이 *아토믹*하다는 것은 [`Atomic`]이나 [`AtomicLazyReference`]의 아토믹 연산을 호출하거나, C 아토믹 연산만을 사용하는 경우를 말한다. 그렇지 않으면 논아토믹(nonatomic)이다. C 아토믹 함수 목록은 `stdatomic(3)` 매뉴얼 페이지를 참고한다.

[`Atomic`]: https://developer.apple.com/documentation/synchronization/atomic
[`AtomicLazyReference`]: https://developer.apple.com/documentation/synchronization/atomiclazyreference

<!--
  Swift에서 C 아토믹 함수를 사용하려면 TSPL 범위를 벗어나는 추가 작업이 필요하다. 예시:
  https://github.com/apple/swift-se-0282-experimental/tree/master/Sources/_AtomicsShims
-->

접근이 *순간적*이라는 것은 해당 접근이 시작된 후 끝나기 전에 다른 코드가 실행될 가능성이 없는 것을 의미한다. 순간적 접근 두 개는 동시에 발생할 수 없다. 대부분의 메모리 접근은 순간적이다. 예를 들어, 아래 코드의 모든 읽기와 쓰기 접근은 순간적이다:

```swift
func oneMore(than number: Int) -> Int {
    return number + 1
}

var myNumber = 1
myNumber = oneMore(than: myNumber)
print(myNumber)
// Prints "2"
```

<!--
  - test: `memory-instantaneous`

  ```swifttest
  -> func oneMore(than number: Int) -> Int {
         return number + 1
     }

  -> var myNumber = 1
  -> myNumber = oneMore(than: myNumber)
  -> print(myNumber)
  <- 2
  ```
-->

하지만 *장기적* 접근이라고 불리는 몇 가지 메모리 접근 방식이 있다. 이는 다른 코드가 실행되는 동안에도 지속된다. 순간적 접근과 장기적 접근의 차이는, 장기적 접근이 시작된 후 끝나기 전에 다른 코드가 실행될 가능성이 있다는 점이다. 이를 *겹침(overlap)*이라고 한다. 장기적 접근은 다른 장기적 접근이나 순간적 접근과 겹칠 수 있다.

겹치는 접근은 주로 함수와 메서드의 in-out 매개변수를 사용하거나 구조체의 뮤테이션 메서드를 사용하는 코드에서 나타난다. 장기적 접근을 사용하는 Swift 코드의 구체적인 종류는 아래 섹션에서 다룬다.


## 인아웃 매개변수에 대한 접근 충돌

함수는 모든 인아웃 매개변수에 대해 장기적인 쓰기 접근 권한을 가진다. 인아웃 매개변수에 대한 쓰기 접근은 모든 비인아웃 매개변수가 평가된 후에 시작되며, 함수 호출이 끝날 때까지 지속된다. 만약 여러 개의 인아웃 매개변수가 있다면, 쓰기 접근은 매개변수가 나타나는 순서대로 시작된다.

이러한 장기적인 쓰기 접근의 한 가지 결과는, 스코핑 규칙과 접근 제어가 허용하더라도 인아웃으로 전달된 원본 변수에 접근할 수 없다는 점이다. 원본 변수에 대한 어떤 접근이든 충돌을 일으킨다. 예를 들어:

```swift
var stepSize = 1

func increment(_ number: inout Int) {
    number += stepSize
}

increment(&stepSize)
// 에러: stepSize에 대한 접근 충돌
```

위 코드에서 `stepSize`는 전역 변수이며, 일반적으로 `increment(_:)` 함수 내에서 접근할 수 있다. 그러나 `stepSize`에 대한 읽기 접근은 `number`에 대한 쓰기 접근과 겹친다. 아래 그림에서 보듯, `number`와 `stepSize`는 모두 메모리의 같은 위치를 참조한다. 읽기와 쓰기 접근이 같은 메모리를 참조하고 겹치기 때문에 충돌이 발생한다.

![](memory_increment)

이 충돌을 해결하는 한 가지 방법은 `stepSize`의 명시적인 복사본을 만드는 것이다:

```swift
// 명시적인 복사본 생성
var copyOfStepSize = stepSize
increment(&copyOfStepSize)

// 원본 업데이트
stepSize = copyOfStepSize
// stepSize는 이제 2
```

`increment(_:)`를 호출하기 전에 `stepSize`의 복사본을 만들면, `copyOfStepSize`의 값이 현재 스텝 크기만큼 증가하는 것이 명확해진다. 읽기 접근은 쓰기 접근이 시작되기 전에 끝나므로 충돌이 발생하지 않는다.

인아웃 매개변수에 대한 장기적인 쓰기 접근의 또 다른 결과는, 같은 함수의 여러 인아웃 매개변수에 단일 변수를 인자로 전달하면 충돌이 발생한다는 점이다. 예를 들어:

```swift
func balance(_ x: inout Int, _ y: inout Int) {
    let sum = x + y
    x = sum / 2
    y = sum - x
}
var playerOneScore = 42
var playerTwoScore = 30
balance(&playerOneScore, &playerTwoScore)  // 정상
balance(&playerOneScore, &playerOneScore)
// 에러: playerOneScore에 대한 접근 충돌
```

위의 `balance(_:_:)` 함수는 두 매개변수를 수정하여 총 값을 균등하게 나눈다. `playerOneScore`와 `playerTwoScore`를 인자로 전달하면 충돌이 발생하지 않는다. 시간적으로 겹치는 두 쓰기 접근이 있지만, 서로 다른 메모리 위치를 접근하기 때문이다. 반면, `playerOneScore`를 두 매개변수의 값으로 전달하면 같은 메모리 위치에 동시에 두 쓰기 접근을 시도하므로 충돌이 발생한다.

> 참고: 연산자도 함수이기 때문에, 인아웃 매개변수에 대해 장기적인 접근 권한을 가질 수 있다. 예를 들어, `balance(_:_:)`가 `<^>`라는 연산자 함수라면, `playerOneScore <^> playerOneScore`를 작성하면 `balance(&playerOneScore, &playerOneScore)`와 같은 충돌이 발생한다.


## 메서드 내에서 self에 대한 접근 충돌

<!--
  이 내용은 (아마도?) 모든 값 타입에 적용되지만,
  구조체에서만 이를 관찰할 수 있다.
  열거형은 뮤테이션 메서드를 가질 수 있지만,
  연관된 값을 직접 변경할 수는 없다.
  튜플은 메서드를 가질 수 없다.
-->

<!--
  메서드는 self가 inout 매개변수로 전달된 것처럼 동작한다.
  실제로 그렇게 동작하기 때문이다.
-->

구조체의 뮤테이션 메서드는 메서드 호출 기간 동안 `self`에 대한 쓰기 접근 권한을 가진다. 예를 들어, 각 플레이어가 체력과 에너지를 가지고 있는 게임을 생각해 보자. 플레이어는 데미지를 입으면 체력이 감소하고, 특수 능력을 사용하면 에너지가 감소한다.

```swift
struct Player {
    var name: String
    var health: Int
    var energy: Int

    static let maxHealth = 10
    mutating func restoreHealth() {
        health = Player.maxHealth
    }
}
```

<!--
  - test: `memory-player-share-with-self`

  ```swifttest
  >> func balance(_ x: inout Int, _ y: inout Int) {
  >>     let sum = x + y
  >>     x = sum / 2
  >>     y = sum - x
  >> }
  -> struct Player {
         var name: String
         var health: Int
         var energy: Int

         static let maxHealth = 10
         mutating func restoreHealth() {
             health = Player.maxHealth
         }
     }
  ```
-->

위의 `restoreHealth()` 메서드에서, `self`에 대한 쓰기 접근은 메서드가 시작될 때 시작되어 메서드가 반환될 때까지 지속된다. 이 경우, `restoreHealth()` 내부에는 `Player` 인스턴스의 프로퍼티에 중복 접근할 가능성이 있는 다른 코드가 없다. 아래의 `shareHealth(with:)` 메서드는 다른 `Player` 인스턴스를 in-out 매개변수로 받아 중복 접근이 발생할 가능성을 만든다.

```swift
extension Player {
    mutating func shareHealth(with teammate: inout Player) {
        balance(&teammate.health, &health)
    }
}

var oscar = Player(name: "Oscar", health: 10, energy: 10)
var maria = Player(name: "Maria", health: 5, energy: 10)
oscar.shareHealth(with: &maria)  // OK
```

<!--
  - test: `memory-player-share-with-self`

  ```swifttest
  -> extension Player {
         mutating func shareHealth(with teammate: inout Player) {
             balance(&teammate.health, &health)
         }
     }

  -> var oscar = Player(name: "Oscar", health: 10, energy: 10)
  -> var maria = Player(name: "Maria", health: 5, energy: 10)
  -> oscar.shareHealth(with: &maria)  // OK
  ```
-->

위 예제에서, Oscar 플레이어가 Maria 플레이어와 체력을 공유하기 위해 `shareHealth(with:)` 메서드를 호출할 때 충돌이 발생하지 않는다. 메서드 호출 동안 `oscar`는 뮤테이션 메서드의 `self` 값이므로 `oscar`에 대한 쓰기 접근이 발생하고, `maria`는 in-out 매개변수로 전달되었으므로 같은 기간 동안 `maria`에 대한 쓰기 접근이 발생한다. 아래 그림에서 보듯이, 이들은 서로 다른 메모리 위치에 접근한다. 두 쓰기 접근이 시간적으로 겹치더라도 충돌하지 않는다.

![](memory_share_health_maria)

그러나 `oscar`를 `shareHealth(with:)`의 인자로 전달하면 충돌이 발생한다:

```swift
oscar.shareHealth(with: &oscar)
// Error: conflicting accesses to oscar
```

<!--
  - test: `memory-player-share-with-self`

  ```swifttest
  -> oscar.shareHealth(with: &oscar)
  // Error: conflicting accesses to oscar
  !$ error: inout arguments are not allowed to alias each other
  !! oscar.shareHealth(with: &oscar)
  !!                         ^~~~~~
  !$ note: previous aliasing argument
  !! oscar.shareHealth(with: &oscar)
  !! ^~~~~
  !$ error: overlapping accesses to 'oscar', but modification requires exclusive access; consider copying to a local variable
  !! oscar.shareHealth(with: &oscar)
  !!                          ^~~~~
  !$ note: conflicting access is here
  !! oscar.shareHealth(with: &oscar)
  !! ^~~~~~
  ```
-->

뮤테이션 메서드는 메서드 호출 기간 동안 `self`에 대한 쓰기 접근이 필요하고, in-out 매개변수는 같은 기간 동안 `teammate`에 대한 쓰기 접근이 필요하다. 메서드 내에서 `self`와 `teammate`는 동일한 메모리 위치를 참조한다. 아래 그림에서 볼 수 있듯이, 두 쓰기 접근이 동일한 메모리를 참조하고 시간적으로 겹치기 때문에 충돌이 발생한다.

![](memory_share_health_oscar)


## 프로퍼티 접근 충돌

구조체, 튜플, 열거형과 같은 타입은 각각의 구성 값으로 이루어져 있다. 예를 들어 구조체의 프로퍼티나 튜플의 요소가 이에 해당한다. 이러한 타입은 값 타입이기 때문에 값의 일부를 변경하면 전체 값이 변경된다. 즉, 프로퍼티 중 하나에 읽기 또는 쓰기 접근을 하려면 전체 값에 대한 접근이 필요하다. 예를 들어, 튜플의 요소에 중복된 쓰기 접근이 발생하면 충돌이 발생한다:

```swift
var playerInformation = (health: 10, energy: 20)
balance(&playerInformation.health, &playerInformation.energy)
// Error: playerInformation의 프로퍼티에 대한 접근 충돌
```

위 예제에서 `balance(_:_:)` 함수를 튜플의 요소에 호출하면 충돌이 발생한다. 이는 `playerInformation`에 중복된 쓰기 접근이 발생하기 때문이다. `playerInformation.health`와 `playerInformation.energy` 모두 in-out 매개변수로 전달되며, 이는 `balance(_:_:)` 함수가 호출되는 동안 두 값에 대한 쓰기 접근이 필요함을 의미한다. 두 경우 모두 튜플 요소에 쓰기 접근하려면 전체 튜플에 대한 쓰기 접근이 필요하다. 따라서 `playerInformation`에 두 번의 쓰기 접근이 중복되면서 충돌이 발생한다.

아래 코드는 전역 변수로 저장된 구조체의 프로퍼티에 중복된 쓰기 접근이 발생할 때 동일한 오류가 나타나는 것을 보여준다:

```swift
var holly = Player(name: "Holly", health: 10, energy: 10)
balance(&holly.health, &holly.energy)  // Error
```

실제로는 구조체의 프로퍼티에 대한 대부분의 접근이 안전하게 중복될 수 있다. 예를 들어, 위 예제에서 변수 `holly`를 전역 변수가 아닌 지역 변수로 변경하면 컴파일러가 구조체의 저장 프로퍼티에 대한 중복 접근이 안전하다고 판단할 수 있다:

```swift
func someFunction() {
    var oscar = Player(name: "Oscar", health: 10, energy: 10)
    balance(&oscar.health, &oscar.energy)  // OK
}
```

위 예제에서 Oscar의 health와 energy는 `balance(_:_:)` 함수의 두 in-out 매개변수로 전달된다. 컴파일러는 두 저장 프로퍼티가 서로 상호작용하지 않으므로 메모리 안전성이 보장된다고 판단할 수 있다.

구조체의 프로퍼티에 대한 중복 접근을 금지하는 제약은 항상 메모리 안전성을 보장하기 위해 필요한 것은 아니다. 메모리 안전성은 보장되어야 하지만, 독점적 접근은 메모리 안전성보다 더 엄격한 요구 사항이다. 따라서 일부 코드는 메모리 안전성을 보장하더라도 메모리에 대한 독점적 접근을 위반할 수 있다. Swift는 컴파일러가 메모리에 대한 비독점적 접근이 여전히 안전하다고 증명할 수 있다면 이러한 메모리 안전 코드를 허용한다. 특히, 다음 조건이 충족되면 구조체의 프로퍼티에 대한 중복 접근이 안전하다고 판단할 수 있다:

- 인스턴스의 저장 프로퍼티에만 접근하고, 계산 프로퍼티나 클래스 프로퍼티에는 접근하지 않는다.
- 구조체가 지역 변수의 값이며, 전역 변수가 아니다.
- 구조체가 클로저에 의해 캡처되지 않거나, nonescaping 클로저에만 캡처된다.

컴파일러가 접근이 안전하다고 증명할 수 없다면 해당 접근을 허용하지 않는다.


