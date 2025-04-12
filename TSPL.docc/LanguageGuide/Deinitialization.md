# 리소스 해제

커스텀 정리가 필요한 리소스를 해제한다.

*디이니셜라이저*는 클래스 인스턴스가 메모리에서 해제되기 직전에 호출된다.  
디이니셜라이저는 `init` 키워드로 이니셜라이저를 작성하는 방식과 유사하게 `deinit` 키워드를 사용해 작성한다.  
디이니셜라이저는 클래스 타입에서만 사용할 수 있다.


## 디이니셜라이저의 동작 원리

Swift는 인스턴스가 더 이상 필요하지 않을 때 자동으로 메모리를 해제하여 리소스를 확보한다. Swift는 *자동 참조 카운팅*(*ARC*)을 통해 인스턴스의 메모리 관리를 처리한다. 이에 대한 자세한 내용은 <doc:AutomaticReferenceCounting>에서 확인할 수 있다. 일반적으로 인스턴스가 해제될 때 수동으로 정리 작업을 수행할 필요는 없다. 하지만 커스텀 리소스를 다룰 때는 추가적인 정리 작업이 필요할 수 있다. 예를 들어, 파일을 열고 데이터를 기록하는 커스텀 클래스를 만든 경우, 클래스 인스턴스가 해제되기 전에 파일을 닫아야 할 수 있다.

클래스 정의에서는 클래스당 최대 하나의 디이니셜라이저를 가질 수 있다. 디이니셜라이저는 매개변수를 받지 않으며, 괄호 없이 작성한다:

```swift
deinit {
    // 디이니셜라이저 수행
}
```

<!--
  - test: `deinitializer`

  ```swifttest
  >> class Test {
  -> deinit {
        // 디이니셜라이저 수행
     }
  >> }
  ```
-->

디이니셜라이저는 인스턴스가 해제되기 직전에 자동으로 호출된다. 개발자가 직접 디이니셜라이저를 호출할 수는 없다. 슈퍼클래스의 디이니셜라이저는 서브클래스에 상속되며, 서브클래스의 디이니셜라이저 구현이 끝나면 자동으로 슈퍼클래스의 디이니셜라이저가 호출된다. 서브클래스가 자체 디이니셜라이저를 제공하지 않더라도 슈퍼클래스의 디이니셜라이저는 항상 호출된다.

디이니셜라이저가 호출된 후에야 인스턴스가 해제되기 때문에, 디이니셜라이저는 호출된 인스턴스의 모든 프로퍼티에 접근할 수 있다. 또한 이러한 프로퍼티를 기반으로 동작을 수정할 수도 있다(예: 닫아야 할 파일의 이름을 조회하는 등).


## 디이니셜라이저의 동작

디이니셜라이저가 어떻게 동작하는지 예제를 통해 살펴보자. 이 예제에서는 간단한 게임을 위해 `Bank`와 `Player`라는 두 가지 타입을 정의한다. `Bank` 클래스는 가상의 통화를 관리하며, 유통되는 코인은 최대 10,000개를 넘을 수 없다. 게임 내에는 오직 하나의 `Bank`만 존재할 수 있으므로, `Bank`는 타입 프로퍼티와 메서드를 사용해 현재 상태를 저장하고 관리한다.

```swift
class Bank {
    static var coinsInBank = 10_000
    static func distribute(coins numberOfCoinsRequested: Int) -> Int {
        let numberOfCoinsToVend = min(numberOfCoinsRequested, coinsInBank)
        coinsInBank -= numberOfCoinsToVend
        return numberOfCoinsToVend
    }
    static func receive(coins: Int) {
        coinsInBank += coins
    }
}
```

<!--
  - test: `deinitializer`

  ```swifttest
  -> class Bank {
        static var coinsInBank = 10_000
        static func distribute(coins numberOfCoinsRequested: Int) -> Int {
           let numberOfCoinsToVend = min(numberOfCoinsRequested, coinsInBank)
           coinsInBank -= numberOfCoinsToVend
           return numberOfCoinsToVend
        }
        static func receive(coins: Int) {
           coinsInBank += coins
        }
     }
  ```
-->

`Bank`는 `coinsInBank` 프로퍼티를 통해 현재 보유한 코인 수를 추적한다. 또한 `distribute(coins:)`와 `receive(coins:)` 두 메서드를 제공해 코인을 분배하고 회수한다.

`distribute(coins:)` 메서드는 코인을 분배하기 전에 은행에 충분한 코인이 있는지 확인한다. 만약 코인이 부족하면, 요청된 수보다 적은 양을 반환한다(은행에 코인이 하나도 없다면 0을 반환). 이 메서드는 실제로 제공된 코인 수를 나타내는 정수 값을 반환한다.

`receive(coins:)` 메서드는 단순히 받은 코인 수를 은행의 코인 저장고에 다시 추가한다.

`Player` 클래스는 게임 내 플레이어를 나타낸다. 각 플레이어는 언제든지 지갑에 일정 수의 코인을 보유한다. 이는 플레이어의 `coinsInPurse` 프로퍼티로 표현된다.

```swift
class Player {
    var coinsInPurse: Int
    init(coins: Int) {
        coinsInPurse = Bank.distribute(coins: coins)
    }
    func win(coins: Int) {
        coinsInPurse += Bank.distribute(coins: coins)
    }
    deinit {
        Bank.receive(coins: coinsInPurse)
    }
}
```

<!--
  - test: `deinitializer`

  ```swifttest
  -> class Player {
        var coinsInPurse: Int
        init(coins: Int) {
           coinsInPurse = Bank.distribute(coins: coins)
        }
        func win(coins: Int) {
           coinsInPurse += Bank.distribute(coins: coins)
        }
        deinit {
           Bank.receive(coins: coinsInPurse)
        }
     }
  ```
-->

각 `Player` 인스턴스는 초기화 과정에서 은행으로부터 지정된 수의 코인을 받는다. 하지만 은행에 코인이 충분하지 않다면, 요청된 수보다 적은 양을 받을 수도 있다.

`Player` 클래스는 `win(coins:)` 메서드를 정의한다. 이 메서드는 은행에서 일정 수의 코인을 가져와 플레이어의 지갑에 추가한다. 또한 `Player` 클래스는 디이니셜라이저를 구현한다. 이 디이니셜라이저는 `Player` 인스턴스가 메모리에서 해제되기 직전에 호출된다. 여기서 디이니셜라이저는 플레이어가 보유한 모든 코인을 은행에 반환한다.

```swift
var playerOne: Player? = Player(coins: 100)
print("A new player has joined the game with \(playerOne!.coinsInPurse) coins")
// Prints "A new player has joined the game with 100 coins"
print("There are now \(Bank.coinsInBank) coins left in the bank")
// Prints "There are now 9900 coins left in the bank"
```

<!--
  - test: `deinitializer`

  ```swifttest
  -> var playerOne: Player? = Player(coins: 100)
  -> print("A new player has joined the game with \(playerOne!.coinsInPurse) coins")
  <- A new player has joined the game with 100 coins
  -> print("There are now \(Bank.coinsInBank) coins left in the bank")
  <- There are now 9900 coins left in the bank
  ```
-->

새로운 `Player` 인스턴스가 생성되고, 가능하다면 100개의 코인을 요청한다. 이 `Player` 인스턴스는 `playerOne`이라는 옵셔널 `Player` 변수에 저장된다. 여기서 옵셔널 변수를 사용한 이유는 플레이어가 언제든지 게임을 떠날 수 있기 때문이다. 옵셔널을 사용하면 현재 게임에 플레이어가 있는지 여부를 추적할 수 있다.

`playerOne`이 옵셔널이기 때문에, `coinsInPurse` 프로퍼티에 접근해 초기 코인 수를 출력하거나 `win(coins:)` 메서드를 호출할 때 느낌표(`!`)를 사용해 강제 언래핑한다.

```swift
playerOne!.win(coins: 2_000)
print("PlayerOne won 2000 coins & now has \(playerOne!.coinsInPurse) coins")
// Prints "PlayerOne won 2000 coins & now has 2100 coins"
print("The bank now only has \(Bank.coinsInBank) coins left")
// Prints "The bank now only has 7900 coins left"
```

<!--
  - test: `deinitializer`

  ```swifttest
  -> playerOne!.win(coins: 2_000)
  -> print("PlayerOne won 2000 coins & now has \(playerOne!.coinsInPurse) coins")
  <- PlayerOne won 2000 coins & now has 2100 coins
  -> print("The bank now only has \(Bank.coinsInBank) coins left")
  <- The bank now only has 7900 coins left
  ```
-->

여기서 플레이어는 2,000개의 코인을 획득한다. 플레이어의 지갑에는 이제 2,100개의 코인이 있고, 은행에는 7,900개의 코인이 남아 있다.

```swift
playerOne = nil
print("PlayerOne has left the game")
// Prints "PlayerOne has left the game"
print("The bank now has \(Bank.coinsInBank) coins")
// Prints "The bank now has 10000 coins"
```

<!--
  - test: `deinitializer`

  ```swifttest
  -> playerOne = nil
  -> print("PlayerOne has left the game")
  <- PlayerOne has left the game
  -> print("The bank now has \(Bank.coinsInBank) coins")
  <- The bank now has 10000 coins
  ```
-->

이제 플레이어가 게임을 떠났다. 이는 옵셔널 `playerOne` 변수를 `nil`로 설정해 나타낸다. 이 시점에서 `playerOne` 변수가 참조하던 `Player` 인스턴스의 참조가 끊어진다. 더 이상 다른 프로퍼티나 변수가 이 `Player` 인스턴스를 참조하지 않으므로, 메모리를 해제하기 위해 인스턴스가 제거된다. 이 과정에서 디이니셜라이저가 자동으로 호출되고, 플레이어가 보유한 모든 코인이 은행에 반환된다.

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


