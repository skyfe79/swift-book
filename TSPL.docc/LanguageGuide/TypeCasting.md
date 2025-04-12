# 타입 캐스팅

값의 런타임 타입을 확인하고 더 구체적인 타입 정보를 제공한다.

*타입 캐스팅*은 인스턴스의 타입을 확인하거나, 해당 인스턴스를 클래스 계층 구조 내의 다른 슈퍼클래스나 서브클래스로 취급하는 방법이다.

Swift에서 타입 캐스팅은 `is`와 `as` 연산자를 통해 구현된다. 이 두 연산자는 값의 타입을 확인하거나 값을 다른 타입으로 캐스팅하는 간단하고 명확한 방법을 제공한다.

타입 캐스팅을 사용해 특정 프로토콜을 준수하는지 여부를 확인할 수도 있다. 자세한 내용은 <doc:Protocols#Checking-for-Protocol-Conformance>를 참고한다.


## 타입 캐스팅을 위한 클래스 계층 구조 정의

클래스와 서브클래스로 이루어진 계층 구조를 활용하면 특정 클래스 인스턴스의 타입을 확인하고, 동일한 계층 구조 내에서 다른 클래스로 캐스팅할 수 있다. 아래 세 개의 코드 스니펫은 타입 캐스팅 예제를 위해 클래스 계층 구조와 해당 클래스의 인스턴스를 포함한 배열을 정의한다.

첫 번째 스니펫은 `MediaItem`이라는 새로운 기본 클래스를 정의한다. 이 클래스는 디지털 미디어 라이브러리에 등장하는 모든 종류의 아이템에 대한 기본 기능을 제공한다. 구체적으로, `String` 타입의 `name` 프로퍼티와 `init(name:)` 초기화 메서드를 선언한다. (모든 미디어 아이템, 영화와 노래를 포함해 이름을 가진다고 가정한다.)

```swift
class MediaItem {
    var name: String
    init(name: String) {
        self.name = name
    }
}
```

<!--
  - test: `typeCasting, typeCasting-err`

  ```swifttest
  -> class MediaItem {
        var name: String
        init(name: String) {
           self.name = name
        }
     }
  ```
-->

다음 스니펫은 `MediaItem`의 두 서브클래스를 정의한다. 첫 번째 서브클래스인 `Movie`는 영화나 필름에 대한 추가 정보를 캡슐화한다. 기본 `MediaItem` 클래스 위에 `director` 프로퍼티와 해당 초기화 메서드를 추가한다. 두 번째 서브클래스인 `Song`은 기본 클래스 위에 `artist` 프로퍼티와 초기화 메서드를 추가한다:

```swift
class Movie: MediaItem {
    var director: String
    init(name: String, director: String) {
        self.director = director
        super.init(name: name)
    }
}

class Song: MediaItem {
    var artist: String
    init(name: String, artist: String) {
        self.artist = artist
        super.init(name: name)
    }
}
```

<!--
  - test: `typeCasting, typeCasting-err`

  ```swifttest
  -> class Movie: MediaItem {
        var director: String
        init(name: String, director: String) {
           self.director = director
           super.init(name: name)
        }
     }

  -> class Song: MediaItem {
        var artist: String
        init(name: String, artist: String) {
           self.artist = artist
           super.init(name: name)
        }
     }
  ```
-->

마지막 스니펫은 `library`라는 상수 배열을 생성한다. 이 배열은 두 개의 `Movie` 인스턴스와 세 개의 `Song` 인스턴스를 포함한다. `library` 배열의 타입은 배열 리터럴의 내용으로 초기화함으로써 추론된다. Swift의 타입 체커는 `Movie`와 `Song`이 `MediaItem`이라는 공통의 슈퍼클래스를 가지고 있다는 것을 추론할 수 있으므로, `library` 배열의 타입을 `[MediaItem]`으로 추론한다:

```swift
let library = [
    Movie(name: "Casablanca", director: "Michael Curtiz"),
    Song(name: "Blue Suede Shoes", artist: "Elvis Presley"),
    Movie(name: "Citizen Kane", director: "Orson Welles"),
    Song(name: "The One And Only", artist: "Chesney Hawkes"),
    Song(name: "Never Gonna Give You Up", artist: "Rick Astley")
]
// the type of "library" is inferred to be [MediaItem]
```

<!--
  - test: `typeCasting`

  ```swifttest
  -> let library = [
        Movie(name: "Casablanca", director: "Michael Curtiz"),
        Song(name: "Blue Suede Shoes", artist: "Elvis Presley"),
        Movie(name: "Citizen Kane", director: "Orson Welles"),
        Song(name: "The One And Only", artist: "Chesney Hawkes"),
        Song(name: "Never Gonna Give You Up", artist: "Rick Astley")
     ]
  >> print(type(of: library))
  << Array<MediaItem>
  // the type of "library" is inferred to be [MediaItem]
  ```
-->

`library`에 저장된 아이템은 여전히 `Movie`와 `Song` 인스턴스다. 그러나 이 배열의 내용을 반복적으로 탐색하면, 반환되는 아이템은 `MediaItem` 타입으로 간주되며, `Movie`나 `Song`으로 간주되지 않는다. 이들을 원래 타입으로 다루려면, 아래에서 설명한 대로 타입을 *확인*하거나 다른 타입으로 *다운캐스팅*해야 한다.


## 타입 확인하기

*타입 확인 연산자* (`is`)를 사용해 인스턴스가 특정 서브클래스 타입인지 확인할 수 있다. 타입 확인 연산자는 인스턴스가 해당 서브클래스 타입이면 `true`를 반환하고, 그렇지 않으면 `false`를 반환한다.

아래 예제는 `library` 배열에서 `Movie`와 `Song` 인스턴스의 개수를 세는 `movieCount`와 `songCount` 변수를 정의한다:

```swift
var movieCount = 0
var songCount = 0

for item in library {
    if item is Movie {
        movieCount += 1
    } else if item is Song {
        songCount += 1
    }
}

print("Media library contains \(movieCount) movies and \(songCount) songs")
// Prints "Media library contains 2 movies and 3 songs"
```

<!--
  - test: `typeCasting`

  ```swifttest
  -> var movieCount = 0
  -> var songCount = 0

  -> for item in library {
        if item is Movie {
           movieCount += 1
        } else if item is Song {
           songCount += 1
        }
     }

  -> print("Media library contains \(movieCount) movies and \(songCount) songs")
  <- Media library contains 2 movies and 3 songs
  ```
-->

이 예제는 `library` 배열의 모든 항목을 순회한다. 각 반복에서 `for`-`in` 루프는 `item` 상수에 배열의 다음 `MediaItem`을 할당한다.

`item is Movie`는 현재 `MediaItem`이 `Movie` 인스턴스인 경우 `true`를 반환하고, 그렇지 않으면 `false`를 반환한다. 마찬가지로, `item is Song`은 항목이 `Song` 인스턴스인지 확인한다. `for`-`in` 루프가 끝나면, `movieCount`와 `songCount`에는 각 타입의 `MediaItem` 인스턴스 개수가 저장된다.


## 다운캐스팅

특정 클래스 타입의 상수나 변수가 실제로는 하위 클래스의 인스턴스를 참조할 수 있다. 이런 경우를 의심할 때, *타입 캐스트 연산자*(`as?` 또는 `as!`)를 사용해 하위 클래스 타입으로 *다운캐스팅*을 시도할 수 있다.

다운캐스팅은 실패할 수 있기 때문에, 타입 캐스트 연산자는 두 가지 형태로 제공된다. 조건부 형태인 `as?`는 다운캐스팅하려는 타입의 옵셔널 값을 반환한다. 강제 형태인 `as!`는 다운캐스팅을 시도하고 결과를 강제 언래핑하는 단일 동작을 수행한다.

다운캐스팅이 성공할지 확신할 수 없을 때는 조건부 형태의 타입 캐스트 연산자(`as?`)를 사용한다. 이 연산자는 항상 옵셔널 값을 반환하며, 다운캐스팅이 불가능한 경우 `nil`을 반환한다. 이를 통해 다운캐스팅이 성공했는지 확인할 수 있다.

다운캐스팅이 항상 성공할 것이라고 확신할 때만 강제 형태의 타입 캐스트 연산자(`as!`)를 사용한다. 이 연산자는 잘못된 클래스 타입으로 다운캐스팅을 시도할 경우 런타임 오류를 발생시킨다.

아래 예제는 `library`에 있는 각 `MediaItem`을 순회하며, 각 항목에 대한 적절한 설명을 출력한다. 이를 위해 각 항목을 `Movie` 또는 `Song`으로 접근해야 한다. 단순히 `MediaItem`으로 접근하는 것만으로는 충분하지 않다. 설명에 사용하기 위해 `Movie`의 `director` 속성이나 `Song`의 `artist` 속성에 접근해야 하기 때문이다.

이 예제에서 배열의 각 항목은 `Movie`일 수도 있고 `Song`일 수도 있다. 각 항목에 대해 어떤 클래스를 사용해야 할지 미리 알 수 없기 때문에, 반복문을 통해 매번 다운캐스팅을 확인하기 위해 조건부 형태의 타입 캐스트 연산자(`as?`)를 사용하는 것이 적절하다:

```swift
for item in library {
    if let movie = item as? Movie {
        print("Movie: \(movie.name), dir. \(movie.director)")
    } else if let song = item as? Song {
        print("Song: \(song.name), by \(song.artist)")
    }
}

// Movie: Casablanca, dir. Michael Curtiz
// Song: Blue Suede Shoes, by Elvis Presley
// Movie: Citizen Kane, dir. Orson Welles
// Song: The One And Only, by Chesney Hawkes
// Song: Never Gonna Give You Up, by Rick Astley
```

<!--
  - test: `typeCasting`

  ```swifttest
  -> for item in library {
        if let movie = item as? Movie {
           print("Movie: \(movie.name), dir. \(movie.director)")
        } else if let song = item as? Song {
           print("Song: \(song.name), by \(song.artist)")
        }
     }

  </ Movie: Casablanca, dir. Michael Curtiz
  </ Song: Blue Suede Shoes, by Elvis Presley
  </ Movie: Citizen Kane, dir. Orson Welles
  </ Song: The One And Only, by Chesney Hawkes
  </ Song: Never Gonna Give You Up, by Rick Astley
  ```
-->

이 예제는 현재 `item`을 `Movie`로 다운캐스팅하는 것으로 시작한다. `item`은 `MediaItem` 인스턴스이기 때문에 `Movie`일 가능성이 있다. 동시에 `Song`일 수도 있고, 단순히 기본 `MediaItem`일 수도 있다. 이러한 불확실성 때문에, 하위 클래스 타입으로 다운캐스팅을 시도할 때 `as?` 형태의 타입 캐스트 연산자는 *옵셔널* 값을 반환한다. `item as? Movie`의 결과는 `Movie?` 타입, 즉 "옵셔널 `Movie`"이다.

`library` 배열에 있는 `Song` 인스턴스에 `Movie`로 다운캐스팅을 시도하면 실패한다. 이를 처리하기 위해 위 예제는 옵셔널 바인딩을 사용해 옵셔널 `Movie`가 실제로 값을 포함하는지 확인한다(즉, 다운캐스팅이 성공했는지 확인한다). 이 옵셔널 바인딩은 “`if let movie = item as? Movie`”로 작성되며, 다음과 같이 읽을 수 있다:

“`item`을 `Movie`로 접근해 보라. 성공한다면, 반환된 옵셔널 `Movie`에 저장된 값을 `movie`라는 새로운 임시 상수로 설정하라.”

다운캐스팅이 성공하면, `movie`의 속성을 사용해 해당 `Movie` 인스턴스에 대한 설명을 출력한다. 여기에는 `director`의 이름이 포함된다. `Song` 인스턴스를 확인하고, `library`에서 `Song`을 찾을 때마다 `artist` 이름을 포함한 적절한 설명을 출력하기 위해 비슷한 원칙이 적용된다.

> 참고: 캐스팅은 실제로 인스턴스를 수정하거나 값을 변경하지 않는다. 기본 인스턴스는 동일하게 유지되며, 단순히 캐스팅된 타입의 인스턴스로 취급되고 접근된다.

<!--
  TODO: This example should be followed by the same example written with switch,
  to introduce type casting in a pattern matching context
  and to set up the crazy Any example at the end of the chapter.
-->

<!--
  TODO: No section on upcasting because nobody can come up with
  an example that isn't excessively contrived.
  The reference shows the behavior in a contrived example.
-->


## Any와 AnyObject를 위한 타입 캐스팅

Swift는 비특정 타입을 다루기 위해 두 가지 특별한 타입을 제공한다:

- `Any`는 함수 타입을 포함한 모든 타입의 인스턴스를 나타낼 수 있다.
- `AnyObject`는 모든 클래스 타입의 인스턴스를 나타낼 수 있다.

`Any`와 `AnyObject`는 명시적으로 그 기능과 동작이 필요할 때만 사용한다. 코드에서 다루는 타입을 구체적으로 지정하는 것이 항상 더 좋다.

다음은 `Any`를 사용해 함수 타입과 비클래스 타입을 포함한 다양한 타입을 다루는 예제다. 이 예제는 `Any` 타입의 값을 저장할 수 있는 `things`라는 배열을 생성한다:

```swift
var things: [Any] = []

things.append(0)
things.append(0.0)
things.append(42)
things.append(3.14159)
things.append("hello")
things.append((3.0, 5.0))
things.append(Movie(name: "Ghostbusters", director: "Ivan Reitman"))
things.append({ (name: String) -> String in "Hello, \(name)" })
```

<!--
  - test: `typeCasting, typeCasting-err`

  ```swifttest
  -> var things: [Any] = []

  -> things.append(0)
  -> things.append(0.0)
  -> things.append(42)
  -> things.append(3.14159)
  -> things.append("hello")
  -> things.append((3.0, 5.0))
  -> things.append(Movie(name: "Ghostbusters", director: "Ivan Reitman"))
  -> things.append({ (name: String) -> String in "Hello, \(name)" })
  ```
-->

`things` 배열은 두 개의 `Int` 값, 두 개의 `Double` 값, 하나의 `String` 값, `(Double, Double)` 타입의 튜플, "Ghostbusters" 영화, 그리고 `String` 값을 받아 다른 `String` 값을 반환하는 클로저 표현식을 포함한다.

`Any` 또는 `AnyObject` 타입으로만 알려진 상수나 변수의 구체적인 타입을 확인하려면, `switch` 문의 케이스에서 `is` 또는 `as` 패턴을 사용할 수 있다. 아래 예제는 `things` 배열의 각 항목을 반복하며 `switch` 문을 사용해 각 항목의 타입을 확인한다. 여러 `switch` 케이스는 매칭된 값을 특정 타입의 상수에 바인딩해 그 값을 출력한다:

```swift
for thing in things {
    switch thing {
    case 0 as Int:
        print("zero as an Int")
    case 0 as Double:
        print("zero as a Double")
    case let someInt as Int:
        print("an integer value of \(someInt)")
    case let someDouble as Double where someDouble > 0:
        print("a positive double value of \(someDouble)")
    case is Double:
        print("some other double value that I don't want to print")
    case let someString as String:
        print("a string value of \"\(someString)\"")
    case let (x, y) as (Double, Double):
        print("an (x, y) point at \(x), \(y)")
    case let movie as Movie:
        print("a movie called \(movie.name), dir. \(movie.director)")
    case let stringConverter as (String) -> String:
        print(stringConverter("Michael"))
    default:
        print("something else")
    }
}

// zero as an Int
// zero as a Double
// an integer value of 42
// a positive double value of 3.14159
// a string value of "hello"
// an (x, y) point at 3.0, 5.0
// a movie called Ghostbusters, dir. Ivan Reitman
// Hello, Michael
```

<!--
  - test: `typeCasting`

  ```swifttest
  -> for thing in things {
        switch thing {
           case 0 as Int:
              print("zero as an Int")
           case 0 as Double:
              print("zero as a Double")
           case let someInt as Int:
              print("an integer value of \(someInt)")
           case let someDouble as Double where someDouble > 0:
              print("a positive double value of \(someDouble)")
           case is Double:
              print("some other double value that I don't want to print")
           case let someString as String:
              print("a string value of \"\(someString)\"")
           case let (x, y) as (Double, Double):
              print("an (x, y) point at \(x), \(y)")
           case let movie as Movie:
              print("a movie called \(movie.name), dir. \(movie.director)")
           case let stringConverter as (String) -> String:
              print(stringConverter("Michael"))
           default:
              print("something else")
        }
     }

  </ zero as an Int
  </ zero as a Double
  </ an integer value of 42
  </ a positive double value of 3.14159
  </ a string value of "hello"
  </ an (x, y) point at 3.0, 5.0
  </ a movie called Ghostbusters, dir. Ivan Reitman
  </ Hello, Michael
  ```
-->

> 참고: `Any` 타입은 옵셔널 타입을 포함한 모든 타입의 값을 나타낼 수 있다. `Any` 타입이 예상되는 곳에 옵셔널 값을 사용하면 Swift는 경고를 표시한다. 만약 옵셔널 값을 `Any` 값으로 사용해야 한다면, 아래와 같이 `as` 연산자를 사용해 명시적으로 옵셔널을 `Any`로 캐스팅할 수 있다.
>
> ```swift
> let optionalNumber: Int? = 3
> things.append(optionalNumber)        // 경고
> things.append(optionalNumber as Any) // 경고 없음
> ```

<!--
  - test: `typeCasting-err`

  ```swifttest
  -> let optionalNumber: Int? = 3
  -> things.append(optionalNumber)        // 경고
  !$ warning: expression implicitly coerced from 'Int?' to 'Any'
  !! things.append(optionalNumber)        // 경고
  !!               ^~~~~~~~~~~~~~
  !$ note: provide a default value to avoid this warning
  !! things.append(optionalNumber)        // 경고
  !!               ^~~~~~~~~~~~~~
  !!                              ?? <#default value#>
  !$ note: force-unwrap the value to avoid this warning
  !! things.append(optionalNumber)        // 경고
  !!               ^~~~~~~~~~~~~~
  !!                              !
  !$ note: explicitly cast to 'Any' with 'as Any' to silence this warning
  !! things.append(optionalNumber)        // 경고
  !!               ^~~~~~~~~~~~~~
  !!                              as Any
  -> things.append(optionalNumber as Any) // 경고 없음
  ```
-->

<!--
  Rejected examples to illustrate AnyObject:

  Array of delegates which may conform to one or more of the class's delegate protocols.

  ```
  protocol MovieDelegate {
      func willPlay(movie: Movie)
  }

  class Library {
      var delegates = [AnyObject]
      ...
  }

  for delegate in delegates {
      guard let delegate = delegate as MovieDelegate else { continue }
      delegate.willPlay(movie: m)
  }
  ```

  A userData object for associating some opaque piece of data or state with an API call.

  ```
  class C {
      // Not userInfo -- that's usually a Dictionary
      let userData: AnyObject?  // In Cocoa APIs, userData is a void*
  }
  ```
-->

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


