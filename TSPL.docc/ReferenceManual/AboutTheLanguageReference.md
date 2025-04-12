# 언어 레퍼런스 소개


공식 문법에서 사용하는 표기법을 먼저 숙지한다.

이 부분에서는 Swift 프로그래밍 언어의 공식 문법을 설명한다. 여기서 다루는 문법은 파서나 컴파일러를 직접 구현하기 위한 것이 아니라, 언어를 더 깊이 이해하는 데 도움을 주기 위한 목적으로 작성되었다.

Swift 언어는 상대적으로 작은 규모를 가지고 있다. Swift 코드에서 거의 모든 곳에 등장하는 흔한 타입, 함수, 그리고 연산자들은 실제로 Swift 표준 라이브러리에서 정의되기 때문이다. 이러한 타입, 함수, 그리고 연산자들은 Swift 언어 자체의 일부는 아니지만, 이 부분의 설명과 코드 예제에서 광범위하게 사용된다.


## 문법 읽는 법

Swift 프로그래밍 언어의 공식 문법을 설명하는 데 사용되는 표기법은 몇 가지 규칙을 따른다:

- 화살표(→)는 문법 생성을 표시하며 "~로 구성될 수 있다"로 읽는다.
- 문법 범주는 *기울임꼴*로 표시되며, 문법 생성 규칙의 양쪽에 나타난다.
- 리터럴 단어와 구두점은 **`굵은 고정폭`** 텍스트로 표시되며, 문법 생성 규칙의 오른쪽에만 나타난다.
- 대체 문법 생성은 수직 막대(|)로 구분된다. 대체 생성이 너무 길어 읽기 어려운 경우, 여러 문법 생성 규칙으로 나뉘어 새 줄에 표시된다.
- 몇 가지 경우, 일반 글꼴 텍스트는 문법 생성 규칙의 오른쪽을 설명하는 데 사용된다.
- 선택적 문법 범주와 리터럴은 뒤에 물음표(*?*)를 붙여 표시한다.

예를 들어, getter-setter 블록의 문법은 다음과 같이 정의된다:

> getter-setter 블록의 문법:
>
> *getter-setter-block* → **`{`** *getter-clause* *setter-clause*_?_ **`}`** | **`{`** *setter-clause* *getter-clause* **`}`**

이 정의는 getter-setter 블록이 중괄호로 둘러싸인 getter 절과 선택적 setter 절로 구성될 수 있거나, 중괄호로 둘러싸인 setter 절과 getter 절로 구성될 수 있음을 나타낸다. 위의 문법 생성은 다음과 같이 명시적으로 대체를 나열한 두 가지 생성과 동일하다:

> getter-setter 블록의 문법:
>
> *getter-setter-block* → **`{`** *getter-clause* *setter-clause*_?_ **`}`** \
> *getter-setter-block* → **`{`** *setter-clause* *getter-clause* **`}`**

<!--
This source file is part of the Swift.org open source project

Copyright (c) 2014 - 2022 Apple Inc. and the Swift project authors
Licensed under Apache License v2.0 with Runtime Library Exception

See https://swift.org/LICENSE.txt for license information
See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
-->


