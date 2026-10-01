<br>

# [Object Oriented Programming]

## 1. 概念
オブジェクト指向プログラミングは、関数（振る舞い）と変数（状態）をどのように管理し、データを扱うかに関する方法論です。<br>
オブジェクト指向を活用することで、コードの重複を減らし、保守性を向上させることができます。

> 객체 지향 프로그래밍은 함수(행위)와 변수(상태)를 어떻게 관리할 지, 데이터를 다룰 지에 대한 방법론이다.  
> 객체 지향을 통해 코드의 중복을 감소시키고 유지보수성을 향상시킨다.

<br>

## 2. カプセル化 (Encapsulation)
関連する変数とメソッドを一つにまとめ、外部からの直接的なアクセスを制限（情報隠蔽）すること。  
アクセス修飾子やgetter/setterなどを通じて、許可された方法でのみデータ操作を可能にし、オブジェクトの独立性と安全性を保証する。

> **캡슐화**  
> 관련된 변수와 메서드를 하나로 묶고, 외부의 직접적인 접근을 제한(정보 은닉)하는 것.  
> 접근 제어자 및 getter/setter 등을 통해 허용된 방식으로만 데이터 조작을 가능하게 하여 객체의 독립성과 안전성을 보장한다.

```java
class BankAccount {

    private int balance; // 외부에서 직접 접근 불가능

    public void deposit(int money) {
        if (money > 0) {
            balance += money;
        }
    }

    public int getBalance() {
        return balance;
    }
}
```

<br>

## 3. 継承 (Inheritance)
親クラスの変数とメソッドを子クラスが引き継ぎ、そのまま使用したり再定義（拡張）すること。  
コードの重複記述を減らして再利用性を最大化し、クラス間の階層関係を形成する。

> **상속**  
> 부모 클래스의 변수와 메서드를 자식 클래스가 물려받아 그대로 사용하거나 재정의(확장)하는 것.  
> 코드의 중복 작성을 줄이고 재사용성을 극대화하며, 클래스 간의 계층 관계를 형성한다.

```java
class Animal {
    String name;

    void eat() {
        System.out.println(name + "이(가) 밥을 먹습니다.");
    }
}
// Dog가 Animal의 속성과 기능을 물려받는다
class Dog extends Animal {
    void bark() {
        System.out.println(name + "이(가) 멍멍!");
    }
}

class Cat extends Animal {
    void meow() {
        System.out.println(name + "이(가) 야옹!");
    }
}
```

<br>

## 4. 抽象化 (Abstraction)
複雑な内部実装ロジックを隠し、ユーザーに必要なコア機能（インターフェース）のみを開示すること。  
詳細な動作仕組みを知らなくても、定義された仕様のみでオブジェクトを容易に活用できるようにする。

> **추상화**  
> 복잡한 내부 구현 로직을 감추고, 사용자에게 꼭 필요한 핵심 기능(인터페이스)만 드러내는 것.  
> 세부 동작 방식을 몰라도 정의된 명세만으로 객체를 손쉽게 활용할 수 있게 한다.

```java
// 여기서 Animal은 추상 클래스이기 때문에 직접 객체를 만들 수 없다 (대신 자식 클래스 만들어서 사용)
abstract class Animal {

    String name;

    // Animal을 상속하는 클래스는 반드시 sound()를 만들어야 한다 (자식 클래스마다 해당 메소드 다르게 사용)
    abstract void sound();

    void eat() {
        System.out.println(name + "이(가) 밥을 먹습니다.");
    }
}

class Dog extends Animal {

    @Override  // 어노이테이션 - 부모 클래스에 있는 메소드를 재정의한다는 의미
    void sound() {
        System.out.println("멍멍!");
    }
}

class Cat extends Animal {

    @Override
    void sound() {
        System.out.println("야옹!");
    }
}

// 호출하는 쪽 입장에서는 구현방법을 알지 못해도 된다 (추상화와 다형성이 만나는 지점)

// Dog는 Animal의 자식 클래스이기 때문에 Animal 타입의 변수에 주소값을 저장할 수 있다
Animal animal = new Dog();
animal.sound();

Animal animal = new Cat();
animal.sound();

// 구체적인 구현을 몰라도, 그 객체가 제공하는 핵심적인 "무엇을 할 수 있는가"만 알고 사용할 수 있도록 만드는 설계를 추상화라고 한다
```

<br>

## 5. 多態性 / ポリモーフィズム (Polymorphism)
一つの型やメソッドが状況に応じて多様な形態で動作すること。  
上位型の参照変数で複数の下位型オブジェクトを扱ったり、メソッドオーバーライドを通じてコードの柔軟性と拡張性を最大化する。

> **다형성**  
> 하나의 타입이나 메서드가 상황에 따라 다양한 형태로 동작하는 것.  
> 상위 타입의 참조 변수로 여러 하위 타입 객체를 다루거나, 메서드 오버라이딩을 통해 코드의 유연성과 확장성을 극대화한다.

```java
Animal animal;

animal = new Dog();
animal.sound(); // 멍멍

animal = new Cat();
animal.sound(); // 야옹

// 여기서 animal 변수는 하나의 자식 클래스 객체만을 참조한다
// 즉, 같은 변수로 자식 객체를 번갈아 넣으면 기존 객체는 참조가 끊길 수 있고, JVM의 Garbage Collector가 실행 중에 회수할 수 있다.
// 그렇기 때문에 메모리 배치를 이미 한 번한 객체더라도, 변수가 다른 객체를 참조하고 있는 상황에서는, 다시 new 클래스명(); 으로 메모리에 배치해서 사용해야한다. 
// 이런 과정이 싫다면 객체마다 변수를 만들어 각각 참조해주면 된다
```