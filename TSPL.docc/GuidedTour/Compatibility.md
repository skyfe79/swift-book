# 버전 호환성

이전 언어 모드에서 사용 가능한 기능을 알아본다.

이 책은 Xcode 16.3에 포함된 기본 버전인 Swift 6.1을 설명한다. Swift 6.1 컴파일러를 사용해 Swift 6.1, Swift 5, Swift 4.2, Swift 4로 작성된 코드를 빌드할 수 있다.

Swift 6.1 컴파일러를 사용해 Swift 5 언어 모드로 작성된 코드를 빌드할 때, Swift 6.1의 새로운 기능을 사용할 수 있다. 이 기능들은 기본적으로 활성화되거나, 곧 추가될 기능 플래그를 통해 활성화된다. 그러나 엄격한 동시성 검사를 활성화하려면 Swift 6.1 언어 모드로 업그레이드해야 한다.

또한, Xcode 15.3을 사용해 Swift 4와 Swift 4.2 코드를 빌드할 때, 대부분의 Swift 5 기능을 여전히 사용할 수 있다. 하지만 Swift 5 언어 모드를 사용하는 코드에서만 다음 변경 사항을 적용할 수 있다:

- 불투명 타입을 반환하는 함수는 Swift 5.1 런타임이 필요하다.
- `try?` 표현식은 이미 옵셔널을 반환하는 표현식에 추가적인 옵셔널 레벨을 도입하지 않는다.
- 큰 정수 리터럴 초기화 표현식은 올바른 정수 타입으로 추론된다. 예를 들어, `UInt64(0xffff_ffff_ffff_ffff)`는 오버플로우 없이 올바른 값을 평가한다.

동시성 기능을 사용하려면 Swift 5 언어 모드와 해당 동시성 타입을 제공하는 Swift 표준 라이브러리 버전이 필요하다. Apple 플랫폼에서는 iOS 13, macOS 10.15, tvOS 13, watchOS 6, visionOS 1 이상의 배포 대상(target)을 설정해야 한다.

Swift 6.1로 작성된 타겟은 Swift 5, Swift 4.2, Swift 4로 작성된 타겟에 의존할 수 있으며, 그 반대도 가능하다. 즉, 여러 프레임워크로 나뉜 대규모 프로젝트가 있다면, 한 번에 하나의 프레임워크씩 새로운 언어 버전으로 마이그레이션할 수 있다.

<!--
이 소스 파일은 Swift.org 오픈 소스 프로젝트의 일부입니다.

Copyright (c) 2014 - 2022 Apple Inc. 및 Swift 프로젝트 기여자
Apache License v2.0 및 Runtime Library Exception에 따라 라이선스가 부여됨

라이선스 정보는 https://swift.org/LICENSE.txt에서 확인할 수 있습니다.
Swift 프로젝트 기여자 목록은 https://swift.org/CONTRIBUTORS.txt에서 확인할 수 있습니다.
-->


