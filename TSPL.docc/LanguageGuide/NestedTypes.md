# 중첩 타입

타입을 다른 타입의 스코프 안에 정의한다.

열거형은 특정 클래스나 구조체의 기능을 지원하기 위해 자주 생성된다. 마찬가지로, 더 복잡한 타입의 컨텍스트 내에서만 사용하기 위한 유틸리티 구조체나 특정 타입과 함께 사용되는 프로토콜을 정의하는 것이 편리할 때가 있다. 이를 위해 Swift는 *중첩 타입*을 정의할 수 있도록 지원한다. 중첩 타입은 열거형, 구조체, 프로토콜과 같은 지원 타입을 해당 타입의 정의 안에 중첩시키는 것을 의미한다.

타입을 다른 타입 안에 중첩시키려면, 지원하는 타입의 외부 중괄호 안에 해당 타입의 정의를 작성한다. 타입은 필요한 만큼의 수준으로 중첩할 수 있다.


## 중첩 타입의 활용

아래 예제는 블랙잭 게임에서 사용하는 카드를 모델링한 `BlackjackCard` 구조체를 정의한다. `BlackjackCard` 구조체는 `Suit`와 `Rank`라는 두 개의 중첩 열거형 타입을 포함한다.

블랙잭에서 에이스 카드는 1 또는 11의 값을 가진다. 이 특징은 `Rank` 열거형 내부에 중첩된 `Values` 구조체로 표현된다:

```swift
struct BlackjackCard {

    // 중첩 Suit 열거형
    enum Suit: Character {
        case spades = "♠", hearts = "♡", diamonds = "♢", clubs = "♣"
    }

    // 중첩 Rank 열거형
    enum Rank: Int {
        case two = 2, three, four, five, six, seven, eight, nine, ten
        case jack, queen, king, ace
        struct Values {
            let first: Int, second: Int?
        }
        var values: Values {
            switch self {
            case .ace:
                return Values(first: 1, second: 11)
            case .jack, .queen, .king:
                return Values(first: 10, second: nil)
            default:
                return Values(first: self.rawValue, second: nil)
            }
        }
    }

    // BlackjackCard 프로퍼티와 메서드
    let rank: Rank, suit: Suit
    var description: String {
        var output = "suit is \(suit.rawValue),"
        output += " value is \(rank.values.first)"
        if let second = rank.values.second {
            output += " or \(second)"
        }
        return output
    }
}
```

<!--
  - test: `nestedTypes`

  ```swifttest
  -> struct BlackjackCard {

        // 중첩 Suit 열거형
        enum Suit: Character {
           case spades = "♠", hearts = "♡", diamonds = "♢", clubs = "♣"
        }

        // 중첩 Rank 열거형
        enum Rank: Int {
           case two = 2, three, four, five, six, seven, eight, nine, ten
           case jack, queen, king, ace
           struct Values {
              let first: Int, second: Int?
           }
           var values: Values {
              switch self {
                 case .ace:
                    return Values(first: 1, second: 11)
                 case .jack, .queen, .king:
                    return Values(first: 10, second: nil)
                 default:
                    return Values(first: self.rawValue, second: nil)
              }
           }
        }

        // BlackjackCard 프로퍼티와 메서드
        let rank: Rank, suit: Suit
        var description: String {
           var output = "suit is \(suit.rawValue),"
           output += " value is \(rank.values.first)"
           if let second = rank.values.second {
              output += " or \(second)"
           }
           return output
        }
     }
  ```
-->

`Suit` 열거형은 네 가지 카드 문양을 설명하며, 각 문양의 심볼을 나타내는 `Character` 원시 값을 가진다.

`Rank` 열거형은 13가지 카드 랭크를 설명하며, 각 랭크의 숫자 값을 나타내는 `Int` 원시 값을 가진다. (잭, 퀸, 킹, 에이스 카드에는 이 원시 값을 사용하지 않는다.)

위에서 언급한 대로, `Rank` 열거형은 `Values`라는 중첩 구조체를 추가로 정의한다. 이 구조체는 대부분의 카드가 하나의 값을 가지지만, 에이스 카드는 두 개의 값을 가진다는 사실을 캡슐화한다. `Values` 구조체는 이를 나타내기 위해 두 가지 프로퍼티를 정의한다:

- `first`: `Int` 타입
- `second`: `Int?` 타입, 즉 "옵셔널 `Int`"

`Rank`는 또한 `values`라는 계산 프로퍼티를 정의한다. 이 프로퍼티는 `Values` 구조체의 인스턴스를 반환한다. 이 계산 프로퍼티는 카드의 랭크를 고려해 적절한 값으로 새로운 `Values` 인스턴스를 초기화한다. 잭, 퀸, 킹, 에이스에 대해 특별한 값을 사용하며, 숫자 카드의 경우 랭크의 원시 `Int` 값을 사용한다.

`BlackjackCard` 구조체 자체는 `rank`와 `suit` 두 가지 프로퍼티를 가진다. 또한 `description`이라는 계산 프로퍼티를 정의하는데, 이 프로퍼티는 `rank`와 `suit`에 저장된 값을 사용해 카드의 이름과 값을 설명하는 문자열을 만든다. `description` 프로퍼티는 옵셔널 바인딩을 사용해 두 번째 값이 있는지 확인하고, 있다면 해당 값을 추가 설명에 포함한다.

`BlackjackCard`는 사용자 정의 이니셜라이저가 없는 구조체이므로, <doc:Initialization#Memberwise-Initializers-for-Structure-Types>에서 설명한 대로 암시적 멤버와이즈 이니셜라이저를 가진다. 이 이니셜라이저를 사용해 `theAceOfSpades`라는 새로운 상수를 초기화할 수 있다:

```swift
let theAceOfSpades = BlackjackCard(rank: .ace, suit: .spades)
print("theAceOfSpades: \(theAceOfSpades.description)")
// Prints "theAceOfSpades: suit is ♠, value is 1 or 11"
```

<!--
  - test: `nestedTypes`

  ```swifttest
  -> let theAceOfSpades = BlackjackCard(rank: .ace, suit: .spades)
  -> print("theAceOfSpades: \(theAceOfSpades.description)")
  <- theAceOfSpades: suit is ♠, value is 1 or 11
  ```
-->

`Rank`와 `Suit`가 `BlackjackCard` 내부에 중첩되어 있더라도, 이들의 타입은 문맥에서 추론할 수 있으므로 이 인스턴스의 초기화는 열거형 케이스를 케이스 이름(`.ace`와 `.spades`)만으로 참조할 수 있다. 위 예제에서 `description` 프로퍼티는 스페이드 에이스가 `1` 또는 `11`의 값을 가진다고 정확히 보고한다.


## 중첩 타입 참조하기

정의된 문맥 밖에서 중첩 타입을 사용하려면, 해당 타입이 속한 타입의 이름을 접두사로 붙인다:

```swift
let heartsSymbol = BlackjackCard.Suit.hearts.rawValue
// heartsSymbol은 "♡"
```

<!--
  - test: `nestedTypes`

  ```swifttest
  -> let heartsSymbol = BlackjackCard.Suit.hearts.rawValue
  /> heartsSymbol is \"\(heartsSymbol)\"
  </ heartsSymbol is "♡"
  ```
-->

위 예제에서 `Suit`, `Rank`, `Values`와 같은 이름은 의도적으로 짧게 유지할 수 있다. 이는 해당 이름들이 정의된 문맥에 의해 자연스럽게 한정되기 때문이다.

<!--
이 소스 파일은 Swift.org 오픈 소스 프로젝트의 일부입니다.

Copyright (c) 2014 - 2022 Apple Inc. 및 Swift 프로젝트 작성자
Apache License v2.0 및 Runtime Library Exception에 따라 라이선스가 부여됨

라이선스 정보는 https://swift.org/LICENSE.txt에서 확인할 수 있습니다.
Swift 프로젝트 작성자 목록은 https://swift.org/CONTRIBUTORS.txt에서 확인할 수 있습니다.
-->


