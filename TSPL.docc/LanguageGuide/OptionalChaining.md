# 옵셔널 체이닝

옵셔널 값의 멤버에 접근할 때 언래핑 없이 사용할 수 있다.

*옵셔널 체이닝*은 현재 `nil`일 수 있는 옵셔널 값의 프로퍼티, 메서드, 서브스크립트를 조회하거나 호출하는 과정이다. 옵셔널에 값이 있으면 프로퍼티, 메서드, 서브스크립트 호출이 성공한다. 옵셔널이 `nil`이면 호출 결과로 `nil`을 반환한다. 여러 조회를 체인으로 연결할 수 있으며, 체인 중 어느 하나라도 `nil`이면 전체 체인이 실패한다.

> 참고: Swift의 옵셔널 체이닝은 Objective-C에서 `nil`에 메시지를 보내는 방식과 유사하지만, 모든 타입에 적용할 수 있고 성공 또는 실패를 확인할 수 있다는 점에서 차이가 있다.


## 강제 언래핑 대신 옵셔널 체이닝 사용하기

옵셔널 체이닝은 옵셔널 값 뒤에 물음표(`?`)를 붙여 사용한다. 이는 옵셔널 값이 `nil`이 아닐 때 프로퍼티, 메서드, 서브스크립트를 호출할 수 있게 해준다. 이는 옵셔널 값 뒤에 느낌표(`!`)를 붙여 강제 언래핑하는 것과 유사하지만, 중요한 차이점이 있다. 옵셔널 체이닝은 옵셔널이 `nil`일 때 실패하지만, 강제 언래핑은 옵셔널이 `nil`일 때 런타임 오류를 발생시킨다.

옵셔널 체이닝은 `nil` 값에서도 호출될 수 있다는 사실을 반영하기 위해, 옵셔널 체이닝 호출의 결과는 항상 옵셔널 값이다. 이는 조회하는 프로퍼티, 메서드, 서브스크립트가 비옵셔널 값을 반환하더라도 마찬가지다. 이 옵셔널 반환 값을 통해 옵셔널 체이닝 호출이 성공했는지(반환된 옵셔널에 값이 있음), 체인 내에 `nil` 값이 있어 실패했는지(반환된 옵셔널 값이 `nil`) 확인할 수 있다.

구체적으로, 옵셔널 체이닝 호출의 결과는 예상된 반환 값과 동일한 타입이지만 옵셔널로 감싸져 있다. 예를 들어, 일반적으로 `Int`를 반환하는 프로퍼티는 옵셔널 체이닝을 통해 접근할 때 `Int?`를 반환한다.

다음 코드 스니펫들은 옵셔널 체이닝이 강제 언래핑과 어떻게 다른지, 그리고 성공 여부를 확인하는 방법을 보여준다.

먼저, `Person`과 `Residence`라는 두 클래스를 정의한다:

```swift
class Person {
    var residence: Residence?
}

class Residence {
    var numberOfRooms = 1
}
```

`Residence` 인스턴스는 기본값이 `1`인 `numberOfRooms`라는 단일 `Int` 프로퍼티를 가진다. `Person` 인스턴스는 `Residence?` 타입의 옵셔널 `residence` 프로퍼티를 가진다.

새로운 `Person` 인스턴스를 생성하면, `residence` 프로퍼티는 옵셔널이기 때문에 기본적으로 `nil`로 초기화된다. 아래 코드에서 `john`의 `residence` 프로퍼티 값은 `nil`이다:

```swift
let john = Person()
```

이 사람의 `residence`의 `numberOfRooms` 프로퍼티에 접근하려고 할 때, `residence` 뒤에 느낌표를 붙여 강제 언래핑을 시도하면, 언래핑할 `residence` 값이 없기 때문에 런타임 오류가 발생한다:

```swift
let roomCount = john.residence!.numberOfRooms
// 이 코드는 런타임 오류를 발생시킨다
```

위 코드는 `john.residence`가 `nil`이 아닌 값을 가질 때 성공하고, `roomCount`를 적절한 방의 수를 포함한 `Int` 값으로 설정한다. 그러나 `residence`가 `nil`일 때는 항상 런타임 오류를 발생시킨다.

옵셔널 체이닝은 `numberOfRooms`의 값에 접근하는 대안을 제공한다. 옵셔널 체이닝을 사용하려면 느낌표 대신 물음표를 사용한다:

```swift
if let roomCount = john.residence?.numberOfRooms {
    print("John's residence has \(roomCount) room(s).")
} else {
    print("Unable to retrieve the number of rooms.")
}
// "Unable to retrieve the number of rooms."를 출력한다
```

이 코드는 Swift에게 옵셔널 `residence` 프로퍼티를 "체인"하고, `residence`가 존재할 경우 `numberOfRooms`의 값을 가져오라고 지시한다.

`numberOfRooms`에 접근하려는 시도가 실패할 가능성이 있기 때문에, 옵셔널 체이닝 시도는 `Int?` 타입의 값을 반환한다. 위 예제에서처럼 `residence`가 `nil`일 때, 이 옵셔널 `Int`도 `nil`이 되며, 이는 `numberOfRooms`에 접근할 수 없었음을 반영한다. 옵셔널 `Int`는 옵셔널 바인딩을 통해 접근되어 정수 값을 언래핑하고, 비옵셔널 값을 `roomCount` 상수에 할당한다.

`numberOfRooms`가 비옵셔널 `Int`임에도 불구하고, 옵셔널 체인을 통해 조회되었다는 사실은 `numberOfRooms`에 대한 호출이 항상 `Int` 대신 `Int?`를 반환한다는 것을 의미한다.

`john.residence`에 `Residence` 인스턴스를 할당하여 더 이상 `nil` 값을 갖지 않도록 할 수 있다:

```swift
john.residence = Residence()
```

이제 `john.residence`는 `nil`이 아닌 실제 `Residence` 인스턴스를 포함한다. 이전과 동일한 옵셔널 체이닝을 사용하여 `numberOfRooms`에 접근하면, 이제 기본 `numberOfRooms` 값인 `1`을 포함한 `Int?`를 반환한다:

```swift
if let roomCount = john.residence?.numberOfRooms {
    print("John's residence has \(roomCount) room(s).")
} else {
    print("Unable to retrieve the number of rooms.")
}
// "John's residence has 1 room(s)."를 출력한다
```


## 옵셔널 체이닝을 위한 모델 클래스 정의

옵셔널 체이닝을 사용하면 프로퍼티, 메서드, 서브스크립트를 여러 단계로 호출할 수 있다. 이를 통해 서로 연관된 타입으로 구성된 복잡한 모델의 하위 프로퍼티를 탐색하고, 해당 하위 프로퍼티에 접근이 가능한지 확인할 수 있다.

아래 코드 스니펫은 여러 예제에서 사용할 네 개의 모델 클래스를 정의한다. 이 클래스들은 앞서 다룬 `Person`과 `Residence` 모델을 확장하여 `Room`과 `Address` 클래스를 추가하고, 관련 프로퍼티, 메서드, 서브스크립트를 포함한다.

`Person` 클래스는 이전과 동일한 방식으로 정의한다:

```swift
class Person {
    var residence: Residence?
}
```

<!--
  - test: `optionalChaining`

  ```swifttest
  -> class Person {
        var residence: Residence?
     }
  ```
-->

`Residence` 클래스는 이전보다 더 복잡하다. 이번에는 `Residence` 클래스가 `rooms`라는 변수 프로퍼티를 정의하며, 이 프로퍼티는 `[Room]` 타입의 빈 배열로 초기화된다:

```swift
class Residence {
    var rooms: [Room] = []
    var numberOfRooms: Int {
        return rooms.count
    }
    subscript(i: Int) -> Room {
        get {
            return rooms[i]
        }
        set {
            rooms[i] = newValue
        }
    }
    func printNumberOfRooms() {
        print("The number of rooms is \(numberOfRooms)")
    }
    var address: Address?
}
```

<!--
  - test: `optionalChaining`

  ```swifttest
  -> class Residence {
        var rooms: [Room] = []
        var numberOfRooms: Int {
           return rooms.count
        }
        subscript(i: Int) -> Room {
           get {
              return rooms[i]
           }
           set {
              rooms[i] = newValue
           }
        }
        func printNumberOfRooms() {
           print("The number of rooms is \(numberOfRooms)")
        }
        var address: Address?
     }
  ```
-->

이 버전의 `Residence`는 `Room` 인스턴스의 배열을 저장하므로, `numberOfRooms` 프로퍼티는 저장 프로퍼티가 아닌 계산 프로퍼티로 구현된다. 계산 프로퍼티인 `numberOfRooms`는 단순히 `rooms` 배열의 `count` 프로퍼티 값을 반환한다.

`rooms` 배열에 접근하기 위한 단축키로, 이 버전의 `Residence`는 `rooms` 배열의 특정 인덱스에 있는 방에 접근할 수 있는 읽기-쓰기 서브스크립트를 제공한다.

이 버전의 `Residence`는 또한 `printNumberOfRooms`라는 메서드를 제공하며, 이 메서드는 거주지의 방 개수를 출력한다.

마지막으로, `Residence`는 `Address?` 타입의 옵셔널 프로퍼티인 `address`를 정의한다. 이 프로퍼티의 타입인 `Address` 클래스는 아래에서 정의된다.

`rooms` 배열에 사용되는 `Room` 클래스는 `name`이라는 하나의 프로퍼티와 해당 프로퍼티를 적절한 방 이름으로 설정하는 초기화 메서드를 가진 간단한 클래스다:

```swift
class Room {
    let name: String
    init(name: String) { self.name = name }
}
```

<!--
  - test: `optionalChaining`

  ```swifttest
  -> class Room {
        let name: String
        init(name: String) { self.name = name }
     }
  ```
-->

이 모델의 마지막 클래스는 `Address`다. 이 클래스는 `String?` 타입의 세 가지 옵셔널 프로퍼티를 가진다. 첫 두 프로퍼티인 `buildingName`과 `buildingNumber`는 주소의 일부로 특정 건물을 식별하는 대체 방법이다. 세 번째 프로퍼티인 `street`는 해당 주소의 거리 이름을 지정하는 데 사용된다:

```swift
class Address {
    var buildingName: String?
    var buildingNumber: String?
    var street: String?
    func buildingIdentifier() -> String? {
        if let buildingNumber = buildingNumber, let street = street {
            return "\(buildingNumber) \(street)"
        } else if buildingName != nil {
            return buildingName
        } else {
            return nil
        }
    }
}
```

<!--
  - test: `optionalChaining`

  ```swifttest
  -> class Address {
        var buildingName: String?
        var buildingNumber: String?
        var street: String?
        func buildingIdentifier() -> String? {
           if let buildingNumber, let street {
               return "\(buildingNumber) \(street)"
           } else if buildingName != nil {
               return buildingName
           } else {
               return nil
           }
        }
     }
  ```
-->

`Address` 클래스는 또한 `buildingIdentifier()`라는 메서드를 제공하며, 이 메서드의 반환 타입은 `String?`이다. 이 메서드는 주소의 프로퍼티를 확인하고, `buildingName`에 값이 있으면 이를 반환하거나, `buildingNumber`와 `street` 모두 값이 있으면 이를 연결하여 반환한다. 그렇지 않으면 `nil`을 반환한다.


## 옵셔널 체이닝을 통한 프로퍼티 접근

<doc:OptionalChaining#Optional-Chaining-as-an-Alternative-to-Forced-Unwrapping>에서 보여준 것처럼,
옵셔널 체이닝을 사용해 옵셔널 값의 프로퍼티에 접근하고,
그 접근이 성공했는지 확인할 수 있다.

앞서 정의한 클래스를 사용해 새로운 `Person` 인스턴스를 생성하고,
이전과 같이 `numberOfRooms` 프로퍼티에 접근해 보자:

```swift
let john = Person()
if let roomCount = john.residence?.numberOfRooms {
    print("John's residence has \(roomCount) room(s).")
} else {
    print("Unable to retrieve the number of rooms.")
}
// Prints "Unable to retrieve the number of rooms."
```

<!--
  - test: `optionalChaining`

  ```swifttest
  -> let john = Person()
  -> if let roomCount = john.residence?.numberOfRooms {
        print("John's residence has \(roomCount) room(s).")
     } else {
        print("Unable to retrieve the number of rooms.")
     }
  <- Unable to retrieve the number of rooms.
  ```
-->

`john.residence`가 `nil`이기 때문에,
이 옵셔널 체이닝 호출은 이전과 동일하게 실패한다.

옵셔널 체이닝을 통해 프로퍼티 값을 설정하려는 시도도 할 수 있다:

```swift
let someAddress = Address()
someAddress.buildingNumber = "29"
someAddress.street = "Acacia Road"
john.residence?.address = someAddress
```

<!--
  - test: `optionalChaining`

  ```swifttest
  -> let someAddress = Address()
  -> someAddress.buildingNumber = "29"
  -> someAddress.street = "Acacia Road"
  -> john.residence?.address = someAddress
  ```
-->

이 예제에서 `john.residence`의 `address` 프로퍼티를 설정하려는 시도는 실패한다.
현재 `john.residence`가 `nil`이기 때문이다.

할당은 옵셔널 체이닝의 일부로 이루어지며,
이는 `=` 연산자의 오른쪽에 있는 코드가 평가되지 않음을 의미한다.
이전 예제에서는 `someAddress`가 평가되지 않았는지 쉽게 확인하기 어렵다.
상수에 접근하는 것은 어떤 부작용도 없기 때문이다.
아래 목록은 동일한 할당을 수행하지만,
주소를 생성하기 위해 함수를 사용한다.
함수는 값을 반환하기 전에 "Function was called"를 출력하므로,
`=` 연산자의 오른쪽이 평가되었는지 확인할 수 있다.

```swift
func createAddress() -> Address {
    print("Function was called.")

    let someAddress = Address()
    someAddress.buildingNumber = "29"
    someAddress.street = "Acacia Road"

    return someAddress
}
john.residence?.address = createAddress()
```

<!--
  - test: `optionalChaining`

  ```swifttest
  -> func createAddress() -> Address {
         print("Function was called.")

         let someAddress = Address()
         someAddress.buildingNumber = "29"
         someAddress.street = "Acacia Road"

         return someAddress
     }
  -> john.residence?.address = createAddress()
  >> let _ = createAddress()
  << Function was called.
  ```
-->

`createAddress()` 함수가 호출되지 않았음을 알 수 있다.
아무것도 출력되지 않았기 때문이다.


## 옵셔널 체이닝을 통해 메서드 호출하기

옵셔널 체이닝을 사용하면 옵셔널 값에 대해 메서드를 호출하고, 그 호출이 성공했는지 확인할 수 있다. 이 방법은 메서드가 반환 값을 정의하지 않은 경우에도 사용할 수 있다.

`Residence` 클래스의 `printNumberOfRooms()` 메서드는 `numberOfRooms`의 현재 값을 출력한다. 이 메서드는 다음과 같이 정의된다:

```swift
func printNumberOfRooms() {
    print("The number of rooms is \(numberOfRooms)")
}
```

이 메서드는 반환 타입을 명시하지 않는다. 하지만 반환 타입이 없는 함수와 메서드는 암시적으로 `Void` 타입을 반환한다. 이는 <doc:Functions#Functions-Without-Return-Values>에서 설명한 바와 같다. 즉, `()` 또는 빈 튜플을 반환한다는 의미이다.

옵셔널 체이닝을 통해 이 메서드를 호출하면, 반환 타입은 `Void`가 아니라 `Void?`가 된다. 옵셔널 체이닝을 통해 호출된 경우 반환 값은 항상 옵셔널 타입이기 때문이다. 이를 통해 `printNumberOfRooms()` 메서드 호출이 가능했는지 확인할 수 있다. 메서드 자체가 반환 값을 정의하지 않더라도 `printNumberOfRooms` 호출의 반환 값을 `nil`과 비교하여 호출이 성공했는지 확인할 수 있다:

```swift
if john.residence?.printNumberOfRooms() != nil {
    print("It was possible to print the number of rooms.")
} else {
    print("It was not possible to print the number of rooms.")
}
// Prints "It was not possible to print the number of rooms."
```

옵셔널 체이닝을 통해 프로퍼티를 설정하려는 경우에도 동일한 원리가 적용된다. 앞서 <doc:OptionalChaining#Accessing-Properties-Through-Optional-Chaining>에서 다룬 예제는 `john.residence`가 `nil`임에도 불구하고 `address` 값을 설정하려고 시도한다. 옵셔널 체이닝을 통해 프로퍼티를 설정하려는 모든 시도는 `Void?` 타입의 값을 반환한다. 이를 통해 `nil`과 비교하여 프로퍼티가 성공적으로 설정되었는지 확인할 수 있다:

```swift
if (john.residence?.address = someAddress) != nil {
    print("It was possible to set the address.")
} else {
    print("It was not possible to set the address.")
}
// Prints "It was not possible to set the address."
```


## 옵셔널 체이닝을 통해 서브스크립트 접근하기

옵셔널 체이닝을 사용하면 옵셔널 값의 서브스크립트에서 값을 가져오거나 설정할 수 있으며, 서브스크립트 호출이 성공했는지 확인할 수 있다.

> 참고: 옵셔널 체이닝을 통해 옵셔널 값의 서브스크립트에 접근할 때, 물음표는 서브스크립트의 대괄호 *앞*에 위치한다. 옵셔널 체이닝의 물음표는 항상 옵셔널인 표현식 부분 바로 뒤에 온다.

아래 예제는 `Residence` 클래스에 정의된 서브스크립트를 사용해 `john.residence` 프로퍼티의 `rooms` 배열에서 첫 번째 방의 이름을 가져오려고 시도한다. 현재 `john.residence`가 `nil`이기 때문에 서브스크립트 호출은 실패한다:

```swift
if let firstRoomName = john.residence?[0].name {
    print("The first room name is \(firstRoomName).")
} else {
    print("Unable to retrieve the first room name.")
}
// Prints "Unable to retrieve the first room name."
```

<!--
  - test: `optionalChaining`

  ```swifttest
  -> if let firstRoomName = john.residence?[0].name {
        print("The first room name is \(firstRoomName).")
     } else {
        print("Unable to retrieve the first room name.")
     }
  <- Unable to retrieve the first room name.
  ```
-->

이 서브스크립트 호출에서 옵셔널 체이닝 물음표는 `john.residence` 바로 뒤, 서브스크립트 대괄호 앞에 위치한다. 왜냐하면 `john.residence`가 옵셔널 체이닝을 시도하는 옵셔널 값이기 때문이다.

마찬가지로, 옵셔널 체이닝을 통해 서브스크립트에 새로운 값을 설정하려고 시도할 수도 있다:

```swift
john.residence?[0] = Room(name: "Bathroom")
```

<!--
  - test: `optionalChaining`

  ```swifttest
  -> john.residence?[0] = Room(name: "Bathroom")
  ```
-->

이 서브스크립트 설정 시도도 `residence`가 현재 `nil`이기 때문에 실패한다.

만약 실제 `Residence` 인스턴스를 생성하고 `john.residence`에 할당한 후, `rooms` 배열에 하나 이상의 `Room` 인스턴스를 추가한다면, 옵셔널 체이닝을 통해 `Residence` 서브스크립트를 사용해 `rooms` 배열의 실제 항목에 접근할 수 있다:

```swift
let johnsHouse = Residence()
johnsHouse.rooms.append(Room(name: "Living Room"))
johnsHouse.rooms.append(Room(name: "Kitchen"))
john.residence = johnsHouse

if let firstRoomName = john.residence?[0].name {
    print("The first room name is \(firstRoomName).")
} else {
    print("Unable to retrieve the first room name.")
}
// Prints "The first room name is Living Room."
```

<!--
  - test: `optionalChaining`

  ```swifttest
  -> let johnsHouse = Residence()
  -> johnsHouse.rooms.append(Room(name: "Living Room"))
  -> johnsHouse.rooms.append(Room(name: "Kitchen"))
  -> john.residence = johnsHouse

  -> if let firstRoomName = john.residence?[0].name {
        print("The first room name is \(firstRoomName).")
     } else {
        print("Unable to retrieve the first room name.")
     }
  <- The first room name is Living Room.
  ```
-->


### 옵셔널 타입의 서브스크립트 접근

서브스크립트가 옵셔널 타입의 값을 반환하는 경우 ---
예를 들어 Swift의 `Dictionary` 타입의 키 서브스크립트와 같은 경우 ---
옵셔널 반환 값에 대해 체이닝을 하려면 서브스크립트의 닫는 대괄호 *뒤에* 물음표를 붙인다:

```swift
var testScores = ["Dave": [86, 82, 84], "Bev": [79, 94, 81]]
testScores["Dave"]?[0] = 91
testScores["Bev"]?[0] += 1
testScores["Brian"]?[0] = 72
// "Dave" 배열은 이제 [91, 82, 84]이고, "Bev" 배열은 [80, 94, 81]이다.
```

<!--
  - test: `optionalChaining`

  ```swifttest
  -> var testScores = ["Dave": [86, 82, 84], "Bev": [79, 94, 81]]
  -> testScores["Dave"]?[0] = 91
  -> testScores["Bev"]?[0] += 1
  -> testScores["Brian"]?[0] = 72
  >> let dave = "Dave"
  >> let bev = "Bev"
  /> the \"Dave\" array is now [\(testScores[dave]![0]), \(testScores[dave]![1]), \(testScores[dave]![2])] and the \"Bev\" array is now [\(testScores[bev]![0]), \(testScores[bev]![1]), \(testScores[bev]![2])]
  </ the "Dave" array is now [91, 82, 84] and the "Bev" array is now [80, 94, 81]
  ```
-->

위 예제는 `testScores`라는 딕셔너리를 정의한다. 이 딕셔너리는 `String` 키를 `Int` 값 배열에 매핑하는 두 개의 키-값 쌍을 포함한다. 예제는 옵셔널 체이닝을 사용해 `"Dave"` 배열의 첫 번째 항목을 `91`로 설정하고, `"Bev"` 배열의 첫 번째 항목을 `1`만큼 증가시키며, `"Brian"` 키에 대한 배열의 첫 번째 항목을 설정하려고 시도한다. 첫 두 호출은 `testScores` 딕셔너리에 `"Dave"`와 `"Bev"` 키가 존재하기 때문에 성공한다. 세 번째 호출은 `testScores` 딕셔너리에 `"Brian"` 키가 없기 때문에 실패한다.


## 다단계 옵셔널 체이닝 연결하기

여러 단계의 옵셔널 체이닝을 연결해 모델 내부의 프로퍼티, 메서드, 서브스크립트에 접근할 수 있다. 하지만 여러 단계의 옵셔널 체이닝을 사용하더라도 반환값의 옵셔널 여부는 달라지지 않는다.

다시 말해:

- 접근하려는 타입이 옵셔널이 아니라면, 옵셔널 체이닝으로 인해 옵셔널 타입이 된다.
- 접근하려는 타입이 이미 옵셔널이라면, 체이닝을 통해 더 옵셔널해지지는 않는다.

따라서:

- `Int` 값을 옵셔널 체이닝으로 접근하면, 체이닝 단계와 상관없이 항상 `Int?`가 반환된다.
- 마찬가지로 `Int?` 값을 옵셔널 체이닝으로 접근하면, 체이닝 단계와 상관없이 항상 `Int?`가 반환된다.

아래 예제는 `john`의 `residence` 프로퍼티의 `address` 프로퍼티의 `street` 프로퍼티에 접근한다. 여기서는 옵셔널 타입인 `residence`와 `address` 프로퍼티를 거치는 두 단계의 옵셔널 체이닝이 사용된다:

```swift
if let johnsStreet = john.residence?.address?.street {
    print("John's street name is \(johnsStreet).")
} else {
    print("Unable to retrieve the address.")
}
// Prints "Unable to retrieve the address."
```

<!--
  - test: `optionalChaining`

  ```swifttest
  -> if let johnsStreet = john.residence?.address?.street {
        print("John's street name is \(johnsStreet).")
     } else {
        print("Unable to retrieve the address.")
     }
  <- Unable to retrieve the address.
  ```
-->

현재 `john.residence`는 유효한 `Residence` 인스턴스를 가지고 있다. 하지만 `john.residence.address`의 값은 현재 `nil`이다. 이 때문에 `john.residence?.address?.street` 호출은 실패한다.

위 예제에서 `street` 프로퍼티의 값을 가져오려고 한다. 이 프로퍼티의 타입은 `String?`이다. 따라서 `john.residence?.address?.street`의 반환값도 `String?`이다. 두 단계의 옵셔널 체이닝이 적용되었지만, 프로퍼티 자체의 옵셔널 타입에 영향을 미치지 않는다.

`john.residence.address`에 실제 `Address` 인스턴스를 할당하고, `street` 프로퍼티에 실제 값을 설정하면, 다단계 옵셔널 체이닝을 통해 `street` 프로퍼티의 값에 접근할 수 있다:

```swift
let johnsAddress = Address()
johnsAddress.buildingName = "The Larches"
johnsAddress.street = "Laurel Street"
john.residence?.address = johnsAddress

if let johnsStreet = john.residence?.address?.street {
    print("John's street name is \(johnsStreet).")
} else {
    print("Unable to retrieve the address.")
}
// Prints "John's street name is Laurel Street."
```

<!--
  - test: `optionalChaining`

  ```swifttest
  -> let johnsAddress = Address()
  -> johnsAddress.buildingName = "The Larches"
  -> johnsAddress.street = "Laurel Street"
  -> john.residence?.address = johnsAddress

  -> if let johnsStreet = john.residence?.address?.street {
        print("John's street name is \(johnsStreet).")
     } else {
        print("Unable to retrieve the address.")
     }
  <- John's street name is Laurel Street.
  ```
-->

이 예제에서 `john.residence`의 `address` 프로퍼티를 설정하는 시도는 성공한다. 현재 `john.residence`는 유효한 `Residence` 인스턴스를 가지고 있기 때문이다.


## 옵셔널 반환 값을 가진 메서드 체이닝

이전 예제에서는 옵셔널 체이닝을 통해 옵셔널 타입의 프로퍼티 값을 가져오는 방법을 보여주었다. 또한 옵셔널 체이닝을 사용해 옵셔널 타입의 값을 반환하는 메서드를 호출하고, 필요한 경우 그 메서드의 반환 값에 대해 추가로 체이닝을 할 수도 있다.

아래 예제는 `Address` 클래스의 `buildingIdentifier()` 메서드를 옵셔널 체이닝을 통해 호출한다. 이 메서드는 `String?` 타입의 값을 반환한다. 앞서 설명한 것처럼, 옵셔널 체이닝을 거친 이 메서드 호출의 최종 반환 타입 역시 `String?`이다:

```swift
if let buildingIdentifier = john.residence?.address?.buildingIdentifier() {
    print("John's building identifier is \(buildingIdentifier).")
}
// Prints "John's building identifier is The Larches."
```

<!--
  - test: `optionalChaining`

  ```swifttest
  -> if let buildingIdentifier = john.residence?.address?.buildingIdentifier() {
        print("John's building identifier is \(buildingIdentifier).")
     }
  <- John's building identifier is The Larches.
  ```
-->

만약 이 메서드의 반환 값에 대해 추가로 옵셔널 체이닝을 수행하고 싶다면, 옵셔널 체이닝 물음표를 메서드의 괄호 *뒤에* 위치시킨다:

```swift
if let beginsWithThe =
    john.residence?.address?.buildingIdentifier()?.hasPrefix("The") {
    if beginsWithThe {
        print("John's building identifier begins with \"The\".")
    } else {
        print("John's building identifier doesn't begin with \"The\".")
    }
}
// Prints "John's building identifier begins with "The"."
```

<!--
  - test: `optionalChaining`

  ```swifttest
  -> if let beginsWithThe =
        john.residence?.address?.buildingIdentifier()?.hasPrefix("The") {
        if beginsWithThe {
           print("John's building identifier begins with \"The\".")
        } else {
           print("John's building identifier doesn't begin with \"The\".")
        }
     }
  <- John's building identifier begins with "The".
  ```
-->

> 주의: 위 예제에서 옵셔널 체이닝 물음표를 괄호 *뒤에* 위치시킨 이유는, 체이닝을 수행하는 대상이 `buildingIdentifier()` 메서드 자체가 아니라 해당 메서드의 반환 값이기 때문이다.

<!--
  TODO: add an example of chaining on a property of optional function type.
  This can then be tied in to a revised description of how
  the sugar for optional protocol requirements works.
-->

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


