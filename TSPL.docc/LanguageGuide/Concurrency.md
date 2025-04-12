# 동시성(Concurrency)


비동기 작업을 수행한다.

Swift는 구조화된 방식으로 비동기 및 병렬 코드를 작성할 수 있도록 내장된 지원을 제공한다.  
*비동기 코드*는 잠시 중단되었다가 나중에 다시 실행될 수 있으며, 프로그램의 한 부분만 동시에 실행된다.  
프로그램 내에서 코드를 중단하고 재개하는 방식은 UI 업데이트와 같은 단기 작업을 계속 진행하면서,  
네트워크를 통해 데이터를 가져오거나 파일을 파싱하는 것과 같은 장기 작업도 동시에 처리할 수 있게 한다.  
*병렬 코드*는 여러 코드 조각이 동시에 실행되는 것을 의미한다.  
예를 들어, 4코어 프로세서를 가진 컴퓨터는 각 코어가 하나의 작업을 수행하며  
동시에 4개의 코드 조각을 실행할 수 있다.  
병렬 및 비동기 코드를 사용하는 프로그램은 여러 작업을 동시에 수행하며,  
외부 시스템을 기다리는 작업은 일시 중단한다.

병렬 또는 비동기 코드를 사용하면 스케줄링 유연성이 증가하지만,  
복잡성도 함께 증가한다는 단점이 있다.  
Swift는 컴파일 타임에 일부 문제를 잡아낼 수 있도록  
의도를 명확히 표현할 수 있는 방법을 제공한다.  
예를 들어, 액터를 사용해 변경 가능한 상태에 안전하게 접근할 수 있다.  
하지만 느리거나 버그가 있는 코드에 동시성을 추가한다고 해서  
빠르거나 정확해진다는 보장은 없다.  
오히려 동시성을 추가하면 코드 디버깅이 더 어려워질 수도 있다.  
그러나 동시성이 필요한 코드에서 Swift의 언어 수준 지원을 사용하면  
컴파일 타임에 문제를 잡아내는 데 도움을 받을 수 있다.

이 장의 나머지 부분에서는 *동시성*이라는 용어를  
비동기 및 병렬 코드의 일반적인 조합을 지칭하는 데 사용한다.

> 참고: 이전에 동시성 코드를 작성해본 적이 있다면,  
> 스레드를 다루는 것에 익숙할 것이다.  
> Swift의 동시성 모델은 스레드 위에 구축되었지만,  
> 직접적으로 스레드를 다루지는 않는다.  
> Swift의 비동기 함수는 실행 중인 스레드를 포기할 수 있으며,  
> 이렇게 하면 첫 번째 함수가 블로킹된 동안  
> 다른 비동기 함수가 해당 스레드에서 실행될 수 있다.  
> 비동기 함수가 재개될 때, Swift는  
> 해당 함수가 어떤 스레드에서 실행될지 보장하지 않는다.

Swift의 언어 지원 없이도 동시성 코드를 작성할 수는 있지만,  
그런 코드는 읽기 어려운 경향이 있다.  
예를 들어, 다음 코드는 사진 이름 목록을 다운로드하고,  
목록의 첫 번째 사진을 다운로드한 후,  
사용자에게 해당 사진을 보여준다:

```swift
listPhotos(inGallery: "Summer Vacation") { photoNames in
    let sortedNames = photoNames.sorted()
    let name = sortedNames[0]
    downloadPhoto(named: name) { photo in
        show(photo)
    }
}
```

이렇게 간단한 경우에도, 코드를 완료 핸들러 시리즈로 작성해야 하기 때문에  
중첩된 클로저를 사용하게 된다.  
이런 스타일에서는, 깊은 중첩이 있는 더 복잡한 코드가  
금방 다루기 어려워질 수 있다.


## 비동기 함수 정의와 호출

*비동기 함수* 또는 *비동기 메서드*는 실행 중간에 일시 중단될 수 있는 특별한 종류의 함수나 메서드다. 일반적인 동기 함수와 달리, 비동기 함수는 완료되거나 오류를 던지거나 반환하지 않을 수 있지만, 실행 중간에 대기 상태로 일시 중단될 수도 있다. 비동기 함수나 메서드 내부에서는 실행이 중단될 수 있는 지점을 명시적으로 표시한다.

함수나 메서드가 비동기임을 나타내려면, `async` 키워드를 선언부에 추가한다. 반환 값이 있는 경우, 반환 화살표(`->`) 앞에 `async`를 쓴다. 예를 들어, 갤러리에서 사진 이름을 가져오는 함수는 다음과 같이 작성할 수 있다:

```swift
func listPhotos(inGallery name: String) async -> [String] {
    let result = // ... 비동기 네트워킹 코드 ...
    return result
}
```

비동기이면서 오류를 던지는 함수나 메서드의 경우, `async`를 `throws` 앞에 쓴다.

비동기 메서드를 호출할 때는 해당 메서드가 반환될 때까지 실행이 일시 중단된다. 호출 앞에 `await`를 추가해 실행이 중단될 수 있는 지점을 표시한다. 이는 오류가 발생할 수 있는 함수를 호출할 때 `try`를 쓰는 것과 유사하다. 비동기 메서드 내부에서는 다른 비동기 메서드를 호출할 때만 실행이 일시 중단되며, 모든 중단 지점은 `await`로 명시적으로 표시된다. 이렇게 하면 동시성 코드를 더 쉽게 읽고 이해할 수 있다.

예를 들어, 아래 코드는 갤러리에 있는 모든 사진의 이름을 가져온 후 첫 번째 사진을 보여준다:

```swift
let photoNames = await listPhotos(inGallery: "Summer Vacation")
let sortedNames = photoNames.sorted()
let name = sortedNames[0]
let photo = await downloadPhoto(named: name)
show(photo)
```

`listPhotos(inGallery:)`와 `downloadPhoto(named:)` 함수는 모두 네트워크 요청을 수행하므로 완료까지 상대적으로 오랜 시간이 걸릴 수 있다. 이 두 함수를 비동기로 만들면, 사진이 준비될 때까지 앱의 나머지 코드가 계속 실행될 수 있다.

위 예제의 동시성 동작을 이해하기 위해, 실행 순서를 살펴보자:

1. 코드는 첫 번째 줄부터 실행되다가 첫 번째 `await`에서 `listPhotos(inGallery:)` 함수를 호출하고, 해당 함수가 반환될 때까지 실행이 일시 중단된다.

2. 이 코드의 실행이 중단된 동안, 프로그램 내의 다른 동시성 코드가 실행될 수 있다. 예를 들어, 오래 걸리는 백그라운드 작업이 새로운 갤러리 목록을 업데이트할 수 있다. 이 코드도 다음 `await` 지점까지 실행되거나 완료된다.

3. `listPhotos(inGallery:)`가 반환되면, 이 코드는 해당 지점부터 실행을 재개하고 반환된 값을 `photoNames`에 할당한다.

4. `sortedNames`와 `name`을 정의하는 줄은 일반적인 동기 코드다. 이 줄들에는 `await`가 없으므로 중단 지점이 없다.

5. 다음 `await`는 `downloadPhoto(named:)` 함수 호출을 표시한다. 이 코드는 해당 함수가 반환될 때까지 다시 실행을 일시 중단하고, 다른 동시성 코드가 실행될 기회를 제공한다.

6. `downloadPhoto(named:)`가 반환되면, 반환 값이 `photo`에 할당되고 `show(_:)`를 호출할 때 인자로 전달된다.

`await`로 표시된 중단 지점은 비동기 함수나 메서드가 반환될 때까지 현재 코드가 실행을 일시 중단할 수 있음을 나타낸다. 이를 *스레드 양보*라고도 한다. Swift는 현재 스레드에서 코드 실행을 일시 중단하고 대신 다른 코드를 실행한다. `await`가 있는 코드는 실행을 중단할 수 있어야 하므로, 비동기 함수나 메서드를 호출할 수 있는 위치는 제한적이다:

- 비동기 함수, 메서드, 프로퍼티의 본문 내부

- `@main`으로 표시된 구조체, 클래스, 열거형의 정적 `main()` 메서드 내부

- 비구조화된 자식 태스크 내부

[`Task.yield()`][] 메서드를 호출해 명시적으로 중단 지점을 추가할 수 있다.

[`Task.yield()`]: https://developer.apple.com/documentation/swift/task/3814840-yield

```swift
func generateSlideshow(forGallery gallery: String) async {
    let photos = await listPhotos(inGallery: gallery)
    for photo in photos {
        // ... 이 사진에 대한 몇 초 분량의 비디오 렌더링 ...
        await Task.yield()
    }
}
```

비디오 렌더링 코드가 동기적이라면 중단 지점이 없다. 렌더링 작업이 오래 걸릴 수 있지만, 주기적으로 `Task.yield()`를 호출해 명시적으로 중단 지점을 추가할 수 있다. 이렇게 하면 Swift가 이 작업의 진행과 프로그램 내 다른 작업의 진행을 균형 있게 조절할 수 있다.

[`Task.sleep(for:tolerance:clock:)`][] 메서드는 동시성 작동 방식을 배우기 위한 간단한 코드를 작성할 때 유용하다. 이 메서드는 현재 태스크를 최소 지정된 시간 동안 일시 중단한다. 다음은 `sleep(for:tolerance:clock:)`을 사용해 네트워크 작업 대기를 시뮬레이션하는 `listPhotos(inGallery:)` 함수의 예시다:

[`Task.sleep(for:tolerance:clock:)`]: https://developer.apple.com/documentation/swift/task/sleep(for:tolerance:clock:)

```swift
func listPhotos(inGallery name: String) async throws -> [String] {
    try await Task.sleep(for: .seconds(2))
    return ["IMG001", "IMG99", "IMG0404"]
}
```

위 코드의 `listPhotos(inGallery:)` 함수는 비동기이면서 오류를 던질 수 있다. 이 함수를 호출할 때는 `try`와 `await`를 모두 쓴다:

```swift
let photos = try await listPhotos(inGallery: "A Rainy Weekend")
```

비동기 함수는 오류를 던지는 함수와 몇 가지 유사점이 있다. 비동기 또는 오류를 던지는 함수를 정의할 때 `async` 또는 `throws`를 표시하고, 해당 함수를 호출할 때 `await` 또는 `try`를 쓴다. 비동기 함수는 다른 비동기 함수를 호출할 수 있으며, 오류를 던지는 함수는 다른 오류를 던지는 함수를 호출할 수 있다.

하지만 중요한 차이점이 있다. 오류를 던지는 코드는 `do`-`catch` 블록으로 감싸 오류를 처리하거나, `Result`를 사용해 오류를 저장할 수 있다. 이 방법을 사용하면 오류를 던지는 함수를 비동기 코드에서 호출할 수 있다. 예를 들어:

```swift
func availableRainyWeekendPhotos() -> Result<[String], Error> {
    return Result {
        try listDownloadedPhotos(inGallery: "A Rainy Weekend")
    }
}
```

반면, 비동기 코드를 감싸 동기 코드에서 호출하고 결과를 기다리는 안전한 방법은 없다. Swift 표준 라이브러리는 의도적으로 이 불안전한 기능을 제외했다. 이를 직접 구현하려고 하면 경합 조건, 스레딩 문제, 교착 상태 등의 문제가 발생할 수 있다. 기존 프로젝트에 동시성 코드를 추가할 때는 상위 계층부터 작업을 시작해야 한다. 구체적으로, 가장 상위 계층의 코드를 동시성을 사용하도록 변환한 후, 호출하는 함수와 메서드를 하나씩 변환하며 프로젝트 아키텍처를 따라 작업한다. 동기 코드는 비동기 코드를 호출할 수 없으므로 하향식 접근 방식만 가능하다.


## 비동기 클로저

함수를 비동기로 만들 수 있는 것처럼, 클로저도 비동기로 만들 수 있다. 클로저 안에 `await`가 포함되면 암시적으로 비동기 클로저가 된다. 명시적으로 표시하려면 `async -> in`을 사용한다.

(여기서 `@MainActor` 클로저에 대한 논의도 함께 다룰 수 있다)


## 비동기 시퀀스

이전 섹션의 `listPhotos(inGallery:)` 함수는 배열의 모든 요소가 준비된 후 한 번에 전체 배열을 비동기적으로 반환한다. 또 다른 접근 방식은 *비동기 시퀀스*를 사용해 컬렉션의 요소를 하나씩 기다리는 것이다. 비동기 시퀀스를 순회하는 방법은 다음과 같다:

```swift
import Foundation

let handle = FileHandle.standardInput
for try await line in handle.bytes.lines {
    print(line)
}
```

<!--
  - test: `async-sequence`

  ```swifttest
  -> import Foundation

  >> func f() async throws {
  -> let handle = FileHandle.standardInput
  -> for try await line in handle.bytes.lines {
         print(line)
     }
  >> }
  ```
-->

일반적인 `for`-`in` 루프 대신, 위 예제에서는 `for` 뒤에 `await`를 사용한다. 비동기 함수나 메서드를 호출할 때와 마찬가지로, `await`는 잠재적인 중단 지점을 나타낸다. `for`-`await`-`in` 루프는 각 반복의 시작 부분에서 다음 요소가 준비될 때까지 실행을 잠시 중단할 수 있다.

<!--
  FIXME TR: 위의 'try'는 어디서 온 것인가?
-->

`for`-`in` 루프에서 사용자 정의 타입을 사용하려면 [`Sequence`][] 프로토콜을 준수해야 하는 것처럼, `for`-`await`-`in` 루프에서 사용자 정의 타입을 사용하려면 [`AsyncSequence`] 프로토콜을 준수해야 한다.

[`Sequence`]: https://developer.apple.com/documentation/swift/sequence
[`AsyncSequence`]: https://developer.apple.com/documentation/swift/asyncsequence

<!--
  TODO ``Series``라는 통화 타입은 어떻게 되었는가?
  Combine에서 나온 것인가?

  또한... 비동기 시퀀스를 생성하는 실제 API가 필요하다.
  여기서 전체 과정을 설명하는 대신,
  프로토콜 참조에 충분한 세부 정보가 있으므로 해당 부분을 보여주는 것이 좋다.
  stdlib에는 AsyncFooSequence 타입 외에는 아무것도 없다.
  다른 Apple 프레임워크의 준수 타입 중 하나를 사용할 수 있을까 --
  Foundation의 FileHandle.AsyncBytes (myFilehandle.bytes.lines)는 어떨까?

  https://developer.apple.com/documentation/swift/asyncsequence
  https://developer.apple.com/documentation/foundation/filehandle

  stdlib에서 비동기 시퀀스 타입을 제공받게 되면,
  위의 내용을 같은 서술 흐름에 맞게 다시 작성하자.
  예를 들어 다음과 같은 코드를 사용할 수 있다.

  let names = await listPhotos(inGallery: "Winter Vacation")
  for await photo in Photos(names: names) {
      show(photo)
  }
-->


## 비동기 함수를 병렬로 호출하기

`await`를 사용해 비동기 함수를 호출하면 한 번에 하나의 코드만 실행한다. 비동기 코드가 실행되는 동안 호출자는 해당 코드가 완료될 때까지 기다린 후 다음 코드를 실행한다. 예를 들어, 갤러리에서 처음 세 개의 사진을 가져오려면 `downloadPhoto(named:)` 함수를 세 번 호출하고 각 호출에 `await`를 사용할 수 있다.

```swift
let firstPhoto = await downloadPhoto(named: photoNames[0])
let secondPhoto = await downloadPhoto(named: photoNames[1])
let thirdPhoto = await downloadPhoto(named: photoNames[2])

let photos = [firstPhoto, secondPhoto, thirdPhoto]
show(photos)
```

<!--
  - test: `defining-async-function`

  ```swifttest
  >> func show(_ images: [Data]) { }
  >> func ff() async {
  >> let photoNames = ["IMG001", "IMG99", "IMG0404"]
  -> let firstPhoto = await downloadPhoto(named: photoNames[0])
  -> let secondPhoto = await downloadPhoto(named: photoNames[1])
  -> let thirdPhoto = await downloadPhoto(named: photoNames[2])

  -> let photos = [firstPhoto, secondPhoto, thirdPhoto]
  -> show(photos)
  >> }
  ```
-->

이 방식에는 중요한 단점이 있다. 다운로드가 비동기로 진행되면서 다른 작업을 할 수 있지만, 한 번에 하나의 `downloadPhoto(named:)` 호출만 실행된다. 각 사진은 완전히 다운로드된 후에 다음 사진 다운로드가 시작된다. 하지만 이러한 작업은 기다릴 필요가 없다. 각 사진은 독립적으로, 심지어 동시에 다운로드될 수 있다.

비동기 함수를 호출하고 주변 코드와 병렬로 실행하려면 상수를 정의할 때 `let` 앞에 `async`를 쓰고, 상수를 사용할 때마다 `await`를 사용한다.

```swift
async let firstPhoto = downloadPhoto(named: photoNames[0])
async let secondPhoto = downloadPhoto(named: photoNames[1])
async let thirdPhoto = downloadPhoto(named: photoNames[2])

let photos = await [firstPhoto, secondPhoto, thirdPhoto]
show(photos)
```

<!--
  - test: `calling-with-async-let`

  ```swifttest
  >> struct Data {}  // Instead of actually importing Foundation
  >> func show(_ images: [Data]) { }
  >> func downloadPhoto(named name: String) async -> Data { return Data() }
  >> let photoNames = ["IMG001", "IMG99", "IMG0404"]
  >> func f() async {
  -> async let firstPhoto = downloadPhoto(named: photoNames[0])
  -> async let secondPhoto = downloadPhoto(named: photoNames[1])
  -> async let thirdPhoto = downloadPhoto(named: photoNames[2])

  -> let photos = await [firstPhoto, secondPhoto, thirdPhoto]
  -> show(photos)
  >> }
  ```
-->

이 예제에서는 `downloadPhoto(named:)` 호출이 세 번 모두 이전 호출이 완료될 때까지 기다리지 않고 시작된다. 시스템 리소스가 충분하다면 동시에 실행될 수 있다. 이 함수 호출에는 `await`가 표시되지 않는다. 코드는 함수의 결과를 기다리며 중단되지 않기 때문이다. 대신 실행은 `photos`가 정의된 라인까지 계속된다. 이 시점에서 프로그램은 비동기 호출의 결과가 필요하므로, 세 사진이 모두 다운로드될 때까지 실행을 일시 중단하기 위해 `await`를 사용한다.

두 접근 방식의 차이점을 다음과 같이 생각할 수 있다:

- 다음 코드가 함수의 결과에 의존할 때 `await`를 사용해 비동기 함수를 호출한다. 이렇게 하면 작업이 순차적으로 수행된다.
- 결과가 나중에 필요할 때 `async`-`let`을 사용해 비동기 함수를 호출한다. 이렇게 하면 작업을 병렬로 수행할 수 있다.
- `await`와 `async`-`let` 모두 중단되는 동안 다른 코드가 실행될 수 있다.
- 두 경우 모두, 비동기 함수가 반환될 때까지 실행이 일시 중단될 수 있음을 나타내기 위해 `await`로 가능한 중단 지점을 표시한다.

동일한 코드에서 두 접근 방식을 혼합해서 사용할 수도 있다.


## 작업(Task)과 작업 그룹(Task Group)

*작업(Task)*은 프로그램의 일부로 비동기적으로 실행할 수 있는 작업 단위다. 모든 비동기 코드는 어떤 작업의 일부로 실행된다. 하나의 작업은 한 번에 한 가지만 처리하지만, 여러 작업을 생성하면 Swift가 이를 동시에 실행하도록 스케줄링한다.

이전 섹션에서 설명한 `async`-`let` 구문은 암묵적으로 자식 작업을 생성한다. 이 구문은 프로그램에서 실행해야 할 작업을 이미 알고 있을 때 유용하다. 또한 [`TaskGroup`][] 인스턴스를 생성하고 명시적으로 자식 작업을 그룹에 추가할 수도 있다. 이 방식은 우선순위와 취소를 더 세밀하게 제어할 수 있으며, 동적으로 여러 작업을 생성할 수 있다는 장점이 있다.

[`TaskGroup`]: https://developer.apple.com/documentation/swift/taskgroup

작업은 계층 구조로 구성된다. 특정 작업 그룹 내의 모든 작업은 동일한 부모 작업을 가지며, 각 작업은 자식 작업을 가질 수 있다. 작업과 작업 그룹 사이의 명시적인 관계 때문에 이 접근 방식을 *구조적 동시성(structured concurrency)*이라고 부른다. 작업 간의 명시적인 부모-자식 관계는 다음과 같은 장점을 제공한다:

- 부모 작업에서 자식 작업이 완료될 때까지 기다리는 것을 잊어버릴 수 없다.

- 자식 작업에 더 높은 우선순위를 설정하면, 부모 작업의 우선순위도 자동으로 상승한다.

- 부모 작업이 취소되면, 모든 자식 작업도 자동으로 취소된다.

- 작업 지역 값(Task-local values)이 자식 작업으로 효율적이고 자동으로 전파된다.

다음은 여러 사진을 다운로드하는 코드의 또 다른 버전으로, 임의의 수의 사진을 처리할 수 있다:

```swift
await withTaskGroup(of: Data.self) { group in
    let photoNames = await listPhotos(inGallery: "Summer Vacation")
    for name in photoNames {
        group.addTask {
            return await downloadPhoto(named: name)
        }
    }

    for await photo in group {
        show(photo)
    }
}
```

위 코드는 새로운 작업 그룹을 생성하고, 갤러리에 있는 각 사진을 다운로드하기 위해 자식 작업을 생성한다. Swift는 가능한 한 많은 작업을 동시에 실행한다. 자식 작업이 사진 다운로드를 완료하면 해당 사진이 즉시 표시된다. 자식 작업이 완료되는 순서는 보장되지 않으므로, 갤러리의 사진은 어떤 순서로든 표시될 수 있다.

> 참고: 사진 다운로드 코드가 오류를 발생시킬 수 있다면, `withThrowingTaskGroup(of:returning:body:)`를 대신 호출해야 한다.

위 코드 예제에서는 각 사진을 다운로드한 후 표시하므로, 작업 그룹은 어떤 결과도 반환하지 않는다. 결과를 반환하는 작업 그룹을 만들려면, `withTaskGroup(of:returning:body:)`에 전달한 클로저 내부에서 결과를 누적하는 코드를 추가하면 된다.

```swift
let photos = await withTaskGroup(of: Data.self) { group in
    let photoNames = await listPhotos(inGallery: "Summer Vacation")
    for name in photoNames {
        group.addTask {
            return await downloadPhoto(named: name)
        }
    }

    var results: [Data] = []
    for await photo in group {
        results.append(photo)
    }

    return results
}
```

이전 예제와 마찬가지로, 이 예제도 각 사진을 다운로드하기 위해 자식 작업을 생성한다. 이전 예제와 달리, `for`-`await`-`in` 루프는 다음 자식 작업이 완료될 때까지 기다린 후, 해당 작업의 결과를 결과 배열에 추가하고, 모든 자식 작업이 완료될 때까지 계속 기다린다. 마지막으로, 작업 그룹은 다운로드된 사진 배열을 전체 결과로 반환한다.

<!--
TODO:
향후에, 작업 그룹에 의해 생성되는 동시 작업의 수를 제한하는 방법을 보여주기 위해 위 예제를 확장할 수 있다. 
동시에 실행할 작업의 수에 대한 구체적인 지침은 없으며, "코드를 프로파일링한 후 조정하라"는 것이 더 적절하다.

참고:
https://developer.apple.com/videos/play/wwdc2023/10170?time=688

또한 withDiscardingTaskGroup(...)을 보여줄 수도 있다.
이것은 값이 수집되지 않는 자식 작업에 최적화되어 있다.
-->


### 작업 취소

Swift의 동시성 모델은 협력적 취소 방식을 사용한다. 각 작업은 실행 중 적절한 시점에 취소되었는지 확인하고, 취소에 적절히 대응한다. 작업의 종류에 따라 취소에 대한 응답은 다음과 같다:

- `CancellationError`와 같은 오류를 던진다.
- `nil`이나 빈 컬렉션을 반환한다.
- 부분적으로 완료된 작업 결과를 반환한다.

이미지 다운로드 작업은 이미지 크기가 크거나 네트워크가 느릴 경우 시간이 오래 걸릴 수 있다. 사용자가 모든 작업이 완료되기를 기다리지 않고 작업을 중단할 수 있도록 하려면, 작업이 취소되었는지 확인하고 취소된 경우 실행을 중단해야 한다. 작업이 취소를 확인하는 방법은 두 가지다: [`Task.checkCancellation()`][] 타입 메서드를 호출하거나 [`Task.isCancelled`][`Task.isCancelled` type] 타입 프로퍼티를 읽는 것이다. `checkCancellation()`은 작업이 취소된 경우 오류를 던지며, 오류를 던지는 작업은 해당 오류를 작업 외부로 전파하여 모든 작업을 중단한다. 이 방식은 구현과 이해가 간단하다는 장점이 있다. 더 유연한 방법으로 `isCancelled` 프로퍼티를 사용하면, 작업을 중단하면서 네트워크 연결을 닫거나 임시 파일을 삭제하는 등의 정리 작업을 수행할 수 있다.

[`Task.checkCancellation()`]: https://developer.apple.com/documentation/swift/task/3814826-checkcancellation
[`Task.isCancelled` type]: https://developer.apple.com/documentation/swift/task/iscancelled-swift.type.property

```swift
let photos = await withTaskGroup(of: Optional<Data>.self) { group in
    let photoNames = await listPhotos(inGallery: "Summer Vacation")
    for name in photoNames {
        let added = group.addTaskUnlessCancelled {
            guard !Task.isCancelled else { return nil }
            return await downloadPhoto(named: name)
        }
        guard added else { break }
    }

    var results: [Data] = []
    for await photo in group {
        if let photo { results.append(photo) }
    }
    return results
}
```

위 코드는 이전 버전과 비교해 몇 가지 변경 사항이 있다:

- 각 작업은 [`TaskGroup.addTaskUnlessCancelled(priority:operation:)`][] 메서드를 사용해 추가되어, 취소 후 새로운 작업이 시작되지 않도록 한다.

- `addTaskUnlessCancelled(priority:operation:)`를 호출한 후, 새로운 자식 작업이 추가되었는지 확인한다. 그룹이 취소된 경우 `added` 값이 `false`가 되며, 이 경우 추가 이미지 다운로드를 시도하지 않는다.

- 각 작업은 이미지 다운로드를 시작하기 전에 취소되었는지 확인한다. 취소된 경우 `nil`을 반환한다.

- 마지막으로, 작업 그룹은 결과를 수집할 때 `nil` 값을 건너뛴다. `nil`을 반환해 취소를 처리하면, 작업 그룹이 완료된 작업을 버리지 않고 취소 시점까지 다운로드된 이미지를 부분적으로 반환할 수 있다.

[`TaskGroup.addTaskUnlessCancelled(priority:operation:)`]: https://developer.apple.com/documentation/swift/taskgroup/addtaskunlesscancelled(priority:operation:)

> 참고:
> 작업 외부에서 작업이 취소되었는지 확인하려면 타입 프로퍼티 대신 [`Task.isCancelled`][`Task.isCancelled` instance] 인스턴스 프로퍼티를 사용한다.

[`Task.isCancelled` instance]: https://developer.apple.com/documentation/swift/task/iscancelled-swift.property

취소에 대한 즉각적인 알림이 필요한 작업에는 [`Task.withTaskCancellationHandler(operation:onCancel:isolation:)`][] 메서드를 사용한다. 예를 들면:

[`Task.withTaskCancellationHandler(operation:onCancel:isolation:)`]: https://developer.apple.com/documentation/swift/withtaskcancellationhandler(operation:oncancel:isolation:)

```swift
let task = await Task.withTaskCancellationHandler {
    // ...
} onCancel: {
    print("Canceled!")
}

// ... some time later...
task.cancel()  // "Canceled!" 출력
```

취소 핸들러를 사용할 때도 작업 취소는 여전히 협력적이다. 작업은 완료될 때까지 실행되거나 취소를 확인하고 조기에 중단한다. 취소 핸들러가 시작될 때 작업이 여전히 실행 중이므로, 작업과 취소 핸들러 간 상태를 공유하지 않도록 주의해야 한다. 그렇지 않으면 경쟁 조건이 발생할 수 있다.


### 비구조적 동시성

이전 섹션에서 설명한 구조적 동시성 접근 방식 외에도, Swift는 비구조적 동시성도 지원한다. **비구조적 태스크**는 태스크 그룹의 일부가 아니며, 부모 태스크가 없다. 프로그램의 필요에 따라 비구조적 태스크를 자유롭게 관리할 수 있지만, 그 정확성에 대한 책임도 전적으로 개발자에게 있다. 현재 액터에서 실행되는 비구조적 태스크를 생성하려면 [`Task.init(priority:operation:)`][] 이니셜라이저를 호출한다. 현재 액터의 일부가 아닌 비구조적 태스크를 생성하려면, 보다 구체적으로 **분리된 태스크(detached task)**라고 알려진 [`Task.detached(priority:operation:)`][] 클래스 메서드를 호출한다. 이 두 작업 모두 태스크를 반환하며, 결과를 기다리거나 취소하는 등 상호작용할 수 있다.

```swift
let newPhoto = // ... some photo data ...
let handle = Task {
    return await add(newPhoto, toGalleryNamed: "Spring Adventures")
}
let result = await handle.value
```

분리된 태스크를 관리하는 방법에 대한 자세한 내용은 [`Task`](https://developer.apple.com/documentation/swift/task) 문서를 참고한다.

[`Task.init(priority:operation:)`]: https://developer.apple.com/documentation/swift/task/init(priority:operation:)-7f0zv
[`Task.detached(priority:operation:)`]: https://developer.apple.com/documentation/swift/task/detached(priority:operation:)-d24l

<!--
  TODO Add some conceptual guidance about
  when to make a method do its work in a detached task
  versus making the method itself async?
  (Pull from my 2021-04-21 notes from Ben's talk rehearsal.)
-->


## 액터

프로그램을 독립적이고 동시에 실행 가능한 부분으로 나누기 위해 작업(task)을 사용한다. 작업은 서로 격리되어 있어 동시에 실행하기에 안전하지만, 때로는 작업 간에 정보를 공유해야 할 때가 있다. 액터는 동시성 코드 간에 정보를 안전하게 공유할 수 있게 해준다.

클래스와 마찬가지로 액터도 참조 타입이다. 따라서 <doc:ClassesAndStructures#Classes-Are-Reference-Types>에서 설명한 값 타입과 참조 타입의 비교는 액터에도 동일하게 적용된다. 클래스와 달리 액터는 한 번에 하나의 작업만이 자신의 가변 상태에 접근할 수 있도록 허용한다. 이는 여러 작업이 동일한 액터 인스턴스와 상호작용할 때 안전성을 보장한다. 예를 들어, 다음은 온도를 기록하는 액터의 예이다:

```swift
actor TemperatureLogger {
    let label: String
    var measurements: [Int]
    private(set) var max: Int

    init(label: String, measurement: Int) {
        self.label = label
        self.measurements = [measurement]
        self.max = measurement
    }
}
```

<!--
  - test: `actors, actors-implicitly-sendable`

  ```swifttest
  -> actor TemperatureLogger {
         let label: String
         var measurements: [Int]
         private(set) var max: Int

         init(label: String, measurement: Int) {
             self.label = label
             self.measurements = [measurement]
             self.max = measurement
         }
     }
  ```
-->

액터는 `actor` 키워드로 정의하며, 중괄호 안에 구현 내용을 작성한다. `TemperatureLogger` 액터는 외부 코드에서 접근할 수 있는 프로퍼티를 가지며, `max` 프로퍼티는 액터 내부 코드만 업데이트할 수 있도록 제한한다.

구조체와 클래스와 동일한 초기화 구문을 사용해 액터 인스턴스를 생성한다. 액터의 프로퍼티나 메서드에 접근할 때는 잠재적인 중단 지점을 나타내기 위해 `await`를 사용한다. 예를 들어:

```swift
let logger = TemperatureLogger(label: "Outdoors", measurement: 25)
print(await logger.max)
// Prints "25"
```

이 예제에서 `logger.max`에 접근하는 것은 잠재적인 중단 지점이다. 액터는 한 번에 하나의 작업만이 가변 상태에 접근할 수 있도록 허용하기 때문에, 다른 작업이 이미 로거와 상호작용 중이라면 이 코드는 프로퍼티에 접근할 때까지 일시 중단된다.

반대로, 액터의 일부인 코드는 액터의 프로퍼티에 접근할 때 `await`를 작성하지 않는다. 예를 들어, 다음은 새로운 온도로 `TemperatureLogger`를 업데이트하는 메서드이다:

```swift
extension TemperatureLogger {
    func update(with measurement: Int) {
        measurements.append(measurement)
        if measurement > max {
            max = measurement
        }
    }
}
```

`update(with:)` 메서드는 이미 액터에서 실행 중이므로, `max`와 같은 프로퍼티에 접근할 때 `await`를 표시하지 않는다. 이 메서드는 또한 액터가 한 번에 하나의 작업만이 가변 상태와 상호작용할 수 있도록 허용하는 이유 중 하나를 보여준다: 액터의 상태를 업데이트할 때 일시적으로 불변성이 깨질 수 있다. `TemperatureLogger` 액터는 온도 목록과 최대 온도를 추적하며, 새로운 측정값을 기록할 때 최대 온도를 업데이트한다. 업데이트 중간에, 새로운 측정값을 추가한 후 `max`를 업데이트하기 전에, 온도 로거는 일시적으로 일관성이 없는 상태가 된다. 여러 작업이 동시에 동일한 인스턴스와 상호작용하지 못하도록 방지함으로써 다음과 같은 일련의 이벤트로 인한 문제를 방지한다:

1. 코드가 `update(with:)` 메서드를 호출한다. 먼저 `measurements` 배열을 업데이트한다.
2. 코드가 `max`를 업데이트하기 전에, 다른 곳의 코드가 최대값과 온도 배열을 읽는다.
3. 코드가 `max`를 변경하여 업데이트를 완료한다.

이 경우, 다른 곳에서 실행 중인 코드는 `update(with:)` 호출 중간에 액터에 접근했기 때문에 잘못된 정보를 읽게 된다. 데이터가 일시적으로 유효하지 않은 상태였기 때문이다. Swift 액터를 사용하면 이 문제를 방지할 수 있다. 액터는 한 번에 하나의 작업만 상태에 접근할 수 있도록 허용하며, `await`로 표시된 중단 지점에서만 코드가 중단될 수 있기 때문이다. `update(with:)`에는 중단 지점이 없으므로, 업데이트 중간에 다른 코드가 데이터에 접근할 수 없다.

액터 외부의 코드가 프로퍼티에 직접 접근하려고 하면, 구조체나 클래스의 프로퍼티에 접근하는 것처럼 컴파일 타임 오류가 발생한다. 예를 들어:

```swift
print(logger.max)  // Error
```

`await`를 작성하지 않고 `logger.max`에 접근하면 실패한다. 액터의 프로퍼티는 액터의 격리된 로컬 상태의 일부이기 때문이다. 이 프로퍼티에 접근하는 코드는 액터의 일부로 실행되어야 하며, 이는 비동기 작업이므로 `await`를 작성해야 한다. Swift는 액터에서 실행 중인 코드만이 해당 액터의 로컬 상태에 접근할 수 있음을 보장한다. 이 보장을 *액터 격리(actor isolation)*라고 한다.

Swift 동시성 모델의 다음과 같은 측면들이 함께 작용하여 공유 가변 상태를 더 쉽게 추론할 수 있게 한다:

- 잠재적인 중단 지점 사이의 코드는 순차적으로 실행되며, 다른 동시성 코드에 의해 중단되지 않는다.

- 액터의 로컬 상태와 상호작용하는 코드는 해당 액터에서만 실행된다.

- 액터는 한 번에 하나의 코드만 실행한다.

이러한 보장 덕분에, `await`를 포함하지 않고 액터 내부에 있는 코드는 프로그램의 다른 부분에서 일시적으로 유효하지 않은 상태를 관찰할 위험 없이 업데이트를 수행할 수 있다. 예를 들어, 다음 코드는 측정된 온도를 화씨에서 섭씨로 변환한다:

```swift
extension TemperatureLogger {
    func convertFahrenheitToCelsius() {
        for i in measurements.indices {
            measurements[i] = (measurements[i] - 32) * 5 / 9
        }
    }
}
```

위 코드는 측정값 배열을 하나씩 변환한다. 맵 작업이 진행되는 동안 일부 온도는 화씨로, 다른 온도는 섭씨로 남아 있을 수 있다. 그러나 이 메서드에는 `await`가 포함되지 않았으므로 잠재적인 중단 지점이 없다. 이 메서드가 수정하는 상태는 액터에 속하며, 액터는 해당 코드가 액터에서 실행될 때를 제외하고는 코드가 상태를 읽거나 수정하지 못하도록 보호한다. 이는 단위 변환이 진행되는 동안 다른 코드가 부분적으로 변환된 온도 목록을 읽을 수 없음을 의미한다.

잠재적인 중단 지점을 생략하여 일시적으로 유효하지 않은 상태를 보호하는 코드를 액터에 작성하는 것 외에도, 이 코드를 동기 메서드로 옮길 수 있다. 위의 `convertFahrenheitToCelsius()` 메서드는 동기 메서드이므로 잠재적인 중단 지점이 *절대* 포함되지 않음을 보장한다. 이 함수는 데이터 모델을 일시적으로 일관성이 없게 만드는 코드를 캡슐화하며, 코드를 읽는 사람이 작업이 완료되어 데이터 일관성이 복원되기 전에는 다른 코드가 실행될 수 없음을 쉽게 인식할 수 있게 한다. 나중에 이 함수에 동시성 코드를 추가하려고 하면, 잠재적인 중단 지점을 도입하게 되며, 이는 버그를 도입하는 대신 컴파일 타임 오류를 발생시킨다.

<!--
  OUTLINE

  Add this post-WWDC when we have a more solid story to tell around Sendable

   .. _Concurrency_ActorIsolation:

   Actor Isolation
   ~~~~~~~~~~~~~~~

   TODO outline impact from SE-0313 Control Over Actor Isolation
   about the 'isolated' and 'nonisolated' keywords

   - actors protect their mutable state using :newTerm:`actor isolation`
   to prevent data races
   (one actor reading data that's in an inconsistent state
   while another actor is updating/writing to that data)

   - within an actor's implementation,
   you can read and write to properties of ``self`` synchronously,
   likewise for calling methods of ``self`` or ``super``

   - method calls from outside the actor are always async,
   as is reading the value of an actor's property

   - you can't write to a property directly from outside the actor

   TODO: Either define "data race" or use a different term;
   the chapter on exclusive ownership talks about "conflicting access",
   which is related, but different.
   Konrad defines "data race" as concurrent access to shared state,
   noting that our current design doesn't prevent all race conditions
   because suspension points allow for interleaving.

   - The same actor method can be called multiple times, overlapping itself.
   This is sometimes referred to as *reentrant code*.
   The behavior is defined and safe... but might have unexpected results.
   However, the actor model doesn't require or guarantee
   that these overlapping calls behave correctly (that they're *idempotent*).
   Encapsulate state changes in a synchronous function
   or write them so they don't contain an ``await`` in the middle.

   - If a closure is ``@Sendable`` or ``@escaping``
   then it behaves like code outside of the actor
   because it could execute concurrently with other code that's part of the actor

   exercise the log actor, using its client API to mutate state

   ::

       let logger = TemperatureSensor(lines: [
           "Outdoor air temperature",
           "25 C",
           "24 C",
       ])
       print(await logger.getMax())

       await logger.update(with: "27 C")
       print(await logger.getMax())
-->


## 전송 가능 타입(Sendable Types)

작업(Task)과 액터(Actor)를 사용하면 프로그램을 동시에 안전하게 실행할 수 있는 여러 부분으로 나눌 수 있다. 작업이나 액터 인스턴스 내부에서, 변수나 프로퍼티와 같이 변경 가능한 상태를 포함하는 프로그램 부분을 *동시성 도메인(concurrency domain)* 이라고 부른다. 일부 데이터는 변경 가능한 상태를 포함하지만, 동시 접근을 방지하지 않기 때문에 동시성 도메인 간에 공유할 수 없다.

한 동시성 도메인에서 다른 동시성 도메인으로 공유할 수 있는 타입을 *전송 가능 타입(Sendable type)* 이라고 한다. 예를 들어, 액터 메서드를 호출할 때 인자로 전달하거나 작업의 결과로 반환할 수 있다. 이 장의 앞부분 예제에서는 동시성 도메인 간에 전달되는 데이터가 항상 안전하게 공유할 수 있는 단순한 값 타입을 사용했기 때문에 전송 가능성에 대해 다루지 않았다. 반면, 일부 타입은 동시성 도메인 간에 안전하게 전달할 수 없다. 예를 들어, 변경 가능한 프로퍼티를 포함하고 해당 프로퍼티에 대한 접근을 직렬화하지 않는 클래스는 다른 작업 간에 인스턴스를 전달할 때 예측할 수 없고 잘못된 결과를 초래할 수 있다.

타입을 전송 가능으로 표시하려면 `Sendable` 프로토콜을 준수하도록 선언한다. 이 프로토콜은 코드 요구사항은 없지만, Swift가 강제하는 의미론적 요구사항이 있다. 일반적으로 타입이 전송 가능하려면 다음 세 가지 방법 중 하나를 만족해야 한다:

- 타입이 값 타입이고, 변경 가능한 상태가 다른 전송 가능 데이터로 구성된 경우. 예를 들어, 전송 가능한 저장 프로퍼티를 가진 구조체나 전송 가능한 연관 값을 가진 열거형이 여기에 해당한다.
- 타입에 변경 가능한 상태가 없고, 불변 상태가 다른 전송 가능 데이터로 구성된 경우. 예를 들어, 읽기 전용 프로퍼티만 있는 구조체나 클래스가 이에 해당한다.
- 타입이 변경 가능한 상태의 안전성을 보장하는 코드를 포함하는 경우. 예를 들어, `@MainActor`로 표시된 클래스나 특정 스레드나 큐에서 프로퍼티 접근을 직렬화하는 클래스가 이에 해당한다.

의미론적 요구사항에 대한 자세한 목록은 [`Sendable`](https://developer.apple.com/documentation/swift/sendable) 프로토콜 참조 문서를 확인한다.

일부 타입은 항상 전송 가능하다. 예를 들어, 전송 가능한 프로퍼티만 있는 구조체나 전송 가능한 연관 값만 있는 열거형이 이에 해당한다. 예를 들어:

```swift
struct TemperatureReading: Sendable {
    var measurement: Int
}

extension TemperatureLogger {
    func addReading(from reading: TemperatureReading) {
        measurements.append(reading.measurement)
    }
}

let logger = TemperatureLogger(label: "Tea kettle", measurement: 85)
let reading = TemperatureReading(measurement: 45)
await logger.addReading(from: reading)
```

`TemperatureReading`은 전송 가능한 프로퍼티만 있는 구조체이며, `public`이나 `@usableFromInline`으로 표시되지 않았기 때문에 암시적으로 전송 가능하다. 다음은 `Sendable` 프로토콜 준수가 암시된 구조체의 예시다:

```swift
struct TemperatureReading {
    var measurement: Int
}
```

암시적 `Sendable` 프로토콜 준수를 재정의하여 타입을 전송 불가능으로 명시적으로 표시하려면 확장을 사용한다:

```swift
struct FileDescriptor {
    let rawValue: CInt
}

@available(*, unavailable)
extension FileDescriptor: Sendable { }
```

위 코드는 POSIX 파일 디스크립터를 감싸는 래퍼의 일부를 보여준다. 파일 디스크립터 인터페이스가 정수 값을 사용하여 열린 파일을 식별하고 상호작용하지만, 파일 디스크립터는 동시성 도메인 간에 안전하게 전송할 수 없다.

위 코드에서 `FileDescriptor`는 암시적으로 전송 가능한 기준을 충족하는 구조체다. 그러나 확장에서 `Sendable` 준수를 사용할 수 없도록 설정하여 타입이 전송 불가능하게 된다.


