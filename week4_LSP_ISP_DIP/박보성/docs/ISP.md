인터페이스 분리의 원칙
-

*불필요한 짐을 실은 무언가에 의존한다면 예상치 못한 문제에 빠질 수 있다!*

- 필요이상의 많은 내용을 포함하는 모듈에 의존하는 것은 해롭다.
- 소스코드 수준에서 이유를 찾자면 불필요한 재컴파일과 재배포가 일어나기 때문이다.
- 이는 고수준의 아키텍쳐에서도 마찬가지이다.
- 예를 들어 장고를 사용하면 반드시 장고 ORM을 사용해야한다고 하면 의존성이 생긴다.
- 만약 장고 ORM이 아닌 참신한 기술을 도입하려한다면, 장고 ORM에 걸려있는 의존성이 문제를 일으킬 수도 있다.
- Archetecture pattern with python에서 구현한 ORM의 분리 등이 예시가 될 수 있을 것 같다.

